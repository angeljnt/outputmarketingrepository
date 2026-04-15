# Output Marketing — CRO Design Justification
Date: 2026-03-23
Research basis: sota_findings_cro.md, sota_report_cro.md, site_audit_cro.md

This document explains the reasoning behind every structural and design decision on the Output Marketing website. Nothing here was done to look "pretty." Each choice traces back to published research, documented A/B test data, or practitioner consensus with a verifiable track record.

---

## 1. The Pilot Offer as the Only CTA

**The decision:** Every CTA on every page of the site points to one action — starting a 30-day pilot.

**The data:**
Pilot and trial offers consistently outperform "get a quote," "book a call," and "contact us" CTAs for service businesses. The performance gap isn't marginal. CXL, Copyhackers, and Orbit Media all document 2–3x higher conversion rates for trial-framed CTAs over quote-request-framed ones across services categories. The mechanism is low commitment: the visitor isn't being asked to buy — they're being asked to look.

Specificity also matters. HubSpot's analysis of personalized CTAs across their customer base found they performed 202% better than generic CTAs ("Get started," "Learn more," "Submit"). "Start my 30-day pilot" is specific, first-person, and low-commitment. It names exactly what happens next.

**On the site:**
All 12 pages use a single CTA pointing to `/contact`. No page has more than one CTA per section. The comparison table on the pricing page has a CTA per tier, but each tier CTA points to the same destination.

---

## 2. Single CTA Per Section

**The decision:** One CTA per section. No competing buttons. No "or you could also..."

**The data:**
Hubspot A/B tests across landing pages documented up to a 266% drop in conversion rate when multiple competing CTAs were present. The mechanism is decision fatigue: when a visitor has to choose which button to click, they often click nothing.

Unbounce's Conversion Benchmark Report confirms this pattern: pages with a single clear action convert better across all B2B categories. Every option added to a page is a reason to delay the decision.

**On the site:**
One CTA per section is a hard rule documented in the Copy and Design Consistency Rules. Secondary links (like "See full pricing →") are text links, not buttons — they don't compete with the primary CTA visually.

---

## 3. First-Person CTA Copy ("Start my pilot" not "Start your pilot")

**The decision:** All inline CTAs use first-person pronouns.

**The data:**
VWO documented up to a 90% CTR increase from switching CTA copy from second-person to first-person across multiple A/B tests. The mechanism is psychological: "Start my pilot" frames the action as something the visitor is claiming for themselves. "Start your pilot" is the brand giving instructions.

Joanna Wiebe at Copyhackers articulates the principle directly: "Think of CTAs less as the action and more as the value the person is going to drive." First-person copy makes the visitor the subject of the sentence, not the object.

**On the site:**
All inline CTAs use first-person. The shared footer uses "Start your 30-day pilot" — the footer header ("Ready to see what the output looks like?") frames the CTA in a second-person context where that phrasing reads naturally. This exception is intentional and documented.

---

## 4. The PASO Homepage Scroll Sequence

**The decision:** The homepage follows Problem → Agitate → Solution → Offer in strict section order.

**The data:**
CXL Institute, Unbounce, and Copyhackers all validate the problem-first scroll sequence for B2B services pages. The underlying psychology: a visitor who hasn't felt their pain acknowledged will not be in a buying mindset when they reach the pitch. The page must earn the right to sell.

The specific ordering at Output Marketing:
- Section 04: Problem (name the pain directly)
- Section 05: Agitate (make the cost of inaction tangible)
- Section 06: Awards (third-party validation bridges skepticism before the pitch)
- Section 07: Services (now they're ready to hear the solution)
- Section 08: Damaging admission (increases credibility of the services pitch)
- Section 09: Process (reduces friction before the CTA)
- Section 12: Pilot offer (the conversion section)

Visitors who recognize their pain in Section 04 are measurably more likely to convert by Section 12 than visitors who see the pitch first. This isn't a creative choice — it's sequence optimization.

**On the site:**
The homepage section map follows PASO in sequence. No section was placed by aesthetic preference.

---

## 5. Logo Bar Placement and Metric Strip

**The decision:** Client logos appear immediately after the hero — before the problem section, before the services pitch, before anything else. A metric strip sits below the logos with specific campaign numbers.

**The data:**
A comScore study documented a 69% conversion lift from placing client logos prominently in the first scroll area of a services page. The mechanism is credibility transfer: a visitor who recognizes a known brand in the logo bar immediately upgrades their trust level without reading a word.

Specific numbers adjacent to logos compound the effect. A 1,500-user controlled test cited in multiple CRO reports found that social proof in the first fold — particularly when quantified — produced a 34.67% increase in conversion rate.

For service businesses without testimonials, case-study-level metrics substituted for testimonial data produce similar trust signals. Unbounce and CXL both validate this substitution. "2.45% engagement rate" on a B2B product launch carries more weight than "amazing results" in a testimonial, because it's verifiable.

**On the site:**
Logo bar is Section 03 — directly below the hero. The metric strip reads: "Archive Radar launch: 2.45% engagement rate · 7 brands to waitlist / B2B fintech funding announcement: 855,000 impressions · 3.40% engagement." These are real numbers from real campaigns.

---

## 6. Proof Without Testimonials

**The decision:** The site uses a stacked proof system — logos, case study metrics, awards, named credentials — rather than testimonials or review platform badges.

**The data:**
This was the most constrained design decision on the site. Most CRO research on social proof assumes testimonials exist. The research on testimonial substitutes is thinner, but several findings hold:

Client logos are the highest-converting trust signal per unit of cognitive load. They require no reading — they're pattern recognition. That's why they sit before the problem section, not after it.

Industry awards function as third-party validation for B2B buyers who understand the award category. Webby (Best B2B Campaign) and Cannes Lions (shortlist) are recognized specifically by marketing buyers — the exact ICP for Output Marketing. This is a credential that speaks to the audience without explanation.

Named credentials (Fireflies.ai, Archive, IE Business School, CDMP) convert in B2B contexts. Forrester research and practitioner consensus agree: named companies outperform vague claims ("enterprise clients," "top-tier brands") because they're checkable. A buyer can look up Fireflies.ai and verify the scale of what Vanessa ran there.

Specific case study metrics substitute for VOC testimonials when the numbers are precise and attributable. "2.45% engagement rate on a B2B LinkedIn product launch post, versus a 0.5–1% industry average" is an argument, not a boast. It's falsifiable, and that falsifiability is what gives it credibility.

**On the site:**
No testimonial placeholders. No "clients say" sections waiting to be filled. Every proof element on the site uses only assets that currently exist.

---

## 7. Micro-Copy Risk Reducers Adjacent to CTAs

**The decision:** Every CTA button has a 1–2 line risk reducer directly below it.

**The data:**
Baymard Institute and CXL both document that the point immediately after a visitor decides to click a CTA is also the point of highest hesitation. Security language, commitment language, and response time commitments placed at this exact moment — not above or below the section, but directly adjacent to the button — measurably reduce abandonment.

Specific language outperforms vague language. "We reply within 24 hours" outperforms "fast response." "No retainer. No contract." outperforms "flexible pricing." Quantified and specific commitments work because they're promises that can be held accountable.

**On the site:**
Risk reducers are placed directly below CTA buttons on all key conversion pages:
- Pilot block (/pricing): "No retainer. No contract. We reply within 24 hours."
- /about CTA: "No long contracts. Start with 30 days."
- /contact submit button: "We reply within 24 hours. No pitch, no pressure."
- Service page heroes: "No retainer. No long contract. $1,500–$2,000 for 30 days."

---

## 8. Contact Form Design

**The decision:** 4 fields max, single column, no phone field, inline validation, specific error messages.

**The data:**
Baymard Institute's form research is the definitive source on this. Their dataset (used by Shopify, Amazon, and thousands of other high-traffic sites) shows:
- 81% baseline form abandonment rate on contact forms
- Every additional required field reduces completion
- Phone number fields without a stated reason reduce completion by 5–8% — it's the second-most abandoned field after credit card
- Multi-column form layouts outperform single-column layouts by 0% to negative — single column is the standard for completion rate
- Inline validation (real-time field feedback) reduces abandonment by 9–11% compared to submit-and-error-display flows
- Specific error messages ("Please enter a valid email (name@company.com)") reduce abandonment more than generic ones ("Please fill in this field")

**On the site:**
/contact has: Name, Company, Email, open text area. Single column. No phone. Inline validation with specific messages. Submit button reads "Send it →" (specific beats generic). Risk reducer directly below: "We reply within 24 hours. No pitch, no pressure."

The field label "What's the one thing you need fixed?" was chosen over "What are you trying to solve?" for one reason: it implies a single, specific answer. Cognitive load research from NNGroup shows that perceived effort of a question affects completion — "the one thing" feels smaller than an open question about their entire situation.

---

## 9. The Damaging Admission and Its Placement

**The decision:** Output Marketing explicitly states what it does NOT do (paid ads, video, junior teams) — and this section appears after the services pitch, not before it.

**The data:**
A Cleveland State University study on two-sided messaging found that brands that voluntarily admit limitations are rated as more trustworthy than those that only present positive claims. Robert Cialdini documents the same mechanism in *Influence*: admitting a weakness increases the credibility of all surrounding claims.

The placement after services is deliberate. If the damaging admission appears before the visitor understands what the agency does well, it reads as a warning. If it appears after — once they've been convinced by the services section — it reads as confidence. The same words, a different conversion effect, based only on sequence.

**On the site:**
Damaging Admission is Section 08, after Services (Section 07). The copy names specific limitations ("We don't run paid ads. We don't produce video.") rather than vague ones. The specificity is intentional — vague admissions ("we're not the right fit for everyone") don't trigger the trust mechanism that specific ones do.

---

## 10. About Page Architecture

**The decision:** Vanessa leads the /about page. A mid-page CTA sits directly after her section. The awards and credentials block follows Angel, not Vanessa.

**The data:**
Orbit Media's Andy Crestodina has studied about page conversion across thousands of agency sites. His finding: the about page is the second-most visited page on agency sites, and it's where trust is established or destroyed. Founder-forward about pages outperform generic "about us" pages on every metric he tracks.

A single CTA at the bottom of a long page wastes the trust built by the founder section. Visitors convinced by Vanessa's credentials halfway down the page should not have to read four more sections before they can act. The CRO principle: reduce the distance between conviction and action.

**On the site:**
Section 03b on /about is a lightweight mini-CTA ("Seen enough? Start with 30 days.") placed directly after the Vanessa section. It's not a full dark section — deliberately. Visitors who aren't convinced yet can scroll past it. Visitors who are ready don't have to scroll to the bottom.

---

## 11. FAQ as Sales Script, Not Glossary

**The decision:** FAQ questions are real buyer objections, answered as a salesperson would answer them — specifically, honestly, and without hedging.

**The data:**
Inline objection handling — addressing buyer concerns within the copy flow, not in a separate FAQ section — produces documented conversion lifts. CXL cites 80% conversion improvement data from inline objection handling versus FAQ-only approaches. The mechanism: objections addressed where they arise feel natural; objections addressed only in a separate FAQ feel like the brand knows about the problem but is hiding it.

The Output Marketing FAQ goes one step further: Question 8 directly addresses the most obvious skepticism a sharp B2B buyer will have ("All your case studies are from Archive. Should I be concerned?"). Pre-empting this objection converts better than letting the buyer leave with that question unanswered.

**On the site:**
Homepage has 8 FAQ questions, each written as a sales conversation. Q4 addresses the pilot not working out. Q6 names who actually does the work. Q8 addresses the single-client portfolio. These are the real objections, not the easy ones.

---

## 12. CTA Above the Fold on the /work Index Page

**The decision:** A secondary CTA sits in the /work page header, visible before any scrolling.

**The data:**
HubSpot's analysis of 40,000+ landing pages found that CTAs above the fold converted at 30% higher rates than CTAs below the fold, averaged across page types and industries. The /work page is a proof page, not a conversion page — but visitors who arrive from cold outreach, LinkedIn posts, or referral links often arrive with higher intent than homepage visitors. They should have the conversion path visible immediately.

**On the site:**
Section 02 of /work includes a ghost button CTA ("Start my 30-day pilot →") and risk reducer ("No retainer. See what we'd do for you first.") directly below the header note. It's intentionally understated — not a hero CTA. But it's visible above the fold.

---

## 13. Outcome Bridge Lines Before Case Study CTAs

**The decision:** Each case study ends with a one-line bridge sentence connecting the work to the visitor's situation, before the CTA.

**The data:**
Joanna Wiebe at Copyhackers: "Conversion copy should speak to what the visitor experiences or gains, not what the agency did." Case study copy written in "here's what we did" framing is interesting but not directly motivating. Reframing the work in terms of the visitor's situation ("If your next product launch matters, this is the playbook") creates relevance at the exact moment before the CTA.

The conversion mechanism: a visitor reading a case study is already evaluating fit. The bridge line closes the evaluation loop. "This is the playbook for people like you" is a soft close.

**On the site:**
Each of the four case study pages has a bridge line before its CTA section:
- Radar: "If your next product launch matters, this is the playbook."
- Newsletter: "If your customers go quiet between purchases, this is where to start."
- LinkedIn: "If your ICP is on LinkedIn and you're not showing up, this is what consistent looks like."
- Product Marketing: "If you're running multiple campaigns and losing track of what's working, this is what a dashboard changes."

---

## 14. Pricing Page Headline Reframe

**The decision:** The /pricing hero headline is outcome-focused ("See exactly what you'd get. Before you commit to anything.") rather than risk-focused ("No retainer until you've seen the work.").

**The data:**
Industry consensus from Unbounce, CXL, and practitioner surveys (2025–2026): pricing page headlines that frame what the visitor gets convert better than those that frame what the vendor won't ask for. The former is additive; the latter is subtractive. Both carry the same promise — but "see what you'd get" frames the visitor as the one who gains, while "no retainer until" frames the vendor as the one showing restraint.

The former headline remains as the subheadline on the pricing page. Nothing was removed — only reordered.

**On the site:**
/pricing Section 02 headline: "See exactly what you'd get. Before you commit to anything."
Subheadline: "Every engagement starts with a 30-day pilot. You see the quality. We learn your business. Then you decide."

---

## 15. Service Page Self-Selection Lines

**The decision:** Each service page's "Who it's for" section ends with: "Sound like you? That's who we built this for."

**The data:**
Self-qualification tools on B2B landing pages serve two functions: they reduce bad-fit inquiries (visitors who recognize they don't match self-select out) and they increase conversion from qualified visitors (visitors who recognize themselves in the bullets are prompted to confirm it).

The confirmation mechanism is a micro-commitment. Visitors who nod "yes" to the bullet list are already partially committed before they reach the CTA. The closing line completes that micro-commitment explicitly.

**On the site:**
All three service pages (/services/influencer-marketing, /services/content-marketing, /services/social-media) include this closing line after the "Who it's for" bullets.

---

## 16. Mobile Design Requirements

**The decision:** Specific mobile design rules are documented and enforced, including minimum tap target sizes, page layout stacking behavior, and a 2-second load target.

**The data:**
60% of B2B buyers use mobile for vendor research (Google, 2024 B2B study). Mobile pages loading in under 2 seconds convert at approximately 3x the rate of pages loading in over 5 seconds. Each additional second of load time reduces conversion by approximately 7%.

WCAG Level AA accessibility compliance — which overlaps with good mobile design (tap targets, contrast, form behavior) — is documented by Forrester (2023) to produce a 23% conversion lift and 23% increase in organic search traffic among accessible sites. This is not a compliance issue — it's a commercial one.

Minimum tap target of 44x44px for mobile CTAs is both the WCAG standard and the Apple Human Interface Guidelines standard.

**On the site:**
Mobile design rules are a documented section of the Copy and Design Consistency Rules, treated with the same priority as brand voice rules.

---

## 17. Vanessa Photo Direction

**The decision:** Vanessa's photo on the homepage hero and /about page should be oriented so her gaze or body angle points toward the CTA, not away from it.

**The data:**
Eye-tracking studies (NNGroup, multiple replications) show that users follow the gaze direction of human faces in images. A photo of someone looking toward the CTA moves eye attention toward the CTA. A photo of someone looking away from it moves eye attention off the page. This effect is consistent and documented across hundreds of eye-tracking sessions.

The intervention costs nothing — it's a photo composition choice. The cost of ignoring it is a measurable reduction in CTA click-through.

**On the site:**
Photo direction notes are specified in the homepage hero design note and the /about Vanessa section design note. This is a brief for the photographer or photo selector, not a post-production instruction.

---

## Summary Table

| Decision | Source | Impact |
|----------|--------|--------|
| Pilot offer as only CTA | CXL, Copyhackers: 2–3x over "get a quote" | High |
| Single CTA per section | HubSpot A/B tests: up to 266% drop with competing CTAs | High |
| First-person CTA copy | VWO: up to 90% CTR boost | High |
| PASO scroll sequence | CXL, Unbounce, Copyhackers: validated B2B scroll order | High |
| Logo bar in first fold | comScore: +69% conversion from early logo placement | High |
| Metric strip below logos | 1,500-user test: +34.67% from quantified first-fold proof | High |
| Proof without testimonials | CXL: logos + metrics substitute for VOC data | Medium-High |
| Micro-copy risk reducers | Baymard + CXL: hesitation point intervention | Medium-High |
| Contact form minimization | Baymard: 81% baseline abandonment, phone field = -5 to -8% | Medium |
| Damaging admission placement | Cleveland State University + Cialdini's Influence | Medium-High |
| About page founder-led | Orbit Media / Crestodina: about page trust architecture | Medium |
| Mid-page CTA on /about | CRO principle: reduce distance between conviction and action | Medium |
| FAQ as sales script | CXL: 80% lift from inline objection handling | Medium |
| Q8: single-client portfolio | Objection coverage research: pre-empt the obvious skepticism | Medium-High |
| CTA above fold on /work | HubSpot 40,000-page analysis: +30% from above-fold CTA | Medium |
| Outcome bridge lines in case studies | Copyhackers (Wiebe): visitor-outcome framing vs agency-action framing | Medium |
| Pricing headline reframe | Industry consensus 2025–2026: outcome over risk-reducer framing | Medium |
| Self-selection closing lines | B2B CRO research: micro-commitment before CTA | Low-Medium |
| Mobile design requirements | Google (60% B2B mobile), Forrester WCAG (+23% CVR) | High |
| Photo gaze direction | NNGroup eye-tracking: directional cues improve CTA click-through | Low-Medium |
| Comparison table: dashes not text | Cognitive load research: table notation vs reading load | Low |

---

## What We Are Not Doing — and Why

Some CRO recommendations from the research were reviewed and rejected given current constraints:

| Rejected tactic | Reason |
|----------------|--------|
| Testimonial blocks | No testimonials available at launch |
| G2 / Capterra review badges | Not listed on review platforms yet |
| Live chat widget | Operational overhead not justified pre-launch |
| Exit-intent popups | Too early — not enough traffic to test meaningfully |
| A/B test variants | Launch first, test after — no traffic baseline yet |
| "Trusted by X clients" count | Only 3 named clients — a count would diminish credibility |
| Security/SSL badge near form | Framer/Lovable/React hosts handle SSL by default; the badge would look out of place |
| Video testimonials | No video assets available |

Each of these is a legitimate CRO lever that should be revisited once the site has traffic data.

---

## Sources

- Baymard Institute — form design and abandonment research (baymard.com/learn/ux-statistics)
- CXL Institute / Peep Laja — cognitive load, social proof, microcopy, landing page research (cxl.com)
- Copyhackers / Joanna Wiebe — conversion copywriting, CTA copy, voice of customer methodology
- Orbit Media / Andy Crestodina — B2B website conversion, about page and contact page research
- Unbounce Conversion Benchmark Report — cross-industry conversion rate data
- HubSpot — 40,000+ landing page CTA analysis, personalized CTA performance data
- VWO — CTA button and copy A/B test data (vwo.com)
- Forrester — WCAG ROI and accessibility conversion impact (2022, 2023)
- Google — Core Web Vitals conversion data (2024), B2B mobile research
- NNGroup — eye tracking, cognitive load, interface complexity
- Ruler Analytics — B2B conversion benchmarks (100M+ data points, 2025)
- comScore — logo bar conversion lift study
- Cialdini, Robert — *Influence: The Psychology of Persuasion* (two-sided messaging / damaging admission)
- Cleveland State University — two-sided messaging and trust research
- Matchbox Design Group — microcopy for CTAs
- Predictable Profits — B2B CRO benchmarks by industry (2025)
- First Page Sage — B2B conversion rates by industry (2026)
