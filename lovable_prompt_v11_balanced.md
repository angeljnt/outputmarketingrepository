# Output Marketing — V11 Balanced CRO Prompt (Lovable)

Use this prompt to improve conversion without over-constraining the build.
Make smart, cohesive updates. Keep the site feeling intentional and clean.

IMPORTANT:
- Ignore the production Lovable badge in this pass (handled manually).
- Keep existing routes and case study pages.
- Do not fabricate new clients, logos, or performance numbers.
- Preserve the current visual brand language (minimal, premium, light neutral + dark contrast sections).
- Prioritize stability over aggressive redesign.

---

## Goal

Improve qualified conversions for B2B SaaS buyers by tightening:
1. CTA clarity
2. Trust and credibility flow
3. Contact conversion path
4. Mobile usability (especially nav/action continuity)

Primary conversion action site-wide:
- `Start my 30-day pilot`

---

## Working Style (Important)

Do this as a refinement pass, not a full rebuild.

- Keep what already works.
- Remove friction and inconsistencies.
- Avoid large structural rewrites unless needed.
- If two options are possible, choose the simpler one.

---

## Core Changes to Implement

### 1) CTA system cleanup

Unify pilot CTA language to:
- `Start my 30-day pilot`

Apply where it makes sense as primary action:
- nav CTA
- hero CTA(s)
- pricing conversion CTA(s)
- contact submit CTA
- final CTA blocks on key pages

Keep secondary actions lower emphasis:
- `See case studies`
- `See full pricing`
- `Book a 20-min intro call` (contact only)

Do not allow secondary CTAs to compete visually with the primary CTA in the same section.

---

### 2) Trust flow improvement (without fake proof)

Current proof leans heavily on one client. Keep all existing proof, but add context so trust feels broader.

Add concise transferability framing in key spots (homepage, pricing, service pages), for example:
- `Most detailed public examples are from Archive. The operating system behind them is what we apply to every engagement.`

Keep this short and natural, not defensive.

---

### 3) Contact page conversion upgrade

Keep current form, but make it easier to convert high-intent users.

Implement:
- keep form as primary path
- add a clear secondary option: `Book a 20-min intro call` (if no scheduler URL yet, placeholder is fine)
- update submit CTA to align with primary action language
- reduce unnecessary friction:
  - Name: required
  - Work email: required
  - Company: optional
  - Problem description: required
  - Optional interest selector is acceptable if cleanly integrated

Success state should reassure speed:
- 24-hour response expectation
- optional link to intro call if urgent

---

### 4) Mobile nav and action continuity

Focus on practical usability:
- mobile nav should open/close cleanly
- avoid visual conflict between menu and underlying page
- lock body scroll while menu is open
- keep action discoverability strong on long pages

If adding a sticky mobile CTA:
- use only if it does not obstruct content/inputs
- hide near footer CTA and on focused form inputs

If sticky CTA introduces clutter, skip it and keep a cleaner non-sticky solution.

---

## Page-Level Guidance

### Homepage (`/`)
- Keep hero message direction.
- Ensure one dominant first-screen CTA.
- Add short fit qualifier for primary audience (B2B SaaS Seed–Series B).
- Keep proof section, but improve flow from proof to action.
- Reduce overly dense paragraphs where scanning can be improved.

### About (`/about`)
- Keep founder/team narrative.
- Add a concise “best fit” section.
- End with clear CTA cluster (primary + secondary).

### Pricing (`/pricing`)
- Keep existing pricing architecture.
- Improve plan clarity (who it’s for + what ships).
- Ensure CTA labels are consistent.
- Add a lightweight decision helper section if it fits naturally.

### Contact (`/contact`)
- Implement dual-path conversion (form + intro call).
- Keep clean, low-friction layout.

### Work + Case Studies (`/work`, `/work/*`)
- Keep content and metrics.
- Add concise conversion bridge from proof to action.
- End case studies with a clean CTA block.

### Services (`/services/*`)
- Keep current positioning.
- Improve consistency of section flow:
  - who it’s for
  - what ships
  - expected outcomes
  - proof
  - CTA
- Add brief transferability line near final conversion zone.

---

## Quality Bar

Before finishing, verify:
1. CTA language is consistent for primary action.
2. No new visual clutter in navbar or mobile menu.
3. Contact path is clearer than before.
4. No broken routes.
5. No fabricated proof.
6. Desktop and mobile both feel more coherent, not more complex.

Test at least:
- `/`
- `/pricing`
- `/contact`
- `/work`
- one service page

---

## Final Response Format

When done, provide:
1. Brief changelog by page
2. CTA labels updated
3. Contact form changes
4. Mobile nav/action changes
5. Anything intentionally not changed (and why)

