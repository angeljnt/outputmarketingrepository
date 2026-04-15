const { chromium, devices } = require('playwright');
const fs = require('fs/promises');
const path = require('path');

const base = 'https://outputmarketing.lovable.app';
const routes = [
  '/',
  '/about',
  '/pricing',
  '/contact',
  '/work',
  '/work/archive-radar-launch',
  '/work/archive-ai-newsletter',
  '/work/archive-linkedin-strategy',
  '/work/archive-product-marketing',
  '/services/founder-linkedin',
  '/services/content-marketing',
  '/services/organic-seo'
];

const outDir = process.argv[2];
if (!outDir) {
  console.error('Usage: node extract_site.cjs <outDir>');
  process.exit(1);
}

function sanitize(route) {
  if (route === '/') return 'home';
  return route.replace(/^\//, '').replace(/\//g, '__');
}

async function extractForContext(browser, contextName, contextOptions) {
  const context = await browser.newContext(contextOptions);
  const results = [];

  for (const route of routes) {
    const page = await context.newPage();
    const url = `${base}${route}`;
    const key = sanitize(route);
    const shotPath = path.join(outDir, `${contextName}-${key}.png`);

    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
      await page.waitForTimeout(1200);

      const data = await page.evaluate(() => {
        const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();

        const title = document.title;
        const metaDescription = document.querySelector('meta[name="description"]')?.getAttribute('content') || '';
        const h1 = Array.from(document.querySelectorAll('h1')).map((e) => clean(e.textContent)).filter(Boolean);
        const h2 = Array.from(document.querySelectorAll('h2')).map((e) => clean(e.textContent)).filter(Boolean);

        const links = Array.from(document.querySelectorAll('a'))
          .map((a) => ({ text: clean(a.textContent), href: a.getAttribute('href') || '' }))
          .filter((x) => x.text || x.href);

        const buttons = Array.from(document.querySelectorAll('button'))
          .map((b) => clean(b.textContent))
          .filter(Boolean);

        const forms = Array.from(document.querySelectorAll('form')).map((f) => {
          const fields = Array.from(f.querySelectorAll('input, select, textarea')).map((el) => ({
            tag: el.tagName.toLowerCase(),
            type: el.getAttribute('type') || '',
            name: el.getAttribute('name') || '',
            placeholder: el.getAttribute('placeholder') || '',
            required: el.hasAttribute('required')
          }));
          return { fieldCount: fields.length, fields };
        });

        const visibleText = clean(document.body?.innerText || '');

        const hasFaq = /questions you probably have|faq|frequently asked/i.test(visibleText);
        const hasPricing = /\$\d|pricing|month|pilot/i.test(visibleText);

        return {
          title,
          metaDescription,
          h1,
          h2,
          links,
          buttons,
          forms,
          textSample: visibleText.slice(0, 4000),
          textLength: visibleText.length,
          hasFaq,
          hasPricing,
        };
      });

      await page.screenshot({ path: shotPath, fullPage: true });

      results.push({
        route,
        url,
        context: contextName,
        screenshot: shotPath,
        ...data,
      });
      console.log(`[ok] ${contextName} ${route}`);
    } catch (err) {
      results.push({ route, url, context: contextName, error: String(err) });
      console.log(`[err] ${contextName} ${route} :: ${String(err)}`);
    } finally {
      await page.close();
    }
  }

  await context.close();
  return results;
}

(async () => {
  await fs.mkdir(outDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });

  const desktop = await extractForContext(browser, 'desktop', { viewport: { width: 1440, height: 900 } });
  const mobile = await extractForContext(browser, 'mobile', {
    ...devices['iPhone 13'],
  });

  await browser.close();

  const all = [...desktop, ...mobile];
  const jsonPath = path.join(outDir, 'site_extract.json');
  await fs.writeFile(jsonPath, JSON.stringify(all, null, 2), 'utf-8');

  const md = [];
  md.push('# Rendered Site Snapshot');
  md.push(`Source: ${base}`);
  md.push('');
  for (const item of all) {
    md.push(`## ${item.context.toUpperCase()} ${item.route}`);
    if (item.error) {
      md.push(`- ERROR: ${item.error}`);
      md.push('');
      continue;
    }
    md.push(`- URL: ${item.url}`);
    md.push(`- Title: ${item.title}`);
    md.push(`- Meta: ${item.metaDescription}`);
    md.push(`- H1: ${item.h1.join(' | ')}`);
    md.push(`- H2 count: ${(item.h2 || []).length}`);
    md.push(`- Buttons: ${(item.buttons || []).slice(0, 25).join(' | ')}`);
    const ctaLinks = (item.links || [])
      .filter((l) => /start|pilot|pricing|contact|book|call|work|case study|read/i.test(`${l.text} ${l.href}`))
      .slice(0, 30)
      .map((l) => `${l.text} -> ${l.href}`);
    md.push(`- CTA-like links: ${ctaLinks.join(' | ')}`);
    md.push(`- Forms: ${item.forms.length}`);
    md.push(`- Text length: ${item.textLength}`);
    md.push(`- Text sample: ${(item.textSample || '').slice(0, 1200)}`);
    md.push('');
  }

  const mdPath = path.join(outDir, 'site_snapshot_rendered.md');
  await fs.writeFile(mdPath, md.join('\n'), 'utf-8');

  console.log(`Wrote ${jsonPath}`);
  console.log(`Wrote ${mdPath}`);
})();
