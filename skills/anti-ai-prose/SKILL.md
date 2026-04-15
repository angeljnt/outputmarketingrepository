---
name: anti-ai-prose
description: rewrite, edit, critique, or generate english prose so it does not read like chatgpt, claude, or gemini output. use when the user asks to humanize a draft, remove ai tone, avoid chatbot phrasing, make writing sound natural, detect llm fingerprints, or produce copy that avoids generic rhetorical scaffolding, hype, filler, and template-driven prose. especially useful for emails, articles, thought leadership, landing pages, sales copy, scripts, and business writing where obvious ai style would reduce trust.
---

# Anti AI Prose

## Overview

Produce English prose that does not read like generic LLM output. Your job is not to make text quirky for its own sake. Your job is to remove recognizable chatbot fingerprints while preserving the user's meaning, audience fit, and intended effect.

Use the references in this skill aggressively. The large inventories live outside this file so you can consult them only when needed.

## Workflow

1. Identify the user's real goal.
   - **Detecting AI fingerprints?** Audit the draft and flag what sounds synthetic.
   - **Rewriting?** Preserve meaning and rewrite for a human cadence.
   - **Generating from scratch?** Draft directly in a non-LLM style rather than generating generic prose and polishing it later.
   - **Building a house style or prompt?** Convert the anti-patterns into explicit instructions.

2. Diagnose risk before rewriting.
   Check for the following high-risk signals:
   - formulaic openers and wrap-ups
   - pseudo-conversational pivots
   - contrast templates
   - inflated abstraction and corporate wording
   - list-heavy structure with frictionless transitions
   - safe hedging and synthetic balance
   - repetitive sentence rhythm
   - idea-thin prose padded with scaffolding

3. Choose the minimum necessary intervention.
   - **Light edit**: remove obvious markers but keep sentence order and structure.
   - **Substantive rewrite**: change syntax, rhythm, sequence, and emphasis.
   - **Full recast**: rebuild the passage from the underlying meaning instead of line editing.

4. Rewrite toward human prose.
   Prefer:
   - concrete nouns and verbs over abstractions
   - point-first writing over suspense framing
   - asymmetry and selective roughness over polished sameness
   - varied sentence lengths and natural emphasis over uniform cadence
   - direct claims over ritual transitions
   - specifics, tradeoffs, and point of view over generic balance

5. Verify against the anti-pattern inventory.
   Before finalizing, scan the output against these references:
   - `references/rhetorical-templates.md`
   - `references/lexicon-and-collocations.md`
   - `references/structural-fingerprints.md`
   - `references/rewrite-playbook.md`

6. Return the clean output the user asked for.
   Only add commentary when the user asks for diagnosis, explanation, or examples.

## Core Operating Rules

- Do not merely swap one cliché for another.
- Do not preserve template scaffolding out of politeness.
- Do not add fake intrigue, fake balance, fake depth, or empty “insight” framing.
- Do not smooth the text so much that it becomes bloodless corporate mush.
- Do not overcorrect into slang, eccentricity, or performative roughness.
- Keep the user's meaning, audience, and strategic intent intact.
- When the user asks for “human,” optimize for believability, not eccentricity.

## What to Remove First

Remove these first because they are strong LLM tells:
- “here’s the thing” type pivots
- “the real question is” type framing
- “it’s not about x, it’s about y” contrasts
- “let’s break this down” scaffolding
- “in today’s fast-paced world” style openers
- “at its core / ultimately / in essence” pseudo-depth markers
- “it’s worth noting / important to note” hedges
- inflated lexicon such as “delve,” “tapestry,” “landscape,” “realm,” “leverage,” “unlock,” “robust,” “seamless,” “transformative” when they add no precision

## Output Modes

### 1. Direct rewrite
Default when the user pastes text and wants a better version.
Return the rewritten text only unless they ask for notes.

### 2. Audit
When the user asks what sounds AI-generated, use this structure:
- `high-risk markers`
- `why they sound synthetic`
- `better direction`

### 3. Pattern inventory
When the user asks for examples, taxonomies, or exhaustive lists, provide them by category, and consult the reference files for maximal coverage.
Be honest that literal exhaustiveness is impossible because templates are productive. Still aim for maximal practical coverage.

### 4. Prompt building
When the user wants a reusable instruction set, convert the rules into imperative constraints. Include explicit bans, positive replacements, and a self-check routine.

## Strong Default Rewriting Moves

Use these moves repeatedly:
- cut the opener and begin where the substance starts
- collapse two-stage sentences into one clear claim
- replace abstract nouns with concrete actors or actions
- remove mirrored contrast structures
- delete throat-clearing transitions
- fuse short bullets into a tighter paragraph when the bullets are just scaffolding
- split dense generic paragraphs when one concrete point deserves its own line
- replace generic summary lines with a sharper last sentence or remove them entirely

## Negative Example

Avoid output like:
- “In today’s fast-paced world, it’s important to recognize that AI is transforming the way businesses operate.”

Prefer output like:
- “AI is changing how businesses work, but the change is uneven. Some tasks speed up. Others just get dressed up in new software.”

## Reference Guide

Open these files when relevant:
- `references/rhetorical-templates.md` for rhetorical templates and phrase families that make prose sound like ChatGPT, Claude, or Gemini.
- `references/lexicon-and-collocations.md` for high-risk words, collocations, metaphors, and stock adjective patterns.
- `references/structural-fingerprints.md` for paragraph-level, rhythm-level, and discourse-level LLM fingerprints.
- `references/rewrite-playbook.md` for rewrite procedures, checklists, and transformation patterns.
