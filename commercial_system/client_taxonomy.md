# Client Taxonomy

## Purpose

This taxonomy gives Output Marketing one consistent client-classification system across outreach, proposals, CRM, and packaging.

## Golden rule

The public offer is still B2B SaaS-first.

Every qualified lead should ideally enter through the `30-Day Pilot`, but the `package_fit` field should reflect the most likely destination after the pilot.

Use `White-Label / Capacity Track` or `Project Track` only when the lead does not map cleanly to `Foundation`, `Engine`, or `Full Stack`.

## Canonical segment definitions

| Segment | client_type | Role in the system | Default fit | Notes |
|---|---|---|---|---|
| `B2B SaaS and AI SaaS` | `software_company` | Core ICP | `High` | Best match across site, pricing, proof, and outreach. |
| `Revenue / Sales / Customer Software` | `software_company` | Core ICP | `High` | Easiest segment for tying content to demos and pipeline. |
| `Workflow / Ops / Automation Software` | `software_company` | Core ICP | `High` or `Medium` | Strong fit when launches, feature rollouts, or technical education are visible. |
| `Analytics / Data / Infrastructure Software` | `software_company` | Core ICP | `High` | Strong fit for technical content, SEO, and measurement-led offers. |
| `Boutique Agency White-Label` | `agency_partner` | Secondary ICP | `Custom` | Real lane, but should not redefine the main public narrative. |
| `B2B Service Business with Active Marketing Motion` | `service_business` | Secondary ICP | `Medium` | Only valid when marketing activity is already visible. |
| `Education / EdTech with Clear Content Motion` | `education_company` | Secondary ICP | `Medium` | Secondary to software, not equal to it. |
| `Selected DTC Brand with Content/Social Need` | `dtc_brand` | Controlled edge case | `Custom` or `Low` | Only when the need is execution support, not influencer-first or paid-first work. |
| `Excluded` | `excluded` | Out of scope | `Exclude` | Staffing, recruiting, media, newsletter, creator-first, enterprise-heavy, or inactive companies. |

## Buyer types

| buyer_type | Use when | Typical titles |
|---|---|---|
| `founder_or_ceo` | Founder-led companies or teams without a marketing hire | Founder, Co-Founder, CEO |
| `head_of_marketing_or_growth` | Lean teams with clear ownership over pipeline or content | Head of Marketing, VP Marketing, Marketing Director, Growth Marketing Manager, Demand Gen Manager |
| `product_marketing_or_content_lead` | Technical products, launches, SEO, or content-led education | Product Marketing Manager, Head of Content, Content Marketing Manager, SEO Manager |
| `marketing_ops_or_revops` | The pain centers on reporting, attribution, or execution systems | Marketing Operations Manager, RevOps Manager |
| `agency_owner_or_ops` | White-label or embedded support scopes | Founder, Agency Owner, Operations Director, Client Services Director |
| `brand_or_social_lead` | Limited DTC edge cases only | Brand Director, Social Media Manager, Content Lead |

## Stage model

| stage_fit | Meaning |
|---|---|
| `Too early / Exclude` | No traction or no visible marketing motion |
| `Seed with no marketing hire` | Founder-led and still building a real content presence |
| `Seed to Series A lean team` | Real GTM motion, still understaffed |
| `Growth-stage lean team` | PMF and visible marketing activity, still needs outside execution |
| `Series A/B content engine` | Ready for distribution, measurement, and a systemized content machine |
| `Agency partner` | White-label or recurring embedded delivery relationship |

## Offer fit

| offer_fit | Definition |
|---|---|
| `High` | Core ICP, reasonable size/geography, and at least one strong buying signal |
| `Medium` | Real fit, but less urgency or less clarity |
| `Custom` | Valid fit, but better sold through `White-Label / Capacity Track` or `Project Track` |
| `Low` | Superficial fit only |
| `Exclude` | Clear mismatch with the agency's positioning |

## Outreach priority

| outreach_priority | Meaning |
|---|---|
| `P1 - First Wave` | High fit, right buyer, and strong urgency signals |
| `P2 - Second Wave` | Good fit with weaker urgency or less evidence |
| `P3 - Monitor` | Keep in view, but do not enrich yet |
| `Exclude` | Do not enrich or contact |

### P1 tie-breakers

- `US`, `Canada`, or `UAE`
- especially `California`, `Texas`, `New York`, or `Massachusetts`
- ideally `10-200` employees
- visible blog, resource center, webinars, case studies, launches, or hiring signals

## Required fields for `clients_master.csv`

| Field | Rule |
|---|---|
| `record_type` | `segment_archetype` or `example_company` |
| `client_name` | Archetype name or example company name |
| `client_type` | Use canonical values only |
| `segment` | Use canonical segment values only |
| `buyer_type` | Use canonical buyer types only |
| `stage_fit` | Use the stage model above |
| `offer_fit` | `High`, `Medium`, `Custom`, `Low`, or `Exclude` |
| `geography_fit` | Ideal or validated geography only |
| `company_size_fit` | Ideal size band, not invented employee counts |
| `buyer_titles` | Semicolon-separated target titles |
| `main_pain` | Main commercial pain |
| `urgency_signals` | Signals that justify outreach or qualification |
| `disqualifiers` | Reasons to downrank or exclude |
| `primary_package_fit` | `Foundation`, `Engine`, `Full Stack`, `White-Label / Capacity Track`, or `Project Track` |
| `secondary_package_fit` | Fallback route |
| `outreach_priority` | `P1 - First Wave`, `P2 - Second Wave`, `P3 - Monitor`, or `Exclude` |
| `source_reference` | Repo source(s) used |
| `notes` | Required whenever the classification is inferred and not validated company by company |

## Classification rules

### Geography

- Ideal: `US`, `Canada`, `UAE`
- Highest priority within the US: `California`, `Texas`, `New York`, `Massachusetts`
- If geography is not validated in the repo, state that in `notes`

### Company size

- Ideal: `10-50`
- Strong: `51-200`
- Acceptable: `201-500` only when the need is especially clear
- Downrank or exclude:
  - `<10` with no traction
  - `1000+` with obvious internal team capacity

### Urgency signals

- active blog or resource center
- active LinkedIn or founder content
- case studies or customer stories
- webinars, demos, or events
- launches, feature announcements, or changelog motion
- hiring for content, SEO, growth, product marketing, or ops
- visible reporting or attribution pain

### Disqualifiers

- no visible marketing motion
- too early and no traction
- enterprise-scale in-house team
- consulting-heavy or implementation-heavy shop
- staffing, recruiting, or talent business
- media, newsletter, or community-led business
- translation or localization company
- creator-economy or influencer-first need
- paid media or video production as the primary pain

## Package assignment rules

| primary_package_fit | Use when | Typical secondary fit |
|---|---|---|
| `Foundation` | Founder-led B2B SaaS with no marketing hire and a basic visibility gap | `Engine` |
| `Engine` | Lean team with PMF or GTM motion that needs recurring organic pipeline support | `Full Stack` |
| `Full Stack` | More mature team that needs distribution, attribution, and a measured content engine | `Engine` |
| `White-Label / Capacity Track` | Agency or partner that needs recurring execution capacity | `Project Track` |
| `Project Track` | Audits, pSEO builds, launch sprints, or adjacent cases not ready for a retainer | `Foundation` or `Engine` |

## Data hygiene rule

Do not invent:

- exact employee counts
- exact HQ location
- exact buyer identity
- exact funding stage

If the classification is based on repo context rather than verified live research, record the assumption in `notes`.
