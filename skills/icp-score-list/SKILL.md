---
name: icp-score-list
description: Score a CSV of companies against the ICP rubric and rank them. Use when the user gives a list of accounts and asks to prioritize, score or rank them.
---

# icp-score-list

**Reads:** [icp](../../context/icp.md), [signals](../../context/signals.md), the user's CSV.
**Writes:** `outputs/lists/<name>-scored.csv` and a short `.md` summary.

1. Read the CSV. Identify the columns that map to size, industry, geography, stack and any signals. Ask for missing key columns instead of guessing.
2. Score each row on the rubric using only the data present; for missing dimensions score zero and mark `unknown` rather than assuming. Use enrichment connectors for gaps only if the user approves the credit cost.
3. Add columns: total score, band (prioritize now, sequence, nurture or self-serve), top signal, suggested persona.
4. Sort by score. Summarize counts per band and the top 10 with one-line reasons.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. Do not make a one-off preference a permanent rule without asking.
3. If the user calls the output excellent, save it to `examples/icp-score-list/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
