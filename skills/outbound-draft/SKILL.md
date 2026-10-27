---
name: outbound-draft
description: Draft a multi-touch outbound sequence (email plus LinkedIn) for one account and persona. Use for 'write outreach to <name> at <company>', 'draft a sequence for this account'.
---

# outbound-draft

**Reads:** the account brief in `outputs/accounts/` (run `account-research` first if missing), the persona file, [voice](../../context/voice.md), `knowledge/customers/`, the matching competitor file if a competitor is in play.
**Writes:** `outputs/outbound/<company>-<persona>.md`.

1. Confirm the account, persona and the one signal that earns the message.
2. Draft 4 touches over about 14 days: email 1 (signal plus outcome plus ask), LinkedIn connect note, email 2 (proof from `knowledge/customers/`), email 3 (a different pillar and a clear close-out). Each email under 100 words.
3. Follow [voice](../../context/voice.md): specific, no banned words, one ask.
4. Use only proof that exists in the knowledge folder. Never invent a customer, metric or quote.
5. Show subject lines, the reasoning for the angle, and a list of personalization facts with sources.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. Do not make a one-off preference a permanent rule without asking.
3. If the user calls the output excellent, save it to `examples/outbound-draft/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
