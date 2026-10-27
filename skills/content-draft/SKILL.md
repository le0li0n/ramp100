---
name: content-draft
description: Draft a LinkedIn post, email or blog outline in Ramp's voice from an insight in knowledge/. Use for 'write a post about X', 'turn this insight into content'.
---

# content-draft

**Reads:** [voice](../../context/voice.md), the chosen note in `knowledge/insights/` and any `knowledge/customers/` proof it cites, [positioning](../../context/positioning.md).
**Writes:** `outputs/content/YYYY-MM-DD-<slug>.md`.

1. Pick the insight or ask which one. Use only validated or clearly labeled emerging insights.
2. Draft in the voice file's tone, avoiding its banned words. Lead with the outcome and a sourced number.
3. Use proof only from `knowledge/customers/`. Never invent a customer, quote or metric.
4. Give two hook options and one body. List the sources used under the draft.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. When the user corrects the output, ask whether it applies to this draft only or is a permanent rule, and write it as a rule only if they say permanent. Put style rules in `context/voice.md`.
3. If the user calls the output excellent, save it to `examples/content-draft/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
