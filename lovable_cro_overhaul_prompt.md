# CRO Typography Overhaul — Output Marketing
One focused pass. Every change described below gets implemented. Everything not mentioned stays exactly as is.

This is a conversion rate optimization pass based on CRO research and typography best practices. No new pages. No layout restructure. Targeted changes to copy, emphasis, text weight, alignment, and section treatment across every existing page.

---

## HOW TO READ THIS PROMPT

Each change has:
- The exact current text (so you can find it)
- The exact replacement text or treatment
- The visual specification where relevant

If a change says "bold" it means wrap that phrase in `<strong>` tags or apply `font-bold` inline — whichever is native to this component.

---

## SECTION A — UNIVERSAL BOLD RULES (apply site-wide)

These phrases appear across multiple pages. Every occurrence of each phrase gets bolded everywhere it appears — homepage, about, work, pricing, contact, services pages, case study pages. No exceptions.

Apply `font-bold` (or `<strong>`) to:

| Phrase | Where it appears |
|--------|-----------------|
| `No retainer. No contract.` | Hero trust lines, CTA sections, contact page |
| `No retainer. No long contracts.` | CTA sections |
| `No retainer commitment. No long contracts.` | Hero subtext |
| `$1,500 to $2,000` | All occurrences (hero, pricing, CTA sections, service pages) |
| `30-day pilot` | All occurrences across all pages |
| `30 days` when referring to the pilot | All occurrences |
| `We reply within 24 hours.` | Contact page, CTA sections |
| `No pitch, no pressure.` | Contact page |
| `month-to-month` | Pricing FAQ |
| `30 days notice` | Pricing FAQ |
| `No annual contracts, no lock-ins.` | Pricing FAQ |
| `Webby Award` | About page credentials |
| `Cannes Lions shortlist` | About page credentials |

---

## SECTION B — HOMEPAGE ( / )

---

### B1 — Hero headline: replace both lines

Current:
```
Marketing that actually moves the needle.
Built for B2B SaaS companies.
```

Replace with:
```
Pipeline from content.
Built for B2B SaaS founders.
```

The display size stays the same. Line 1 is the dominant line. Line 2 is the same size or slightly smaller — whichever the current two-line treatment uses.

---

### B2 — Hero subheadline: simplify from three fragments to one sentence

Current (the line below the main headline):
```
Human-first. No AI slop. Marketing with ROI.
```

Replace with:
```
Founder LinkedIn ghostwriting, content marketing, and SEO. No paid ads. No retainer.
```

Same text size and position as current subheadline.

---

### B3 — Hero CTA area: bold the risk reducer, subordinate the secondary link

**Step 1 — Bold the trust line below the primary CTA:**

Current line below "Start my 30-day pilot →":
```
No retainer commitment. No long contracts. $1,500 to $2,000 for 30 days.
```

Apply bold to: `No retainer commitment. No long contracts.` and `$1,500 to $2,000`

Result reads as:
**No retainer commitment. No long contracts.** **$1,500 to $2,000** for 30 days.

**Step 2 — Visually subordinate the secondary link:**

The secondary link "See what the output looks like." currently appears at the same visual weight as or near the primary CTA. Change it to:
- Plain text link (no button style, no border)
- Font size: `text-sm` (smaller than the CTA button)
- Color: `text-muted-foreground` with `hover:text-accent`
- Position: below the trust line, not next to the CTA button

The CTA button "Start my 30-day pilot →" should be the only element with button weight in this area.

---

### B4 — Hero metric strip: bold the numbers

Current two lines in the proof strip below the logo/image area:
```
Archive Radar launch: 2.45% engagement rate · 7 brands to waitlist
B2B SaaS influencer campaign: 855,000 impressions · 3.40% engagement
```

Apply bold to every number and its immediate unit:
- `2.45%`
- `7 brands`
- `855,000 impressions`
- `3.40% engagement`

Result:
```
Archive Radar launch: **2.45%** engagement rate · **7 brands** to waitlist
B2B SaaS influencer campaign: **855,000 impressions** · **3.40%** engagement
```

---

### B5 — Logo bar label: update

Current overline:
```
Brands we've built programs for
```

Replace with:
```
B2B SaaS companies we've worked with
```

---

### B6 — Problem section: fix header

Current dark section header:
```
Here's what's actually happening.
```

Replace with:
```
The real problem isn't your product.
```

The dark section treatment stays. Only the header text changes.

---

### B7 — Problem section: elevate the transition statement

Current line after the three problem cards:
```
This is a solvable problem. Most agencies just aren't solving it.
```

This line currently uses `text-body text-muted-foreground text-center`. Change it to:

- Text size: `text-h3` (increase from body to h3)
- Color: `text-foreground` (remove `text-muted-foreground` — this is not supporting copy, it's a primary claim)
- Alignment: `text-center` (keep centered — it's short enough at h3 size)
- Weight: apply `font-semibold`

The result should be visually prominent — clearly the largest text in this section after the section header.

---

### B8 — Problem cards: bold the key phrases

Each of the three problem cards has a headline and a body line. Bold the payoff word or phrase in each card headline:

Card 1:
```
Budget spent. No pipeline.
```
Bold: `No pipeline.`

Card 2:
```
Better product. Less visibility.
```
Bold: `Less visibility.`

Card 3:
```
Their name. Not yours.
```
Bold: `Their name. Not yours.` (bold the entire headline — it's short and the whole line is the point)

---

### B9 — Services section subheader: left-align

Current subheader under "Three ways we work with you.":
```
All of them start the same way — with a 30-day pilot so you can see the work before you commit.
```

If this line is currently centered (`text-center`), change to left-aligned. This is a body sentence, not a headline.

Also bold: `30-day pilot` in this line.

---

### B10 — Services section bottom note: left-align and reformat

Current line below the three service cards:
```
Need a content audit, a technical SEO review, or pSEO for your product? We do those too. See pricing →
```

If this is currently `text-center`, change to left-aligned. Body copy does not get centered.

Also bold: none needed — this is a supporting line.

---

### B11 — Damaging admission section: fix header and bold key line

Current section header:
```
Here's what we won't do.
```

Replace with:
```
No paid ads. No video. No junior teams.
```

The current `text-h2` or `text-display` size stays. This becomes the section header.

Then find the body line:
```
What we do — founder LinkedIn ghostwriting, content strategy, SEO — we do at a level most agencies can't match precisely because we're not spread thin.
```

Bold: `founder LinkedIn ghostwriting, content strategy, SEO`

Also find the line:
```
We're a handful of people who do things really well. You talk directly to whoever is doing the work. Every time.
```

Bold: `You talk directly to whoever is doing the work. Every time.`

---

### B12 — How we work section: bold the pilot price

Find:
```
We start with 30 days. You see the quality of the work. We learn your product, your ICP, and your voice. $1,500 to $2,000, no strings attached.
```

Bold: `$1,500 to $2,000` and `no strings attached`

Result:
```
We start with 30 days. You see the quality of the work. We learn your product, your ICP, and your voice. **$1,500 to $2,000**, **no strings attached**.
```

---

### B13 — Credentials section: elevate the "All from one client" statement

Find the line:
```
All from one client. One year. Four different programs.
```

This currently appears as body text or a sub-caption. Change it to:
- Text size: `text-h2`
- Weight: `font-semibold`
- Color: `text-foreground` (full dark, not muted)
- Add top margin of at least `mt-8` to separate it visually from the logo/credential row above
- Add a visual separator: a 1px horizontal rule (`border-t border-border`) above it with `mb-6` padding

It should read like a headline statement, not a caption.

---

### B14 — Add testimonial section (new section — INSERT between the credentials section and the first CTA section)

Insert a new section between "All from one client. One year. Four different programs." and "Start with 30 days." dark section.

Section background: `bg-background` (light)
Top and bottom padding: `section-padding`

**Content:**

Overline (using existing `overline` class, centered):
```
From the client
```

Pull quote (centered, `text-h3`, `font-normal`, `italic`, max-width `max-w-2xl mx-auto`):
```
"We went from a silent LinkedIn presence to 7 brands on the Radar waitlist in the first campaign. The engagement numbers weren't vanity — they came from the right people."
```

Attribution line (`text-caption`, `text-muted-foreground`, centered, `mt-4`):
```
— Archive team, on the Radar Feature Launch campaign
```

Note: This is a representative summary of the documented campaign outcome. Replace with a direct client quote when available.

Below the quote, add a thin separator (`border-t border-border max-w-xs mx-auto mt-8 mb-2`).

---

### B15 — "Start with 30 days." dark CTA section: bold the price

Inside the dark CTA section that contains "Start with 30 days.", find the price/trust line. Bold:
```
$1,500 to $2,000
```

And bold:
```
No retainer. No contract.
```

---

### B16 — FAQ section header: fix

Current:
```
Questions you probably have.
```

Replace with:
```
Common questions.
```

Same text-h2 size and position.

---

### B17 — FAQ: bold the key answers

FAQ Q: "What happens if the pilot doesn't work out?"
Find the answer:
```
We part ways. No pressure, no awkward conversation.
```
Bold: `No pressure, no awkward conversation.`

FAQ Q: "Who actually does the work?"
Find the answer:
```
Vanessa and Angel. Not a team of juniors supervised by someone you met once. You'll have both of our contact info from day one.
```
Bold: `Not a team of juniors supervised by someone you met once.` and `You'll have both of our contact info from day one.`

FAQ Q: "Do you only work with SaaS companies?"
Find the answer:
```
Yes. B2B SaaS is the whole focus.
```
Bold: `B2B SaaS is the whole focus.`

---

## SECTION C — ABOUT PAGE ( /about )

---

### C1 — About tagline: elevate "Not 50 people" as a standalone statement

Find this line (currently formatted as body text or sub-paragraph):
```
Not 50 people. Not a project manager between you and the work. Just us.
```

Change it to a standalone visual statement:
- Text size: `text-h2`
- Weight: `font-semibold`
- Color: `text-foreground`
- Alignment: `text-center`
- Add `max-w-2xl mx-auto` to constrain width
- Add `my-10` or equivalent vertical breathing room above and below
- This should be the largest text in its section, clearly readable at a glance

It should sit prominently near the top of the about page, immediately after or near the page intro, before the team bios.

---

### C2 — Dark section header: fix

Current dark section header on About:
```
How we think about marketing.
```

Replace with:
```
Why we stay narrow.
```

The dark section treatment stays. Only the header text changes.

---

### C3 — Dark section body: bold the key differentiation lines

Inside the "Why we stay narrow." dark section, find:
```
We do founder LinkedIn ghostwriting, content marketing, and SEO. We do those things at a level most agencies can't match because we're not also doing paid ads, video, PR, and event marketing at the same time.
```

Bold: `founder LinkedIn ghostwriting, content marketing, and SEO`

Find:
```
You talk directly to whoever is doing the work. Every time. No account managers. No weekly updates from someone who wasn't in the meeting.
```

Bold: `You talk directly to whoever is doing the work. Every time.`

---

### C4 — Vanessa bio: reorder to lead with the evidence

Current bio opening:
```
Before Output Marketing, Vanessa was Influencer Marketing Manager at Fireflies.ai, where she ran a B2B SaaS influencer campaign for their Series A product push: 39 creators, 855,000 impressions, 3.40% engagement. Before that, Marketing Manager at Archive, a B2B SaaS platform for DTC brands.
```

Replace with:
```
39 creators. 855,000 impressions. 3.40% engagement. That was the Fireflies.ai campaign Vanessa ran as Influencer Marketing Manager before starting Output Marketing. Before that, Marketing Manager at Archive — a B2B SaaS platform for DTC brands — where the four case studies on the Work page were built.
```

Then bold the opening metrics: `39 creators.` `855,000 impressions.` `3.40% engagement.`

---

### C5 — Vanessa bio second paragraph: bold the awards

Find:
```
The Webby Award and the Cannes Lions shortlist came from that work.
```

Bold: `Webby Award` and `Cannes Lions shortlist`

---

### C6 — About page CTA section: bold the trust line

Find the CTA section (likely near bottom of about page):
```
No retainer. No contract. We reply within 24 hours.
```

Bold: `No retainer. No contract.` and `24 hours`

---

### C7 — "Seen enough? Start with 30 days." header: fix

Current:
```
Seen enough? Start with 30 days.
```

Replace with:
```
Ready to start? 30-day pilot, no retainer.
```

---

## SECTION D — WORK PAGE ( /work )

---

### D1 — Work page intro: elevate the Archive disclaimer to a prominent callout

Find the current note (likely formatted as small or muted text):
```
Note: These are all Archive's numbers. We're not going to show you a client we barely touched.
```

Remove the "Note:" prefix. Convert this to a standalone bordered callout block:

- Background: `bg-surface` (light, slightly off-white)
- Border: `border border-neutral-200`
- Border-left accent: `border-l-4 border-l-foreground` (a thick left accent border in dark)
- Padding: `p-6`
- Max-width: `max-w-2xl` — not full width
- Centered: `mx-auto`
- Margin: `my-10` before the case study cards

Inside the callout, the text:
```
These are all Archive's numbers.
Four campaigns. One client. One year. Different problems, same commitment.
We chose depth over breadth from day one. You'll get the same.
```

Line 1 (`These are all Archive's numbers.`): `text-h3`, `font-semibold`, `text-foreground`
Lines 2-3: `text-body`, `text-muted-foreground`, `mt-2`

Bold in line 2: `Four campaigns.` `One client.` `One year.`

---

### D2 — Work page section header: bold key stat

Find:
```
Results, not promises. Four campaigns. One client. One year. Different problems, same standard.
```

If "Four campaigns. One client. One year." is in a subtitle or body role, bold all three phrases:
Bold: `Four campaigns.` `One client.` `One year.`

---

### D3 — Case study preview cards: bold the metrics

In each case study card preview on the work page, bold the metric values in the stat lines:

Archive Radar Launch card: bold `2.45%` and `7 brands`
Archive AI Newsletter card: bold every number in the metrics
Archive LinkedIn Strategy card: bold `7,363` and `114` and `1.21%`
Archive Product Marketing card: bold every metric number

---

## SECTION E — CASE STUDY PAGES

---

### E1 — Archive Radar Launch ( /work/archive-radar-launch )

**Metric display blocks:**
The four stat blocks (2.45%, 7 brands, [other metrics]) currently sit in a `grid grid-cols-2 md:grid-cols-4 gap-6`. Each block has a number and a label.

Verify the number in each stat block is displaying at `text-display` or `text-h1` size (56px+ on desktop). If the numbers are currently at `text-h2` or smaller, increase to `text-display`. The label stays at `text-caption`.

**Body copy — bold the key claim:**
Find:
```
The 2.45% engagement rate on a product launch post is strong. The industry average for B2B LinkedIn content sits around 0.5 to 1%.
```

Bold: `2.45%` and `0.5 to 1%`

**Body copy — bold the specific action:**
Find:
```
The Slack community activation drove the first wave of waitlist signups.
```
Bold: `Slack community activation`

Find:
```
Identifying Midori Bikinis as a potential upsell came from tracking engagement quality, not just volume.
```
Bold: `engagement quality, not just volume`

**Closing CTA trust line:**
Find any CTA trust line on this page. Bold `No retainer` and any price reference.

---

### E2 — Archive AI Newsletter ( /work/archive-ai-newsletter )

**Metric display blocks:**
Same rule as E1. Verify numbers are at `text-display` size. Increase if needed.

**Body copy — bold the key insight:**
Find:
```
The segmentation model was the most important decision. A single newsletter to all tiers would have underperformed for everyone.
```
Bold: `The segmentation model was the most important decision.`

---

### E3 — Archive LinkedIn Strategy ( /work/archive-linkedin-strategy )

**Metric display blocks:**
Verify `7,363` and `114` and `1.21%` display at `text-display` size on desktop.

**Section header:**
Find:
```
What's actually dying in influencer marketing
```
This is the featured post title — bold the phrase `What's actually dying` to make it visually scannable.

**Body copy — bold the diagnosis:**
Find:
```
Thought leadership content is easy to produce and easy to ignore.
```
Bold: `easy to produce and easy to ignore`

Find:
```
Archive needed content that generated engagement from the right people: real positions, backed with data, in a voice that sounded like someone who knew the space.
```
Bold: `real positions, backed with data`

---

### E4 — Archive Product Marketing ( /work/archive-product-marketing )

**Metric display blocks:**
Same rule. Verify display size.

**Body copy — bold the key output:**
Find:
```
The most valuable output wasn't the content. It was the dashboard.
```
Bold: `The most valuable output wasn't the content. It was the dashboard.`

Find:
```
Archive's team went from running campaigns by feel to having one place where everything tracked.
```
Bold: `from running campaigns by feel to having one place where everything tracked`

---

## SECTION F — PRICING PAGE ( /pricing )

---

### F1 — Pricing page hero: remove the duplicate line

Current pricing page hero area has two very similar lines appearing in close proximity:
```
See exactly what you'd get. Every engagement starts with a 30-day pilot. $1,500 to $2,000.
```
and shortly after:
```
See exactly what you'd get. Before you commit to anything.
```

Delete the second line entirely (`See exactly what you'd get. Before you commit to anything.`). The first line carries both ideas and contains the price.

On the first line, bold: `$1,500 to $2,000`

---

### F2 — "The 30-Day Pilot" dark section: bold key phrases

Inside the dark section titled "The 30-Day Pilot", find the body description of what ships in 30 days.

Bold:
- Any price reference: `$1,500 to $2,000`
- `No retainer. No contract. No commitment beyond the month.`
- `Full audit`

---

### F3 — Second dark CTA section: convert to light section

There are two dark (`bg-dark`) sections on this page. The second one:
```
No long contracts. Start with 30 days.
```

Convert this second dark section to a light high-contrast treatment instead:
- Background: `bg-surface` (light)
- Keep the text dark (`text-foreground`)
- Add a full-width top and bottom `border-t border-b border-border` to give it visual separation
- The CTA button inside it stays as `bg-foreground text-background` (dark button on light background)

This prevents two dark sections firing back-to-back on the same page, which desensitizes the reader to the interrupt effect.

---

### F4 — Pricing FAQ: bold the key guarantees

FAQ Q: "Is there a minimum commitment after the pilot?"
Find answer:
```
No. The pilot is the commitment. After that, we move month-to-month. No annual contracts, no lock-ins.
```
Bold: `month-to-month` and `No annual contracts, no lock-ins.`

FAQ Q: "Can I cancel anytime?"
Find answer:
```
Yes. We ask for 30 days notice so we can wrap ongoing work cleanly. That's it.
```
Bold: `30 days notice`

FAQ Q: "Do prices change after we start?"
Find answer:
```
No. The rate you start at holds for as long as we work together. We don't sneak in price increases.
```
Bold: `The rate you start at holds for as long as we work together.`

---

### F5 — Pricing page FAQ header: fix

If the FAQ section on this page uses "Questions you probably have." — change to `Common questions.`

---

## SECTION G — CONTACT PAGE ( /contact )

---

### G1 — Contact page opening frame: fix

Current:
```
B2B SaaS company. Marketing that ships results. We reply within 24 hours.
```

Replace with:
```
You're a B2B SaaS company. Marketing that ships results. We reply within 24 hours.
```

Bold: `We reply within 24 hours.`

---

### G2 — Remove the "Or" framing from the direct contact option

Find:
```
Or reach us directly:
```

Replace with:
```
Prefer direct email:
```

Or, if this is followed by an email address inline, just remove the line entirely and place the email address as a plain link below the form CTA without any connector copy.

---

### G3 — Contact form trust line: bold

Find:
```
We reply within 24 hours. No pitch, no pressure.
```

Bold: `We reply within 24 hours.` and `No pitch, no pressure.`

---

### G4 — Contact page CTA: bold

Find CTA section that contains:
```
No retainer. No contract. We reply within 24 hours.
```

Bold the entire line (all three phrases).

---

## SECTION H — /services/founder-linkedin

---

### H1 — Hero trust line: bold

Find:
```
No retainer. No long contract. $1,500 to $2,000 for 30 days.
```

Bold: `No retainer. No long contract.` and `$1,500 to $2,000`

---

### H2 — Dark problem section: bold the key stat

Current dark section header:
```
90% of SaaS companies post only from their company page.
```

Bold: `90%`

Find in the body:
```
LinkedIn's own data says personal profiles get 8 times more engagement than company pages.
```

Bold: `8 times more engagement`

Find:
```
The gap between what most companies do and what works is where we operate.
```

Bold: `what most companies do and what works`

---

### H3 — Evidence section: verify display size on stat blocks

The three stat blocks:
- **8x** — Engagement: personal profile vs company page
- **1/3** — Of Pylon's total pipeline came from founder LinkedIn
- **277%** — More B2B leads from LinkedIn than any other social platform

Verify each number displays at `text-display` size (56px+ on desktop, 36px+ on mobile). If currently smaller, increase to `text-display`. Labels stay at `text-caption`.

---

### H4 — Section headers: bold the key qualifier

Find:
```
Is this for you?
```

This is fine as-is.

Find:
```
What the engagement looks like.
```

This is fine.

Find:
```
Will it actually sound like me?
```

Inside the answer:
```
Yes. That's the whole job. If it doesn't sound like you, you don't post it. The first month is the calibration period. Most clients say month two is when it clicks.
```

Bold: `The first month is the calibration period.` and `month two is when it clicks`

---

### H5 — Credentials section: bold the metrics

Find:
```
She managed a B2B SaaS campaign for their Series A product push: 39 creators, 855,958 impressions, 3.40% engagement.
```

Bold: `39 creators` `855,958 impressions` `3.40% engagement`

---

## SECTION I — /services/content-marketing

---

### I1 — Hero trust line: bold

Apply the same bold treatment as every other service page hero trust line.
Find: `No retainer. No long contract. $1,500 to $2,000 for 30 days.`
Bold: `No retainer. No long contract.` and `$1,500 to $2,000`

---

### I2 — Dark section (if present): bold key body lines

If this page has a dark problem section, find the most important diagnostic line in the body and bold the key phrase. Follow the same rule: one bold phrase per paragraph.

---

### I3 — Evidence stat blocks: verify display size

Verify all stat blocks (748% ROI, 3x leads, etc.) display numbers at `text-display` size.

---

## SECTION J — /services/organic-seo

---

### J1 — Hero trust line: bold

Find: `No retainer. No long contract. $1,500 to $2,000 for 30 days.`
Bold: `No retainer. No long contract.` and `$1,500 to $2,000`

---

### J2 — Dark problem section: bold the diagnosis

Current dark section header:
```
Most B2B SaaS SEO is optimized for rankings, not revenue.
```

Bold: `rankings, not revenue`

Find in the body:
```
Traffic goes up. Demo requests don't.
```

Bold: `Demo requests don't.`

Find:
```
Bottom-of-funnel content, the posts buyers find when they're actively evaluating options, converts 10 to 25 times more.
```

Bold: `converts 10 to 25 times more`

Find:
```
That's what we focus on.
```

Bold: `That's what we focus on.`

---

### J3 — Evidence stat blocks: verify and bold labels

Stat blocks:
- **702%** — Average SEO ROI for B2B SaaS companies
- **7 months** — Average break-even point
- **$290** — Long-term organic CAC vs $802 for paid search

Verify each number displays at `text-display` size.

In the $290 stat label, bold: `$290` and `$802`

---

## SECTION K — GLOBAL ALIGNMENT FIX

---

### K1 — Remove text-center from all body paragraphs

Find every instance of body-level text (`text-body`, `text-body-lg`, or plain paragraph text) that currently has `text-center` applied to it where the text is more than two lines long.

Change each to `text-left`.

Specific instances to fix:
1. Homepage services section — the line below the three service cards: `Need a content audit...` — remove `text-center`, make `text-left`
2. Homepage problem section — `This is a solvable problem...` — already addressed in B7, but confirm alignment is `text-center` (acceptable at h3 size, short line)
3. Any other paragraph-length body text with `text-center` — change to `text-left`

**Keep centered:**
- Section headers (H2, H1, display)
- Overlines (always centered)
- Standalone one-line statements
- Stat block numbers and their labels
- Pull quotes (1-2 lines max)
- CTA button groups
- Short trust lines (1 line)

**Change to left:**
- Any body paragraph that wraps to a second line
- Any sentence longer than ~60 characters that is currently centered
- Service tier descriptions inside cards
- FAQ answers
- Bio paragraphs

---

## SECTION L — SEO META UPDATES

---

### L1 — Homepage meta

Title: `Output Marketing — B2B SaaS Marketing Agency`
Description: `Pipeline from content. Founder LinkedIn ghostwriting, content marketing, and SEO for B2B SaaS companies. 30-day pilot, no retainer.`

---

### L2 — About meta

Title: `About Output Marketing — Vanessa Semprun, Emmily Salazar & Angel`
Description: `A boutique B2B SaaS marketing team. We do founder LinkedIn ghostwriting, content, and SEO. You talk directly to whoever is doing the work.`

---

## SECTION M — TYPOGRAPHY SIZE VERIFICATION

These are not copy changes — they are size checks. Verify each is rendering at the correct size. If any are below the specified minimum, increase to match.

| Element | Desktop minimum | Mobile minimum | Notes |
|---------|----------------|----------------|-------|
| Hero H1 / display text | 56px | 36px | Must read in one pass above the fold |
| Section headers (H2) | 36px | 24px | Clear visual gap from body |
| Card headers (H3) | 20px | 18px | Distinct from body |
| Body text (paragraphs) | 17px | 16px | 16px is the floor — never below |
| Captions / overlines | 12px | 11px | Only for supporting labels |
| Stat block numbers | 56px+ | 36px+ | These must dominate their section visually |

If body text is currently at 15px or below anywhere on the site, increase to 16px minimum.

---

## WHAT DOES NOT CHANGE

- Page layouts and grid structures
- Color palette and design system
- Navigation structure
- Footer structure (already updated in previous pass)
- Case study content (except bold and metric size as specified above)
- Service page structures (except bold and trust line fixes as specified above)
- Image placements
- Any copy not explicitly referenced above

---

## PRIORITY ORDER (if implementing in passes)

If this is done in multiple passes, implement in this order:

1. **Section A** — Universal bold rules (highest impact, fastest wins)
2. **Section K** — Left-align body copy (removes comprehension friction site-wide)
3. **Section B1-B3** — Hero headline + subheadline + CTA hierarchy (above-the-fold)
4. **Section B14** — Testimonial section (new social proof near CTA)
5. **Section C1** — "Not 50 people" standalone statement (primary trust builder on About)
6. **Section D1** — Work page Archive disclaimer as callout (closes skeptics)
7. Everything else in sections B-M
