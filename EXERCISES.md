# Exercises: learning context layers with the Ramp GTM brain

Five short exercises for people new to Claude Code. Each takes 10 to 15 minutes. Do them in order. By the end you will have seen what a context layer is, why it has a map, why every fact lives in one place, how new material gets in, and how the brain learns from your corrections.

The company and call details in these exercises are fictional and exist only to practice with. Do not treat them as real Ramp facts.

## Setup (once)

Work on a throwaway branch so nothing you do changes the real brain. In a terminal, from the repo folder, run `git switch -c practice-yourname`. Then open Claude Code in this folder.

When an exercise says "reset", run `git restore . && git clean -fd` to throw away every change since your last commit.

## Exercise 1: See the difference a context layer makes

**Idea:** the repo is the context layer. It is the material the agent reads before it answers.

**Do:**
1. Open Claude Code in an empty folder (make one anywhere) and ask: "Who is the ideal customer for Ramp's sales team, and how would you score a lead?"
2. Open Claude Code in this repo and ask the exact same question.

**Look for:**
- The first answer is generic and confident. The second quotes tiers, employee ranges and a 0 to 100 rubric.
- Which files did the second session open? Scroll up and find them. Is `context/icp.md` one of them?
- Notice the `[assumption]` tags. The brain admits what it does not know instead of inventing it.

**Discuss:** what did the agent do differently, the model or the files?

## Exercise 2: Follow the map

**Idea:** a context layer needs a front door. Here it is `AGENTS.md`, a table that says "if you need X, read Y".

**Do:** in this repo, ask three questions and, after each answer, ask "which files did you read and why?"
1. "What do we say when a prospect says they already use Brex?"
2. "Which events mean we should reach out to a company?"
3. "What are the stages of a deal?"

**Look for:**
- Each answer comes from one or two files, not a search of everything.
- Open `AGENTS.md` and match each question to its row in the table.
- Ask a fourth question the map does not cover, such as "What is our refund policy for customers?". Does the agent say it does not know, or make something up? Rule 3 in `AGENTS.md` says never invent.

**Discuss:** what would happen if the table did not exist and there were 500 files?

## Exercise 3: One home per fact

**Idea:** rule 1 in `AGENTS.md` says a fact lives in one file and everything else links to it. Change it once and every answer updates.

**Do:**
1. Ask: "Is a company with 150 employees a Tier 1 account?" Note the answer. It should be no, because Tier 1 is 200 to 1,000.
2. Open `context/icp.md` and change the Tier 1 row to "50 to 300 employees". Save.
3. Type `/clear` (so it rereads the file) and ask the same question again. Then ask it to score a made-up company with 100 employees using the `account-research` skill.
4. Reset.

**Look for:**
- The answer flipped without you touching any skill or prompt.
- Your edit made the tiers inconsistent: Tier 3 still says "under 200", so it now overlaps Tier 1, and 300 to 1,000 belongs to no tier. Did the agent notice and say so? A good brain makes this kind of error easy to spot because the range lives in one table.
- Search the repo for the old range: ask "where else does the brain mention the Tier 1 range?" The range should appear only in `context/icp.md`. Other files link to it or only say "Tier 1". Finding no second copy is the right result, and it shows rule 1 working.

**Discuss:** what breaks when the same number is written in five files and you update only one?

## Exercise 4: Feed the brain

**Idea:** a context layer is only useful if new material gets in cleanly. The `ingest` skill turns a raw note into small, sourced updates in the right files.

**Do:**
1. Create `_inbox/acme-freight-call.md` with this text:
   ```
   Call with Dana, Controller at Acme Freight (about 400 employees, trucking).
   She said month-end close takes 9 days because drivers submit paper receipts.
   They use Brex cards today but hate the expense approval flow.
   She also said Brex approvals are fast and she has no complaints about them.
   Budget decision is in Q1. Her CFO cares most about audit trail.
   ```
   The last two lines of the Brex material contradict each other on purpose. The agent should not quietly pick one.
2. Ask Claude: "Ingest what's in _inbox."
3. Read the diff with `git diff` and `git status`.
4. Reset.

**Look for:**
- Which files changed? Expect `context/competitors/brex.md`, `context/personas/controller.md` and `knowledge/log.md`. Acme is a prospect, not a customer, so there should be no new file in `knowledge/customers/` (that folder holds proof points).
- Every new claim should carry `[source: acme-freight-call.md]`.
- The source file should move to `_inbox/processed/`.
- Did it flag the Brex contradiction and keep both claims, as the skill says?
- Did it list anything it was unsure about? Likely candidates are the Q1 budget decision, which has no obvious home, and the 9-day close figure, which has only one source.
- No note appears in `knowledge/insights/`. The skill only promotes a pattern there when a second source supports it.

**Discuss:** why not just paste the whole call into the chat each time?

## Exercise 5: Teach it a preference

**Idea:** the Learn Loop. After each skill runs, the agent asks what you changed or disliked and records durable lessons, but should not turn a one-off whim into a permanent rule without asking.

**Do:**
1. Ask: "Use outbound-draft to write a short email sequence to the Controller at Acme Freight. Skip the account-research step and use these details: about 400 employees, trucking, month-end close takes 9 days, uses Brex today." (`outbound-draft` normally wants a brief in `outputs/accounts/` first, so without this line it will tell you to run `account-research`.)
2. Read the draft. Pick something you dislike. Say, for example: "Don't open with a question. Start with something specific about their business."
3. Notice whether the agent asks if that is a rule for all emails or just this one. If it does not, ask it: "Is that now a permanent rule?" Then answer: "Always, for every email."
4. Check where it was recorded. `context/voice.md` is the best home, but a note in `knowledge/insights/` is also reasonable. Either way there should be a line in `knowledge/log.md`.
5. Start a new session and ask for a sequence to a different company. Is the preference still applied?
6. Reset only if you do not want to keep the change.

**Look for:**
- Did it ask before making your preference permanent?
- Is the lesson stored in one place that you can find and edit, not buried in a chat?
- The skill only says "the relevant context file", so different learners will see different homes. Compare notes. That is a good prompt for deciding where such rules should go.

**Discuss:** how is this different from telling the agent the same thing at the start of every chat?

## If you finish early

- Run the `brain-review` skill after Exercises 3 and 4 (before resetting) and see whether it catches the contradictions you introduced.
- Add a new competitor file in `context/competitors/` for a company you know. Update the `AGENTS.md` table so the agent can find it.
- Find a file that breaks rule 4 (over 150 lines) or rule 3 (a claim without a source).

## For the facilitator

- Keep the order. Exercise 1 creates the "aha", Exercise 3 makes it stick, and Exercise 5 introduces the idea that the brain improves.
- If someone's second session looks identical to the first in Exercise 1, check they actually opened Claude Code inside this folder.
- Remind people to reset. A stray edit to `context/icp.md` will quietly change every later answer.
