# Output Marketing — Full CRO Overhaul
One complete pass. Implement every change below exactly as written. Everything not mentioned stays as is.

---

## PART 1 — HOMEPAGE ( / )

---

### 1.1 Hero headline — replace both lines

Find:
> Marketing that actually moves the needle.
> Built for B2B SaaS companies.

Replace with:
> Pipeline from content.
> Built for B2B SaaS founders and their teams.

---

### 1.2 Hero subheadline — replace

Find:
> Human-first. No AI slop. Marketing with ROI.

Replace with:
> Founder LinkedIn ghostwriting, content marketing, and SEO. No paid ads. No retainer.

---

### 1.3 Hero trust line — bold the key phrases

Find:
> No retainer commitment. No long contracts. $1,500 to $2,000 for 30 days.

Render as:
> **No retainer commitment. No long contracts.** **$1,500 to $2,000** for 30 days.

Wrap `No retainer commitment. No long contracts.` and `$1,500 to $2,000` in `<strong>` tags.

---

### 1.4 Hero — visually subordinate the secondary link

The link "See what the output looks like." must not compete with the primary CTA button. Change it to:
- No button styling, no border, no background
- Font size: `text-sm`
- Color: `text-muted-foreground` with `hover:text-foreground`
- Position: below the trust line, not beside the CTA button

---

### 1.5 Hero metric strip — bold the numbers

Find:
> Archive Radar launch: 2.45% engagement rate · 7 brands to waitlist
> B2B SaaS influencer campaign: 855,000 impressions · 3.40% engagement

Render as:
> Archive Radar launch: **2.45%** engagement rate · **7 brands** to waitlist
> B2B SaaS influencer campaign: **855,000 impressions** · **3.40%** engagement

---

### 1.6 Logo bar overline — update

Find:
> Brands we've built programs for

Replace with:
> B2B SaaS companies we've worked with

---

### 1.7 Problem section — dark section header

Find:
> Here's what's actually happening.

Replace with:
> The real problem isn't your product.

Dark section background stays. Only the header text changes.

---

### 1.8 Problem cards — bold the payoff phrase in each card headline

Card 1 — find:
> Budget spent. No pipeline.

Bold: `No pipeline.`

Card 2 — find:
> Better product. Less visibility.

Bold: `Less visibility.`

Card 3 — find:
> Their name. Not yours.

Bold the entire headline: `Their name. Not yours.`

---

### 1.9 Problem section — elevate the transition statement

Find:
> This is a solvable problem. Most agencies just aren't solving it.

Change this element:
- Text size: `text-h3`
- Font weight: `font-semibold`
- Color: `text-foreground` (remove `text-muted-foreground`)
- Alignment: `text-center` (keep — it is short enough at this size)

---

### 1.10 Services section — add the founder/company bridge sentence

Find the services section header:
> Three ways we work with you.

Immediately below that header (and above the service cards), add this new line:

> We build the founder's personal brand and the company's content machine. At Seed to Series A, you need both.

Style: `text-body-lg`, `text-muted-foreground`, `text-center`, `max-w-2xl mx-auto`, `mb-10`

---

### 1.11 Service cards — update Engine and Full Stack ICP lines

**Engine card** — find:
> For: Series A B2B SaaS companies that need leads from content, not just presence.

Replace with:
> For: Series A B2B SaaS founders and their teams that need leads from content, not just presence.

**Full Stack card** — find:
> For: Series A/B companies ready to treat content as a growth engine, not a line item.

Replace with:
> For: Series A/B founders and their teams ready to treat content as a growth engine, not a line item.

**Foundation card** — stays as is. Already says "Seed-stage B2B SaaS founders."

---

### 1.12 Services section bottom note — left-align

Find:
> Need a content audit, a technical SEO review, or pSEO for your product? We do those too.

If this line is currently `text-center`, change to `text-left`. Body sentences are never centered.

---

### 1.13 Damaging admission — section header

Find:
> Here's what we won't do.

Replace with:
> No paid ads. No video. No junior teams.

Same heading size. Only the text changes.

---

### 1.14 Damaging admission — bold the key lines

Find:
> What we do: founder LinkedIn ghostwriting, content strategy, SEO. We do it at a level most agencies can't match precisely because we're not spread thin.

Bold: `founder LinkedIn ghostwriting, content strategy, SEO`

Find:
> You talk directly to whoever is doing the work. Every time.

Bold the entire sentence: `You talk directly to whoever is doing the work. Every time.`

---

### 1.15 How we work — bold the pilot terms

Find:
> We start with 30 days. You see the quality of the work. We learn your product, your ICP, and your voice. $1,500 to $2,000, no strings attached.

Bold: `$1,500 to $2,000` and `no strings attached`

---

### 1.16 Credentials section — elevate "All from one client"

Find:
> All from one client. One year. Four different programs.

Change this element:
- Text size: `text-h2`
- Font weight: `font-semibold`
- Color: `text-foreground`
- Add a top border separator: `border-t border-border pt-8 mt-8`

This must read as a headline-level statement, not a caption or subtitle.

---

### 1.17 Add testimonial section — new section between credentials and the "Start with 30 days" CTA

Insert a new section between the credentials block and the dark CTA section. Light background (`bg-background`), full section padding.

**Overline** (using existing `overline` class, `text-center`):
> From the work

**Pull quote** (`text-h3`, `font-normal`, `italic`, `text-center`, `max-w-2xl mx-auto`, `mt-6`):
> "We went from a quiet LinkedIn presence to 7 brands on the Radar waitlist in the first campaign. The engagement came from the right people, not just volume."

**Attribution** (`text-caption`, `text-muted-foreground`, `text-center`, `mt-4`):
> — Archive team, Radar Feature Launch

**Separator** (`border-t border-border max-w-xs mx-auto mt-10`)

Note: Replace with a direct client quote when available. The structure and placement stay exactly as specified regardless of copy.

---

### 1.18 Dark CTA section — bold the guarantee

Inside the dark section containing "Start with 30 days.", find:
> No retainer. No contract. No commitment beyond the month.

Bold: `No retainer. No contract. No commitment beyond the month.` — the entire line.

---

### 1.19 FAQ section header — update

Find:
> Questions you probably have.

Replace with:
> Common questions.

---

### 1.20 FAQ — bold the key answers

**Q: "Who actually does the work?"** — find answer:
> Vanessa and Angel. Not a team of juniors supervised by someone you met once. You'll have both of our contact info from day one.

Bold: `Not a team of juniors supervised by someone you met once.` and `You'll have both of our contact info from day one.`

**Q: "What happens if the pilot doesn't work out?"** — find:
> We part ways. No pressure, no awkward conversation.

Bold: `No pressure, no awkward conversation.`

**Q: "Do you only work with SaaS companies?"** — find:
> Yes. B2B SaaS is the whole focus.

Bold: `B2B SaaS is the whole focus.`

**Q: "Do you work with early-stage startups?"** — find:
> That's exactly the stage where getting the marketing right compounds the most.

Bold: `getting the marketing right compounds the most`

---

## PART 2 — ABOUT PAGE ( /about )

---

### 2.1 Elevate "Not 50 people" as a standalone statement

Find:
> Not 50 people. Not a project manager between you and the work. Just us.

Change this element:
- Text size: `text-h2`
- Font weight: `font-semibold`
- Color: `text-foreground`
- Alignment: `text-center`
- Width: `max-w-2xl mx-auto`
- Spacing: `my-10` above and below

It must be visually dominant — the largest text in its area after the page headline.

---

### 2.2 Dark section header — update

Find:
> How we think about marketing.

Replace with:
> Why we stay narrow.

Dark section background stays. Only the text changes.

---

### 2.3 Dark section body — bold the key lines

Find:
> We do founder LinkedIn ghostwriting, content marketing, and SEO. We do those things at a level most agencies can't match because we're not also doing paid ads, video, PR, and event marketing at the same time.

Bold: `founder LinkedIn ghostwriting, content marketing, and SEO`

Find:
> You talk directly to whoever is doing the work. Every time. No account managers. No weekly updates from someone who wasn't in the meeting.

Bold: `You talk directly to whoever is doing the work. Every time.`

---

### 2.4 Vanessa bio — reorder to lead with the evidence

Find the full bio paragraph:
> Before Output Marketing, Vanessa was Influencer Marketing Manager at Fireflies.ai, where she ran a B2B SaaS influencer campaign for their Series A product push: 39 creators, 855,000 impressions, 3.40% engagement. Before that, Marketing Manager at Archive, a B2B SaaS platform for DTC brands.

Replace with:
> **39 creators. 855,000 impressions. 3.40% engagement.** That was the Fireflies.ai campaign Vanessa ran as Influencer Marketing Manager before starting Output Marketing. Before that, Marketing Manager at Archive — a B2B SaaS platform for DTC brands — where the four case studies on the Work page were built.

Apply `<strong>` to: `39 creators.` `855,000 impressions.` `3.40% engagement.`

---

### 2.5 Vanessa bio second paragraph — bold the awards

Find:
> The Webby Award and the Cannes Lions shortlist came from that work.

Bold: `Webby Award` and `Cannes Lions shortlist`

---

### 2.6 About page CTA header — update

Find:
> Seen enough? Start with 30 days.

Replace with:
> Ready to start? 30-day pilot, no retainer.

---

### 2.7 About page CTA trust line — bold

Find:
> No retainer. No contract. We reply within 24 hours.

Bold the entire line: `No retainer. No contract. We reply within 24 hours.`

---

## PART 3 — WORK PAGE ( /work )

---

### 3.1 Archive disclaimer — convert to prominent callout

Find:
> Note: These are all Archive's numbers. We're not going to show you a client we barely touched.

Remove this element and replace it with a bordered callout block positioned above the case study cards, with `my-10`:

**Callout block styles:**
- Background: `bg-surface`
- Border: `border border-neutral-200`
- Left accent: `border-l-4 border-l-foreground`
- Padding: `p-6`
- Max-width: `max-w-2xl mx-auto`

**Content inside the callout:**

Line 1 (`text-h3`, `font-semibold`, `text-foreground`, `mb-2`):
> These are all Archive's numbers.

Line 2 (`text-body`, `text-muted-foreground`):
> **Four campaigns. One client. One year.** Different problems, same commitment. We chose depth over breadth from day one. You'll get the same.

Apply bold to: `Four campaigns.` `One client.` `One year.`

---

### 3.2 Work page intro stats — bold the numbers

Find:
> Four campaigns. One client. One year. Different problems, same standard.

Bold: `Four campaigns.` `One client.` `One year.`

---

### 3.3 Case study preview cards — bold the metrics

In each preview card on the work page, bold every number in the metric line:
- `2.45%`, `7 brands` (Radar card)
- `7,363`, `114`, `1.21%` (LinkedIn card)
- Bold every metric number in the remaining two cards

---

## PART 4 — PRICING PAGE ( /pricing )

---

### 4.1 Remove the duplicate line

Find this line (appears shortly after the first version of the same phrase):
> See exactly what you'd get. Before you commit to anything.

Delete this line entirely. The line that precedes it — "See exactly what you'd get. Every engagement starts with a 30-day pilot. $1,500 to $2,000." — already covers both ideas and stays.

On the remaining line, bold: `$1,500 to $2,000`

---

### 4.2 Convert the second dark section to a light section

There are two dark (`bg-dark`) sections on this page. The second one contains:
> No long contracts. Start with 30 days.

Convert this section:
- Background: `bg-surface` (light)
- Text: `text-foreground` (stays dark)
- Add `border-t border-b border-border` to define the section visually
- The CTA button inside it: `bg-foreground text-background` (dark button on light background — keeps visual punch)

Do not change the first dark section ("The 30-Day Pilot"). That one stays dark.

---

### 4.3 Pricing page — bold the key guarantees in FAQ

**Q: "Is there a minimum commitment after the pilot?"** — find:
> No. The pilot is the commitment. After that, we move month-to-month. No annual contracts, no lock-ins.

Bold: `month-to-month` and `No annual contracts, no lock-ins.`

**Q: "Can I cancel anytime?"** — find:
> Yes. We ask for 30 days notice so we can wrap ongoing work cleanly. That's it.

Bold: `30 days notice`

**Q: "Do prices change after we start?"** — find:
> No. The rate you start at holds for as long as we work together. We don't sneak in price increases.

Bold: `The rate you start at holds for as long as we work together.`

---

### 4.4 Pricing FAQ header — update if showing old version

If the pricing page FAQ header reads "Questions you probably have.", change it to:
> Common questions.

---

## PART 5 — CONTACT PAGE ( /contact )

---

### 5.1 Opening frame — fix the subject ambiguity

Find:
> B2B SaaS company. Marketing that ships results. We reply within 24 hours.

Replace with:
> You're a B2B SaaS company. Marketing that ships results. **We reply within 24 hours.**

Apply bold to `We reply within 24 hours.`

---

### 5.2 Form subheadline — same fix

Find:
> B2B SaaS company. Marketing that ships results. You're in the right place.

Replace with:
> You're a B2B SaaS company. Marketing that ships results. You're in the right place.

---

### 5.3 "Or reach us directly" — fix the framing

Find:
> Or reach us directly:

Replace with:
> Prefer direct email:

---

### 5.4 Contact form trust line — bold

Find:
> We reply within 24 hours. No pitch, no pressure.

Bold: `We reply within 24 hours.` and `No pitch, no pressure.`

---

## PART 6 — /services/founder-linkedin

---

### 6.1 Hero trust line — bold

Find:
> No retainer. No long contract. $1,500 to $2,000 for 30 days.

Bold: `No retainer. No long contract.` and `$1,500 to $2,000`

---

### 6.2 Problem section — bold the key stat

Find:
> LinkedIn's own data says personal profiles get 8 times more engagement than company pages.

Bold: `8 times more engagement`

Find:
> The gap between what most companies do and what works is where we operate.

Bold: `what most companies do and what works`

---

### 6.3 "90% of SaaS companies" header — bold the number

Find the dark section header:
> 90% of SaaS companies post only from their company page.

Bold: `90%`

---

### 6.4 Evidence stat blocks — verify display size

The three stat blocks (8x, 1/3, 277%) must display numbers at `text-display` size (minimum 56px on desktop, 36px on mobile). If any are smaller, increase to `text-display`. Labels stay at `text-caption`.

---

### 6.5 Credentials — bold the metrics

Find:
> 39 creators, 855,958 impressions, 3.40% engagement.

Bold: `39 creators` `855,958 impressions` `3.40% engagement`

---

### 6.6 FAQ — bold key answer

Find:
> Yes. That's the whole job. If it doesn't sound like you, you don't post it. The first month is the calibration period. Most clients say month two is when it clicks.

Bold: `The first month is the calibration period.` and `month two is when it clicks`

---

## PART 7 — /services/content-marketing

---

### 7.1 Hero trust line — bold

Find:
> No retainer. No long contract. $1,500 to $2,000 for 30 days.

Bold: `No retainer. No long contract.` and `$1,500 to $2,000`

---

### 7.2 Evidence stat blocks — verify display size

Verify all stat block numbers (748%, 3x, etc.) display at `text-display` size on desktop.

---

## PART 8 — /services/organic-seo

---

### 8.1 Hero trust line — bold

Find:
> No retainer. No long contract. $1,500 to $2,000 for 30 days.

Bold: `No retainer. No long contract.` and `$1,500 to $2,000`

---

### 8.2 Problem section — bold the diagnosis

Find:
> Traffic goes up. Demo requests don't.

Bold: `Demo requests don't.`

Find:
> Bottom-of-funnel content, the posts buyers find when they're actively evaluating options, converts 10 to 25 times more.

Bold: `converts 10 to 25 times more`

Find:
> That's what we focus on.

Bold the entire line.

---

### 8.3 Evidence stat blocks — verify display size and bold label

Numbers (702%, 7 months, $290) must display at `text-display` size.

In the $290 stat label:
> Long-term organic CAC as content compounds vs $802 for paid search

Bold: `$290` (the stat number) and `$802`

---

## PART 9 — CASE STUDY PAGES

---

### 9.1 All four case study pages — metric blocks at display size

On each of the four case study pages (/work/archive-radar-launch, /work/archive-ai-newsletter, /work/archive-linkedin-strategy, /work/archive-product-marketing):

The large metric numbers in the stat grid must display at `text-display` size (minimum 56px on desktop, 36px on mobile). If they are currently at `text-h2` or smaller, increase to `text-display`. Labels stay at `text-caption`.

---

### 9.2 Radar Launch — bold the key analysis line

Find:
> The 2.45% engagement rate on a product launch post is strong. The industry average for B2B LinkedIn content sits around 0.5 to 1%.

Bold: `2.45%` and `0.5 to 1%`

---

### 9.3 Product Marketing — bold the key insight

Find:
> The most valuable output wasn't the content. It was the dashboard.

Bold the entire sentence.

---

### 9.4 LinkedIn Strategy — bold the standard

Find:
> Archive needed content that generated engagement from the right people: real positions, backed with data, in a voice that sounded like someone who knew the space.

Bold: `real positions, backed with data`

---

## PART 10 — GLOBAL ALIGNMENT FIX

---

### 10.1 Left-align all body paragraphs currently centered

Any paragraph-length text element (`text-body`, `text-body-lg`, or a `<p>` tag) that currently has `text-center` applied and wraps to more than one line must be changed to `text-left`.

**Keep centered:**
- All section headers (H1, H2, display)
- All overlines
- Standalone one-line statements
- Stat block numbers and short labels
- Short pull quotes (2 lines max)
- CTA button groups and short trust lines (1 line)
- The new bridge sentence in Section 1.10 (short, max-width constrained — ok centered)

**Change to left:**
- The "Need a content audit..." line on the homepage (Services section)
- Any service card description text that is centered
- Any FAQ answer text that is centered
- Any bio paragraph text that is centered
- Any paragraph on services pages that wraps to 2+ lines and is centered

---

## PART 11 — UNIVERSAL BOLD (apply across all remaining pages and sections)

Every occurrence of these exact phrases, wherever they appear across the entire site, must be wrapped in `<strong>`:

| Phrase |
|--------|
| `No retainer. No contract.` |
| `No retainer. No long contracts.` |
| `No retainer commitment. No long contracts.` |
| `We reply within 24 hours.` |
| `No pitch, no pressure.` |
| `No annual contracts, no lock-ins.` |
| `30 days notice` |
| `month-to-month` |
| `$1,500 to $2,000` |
| `Webby Award` |
| `Cannes Lions shortlist` |

---

## PART 12 — WHAT DOES NOT CHANGE

- All page layouts and grid structures
- The full design system (colors, spacing, fonts, components)
- Navigation structure and footer (already updated in previous pass)
- All copy on case study pages not referenced above
- Service page structures not referenced above
- All image placements and alt text
- All links and routing

---

## PRIORITY ORDER

If implementing in passes, do it in this sequence:

1. Parts 1.1–1.3 — Hero copy (above the fold, highest traffic)
2. Part 1.10–1.11 — Service cards founder/company bridge (core positioning fix)
3. Part 11 — Universal bold (every page, highest skimmer impact)
4. Part 10 — Left-align body copy (removes friction across all pages)
5. Parts 2.1, 2.4 — About page "Not 50 people" + Vanessa bio reorder
6. Parts 3.1 — Work page Archive callout (closes skeptics)
7. Part 1.17 — Testimonial section (new social proof)
8. Everything else in Parts 1–9
