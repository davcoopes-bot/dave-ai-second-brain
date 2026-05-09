---
name: fba-daily-sync
description: >
  End-of-day sync skill for Amazon FBA business partners. Use this skill whenever the user says anything like
  "run daily sync", "generate today's summary", "end of day", "daily debrief", or "sync up". Also triggers
  when the user pastes in a message that starts with "FBA DAILY SYNC" — that means they've received their
  partner's summary and want Claude to absorb it. This skill covers both generating the outgoing summary AND
  receiving and integrating an incoming one.
---

# FBA Daily Sync

You and your user are building an Amazon FBA business together from scratch. At the end of each day, they
sync with their business partner by generating a structured summary of everything that happened, then
pasting it into their partner's Claude — and vice versa. The goal is that the receiving Claude can start the
next conversation fully briefed, with zero need to ask "what's the context?" — as if they'd been in the
room all day.

There are two modes. Detect which one applies from context.

---

## Mode 1: Generate (outgoing summary)

Triggered when the user asks you to run the sync, do the debrief, or generate the daily summary.

You've been in the conversation all day. You know what was researched, what was found, what was decided,
and what's still uncertain. Don't ask questions — synthesise it yourself.

**The summary must be complete enough that the partner's Claude can pick up where you left off without
asking any clarifying questions.** That's the standard. If someone reads it cold and still doesn't
understand why a decision was made, or what the actual data showed, or what hypothesis is being tested
tomorrow — it's not done.

Write the summary using this format:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FBA DAILY SYNC — [their first name] — [today's date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**WORKED ON**
[Full picture of the day — not just what topics were covered, but how: what tools were used, what
approach was taken, what the goal going in was, and roughly how much time/effort. This gives the
receiving Claude the methodology context they need to interpret everything that follows.]

**KEY FINDINGS**
[This is the core of the briefing. For every product, niche, supplier, or topic researched, provide
the full picture: the actual data (BSR, review count, star rating, price, estimated monthly revenue
if available), what that data tells you about competition and margin, any notable patterns from
reviews or listings, and your read on whether it's promising. Don't summarise to the point of
stripping out the useful detail — the receiving Claude needs enough to reason about these products
independently.]

**DECISIONS MADE**
[Every decision, large or small, with the reasoning behind it. Not just "ruled out rope toys" but
"ruled out rope toys — BSR ~4,000 with 3,000-8,000 reviews signals an entrenched market; a new
entrant would need heavy launch spend to compete and margins at £9.99-£13.99 are too tight."
The reasoning is what the partner's Claude needs to not re-litigate settled questions.]

**OPEN QUESTIONS**
[Everything that's still unresolved, uncertain, or needs investigation — with enough context to
understand why it matters. Not just "shipping costs unknown" but "shipping costs from China not
yet calculated — this could materially change the slow feeder margin case, so it needs to be
resolved before committing to samples." Include anything the partner should factor in on their end.]

**CURRENT DIRECTION**
[The working hypothesis or strategic focus at end of day — where this is all heading. What niche(s)
are still in contention, what the criteria are for moving forward, what success looks like in the
next few days. This helps the partner's Claude understand the bigger picture behind tomorrow's tasks.]

**TOMORROW'S FOCUS**
[Specific plan for the next session — not just "look at pet accessories" but what exactly to look
for, what question is being tested, and what a good vs. bad result would tell you.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END SYNC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After writing it, tell the user: "Copy everything between the lines and send it to your partner."

**Writing guidelines:**
- Write each section as prose or detailed bullets — not one-liners. The receiving Claude needs
  substance, not a skeleton.
- Include real numbers wherever they exist. "Margins look thin" is not useful. "BSR ~6,000,
  selling at £12.99, likely 200-400 units/month — at a £3-4 landed cost that leaves almost no
  room for PPC and fees" is useful.
- Reasoning behind decisions is non-negotiable. The partner's Claude should never have to guess
  why something was ruled in or out.
- If the day was slow or inconclusive, say so honestly and explain why — that's still useful
  context. Don't pad with fake insights, but do explain the situation fully.
- The CURRENT DIRECTION section is especially important early in the process when niche selection
  is still open — it tells the partner's Claude what the current thinking is and prevents the
  two research threads from going in completely different directions without realising it.

---

## Mode 2: Receive (incoming summary)

Triggered when the user pastes in a message starting with "FBA DAILY SYNC".

Read the summary carefully and thoroughly. Then give a substantive response that shows you've
actually absorbed and thought about it — not just a checklist of what was said.

Your response should:

1. **Confirm what you now understand** — synthesise the key things you've taken on board in a
   way that demonstrates comprehension, not just repetition. If something stands out as
   particularly significant for the business, say so and explain why.

2. **Add relevant analysis** — this is where you earn your keep. Use your knowledge of FBA
   mechanics to enrich what the partner found. If they found a supplier at $3.20/unit with MOQ
   200, work through what the margin looks like with likely shipping and FBA fees. If they found
   a BSR, give a sense of what monthly sales volume that implies. Help them see what the data
   means, not just what it says.

3. **Flag connections to your user's work** — if the partner's findings are relevant to what
   your user has been researching (same niche, competing niche, complementary data), surface
   that explicitly. This is the whole point of the sync.

4. **Surface what matters most** — identify the one or two things from this summary that most
   need to be resolved or acted on. What's the critical path question?

5. **Ask any clarifying questions** — if something is unclear or seems like an important gap,
   ask. Keep it focused — one or two good questions, not a list.

Keep the response substantive but readable. The goal is to make the partner's work genuinely
useful to your user, not just acknowledged.

---

## FBA context to keep in mind

These two people are starting an Amazon FBA business from scratch. At this stage the key questions are
around niche and product selection. The things that matter most in that process:

- **BSR (Best Sellers Rank)**: lower = more sales. A BSR of ~1,000 in a category means very high
  monthly sales but also very high competition. ~10,000-20,000 is often the sweet spot for new
  entrants — enough demand to be viable, not so much competition that launch is prohibitive.
- **Review count**: high review counts (3,000+) mean an entrenched market. Under 1,000-2,000 on
  the top listings is generally more accessible for a new brand.
- **Price and margin**: FBA fees + shipping + COGs typically need to be under 30-35% of the
  selling price to leave room for PPC and profit. At £12.99 there's almost no room. £18-25 is
  a much healthier price point for a new seller.
- **MOQ and cash flow**: starting from scratch means capital is limited. MOQ 200 at ~$3-4/unit
  is a manageable first order. Higher MOQs need more scrutiny.
- **Product quality signals**: review complaints about durability, poor instructions, or bad
  packaging are opportunities — if you can source better, you can differentiate.

Use this context to make both the summaries and the receive-mode responses more analytically useful.
