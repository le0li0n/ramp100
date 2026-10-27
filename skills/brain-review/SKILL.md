---
name: brain-review
description: Weekly health check of this repo: find stale files, TODOs, broken links, orphaned notes, duplicated facts and contradictions, then propose fixes. Use for 'review the brain', 'health check', or on a weekly schedule.
---

# brain-review

**Reads:** the whole repo.
**Writes:** `outputs/brain-review/YYYY-MM-DD.md`; fixes only after the user approves.

Check:
1. **Broken links:** every relative markdown link resolves.
2. **TODOs:** list all `TODO:` markers by file, most important first.
3. **Orphans:** files not linked from AGENTS.md or another file within three hops.
4. **Duplicates and contradictions:** the same fact in two files, or two files disagreeing. Facts have one home.
5. **Stale:** competitor files whose "Last checked" is over 90 days old; context files not touched in a quarter.
6. **Unsourced claims:** claims with no `[source]`, `[stated by user]` or `[assumption]` tag.
7. **Length:** files over 150 lines.

Write the report with a fix proposal for each finding. Apply mechanical fixes (links, tags) once approved.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. Do not make a one-off preference a permanent rule without asking.
3. If the user calls the output excellent, save it to `examples/brain-review/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
