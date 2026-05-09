---
name: automation-opportunity-finder
description: >
  Systematically surface what's worth automating next in Dave's workflow. Use this skill when Dave says
  "what should I automate next", "what's the highest-leverage thing to build", "help me figure out what
  to systemise", "what skill should I build next", "I feel like I'm doing too much manually", or during
  any monthly AIOS review. Produces a ranked list of automation candidates with a clear recommended
  first build.
---

# Skill: Automation Opportunity Finder

Stop guessing what to build next. Run this to systematically find the highest-leverage automation sitting right in front of you.

---

## Step 1 — Answer the 5 Questions

Walk Dave through these. Get real answers, not vague ones.

1. What have you done 3+ times this week?
2. What felt manual, boring, or copy-paste?
3. What could a smart assistant handle if you spent 15 minutes briefing them upfront?
4. If 10× more volume hit tomorrow — more products to research, more trades to track, more admin — what breaks first?
5. What would generate 10× output if it ran on autopilot?

---

## Step 2 — Classify Each Answer

For each item identified, tag it:

| Type | What it means |
|------|--------------|
| **Context gap** | Claude doesn't know enough about this domain to help well |
| **Skill gap** | Claude lacks a repeatable SOP for this task |
| **Connection gap** | Claude can't reach the relevant tool or data |
| **Cadence gap** | Claude could do this on a schedule but isn't |

---

## Step 3 — Score Each Candidate

Rate each item on three factors (1–3 each):

| Factor | 1 | 2 | 3 |
|--------|---|---|---|
| **Frequency** | Rarely (monthly) | Sometimes (weekly) | Often (daily) |
| **Time cost** | <15 min | 15–60 min | >1 hour |
| **Repeatability** | Highly variable | Mostly consistent | Near-identical every time |

**Score = Frequency × Time × Repeatability** (max 27)

Sort descending. The top item is what to build next.

---

## Step 4 — Recommend and Explain

Present the top 3 candidates in order with scores. For the top item, explain:
- Why it scored highest
- What building it would actually save in time/effort
- What type of gap it is and how to close it

---

## Step 5 — Identify the Build Path

Based on the gap type of the winning candidate:

- **Skill gap** → run the `skill-builder` skill to create `05 Skills/[name]/SKILL.md`
- **Context gap** → update the relevant wiki page in `06 Wiki/wiki/` or add context to `CLAUDE.md`
- **Connection gap** → run the `tool-connection-setup` skill
- **Cadence gap** → set up a scheduled trigger or recurring reminder

---

## Step 6 — Log It

Append to `06 Wiki/system/log.md`:

```
## [YYYY-MM-DD] | Automation Review
- Top candidate: [name]
- Score: [X/27]
- Gap type: [type]
- Next action: [what's being built or connected]
```

---

## Rules

- Don't let Dave pick based on what's interesting — pick based on score
- Frequency beats cleverness every time
- If two items score the same, pick the one with higher repeatability — that's the safer build
- End with one clear next action, not a menu of options
