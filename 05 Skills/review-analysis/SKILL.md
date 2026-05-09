---
name: review-analysis
description: >
  Transform raw user feedback — reviews, comments, survey responses, forum posts — into
  structured, actionable insights. Use this skill any time Dave (or anyone) pastes in a batch
  of reviews or feedback and wants to understand what's working, what's broken, what users
  actually care about, and what to do about it. Trigger on: "analyse these reviews",
  "what are people complaining about", "run this feedback through the wiki", "extract insights
  from these comments", "what patterns are showing up", "summarise this feedback", or any time
  a chunk of raw user opinions lands in the conversation. Works across ALL domains — products,
  services, content, courses, apps, ideas. Always run this skill rather than answering
  conversationally when feedback analysis is requested.
---

# Review Analysis Skill

You are turning raw user opinions into structured intelligence. The goal isn't just
summarisation — it's finding the signal in the noise: what matters, what's broken,
what's valued, and what to actually do next.

---

## Step 1 — Read the Input

Scan everything the user has given you. This could be:
- Amazon / Google / Trustpilot reviews
- Reddit / forum comments
- Survey open-text responses
- App store reviews
- Customer support tickets
- Social media comments
- Internal team feedback

Don't assume the domain. Let the content tell you what it's about.

---

## Step 2 — Classify Each Piece of Feedback

Sort every review / comment into one of three buckets:

| Bucket | What belongs here |
|--------|-------------------|
| **Positive** | Things users praise, appreciate, or say are working |
| **Negative** | Complaints, frustrations, deal-breakers, recurring problems |
| **Neutral / Mixed** | Suggestions, caveats, "it's ok but…" opinions |

You don't need to list every item — just hold this classification in mind as you move through Steps 3–5.

---

## Step 3 — Extract Patterns

This is the most important step. Individual opinions are noise; patterns are signal.

Look for:

**Complaint patterns** — What do multiple people complain about? Which complaints come up most often? Which carry the most emotional weight (frustration, anger, confusion, regret)?

**Value patterns** — What do people specifically call out as good? What keeps them coming back? What do they brag about to others?

**Emotional signals** — Frustration? Confusion? Betrayal? Excitement? Trust? These emotional undercurrents tell you how users *feel*, not just what they *think*.

**Unmet needs** — What do users wish existed? What workarounds are they doing? What are they asking for that isn't there?

Weight patterns by: (a) how many people mention it, (b) how strongly they feel about it, (c) how much impact it likely has on behaviour (purchase, churn, referral).

---

## Step 4 — Synthesise Insights

Convert patterns into intelligence under four lenses:

### A. Key Pain Points
What are the core problems people keep running into? State them precisely — not "bad UX" but "users can't find the settings page because it's buried under the account menu."

### B. Key Value Drivers
What do users care about most? What made them choose this, stay, or recommend it? These are your levers.

### C. Opportunities
Gaps between what exists and what users want. Unmet needs. Things competitors do that users mention. Quick wins hiding inside complaints.

### D. Risks
Issues that could erode trust, satisfaction, or performance if left unaddressed. Watch for: safety concerns, trust language, words like "never again", "misleading", "disappointed".

---

## Step 5 — Convert to Actionable Output

Translate insights into things someone can actually do:

**Improvements** — Specific changes to fix or optimise. Be concrete: "Rewrite the onboarding flow to explain X upfront" beats "improve onboarding."

**Messaging angles** — How to communicate value based on what users actually care about. Pull language directly from positive reviews — users wrote your best copy.

**Objections to address** — Recurring concerns or hesitations that need to be pre-empted in sales, marketing, or product copy.

**Differentiation opportunities** — Where competitors are weak based on what users say they're missing elsewhere.

---

## Step 6 — Wiki Integration

After producing insights, create or update the following pages in the wiki. Use the `(C)` prefix on all AI-generated files.

### Pages to create or update

**`06 Wiki/wiki/fba/(C) Review Insights — [Topic/Product].md`** (for FBA reviews)
**`06 Wiki/wiki/research/(C) Review Insights — [Topic].md`** (for other domains)

```markdown
# (C) Review Insights — [Topic/Product]
*Analysed: [DATE]*

## Summary
[2–3 sentence overview of what the feedback reveals]

## Top Pain Points
[Ranked list]

## Top Value Drivers
[Ranked list]

## Opportunities
[Bulleted list]

## Risks
[Bulleted list]

## Actionable Improvements
[Bulleted list]

## Messaging Angles
[Bulleted list]

## Objections to Address
[Bulleted list]

## Key Patterns
[Narrative: what themes kept surfacing and why they matter]
```

---

## Step 7 — Update log.md

Append to `06 Wiki/system/log.md`:

```markdown
## [DATE] ingest | Review Analysis — [Topic/Product]
- Source: [type of feedback, e.g. "Amazon reviews", "survey responses"]
- Volume: [number of items processed]
- Key finding: [single most important insight]
- Pages created/updated: [list]
```

---

## Step 8 — Deliver the Structured Output

Always return this exact structure at the end, regardless of domain:

---

### 🔴 Top 5 Pain Points
*(ranked: most frequent / most severe first)*
1. …
2. …
3. …
4. …
5. …

### 🟢 Top 5 Value Drivers
*(what users care about most)*
1. …
2. …
3. …
4. …
5. …

### 💡 3 Key Opportunities
1. …
2. …
3. …

### ⚙️ 3 Actionable Improvements
1. …
2. …
3. …

### 📣 3 Messaging Angles
*(language to use in copy, pitches, positioning)*
1. …
2. …
3. …

---

## Rules

- **Patterns over individuals.** Never over-index on a single outlier. If only one person says it, note it but don't rank it high.
- **Severity beats frequency when warranted.** One trust-destroying complaint outweighs ten mild annoyances.
- **Domain-agnostic.** Don't assume you're analysing a product. Adapt your lens to whatever the feedback is about.
- **Steal the user's language.** The best copy comes directly from positive reviews. Quote them when framing messaging angles.
- **End with clear direction.** Don't leave Dave with analysis and no "so what." The improvement and messaging sections are not optional.
- **No padding.** If a section has nothing meaningful, say so rather than filling it with waffle.
