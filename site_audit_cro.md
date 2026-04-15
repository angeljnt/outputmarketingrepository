# Output Marketing — CRO Audit
Based on: sota_report_cro.md + sota_findings_cro.md
Constraint: No testimonials. Only work with available assets.
Date: 2026-03-23

---

## Audit Method

Each finding is:
- **Source**: the research backing it
- **Gap**: what's missing or suboptimal in the current wireframe
- **Fix**: the specific change to make — with copy where applicable
- **Impact**: estimated conversion lever (High / Medium / Low)

---

## FINDING 01 — CTA copy is second-person throughout

**Source:** First-person CTA pronouns tested at up to 90% CTR boost (VWO, multiple A/B studies). Joanna Wiebe: "Think of CTAs as the value the person drives, not the action they take."

**Gap:** Every CTA in the wireframe reads "Start your 30-day pilot." Second-person. The research is clear that first-person performs better in almost every test.

**Fix:** Change to first-person across all 12 pages.

| Current | Change to |
|---------|-----------|
| Start your 30-day pilot → | Start my 30-day pilot → |
| Start your pilot → | Start my pilot → |
| Start with a pilot → | Start my pilot → |

**Note:** Keep the footer CTA in the current form as an option — "Ready to see what the output looks like?" sets up second-person naturally. That one is debatable. All inline CTAs: first-person.

**Impact:** High

---

## FINDING 02 — Micro-copy risk reducers are inconsistent across pages

**Source:** Micro-copy adjacent to CTAs is one of the most validated low-effort, high-return CRO fixes. Security/commitment language directly below the CTA button reduces friction at the point of hesitation. "We reply within 24 hours" is a documented friction reducer (Baymard, CXL).

**Gap:** The homepage hero and pilot offer blocks have risk reducers. The service pages have "No retainer. No long contract. $1,500–$2,000 for 30 days." as an inline trust line. But the /pricing pilot block CTA and the /about CTA are missing them. The /contact form is also missing a risk reducer near the submit button.

**Fix:** Add below every CTA button. Two lines max. Must be specific — not "We take privacy seriously."

Pages needing updates:

**Homepage CTA #2 (Pilot Offer section) — already has:**
> No retainer. No contract. No commitment beyond the month.
This is good. Keep.

**/pricing pilot block — add below the CTA:**
> No retainer. No contract. We reply within 24 hours.

**/about Section 07 CTA — add below the CTA:**
> No long contracts. Start with 30 days.

**/contact submit button — add directly below:**
> We reply within 24 hours. No pitch, no pressure.

**Service pages (all three heroes) — already have:**
> No retainer. No long contract. $1,500–$2,000 for 30 days.
This is solid. Keep.

**Impact:** Medium-High

---

## FINDING 03 — Contact form has no inline validation specified and may have too many fields

**Source:** Baymard Institute: 81% form abandonment baseline. Inline validation (real-time field error feedback) reduces abandonment by 9–11%. Phone field without explanation: -5 to -8% completion. Single-column forms outperform multi-column.

**Gap:** The /contact wireframe specifies 4 fields: Name, Company, Email, open text area. No phone field — that's correct. But the wireframe doesn't specify inline validation behavior or that the form is single-column.

**Fix:**

Add to /contact wireframe:
- Single-column layout (explicit in design note)
- Inline validation: show green checkmark when field is valid, red + specific message when not (not just "Please fill this field")
- Error message for email: "Please enter a valid email (name@company.com)"
- The open-text field label should be: "What's the one thing you need fixed?" — more specific than "What are you trying to solve?" — lower perceived effort, conversational

The current 4-field structure is correct. Do not add phone. Do not add company size, budget range, or any other qualifying field at this stage. Pre-qualify with the copy, not the form.

**Impact:** Medium

---

## FINDING 04 — Vanessa's photo direction is unspecified relative to the CTA

**Source:** Eye tracking studies consistently show that directional cues — photos of people looking toward the CTA — measurably improve click-through. This is one of the cheapest CRO wins: it costs nothing, it's built into the photo choice.

**Gap:** The wireframe specifies that Vanessa should be in a "working" photo that is "warm but direct" and "not a headshot." Good framing. But it doesn't specify that her gaze or body direction should orient toward the CTA button.

**Fix:** Add to the design note for the hero photo (homepage and about page):

> Photo direction note: Vanessa's gaze or body angle should point subtly toward the CTA. If she's looking at the camera, the CTA should be on the same side as her natural gaze line. Do not place the CTA on the opposite side of where she's looking — that pulls attention away from conversion.

This applies to:
- Homepage Section 02 (HERO)
- /about Section 03 (VANESSA)

**Impact:** Low-Medium (cheap to get right, costly to ignore)

---

## FINDING 05 — The /about page has only one CTA and it's at the bottom

**Source:** Andy Crestodina (Orbit Media): the About page is the second-most visited page on agency sites and is often where trust converts. A single CTA at the bottom is a missed opportunity — visitors who are convinced by the Vanessa section don't need to scroll to the awards block to take action.

**Gap:** /about has 7 sections before the CTA. The Vanessa section (Section 03) is where most visitors will be most convinced. The current wireframe makes them scroll through the Angel section, the philosophy section, and the awards block before seeing a CTA.

**Fix:** Add a CTA directly after the Vanessa section (Section 03), before the Angel section:

**New Section 03b — MINI CTA (after Vanessa, before Angel):**

> Seen enough? Start with 30 days.
> [Start my 30-day pilot →]
> No retainer. No contract.

Design note: This should be lightweight — not a full dark-background section. A simple centered block, muted background, brief. It captures visitors who are ready after reading about Vanessa and don't need more convincing.

**Impact:** Medium

---

## FINDING 06 — The /work index page has no CTA above the fold

**Source:** HubSpot 40,000-page analysis: CTAs above the fold → +30% higher conversion. The /work index is a proof page, but visitors who arrive there from outreach or referral are often ready to engage — they just need the path to be visible.

**Gap:** The /work index page flows: Header → Case study cards → CTA block. The CTA block is at the bottom. A visitor who lands on /work from a cold email, a LinkedIn post, or a referral link has no CTA visible without scrolling.

**Fix:** Add a secondary CTA to the page header section (Section 02), below the subheadline and the "These are all Archive's numbers" note:

**Updated Section 02 — HEADER:**
> Results, not promises.
> Four campaigns. One client. One year. Different problems, same standard.
> (note: These are all Archive's numbers. We're not going to show you a client we barely touched.)

**Add below the note:**
> [Start my 30-day pilot →]
> No retainer. See what we'd do for you first.

Design note: Small, not a hero-level CTA. But visible without scrolling.

**Impact:** Medium

---

## FINDING 07 — Case study metrics don't appear on the homepage until Section 10

**Source:** Social proof (specific numbers) in the first fold or early scroll increases conversions significantly. The 2.45% engagement rate is a weapon. Currently, a visitor must scroll through 9 sections before seeing the first hard metric.

**Gap:** The Logo Bar (Section 03) shows brand names but no numbers. The Agitate section (Section 05) has pain cards but no proof. The Awards section (Section 06) has credentials but no output metrics. Sections 07, 08, 09 pass before the case study section.

**Fix:** Add one metric to the logo bar label or create a "proof bar" immediately below the logo bar.

**Updated Section 03 — LOGO BAR:**

Current label:
> Brands we've built programs for

Updated label + add one-line metric strip below logos:

> Brands we've built programs for
> [Archive logo] [Fireflies.ai logo] [ZENIQ logo]
>
> — — — — — — — — — — — — — — — —
> Archive Radar launch: 2.45% engagement rate · 7 brands to waitlist
> Airwallex Series G: 855,000 impressions · 3.40% engagement

Design note: The metric strip sits between the logo bar and the divider line. Small text, muted color. Not a full section — just a number that anchors the logos to real outcomes. This is the closest equivalent to a testimonial that the research validates when testimonials aren't available.

**Impact:** High

---

## FINDING 08 — The pricing page hero is passive

**Source:** Pricing page headlines that frame outcome convert better than those that just announce terms. "No retainer until you've seen the work" is honest and low-friction, but it's framed around what you *won't* ask for — not what the visitor *will* get.

**Gap:** The current headline is: "No retainer until you've seen the work." It's a good risk reducer but it leads with a negative (retainer/commitment) rather than a positive outcome.

**Fix:** Keep the current headline as the subheadline. Add a new headline above it:

**Updated /pricing HERO:**

**HEADLINE (new):**
> See exactly what you'd get. Before you commit to anything.

**SUBHEADLINE (current headline becomes subheadline):**
> Every engagement starts with a 30-day pilot. You see the quality. We learn your business. Then you decide.

This reframes the page: from "we won't trap you" to "you get to evaluate us first." Same promise, more positive framing, better outcome orientation.

**Impact:** Medium

---

## FINDING 09 — The /contact page subheadline is a conditional that adds friction

**Source:** Cognitive load research: every word a visitor has to parse before acting is friction. Conditional sentences ("If you're a B2B SaaS startup or DTC brand that...") require more processing than direct statements.

**Gap:** Current subheadline: "B2B SaaS startup or DTC brand that needs marketing that ships results. You're in the right place."

This is already improved from the original (em dash removed, conditional shortened). But the two-sentence structure still delays the directive.

**Fix:**
> B2B SaaS or DTC brand. Marketing that ships results. You're in the right place.

Three declarative fragments. Zero conditional processing required. Faster to read, faster to decide.

**Impact:** Low-Medium

---

## FINDING 10 — Service page "Who it's for" sections could add a self-selection line

**Source:** Self-qualification tools on B2B pages reduce bad-fit inquiries and increase qualified conversion. When visitors actively identify themselves in the copy, they're more likely to take action.

**Gap:** The "Who it's for" sections on all three service pages list characteristics of the ideal client in bullet form. They're accurate and useful. But there's no closing line that prompts the visitor to commit to the identification.

**Fix:** Add one line at the end of each "Who it's for" section, before the next section divider:

> Sound like you? That's who we built this for.

This is a micro-commitment: the visitor who nods "yes" to the bullets is now invited to confirm. The visitors who don't fit self-select out. Both outcomes are good.

**Impact:** Low-Medium

---

## FINDING 11 — Case study insight sections use "we" language where "you" language would convert better

**Source:** Joanna Wiebe: conversion copy should speak to what the visitor experiences or gains, not what the agency did. The insights sections in the case studies are currently written as "here's what we learned." Reframing them as "here's what this means for you" increases relevance and conversion intent.

**Gap:** Current insight language:
> "Identifying Midori Bikinis as a potential upsell came from tracking engagement quality, not just volume."

This is about what Vanessa did. It's interesting but not directly connected to the visitor's outcome.

**Fix:** Add one line at the end of each case study insights section that bridges the work to the visitor:

**Archive Radar — add after insights:**
> If your next product launch matters, this is the playbook.

**Archive Newsletter — add after insights:**
> If your customers go quiet between purchases, this is where to start.

**Archive LinkedIn — add after insights:**
> If your ICP is on LinkedIn and you're not showing up, this is what consistent looks like.

**Archive Product Marketing — add after insights:**
> If you're running multiple campaigns and losing track of what's working, this is what a dashboard changes.

These are not CTAs — they're bridges. They go before the CTA section.

**Impact:** Medium

---

## FINDING 12 — The FAQ on the homepage doesn't address one key B2B objection: "How do I know the quality is real?"

**Source:** Objection coverage research: track the % of top objections addressed inline. For a boutique agency with one client's case studies, the #1 unaddressed objection is: "All your work is from one client. Is that a risk?"

**Gap:** The homepage FAQ has 7 questions. None of them address why there's only one featured client and why that's not a weakness.

**Fix:** Add one FAQ question (Q8) to the homepage FAQ:

**Q8: All your case studies are from Archive. Should I be concerned?**
> No. We chose to go deep with one client rather than shallow with ten. Four different campaigns, different channels, different goals — all from the same relationship. That's what it looks like when an agency actually commits to a client's growth. You'll get the same.

**Impact:** Medium-High (pre-empts the most obvious skepticism from a sharp B2B buyer)

---

## FINDING 13 — The /pricing comparison table uses "none" for empty cells

**Source:** Minor UX detail with a real impact: table cells that say "none" require the visitor to read and process a negative. A dash or blank cell communicates the same thing with zero cognitive load.

**Gap:** The comparison table was updated to use "none" (replacing the original em dash) during the anti-ai-prose edit. But a dash in a table is not an em dash — it's a standard visual convention meaning "not included." The text "none" adds unnecessary reading load.

**Fix:** Replace all "none" cells in the comparison table with a simple dash (—) or leave blank.

| | Signal | Engine | Program |
|---|---|---|---|
| Price | $2,000/mo | $3,500/mo | $5,000/mo |
| Social posts | 12/mo | 16/mo | — |
| SEO articles | — | 4/mo | — |
| Ghostwriting (founder) | — | Yes | — |
| Creator management | — | — | 5–10/mo |
| Content strategy | — | Yes | Yes |
| Campaign execution | — | — | Yes |
| ROI reporting | — | Monthly KPI | Executive monthly |
| Monthly strategy call | Yes | Yes | Yes |

**Note:** The "no em dashes" rule applies to prose body copy and should not extend to table cells. A dash in a table is data notation, not punctuation.

**Impact:** Low (UX polish, reduces reading friction)

---

## FINDING 14 — No explicit mobile design notes anywhere in the wireframe

**Source:** 60% of B2B buyers use mobile for vendor research. CTA tap targets must be 44x44px minimum. Mobile pages must load under 2 seconds. These aren't optional — they're the standard.

**Gap:** The wireframe has zero mobile-specific design notes. A builder working from this document has no guidance on mobile behavior for any of the 12 pages.

**Fix:** Add a mobile design section to the Copy and Design Consistency Rules at the bottom of the wireframe:

**Mobile Design Rules (add to the rules table):**
- All CTA buttons: minimum 44x44px tap target on mobile
- Hero layout: stack vertically on mobile (photo below headline, not beside it)
- Logo bar: horizontal scroll on mobile if 3+ logos don't fit the viewport
- Case study cards: single column on mobile (not 2x2 grid)
- Comparison table: horizontal scroll on mobile (do not collapse to stacked list — it kills scannability)
- Contact form: single column, each field full-width
- Nav: hamburger menu on mobile, CTA ghost button visible in hamburger
- Page load target: under 2 seconds on mobile (Framer default helps; optimize all images before publishing)

**Impact:** High (foundational — without this, the build will have mobile conversion issues)

---

## Summary: What to Change

| # | Finding | Pages Affected | Impact | Effort |
|---|---------|---------------|--------|--------|
| 01 | CTA copy: second-person → first-person | All 12 | High | Low |
| 02 | Micro-copy risk reducers: add to /pricing, /about, /contact | 3 pages | Med-High | Low |
| 03 | Contact form: single column, inline validation, sharper field label | /contact | Medium | Low |
| 04 | Vanessa photo direction note: gaze toward CTA | / + /about | Low-Med | Low |
| 05 | /about: add mid-page CTA after Vanessa section | /about | Medium | Low |
| 06 | /work: add CTA in header section, not just bottom | /work | Medium | Low |
| 07 | Logo bar: add metric strip below logos | / | High | Low |
| 08 | Pricing hero: reframe from risk-reducer to outcome-lead | /pricing | Medium | Low |
| 09 | Contact subheadline: remove conditional, use three fragments | /contact | Low-Med | Low |
| 10 | Service pages: add self-selection closing line to "Who it's for" | 3 service pages | Low-Med | Low |
| 11 | Case studies: add outcome bridge before each CTA | 4 case study pages | Medium | Low |
| 12 | Homepage FAQ: add Q8 about single-client case studies | / | Med-High | Low |
| 13 | Comparison table: replace "none" with dash — | /pricing | Low | Low |
| 14 | Mobile design notes: add to wireframe rules | All 12 | High | Low |

**All 14 fixes are low effort.** None require new assets, new content, or new proof. They're copy edits, design notes, and structural additions using what already exists.

---

## What We Are NOT Changing

Per the constraint: only work with available assets.

| CRO recommendation from research | Why we're not applying it |
|----------------------------------|--------------------------|
| Video testimonials on landing page | No video yet |
| G2 / review platform badges | Not on G2 or Capterra yet |
| Live chat widget | Operational overhead not justified at launch |
| Exit-intent popups | Too early; not enough traffic to test |
| A/B test variants | Launch first, then test |
| "Trusted by X customers" count | Only 3 named clients — don't dilute with a number |
| Security/SSL badge near form | Framer handles SSL by default; mention not needed |

---

## Priority Build Order (CRO-informed)

The research confirms the existing launch priority from sota_report_agency_structure.md. No change needed. The additions above layer into the existing pages — they don't add pages.

The single highest-leverage page to get right before any outreach: **the homepage**. It has the highest traffic and the most CRO surface area. Findings 01, 02, 04, 07, and 12 all touch the homepage.
