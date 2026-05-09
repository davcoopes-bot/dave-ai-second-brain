---
name: skill-builder
description: >
  Convert any repeatable process into a proper vault skill file. Use this skill when Dave says
  "build a skill for this", "turn this into a skill", "make this repeatable", "create a skill file",
  "save this as a skill", or any time a process has been done manually more than twice and deserves
  a permanent home. Output is a ready-to-use SKILL.md filed under 05 Skills/.
---

# Skill: Skill Builder

Turn any repeatable process into a permanent, reusable skill. The goal is compounding capability — every skill built means you never have to re-explain that process again.

---

## Step 1 — Define the Process

Before writing anything, clarify:
- **What triggers this skill?** What does Dave say or do that kicks it off?
- **What inputs does it need?** What does Claude need to know to run it?
- **What does it do step by step?** Walk through the full process.
- **What does the output look like?** Be specific — a file, a table, a decision, a plan?
- **What are the common failure points?** Where does this typically go wrong?

If any of these are unclear, ask one targeted question before proceeding.

---

## Step 2 — Identify Where It Lives

Determine the correct folder under `05 Skills/`:
- FBA-specific skills → `05 Skills/FBA/`
- General vault skills → `05 Skills/[skill-name]/`
- Check what already exists before creating a new folder

---

## Step 3 — Write the SKILL.md

Create `05 Skills/[skill-name]/SKILL.md` using this structure:

```markdown
---
name: [skill-name]
description: >
  [When to trigger this skill. Include the exact phrases Dave might say.
  Be specific enough that Claude auto-detects when to use it.]
---

# Skill: [Name]

[One sentence on what this skill does and why it exists.]

---

## Step 1 — [First action]
[Detail]

## Step 2 — [Next action]
[Detail]

[Continue for all steps...]

---

## Rules
- [Any non-negotiables for this skill]
- [Common mistakes to avoid]
```

---

## Step 4 — Test It

Run the skill immediately with a real or realistic input. Ask:
- Did the output match what was expected?
- Were any steps unclear or skipped?
- Is the trigger description specific enough that Claude would auto-detect it?

If anything is off, fix the SKILL.md before calling it done.

---

## Step 5 — Log It

Append to `06 Wiki/system/log.md`:

```
## [YYYY-MM-DD] | Skill Created — [skill-name]
- Location: 05 Skills/[skill-name]/SKILL.md
- Purpose: [one line]
- Trigger phrases: [list]
```

---

## Rules

- Skills live in `05 Skills/` — never anywhere else
- Every skill needs explicit trigger phrases in the frontmatter description
- Don't over-engineer — if it can be done in 3 steps, don't write 8
- The test run is not optional — an untested skill is just a hope
- AI-generated skill files get the `(C)` prefix only if Dave didn't write the process himself
