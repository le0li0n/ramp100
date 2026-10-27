---
name: account-research
description: Research one target account and produce a one-page brief with an ICP fit score. Use for 'research <company>', 'is <company> a fit', 'brief me on <company>' before outbound or a call.
---

# account-research

**Reads:** [icp](../../context/icp.md), [signals](../../context/signals.md), [personas](../../context/personas/), [positioning](../../context/positioning.md).
**Writes:** `outputs/accounts/<company>.md`.

1. Get the company name and domain. Research: what they do, size and growth, finance team and leaders, ERP or accounting stack, current card or spend tool, recent news, funding and hires. If Sumble, Clay or Exa are connected, use them; otherwise use web search and page fetch.
2. Score against the rubric in `context/icp.md`. Show points per dimension and the evidence for each.
3. List live [signals](../../context/signals.md) and the play each suggests.
4. Pick the best-fit persona and the one pillar from [positioning](../../context/positioning.md) to lead with.
5. Output: summary, score table, signals, recommended persona and angle, open questions. Tag every fact with its source.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. Do not make a one-off preference a permanent rule without asking.
3. If the user calls the output excellent, save it to `examples/account-research/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
