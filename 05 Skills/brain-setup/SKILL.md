---
name: brain-setup
description: >
  Set up or refresh the CLAUDE.md context file for a new or existing vault. Use this skill when
  Dave says "set up my vault", "initialise the brain", "refresh CLAUDE.md", "the CLAUDE.md needs
  updating", "set up the context file", or when setting up this system for the first time.
  Interviews Dave in 5 structured rounds and generates a fully personalised CLAUDE.md in his
  own voice. Also use when onboarding a fresh Claude session that has no CLAUDE.md yet.
---

# Skill: Brain Setup

Generate a personalised CLAUDE.md by scanning the vault structure and interviewing the user. The result is a fully populated context file that makes Claude an effective thinking partner for this vault.

---

## When to Use

- User just copied the vault template and needs to set it up
- CLAUDE.md is missing or contains only placeholder text
- User explicitly asks to set up or initialise their vault
- CLAUDE.md exists but is significantly out of date

If a CLAUDE.md already exists with real content, ask the user whether they want to start fresh or build on what's there.

---

## Phase 1: Scan the Vault

Before asking anything, scan the folder structure silently:

```bash
# Top-level folders
ls -d */

# Project subfolders
ls -d "03 Projects"/*/ 2>&1 || echo "No projects yet"
```

Record:
- Which system folders exist (Weekly Reviews, Books, Chess Moves, etc.)
- Which project folders exist under `03 Projects/`
- Whether CLAUDE.md or GOALS.md already exist

Use this to auto-populate the Folder Structure section — don't ask Dave to describe folders you already scanned.

---

## Phase 2: Interview (5 Rounds)

Conduct conversationally. After each round, briefly summarise what you captured so Dave can correct anything before you move on.

**Pacing:** Some rounds list 3–5 sub-questions. Group related ones naturally — fine to ask 4–5 at once if they flow together. If an answer is thin, probe once then move on. Don't interrogate.

---

### Round 1: Who You Are & Your Purpose

Ask:
- **What do you want to call this vault?** (Default: use the vault folder name)
- **What do you do?** Creator, developer, entrepreneur, tradesman — what's the one-liner?
- **What's your purpose?** The thing that drives you, the mission behind the work.
- **What do you love doing?** The activities that energise you — not obligations.
- **What do you refuse to do?** Values, hard lines, things you won't compromise on.
- **Any personal context** that shapes how you work? (family, health goals, life stage, etc.)

**Goal:** Capture their identity in THEIR voice. This should sound like them talking, not a LinkedIn bio.

---

### Round 2: What You Want Claude to Do

Ask:
- **At this top level**, what do you want Claude to help with?
- **What kind of thinking partner** do you need? Strategic planning? Accountability? Brainstorming? Decision-making?
- **What's the prime directive?** If Claude could only do ONE thing well in this vault, what should it be?

**Goal:** Define Claude's role so it knows what's in-scope here vs. what belongs in project-level CLAUDE.md files.

---

### Round 3: Rules & Boundaries

Start with a direct question on communication style:

> "How should Claude communicate with you?"
> - **Blunt and direct** — Challenge me, don't sugarcoat, call me out when I'm wrong
> - **Supportive but honest** — Encourage me, but flag real issues when they matter
> - **Balanced** — Match my energy, be direct when it counts

Then ask open-ended:
- **Any specific rules or pet peeves?** (e.g., "don't give me 10 options when I need one")
- **How should Claude handle files?** (e.g., prefix AI-generated files with `(C)`, ask before editing)
- **Anything Claude should NEVER do** in this vault?

**Defaults if no preference stated:** Use `(C)` prefix on AI-generated files. Don't edit existing files without permission.

**Goal:** Concrete, actionable rules — not vague preferences.

---

### Round 4: Strengths & Weaknesses

Ask:
- **What are you genuinely great at?** Skills, natural talents, unfair advantages.
- **What are your blind spots or recurring failure modes?** The patterns that bite you.
- **What do you default to when stressed or overwhelmed?** (e.g., "I retreat to busy-work")

**Goal:** Honest self-assessment Claude can reference to give better advice. Specific beats generic.

---

### Round 5: Goals & Current Progress

Ask:
- **What's your main goal right now?** Financial target, launch milestone, growth number — make it concrete.
- **Where are you today?** Current income, progress, resources, runway.
- **What's the plan to get there?** Even rough steps.
- **Any risks or time-sensitive factors?** Deadlines, runway limits, dependencies.

**Goal:** Real numbers and timelines wherever possible. Push gently for specifics.

**If the plan is vague:** Write what they gave you. Suggest a Chess Moves session to flesh it out.

---

## Phase 3: Generate CLAUDE.md

After all 5 rounds, assemble the CLAUDE.md. **Write in the user's voice** — mirror their language, don't sanitise it.

```markdown
# [Vault Name] — Claude Context File

[One sentence: what this vault is and who it serves.]

## Who I Am & My Purpose
[From Round 1. 2–3 paragraphs in first person.]

## Claude's Purpose in This Level
[From Round 2. Framing sentence + bulleted responsibilities + prime directive.]

## Claude's Rules & Boundaries
[From Round 3. Bulleted list — bold the key phrase in each bullet.]

## Folder Structure
[Auto-generated from Phase 1 scan. Every system folder and project subfolder with short descriptions.]

## My Strengths & Weaknesses
**Strengths:**
[Bulleted list from Round 4]

**Weaknesses & blind spots:**
[Bulleted list from Round 4]

## My Goals & Current Progress
[From Round 5. Target number/milestone, current state with real numbers, the plan, risks.]

## Weekly Update
> **Last updated:** _[run the weekly-update skill to populate this]_
- What's working:
- What's not working:
- What I'm sitting on / need to decide:
- What I'm feeling pulled toward:
- Any deadlines or time-sensitive things:

## My Current Projects & Overviews
_No projects yet. Use the New Project skill to create your first project._
```

**Critical rules for generation:**
- **Don't fabricate.** Thin answer = thin section. Never pad with assumptions.
- **Use their words.** If they said "I build cool shit", write that. Don't sanitise it.
- **Folder structure is auto-detected.** Don't ask them to describe folders you already scanned.
- **Weekly Update is always a blank template.** Never pre-fill it.

---

## Phase 4: Review & Confirm

Show the full generated CLAUDE.md and ask:

> "Here's your CLAUDE.md — read through it. Anything you want to change, add, or remove before I save it?"

Make targeted edits to flagged sections only. Loop until confirmed. **Only write the file after explicit confirmation.**

---

## Phase 5: Next Steps

After writing, tell the user:

1. **CLAUDE.md is live** — Claude reads it at the start of every session
2. **Run the weekly-update skill** each week to keep Claude current
3. **Create your first project** — use the new-project skill to scaffold a project folder
4. **If goals feel vague** — run a Chess Moves strategic thinking session
5. **First session idea** — try a weekly review or Chess Moves session to break in the setup

---

## Rules

- Never write CLAUDE.md without explicit confirmation in Phase 4
- Don't fabricate answers the user didn't give — leave TODOs instead
- Write in the user's voice, not corporate language
