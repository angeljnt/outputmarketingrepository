---
name: upwork-proposal-generator
description: generate, customize, or audit Upwork proposals and Upwork client-message replies for Vanessa or Output Marketing using a fixed proposal structure, a growing knowledge base, and anti-AI prose guardrails. Use when the user wants to draft an Upwork proposal, answer an Upwork lead, keep proposal structure fixed while expanding reusable proof points, or add new agency/Vanessa knowledge without changing the proposal skeleton.
---

# Upwork Proposal Generator

Generate Upwork proposals with a frozen structure and a separate knowledge base. The structure files stay stable. The knowledge base grows.

## Read in this order

1. `references/proposal-rules.md`
2. `knowledge-base/00-index.md`
3. If you need tone calibration from a real proposal, read:
   - `references/real-proposal-calibration.md`
4. The template that matches the request:
   - `assets/templates/standard-full.md`
   - `assets/templates/short.md`
   - `assets/templates/message-response.md`
   - `assets/templates/complex.md`

Then read only the KB files that matter for the job.

## Core rule

Keep the proposal structure intact. Swap substance, not skeleton.

That means:
- keep the section order and role of each section
- keep the CTA simple
- end with one easy-to-answer question
- choose proof points selectively
- do not rewrite template files unless the user explicitly wants to change proposal structure

## Default workflow

1. Read the job post or client message carefully.
2. Identify:
   - desired outcome
   - main pain or risk
   - proposal type
   - strongest relevant proof points
3. Choose the right template.
4. Pull only relevant facts from the KB.
5. Draft inside the template without changing the skeleton.
6. Run the checklist in `references/proposal-rules.md`.

## What to load from the KB

Start with:
- `knowledge-base/profiles/vanessa.md`
- `knowledge-base/profiles/agency.md`
- `knowledge-base/rules/accuracy-guardrails.md`
- `knowledge-base/job-types/playbooks.md`

Then load only the relevant files from:
- `knowledge-base/experience/`
- `knowledge-base/proof-points/`
- `knowledge-base/differentiators/`

Do not bulk-load the whole KB unless the user asks for a full audit or a broader rewrite of the skill.

## Selection rules

- Lead with the client's problem, not Vanessa's biography.
- Use the Webby Award when it strengthens the case.
- Use full URLs in body text without hyperlinking.
- Exception: portfolio and Webby Award may be hyperlinked if the surface supports it.
- Avoid specific percentages unless they are explicitly approved as reusable and real.
- Prefer durable performance language over flashy numbers.
- Change `campaigns` to `content` when that wording is more accurate for the job.
- Keep tone confident, natural, and slightly sharp. Never smug.

## Knowledge-base growth rule

When the user wants to add new experience, proof, or positioning:

1. Do not edit the templates.
2. Add a new KB entry or update the single most relevant KB file.
3. Follow `knowledge-base/00-entry-template.md`.
4. Keep facts verifiable and reusable.
5. Add `use_when` guidance so future proposals can find the entry fast.

## Optional cleanup

If the draft starts sounding synthetic, read:
- `../anti-ai-prose/SKILL.md`
- relevant files in `../anti-ai-prose/references/`

Use that material to clean phrasing, but do not let it change the fixed proposal structure.

## Output expectation

Return the final proposal only unless the user asks for notes, alternatives, or an audit.
