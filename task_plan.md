# Task Plan: Lovable Update Prompt — Service Restructure
Date: 2026-03-24

## Goal
Write the single best Lovable update prompt that implements all service and copy changes
from the SOTA research into the Output Marketing website. One prompt. Send once.

## Inputs
- sota_report_b2b_saas_services.md — new service structure + pricing
- sota_report_services_packages.md — previous SOTA (package logic)
- lovable_prompt.md — current site spec (need to read to find all instances to change)

## Phases

### Phase 1: Audit lovable_prompt.md
- [ ] Read full lovable_prompt.md
- [ ] Identify every section that references: services, packages, influencer marketing, Fireflies copy, pricing
- [ ] Log all line numbers / section names in findings.md
- **Status:** in_progress

### Phase 2: Map all changes
- [ ] Map old service names → new service names
- [ ] Map old package names → new (Foundation / Engine / Full Stack)
- [ ] Identify all 4 Fireflies fintech → AI SaaS copy instances
- [ ] Identify influencer marketing mentions to cut vs. keep as credential
- **Status:** pending

### Phase 3: Write the prompt
- [ ] Draft lovable_update_prompt_services.md
- [ ] Apply anti-ai-prose rules
- [ ] Verify completeness against findings
- **Status:** pending

## Decisions
| Decision | Reasoning |
|----------|-----------|
| One prompt, not staged | Services restructure affects multiple pages — do it all at once |
| Keep influencer credentials | Case studies stay; only remove it from services offered |

## Errors
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |

## Status
- [x] Phase 1: Audit lovable_prompt.md — complete
- [x] Phase 2: Map all changes — complete
- [x] Phase 3: Write prompt — complete
- Deliverable: lovable_update_prompt.md (534 lines)
