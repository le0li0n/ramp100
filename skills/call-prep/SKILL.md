---
name: call-prep
description: Prepare a meeting brief for a sales call: who is attending, what we know, discovery questions, likely objections. Use for 'prep me for my call with <company>', 'meeting brief'.
---

# call-prep

**Reads:** account brief in `outputs/accounts/` if it exists, [personas](../../context/personas/), [sales-process](../../context/sales-process.md), competitor files, `knowledge/customers/`.
**Writes:** `outputs/calls/<company>-<date>.md`.

1. Ask for the stage, attendees and any call history. Run a short `account-research` if there is no brief.
2. Output: goal of the call and the exit criteria for the stage; per attendee, persona, likely goals and pains; 5 discovery questions tied to [signals](../../context/signals.md); likely objections with replies from the persona file; proof to cite; next step to ask for.
3. Flag unknowns as questions to ask, not guesses.

## Learn Loop (finish every run with this)
1. Ask the user what they changed or disliked, if present.
2. Record durable lessons in the relevant context file or a note in `knowledge/insights/`. Promote an insight from emerging to validated once two separate sources support it. When the user corrects the output, ask whether it applies to this draft only or is a permanent rule, and write it as a rule only if they say permanent. Put style rules in `context/voice.md`.
3. If the user calls the output excellent, save it to `examples/call-prep/`.
4. Append one line to `knowledge/log.md`: date, skill, what changed.
