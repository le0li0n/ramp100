# AGENTS.md: Ramp GTM brain

Ramp is a finance platform (corporate cards, expenses, bill pay, procurement, accounting automation, travel, banking) with AI agents for finance work. This brain serves Ramp's own GTM team.

**GTM model:** B2B sales-led (primary) plus a self-serve SMB funnel (secondary). Details in [company](context/company.md).

## If you need X, read Y

| Need | Read |
|---|---|
| What Ramp does, pricing | [context/company.md](context/company.md) |
| How we describe ourselves | [context/positioning.md](context/positioning.md) |
| Tone, banned words, examples | [context/voice.md](context/voice.md) |
| Who to target, how to score | [context/icp.md](context/icp.md) |
| Who we talk to | [context/personas/](context/personas/) |
| When to reach out and why | [context/signals.md](context/signals.md) |
| Deal stages | [context/sales-process.md](context/sales-process.md) |
| Self-serve funnel and hand-off | [context/product-journey.md](context/product-journey.md) |
| Competitor talk tracks | [context/competitors/](context/competitors/) |
| Proof points and customers | [knowledge/customers/](knowledge/customers/) |
| Patterns learned from work | [knowledge/insights/](knowledge/insights/) |
| Tools and systems of record | [context/stack.md](context/stack.md) |
| This quarter's goals | [context/priorities.md](context/priorities.md) |

## Rules
1. **One home per fact.** Link to it; do not restate it.
2. **Check before you create.** Search the repo first.
3. **Source everything.** Tag `[source: <url or file>]`, `[stated by user]` or `[assumption]`. Never invent customers, metrics, quotes or pricing; leave `TODO:`.
4. **Keep files under 150 lines.**
5. **Plain language.** Write for a new GTM hire on day one.
6. Numbers marked `[assumption]` are placeholders from the build exercise. Do not present them to customers.

## Skills

| Skill | Use when |
|---|---|
| [ingest](skills/ingest/SKILL.md) | New material in `_inbox/` |
| [competitive-update](skills/competitive-update/SKILL.md) | Refreshing a competitor file |
| [content-draft](skills/content-draft/SKILL.md) | Writing a post, email or outline |
| [brain-review](skills/brain-review/SKILL.md) | Weekly health check |
| [account-research](skills/account-research/SKILL.md) | Brief and fit score for one account |
| [icp-score-list](skills/icp-score-list/SKILL.md) | Scoring a CSV of accounts |
| [outbound-draft](skills/outbound-draft/SKILL.md) | Multi-touch sequence for one account |
| [call-prep](skills/call-prep/SKILL.md) | Before a sales call |
| [pql-review](skills/pql-review/SKILL.md) | Ranking self-serve accounts by usage |
| [expansion-brief](skills/expansion-brief/SKILL.md) | Upgrade case for a self-serve account |

The generic Developer/PLG skills `dev-content` and `community-monitor` were left out: Ramp's buyer is finance, not developers.

## Learn Loop
After producing output, every skill: (1) asks what the user changed or disliked; (2) records durable lessons in the relevant file or `knowledge/insights/` (emerging, then validated at two sources), never a one-off preference as a rule without asking; (3) saves approved excellent output to `examples/<skill>/`; (4) appends a line to [knowledge/log.md](knowledge/log.md).
