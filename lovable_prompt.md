# Output Marketing — Full Website Build Brief for Lovable

---

## HOW TO USE THIS PROMPT

Read the entire brief before responding. At the end, you will find the attachment request protocol. Follow it exactly. Do not begin building until instructed.

---

## 1. Project Brief

Build a 12-page marketing website for **Output Marketing**, a boutique B2B marketing agency run by Vanessa Semprun and Angel. The site sells a productized marketing service to B2B SaaS startups and DTC brands.

The primary conversion goal is a single action: getting visitors to start a 30-day pilot engagement ($1,500–$2,000). Every page points to this one offer.

The site is clean, direct, and minimal. No stock photos. No AI-generated imagery. No decorative illustrations. The design should feel like a premium boutique agency, not a SaaS template.

---

## 2. Tech Stack

- **Framework:** React 18 + TypeScript
- **Styling:** Tailwind CSS
- **UI Components:** shadcn/ui (use sparingly — mostly for the contact form and nav)
- **Routing:** React Router v6
- **Animations:** Framer Motion (subtle only — fade-in on scroll, no parallax, no slide carousels)
- **Contact form:** On submit, show a success toast ("We got it. You'll hear from us within 24 hours.") and reset the form. No backend needed at build time.
- **Fonts:** Inter (import via Google Fonts)
- **Icons:** Lucide React (minimal use — only where explicitly specified)

---

## 3. Design System

### Colors

```
Background (default):     #FAFAF8
Surface / card:           #F2F2EF
Dark section background:  #0F0F0F
Body text:                #111111
Muted text:               #6B6B6B
Divider lines:            #E4E4DF
CTA button fill:          #111111
CTA button text:          #FFFFFF
Ghost button border:      #111111
Ghost button text:        #111111
Dark section text:        #F0F0EB
Dark section muted text:  #999990
Metric/highlight color:   #111111
Success green:            #16A34A
Error red:                #DC2626
```

### Typography (Inter)

```
Display / Hero headline:    font-size: 60px (desktop), 36px (mobile) | weight: 700 | line-height: 1.1
H2 / Section header:        font-size: 40px (desktop), 28px (mobile) | weight: 600 | line-height: 1.2
H3 / Card header:           font-size: 22px | weight: 600 | line-height: 1.3
Body large:                 font-size: 18px | weight: 400 | line-height: 1.7
Body regular:               font-size: 16px | weight: 400 | line-height: 1.7
Label / overline:           font-size: 12px | weight: 600 | letter-spacing: 0.1em | uppercase | color: muted
Caption / small:            font-size: 14px | weight: 400 | color: muted
```

### Spacing

```
Section vertical padding:   80px desktop / 56px mobile (use py-20 md:py-28)
Container:                  max-w-5xl mx-auto px-6
Wide container:             max-w-6xl mx-auto px-6
Narrow container:           max-w-3xl mx-auto px-6
Card gap (grid):            24px (gap-6)
```

### Component Patterns

**Primary CTA button:**
```
bg-[#111111] text-white text-sm font-medium px-6 py-3
tracking-wide hover:opacity-75 transition-opacity duration-150
```

**Ghost CTA button:**
```
border border-[#111111] text-[#111111] text-sm font-medium px-6 py-3
tracking-wide hover:bg-[#111111] hover:text-white transition-colors duration-150
```

**Section label (overline):**
```
text-xs font-semibold uppercase tracking-[0.1em] text-[#6B6B6B]
```

**Dark section override:** When `bg-[#0F0F0F]`, all text becomes `#F0F0EB`, muted text becomes `#999990`, CTA button becomes white fill with black text.

**Divider line:** `border-t border-[#E4E4DF]`

**Metric display (large numbers in case studies):**
```
text-5xl md:text-6xl font-bold text-[#111111] leading-none
```

---

## 4. Shared Components

### NAV (sticky, all pages)

Layout: Logo left. Links center-right. CTA button far right.

```
[Output Marketing logo]          Work  Services  Pricing  About     [Start a pilot →]
```

- Sticky on scroll. Add `shadow-sm bg-[#FAFAF8]/95 backdrop-blur` on scroll.
- Logo: use `output-marketing-logo.png` (provided as attachment). Height 28px.
- Links: text-sm font-medium text-[#111111] hover:opacity-60 transition
- "Services" opens a simple dropdown/popover with 3 links: Influencer Marketing, Content Marketing, Social Media
- "Start a pilot →" is the ghost button style. Links to `/contact`.
- Mobile: hamburger menu. Show all nav links + ghost CTA inside the mobile drawer.

---

### FOOTER (all pages)

```
Ready to see what the output looks like?

[Start your 30-day pilot →]

Or reach us directly: vanessa@output-marketing.com

────────────────────────────────────────────

Work · Services · Pricing · About · Contact

LinkedIn (Vanessa Semprun) · X (@vanessasemprun)

© 2026 Output Marketing · Privacy
```

- The footer header text ("Ready to see what the output looks like?") is H2 size, centered.
- "Start your 30-day pilot →" is primary CTA button. Links to `/contact`.
- Nav links are small, muted, spaced evenly.
- Footer background: `#F2F2EF`. Not white, not dark.

---

## 5. Pages

---

### PAGE 01 — HOME ( / )

**SEO:** `<title>Output Marketing — B2B Marketing Agency for SaaS and DTC</title>` | `<meta name="description" content="Influencer programs, content strategy, and LinkedIn marketing for B2B SaaS and DTC brands. 30-day pilot, no retainer.">`

---

#### Section 01 — NAV
(Shared)

---

#### Section 02 — HERO

Layout: Two-column on desktop (copy left, photo right). Single column on mobile (copy above, photo below).

**HEADLINE:**
> Marketing that actually moves the needle.
> Built for B2B SaaS and DTC brands.

**SUBHEADLINE:**
> Human-first. No AI slop. Marketing with ROI.

**CTA:**
> Start my 30-day pilot →
> *(primary CTA button, links to /contact)*

**Trust line (below CTA, small muted text):**
> No retainer commitment. No long contracts. $1,500–$2,000 for 30 days.

**Photo:** Use `vanessa-hero.jpg` — positioned right column on desktop. She should appear to be looking/angled toward the CTA (left side). Rounded corners or full bleed depending on layout.

**Design:** White background. Headline is display size. Subheadline muted. CTA is the only colored element above the fold.

---

#### Section 03 — LOGO BAR

**Label (overline):**
> Brands we've built programs for

**Logos (grayscale, centered row):**
`logo-archive.png` &nbsp;&nbsp;&nbsp; `logo-fireflies.png` &nbsp;&nbsp;&nbsp; `logo-zeniq.png`

**Metric strip (below logos, small muted text, centered):**
> Archive Radar launch: 2.45% engagement rate · 7 brands to waitlist
> B2B fintech funding announcement: 855,000 impressions · 3.40% engagement

**Design:** Thin divider lines above and below the entire section. Logos are grayscale (`filter: grayscale(100%)`). Metric strip is 13px muted text.

---

#### Section 04 — PROBLEM

Background: `#0F0F0F` (dark). White text.

**HEADER:**
> Here's what's actually happening.

**Body (3 paragraphs):**
> You're spending on content. You're spending on influencers. But when you pull the metrics, the investment doesn't justify the return. If there's even any return.

> Meanwhile your competitor — the one with the worse product and half your budget — is getting all the engagement. Their content is everywhere. Their name comes up in every conversation.

> That's not a product problem. That's a marketing problem.

**Design:** No icons. No bullet points. Narrow container (max-w-3xl). Just copy. This section should feel like someone looked you in the eye.

---

#### Section 05 — AGITATE

Background: default (`#FAFAF8`).

**3 pain cards (horizontal row on desktop, stacked on mobile):**

**Card 1:**
Label icon: Lucide `TrendingDown`
Headline: Budget spent. No pipeline.
Body: You've paid for posts, campaigns, and creator fees. The CAC math doesn't work.

**Card 2:**
Label icon: Lucide `EyeOff`
Headline: Better product. Less visibility.
Body: Your roadmap is stronger. Your pricing is tighter. But no one outside your current users knows you exist.

**Card 3:**
Label icon: Lucide `Users`
Headline: Their name. Not yours.
Body: Every time your ICP searches, reads, or asks around — your competitor's name is the one that comes up.

**Transition line (centered, below cards, muted):**
> This is a solvable problem. Most agencies just aren't solving it.

---

#### Section 06 — AWARDS

Background: default.

**Overline:**
> Industry recognition

**Two award blocks side by side, centered:**

Left:
`badge-webby.png` (official badge, height 80px)
**Webby Awards**
Best B2B Campaign

Right:
`badge-cannes.png` (official badge, height 80px)
**Cannes Lions**
Shortlist Recognition

**Design:** Centered. Clean. No paragraph explaining the awards. The ICP knows what these are.

---

#### Section 07 — SERVICES

**HEADER:**
> Three ways we work with you.

**SUBHEADER (muted):**
> All of them start the same way — with a 30-day pilot so you can see the work before you commit.

**Three cards (grid on desktop, stacked on mobile):**

**Card 1 — SIGNAL**
$2,000/month
> A consistent, human social presence on the channels that matter for your ICP.
> LinkedIn + one other channel. 12 posts/month. Content calendar. Monthly report.
> For: Early-stage SaaS teams with no marketing hire yet.
[Learn more →] links to `/services/social-media`

**Card 2 — ENGINE** ← badge: "Most popular"
$3,500/month
> A content system that builds organic pipeline. Not just followers.
> Content strategy, 4 SEO articles/month, 16 social posts, founder LinkedIn ghostwriting, monthly KPI report.
> For: SaaS companies that need leads from content, not just presence.
[Learn more →] links to `/services/content-marketing`

**Card 3 — PROGRAM**
$5,000/month
> Your first influencer program. Or the one that actually works this time.
> 5–10 qualified creators/month, strategy, execution, ROI measurement, executive report.
> For: B2B SaaS and DTC brands ready to build pipeline through creators.
[Learn more →] links to `/services/influencer-marketing`

**Below cards:**
> Need a landing page, an AEO audit, or CEO ghostwriting? We do those too. [See pricing →] links to `/pricing`

---

#### Section 08 — DAMAGING ADMISSION

Background: `#F5F5F0` (slightly different from default — off-white, signals a tonal shift).

**HEADER:**
> Here's what we won't do.

**Body:**
> We don't run paid ads. We don't produce video. We don't have a floor of junior coordinators managing your account while the senior team stays busy winning new clients.

> What we do — influencer programs, content strategy, LinkedIn, SEO — we do at a level most agencies can't match precisely because we're not spread thin.

> We're a handful of people who do things really well. You talk directly to whoever is doing the work. Every time.

**Design:** No icons. No bullets. Narrow container. This should feel like a direct statement, not a section.

---

#### Section 09 — PROCESS

**HEADER:**
> How it works.

**Three steps, horizontal on desktop, stacked on mobile:**

**Step 1 — The Pilot**
> We start with 30 days. You see the quality of the work. We learn your product, your ICP, and your voice. $1,500–$2,000, no strings attached.

**Step 2 — The Strategy**
> If we continue, we build the full program — content calendar, creator roster, or both. Strategy first, execution second. No guessing.

**Step 3 — The Output**
> You get the results. We handle the work. You own everything we produce — content, relationships, playbooks.

**Below steps (muted, centered):**
> Most of our client relationships start with the pilot. Most of them don't stop there.

---

#### Section 10 — CASE STUDIES

Background: default.

**HEADER:**
> Results, not promises.

**SUBHEADER (muted):**
> All from one client. One year. Four different programs.

**4 cards (2x2 grid desktop, single column mobile):**

**Card 1**
`logo-archive.png` (small, 32px height)
Archive — Radar Feature Launch
Product Launch Marketing · Feb 2025
— 7 brands added to waitlist
— 2.45% engagement rate
— 1 upsell opportunity identified
[Read case study →] links to `/work/archive-radar-launch`

**Card 2**
`logo-archive.png`
Archive — AI Insider Newsletter
Product Launch & Customer Retention · 2025
— Recurring revenue stream established
— 3-tier customer segmentation executed
— Retention improved through value-driven content
[Read case study →] links to `/work/archive-ai-newsletter`

**Card 3**
`logo-archive.png`
Archive — LinkedIn Content Strategy
Thought Leadership · Ongoing
— 114 reactions + 68 comments on featured post
— 7,363 impressions
— 1.21% engagement rate maintained
[Read case study →] links to `/work/archive-linkedin-strategy`

**Card 4**
`logo-archive.png`
Archive — Product Marketing Campaign
Product Marketing · Ongoing
— Full campaign dashboard built
— AI Assistant + Gifting campaigns managed
— DTC brand pipeline tracked end-to-end
[Read case study →] links to `/work/archive-product-marketing`

**Below cards (small muted text):**
> These are Archive's numbers. We're not going to show you a client we barely touched.

---

#### Section 11 — CREDENTIALS

**HEADER:**
> Why Vanessa.

**Photo:** `vanessa-hero.jpg` or `vanessa-about.jpg` — same photo as hero or different angle.

**Body:**
> Before Output Marketing, Vanessa was Influencer Marketing Manager at Fireflies.ai, where she ran a B2B fintech Series G campaign: 39 creators, 855,000 impressions, 3.40% engagement. Before that, Marketing Manager at Archive — a B2B SaaS platform for DTC brands.

> She's been on the client side. She knows what it feels like to hire an agency that doesn't understand your product, your sales cycle, or your buyers. She built influencer programs from scratch, managed creator rosters, launched products, and ran the full content machine.

> The Webby Award and the Cannes Lions shortlist came from that work.

> IE Business School. CDMP certified.

**Credentials row (logos/badges, grayscale, small):**
`logo-fireflies.png` · `logo-archive.png` · `badge-ie.png` · `badge-cdmp.png`

**Link:**
[Read the full story →] links to `/about`

---

#### Section 12 — PILOT OFFER (CTA #2)

Background: `#0F0F0F` (dark).

**HEADER:**
> Start with 30 days.

**Body:**
> $1,500–$2,000. Full audit of your current presence. A strategic roadmap. Two to three weeks of live execution so you can see exactly what working with us looks like.

> No retainer. No contract. No commitment beyond the month.

**CTA:**
> Start my 30-day pilot →
> *(primary CTA, white fill / black text on dark background, links to /contact)*

**Risk reducer (below CTA, muted small text):**
> No retainer. No contract. We reply within 24 hours.

**Secondary link (muted):**
> See full pricing →

---

#### Section 13 — FAQ

**HEADER:**
> Questions you probably have.

8 FAQ items (accordion-style or all expanded — no JavaScript required if all expanded):

**Q1: Do you work with early-stage startups?**
Yes. Most of our clients are Seed to Series A, with ARR between $300K and $5M. That's exactly the stage where getting the marketing right compounds the most.

**Q2: We've never done influencer marketing before. Is that a problem?**
That's actually where we do our best work. Building a program from scratch is cleaner than fixing one that went sideways. We've done both.

**Q3: Do you run paid social or Google ads?**
No. We don't run paid. If that's what you need, we'll tell you who does it well. What we do — influencer programs, content, LinkedIn, SEO — we do without the waste that comes from spreading across everything.

**Q4: What happens if the pilot doesn't work out?**
We part ways. No pressure, no awkward conversation. The pilot exists precisely so neither of us has to make a long-term commitment before we know it's the right fit.

**Q5: How fast can we start?**
Usually within a week of the first call. We don't have an onboarding queue.

**Q6: Who actually does the work?**
Vanessa and Angel. Not a team of juniors supervised by someone you met once. You'll have both of our contact info from day one.

**Q7: Do you work with DTC eCommerce brands too?**
Yes. The influencer and content work maps cleanly to DTC — especially brands that have found their product-market fit but are burning too much on paid social and need organic and creator growth.

**Q8: All your case studies are from Archive. Should I be concerned?**
No. We chose to go deep with one client rather than shallow with ten. Four different campaigns, different channels, different goals — all from the same relationship. That's what it looks like when an agency actually commits to a client's growth. You'll get the same.

---

#### Section 14 — FOOTER
(Shared footer component)

---

---

### PAGE 02 — ABOUT ( /about )

**SEO:** `<title>About Output Marketing — Vanessa Semprun & Angel</title>` | `<meta name="description" content="A boutique marketing team that does a few things very well. No retainers. You talk directly to the people doing the work.">`

---

#### Section 01 — NAV (Shared)

#### Section 02 — HERO

Background: default. No CTA in the hero — the page earns it lower.

**HEADLINE:**
> We're a handful of people who do things really well.

**SUBHEADLINE:**
> Not 50 people. Not a project manager between you and the work. Just us.

**Design:** Large headline. Clean white. No photo here. Let the headline breathe.

---

#### Section 03 — VANESSA

**Overline:** The founder

**Photo:** `vanessa-about.jpg` — professional, warm but direct, not a headshot. Working. Photo should be oriented so her gaze/body angles subtly toward the CTA below (right side of layout on desktop).

**Body:**
> Before Output Marketing, Vanessa was Influencer Marketing Manager at Fireflies.ai, where she ran a B2B fintech Series G campaign: 39 creators, 855,000 impressions, 3.40% engagement on a B2B funding announcement. Before that, Marketing Manager at Archive, a B2B SaaS platform for DTC brands.

> She's been on the client side. She knows what it feels like to hire an agency that doesn't understand your product, your sales cycle, or your buyers. She built influencer programs from scratch, ran the full content machine, and managed product launches. All of it measurable.

> The Webby Award and the Cannes Lions shortlist came from that work.

**Credentials row:**
`logo-fireflies.png` · `logo-archive.png` · `badge-ie.png` · `badge-cdmp.png`
*(small logos, grayscale, centered)*

**Awards row:**
`badge-webby.png` &nbsp;&nbsp; `badge-cannes.png`
*(official badges, 60px height)*

**LinkedIn link:**
[LinkedIn →] href="https://linkedin.com/in/vanessasemprun" target="_blank"

---

#### Section 03b — MINI CTA (after Vanessa, before Angel)

Background: `#F5F5F0` (muted, lightweight — not a full dark section)

Centered layout, minimal:

> Seen enough? Start with 30 days.

**CTA:**
> [Start my 30-day pilot →] links to `/contact`

**Risk reducer:**
> No retainer. No contract.

---

#### Section 04 — ANGEL

**Overline:** Strategy and operations

**Photo:** `angel-photo.jpg`

**Body:**
> Angel handles strategy, operations, and the technical side of execution. Landing pages, written content, systems that keep things running.

> He doesn't touch video or paid ads. He doesn't have to. What he builds generates pipeline without burning budget.

**Design:** Shorter than Vanessa's section. Intentionally. She's the named founder.

---

#### Section 05 — PHILOSOPHY

Background: `#0F0F0F` (dark).

**HEADER:**
> How we think about marketing.

**Body:**
> Most agencies spread thin. They take every client, every channel, every ask. The work suffers. The client notices. The relationship ends.

> We do influencer programs, content strategy, LinkedIn, and SEO. We do those things at a level most agencies can't match because we're not also doing paid ads, video, PR, and event marketing at the same time.

> You talk directly to whoever is doing the work. Every time. No account managers. No weekly updates from someone who wasn't in the meeting.

---

#### Section 06 — AWARDS + CREDENTIALS BLOCK

**Overline:** Recognition and background

Two-column layout:

**Left — Awards:**
`badge-webby.png`
Webby Awards / Best B2B Campaign

`badge-cannes.png`
Cannes Lions / Shortlist Recognition

**Right — Experience:**
Fireflies.ai — Influencer Marketing Manager
Archive — Marketing Manager
IE Business School — MBA
CDMP — Certified Digital Marketing Professional

---

#### Section 07 — CTA

**HEADER:**
> Work with people who have done this before.

**CTA:**
> Start my 30-day pilot →
> *(primary CTA button, links to /contact)*

**Risk reducer (below CTA):**
> No long contracts. Start with 30 days.

**Secondary:**
> Or reach us at vanessa@output-marketing.com

**Trust line:**
> We reply within 24 hours.

---

#### Section 08 — FOOTER (Shared)

---

---

### PAGE 03 — PRICING ( /pricing )

**SEO:** `<title>Pricing — Output Marketing</title>` | `<meta name="description" content="No retainer until you've seen the work. Every engagement starts with a 30-day pilot at $1,500–$2,000. Three tiers for ongoing work.">`

---

#### Section 02 — HERO

**HEADLINE:**
> See exactly what you'd get. Before you commit to anything.

**SUBHEADLINE:**
> Every engagement starts with a 30-day pilot. You see the quality. We learn your business. Then you decide.

**Design:** No CTA above the fold. The pilot block immediately below does the work.

---

#### Section 03 — PILOT BLOCK

Background: `#0F0F0F` (dark, full-width, prominent).

**Overline:** Start here

**HEADER:**
> The 30-Day Pilot

**Price:**
> $1,500 to $2,000

**Body:**
> Full audit of your current marketing presence. A roadmap for where to go next. Two to three weeks of live execution so you can see exactly what working with us looks like.

> No retainer. No contract. No commitment beyond the month.

**What's included (bullet list):**
- Current-state audit (LinkedIn, content, creator presence, or all three depending on your need)
- Roadmap covering where to put your attention and why
- 2 to 3 weeks of live work in your highest-priority channel
- End-of-pilot debrief with recommendations

**CTA:**
> Start my pilot →
> *(white fill button on dark background, links to /contact)*

**Risk reducer (below CTA):**
> No retainer. No contract. We reply within 24 hours.

**Secondary trust line (muted):**
> Most of our client relationships start here. Most of them don't stop here.

---

#### Section 04 — THREE TIERS

**Header:**
> What comes after the pilot.

**Subheader (muted):**
> If we continue, you pick the program that fits where you are.

**Three cards:**

**SIGNAL — $2,000 / month**
> A consistent, human social presence on the channels that matter for your ICP.
Included: LinkedIn + one additional channel · 12 posts/month · Content calendar · Monthly report · 1 strategy call/month
For: Early-stage SaaS teams with no marketing hire yet.
[Start my pilot →] links to `/contact`

**ENGINE — $3,500 / month** ← "Most popular" badge
> A content system that builds organic pipeline. Not just followers.
Included: Full content strategy · 4 SEO articles/month · 16 social posts · Founder LinkedIn ghostwriting · Monthly KPI report
For: SaaS companies that need leads from content, not just presence.
[Start my pilot →] links to `/contact`

**PROGRAM — $5,000 / month**
> Your first influencer program. Or the one that actually works this time.
Included: 5–10 qualified creators/month · Creator sourcing, briefing, and management · Full campaign strategy and execution · ROI measurement and tracking · Executive-level monthly report
For: B2B SaaS and DTC brands ready to build pipeline through creators.
[Start my pilot →] links to `/contact`

---

#### Section 05 — COMPARISON TABLE

**Overline:** Side by side

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

**Design:** Clean table, no star icons. Horizontal scroll on mobile (do not collapse).

---

#### Section 06 — ADD-ONS

**Header:**
> Need something specific?

| Add-on | Price |
|--------|-------|
| CEO / Founder LinkedIn ghostwriting | +$800 / month |
| AEO (Answer Engine Optimization) audit | $1,500 one-time |
| Campaign landing page | $1,500 to $2,500 one-time |
| Influencer campaign measurement report | $500 to $1,000 / month |

**Note below:**
> Add-ons bolt onto any tier. Ask during the pilot debrief and we'll tell you if it makes sense for your stage.

---

#### Section 07 — FAQ (Pricing-specific)

**Q1: Is there a minimum commitment after the pilot?**
No. The pilot is the commitment. After that, we move month-to-month. No annual contracts, no lock-ins.

**Q2: Can I cancel anytime?**
Yes. We ask for 30 days notice so we can wrap ongoing work cleanly. That's it.

**Q3: Do prices change after we start?**
No. The rate you start at holds for as long as we work together. We don't sneak in price increases.

**Q4: What if I want more than one service?**
We've run Engine and Program simultaneously for the same client. If the budget and scope makes sense, we can build a custom package. Start with the pilot and we'll figure out the right structure.

**Q5: Can I start with the pilot and move to a different tier than I expected?**
Yes. That's the point of the pilot. We both learn what's actually needed. The tier recommendation at the end is based on what we saw in the work, not what we hoped to sell.

**Q6: Do you offer discounts for early-stage startups?**
The pilot is already priced to be accessible. For pre-revenue companies, we sometimes structure the pilot differently. Reach out and we'll be straight with you about whether we're the right fit.

---

#### Section 08 — FOOTER CTA (before shared footer)

**HEADER:**
> Not sure which plan? Start with the pilot.

**CTA:**
> Start my 30-day pilot →
> *(links to /contact)*

**Secondary:**
> Or email vanessa@output-marketing.com with where you're at.

---

#### Section 09 — FOOTER (Shared)

---

---

### PAGE 04 — CONTACT ( /contact )

**SEO:** `<title>Contact Output Marketing</title>` | `<meta name="description" content="B2B SaaS or DTC brand. Ready to talk. We reply within 24 hours.">`

---

#### Section 02 — CONTACT FORM

Layout: Centered, narrow container (max-w-lg).

**HEADLINE:**
> Let's talk.

**SUBHEADLINE:**
> B2B SaaS or DTC brand. Marketing that ships results. You're in the right place.

**Form (single-column, each field full-width):**

Field 1: Name
- Label: "Name"
- Placeholder: "Your name"
- Required: yes

Field 2: Company
- Label: "Company"
- Placeholder: "Company name"
- Required: yes

Field 3: Email
- Label: "Email"
- Placeholder: "name@company.com"
- Required: yes
- Inline validation: green checkmark when valid. Red indicator + message "Please enter a valid email (name@company.com)" when invalid.
- Validate on blur.

Field 4: What's the one thing you need fixed?
- Label: "What's the one thing you need fixed?"
- Type: textarea, min-height: 120px
- Placeholder: "Tell us where you're stuck."
- Required: yes

**CTA:**
> Send it →
> *(primary CTA button)*

**Risk reducer (directly below button):**
> We reply within 24 hours. No pitch, no pressure.

**On successful submit:** Show toast notification: "We got it. You'll hear from us within 24 hours." Reset form.

**Alternative (below form, muted):**
> Prefer email? vanessa@output-marketing.com

---

#### Section 03 — FOOTER (Shared)

---

---

### PAGE 05 — WORK INDEX ( /work )

**SEO:** `<title>Work — Output Marketing</title>` | `<meta name="description" content="Four campaigns. One client. One year. Different problems, same standard.">`

---

#### Section 02 — HEADER

**HEADLINE:**
> Results, not promises.

**SUBHEADLINE:**
> Four campaigns. One client. One year. Different problems, same standard.

**Note (small muted text):**
> These are all Archive's numbers. We're not going to show you a client we barely touched.

**Secondary CTA (below the note, visible above the fold):**
> [Start my 30-day pilot →] links to `/contact`
> No retainer. See what we'd do for you first.
> *(small, not a hero CTA — ghost button style)*

---

#### Section 03 — CASE STUDY CARDS

2x2 grid desktop / single column mobile.

*(Same 4 cards as homepage Section 10 — use a shared CaseStudyCard component.)*

---

#### Section 04 — CTA BLOCK

**HEADER:**
> Want results like these for your brand?

**CTA:**
> Start my 30-day pilot →
> *(links to /contact)*

---

#### Section 05 — FOOTER (Shared)

---

---

### PAGE 06 — CASE STUDY: Archive Radar Feature Launch ( /work/archive-radar-launch )

**SEO:** `<title>Archive Radar Launch — Output Marketing</title>` | `<meta name="description" content="2.45% engagement rate. 7 brands to waitlist. Product launch marketing for Archive's Radar feature.">`

---

**Client:** Archive | **Campaign:** Radar Feature Launch | **Type:** Product Launch Marketing | **Date:** February 2025

---

#### The company
Archive is a B2B SaaS platform for DTC brands. Creator discovery, analytics, and influencer campaign tracking, all in one place.

In early 2025, Archive launched Radar: a new feature for brands to get early visibility on emerging creators before they break out. The challenge was making that launch land with the right people, not just make noise.

#### The problem
A new feature inside an existing product is one of the hardest things to market. Existing customers already have a mental model of what the product does. New prospects don't know it exists. The window for early-adoption energy is short.

Archive needed real waitlist demand, not just impressions. And it needed to prime the top-tier DTC brands on that list for an upsell conversation.

#### The execution
- Value-first positioning: Radar was framed as early access with VIP advantage, not just another feature announcement
- Tiered customer messaging: different content for existing customers (Slack community), prospects (LinkedIn), and investors — each version spoke to what that group actually cared about
- Community activation: announced in Archive's existing Slack community to warm the list before going broader
- Lead generation mechanic: $250 early-access investment as a qualifying signal that separated serious interest from passive click-throughs
- Multi-channel coordination: LinkedIn content, email, Slack, and direct outreach running in sequence, not simultaneously

#### The numbers

Large metric display:

**7,363** impressions
**4,757** members reached
**2.45%** engagement rate
**7** brands added to waitlist
**68** comments
**12** reposts
**1** upsell opportunity identified (Midori Bikinis: tier upgrade conversation opened)

#### What worked and why

> The 2.45% engagement rate on a product launch post is strong. The industry average for B2B LinkedIn content sits around 0.5 to 1%. That gap came from specificity. The messaging spoke to a narrow ICP about a pain they recognized, not a broad audience about a vague benefit.

> The Slack community activation drove the first wave of waitlist signups. Existing customers who already trusted the product were the easiest to move. That momentum made the broader LinkedIn push land harder when it launched.

> Identifying Midori Bikinis as a potential upsell came from tracking engagement quality, not just volume. That's the difference between reporting impressions and reporting business outcomes.

---

#### CTA Section

**Bridge line:**
> If your next product launch matters, this is the playbook.

**HEADER:** Building a product launch? Start with a pilot.

**CTA:** Start my 30-day pilot → *(links to /contact)*

**Secondary:** See all case studies → *(links to /work)*

---

---

### PAGE 07 — CASE STUDY: Archive AI Insider Newsletter ( /work/archive-ai-newsletter )

**SEO:** `<title>Archive AI Newsletter — Output Marketing</title>` | `<meta name="description" content="3-tier customer segmentation, recurring revenue stream. Retention marketing for Archive's B2B customer base.">`

---

**Client:** Archive | **Campaign:** AI Insider Newsletter | **Type:** Product Launch & Customer Retention | **Date:** 2025

---

#### Context
Archive's customer base spans DTC brands at different stages and different budgets — enterprise, mid-market, newer brands still figuring out influencer marketing. A single message to all of them doesn't work.

The AI Insider Newsletter was built to do two things: keep existing customers engaged, and create a recurring revenue stream in the process.

#### The challenge
B2B SaaS retention runs on perceived value between purchase and renewal. Customers who only hear from you when something breaks or when renewal is due don't renew.

Archive needed a content program that gave customers a reason to stay engaged, and that spoke differently to each tier.

#### What we did
- Built a 3-tier segmentation model: premium tier (VIP positioning and early access), standard tier (value and insight emphasis), lower tier (exclusive content preview to drive upsell conversations)
- Multi-channel coordination: email per tier, LinkedIn posts supporting the newsletter themes, Slack announcements to the existing community, creator partnerships, and supporting blog content
- Established recurring newsletter cadence with AI-specific content relevant to the ICP
- Created a platform for ongoing thought leadership: Archive's team contributing expertise, not just promotional content

#### The outcomes

**1** new recurring revenue stream established
**3** customer tiers segmented and activated
**Multi-channel** coordination across email, LinkedIn, Slack, creators, and blog. One content calendar, all of it.
**Retention** improved through value-driven content between product touchpoints

#### What worked and why

> The segmentation model was the most important decision. A single newsletter to all tiers would have underperformed for everyone: too basic for premium customers, too aspirational for lower-tier ones. Tiering the message increased open rates and click-through across all three groups.

> No single channel reaches the whole customer base reliably. Email has the highest intent. LinkedIn has the highest visibility. Slack has the highest trust. Running them in coordination, not simultaneously with the same message, is what made the program work.

---

#### CTA Section

**Bridge line:**
> If your customers go quiet between purchases, this is where to start.

**HEADER:** Building a retention program? Start with a pilot.

**CTA:** Start my 30-day pilot → *(links to /contact)*

**Secondary:** See all case studies → *(links to /work)*

---

---

### PAGE 08 — CASE STUDY: Archive LinkedIn Content Strategy ( /work/archive-linkedin-strategy )

**SEO:** `<title>Archive LinkedIn Strategy — Output Marketing</title>` | `<meta name="description" content="1.21% engagement rate maintained. 7,363 impressions. LinkedIn content strategy for Archive.">`

---

**Client:** Archive | **Campaign:** LinkedIn Content Strategy | **Type:** Thought Leadership & Content Marketing | **Status:** Ongoing

---

#### Context
Archive sells to DTC brands. Its ICP: brand managers, CMOs, and founders at DTC companies. They spend meaningful time on LinkedIn. That's where influencer marketing gets discussed, creator economy news circulates, and buying decisions get informed.

A credible LinkedIn presence for Archive wasn't nice to have. It was the organic channel with the highest concentration of their buyers.

#### The challenge
Thought leadership content is easy to produce and easy to ignore. Most brands post consistently and see flat results because the content is generic: trend roundups, product announcements, surface-level takes.

Archive needed content that generated engagement from the right people. That meant taking real positions, backing claims with data, and writing in a voice that sounded like someone who knew the space. Not a brand account managed by a scheduler.

#### What we did
- Built content pillars specific to Archive's ICP: creator economy insights, AI in influencer marketing, micro-influencer strategy, and contrarian takes on what's working and what's dying in DTC marketing
- Wrote from Archive's brand voice: data-backed, direct, and opinionated rather than promotional
- Kept a consistent publishing cadence to build momentum in the algorithm
- Tracked performance at the post level: reactions, comments, shares, and engagement rate — identifying which topics drove the most conversation

#### The numbers (featured post)

**7,363** impressions
**114** reactions
**68** comments
**12** reposts
**1.21%** engagement rate maintained across ongoing content

#### What worked and why

> The posts that drove the most engagement weren't trend reports or product features. They were contrarian takes: things the ICP thought they understood, but that Archive could complicate or push back on. "What's actually dying in influencer marketing" outperforms "5 influencer marketing trends to watch" every time.

> 1.21% on B2B LinkedIn content is above benchmark. The industry average sits around 0.5%. The difference comes from posting less often but making each post worth reading. Not filling a calendar with volume.

---

#### CTA Section

**Bridge line:**
> If your ICP is on LinkedIn and you're not showing up, this is what consistent looks like.

**HEADER:** Want LinkedIn content that actually gets engagement?

**CTA:** Start my 30-day pilot → *(links to /contact)*

**Secondary:** See all case studies → *(links to /work)*

---

---

### PAGE 09 — CASE STUDY: Archive Product Marketing Campaign ( /work/archive-product-marketing )

**SEO:** `<title>Archive Product Marketing — Output Marketing</title>` | `<meta name="description" content="Two simultaneous product campaigns. One dashboard. Full pipeline tracking. Product marketing for Archive.">`

---

**Client:** Archive | **Campaign:** Product Marketing Campaign Dashboard | **Type:** Product Marketing | **Status:** Ongoing

---

#### Context
Archive builds tools for DTC brands to manage influencer marketing. Their product line expanded to include an AI Assistant and a Gifting campaign feature. Both needed product marketing: not just an announcement, but a full-funnel program that moved DTC brand prospects from awareness to trial.

#### The challenge
Product marketing for a SaaS platform is different from campaign marketing. The goal isn't a spike in impressions. It's a system that generates pipeline: qualified DTC brands who understand what Archive does and are ready to buy.

Running two product campaigns simultaneously (AI Assistant + Gifting) while keeping the messaging distinct for each required coordination that most agencies can't execute cleanly.

#### What we did
- Built a full campaign dashboard giving Archive visibility into both campaigns in one place: metrics, content status, creator activity, and pipeline attribution, all tracked together
- Ran AI Assistant campaign: positioned Archive's AI as a practical tool for brand teams, not a gimmick. Messaging anchored to the DTC buyer's actual workflow.
- Gifting campaign: designed for brands already using product gifting who hadn't built a repeatable system around it. Archive as the operational backbone.
- Tracked pipeline end-to-end from content impression to sales conversation, giving Archive's team data they could bring to board meetings

#### The results

**2** simultaneous product campaigns managed
**1** full campaign dashboard built from scratch
**End-to-end** DTC brand pipeline tracking implemented
**0** dropped balls. Both campaigns ran on schedule, on brief, and within budget.

#### What worked and why

> The most valuable output from this engagement wasn't the content. It was the dashboard. Archive's team went from running campaigns by feel to having one place where everything tracked. That kind of system survives personnel changes.

> Running two product campaigns simultaneously with distinct messaging for each required strict content separation at the brief level. The AI Assistant audience and the Gifting audience overlap but aren't the same people. Collapsing them into a single message would have diluted both.

---

#### CTA Section

**Bridge line:**
> If you're running multiple campaigns and losing track of what's working, this is what a dashboard changes.

**HEADER:** Running multiple campaigns and losing track?

**CTA:** Start my 30-day pilot → *(links to /contact)*

**Secondary:** See all case studies → *(links to /work)*

---

---

### PAGE 10 — SERVICE: Influencer Marketing ( /services/influencer-marketing )

**SEO:** `<title>Influencer Marketing — Output Marketing</title>` | `<meta name="description" content="Influencer programs that build pipeline, not just awareness. For B2B SaaS and DTC brands.">`

---

#### Section 02 — HERO

**HEADLINE:** Influencer programs that build pipeline, not just awareness.

**SUBHEADLINE:** For B2B SaaS companies and DTC brands that are done paying for impressions with no ROI to show for it.

**CTA:** Start my 30-day pilot →

**Trust line:** No retainer. No long contract. $1,500–$2,000 for 30 days.

---

#### Section 03 — WHO IT'S FOR

**Header:** Is this for you?

**B2B SaaS (Seed to Series A)**
- ARR between $300K and $5M
- No influencer program yet. Or one that didn't produce pipeline.
- ICP is on LinkedIn and follows creators in your category
- You want creator-driven pipeline, not just brand lift

**DTC Brands ($500K–$5M revenue)**
- Found product-market fit
- Burning too much on paid social
- Need organic and creator-led growth to reduce CAC
- Your buyers follow creators but you haven't activated that channel

> Sound like you? That's who we built this for.

---

#### Section 04 — WHAT WE DO

**Header:** What the program looks like.

- Creator sourcing: We find creators your ICP actually follows. Not the biggest names. The right ones.
- Strategy and briefing: Every creator gets a clear brief. No guessing on messaging. No off-brand posts.
- Campaign execution: We manage the timeline, the deliverables, the approval process. You review. We handle the back-and-forth.
- ROI measurement: We track from content impression to pipeline. Impressions are not a deliverable. Pipeline is.
- Monthly reporting: An executive-level report your team can share. Numbers, analysis, and next steps. Not a vanity deck.

---

#### Section 05 — CREDENTIALS

**Overline:** We've done this at scale.

> Before Output Marketing, Vanessa ran influencer programs at Fireflies.ai. She managed a B2B fintech Series G announcement: 39 creators, 855,958 impressions, 3.40% engagement on a B2B campaign. The four Archive campaigns that followed were built on the same playbook.

**Credentials row (grayscale logos):** `logo-fireflies.png` · `logo-archive.png` · `badge-webby.png` · `badge-cannes.png`

---

#### Section 06 — CASE STUDY PREVIEWS

**Header:** From the work.

2 cards:
- Archive Radar Feature Launch — 7 brands to waitlist · 2.45% engagement rate — [Read case study →]
- Archive AI Insider Newsletter — Recurring revenue stream · 3-tier segmentation — [Read case study →]

---

#### Section 07 — PROCESS

Step 1 — Pilot (30 days): We audit your current presence, map which creators your ICP actually follows, and run a small-scale test so you can see the quality before committing to a full program.

Step 2 — Program Build: We build the creator roster, brief strategy, and campaign calendar. You approve everything before it goes live.

Step 3 — Execution and Measurement: We run the program, track the pipeline, and report monthly. You own all the creator relationships and content we produce.

---

#### Section 08 — PRICING

**Program tier: $5,000 / month**
Includes: 5–10 qualified creators per month, strategy, execution, ROI measurement, executive monthly report.

**Or start with the pilot: $1,500–$2,000 for 30 days.**

**CTA:** Start my 30-day pilot → *(links to /contact)*

**Link:** See full pricing → *(links to /pricing)*

---

#### Section 09 — FAQ (Influencer-specific)

**Q1: Do you only work with B2B brands?**
No. The creator programs we run work for both B2B SaaS and DTC brands. The creator pool and briefing strategy are different for each. The rigor is the same.

**Q2: How do you find the right creators?**
We start with your ICP. We map who they follow, what content they engage with, and which creators actually influence their buying decisions. Not just the ones with large followings. Then we vet for engagement quality, audience fit, and content alignment.

**Q3: What's the minimum creator budget on top of the retainer?**
It depends on your ICP and creator tier. Micro-influencers in most B2B categories can be activated for $200–$800 per post. We'll give you a realistic number in the pilot debrief.

**Q4: How long until we see pipeline results?**
Most programs start generating measurable activity in month two. Month one is setup. Month two is when posts go live. Month three is when patterns emerge. We'll tell you this before you sign, not after.

**Q5: Do we own the creator relationships after we stop working with you?**
Yes. Everything we build belongs to you. Creator contacts, briefs, relationships, reporting templates. We don't hold any of it hostage.

---

#### Section 10 — FOOTER (Shared)

---

---

### PAGE 11 — SERVICE: Content Marketing ( /services/content-marketing )

**SEO:** `<title>Content Marketing — Output Marketing</title>` | `<meta name="description" content="SEO articles, LinkedIn ghostwriting, and content strategy for B2B SaaS teams that need organic pipeline.">`

---

**HERO HEADLINE:** Content that sounds like a person wrote it. Because one did.
**SUBHEADLINE:** SEO articles, LinkedIn ghostwriting, and content strategy for B2B SaaS teams that need organic pipeline, not just word count.
**CTA:** Start my 30-day pilot → | **Trust line:** No retainer. No long contract. $1,500–$2,000 for 30 days.

---

**WHO IT'S FOR:**

Column 1 — SaaS founders without a content team:
- Seed to Series A
- You know content matters but you haven't prioritized it
- Your LinkedIn is inconsistent. Your blog is empty or outdated.
- You want a system that runs without you writing everything yourself

Column 2 — DTC brands strong on product, silent online:
- You've found PMF
- Your paid social is expensive and the CAC math is getting worse
- You need content that brings buyers to you instead of renting audience from platforms

> Sound like you? That's who we built this for.

---

**WHAT WE DO:**
- SEO articles: Written by humans, optimized for search, structured to answer the questions your ICP is actively looking for
- LinkedIn ghostwriting: Founder or brand voice. We write it, you post it, it sounds like you.
- Content strategy: A document that tells you what to write, why, for whom, and in what order. Execution is never a blank page problem.
- AEO (Answer Engine Optimization): Making sure your content answers the questions being asked in ChatGPT, Perplexity, and Google's AI overviews. Not just traditional search.
- Monthly KPI reporting: Traffic, rankings, engagement rate, leads attributed. Actual numbers with context.

---

**CASE STUDY PREVIEWS:**
- Archive LinkedIn Content Strategy — 7,363 impressions · 114 reactions · 1.21% engagement rate
- Archive Product Marketing Campaign — 2 campaigns managed simultaneously · Full dashboard built

---

**PROCESS:**
Step 1 — Audit: We look at what you have, find the gaps, and identify the openings.
Step 2 — Strategy: Content calendar, keyword targets, topic clusters, voice guide. You approve. Then we execute.
Step 3 — Publish and Measure: Monthly report on what moved: rankings, traffic, engagement, leads.

---

**PRICING:** Engine tier: $3,500 / month. Or start with the pilot: $1,500–$2,000 for 30 days.
**CTA:** Start my 30-day pilot →

---

**FAQ:**
Q1: We write it. You review and approve before anything goes live. Most clients do a light edit pass.
Q2: Realistically, 3 to 6 months for new content to rank in competitive categories. We'll set expectations on your specific targets in the strategy phase.
Q3: The Engine tier includes founder LinkedIn ghostwriting. The add-on (+$800/month) is for Signal-tier clients who want personal LinkedIn on top.
Q4: Yes. Every article, post, strategy doc, and content calendar belongs to you.
Q5: Yes. Some clients use us to add capacity to an existing team. Others use us to build the system their team works from.

---

**FOOTER (Shared)**

---

---

### PAGE 12 — SERVICE: Social Media ( /services/social-media )

**SEO:** `<title>Social Media — Output Marketing</title>` | `<meta name="description" content="A social presence that sounds like you. Consistent content for B2B SaaS and DTC brands.">`

---

**HERO HEADLINE:** A social presence that sounds like you. Not a scheduler.
**SUBHEADLINE:** Consistent content for B2B SaaS and DTC brands that need to show up on social without spending 10 hours a week on it themselves.
**CTA:** Start my 30-day pilot → | **Trust line:** No retainer. No long contract. $1,500–$2,000 for 30 days.

---

**WHO IT'S FOR:**

Column 1 — SaaS startups with no social strategy:
- You post when you have time, which is never
- Your LinkedIn looks abandoned
- Your ICP is on social but your company isn't showing up
- You need someone to build the habit and the voice, not just post content

Column 2 — DTC brands with an inconsistent presence:
- Product photos and promotions but no personality
- Followers aren't growing
- You don't have a point of view in the content
- You want social that builds brand, not just broadcasts products

> Sound like you? That's who we built this for.

---

**WHAT WE DO:**
- Content calendar: A full month of planned content, mapped to your ICP and brand voice. Built before the month starts.
- Copy: We write every post. You review. Nothing goes live without your approval.
- Creative direction: Photography guidelines, graphic specs, or design briefs depending on your setup.
- Posting: We handle the scheduling and posting.
- Monthly report: Impressions, engagement rate, follower growth, and top-performing posts with context.

---

**CHANNELS:**
LinkedIn: Primary for B2B SaaS.
Instagram: Primary for DTC.
X (Twitter): For founders in tech and SaaS who want a public voice.
TikTok: For DTC brands where the ICP skews under-35. We don't do it half-heartedly or we don't do it at all.

Note: Signal tier covers LinkedIn + one additional channel. We'll recommend the right second channel in the pilot.

---

**CASE STUDY PREVIEW:**
Archive LinkedIn Content Strategy — 7,363 impressions · 1.21% engagement rate · 114 reactions on featured post

---

**PROCESS:**
Step 1 — Voice and Calendar: Brand voice + ICP alignment. First month's calendar. You approve direction before we write a post.
Step 2 — Write and Review: Full month of posts in one batch. One revision round, usually.
Step 3 — Post and Report: Post on schedule. Monthly report on what performed and what we're adjusting.

---

**PRICING:** Signal tier: $2,000 / month. Or start with the pilot: $1,500–$2,000 for 30 days.
**CTA:** Start my 30-day pilot →

---

**FAQ:**
Q1: LinkedIn, Instagram, X, and TikTok. We recommend based on where your ICP actually is.
Q2: We provide creative direction. If you have a designer, we brief them. If not, we recommend tools and templates.
Q3: Signal tier is 12 posts across LinkedIn and one other channel. Quality and consistency over volume.
Q4: Yes. Nothing goes live without your approval. After the first month, most clients go to a lighter review cycle.
Q5: We don't run paid. We build the organic presence that makes paid more efficient when you do run it.

---

**FOOTER (Shared)**

---

---

## 6. Routing Structure

```
/                               → Home
/about                          → About
/pricing                        → Pricing
/contact                        → Contact
/work                           → Work Index
/work/archive-radar-launch      → Case Study 1
/work/archive-ai-newsletter     → Case Study 2
/work/archive-linkedin-strategy → Case Study 3
/work/archive-product-marketing → Case Study 4
/services/influencer-marketing  → Service 1
/services/content-marketing     → Service 2
/services/social-media          → Service 3
```

Scroll to top on route change.

---

## 7. Animation Behavior

- **Section entrance:** `fade-in + slight translate-y (8px → 0)` on scroll into viewport. Duration 400ms, ease-out. Use Framer Motion's `whileInView` with `once: true`.
- **Hero headline:** No animation delay. Appears instantly.
- **CTA buttons:** opacity hover only. No scale transforms.
- **Nav on scroll:** subtle `shadow-sm` appears after 40px scroll.
- **No parallax. No slide carousels. No spinning icons.**

---

## 8. Mobile Behavior

- All CTA buttons: minimum 44x44px tap target
- Hero layout: photo stacks below copy on mobile
- Logo bar: horizontal scroll if logos don't fit viewport
- Case study cards: single column
- Comparison table: horizontal scroll container — do not collapse to stacked list
- Contact form: each field full-width
- Nav: hamburger on mobile, ghost CTA visible in the drawer
- Page load: Vite + Tailwind will handle performance; optimize all images (use WebP where possible)

---

## 9. Image Handling

- All images should use `object-fit: cover` with a defined aspect ratio wrapper
- Vanessa hero photo: 1:1 or 4:5 aspect ratio
- Award badges: rendered at consistent heights (80px), no stretching
- Logos in logo bar: rendered at consistent heights (28px), all grayscale via CSS `filter: grayscale(100%)`
- Use `loading="lazy"` on all images below the fold

---

## 10. SEO and Meta

Each page has its own `<title>` and `<meta name="description">` as specified in the page sections above. Use React Helmet or the equivalent for per-page meta management.

Add `<link rel="canonical" href="https://output-marketing.com/[path]">` to each page.

---

## 11. File Structure (Suggested)

```
src/
  components/
    Nav.tsx
    Footer.tsx
    CTAButton.tsx
    GhostButton.tsx
    CaseStudyCard.tsx
    MetricDisplay.tsx
    FAQItem.tsx
    ContactForm.tsx
  pages/
    Home.tsx
    About.tsx
    Pricing.tsx
    Contact.tsx
    Work.tsx
    work/
      RadarLaunch.tsx
      AINewsletter.tsx
      LinkedInStrategy.tsx
      ProductMarketing.tsx
    services/
      InfluencerMarketing.tsx
      ContentMarketing.tsx
      SocialMedia.tsx
  assets/
    images/         ← all uploaded attachment files go here
  App.tsx
  main.tsx
```

---

## ATTACHMENT REQUEST PROTOCOL

You now have the complete build brief for the Output Marketing website: 12 pages, full copy, design system, component specs, and routing.

**Do not write any code yet.**

Reply with exactly two things:

1. One sentence confirming you understand the full scope.
2. A numbered list of every image or asset file you need me to upload before you can build — using the exact filename specified in this brief, and a one-line note on what each file is used for.

Once I confirm all assets are uploaded, I will send a single follow-up message to begin. Until then, wait.
