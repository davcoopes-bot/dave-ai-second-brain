---
name: ai-decision-filter
description: >
  Apply a consistent decision framework before any AI tool or automation choice. Use this skill
  when Dave says "should I use MCP or API for this", "which tool should I use", "is this worth
  integrating", "should I build this or use an existing tool", "what's the right way to connect
  this", or any time a new AI integration or automation approach is being considered. Prevents
  over-engineering and tool lock-in.
---

# Skill: AI Decision Filter

Before committing to any new tool, integration, or automation approach — run this. Most bad AI decisions come from skipping the fundamentals and jumping to the shiny thing.

---

## Rule 1 — Foundation First

**Question:** Have the foundations been built in the right order?
- Context (Claude knows the domain and priorities) → Connections (Claude can reach the data) → Capabilities (skills exist for recurring tasks) → Cadence (things run on schedule)

If a foundation layer is missing, build that before adding anything new. Adding capabilities on top of missing context is wasted effort.

---

## Rule 2 — Tool Agnosticism Test

**Question:** If this tool disappears in 6 months, does the system survive?

- **Yes** → continue
- **No** → decouple the dependency first. Abstract the logic so it could work with another tool. Then go deeper.

Don't build deep integrations into single-vendor tools unless the switching cost is acceptable.

---

## Rule 3 — API vs MCP

**Question:** Does a direct API exist for this tool?

- **Yes** → use the API. It's faster, cheaper on tokens, and gives more control. Document the endpoints used.
- **No** → use an MCP server if one exists, but note which endpoints it wraps so you can replace it later if needed.

MCP is a convenience layer, not a permanent strategy.

---

## Rule 4 — Leverage Check

**Question:** Does this automation save at least 20% of time on a recurring task?

- **Yes** → worth building
- **No** → don't build it yet. The setup cost won't pay back.

Run the `leverage-finder` skill if unsure.

---

## Rule 5 — Skill vs One-Off Prompt

**Question:** Will this process come up more than twice?

- **Yes** → build a skill in `05 Skills/`
- **No** → use a one-off prompt. Don't over-engineer it.

---

## Rule 6 — Failure Recovery

**Question:** If this automation produces wrong output, what's the cost?

- **High cost** (wrong trade decision, wrong product commitment, money on the line) → add a human review step. Claude produces, Dave approves before any action is taken.
- **Low cost** (bad formatting, wrong draft, recoverable output) → ship it and learn from failures. Don't slow down for low-stakes errors.

---

## Output Format

After applying all 6 rules, give Dave:

1. **Recommendation** — what to do and why
2. **Any rules that blocked or changed the direction** — be explicit
3. **Next action** — one specific thing to do now

---

## Rules

- Apply all 6 rules in order — don't skip ahead to the recommendation
- If a rule says "stop", stop. Don't rationalise past it.
- Be blunt about over-engineering — if the right answer is "just use a prompt", say so
