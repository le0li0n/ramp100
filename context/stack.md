# GTM stack

Which tool is the system of record for what. All rows are `[assumption]` until Ramp's RevOps confirms; replace freely.

| Need | Tool | System of record for |
|---|---|---|
| CRM | TODO: Salesforce? | accounts, contacts, opportunities |
| Sales engagement | TODO | sequences, touches |
| Product usage | TODO | self-serve signups, activation, PQL data |
| Calls | TODO | call transcripts |
| Enrichment | TODO | firmographics, contacts |

## Data sources connected now (this build)
- Built-in web search and page fetch: yes.
- Exa connector: installed but its API key was rejected on 2026-10-26, so it is not used.
- Clay, Sumble, Apollo: available as optional upgrades; see `.env.example`. Skills work without them.
