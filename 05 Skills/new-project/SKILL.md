---
name: new-project
description: >
  Create a new project folder inside 03 Projects/ with full scaffolding — folder structure,
  CLAUDE.md, and COMMANDS.md. Use this skill when Dave says "create a new project", "set up a
  project for X", "new project", "start a project folder", "I want to track X as a project",
  or any time a new area of work needs its own dedicated space in the vault. Interviews Dave
  in 6 questions then builds the full structure automatically.
---

# Skill: New Project

Create a new project inside `03 Projects/` by interviewing Dave, then scaffolding the full folder structure, CLAUDE.md, and COMMANDS.md.

---

## How It Works

1. Duplicate `03 Projects/(PROJECT TEMPLATE)/` into a new folder
2. Interview Dave one question at a time (6 questions max)
3. Build the folder structure and files based on answers
4. If Dave doesn't have an answer yet — use sensible defaults and leave TODOs for him to fill in later

---

## Interview Questions (Ask One at a Time)

Ask conversationally. Each answer can shape the next question. If Dave says "I'm not sure yet" — don't push, just work with what you have.

### Q1. What's the project called?
Used for the folder name under `03 Projects/`.

### Q2. What is this project?
One paragraph. What are we building / doing / creating? Who is it for?

### Q3. What does "shipped" look like?
What's the goal? What does success look like? This becomes the prime directive in the CLAUDE.md — the thing Claude nudges toward in every session.

### Q4. Who else is involved?
Key people and their roles. "Just me" is a valid answer.

### Q5. What's the process from start to finish?
Walk through how something goes from idea to done in this project. This creates the numbered project folders (inputs → process → outputs).

**If Dave isn't sure:** Use this default structure:
- `00 Ideas/` (input)
- `01 In Progress/` (process)
- `02 Done/` (output)

Tell him he can restructure later as the process becomes clearer.

### Q6. Any rules or conventions Claude should follow?
Things Claude should always or never do in this project — specific formats, naming conventions. Optional — skip if nothing yet.

---

## After the Interview

### Step 1: Duplicate the template
```bash
cp -R "03 Projects/(PROJECT TEMPLATE)" "03 Projects/[Project Name]"
```

### Step 2: Clean up template artifacts
- Remove the `00 Duplicate/` folder (for manual duplication only)
- Remove the placeholder `CLAUDE.md`
- Remove the placeholder `COMMANDS.md`

### Step 3: Create project-specific folders
Based on Q5, create numbered folders following the input → process → output flow. Then add the standard utility folders at the end with the next available numbers:

- `XX System/` — scripts, config, reusable processes
- `XX Skills/` — skill markdown files
- `XX Attachments/` — images, screenshots, PDFs
- `XX Iteration Logs/` — notes on what to improve

**Note:** The template creates `04 System/`, `05 Skills/`, `06 Attachments/` — but the numbers may need to shift depending on how many project-specific folders were created. Remove the template defaults and recreate with correct numbering.

### Step 4: Write CLAUDE.md

```markdown
# [Project Name]

[One paragraph: what this project is — from Q2]

## Claude's Role

[What Claude does in this project. Specific — not "help me ship" but the actual job.]

[Prime directive from Q3. Format:]
If a session is drifting without moving toward [shipped output], nudge me back: "[contextual nudge message]"

## Process

[Step-by-step from Q5. Numbered steps showing how work flows start to finish.]

## Key People

[From Q4. Name — role. Skip if solo project.]

## Folder Structure

[Every folder with a short description of what goes in it.]

## Rules & Conventions

- **`(C)` prefix** — Files created by Claude are prefixed with `(C)` so they're clearly AI-generated.
- **Editing rule** — Before editing any file without the `(C)` prefix, ask for permission first.
[Add any project-specific rules from Q6]

## Current Status

> **Last updated:** [today's date]
> **Status:** Just created — getting started.

<!-- TODO: Update this as the project progresses -->
```

For anything Dave wasn't sure about, add a `<!-- TODO: fill this in -->` comment so he can find and complete it later.

### Step 5: Write COMMANDS.md

```markdown
# Commands & Skills

Quick reference for all available skills and commands in this project.

## Skills (in XX Skills/)
_No project-specific skills yet._

## Commands
_No project-specific commands yet._
```

### Step 6: Update the root CLAUDE.md

Two sections need to stay in sync with active projects:

1. **Folder Structure** — Add the new project folder under the `03 Projects/` tree with a short description.
2. **My Current Projects & Overviews** — Add a new subsection:

```markdown
### [Project Name] — `03 Projects/[Project Name]/`
**Status:** Just created
[One-line description from Q2]
```

### Step 7: Confirm to Dave

Show him:
- The folder structure that was created
- A summary of the CLAUDE.md
- Any sections with TODOs — point these out so he knows what to fill in
- Remind him the structure can be updated anytime as the project evolves

---

## Rules

- Always duplicate from the template — don't build from scratch
- Use TODOs for anything Dave wasn't sure about — never invent answers
- Always update root CLAUDE.md after creating a project — the vault context must stay in sync
- Keep the interview to 6 questions max — if something is unclear, use a sensible default
