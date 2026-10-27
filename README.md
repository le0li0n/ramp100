# Ramp GTM brain

A repo of structured markdown that AI agents (Claude Code, Codex, Cursor) read to do go-to-market work for Ramp without being re-briefed. Built 2026-10-26 from public sources as an exercise; non-public numbers are tagged `[assumption]`.

## Use it
Open this folder in your agent and ask for work: "research <company>", "draft outreach to the Controller at <company>", "prep me for my call". The agent starts at [AGENTS.md](AGENTS.md).

## Add to it
Drop calls, decks and threads in `_inbox/` and run the `ingest` skill. Run `brain-review` weekly.

## Learn it
New to context layers and company brains? Work through the five hands-on exercises in [EXERCISES.md](EXERCISES.md).

## Layout
`context/` stable truth, `knowledge/` what we learn from work, `skills/` repeatable jobs, `examples/` gold outputs, `outputs/` generated work, `_inbox/` raw material.
