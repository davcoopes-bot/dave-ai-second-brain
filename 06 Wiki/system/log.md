# Wiki Log — Append-Only Timeline

> **Rule:** Never delete or edit entries. Append only.
> **Format:** `## [YYYY-MM-DD] action | description`
> **Actions:** `setup` `ingest` `query` `update` `lint` `contradiction`

---

## [2026-05-03] setup | Wiki layer initialised

- Structure created: `06 Wiki/` with `raw/`, `wiki/`, `system/`
- Files created: `WIKI-SCHEMA.md`, `index.md`, `log.md`
- Categories: business, fba, finance, fitness, cars, personal, research, people, concepts, sources
- Nothing outside `06 Wiki/` was modified
- Triggered by: Dave — pasted LLM Wiki idea file and requested integration

---

## [2026-05-03] ingest | Gym Accessories Research (2026-05-03)

- Raw source: `03 Projects/FBA Research/(C) Gym Accessories Research — 2026-05-03.md` (read in-place — source already in main brain)
- Summary page created: `wiki/sources/src — Gym Accessories Research.md`
- Niche pages created: `wiki/fba/niche-padded-lifting-straps.md`, `wiki/fba/niche-fabric-resistance-bands.md`
- Pages updated: `system/index.md`
- Contradictions: none
- Open questions: Sub-keyword H10 Xray needed on "padded lifting straps" and "figure 8 lifting straps" before niche can be re-scored

---

## [2026-05-03] ingest | Silicone Splatter Screen Research (2026-05-03)

- Raw source: `03 Projects/FBA Research/(C) Silicone Splatter Screen Research — 2026-05-03.md`
- Summary page created: `wiki/sources/src — Silicone Splatter Screen Research.md`
- Niche page created: `wiki/fba/niche-silicone-splatter-screen.md`
- Pages updated: `system/index.md`
- Contradictions: none
- Open questions: Alibaba COGS for silicone handle variant — is $6.30 midpoint achievable?

---

## [2026-05-03] ingest | Three Niche Comparison (2026-05-03)

- Raw source: `03 Projects/FBA Research/(C) Three Niche Comparison — 2026-05-03.md`
- Summary page created: `wiki/sources/src — Three Niche Comparison.md`
- Niche pages created: `wiki/fba/niche-cable-management.md`, `wiki/fba/niche-dog-travel-accessories.md`, `wiki/fba/niche-bamboo-kitchen-utensils.md`
- Synthesis page created: `wiki/fba/fba-research-overview.md`
- Concept page created: `wiki/concepts/fba-scoring-framework.md`
- Pages updated: `system/index.md`
- Contradictions: none
- Open questions: Cable management COGS for quality lid mechanism?

---

## [2026-05-03] ingest | AI 2027 (ai-2027.com)

- Raw source: `raw/AI 2027.md` (placed by Dave in main brain raw folder)
- Summary page created: `wiki/sources/src — AI 2027.md`
- Research page created: `wiki/research/ai-2027-scenario.md`
- Concept pages created: `wiki/concepts/ai-capability-milestones.md`, `wiki/concepts/ai-alignment-risk.md`
- Pages updated: `system/index.md`
- Contradictions: none
- Open questions:
  - How does the AI 2027 timeline affect Dave's 7-year financial freedom plan?
  - Is the race ending or slowdown ending more likely?
  - What income streams are most durable in a post-AGI world?

---

## [2026-05-03] ingest | LLM Wiki Pattern

- Source: pasted directly into conversation (idea file / article)
- Raw source saved: `raw/sources/2026-05-03 — LLM Wiki Pattern.md`
- Summary page created: `wiki/sources/src — LLM Wiki Pattern.md`
- Concept page created: `wiki/concepts/llm-wiki-pattern.md`
- Pages updated: `system/index.md`
- Contradictions: none (first ingest)
- Open questions:
  - What search tooling to add when wiki exceeds ~100 pages? (qmd suggested in source)
  - Which Obsidian plugins to install? (Dataview, Marp mentioned as useful)
  - What's the first real domain to populate — FBA, finance, or trading?

---

## [2026-05-03] ingest | Amazon Product Detail Page Rules

- Raw source: `raw/Product detail page rules.md` (placed by Dave from Amazon Seller Central)
- Source URL: https://sellercentral.amazon.com/help/hub/reference/external/200390640
- Summary page created: `wiki/sources/src — Amazon Product Detail Page Rules.md`
- Pages created:
  - `wiki/fba/fba-listing-optimisation.md` — title rules, bullet structure, image sequence, backend keywords, A+ Content
  - `wiki/fba/fba-ranking-factors.md` — A10 signals: sales velocity, CTR, CVR, keyword relevance, FBA status, stock rate
  - `wiki/fba/fba-compliance-suppression.md` — full suppression risk table, all prohibited content, ASIN creation/editing rules
- Pages updated: `system/index.md` (total pages: 19 → 24)
- Contradictions: none
- Key insights:
  - Title hard cap 200 chars, but mobile truncates at ~80 — most sellers optimise for the wrong number
  - New version of a product (colour, size, material, features) = mandatory new ASIN — common costly mistake
  - Re-branding requires a new ASIN — cannot change brand name on existing ASIN
  - GTIN must be GS1-issued — third-party barcodes get listings blocked
  - Repeatedly adding/removing prohibited content = evasive behaviour = no reinstatement path
- Open questions:
  - Amazon image requirements (G1881) — referenced but not ingested; worth a dedicated image optimisation page
  - Amazon Prohibited Product Claims (G202024200) — referenced; compliance implications for Voya's marketing language
  - What environmental/sustainability claims can Voya legitimately make for packaging?

---

## [2026-05-05] update | System audit + structural fixes

- Triggered by: Dave — ran full systems audit, then requested architectural fixes
- Audit score (pre-fix): Structure 5/10, Cohesion 3/10, Knowledge 6/10, Skills 6/10, Scalability 5/10 — Overall 5/10
- Changes made:
  - `CLAUDE.md` (root): Added wiki wiring to Claude's Purpose, added wiki check rule, updated folder structure map, added FBA and trading to projects section
  - `06 Wiki/system/WIKI-SCHEMA.md`: Updated Folder Layout to correctly show root `raw/` as the source inbox (not `06 Wiki/raw/sources/`); added warning about root wiki/ path confusion
  - `05 Skills/FBA/fba-product-research/SKILL.md`: Removed duplicate scoring rubric from Phase 6; replaced with pointer to `06 Wiki/wiki/concepts/fba-scoring-framework.md` as single source of truth
  - `06 Wiki/system/index.md`: Added Finance and People sections, updated total page count to 26
- Files archived: `02 Chess Moves/(ARCHIVED) Chess Moves Example — KJ.md` — KJ's strategy document archived; was incorrectly imported as a vault template example
- New files created:
  - `02 Chess Moves/(C) Chess Moves — Dave 2026.md` — Dave's actual strategic thinking document with income stream status board and unsettled questions
  - `05 Skills/wiki-ingest/SKILL.md` — New skill for ingesting sources into the wiki
  - `05 Skills/chess-moves/SKILL.md` — New skill for running strategic thinking sessions
  - `05 Skills/stock-trading-review/SKILL.md` — New skill for trading position reviews and framework builds
  - `06 Wiki/wiki/finance/stock-trading-overview.md` — PLACEHOLDER trading page (run stock-trading-review skill to populate)
  - `06 Wiki/wiki/people/josh.md` — PLACEHOLDER people page for Josh
- Remaining manual tasks for Dave:
  - Delete `02 Chess Moves (Long-Term Planning)/Chess Moves (EXAMPLE).md` (original KJ file — now archived)
  - Delete root `wiki/` folder and its empty file `wiki/fba/fba-advertising-launch-strategy.md`
  - Fill in Weekly Update section in CLAUDE.md (run weekly-update.md skill)
  - Run stock-trading-review skill to populate trading wiki page
  - Run chess-moves skill to settle the FBA vs. trading priority decision
- Contradictions: none
- Open questions:
  - What is Dave's actual trading strategy and current positions?
  - What is Josh's specific role/stake in FBA and trading?
  - When will real Helium 10 data be available to validate simulated FBA research?

---

## [2026-05-06] restructure | Skill Migration — Standardised to folder+SKILL.md format

- Triggered by: Dave — system audit identified three inconsistent skill formats; migration requested
- Files converted into proper `folder/SKILL.md` structure:
  - `brain-setup.md` → `05 Skills/brain-setup/SKILL.md`
  - `weekly-update.md` → `05 Skills/weekly-update/SKILL.md`
  - `new-project.md` → `05 Skills/new-project/SKILL.md`
  - `(C) review-analysis.skill` (zip) → `05 Skills/review-analysis/SKILL.md`
  - `FBA/(C) fba-keyword-research.md` → `05 Skills/FBA/fba-keyword-research/SKILL.md`
- Changes made per file:
  - Added proper YAML frontmatter (`name:`, `description:` with trigger phrases) to all migrated skills
  - Fixed "KJ OS" reference in new-project → "Dave's AI Brain"
  - Updated review-analysis wiki paths to match actual vault structure (`06 Wiki/wiki/fba/` and `06 Wiki/wiki/research/`)
  - All original files preserved and marked with migration notice
- Original files kept (not deleted): awaiting Dave's approval before removal
- New skills also added this session (separate from migration):
  - `05 Skills/skill-builder/`, `automation-opportunity-finder/`, `leverage-finder/`
  - `05 Skills/ai-decision-filter/`, `aios-audit/`, `tool-connection-setup/`
- Pending Dave approval: delete original .md files and `(C) review-analysis.skill` zip once migration confirmed clean

---

## [2026-05-06] update | Weekly Update — first run

- Pages updated: `CLAUDE.md` → Weekly Update section
- What's working: Vault development — happy with progress building Claude as a thinking partner
- What's not working: Vault not yet complete — skills and key information still being locked in
- Sitting on / need to decide: Which income route to commit to (trading vs FBA)
- Feeling pulled toward: Both trading and FBA — priority decision between them is the key thing to settle
- Deadlines: None
- Project status changes: None reported
- Note: First weekly update ever run — section was blank since vault setup on 2026-05-03

---

## [2026-05-06] update | Chess Moves — Session 1

- Pages updated: `02 Chess Moves (Long-Term Planning)/(C) Chess Moves — Dave 2026.md`
- Decisions settled:
  - FBA = primary income engine, Trading = background wealth builder (roles no longer confused)
  - YouTube Shorts + Ecom parked indefinitely until FBA generates consistent revenue
  - EXR (Elixir Energy) — sell, thesis invalidated by announcement
  - ERA (Energy Resources) — sell, -98.82%, done
  - Get H10 before committing any FBA capital — non-negotiable
  - FBA launch budget $3k to start, push to $4–5k if H10 strongly validates product
  - 6-month FBA success = product live on Amazon with real sales data + active PPC campaign
- Unsettled questions remaining: How much of the $60k liquid to deploy and into what
- Portfolio reviewed: ~$18k+ ASX + US positions, ETF strategy sound, two speculative positions to exit

---

## [2026-05-06] update | Stock Trading Overview — fully populated

- Pages updated: `wiki/finance/stock-trading-overview.md`, `system/index.md`
- Source: Chess Moves Session 1 — documented from live portfolio review
- What was captured:
  - Full portfolio holdings (ASX ETFs + individual stocks + US via Revolut)
  - Core thesis: AI/power infrastructure boom — semiconductors, data centres, energy
  - Trading role clarified: background compounder, not income engine
  - Individual stock rule formalised: catalyst is the exit trigger, not the price
  - EXR decision: hold pending Diona-1 flow test, sell immediately if disappointing
  - ERA decision: sell
  - NBIS active trading pattern documented
  - Review log started

---

## [2026-05-06] update | Budget — first version created

- Pages created: `03 Projects/Finances/01 Budget/Budget.md`
- Source: Bank statement analysis (Apr–May 2026, CommBank Smart Access)
- What was captured:
  - Monthly take-home: ~$7,100 (wages) + ~$500 irregular (construction)
  - Fixed expenses: $1,523/month (RS3 finance $1,092 is the dominant cost)
  - Subscriptions: $144/month (ChatGPT + BlossomUp cancelled)
  - Variable target: $750/month
  - Savings & investment target: $3,217/month
  - Monthly surplus/buffer: ~$1,466
  - Amex noted as shared with Josh + medical costs — to be tracked separately
  - Budget v2 flagged for when tradesman income kicks in

---

## [2026-05-06] update | fba-delegation skill created

- File created: `05 Skills/FBA/fba-delegation/SKILL.md`
- Purpose: FBA stage detection + Dave/Josh task split with no-overlap check + routing to existing skills
- Trigger phrases: "plan our fba work", "what should we do today", "split the work", "delegation", "who does what"
- What it does NOT do: run research, handle daily sync (fba-daily-sync), write wiki pages (wiki-ingest), score sessions
- Stage detection table covers: Research → Validation → Sourcing → Listing → Launch → Optimisation → Scaling
- Routes to: fba-product-research, fba-keyword-research, review-analysis, fba-daily-sync, wiki-ingest, chess-moves
- Contradictions: none
- Note: Stripped-down version of proposed FBA Control Panel — removed duplication with 8 existing skills

---

## [2026-05-06] ingest | Amazon Product Image Guide (G1881)

- Raw source: `raw/Product image guide.md` (Amazon Seller Central AU — G1881)
- Source URL: https://sellercentral.amazon.com.au/help/hub/reference/external/G1881
- Summary page created: `wiki/sources/src — Amazon Product Image Guide.md`
- Wiki page created: `wiki/fba/fba-image-requirements.md`
- Pages updated: `system/index.md` (total pages: 26 → 28)
- Contradictions: none — extends fba-listing-optimisation.md which referenced G1881 but hadn't ingested it
- Key insights:
  - Main image must be pure white background (RGB 255, 255, 255) — no exceptions for most categories
  - Product must fill 85% of the image frame
  - No text, logos, watermarks, or badges on any image — includes "Best seller" and "Amazon's Choice"
  - Lifestyle main image NOT allowed for most product types — white background hero shot is the default
  - No compliant main image = listing suppressed from search automatically
  - Amazon recommends 6+ images + 1 video per listing
  - Images can take up to 24 hours to appear after upload
- Open questions:
  - Which product types are allowed to use a lifestyle shot as main image?
  - What environmental/sustainability claims can Voya legitimately make for packaging?

---

## [2026-05-06] update | session-close skill created

- File created: `05 Skills/session-close/SKILL.md`
- Purpose: End-of-session capture — decisions, new info, contradictions, stale pages, next session primer
- Trigger phrases: "close the session", "wrap up", "before we finish", "anything to update"
- Process: 5 questions → immediate wiki fixes → queue larger ingests → log entry → clean close message
- Why it matters: knowledge only compounds if it gets filed — this is the mechanism that makes the vault learn every session, not just when Dave explicitly requests an ingest

---

## [2026-05-06] session-close | Vault prep, H10 brief, session-close skill

- Decisions captured: H10 confirmed — Dave and Josh purchasing Saturday
- Wiki pages updated:
  - `wiki/fba/niche-silicone-splatter-screen.md` — corrected main image recommendation (lifestyle → white background hero shot per G1881)
  - `wiki/fba/fba-image-requirements.md` — created from Amazon G1881 ingest
  - `02 Chess Moves — Dave 2026.md` — FBA next action updated to reflect H10 Saturday + delegation skill complete
- New files created this session:
  - `05 Skills/FBA/fba-delegation/SKILL.md`
  - `05 Skills/session-close/SKILL.md`
  - `03 Projects/FBA Research/(C) H10 Validation Brief — Saturday Session.md`
  - `wiki/sources/src — Amazon Product Image Guide.md`
- Queued for future build: `monthly-review` skill, `wiki-health` skill
- Contradictions fixed: splatter screen main image (lifestyle → white bg)
- Next session: FBA focus, before Saturday

---

## [2026-05-07] session-close | Anti-glazing directive added to CLAUDE.md

- Decisions captured: "Pressure-test before validating" bullet added to Claude's Rules & Boundaries in CLAUDE.md
- What changed: Dave proposed a Critical Thinking / Anti-Glazing skill — evaluated as too rigid (fixed output format, applied universally). Distilled the core value into one CLAUDE.md directive instead. Sequencing is the key addition: challenge first, conditional agreement after, confidence = more scrutiny.
- Wiki pages updated: none
- Queued for ingest: none
- Contradictions fixed: none
- Next session: open — FBA likely

---

## [2026-05-07] update | supplier-outreach skill created + Alibaba shortlist built

- Files created:
  - `05 Skills/FBA/supplier-outreach/SKILL.md` — generates original first contact emails to suppliers from product specs + supplier context
  - `03 Projects/FBA Research/(C) Alibaba Supplier Shortlist — Silicone Splatter Screen.md` — search terms, evaluation criteria, shortlist table, red flags, first contact template, margin check
- Trigger phrases: "write a supplier email", "contact a supplier", "first contact email", "supplier inquiry"
- Skill process: reads niche page → 4 questions → generates tailored email → review → optional log to shortlist
- Known suppliers identified: Kangde Silicone (21yr OEM), Shunyao — both need spec confirmation (foldable vs solid)
- Real COGS data found: ~$5.75–$6.05/unit at 200–499 MOQ — aligns with simulated estimate ($5.00–$7.60)

---

## [2026-05-07] update | product-launch-hub skill created

- File created: `05 Skills/FBA/product-launch-hub/SKILL.md`
- Folder created: `03 Projects/FBA Launches/` (launch execution — separate from FBA Research)
- Trigger phrases: "set up a launch hub", "product agreed", "product is confirmed", "launch hub"
- Output: 7 files per product — Overview, Supplier Tracker, Launch Timeline, Listing Build, PPC Strategy, Marketing Strategy, Job Delegation
- Rule: only runs after real H10 validation — not on simulated data
- PPC and Marketing Strategy files are framework-only until H10 data available
- Delegation file routes to fba-delegation skill for task splitting

---

## [2026-05-07] session-close | Supplier outreach + launch hub skills built

- Decisions captured: none
- Wiki pages updated: none beyond what was logged during the session
- New files this session: supplier-outreach skill, product-launch-hub skill, Alibaba supplier shortlist, FBA Launches folder created
- CLAUDE.md updated: "Pressure-test before validating" directive added
- Contradictions: none
- Next session: before Saturday — FBA focus

---

## [2026-05-09] session-close | H10 validation, automation pipeline, skills build

- Decisions captured: Silicone splatter screen → ❌ PASS (real H10 data: ~$1,277/month total market vs simulated $124k — 97% discrepancy; dead product)
- Contradictions fixed: All simulated FBA revenue data confirmed unreliable — real H10 is mandatory before any capital commitment
- Wiki pages updated:
  - `wiki/fba/niche-silicone-splatter-screen.md` — verdict changed from 93/100 ✅ Green Light → ❌ PASS; market snapshot updated with real H10 numbers
  - `wiki/fba/fba-research-overview.md` — splatter screen row updated to PASS; cable management promoted to #1 priority
  - `wiki/system/index.md` — splatter screen updated to PASS; new H10 source added; priority actions updated
  - `CLAUDE.md` — Weekly Update section updated (2026-05-09)
- New files created:
  - `wiki/sources/src — H10 Silicone Splatter Screen.md` — real H10 data for 3 keywords with full product tables
  - `05 Skills/FBA/h10-export-guide/SKILL.md` — exact H10 search terms, column checklist, export instructions
  - `05 Skills/FBA/niche-decision/SKILL.md` — ingests H10 CSVs, scores against framework, issues go/no-go verdict
  - `05 Skills/FBA/fba-research-review/SKILL.md` — morning briefing: agent commits, what needs action vs what can wait
  - `.github/workflows/trigger-fba-agent.yml` — GitHub Action: triggers FBA agent on H10 CSV push to raw/
  - `~/Library/LaunchAgents/com.dave.vault-autopull.plist` — macOS launchd: pulls vault from GitHub at 7:30am daily
- Automation pipeline live:
  - Vault pushed to GitHub: `github.com/davcoopes-bot/dave-ai-second-brain` (public)
  - Remote FBA research agent scheduled: `trig_016gto8no4HwX9Va1UjUdJwu` — runs 7am Perth daily
  - Mac auto-pull loaded and active (7:30am daily)
  - H10 push trigger deployed (note: CLAUDE_SESSION_TOKEN placeholder — may need manual trigger)
- Queued for ingest: none
- Next session: Run fba-research-review skill to check overnight agent output; get cable management product locked down (run H10 Xray on "cable management box" and "under desk cable organizer")
