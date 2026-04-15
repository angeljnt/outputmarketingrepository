# Output Marketing - Design Optimize CRO Audit

Date: 2026-04-02
Site evaluated: https://outputmarketing.lovable.app
Evidence basis:
- Rendered crawl across 12 routes on desktop + mobile
- Above-the-fold screenshots (home, pricing, contact)
- Extracted DOM text/CTAs/forms from each route
- Skill script output: `design-optimize-cro-audit.md`

## 1) Executive Summary
- Conversion objective: Increase qualified pilot starts and contact form submissions from B2B SaaS buyers.
- Top constraints:
  - Credibility proof is concentrated around one client (Archive) across most pages.
  - Primary CTA language is inconsistent across routes (`Start a pilot`, `Start my pilot`, `Start my 30-day pilot`, `Start your 30-day pilot`, `Send it`).
  - Mobile journey has no persistent primary action; the menu state can feel visually mixed with underlying content.
  - Production build still shows Lovable badge overlay on all tested routes.
- Top opportunities:
  - Build a single CTA system and one dominant conversion path.
  - Increase trust depth near conversion points with broader proof and stronger risk reversal.
  - Tighten message match and segmentation (B2B SaaS primary vs DTC secondary) in first screen + nav + pricing.
  - Reduce form friction while preserving lead quality.

Assumptions (explicit):
- Primary audience is B2B SaaS founders/marketing teams (Seed-Series B); DTC is secondary.
- Primary conversion action is `Start my 30-day pilot`.
- Scope is both desktop and mobile.
- No baseline analytics were provided, so metric targets are directional until instrumentation is confirmed.

## 2) Prioritized Findings

### P1 - CTA architecture is fragmented across high-intent pages
- Rule IDs: LAW-03, CTA-001, MOB-001
- Issue:
  - CTA labels vary across routes and contexts.
  - Extracted labels include: `Start a pilot`, `Start my pilot`, `Start my 30-day pilot`, `Start your 30-day pilot`, `Send it`.
  - Homepage alone exposes many CTA-like pathways (pricing, work, case studies, multiple pilot labels), which dilutes one clear next step.
- Why it matters:
  - Users cannot form one stable action model. Label inconsistency increases cognitive load and harms click confidence.
- Recommended change:
  - Standardize primary CTA globally to one label: `Start my 30-day pilot`.
  - Keep one secondary CTA (`See case studies`) with visibly lower weight.
  - Rename form submit from `Send it` to `Start my 30-day pilot` (or `Request my 30-day pilot`) to preserve continuity.
- Expected impact:
  - Higher primary CTA CTR, clearer funnel progression, lower CTA cannibalization.

### P1 - Trust depth is narrow and over-indexed on one client
- Rule IDs: LAW-05, PROOF-001, FAQ-001
- Issue:
  - `Archive` appears across homepage, work page, case studies, and service pages.
  - Most visible outcomes are from one account, even though results are strong.
- Why it matters:
  - Concentrated proof creates transferability skepticism (`Can they do this for us?`) especially for enterprise or non-Archive-like buyers.
- Recommended change:
  - Add at least 3 new proof types above and near CTA points:
  - Distinct client/logo strip by segment (SaaS category diversity).
  - Mini outcomes matrix (problem -> intervention -> result) for multiple accounts.
  - Testimonial snippets tied to each service page's use case.
  - Add a direct objection block on homepage: `Yes, most detailed studies are Archive. Here is why the method generalizes.`
- Expected impact:
  - Better trust at decision stage, stronger form start rate, improved qualified submission share.

### P1 - Production trust leak: Lovable badge visible site-wide
- Rule IDs: LAW-05, VIS-001, STICKY-001
- Issue:
  - Fixed `Edit with Lovable` badge is present across tested routes (desktop and mobile), high z-index, bottom-right overlay.
- Why it matters:
  - It weakens brand polish, can distract from primary CTA, and may reduce buyer confidence on high-value service pages.
- Recommended change:
  - Remove badge for production domain immediately.
  - Re-run visual QA to ensure no new overlap or focus order side effects.
- Expected impact:
  - Cleaner professional perception and improved trust at first impression.

### P2 - Message segmentation is clear but not fully aligned across funnel
- Rule IDs: LAW-01, LAW-02, HERO-001, CONTENT-001
- Issue:
  - Hero emphasizes B2B SaaS strongly, while metadata and some proof references include DTC framing.
  - This can blur “who this is for right now” on high-intent pages.
- Why it matters:
  - Ambiguous ICP boundaries reduce perceived relevance and increase bounce from qualified SaaS buyers.
- Recommended change:
  - Keep homepage and service pages explicitly B2B SaaS-first.
  - Move DTC references into a secondary segment block (`Also relevant for DTC teams with SaaS-like GTM motion`) instead of mixed top-level messaging.
  - Add one-line fit filter near hero CTA: `Best fit: Seed-Series B SaaS teams needing pipeline from content in 90-180 days.`
- Expected impact:
  - Higher first-screen relevance and improved qualified traffic-to-lead conversion.

### P2 - Contact conversion flow is solid but missing speed-to-conversation option
- Rule IDs: LAW-04, FORM-001, LAW-05
- Issue:
  - Contact form has 4 required fields and clear labels (good).
  - There is no instant scheduling path for high-intent users.
- Why it matters:
  - High-intent visitors often prefer immediate booking; async-only response can lose urgency and intent.
- Recommended change:
  - Keep existing form, but add `Book a 20-min intro call` secondary action above the form.
  - Add optional selector in form: `I'm interested in: Founder LinkedIn / Content Marketing / Organic SEO / Not sure`.
  - Keep company optional (or conditionally required) to reduce top-funnel friction.
- Expected impact:
  - Faster meeting conversion, lower abandonment among urgent buyers, better routing quality.

### P2 - Mobile continuity can improve with persistent action strategy
- Rule IDs: LAW-07, MOB-001, MOB-002, STICKY-001
- Issue:
  - Mobile has a good hero, but no persistent CTA as users scroll long pages.
  - Open menu state still leaves underlying hero content visible, which can feel visually noisy.
- Why it matters:
  - On long mobile pages, users lose action affordance and re-orientation costs increase.
- Recommended change:
  - Add sticky bottom mobile CTA (`Start my 30-day pilot`) with safe-area spacing.
  - Lock body scroll when mobile menu is open and increase menu visual separation.
  - Ensure sticky CTA never obscures form fields or footer links.
- Expected impact:
  - Higher mobile session-to-lead rate and lower backtracking.

### P3 - Homepage information density can be tightened for scan speed
- Rule IDs: VIS-003, VIS-004, CONTENT-001, VIS-005
- Issue:
  - Long narrative blocks and repeated claims increase reading load.
- Why it matters:
  - Scanners need fast qualification and proof before deeper reading.
- Recommended change:
  - Compress long paragraphs into stronger heading + 2-3 bullets.
  - Add anchor shortcuts after hero (`How we work`, `Proof`, `Pricing`, `FAQ`).
  - Keep detailed rationale but progressively disclose lower-priority copy.
- Expected impact:
  - Better scroll progression and faster path to CTA clicks.

## 3) Layout Redesign Spec

### Above-the-fold structure (homepage)
- Eyebrow: `B2B SaaS Content & SEO Agency`.
- Headline: Keep current core but shorten to one outcome-first sentence.
- Subhead: 1 line on mechanism (Founder LinkedIn + content + SEO) and timeframe expectation.
- Primary CTA: `Start my 30-day pilot`.
- Secondary CTA: `See case studies`.
- Trust micro-row directly under CTAs: `No retainer`, `30-day pilot`, `Reply in 24h`.

### Component order and hierarchy
- Hero + dual CTA (primary heavy, secondary light)
- Problem framing (compressed)
- Service pathways (3 cards)
- Proof matrix (multi-client, multi-outcome)
- How it works (pilot -> strategy -> output)
- Pricing snapshot + link to full pricing
- FAQ near commitment zones
- Final conversion block

### CTA system and interaction states
- One primary label everywhere: `Start my 30-day pilot`.
- One secondary label style: `See case studies` or `See full pricing` depending on page.
- Form submit mirrors primary action language.
- Mobile sticky CTA appears after first viewport and hides on form focus.

### Trust and objection handling placement
- Place trust indicators next to every key CTA cluster.
- Add `Why this is not just Archive-specific` section immediately before final CTA.
- On pricing/contact pages, include proof snippet adjacent to form or pilot box.

### Mobile specifics
- Keep top nav concise, lock scroll when menu open.
- Sticky CTA with safe spacing and 44px+ touch targets.
- Reduce paragraph lengths and increase visual chunking on long service pages.

## 4) Experiment Backlog

### Test 1 - CTA normalization
- Hypothesis: A single CTA label across all pages increases click confidence and conversion continuity.
- Primary metric: Primary CTA CTR by page template.
- Guardrails: Case-study clicks, pricing page visits.
- Expected effect: +8% to +20% primary CTA CTR.
- Effort: Low.

### Test 2 - Multi-client proof module above fold+1
- Hypothesis: Diversified proof increases trust for non-Archive prospects.
- Primary metric: Contact form start rate from homepage and service pages.
- Guardrails: Lead quality score, bounce rate.
- Expected effect: +10% to +25% form starts.
- Effort: Medium.

### Test 3 - Contact flow split (book call + form)
- Hypothesis: Offering instant scheduling captures high-intent visitors who avoid forms.
- Primary metric: Meetings booked + qualified submissions (combined).
- Guardrails: No-show rate, low-fit lead ratio.
- Expected effect: +12% to +30% total conversion actions.
- Effort: Medium.

### Test 4 - Mobile sticky CTA + menu scroll lock
- Hypothesis: Persistent mobile action and cleaner nav state improve completion on long pages.
- Primary metric: Mobile session-to-contact conversion rate.
- Guardrails: Scroll depth, rage clicks, CLS complaints.
- Expected effect: +8% to +18% mobile conversions.
- Effort: Medium.

### Test 5 - Remove production badge + clean trust polish
- Hypothesis: Removing non-brand overlay improves perceived quality and micro-conversion behavior.
- Primary metric: Hero CTA CTR.
- Guardrails: Page performance, layout stability.
- Expected effect: +2% to +6% CTR.
- Effort: Low.

## 5) Validation Checklist
- [ ] Primary CTA copy is identical across nav, hero, pricing, service pages, and contact form.
- [ ] Exactly one visual primary CTA per viewport context.
- [ ] Proof module includes multiple clients/use cases, not just one brand concentration.
- [ ] Contact flow offers both async form and immediate booking path.
- [ ] Mobile menu locks body scroll and does not visually compete with underlying content.
- [ ] Sticky CTA does not cover fields/controls and respects safe-area insets.
- [ ] Form labels, focus states, and error states are keyboard and screen-reader friendly.
- [ ] Tracking events fire for CTA click, form start, form submit, meeting booked, and qualified lead status.

## 6) Measurement Plan
- Primary metrics:
  - Primary CTA CTR (by page and device)
  - Contact form start rate
  - Contact form completion rate
  - Meetings booked rate
  - Qualified lead rate (MQL/SQL definition required)
- Guardrail metrics:
  - Bounce/rapid-exit rate
  - Case study click-through rate
  - Low-fit lead ratio
  - Mobile rage-click rate and backtrack rate
  - Core web vitals (LCP/INP/CLS)
