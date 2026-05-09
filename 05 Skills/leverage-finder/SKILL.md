---
name: leverage-finder
description: >
  Quickly assess how much of any task Claude can handle before Dave starts doing it manually.
  Use this skill when Dave says "should I do this manually", "is this worth automating", "what's
  the leverage on this", "can you help with this task", "how much of this can AI handle", or when
  about to start any repetitive or research-heavy task. Produces a leverage percentage and a clear
  decision: automate now / assist only / do manually.
---

# Skill: Leverage Finder

Before starting any manual task, run this. The goal is to never spend an hour doing something Claude could handle in 5 minutes — and to avoid wasting time automating something that needs human judgment every time.

---

## Step 1 — Describe the Task

Get a plain-language breakdown of the task:
- What are the inputs?
- What are the steps?
- What does the output look like?
- How often does this come up?

If Dave hasn't described it fully, ask one question to fill the gap.

---

## Step 2 — Apply the Three Questions

1. **Is any part repetitive or rule-based?** → Yes = automation candidate
2. **Has this been done before in a similar form?** → Yes = likely skill-able
3. **Does each instance require fresh human judgment?** → Yes = human stays in the loop, but AI can still assist

---

## Step 3 — Estimate the Leverage Percentage

| % | What it means | Decision |
|---|---------------|----------|
| **0–20%** | Mostly judgment — AI can draft or research, human decides everything | Do manually, use Claude as a sounding board only |
| **20–50%** | Mixed — automate the research/formatting/drafting chunks, human reviews and decides | Identify which specific chunks to hand off |
| **50–80%** | High leverage — build a skill, human does final QC only | Build a skill in `05 Skills/` |
| **80–100%** | Fully automatable — build a skill and schedule it if recurring | Build + schedule |

Give a specific percentage estimate, not just a range. Explain your reasoning briefly.

---

## Step 4 — Identify What to Hand Off

If the leverage is above 20%, break the task into chunks:
- Which specific parts can Claude handle fully?
- Which parts need Dave's eyes or judgment?
- What's the handoff point?

Be concrete. "Claude pulls the data and formats the table, Dave decides whether the numbers justify moving forward" is useful. "Claude assists" is not.

---

## Step 5 — Recommend Next Action

| Leverage | Action |
|----------|--------|
| <20% | Start the task now — use Claude as a prompt assistant if helpful |
| 20–80% | Define the chunks to hand off, start immediately with that split |
| >80% | Run `skill-builder` to make this permanent before doing it again manually |
| >80% + recurring | Run `skill-builder` + flag for scheduling |

---

## Rules

- Give a specific number — "about 60%" is more useful than "high"
- If the task has never been done before, assume lower leverage until patterns emerge
- Recurring tasks get a bias toward building a skill, even at 50%
- Don't recommend automating something Dave only does once — ROI doesn't justify it
