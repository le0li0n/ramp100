---
name: competitive-update
description: Research a competitor's recent changes (pricing, launches, messaging, news) and update its file in context/competitors/. Use for 'what's new with Brex', 'refresh the Navan file', or before a competitive deal.
---

# competitive-update

**Reads:** `context/competitors/<name>.md`, [positioning](../../context/positioning.md).
**Writes:** the same competitor file; a dated line in `knowledge/log.md`.

1. Read the competitor file. Search the web for changes in the last 90 days: pricing page, launches, funding, leadership, customer wins or losses, review sites. Prefer the competitor's own pages over third-party summaries.
2. Update only sections that changed, keep the headings identical to other competitor files, and tag each claim with its source URL. Mark vendor-biased sources as such.
3. Set "Last checked" to today.
4. Flag anything that should change a talk track or the positioning file, and ask before editing positioning.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. Do not make a one-off preference a permanent rule without asking.
3. If the user calls the output excellent, save it to `examples/competitive-update/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
