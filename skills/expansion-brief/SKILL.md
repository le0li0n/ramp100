---
name: expansion-brief
description: Build the upgrade case for a self-serve or existing account moving to Plus, an add-on (Procurement, AR) or Enterprise. Use for 'make the case to upgrade <account>' or 'expansion brief'.
---

# expansion-brief `[self-serve]`

**Reads:** [company](../../context/company.md) pricing table, [product-journey](../../context/product-journey.md), [personas](../../context/personas/), the user's usage data on the account.
**Writes:** `outputs/expansion/<company>.md`.

1. Establish current plan, usage, team size and the friction they have shown (feature requests, limits hit).
2. Map each friction to the plan or add-on that removes it, quoting prices only from the pricing table in `context/company.md`.
3. Write a one-page case: what they use today, what is costing them time or money, the recommended upgrade, the proof from `knowledge/customers/`, the ask.
4. Name who should hear it (champion and economic buyer) from the personas.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. Do not make a one-off preference a permanent rule without asking.
3. If the user calls the output excellent, save it to `examples/expansion-brief/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
