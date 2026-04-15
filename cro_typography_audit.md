# CRO Typography Audit: outputmarketing.lovable.app
Date: 2026-03-24
Framework: sota_report_cro_typography.md
Method: JS bundle extraction + structural analysis

---

## How to read this audit

Each issue has:
- **What is wrong** — the exact copy or element
- **Why it matters** — the CRO principle it violates
- **What to do** — the specific fix

Issues are grouped by type, then by page. Priority: High → Medium → Low.

---

## SITE-WIDE ISSUES

---

### ISSUE 1 — Dark sections: 7 across the site (no per-page cap enforced)

**What is wrong:**
Seven `bg-dark` sections exist across the site:
1. Homepage — "Here's what's actually happening."
2. Homepage — "Start with 30 days."
3. About — "How we think about marketing."
4. Pricing — "The 30-Day Pilot"
5. Pricing/Contact — "No long contracts. Start with 30 days."
6. Work page — (case study section)
7. Services/SEO page — "Most B2B SaaS SEO is optimized for rankings, not revenue."

**Why it matters:**
The SOTA rule is 1-2 dark sections per page, maximum. More than 2 per page triggers desensitization — each section loses its visual interrupt power. Dark sections derive their conversion value from contrast with surrounding light content. When they're common, they stop being interrupts.

**What to do:**
Audit each page for its dark section count:
- Homepage: 2 — at the limit. Both are justified (problem statement + CTA). Keep both, but each must carry exactly one message.
- About: 1 — correct. Keep.
- Pricing: 2 — review whether both are necessary or whether one should become a light callout block instead.
- Services (SEO page): 1 — correct.

No individual page should have more than 2 dark sections. When in doubt, convert the secondary dark section to a bordered callout block (light background, accent border) instead.

---

### ISSUE 2 — Centered body copy in 3+ places

**What is wrong:**
`text-center` appears on multiple body text instances:
- "Need a content audit, a technical SEO review, or pSEO for your product? We do those too." — centered, ~90 characters, 2+ lines on mobile
- "This is a solvable problem. Most agencies just aren't solving it." — centered body text in problem section
- The closing line under service tiers on the pricing page — centered

**Why it matters:**
The SOTA rule: never center text longer than 2 lines. Centering multi-line body copy forces the brain to search for line starts on every line — cognitive load goes up, comprehension drops. This is one of the most consistent conversion anti-patterns documented across A/B tests.

**What to do:**
- Left-align all body paragraphs and sentences that run longer than ~60 characters or wrap to a second line.
- "Need a content audit..." should be left-aligned or converted to a CTA row (icon + text + link) rather than centered text.
- "This is a solvable problem..." should be left-aligned within its section or pulled out as a standalone callout box (not centered paragraph).
- Reserve centering for: overlines, H2 headers, statistics/single-number displays, short pull quotes (≤2 lines), and standalone CTA button groups.

---

### ISSUE 3 — "Here's" section headers: weak F-pattern front-loading

**What is wrong:**
Three section headers start with "Here's":
- "Here's what's actually happening." (Homepage problem section)
- "Here's what we won't do." (Homepage/Services)

And one FAQ header:
- "Questions you probably have." (Homepage, About)

**Why it matters:**
F-pattern scanning means the first 2 words of every line carry disproportionate weight. "Here's what" conveys nothing about the content. A skimmer who reads only the first 2 words sees "Here's what" — zero information. "Questions you" is equally empty. Subheadings must be self-sufficient: a reader scanning only headings should understand what each section is about.

**What to do:**
| Current | Better |
|---------|--------|
| "Here's what's actually happening." | "The problem with your current spend." or "Your marketing isn't the problem. The strategy is." |
| "Here's what we won't do." | "What we don't do — and why." or "No paid ads. No video. No junior teams." |
| "Questions you probably have." | "Common questions." or "Before you reach out." |

The goal: any skimmer reading only the headings should get the full story.

---

### ISSUE 4 — Bold is nearly absent from body copy

**What is wrong:**
`font-bold` appears in only 1-2 contexts in the entire bundle. `font-semibold` appears in a few UI elements (labels, badges). The vast majority of body copy is unweighted.

**Why it matters:**
Bold text is "spotted" during F-pattern scanning — fixated even by users who aren't reading linearly. The site contains high-value claims that are currently invisible to skimmers:
- "7 brands added to waitlist"
- "855,000 impressions · 3.40% engagement"
- "2.45% engagement rate"
- "No retainer. No contract."
- "We reply within 24 hours."
- "39 creators"

None of these are bolded. A skimmer lands on the homepage and can't spot-read the specific outcomes. They see undifferentiated paragraphs.

**What to do:**
Apply bold to exactly one phrase per paragraph — the specific outcome or risk reducer. Rules:
- Numbers + outcomes: bold the number and the result ("**7 brands** added to waitlist")
- Risk reducers: bold the key phrase ("**No retainer. No contract.**")
- Differentiators in competitive claims: bold the differentiating data point
- Never bold entire sentences. Never bold adjectives without specifics.

Specific phrases to bold across the site (see per-page breakdown below).

---

### ISSUE 5 — No testimonial quotes anywhere on the site

**What is wrong:**
There are no direct testimonial quotes from clients on any page. The work/case studies section has metrics and narrative but no client voice.

**Why it matters:**
Social proof placed immediately before or after a CTA produces a documented 35.6% conversion lift. The current site has strong numbers (2.45% engagement rate, 855K impressions) but no human voice validating the experience of working with Output Marketing. Metrics prove output. Testimonials prove trust.

**What to do:**
Add 1-3 direct client quotes. These should:
- Appear immediately before or after the primary CTA section on the homepage
- Include a specific metric inside the quote (not just a vague endorsement)
- Be formatted as visually isolated pull quotes (larger text, visually set apart — not inline paragraphs)
- Example of what to aim for: "We went from no LinkedIn presence to **7 brands on the Radar waitlist** in the first campaign." — [Name, Title, Archive]

If you have client quotes, the placement that produces the most lift is: immediately above the "Start my 30-day pilot →" CTA on the homepage.

---

## HOMEPAGE

---

### ISSUE 6 — Hero headline: "Marketing" is the weakest possible first word

**What is wrong:**
The display headline opens with "Marketing that actually moves the needle."

**Why it matters:**
F-pattern: the first word of the H1 is the highest-attention real estate on the page. "Marketing" tells the reader nothing they didn't know from navigating to a marketing agency's website. It wastes the most-read position on the page with a category label.

**What to do:**
Front-load the specific differentiator in the first 2 words. Options:

| Direction | Example |
|-----------|---------|
| Front-load the ICP | "B2B SaaS marketing that actually moves the needle." |
| Front-load the outcome | "Pipeline from content. Built for B2B SaaS." |
| Front-load the differentiator | "Founder-led content that compounds. No paid ads." |

The current second line — "Built for B2B SaaS companies." — contains the key differentiator but sits in a lower-attention position. Either move it to line 1 or restructure the headline so the differentiator is in the first 2 words of line 1.

---

### ISSUE 7 — "Human-first. No AI slop. Marketing with ROI." — three competing subheads

**What is wrong:**
The hero subheadline or tagline area contains three separate fragments. "No AI slop" is a negative frame that may introduce doubt before the visitor is sold on anything.

**Why it matters:**
The hero has one job: establish the value proposition in one pass. Three fragments compete for attention. "No AI slop" signals defensiveness, not confidence. Visitors who weren't thinking about AI content are now thinking about AI content.

**What to do:**
Choose one supporting line under the H1. Lead with the outcome, not the rejection. Options:
- "Founder LinkedIn ghostwriting, content, and SEO. B2B SaaS only."
- "Content that builds pipeline. Not vanity metrics."
- Drop the fragment list entirely and let the subheadline be one clean sentence.

---

### ISSUE 8 — Problem section: "This is a solvable problem. Most agencies just aren't solving it."

**What is wrong:**
This line is currently body text (`text-body text-muted-foreground text-center mt-10`) — small, centered, and visually subordinate. It follows the three problem cards.

**Why it matters:**
This is one of the highest-converting sentences on the page. It names the product category, differentiates from the competition, and creates tension toward the solution. It should be impossible to miss.

**What to do:**
Convert this to a standalone callout. Options:
1. Pull it out as a centered large-text statement (text-h3 or text-h2, dark text, no muted color)
2. Give it a dark callout box treatment — short, isolated, high contrast
3. At minimum: remove `text-muted-foreground` (muted gray is for supporting copy, not primary claims) and increase the font size

---

### ISSUE 9 — Logo bar label is weak

**What is wrong:**
"Brands we've built programs for" — 6 words, specific to "programs" which is now secondary to the services offered.

**Why it matters:**
The overline above a logo bar sets context for who the agency has worked with. "Programs" is the old influencer-program language and understates the relationship.

**What to do:**
Replace with: "Clients" or "Who we've worked with" or "B2B SaaS brands we've worked with."

---

### ISSUE 10 — "See what the output looks like." link in hero

**What is wrong:**
There is a secondary link in the hero area: "See what the output looks like." This appears alongside "Start my 30-day pilot →."

**Why it matters:**
Two CTAs at the same visual weight create decision paralysis. The SOTA rule: one primary CTA, one clearly subordinate secondary. If both look the same, the visitor doesn't know what to do.

**What to do:**
Visually subordinate the secondary link — smaller text, no button styling, different color. The primary CTA ("Start my 30-day pilot →") should be the only element with button weight. "See what the output looks like." should appear as a plain text link below the button.

---

### ISSUE 11 — "All from one client. One year. Four different programs." — buried in section

**What is wrong:**
This is the strongest unique credibility claim on the site. It addresses the obvious objection ("you only have one client") and reframes it as proof of commitment. It currently appears as body text within a section.

**Why it matters:**
This sentence should be impossible to miss. It's a damaging admission that becomes a conversion asset. Spotted-pattern scanning means it needs to be visually distinct to guarantee it gets read.

**What to do:**
Treat this as a standalone one-line statement — either:
- A pull quote: larger text (text-h3 or bigger), visually isolated with whitespace or a border
- An opening line of a dark callout section with nothing else in it
- At minimum: bold the key numbers and make it a visual anchor

---

## ABOUT PAGE

---

### ISSUE 12 — "How we think about marketing." dark section

**What is wrong:**
This dark section header is passive and vague. "How we think" is inside-out — it centers the agency's perspective rather than the visitor's need.

**Why it matters:**
Dark section headers carry extra visual weight. A header that doesn't front-load a benefit wastes the interrupt. The reader who glances at "How we think about marketing" learns nothing actionable.

**What to do:**
Reframe around the differentiation claim, not the agency's process:
- "Why we stay narrow." — front-loads the counterintuitive position
- "We do fewer things. That's the strategy." — bold claim, immediately differentiated
- "Three services. Done well. Nothing else." — specific and verifiable

---

### ISSUE 13 — "Not 50 people. Not a project manager between you and the work. Just us." — body text

**What is wrong:**
This is the single most powerful risk reducer on the About page. It addresses every agency client's primary fear (never talking to the people who do the work). It's currently formatted as body text.

**Why it matters:**
Risk reducers near decision points produce the largest conversion lifts in A/B tests. This sentence should be the first thing a visitor sees and remembers from the About page.

**What to do:**
Convert to a standalone callout — either:
- A bold oversize statement (text-h2 or text-h3) visually separated from surrounding text
- A pull quote at the top or middle of the about page
- A three-line stacked statement with line breaks: "Not 50 people. / Not a project manager between you and the work. / Just us." — each on its own line at display size

---

### ISSUE 14 — Vanessa bio front-loading

**What is wrong:**
The Vanessa bio paragraph opens: "Before Output Marketing, Vanessa was Influencer Marketing Manager at Fireflies.ai..."

**Why it matters:**
F-pattern: the first word is "Before" — past tense, retrospective framing. The most valuable information (what she achieved, why she's qualified to run your marketing) is buried after the context.

**What to do:**
Open with the achievement, then give the context:
- "39 creators. 855,000 impressions. 3.40% engagement. That was the Fireflies.ai campaign Vanessa ran as Influencer Marketing Manager before starting Output Marketing."
- Or: "Vanessa ran the full influencer program at Fireflies.ai — 39 creators, 855,000 impressions, 3.40% engagement. Before that, Marketing Manager at Archive."

Lead with the evidence. Then give the narrative.

---

## WORK PAGE

---

### ISSUE 15 — "Note: These are all Archive's numbers..." — buried as body text

**What is wrong:**
"Note: These are all Archive's numbers. We're not going to show you a client we barely touched." — This appears as a small note, likely in muted color.

**Why it matters:**
This is a masterclass damaging admission. It preempts the visitor's most likely objection to the work page, turns a weakness into a proof of commitment, and reads as radically honest. Muted small text buries it. The opposite is needed.

**What to do:**
This should be a standalone callout — prominent, dark or bordered, with full visual weight. Not a footnote. Not muted text. This is the thing that earns trust before the case studies do.

Format it as a three-line statement:
> These are all Archive's numbers.
> Four campaigns. Four different problems. One relationship.
> That's what it looks like when we actually commit to a client.

---

### ISSUE 16 — Case study metrics: numbers not visually anchored

**What is wrong:**
From the case study pages, metrics appear in body text or caption-level formatting:
- "2.45% engagement rate"
- "7 brands to waitlist"
- "855,000 impressions"
- "114 reactions"
- "7,363 impressions"

**Why it matters:**
Numbers are "spotted" during F-pattern scanning — they receive fixation even from users who skip all other text. Numbers formatted at body text size get skipped like the rest. Numbers formatted at display size become anchors that pull the eye and anchor the entire section's message.

**What to do:**
Each case study page should have a metrics block where the key numbers display at 36-56px (text-h1 or text-display level), with a short label below at caption size. The current grid layout (`grid grid-cols-2 md:grid-cols-4 gap-6`) suggests this structure exists — verify the number size is actually large (not body-size inside the grid cell).

If numbers currently display at body size, increase to at minimum text-h2 (36-44px). The metric is the anchor. Everything else is context.

---

## PRICING PAGE

---

### ISSUE 17 — Two dark sections may overlap in purpose

**What is wrong:**
Pricing page has two dark sections:
1. "The 30-Day Pilot" — explaining the pilot structure
2. "No long contracts. Start with 30 days." — the CTA section

**Why it matters:**
Two dark sections per page is the maximum. These two are close together (both focused on the pilot). When dark sections appear too close to each other, the second one loses its interrupt effect.

**What to do:**
Keep "The 30-Day Pilot" as a dark section (it's the most important section on the pricing page). Convert "No long contracts. Start with 30 days." to a high-contrast light section (white background, large text, strong CTA button) rather than a second dark section. The visual contrast from dark-to-light-to-dark is jarring; the transition from dark-to-light-CTA section is clean.

---

### ISSUE 18 — "See exactly what you'd get. Every engagement starts with a 30-day pilot. $1,500 to $2,000."

**What is wrong:**
The hero/intro of the pricing page has two very similar lines:
- "See exactly what you'd get. Every engagement starts with a 30-day pilot. $1,500 to $2,000."
- "See exactly what you'd get. Before you commit to anything."

**Why it matters:**
This is near-identical copy repeated twice in the same section. Repetition in close proximity reads as either an error or filler. It dilutes the credibility of both statements.

**What to do:**
Pick one. The first version (with the price) is stronger because the specific price ($1,500 to $2,000) is a risk reducer. Delete the second line or replace it with something that adds new information.

---

## CONTACT PAGE

---

### ISSUE 19 — "Or reach us directly:" weakens the CTA

**What is wrong:**
The form section includes "Or reach us directly:" before a direct email/contact option.

**Why it matters:**
"Or" is a decision fork. It introduces doubt about whether the form is the right action. The visitor who reads "Or reach us directly" starts wondering whether they should use the form or the direct contact instead of just submitting.

**What to do:**
Remove "Or reach us directly:" framing entirely. Present both the form and the direct contact as the same action, not alternatives:
- "We reply within 24 hours. Prefer email? angel@outputmarketing.com"
- Or remove the "or" framing and just list the email address below the form without an "or" connector.

---

### ISSUE 20 — Contact page opening: "B2B SaaS company. Marketing that ships results. We reply within 24 hours."

**What is wrong:**
"B2B SaaS company." opens the contact page description — but this is the visitor's description, not Output Marketing's. It's framed as a label for the visitor, which creates a jarring perspective shift.

**Why it matters:**
F-pattern: first words of the page set the frame. "B2B SaaS company" is ambiguous — is this a label for the visitor, a statement about the agency's focus, or something else?

**What to do:**
Make the frame clear immediately: "You're a B2B SaaS company. We can help." or simplify to just "Marketing that ships results. We reply within 24 hours." — remove the ambiguous label opening.

---

## SERVICES PAGES

---

### ISSUE 21 — SEO page dark section opener

**What is wrong:**
"Most B2B SaaS SEO is optimized for rankings, not revenue." opens a dark section. This is good copy — strong claim, front-loaded differentiator.

**But:** The body continues: "The agency publishes 8 articles a month. Traffic goes up. Demo requests don't. The client renews anyway because the traffic chart looks good."

**Why it matters:**
This is strong problem-framing copy. The dark section treatment is correct. The risk is in the body text that follows — if it's formatted as a wall of paragraph text inside a dark section, it will be skipped. Dark section body copy needs more visual breaks, shorter paragraphs, and at least one bolded phrase per paragraph.

**What to do:**
- Verify the body copy inside this dark section has ≤3 sentences per paragraph
- Bold the key diagnostic line: "Traffic goes up. **Demo requests don't.**"
- The dark section should end with a transition to the solution, not hang as a problem statement

---

## SUMMARY TABLE

| # | Page | Issue | Priority | Type |
|---|------|-------|----------|------|
| 1 | Site-wide | 7 dark sections — audit per-page cap | High | Structure |
| 2 | Site-wide | Centered body copy in 3+ places | High | Alignment |
| 3 | Site-wide | "Here's" section headers — empty front-loading | High | Copy/F-pattern |
| 4 | Site-wide | Bold virtually absent from body copy | High | Emphasis |
| 5 | Site-wide | No testimonial quotes anywhere | High | Social proof |
| 6 | Homepage | Hero H1 starts with "Marketing" — weakest first word | High | Copy/F-pattern |
| 7 | Homepage | "Human-first. No AI slop." — 3 competing sub-fragments | Medium | Copy |
| 8 | Homepage | "This is a solvable problem." — buried, muted, centered | High | Structure/Emphasis |
| 9 | Homepage | Logo bar label uses "programs" — old language | Low | Copy |
| 10 | Homepage | Two CTAs at equal visual weight | Medium | Visual hierarchy |
| 11 | Homepage | "All from one client. One year. Four programs." — buried | High | Social proof/Emphasis |
| 12 | About | Dark section header: "How we think about marketing." | Medium | Copy/F-pattern |
| 13 | About | "Not 50 people..." risk reducer is body text | High | Emphasis/Structure |
| 14 | About | Vanessa bio opens with "Before" — retrospective | Medium | Copy/F-pattern |
| 15 | Work | Archive disclaimer buried as small note | High | Social proof/Structure |
| 16 | Work | Case study numbers not at display size | High | Typography/Size |
| 17 | Pricing | Two dark sections close together | Medium | Structure |
| 18 | Pricing | Near-identical copy repeated twice | Medium | Copy |
| 19 | Contact | "Or reach us directly:" introduces decision doubt | Medium | Copy |
| 20 | Contact | "B2B SaaS company." — ambiguous opening frame | Low | Copy |
| 21 | Services | SEO dark section body needs paragraph breaks + bold | Medium | Emphasis |

---

## The 5 highest-leverage changes

If you can only fix 5 things, fix these. Ordered by expected conversion impact:

**1. Bold the key numbers and risk reducers across every page.**
Every occurrence of a specific metric, outcome, or risk reducer (No retainer, No contract, 7 brands, 855K impressions, etc.) should be bolded. This is the lowest-effort change with the highest skimmer impact. Spotted-pattern scanning means bolded text is read even by people who skip everything else.

**2. Add one testimonial directly above the primary CTA on the homepage.**
The 35.6% conversion lift from social proof proximity is the most consistently documented finding in the research. The homepage has no client voice at all. One specific, metric-containing quote above "Start my 30-day pilot →" closes more skeptical visitors than any copy change.

**3. Fix the hero headline first word.**
"Marketing that actually moves the needle" buries the differentiator (B2B SaaS, founder-led, no paid ads) 3-5 words in. F-pattern scanning means the first 2 words are what gets read. The highest-attention position on the site is currently occupied by the most generic word in marketing.

**4. "Not 50 people. Not a project manager. Just us." — give it visual weight.**
This sentence is doing the work that a $10,000 agency differentiator deck usually tries to do. It's currently in the same format as everything else. Converting it to a large standalone statement on both the About and Homepage will reduce the primary objection (agency accountability) without requiring new copy.

**5. Left-align all body paragraphs currently centered.**
Centering multi-line body copy is the most common CRO anti-pattern on the site. It adds cognitive friction on every paragraph where it appears. This is a CSS change — `text-center` removed from body copy elements — and it eliminates a comprehension penalty on every page it touches.
