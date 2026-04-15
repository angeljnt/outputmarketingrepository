# SOTA Findings: CRO Typography and Text Formatting for Conversion
Date: 2026-03-24
Topic: What text formatting, sizing, emphasis, and layout decisions maximize engagement and conversion on marketing websites

> 2-Action Rule: Write findings after every 2 searches.

---

## Pilar 1 — Articulos Cientificos / Eye Tracking / Readability Research

### Eye tracking: F-pattern and Z-pattern (Nielsen Norman Group)
- **F-pattern**: Most common on text-heavy pages. Users read horizontally across the top, then a shorter horizontal movement lower, then scan vertically down the left side. Result: left column and first two words of every line are the most-read zones.
- **Z-pattern**: Dominant on pages with little text / landing pages. Eye travels top-left → top-right → diagonal to bottom-left → bottom-right. CTAs placed at bottom-right of Z-sections get the most natural attention.
- **Application**: First words of every line carry disproportionate weight. Bold/large text at line starts gets seen even when users don't read. Key phrases need to be front-loaded, not buried mid-sentence.
- Source: Nielsen Norman Group — F-Shaped Pattern of Reading Web Content (original + 2017 update)

### Multiple scanning patterns beyond F and Z (NN/G 2017 eyetracking update)
- NN/G identified several additional patterns: layer cake, spotted, marking, bypassing, commitment
- "Commitment" pattern: user reads every word — only triggered by highly relevant content
- "Spotted" pattern: users skip to specific words/numbers they're hunting for
- **Key insight**: Bold text and numbers are "spotted" even during skimming — they act as visual anchors

### Font size + readability → conversion
- 16px is the established web standard for body text; matches 11-12pt print comfort zone
- Typography optimization alone increases conversion rates by 15-40% (multiple practitioners)
- One documented case: font size change from 10px → 13px measurably improved conversions
- Easier-to-read fonts increase trust by up to 40%
- Appropriate font choices increase conversion rates by up to 35%
- Source: CXL — "How Typography Affects Conversions and UX"

### Readability score → conversion (Portent empirical study, 2021)
- Plotted Flesch Reading Ease score against conversion rate across multiple sites
- R² = 0.114 — readability explains ~11% of conversion rate variance (statistically significant, not dominant)
- Optimal Flesch score for marketing sites: 60–90 (6th–8th grade reading level)
- **Implication**: Lower sentence complexity + shorter words = measurable conversion lift

### Visual hierarchy + conversion
- Stronger visual hierarchy (clear size differentiation between H1/H2/H3/body) guides users toward CTA
- Headline must be readable at a glance — visible size AND weight difference from subheading and body
- Visual hierarchy optimizations on landing pages show significant conversion improvements in A/B tests
- Source: abmatic.ai, IxDF, CXL

### Line spacing effect on reading
- Line spacing of 1.5–2.0x improves reading speed and comprehension
- 2.5x spacing shows best results for low-vision users
- 25% reduction in reading fatigue with proper spacing
- Source: ResearchGate "Make It Big!" study

### Typography trust signals
- Clean, readable fonts communicate competence and reliability — formed within seconds
- Geometric sans-serifs: +41% trust scores vs decorative fonts (fintech study)
- Font legibility > font personality for conversion pages
- Source: dot2shape.com, developerux.com

---

## Pilar 2 — Estandares Internacionales

### (to fill in Fase 2)

---

## Pilar 3 — Reportes de la Industria

### (to fill in Fase 3)

---

## Pilar 4 — Mejores Practicas

### (to fill in Fase 4)

---

## Pilar 5 — Opiniones de Expertos

### (to fill in Fase 5)

---

## Fuentes consultadas (Pilar 1)
- https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/
- https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/
- https://cxl.com/blog/the-effects-of-typography-on-user-experience-conversions/
- https://portent.com/blog/cro/study-the-readability-of-your-website-is-affecting-your-conversion-rates.htm
- https://www.researchgate.net/publication/301935601_Make_It_Big_The_Effect_of_Font_Size_and_Line_Spacing_on_Online_Readability
- https://abmatic.ai/blog/impact-of-visual-hierarchy-on-landing-page-conversion
- https://abmatic.ai/blog/impact-of-website-font-size-on-conversion-rate

---

## Pilar 2 — Estandares Internacionales (WCAG)

### WCAG 2.1 / 2.2 Typography Standards (W3C)
| Estandar | Organismo | Requisito | Implicacion para diseno |
|----------|-----------|-----------|------------------------|
| WCAG 2.1 SC 1.4.12 Text Spacing (AA) | W3C | Line height >= 1.5x font size; paragraph spacing >= 2x font size; letter spacing >= 0.12x; word spacing >= 0.16x | These are minimums — best-converting sites exceed them |
| WCAG 2.1 SC 1.4.4 Resize Text | W3C | Text resizable to 200% without loss of content | Use em/rem not px for sizing |
| WCAG 2.1 SC 1.4.3 Contrast (AA) | W3C | Normal text: 4.5:1 minimum; Large text (18pt/14pt bold): 3:1 minimum | Key constraint for emphasis color choices |
| WCAG 2.1 SC 1.4.6 Contrast Enhanced (AAA) | W3C | 7:1 for normal text; 4.5:1 for large text | Premium standard |

### Minimum font sizes (WCAG-aligned practice, not strict mandate)
- AA compliance: minimum 12px (normal text); 16px recommended
- AAA compliance: minimum 18px (normal text)
- Industry consensus: 16px body text is the baseline; 18-20px is preferred on marketing sites
- Line length: under 80 characters per line for readability

### Scroll behavior standard (industry finding, not formal standard)
- Nielsen Norman Group: users spend 57% of time above the fold
- Critical content placed below 30% scroll depth gets seen by <50% of visitors
- **Implication**: Key credibility phrases, stats, and CTAs must appear in the first screenful or the second, not later

### Fuentes Pilar 2
- https://www.w3.org/TR/WCAG21/
- https://dequeuniversity.com/resources/wcag2.1/1.4.12-text-spacing
- https://font-converters.com/accessibility/font-size-requirements
- https://robustbranding.com/ultimate-guide-wcag-typography-testing/

---

## Pilar 3 — Reportes de la Industria

### Heatmap data: scroll behavior and content engagement
- Users spend 57% of viewing time above the fold (NN/G)
- Scroll heatmaps show where engagement drops: typically at 30-40% page depth for generic pages
- Only 40% of users reach a CTA placed in the lower third of a page (common finding)
- Revenue heatmaps show: users who reach specific content sections before converting — identifies the "money content"
- 2.5x conversion lift documented from CRO changes guided by heatmap analysis (skymooninfotech case study)

### Fuentes Pilar 3 (partial — more to add)
- https://www.leadpages.com/blog/heatmap-analysis-for-cro
- https://www.heatmap.com/blog/heatmap-analysis
- https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/

---

## Pilar 4 — Mejores Practicas (updated)

### Text alignment: when to center, when to left-align
| Situation | Rule | Reason |
|-----------|------|--------|
| Body copy / paragraphs | LEFT align always | Ragged left edge forces brain to search for line start — increases cognitive load, reduces comprehension |
| Hero headlines (1-2 lines) | CENTER or LEFT (test) | Centering a short headline sets it apart; acceptable when the line is short enough to read in one pass |
| Section headers | CENTER acceptable | Short enough that centering is readable; signals a new topic |
| Subheadings inside body | LEFT align | Part of reading flow |
| CTAs / buttons | CENTER for standalone CTA sections | Draws eye to action; full-width on mobile |
| Overlines / labels | CENTER acceptable | Short (1-5 words), sets context |
| Long testimonials | LEFT align | Must be readable; centered multi-line text fails |
| Pull quotes (1-2 sentences) | CENTER acceptable | Short + isolated; centering adds emphasis |
| Statistics / metric blocks | CENTER | Single number or data point; centering creates visual anchor |

**Rule of thumb**: Never center text longer than 2 lines in body copy. Center only what can be consumed in a single visual fixation.

### Bold text: what to emphasize and what not to
**Bold for:**
- Specific outcomes: "7 brands to waitlist" — the number and the outcome
- Constraints that reduce risk: "No retainer. No contract." — exactly these phrases
- Names and credentials (on credential pages)
- Key differentiators in a competitive claim
- CTA text (inherent — all CTAs should be bold weight)
- The single most important word or phrase in a section (one per paragraph maximum)

**Do NOT bold:**
- Entire sentences or paragraphs (destroys the signaling effect)
- Adjectives without specifics ("proven," "best," "exceptional")
- Features rather than outcomes
- Random words for visual texture

**Evidence**: If everything is highlighted, nothing stands out. Bold = scarcity principle applied to text.

### Pull quotes and callout blocks
- Pull quotes: short excerpt (1-3 sentences) pulled from body copy and visually isolated in larger text
- Purpose: give skimmers the gist; reward readers with emphasis; slow down scrollers
- Best content for pull quotes: the ONE sentence that summarizes why someone should buy
- Best content for callout blocks: risk-reducers ("No retainer. No contract."), social proof stats, damaging admissions
- Dark sections (standalone): 70-80% of page is light; dark sections used to highlight specific content the viewer must not miss
- Rule: use dark sections for 1-2 moments per page maximum — overuse kills the emphasis effect

### Standalone sections: what they do and when to use them
**Function**: Visual interruption forces attention reset — reader's eye "wakes up" after a dark/contrast section
**Use for**:
1. The single most important CRO statement on the page (the "why act now" moment)
2. Risk reducers immediately before or after CTA ("No retainer. No contract.")
3. Credibility/social proof (a stat or testimonial that earns trust)
4. Section transition between problem and solution

**Do NOT use for**: Multiple messages in one dark section (pick ONE), pure decoration, repetitive use (more than 2 per page = no impact)

### Typographic scale and size hierarchy
- Display/Hero (H1): 56-72px — one per page, one idea only
- Section header (H2): 36-44px — signals new major topic
- Card header (H3): 20-24px — within a section
- Body large: 18-20px — for intro paragraphs or emphasis contexts
- Body regular: 16-18px — minimum for paragraph text
- Caption/label: 12-14px — only for supporting info (dates, categories, overlines)
- Rule: each level should be visually obvious — a reader should never confuse H2 with H3

### Overlines (small labels above headlines)
- 10-13px, uppercase, wider letter spacing (0.1-0.15em), muted color
- Function: context-setter — tells reader what category/topic before they read the headline
- CRO value: primes the reader's mental model → headline lands harder
- Example: "The work" above a case studies header — filters in/out the right reader

### What gets seen vs what gets skipped (F-pattern applied)
| Position | Gets seen? | What to put there |
|----------|------------|-------------------|
| First 2 words of a line | Always | Key term, benefit, or differentiator |
| Line ends | Often skipped | Supporting detail, not the key point |
| Subheadings | Almost always scanned | Make them self-sufficient — reader should understand the section from subheadings alone |
| First sentence of paragraph | High probability | Lead with the claim — do not bury the lede |
| Last sentence of paragraph | Lower probability | Summary or transition — important but not primary |
| Numbers / bold text anywhere | Very high — "spotted" pattern | Stats, metrics, key phrases — these are fixation magnets |
| Below the fold (>50% scroll) | Seen by ~50% of users | Do not put the primary CTA only here |

### Font sizing rules for marketing pages (CRO-optimized, not just accessible)
| Element | Desktop | Mobile | Notes |
|---------|---------|--------|-------|
| Hero headline | 56-72px | 36-44px | Must read in one pass, above fold |
| Section header | 36-44px | 24-32px | Visible during scroll scan |
| Card / item header | 20-24px | 18-22px | |
| Body text | 17-20px | 16-18px | Go above minimum for trust signal |
| Overline / label | 11-13px | 11-12px | |
| Footer / caption | 13-14px | 12-13px | |

**Note**: Going to 18-20px body text (above WCAG minimum) increases perceived professionalism and trust. Several practitioners report lift from this change alone.

### Anti-patterns (what kills conversion through poor text formatting)
| Anti-pattern | What it does to conversion |
|-------------|--------------------------|
| Walls of body text with no visual breaks | Skimmers bounce — they never reach the CTA |
| Centering long body paragraphs | Increases cognitive load; reduces comprehension |
| Bolding random phrases | Destroys bold's ability to signal what matters |
| More than 2 dark/callout sections per page | Desensitization — each one loses impact |
| Hero headline too small (< 36px) | Fails the "read in one pass" test above the fold |
| Body text < 16px | Trust penalty; accessibility failure |
| No overlines on sections | Reader has no context before reading the headline |
| CTA placed only below 50% scroll | Seen by less than half of visitors |
| Multiple CTAs competing at the same visual weight | Paralysis — user doesn't know what to do |
| No whitespace between sections | Sections bleed together; hierarchy collapses |

### Fuentes Pilar 4
- https://cxl.com/blog/how-to-build-a-high-converting-landing-page/
- https://unbounce.com/conversion-rate-optimization/cro-best-practices/
- https://www.leadfeeder.com/blog/landing-pages-convert/
- https://guppyfishweb.com/web-design/text-alignment-center/
- https://www.subframe.com/tips/callout-section-design-examples
- https://studio1design.com/2024-website-design-trends-conversion-killers/
- https://folwell.umn.edu/typography/pull-quotes-and-block-quotes

---

## Pilar 5 — Opiniones de Expertos

### Joanna Wiebe (Copyhackers — the foundational CRO copywriter)
- **Front-loading principle**: Most important information comes FIRST in every line, paragraph, and section. Never bury the key claim.
- **Eye-path awareness**: When scanning the left 2 inches of any page, you should see the critical information. Structure copy so the left-edge scan tells the full story.
- **Centered headlines**: When controlling line breaks on a centered headline, ensure the first 2 words of line 1 AND line 2 are the most important words. Don't let a filler word anchor a line.
- **Emphasis philosophy**: Strategic, sparing. Bold what earns bold — not what sounds good.

### Peep Laja / CXL (leading CRO training institute)
- Strong visual hierarchy is one of the most consistently validated principles in CRO — confirmed across thousands of A/B tests
- Every page should have 1-2 clearly defined "most wanted actions" — everything else is noise that should be visually subordinated
- Headlines: bold typography, placed prominently above the fold — non-negotiable
- Visuals processed 50x faster than words — images of people + large text numbers are processed before any body copy is read
- Landing page case study: 79.3% conversion improvement from CXL — included visual hierarchy as a key lever

### Nielsen Norman Group (leading UX research institution)
- Users read at most 20-28% of text on an average page — design for skimmers first, readers second
- Optimal line length: 50-75 characters per line (including spaces)
- 16px is the minimum body text — NN/G confirms larger sizes improve both legibility and user satisfaction
- "Glanceable reading" study: bigger IS better for key information — especially for numbers, headlines, and CTAs
- Legibility, readability, and comprehension are distinct: a font can be legible (identifiable) but still low-readability (hard to read continuously)

### Consensus del campo (CRO practitioners, 2024)
- **Formatting for skimmers is the default**: Body copy is written for readers, but layout + formatting must serve skimmers — they are the majority
- **Social proof near CTAs**: Testimonials placed immediately before or after CTAs improve conversion — "35.6% increase in sales" documented from proximity placement
- **Specific > vague in testimonials**: "7 brands added to waitlist" formats better than "great results" — specificity is the emphasis
- **Quote size matters**: Featured testimonials (large, pulled out) convert better than inline text — same principle as pull quotes
- **Numbers as anchors**: Any metric (7,363 impressions; $1,500; 2.45%) should be visually distinct — they're "spotted" during skimming and anchor the rest of the message

### Debates activos
- **Centered vs left hero copy**: Some CRO practitioners prefer left-aligned hero copy for two-column layouts (copy left, image right); others center for single-column landing pages. No universal answer — test for context.
- **How many section breaks per page**: Some practitioners use dark sections liberally; others cap at 2. Consensus leans toward restraint.
- **Bold on testimonials**: Some argue bold within testimonials is noise; others say highlighting the specific metric ("7 brands to waitlist") inside a quote increases credibility. Evidence favors highlighting specific metrics.

### Fuentes Pilar 5
- https://copyhackers.com/3-essential-copy-techniques/
- https://copyhackers.com/2012/09/headline-formulas-and-the-science-of-high-converting-copywriting/
- https://cxl.com/blog/how-to-build-a-high-converting-landing-page/
- https://cxl.com/blog/case-study-how-we-improved-landing-page-conversion/
- https://www.nngroup.com/articles/glanceable-fonts/
- https://www.nngroup.com/articles/legibility-readability-comprehension/
- https://vwo.com/blog/testimonials-improve-conversion-rate/
- https://boast.io/how-to-increase-landing-page-conversion-rates-with-testimonials/
