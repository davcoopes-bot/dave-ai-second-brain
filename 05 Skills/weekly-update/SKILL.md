---
name: weekly-update
description: >
  Interview Dave to update all context files across the vault — the root CLAUDE.md, GOALS.md,
  and each project's CLAUDE.md. Use this skill when Dave says "weekly update", "let's do a weekly
  review", "update my vault", "update the context", "keep Claude current", or when the Weekly
  Update section in CLAUDE.md hasn't been updated in a week or more. Also trigger if the last
  updated date in the Weekly Update section is stale. Keeps Claude accurate so every session
  starts from a real map of the world, not a stale one.
---

# Skill: Weekly Update

Interview Dave to update all context files across the vault. The goal is simple: Claude should never start a session working from last week's map when this week's reality is different.

---

## When to Use

- Dave says "weekly update", "let's do a weekly review", "update my vault"
- The Weekly Update section in `CLAUDE.md` hasn't been touched in 7+ days
- A major project status has changed and context is out of date

---

## Phase 1: Scan Current State

Read everything before asking a single question:

```bash
ls -d "03 Projects"/*/ 2>&1 || echo "No projects yet"
```

**Read these files:**
- `CLAUDE.md` — focus on the **Weekly Update** section, **My Goals & Current Progress**, and **My Current Projects & Overviews**
- `GOALS.md` — scan for numbers, dates, or milestones that might need updating
- Each project's `CLAUDE.md` — specifically the **Current Status** section

**What you're building:** A mental map of what was true last time, so you can ask targeted questions about what changed — not make Dave repeat everything from scratch.

---

## Phase 2: Meta-Level Interview

Covers the root CLAUDE.md and GOALS.md. Reference what you read in Phase 1 so Dave knows you're caught up.

### Weekly Pulse

Show Dave what the Weekly Update section currently says (or note it's blank), then ask:

- **What's working right now?**
- **What's not working?**
- **What are you sitting on or need to decide?**
- **What are you feeling pulled toward?**
- **Any deadlines or time-sensitive things coming up?**

These map directly to the five Weekly Update fields. If a field hasn't changed, Dave can say "same" and you keep what was there.

### Goals Check-In

Reference the current state from **My Goals & Current Progress** in CLAUDE.md and anything in GOALS.md. Then ask:

- **Any progress on your main goal since last time?** (New numbers, milestones hit, setbacks)
- **Has the plan changed at all?** (New strategy, dropped something, added something)
- **Anything new on the risk/runway front?**

**Keep this tight.** If nothing changed, move on. Don't make Dave re-justify existing goals every week.

### GOALS.md Specifics

If GOALS.md exists and has trackable items, briefly surface anything that looks like it needs updating:

> "Your GOALS.md shows [X]. Still accurate, or should I update that?"

---

## Phase 3: Project Updates

Walk through **each project folder** found in Phase 1. For each:

1. Show the current status from that project's CLAUDE.md
2. Ask: **"What's the update on [Project Name]? Any status change or progress this week?"**
3. If nothing changed, Dave says "no change" and you move on

**Keep this fast.** One question per project, maybe a quick follow-up if something big happened. This is a check-in, not a deep dive.

---

## Phase 4: Update All Files

After the interview, summarise all changes you're about to make and confirm before writing.

### Root CLAUDE.md — update these sections:

**Weekly Update section:**
```markdown
## Weekly Update

> **Last updated:** [today's date]

- What's working: [from interview]
- What's not working: [from interview]
- What I'm sitting on / need to decide: [from interview]
- What I'm feeling pulled toward: [from interview]
- Any deadlines or time-sensitive things: [from interview]
```

**My Goals & Current Progress** — only update if something actually changed.

**My Current Projects & Overviews** — update the status line and overview for any project whose status changed. Leave unchanged projects alone.

### GOALS.md — update any specific numbers, dates, or milestones Dave called out. Don't restructure it.

### Each project's CLAUDE.md — update the **Current Status** section:

```markdown
## Current Status

> **Last updated:** [today's date]
> **Status:** [updated status]

[Any additional context Dave provided this week]
```

**Critical rule:** Only edit status and progress sections. Never rewrite a project's structure, process, rules, or other sections during a weekly update.

---

## Phase 5: Weekly Review Note (Optional)

After all files are updated, ask:

> "Want me to create a weekly review note in your reviews folder?"

**If yes:** Create a dated note in `04 Reviews/l Weekly Reviews l/` using the interview answers as content. Check if a previous review note exists first — if so, match the format.

**If no:** Skip it. Don't push.

---

## Summary of What Gets Updated

| File | What changes |
|------|-------------|
| Root `CLAUDE.md` → Weekly Update | All five pulse fields + date |
| Root `CLAUDE.md` → Goals & Progress | Only if numbers/plan/risks changed |
| Root `CLAUDE.md` → Projects & Overviews | Status line for changed projects only |
| `GOALS.md` | Any trackable items that changed |
| Each project `CLAUDE.md` → Current Status | Status + date + what happened |
| Weekly review note | Optional — Dave's choice |

---

## Rules

- Scan everything before asking a single question — come in prepared
- If nothing changed on a topic, don't labour it — move on
- Only edit the sections explicitly listed — don't restructure files during a weekly update
- Always confirm the list of changes before writing anything
