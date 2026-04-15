# Output Marketing — V10 Conversion System Overhaul (Lovable Execution Prompt)

Read this entire prompt before making changes.
Implement every requirement exactly.
Everything not explicitly mentioned should remain unchanged.

IMPORTANT:
- Ignore the production Lovable badge in this pass. We will remove it manually.
- Do not invent new client logos, client names, or performance metrics.
- Do not remove existing case study routes.
- Keep current visual brand direction (minimal, clean, premium, light neutral base + dark accent sections).

---

## 0) Objective, Audience, Primary Action

Objective:
- Increase qualified pilot inquiries and contact form submissions.

Primary audience:
- B2B SaaS founders and small marketing teams, Seed to Series B.

Secondary audience:
- DTC-aligned teams with similar go-to-market motion.

Single primary conversion action across the site:
- `Start my 30-day pilot`

Do not use multiple competing primary CTA labels.

---

## 1) Scope and Routes

Apply this pass to these existing routes:
- `/`
- `/about`
- `/pricing`
- `/contact`
- `/work`
- `/work/archive-radar-launch`
- `/work/archive-ai-newsletter`
- `/work/archive-linkedin-strategy`
- `/work/archive-product-marketing`
- `/services/founder-linkedin`
- `/services/content-marketing`
- `/services/organic-seo`

No new routes required.

---

## 2) Global Non-Negotiables (Site-Wide)

### 2.1 CTA language normalization

Use this exact primary CTA label everywhere a primary conversion action appears:
- `Start my 30-day pilot`

Replace all variants:
- `Start a pilot`
- `Start my pilot`
- `Start your 30-day pilot`
- Any other pilot CTA variation

Where this must be updated:
- Top nav CTA
- Hero primary CTA
- Pricing plan CTAs
- Mid-page and bottom-page primary CTAs
- Contact page submit label or immediate post-submit action label text

Secondary CTA rules:
- Allowed secondary labels:
- `See case studies`
- `See full pricing`
- `Book a 20-min intro call` (contact page only)
- Secondary CTAs must be visually subordinate to the primary CTA.

### 2.2 Conversion hierarchy rule

For every viewport and section:
- One visually dominant CTA only.
- Secondary links can exist but must not match primary CTA weight.
- Avoid clusters of equal-weight buttons.

### 2.3 Trust architecture rule

Because proof is currently concentrated around Archive:
- Keep existing Archive proof.
- Add explicit transferability framing so users understand methodology applies beyond one client.
- Do not fabricate additional client outcomes.

Add this principle line near proof sections:
- `Most detailed public examples are from Archive. The operating system behind them is what we apply to every engagement.`

### 2.4 ICP clarity rule

B2B SaaS is primary.
DTC is secondary.

Every major page should make this clear in first screen or first content block:
- Primary fit statement for SaaS
- Secondary note for DTC-like buyers (not equal weighting)

### 2.5 Body copy scanability rule

Reduce reading friction:
- Maximum 2-3 sentences per paragraph in high-impact sections.
- Use short bullets for lists of outcomes, deliverables, or objections.
- Avoid long unbroken narrative walls where a heading + bullets is stronger.

### 2.6 Accessibility and interaction baseline

Do not regress accessibility:
- Keep semantic heading order.
- Ensure form labels are explicit and visible.
- Preserve keyboard navigation.
- Keep strong contrast for text and CTAs.
- Preserve focus styles.

---

## 3) Global Component Specs

### 3.1 Primary CTA component

Purpose:
- Single dominant conversion action.

Label:
- `Start my 30-day pilot`

Visual:
- Filled dark button.
- Medium-to-high contrast.
- Clearly dominant over links and ghost buttons.

Interaction:
- Hover, focus-visible, active states.
- Pointer + keyboard friendly.

### 3.2 Secondary CTA component

Use for:
- `See case studies`
- `See full pricing`
- `Book a 20-min intro call`

Visual:
- Lower emphasis than primary.
- Link or ghost style.
- Never visually equivalent to primary CTA in same block.

### 3.3 Trust micro-row component (reusable)

Use below primary CTA in hero and major conversion blocks:
- `No retainer`
- `30-day pilot`
- `Reply within 24 hours`

Render as concise chips or short inline separators.
Keep compact and scannable.

### 3.4 Transferability proof component (new reusable block)

Create a reusable block titled:
- `Why this works beyond one client`

Include:
- One short paragraph explaining method portability.
- Three short bullets:
- `Same execution framework`
- `Same measurement discipline`
- `Same channel-to-pipeline focus`

Use this block:
- Homepage (after core proof area)
- Services pages (before final CTA)
- Pricing (before final CTA)

---

## 4) Navigation and Header

### 4.1 Desktop nav

Keep existing structure and links.
Update top-right CTA label to:
- `Start my 30-day pilot`

### 4.2 Mobile nav behavior fix

Current issue:
- When menu opens, underlying page remains visually noisy.

Implement:
- Full-screen menu overlay.
- Body scroll lock when menu is open.
- Clear visual separation between menu layer and page layer.
- Menu close icon remains visible and accessible.

Mobile menu content:
- Work
- Services
- Pricing
- About
- Primary CTA button: `Start my 30-day pilot`

---

## 5) Homepage (`/`) — Detailed Changes

### 5.1 Hero structure

Keep overall visual direction.
Use this above-the-fold order:
1. Eyebrow:
- `B2B SaaS Content & SEO Agency`
2. H1:
- Keep current core message, tighten only if needed:
- `Pipeline from content. Built for B2B SaaS founders and their teams.`
3. Subhead:
- Keep concise mechanism statement:
- `Founder LinkedIn ghostwriting, content marketing, and organic SEO. No paid ads. No retainer.`
4. Primary CTA:
- `Start my 30-day pilot`
5. Trust micro-row:
- `No retainer` / `30-day pilot` / `Reply within 24 hours`
6. Secondary CTA:
- `See case studies`

### 5.2 Above-the-fold fit qualifier (new)

Directly under trust micro-row, add one short fit line:
- `Best fit: Seed to Series B B2B SaaS teams that need pipeline from content in the next 90-180 days.`

### 5.3 Quick-jump anchor row (new)

Add compact inline anchors after hero:
- `How we work`
- `Proof`
- `Pricing`
- `FAQ`

Each anchors to relevant homepage sections.

### 5.4 Problem section refinement

Keep intent and tone.
Make scanability tighter:
- Strong section header
- Shorter paragraphs
- Preserve three-card problem framing

For each problem card:
- Keep strong headline.
- Ensure one-line impact takeaway.

### 5.5 Services triad section

Keep 3 service pathways.
Improve decision speed:
- Each card must include:
- Who it is for
- What ships
- Primary expected outcome
- One CTA path to either service detail or contact

Do not let service CTAs compete with main page primary CTA.

### 5.6 Proof section restructure

Keep existing Archive case studies and numbers.
Add explicit trust layering:
1. Existing proof cards (unchanged metrics)
2. New transferability proof component:
- `Why this works beyond one client`
3. CTA block:
- Primary: `Start my 30-day pilot`
- Secondary: `See case studies`

### 5.7 FAQ block

Keep FAQ on homepage.
Ensure:
- Top objections are present:
- timeline
- commitment
- deliverables
- fit
- communication model

FAQ toggles must be clearly tappable on mobile.

### 5.8 Final CTA block

Use strict hierarchy:
- Headline: one clear decision prompt
- Primary CTA: `Start my 30-day pilot`
- Secondary CTA: `See full pricing`
- Trust micro-row under CTA

---

## 6) About (`/about`) — Detailed Changes

Goal:
- Convert credibility narrative into confidence + action.

Changes:
1. Keep team/founder story.
2. Add compact section:
- `Who we are best for`
- bullets for fit.
3. Add compact section:
- `How we work with clients`
- direct access
- execution ownership
- reporting cadence
4. Add CTA cluster at end:
- Primary: `Start my 30-day pilot`
- Secondary: `See full pricing`
- trust micro-row

Tone:
- Direct and human.
- Avoid generic agency language.

---

## 7) Pricing (`/pricing`) — Detailed Changes

Goal:
- Improve pricing comprehension and decision confidence.

### 7.1 First screen

Keep current headline concept.
Ensure first screen includes:
- Pricing model summary
- What pilot includes
- No-retainer framing
- Primary CTA: `Start my 30-day pilot`

### 7.2 CTA label cleanup

Replace all `Start my pilot` variants with:
- `Start my 30-day pilot`

### 7.3 Plan clarity block

For each plan tier:
- Add explicit ideal customer profile line.
- Add top 5 deliverables.
- Add one expected business outcome line.

### 7.4 Decision support module (new)

Add compact section:
- `Not sure which tier fits?`
- 3-question decision helper:
- stage
- current content maturity
- internal team bandwidth

End this helper with:
- Primary CTA: `Start my 30-day pilot`

### 7.5 Risk-reversal reinforcement

Near pricing CTA:
- Repeat trust micro-row.
- Include 24-hour response promise.
- Clarify no lock-in language.

### 7.6 Proof before final CTA

Insert transferability proof component before final conversion block.

---

## 8) Contact (`/contact`) — Detailed Changes

Goal:
- Increase total qualified conversion actions while preserving lead quality.

### 8.1 Dual conversion paths (new)

Above the form, present two paths:
1. Primary:
- `Start my 30-day pilot` (submits form path)
2. Secondary:
- `Book a 20-min intro call` (link target placeholder if no scheduler URL: `#`)

If scheduler URL exists, use it.
If not, keep secondary button visible with clear placeholder link for future integration.

### 8.2 Form optimization

Current fields are all required.
Update to:
- Name (required)
- Work email (required)
- Company (optional)
- What do you need fixed in the next 90 days? (required textarea)
- Service interest select (new, optional):
- Founder LinkedIn
- Content Marketing
- Organic SEO
- Not sure yet

### 8.3 Submit button and confirmation

Submit button label:
- `Start my 30-day pilot`

Success state copy:
- `Got it. We’ll reply within 24 hours. If your timeline is urgent, book a 20-min intro call.`

### 8.4 Contact reassurance block

Below form:
- `No retainer`
- `30-day pilot`
- `Reply within 24 hours`
- Direct email line retained

---

## 9) Work Hub and Case Studies (`/work` + `/work/*`)

Goal:
- Use proof to drive conversion, not just passive reading.

### 9.1 Work hub (`/work`)

Keep current case study cards.
Improve conversion framing:
- Add short intro line:
- `These are public examples. The system behind them is what we apply to every engagement.`

At end of grid:
- Primary CTA: `Start my 30-day pilot`
- Secondary CTA: `See full pricing`
- trust micro-row

### 9.2 Individual case study pages

Keep all current metrics and narrative.
Add consistent conversion footer block on each case page:
- Headline:
- `Want this operating system applied to your team?`
- Primary CTA:
- `Start my 30-day pilot`
- Secondary CTA:
- `See all case studies`
- trust micro-row

---

## 10) Service Pages (`/services/*`) — Detailed Changes

Apply consistent structure to all three service pages:
- `/services/founder-linkedin`
- `/services/content-marketing`
- `/services/organic-seo`

### 10.1 Page blueprint

Use this order:
1. Hero
2. Who this is for
3. What ships
4. What changes in the business
5. Proof snippets
6. Process
7. FAQ
8. Transferability proof component
9. Final CTA block

### 10.2 Hero standard

Each service hero must include:
- clear problem statement
- specific mechanism
- primary CTA `Start my 30-day pilot`
- trust micro-row
- secondary CTA `See full pricing`

### 10.3 Deliverables clarity

In `What ships`:
- use bullets.
- concrete, countable outputs where possible.
- no vague “ongoing support” phrasing without specifics.

### 10.4 Outcome framing

Include one section:
- `What this should change`
- 3-5 bullet outcomes tied to pipeline, engagement quality, or conversion quality.

### 10.5 Proof integration

Keep existing case-study links.
Add one-line context on proof portability:
- `Public examples are concentrated in one account, but the operating model is channel-agnostic and repeatable.`

### 10.6 Final conversion block

On each service page footer:
- Primary CTA: `Start my 30-day pilot`
- Secondary CTA: `See full pricing`
- trust micro-row

---

## 11) Mobile CRO Upgrades (All Pages)

### 11.1 Sticky mobile CTA (new)

Add sticky bottom CTA on mobile for long pages:
- Label: `Start my 30-day pilot`
- Visibility:
- appears after user scrolls past hero.
- hides when footer CTA is in view.
- hides on focused input fields to avoid obstruction.

### 11.2 Spacing and scan rhythm

On mobile:
- tighten long text blocks.
- keep headings clear and frequent.
- increase spacing between unrelated content groups.

### 11.3 Tap ergonomics

Ensure:
- tap targets are comfortable.
- FAQ controls are easy to open/close.
- menu controls and CTA buttons are consistently reachable.

### 11.4 Menu continuity

When mobile menu is open:
- lock body scroll.
- reduce visual noise from underlying page.
- keep CTA visible in menu.

---

## 12) Instrumentation Requirements (Add if not already present)

Track these events:
- `cta_primary_click` with page and location context
- `cta_secondary_click` with label context
- `contact_form_start`
- `contact_form_submit`
- `contact_form_success`
- `book_intro_call_click`
- `faq_expand`
- `pricing_tier_cta_click`

Attach route + device + section metadata to events.

---

## 13) QA Acceptance Checklist

Ship only when all are true:

1. Every primary CTA uses exact label `Start my 30-day pilot`.
2. No remaining `Start a pilot`, `Start my pilot`, or `Start your 30-day pilot`.
3. Contact submit is aligned to pilot action language.
4. Mobile menu locks body scroll and reads as clean overlay.
5. Sticky mobile CTA works without covering interactive elements.
6. Proof sections include explicit transferability framing.
7. No fabricated client logos, names, or new metrics.
8. Existing case study routes still work.
9. No layout regressions in desktop or mobile.
10. Form remains accessible and keyboard-friendly.

---

## 14) Final Output Requirements

After implementing:
1. Provide a concise changelog grouped by route.
2. List every CTA label updated.
3. Confirm where transferability proof component was added.
4. Confirm contact form field requirement changes.
5. Confirm mobile menu and sticky CTA behavior.
6. Report any item not completed and why.

This is a full conversion architecture pass.
Do not return partial work.

---

## 15) Exact Copy Pack (Use Exactly)

Use these exact strings for all newly added or replaced conversion-critical copy.

### 15.1 Global find/replace (required)

Replace any of these labels:
- `Start a pilot`
- `Start my pilot`
- `Start your 30-day pilot`

With:
- `Start my 30-day pilot`

Do not leave any old variant on any route.

### 15.2 Homepage exact new/updated lines

Hero eyebrow:
- `B2B SaaS Content & SEO Agency`

Fit qualifier:
- `Best fit: Seed to Series B B2B SaaS teams that need pipeline from content in the next 90-180 days.`

Transferability section title:
- `Why this works beyond one client`

Transferability paragraph:
- `Most detailed public examples are from Archive. The operating system behind them is what we apply to every engagement.`

Transferability bullets:
- `Same execution framework`
- `Same measurement discipline`
- `Same channel-to-pipeline focus`

Quick anchors:
- `How we work`
- `Proof`
- `Pricing`
- `FAQ`

### 15.3 About page exact new sections

Section title:
- `Who we are best for`

Bullets:
- `B2B SaaS founders who need content to generate pipeline, not vanity metrics.`
- `Small marketing teams that need senior execution without a full agency org chart.`
- `Teams that value direct communication and measurable output over volume.`

Section title:
- `How we work with clients`

Bullets:
- `Direct access to the people doing the work.`
- `Clear execution scope every month.`
- `Reporting focused on pipeline signals, not noise.`

### 15.4 Pricing page exact new decision helper

Section title:
- `Not sure which tier fits?`

Section body:
- `Answer these three questions and start with the most likely fit. We can adjust after the pilot based on what the data shows.`

Three helper prompts:
- `What stage are you in today?`
- `How consistent is your current content engine?`
- `How much internal bandwidth do you have for execution?`

### 15.5 Contact page exact new conversion copy

Secondary path label:
- `Book a 20-min intro call`

Textarea label:
- `What do you need fixed in the next 90 days?`

Textarea placeholder:
- `Tell us what is blocking pipeline right now.`

Service interest field label:
- `What are you most interested in?`

Service interest options:
- `Founder LinkedIn`
- `Content Marketing`
- `Organic SEO`
- `Not sure yet`

Success state:
- `Got it. We’ll reply within 24 hours. If your timeline is urgent, book a 20-min intro call.`

### 15.6 Work hub and case-study pages exact conversion copy

Work intro line:
- `These are public examples. The system behind them is what we apply to every engagement.`

Case-study footer headline:
- `Want this operating system applied to your team?`

### 15.7 Services pages exact transferability line

Use this line on all three service pages before final CTA:
- `Public examples are concentrated in one account, but the operating model is channel-agnostic and repeatable.`

---

## 16) Build Order (Required Sequence)

Implement in this order to avoid regressions:

1. Global CTA label normalization across all routes.
2. Navigation updates (desktop label + mobile overlay/scroll lock).
3. Homepage hierarchy and new conversion modules.
4. Pricing page label cleanup + decision helper + trust reinforcement.
5. Contact dual-path conversion + form field changes.
6. Work hub and case-study conversion footer blocks.
7. Services page structure normalization and transferability module.
8. Mobile sticky CTA behavior and obstruction checks.
9. Event instrumentation.
10. QA checklist verification.

Do not skip order.

---

## 17) Regression Guardrails

Do not change these unless explicitly required above:
- Existing brand colors and base typography scale.
- Existing route map and URL structure.
- Existing public case study numbers.
- Existing image assets and attribution.
- Existing legal/privacy footer links.

If a requested improvement conflicts with a guardrail:
- keep guardrail intact
- implement closest compliant alternative
- report it in final changelog
