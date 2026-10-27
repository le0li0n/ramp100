---
name: ingest
description: Turn anything in _inbox (call transcript, doc, email thread, deck) into updates to context/ and knowledge/. Use when the user drops material in _inbox or says 'ingest this', 'add this call to the brain'.
---

# ingest

**Reads:** every file in `_inbox/` (not `_inbox/processed/`), plus the context file each fact belongs in.
**Writes:** updates to `context/` (including `context/competitors/` and `context/personas/`), `knowledge/customers/`, `knowledge/insights/`, and `knowledge/log.md`. Moves source files to `_inbox/processed/`.

1. List the files in `_inbox/`. Read each.
2. For each durable fact (objection, pain in the buyer's words, competitor claim, proof point, process detail), find its one home with a repo search before creating anything.
   `knowledge/customers/` holds proof points about signed customers. A call with a prospect does not get a file there: put what the buyer said in the persona, competitor or signals file it belongs to, and list any deal-specific fact with no home (budget timing, a named deal) in your summary instead of inventing a place for it.
3. Update that file and tag the claim `[source: <file name>]`. If it contradicts an existing claim, keep both, mark the conflict, and tell the user.
4. Add or update a note in `knowledge/insights/` when the same pattern now has a second source.
5. Move processed files to `_inbox/processed/`.
6. Summarize what changed and what you were unsure about.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. When the user corrects the output, ask whether it applies to this draft only or is a permanent rule, and write it as a rule only if they say permanent. Put style rules in `context/voice.md`.
3. If the user calls the output excellent, save it to `examples/ingest/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
