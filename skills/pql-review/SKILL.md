---
name: pql-review
description: Rank self-serve (Free or Plus) accounts by product-usage signals and recommend a next action for each. Use for 'which free accounts should sales call', 'review PQLs', or when the user shares a usage export.
---

# pql-review `[self-serve]`

**Reads:** [product-journey](../../context/product-journey.md), [signals](../../context/signals.md), [icp](../../context/icp.md), the user's usage export.
**Writes:** `outputs/pql/<date>.md`.

1. Read the export. Map columns to journey stages (cards issued, active users, accounting connected, spend, add-on requests). Ask for missing columns.
2. Score each account on activation depth, team growth, requests for paid or enterprise features, and [ICP](../../context/icp.md) tier.
3. Recommend one action per account: self-serve nudge, Plus upgrade prompt, or hand to an AE, using the hand-off rule in the journey file. Thresholds there are TODO; say so and use the user's if given.
4. Rank the top 20 with the reason and the suggested first line of outreach.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. When the user corrects the output, ask whether it applies to this draft only or is a permanent rule, and write it as a rule only if they say permanent. Put style rules in `context/voice.md`.
3. If the user calls the output excellent, save it to `examples/pql-review/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
