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

---

## [2026-05-09] update | Real data scoring — cable management box + priority restack

- Triggered by: Autonomous workflow continuation — applying real ASINSight data gathered this session
- Key finding: "Cable hider" keyword (~28,100/month) is dominated by wall raceways, not cable management boxes. Keyword disambiguation invalidates simulated 88/100 Green Light score.
- Real data points: Cable management box confirmed at position #10 in "cable hider" — rattan style, $22.99, 1,204 reviews, 3,000+/month orders. Box sub-niche is real and has revenue; just needs box-specific keyword Xray.
- Review distribution for "cable hider": 23.66% under 100 reviews, 26.87% at 100–500 — healthy spread, not top-heavy.
- Confirmed fitness brands in lifting straps: Gymreapers, Element 26, Harbinger — established players but confined to head term; sub-keywords still uncontested at specific review levels.
- Wiki pages updated:
  - `wiki/fba/niche-cable-management.md` — revised from 88/100 Green Light → 72/100 Investigate More; added real data update section; updated next steps
  - `wiki/fba/fba-research-overview.md` — master rankings table restacked; padded lifting straps promoted to #1; priority queue rewritten; no Green Light niches currently
  - `wiki/system/index.md` — cable management summary updated; priority actions updated
- Current leading candidate: Padded Lifting Straps (85/100, 46% net margin) — sub-keyword H10 Xray is the next required step
- Next action for Dave: Run H10 Xray on "padded lifting straps" and "figure 8 lifting straps" — export with Reviews column

---

## [2026-05-10] update | Composio integration + agent email alerts

- Triggered by: Dave — session focused on wiring up external app integrations and 24/7 automation coverage
- What was built:
  - Composio CLI installed: `~/.composio/composio` v0.2.27
  - Gmail connected and tested (word_id: `gmail_bedip-pegbox`) — confirmed emails send via CLI
  - Google Calendar connected (word_id: `googlecalendar_plaque-teju`)
  - Composio MCP added to Claude: `connect.composio.dev/mcp` with consumer key — available next session
  - `COMPOSIO_API_KEY` + `COMPOSIO_CONSUMER_KEY` added to GitHub Secrets for remote agents
  - Both keys stored permanently in `~/.zshrc`
- Agents updated:
  - FBA agent (`trig_016gto8no4HwX9Va1UjUdJwu`) — now emails davcoopes@gmail.com immediately when any niche scores 80+ (Green Light)
  - Stock agent (`trig_01QiXPJoRawub6hEGUVyvDxS`) — now emails davcoopes@gmail.com on IMMEDIATE ACTION REQUIRED alerts (EXR catalyst, ERA sell)
  - Email mechanism: agents download Composio CLI, seed credentials from GitHub Secrets, execute GMAIL_SEND_EMAIL
- Skills updated:
  - `05 Skills/connect/SKILL.md` — full status table, key types documented, both apps confirmed active
- Next session: MCP tools (Gmail, Calendar) available natively in Claude — no scripts needed. Start fresh session to use them.
- Next action for Dave: H10 Xray on "padded lifting straps" + "cable management box" — export CSVs and drop in `raw/sources/`

---

## [2026-05-10] update | H10 scraper — full pipeline live, all three queue keywords validated

- Triggered by: Dave — continued previous session building H10 automation
- What was built:
  - Reverse-engineered H10's private API: `research-tools.helium10.com/api/xray/v1/searches/` (POST with ASINs), `members.helium10.com/api/v1/product/sales-chart`, `bsr-chart`, `review-chart` — all working with Bearer token from `~/.h10-session.json`
  - Full `h10_scraper.py` rewritten — Amazon search via Playwright + pycookiecheat (Chrome cookies), H10 API enrichment, CSV output
  - Queue processed: padded lifting straps ✅, figure 8 lifting straps ✅, cable management box ✅
  - Session file: auth is `CORE_BEARER_TOKEN` from localStorage; Amazon cookies pulled fresh from Chrome each run
- Real H10 data results:
  - **Padded lifting straps**: $104,368/mo total page 1 revenue ✅ PASSES revenue filter — BUT avg 13,277 reviews ❌ closed review moat; prices avg $12.48 ❌ thin margins — LIKELY PASS on competition grounds
  - **Figure 8 lifting straps**: $7,196/mo total ❌ FAILS revenue filter — too small a niche
  - **Cable management box**: $9,789/mo total ❌ FAILS revenue filter — too small a niche (confirms earlier finding)
- Wiki pages to update: `fba-research-overview.md`, niche-padded-lifting-straps.md` — scores need revision to real data
- Skills updated: `05 Skills/FBA/h10-scraper/SKILL.md` — fully updated for new API-based approach
- CLAUDE.md: Weekly Update updated
- Next action: Update wiki niche pages with real data scores, then decide whether to continue researching new niches or pivot strategy

---

## [2026-05-10] update | Obsidian tracker auto-wired + 15 new niche candidates generated

- Triggered by: Dave — continued from previous session, wrapping pipeline and generating new niche queue
- What was built:
  - `h10_scraper.py` updated — `update_obsidian_tracker()` function added; now auto-updates `03 Projects/FBA Research/(C) Niche Research Tracker.md` on every scrape run
  - Tracker auto-updates three sections: Summary table (new row), ❌ Failed Niches or ✅ Green Lights (new detail block), Research Log (new or appended row); frontmatter `updated:` date also bumped
  - `05 Skills/FBA/h10-scraper/SKILL.md` updated to document the Obsidian auto-update behaviour
- Niche candidates generated: 15 keywords across 3 batches for next H10 queue
  - Batch 1 (highest confidence): fridge organizer bins set, car seat back organizer with tablet holder, camping hammock with tree straps, acupressure mat and pillow set, under sink organizer and storage
  - Batch 2: monitor stand riser with drawer, insulated lunch bag large, dog car seat cover waterproof, spice rack organizer for cabinet, massage gun attachment heads set
  - Batch 3: elevated dog bowl stand large, hammock chair with stand, yoga mat strap carrier, silicone stretch lids set, wall mounted laundry drying rack
- Gmail integration: Composio MCP connector not yet active in this session — needs fresh session to pick up
- Next action: Start new session → ingest Josh's emails (Composio Gmail now available) → add Batch 1 keywords to `raw/h10-queue.txt` → run scraper

---

## [2026-05-10] ingest | Josh Foo emails — 9 FBA research notes (Gmail)

- Source: Gmail — sinclairjosh50@gmail.com, 9 emails sent 2026-05-10, retrieved via Gmail MCP
- Summary pages created (9):
  - `wiki/sources/src — Selling on Amazon US from Australia.md`
  - `wiki/sources/src — Amazon Private Label Startup Costs Full Breakdown 2025.md`
  - `wiki/sources/src — Amazon PPC Strategy Simple System That Works.md`
  - `wiki/sources/src — Sourcing Alibaba to Amazon FBA Step-by-Step.md`
  - `wiki/sources/src — Top Amazon FBA Mistakes to Avoid 2025.md`
  - `wiki/sources/src — Amazon FBA Product Research Data-Driven 2025.md`
  - `wiki/sources/src — Selling Private Label Products on Amazon 9 Steps.md`
  - `wiki/sources/src — Amazon FBA Private Label Make It Big 7 Steps.md`
  - `wiki/sources/src — How to Sell on Amazon Explained in 5 Minutes.md`
- Concept pages created (5):
  - `wiki/fba/fba-aus-seller-setup.md` — Wise account, W-8BEN, AU-US tax treaty, sales tax nexus
  - `wiki/fba/fba-startup-costs.md` — $3k–$10k range, all fee layers, landed cost, margin formula
  - `wiki/fba/fba-ppc-strategy.md` — 3-tier campaign, break-even ACOS, listing quality gate
  - `wiki/fba/fba-sourcing-alibaba.md` — 8-step workflow, supplier vetting, 5 sourcing mistakes
  - `wiki/fba/fba-product-research-framework.md` — winning product formula, 7-step workflow, micro-test
- Pages updated: `system/index.md` (total pages: 28 → 42)
- Contradictions logged:
  - Review threshold: Savvy FBA says <300; Helium 10 says <500. Resolution: use <300 (conservative). Noted in both source pages and fba-product-research-framework.md.
- Key insights from batch:
  - W-8BEN non-negotiable for Australian sellers — skip it and Amazon withholds 30% of all earnings
  - 64% of PL sellers started with under $5k; 58% profitable within year one
  - BigCommerce source most objective — less tool-pitching, stronger on risk and cost realism
  - Online Arbitrage (OA) is a separate model to PL — filed for reference, not our path
- Open questions:
  - What is Dave's committed capital for the first FBA order?
  - Which US states to prioritise for sales tax registration at scale?
  - Freight forwarder recommendation for China → USA (Australian seller)?

---

## [2026-05-11] ingest | Josh's branding research — 3 sources ingested via email

- Triggered by: Josh's Claude emailed 3 branding research articles + positioning exercise cover
- Sources ingested:
  - `sources/src — Brand Positioning How to Own a Space in Your Customers Mind.md` — "Logic of the Only" framework, white space mapping, category disruption strategy
  - `sources/src — Branding for Private Label Building a Distinct Identity.md` — USP discovery, brand storytelling, design as communication, loyalty tactics
  - `sources/src — Product Naming Strategy How to Name Your Brand.md` — 6 naming approaches, 5-step process, trademark checklist
- Key action item from Josh's Claude: Complete the positioning exercise ("We are the ONLY...") together once a product category is locked in — everything else flows from that sentence
- Summary email drafted and sent to Josh covering today's scraper results, the bifurcation pattern, rate limit status, and 60 queued keywords

---

## [2026-05-11] update | H10 scraper — Batches 1–3 complete, 0 green lights, strategy pivot

- Triggered by: Dave — scraper ran overnight on all 15 queued keywords
- Scraper results: 15 keywords processed, 0 pass, 0 errors
- Fail breakdown:
  - Revenue fails only: wall mounted laundry drying rack ($12,900), massage gun attachments ($1,606)
  - Reviews fail only (revenue passes): under sink organizer ($116k, 5,589 avg), insulated lunch bag ($124k, 7,968 avg), dog car seat cover ($56k, 8,200 avg), acupressure mat & pillow ($52k, 21,824 avg), camping hammock ($51k, 16,781 avg)
  - Both fail: fridge organizer, car seat organizer, monitor stand riser, spice rack, yoga mat strap, elevated dog bowl, hammock chair with stand, silicone stretch lids
- Key insight: 22 niches tested total (7 original + 15 scraper batches) — 0 green lights. Every high-revenue category has 5k–22k average reviews (locked). Low-review categories have no revenue. Broad, established categories are structurally closed. Batch 3 needs a different input strategy.
- Wiki pages updated:
  - `wiki/fba/fba-research-overview.md` — scraper results section added; eliminated niches table expanded with all 15 failures; priority queue updated with Batch 3 strategy pivot; revision history updated
  - `03 Projects/FBA Research/(C) Niche Research Tracker.md` — auto-updated by scraper
- Next action: Build Batch 3 keyword list using trending/emerging product methodology (TikTok-driven demand, accessories to hot primaries, seasonal sub-niches entering window) — not broad category brainstorming

---

## [2026-05-23] ingest | LegacyX FBA FAQ + Product Dashboard V2

- Raw source: Scraped autonomously via Composio browser automation (Notion public pages — JS rendering required)
- Source URLs:
  - https://brycejoe.notion.site/LegacyX-FBA-FAQ-220c7d93cfc7804cab34d2b67b3fa4d4
  - https://brycejoe.notion.site/LegacyX-FBA-Product-Dashboard-V2-6c5634e8a40146038bdace37647b2424
- Summary pages created:
  - `wiki/sources/src — LegacyX FBA FAQ.md`
  - `wiki/sources/src — LegacyX FBA Product Dashboard V2.md`
- Pages created (5):
  - `wiki/fba/fba-account-setup-legal.md` — LLC, NAICS 455219, separate accounts, liability insurance, taxes
  - `wiki/fba/fba-launch-and-reviews.md` — launch sequence, review stacking ratio, units to order, custom packaging dos/don'ts
  - `wiki/fba/fba-inventory-management.md` — reorder quantities, removal notices, return rate benchmarks, storage capacity
  - `wiki/fba/fba-hijackers.md` — detection, response protocol, Buy Box dynamics, prevention
  - `wiki/fba/fba-tools-software.md` — H10 vs Seller Sprite vs Jungle Scout, LegacyX in-house service contacts
- Pages updated (2):
  - `wiki/fba/fba-sourcing-alibaba.md` — Added 1688.com opening offer tactic
  - `wiki/fba/fba-product-research-framework.md` — Added LegacyX research tips section
- Index updated: 42 → 50 pages
- Contradictions:
  - GTIN sourcing: Existing compliance page recommends GS1. LegacyX recommends FBA-Pro GTIN exemption service instead of GS1/Barcodemania (recycled UPC risk). Not contradictory — different approaches. Noted in FAQ source page.
  - Samples policy: LegacyX says order stock samples (not custom) at selection stage. Minor difference in emphasis from existing sourcing page — LegacyX is more cost-efficient for early validation.
- What remains unscrapped:
  - Thinkific course lessons (full curriculum) — behind authentication, couldn't access autonomously
  - LegacyX Assets Drive (Google Drive PDFs: product workflow, barcode guide, Super URL method)
  - LegacyX service hub (https://inhouse.legacyxfba.com/) — rendered minimally
- Open questions:
  - What does the Thinkific lesson curriculum actually cover week-by-week?
  - What is the LegacyX Assets Drive URL?
  - What does Nawprotect cost for hijacker removal?
  - What is LaunchFast and how does it work?

---

## [2026-05-12] update | H10 scraper — Batches 4–7 complete, 0 green lights, Batches 8–10 queued

- Triggered by: Autonomous continuation — scraper ran overnight through Batches 4–7
- Batches 4 & 5 completed (prior session, results confirmed this session):
  - 15 keywords, 0 pass — trending/growth-signal strategy (mouth tape 134%, sleep bonnet 64%, pimple patches 20k reviews) all closed or too small
- Batch 6 — Premium price floor (15 keywords, 0 pass, all legitimate fails):
  - Closed: beef tallow balm ($142k/mo, 2,788 avg reviews), blue light glasses ($83k/mo, 21,508 avg), knee compression ($339k/mo, 42,776 avg)
  - Too small: cold brew pitcher, beeswax wrap, electric kettle, cocktail smoker, jaw exerciser, portable espresso, matcha whisk, fishing rod holder, silicone ice ball, hair diffuser, reusable straws, sleep headphones
- Batch 7 — Niche sports + craft hobbies + seasonal (15 keywords, 0 pass, all legitimate fails):
  - Closed: solar string lights ($76k/mo, 5,216 avg reviews)
  - Too small: pickleball hopper ($3,535/mo, 77 avg reviews), pickleball bag ($6,963/mo, 298 avg), pool thermometer ($15,814/mo, 229 avg), punch needle (304 avg), disc golf, diamond painting, resin art, candle making, kombucha, sauna ladle, hydroponic, calligraphy, beach tent, dry bag
  - Notable: several products with <300 avg reviews but revenue too small to enter (<$16k/mo)
- Rate limit pattern confirmed: ~90 enrichment API calls per session before H10 rate limits (~30 keywords). Running immediately after previous session hits limit from call 1. Must wait 1+ hour between runs.
- Batch 8 (van life/fitness/creator) — hit rate limit in two consecutive runs, both false fails. Re-queued.
- Queue state: 45 keywords ready — Batch 8 (15) + Batch 9 (15, regulatory/Gen Z) + Batch 10 (15, biohacking/new tech)
- Batch 10 highest conviction: stelo dexcom sensor cover patch (OTC CGM <18 months old), PFAS free beeswax food wrap sheet set (state bans live Jan 2025/2026), carbon steel wok flat bottom (non-toxic cookware shift), Ray-Ban Meta glasses lens replacement (millions of units, accessory sub-niche barely exists)
- Next action: Wait for H10 rate limit to reset (~1 hour), then run scraper on Batches 8/9/10

---

## [2026-05-23] ingest | LegacyX FBA Full Course (Thinkific) — 37/115 lessons

- Raw source: `raw/sources/2026-05-23 — LegacyX FBA Full Course.md` — scraped via Playwright + pycookiecheat (Chrome cookie auth)
- Source URL: https://legacyxfba.thinkific.com/courses/take/new-course
- Scraper: `/tmp/thinkific_scraper.py` — reusable; re-run as Dave progresses through course
- Summary page created: `wiki/sources/src — LegacyX FBA Full Course (Thinkific).md`
- Pages updated (2):
  - `wiki/fba/fba-tools-software.md` — LaunchFast pricing details ($49/month student rate, QUICKSTART3 trial code, A10–F1 grading system)
  - `wiki/fba/fba-account-setup-legal.md` — Business name = 5-minute decision tip; LLC before Amazon account setup warning
- Index updated: 50 → 51 pages
- Course status: Dave is 31% complete — 37 lessons accessible (6 full modules + 1 partial), 78 lessons locked behind prerequisite (must complete Branding On Amazon section)
- Key takeaways from accessible lessons:
  - Business name = zero-impact decision; initials + "Distribution"
  - LLC before Seller Central setup — changing structure later triggers re-verification
  - LaunchFast grades A10–F1; B1 and above = worth pursuing; $49/month student rate (code QUICKSTART3)
  - FBA-Pro provides laser-etched brand approval images (brand approval ≠ brand registry)
  - Profit margin calculator: live Google Sheet, orange cells only
- Contradictions: none — all accessible content consistent with existing wiki
- What remains locked (needs course progression):
  - Branding On Amazon (7/8 lessons), Creating Your First Listing, Product Sourcing, Shipping, Listing Creation, AI Tools, Launching, Advertising, PPC (Kunze + Wilco strategies), Scaling
- Re-ingest plan: `python3 /tmp/thinkific_scraper.py` — Chrome cookie auth auto-picks up newly unlocked lessons
- Open questions:
  - What are Kunze's and Wilco's specific PPC methods? (locked)
  - What does "Your Included LegacyX Product Selection" lesson contain?
  - What does "Section 8" refer to in the Scaling module?

---

## [2026-05-24] ingest | FBA niche research — full ingest, product confirmed

- Triggered by: Dave — requested full ingest of all FBA niche research resources
- New files ingested:
  - `03 Projects/FBA Research/(C) Supplement Gummy Brand — Launch Plan.md` (created 2026-05-15)
  - `03 Projects/FBA Research/(C) Three Product Comparison — 2026-05-05.md`
  - `03 Projects/FBA Research/(C) Niche Research Tracker.md` — read for batches 4–10 data
- Pages created (4):
  - `wiki/fba/niche-supplement-gummies.md` — confirmed product page, all 3 SKUs, unit economics, manufacturer list, launch sequence
  - `wiki/fba/niche-glp1-cooling-case.md` — green light found but not pursuing; GLP-1 space documented
  - `wiki/sources/src — Supplement Gummy Brand Launch Plan.md` — source summary
  - `wiki/sources/src — Three Product Comparison 2026-05-05.md` — source summary (simulated data)
- Pages updated (1):
  - `wiki/fba/fba-research-overview.md` — major rewrite: product confirmed, GLP-1 green lights documented, batches 4–10 added, priority queue updated, overview restructured
- Index updated: 51 → 55 pages
- Product decision: Supplement gummies confirmed. Three real H10 green lights (creatine 253 avg reviews, magnesium glycinate 994, NMN 776). Launch creatine first. Target: September/October 2026.
- Current FBA status: MsWLL dummy brand submitted to FBA-Pro for GTIN exemption. Waiting on approval.
- Key insight from full research run (80+ niches): Only strategy that found green lights was targeting products where the FORMAT is new (gummy supplement) or the market is forming around a new primary product (GLP-1 drugs). Established categories with broad keywords are universally closed (2,000–42,000 avg reviews).
- Contradictions: none
- Open questions:
  - What will the actual supplement brand name be? (MsWLL is placeholder only)
  - Which US GMP gummy manufacturer to use?
  - Current FDA status of NMN specifically?

---

## [2026-05-24] update | LegacyX Thinkific course — Branding module fully extracted; wiki updates across 6 pages

- Triggered by: Dave — "go through LegacyX course content and catch up to where i am"
- Note: Previous log entry at 2026-05-23 captured only 1/8 Branding lessons. All 8 Branding lessons were accessible in the existing raw file — rest ingested now.
- Page created (1):
  - `wiki/fba/fba-branding-gtin.md` — NEW: complete GTIN exemption + brand approval flow; brand naming rules; FBA Pro process; barcode types table; dummy listing 3-stage sequence; catalogue auth verification method
- Pages updated (5):
  - `wiki/fba/fba-account-setup-legal.md` — Full Brand Name section added (naming rules, 4-step check, trademark filing link, MsWLL status); Amazon account setup specifics (Pro account $39.99/mo, brand status = private label, UPC = no)
  - `wiki/fba/fba-tools-software.md` — Seller-Shark added to supporting tools; A2X new vs existing seller note
  - `wiki/fba/fba-compliance-suppression.md` — Restricted/Prohibited products section added; GTIN exemption note added to Section 4
  - `wiki/fba/fba-product-research-framework.md` — LegacyX H10 criteria vs our scraper table; Seller Sprite niche-down + rabbit hole strategy; open question on threshold alignment
  - `wiki/fba/fba-sourcing-alibaba.md` — 30-supplier rule; 2–4x Alibaba inflation confirmation; Trade Assurance 30-day payment protection
- Index updated: 55 → 56 pages
- Batch 11 scraper results (15 keywords): all FAIL — $346–$37,738/mo range, all below $50k floor. Cold plunge/bath tubs both around $3–4k/mo (tiny market). Walking pads $346/mo ($309 avg price — too expensive to enter). Oura ring case $33k but 590 avg reviews and $7 price point. No green lights.
- Fresh Thinkific scrape: in progress — results pending. Will update this entry if new lessons are unlocked.
- Key question raised: LegacyX uses $200k+ niche revenue threshold vs our $50k scraper floor. Difference is measurement scope (total niche vs single keyword). Review ceiling: LegacyX recommends ≤500 avg reviews vs our ≤1,000. Should probably tighten.
- Contradictions: None — new content consistent with existing wiki

---

## [2026-05-28] ingest | LegacyX Thinkific course — 52% complete, major content expansion

- Triggered by: Dave — comprehensive wiki update from newly scraped LegacyX course content (modules unlocked after gate cleared)
- Course progress: 45/115 → 64/115 (39% → 52%). Gate cleared: Creating Your First Listing 8/8 complete.
- Newly completed modules: Creating Your First Listing (8/8), Product Sourcing (5/5), Done For You Product Sourcing (5/5). Shipping started (1/8).
- Pages created (1):
  - `wiki/fba/fba-shipping.md` — NEW: EXW vs DDP, Freight Shark, FBA fee tiers and 18" threshold, volumetric weight, shipping plan overview
- Pages updated (5):
  - `wiki/sources/src — LegacyX FBA Full Course (Thinkific).md` — Progress updated to 52%, course table updated, key takeaways expanded (dummy listing 2025, FNSKU fix, variations, supplier outreach, negotiating, profitability, bosssourcing.com, Brand Registry), re-ingest plan updated
  - `wiki/fba/fba-sourcing-alibaba.md` — LegacyX supplier outreach protocol (15–20 direct contacts), negotiating masterclass (state quantity at target price, 45–60% net margin), profitability notes (35–45% target, volumetric weight, 18" threshold), Done For You section (bosssourcing.com, qcadvisor.com, gescmanagement.com caveat), margin rule updated
  - `wiki/fba/fba-branding-gtin.md` — FNSKU barcode preference fix, 2025 dummy listing creation steps, variations strategy (2–3 max, child first, review stacking), Brand Registry section (trademark, photo rules, Fiverr warning), Brand Approval vs Registry table updated
  - `wiki/system/index.md` — fba-shipping.md added, page count 56 → 57, priority actions updated, source entry updated
  - `CLAUDE.md` — Weekly Update section updated (date, brand approved, GTIN ready, course progress, actions)
- External status updates captured:
  - MsWLL Brand Qualification APPROVED across all stores/countries (Amazon email 2026-05-27)
  - GTIN exemption files ready for download at agency-studios.com/customer/orders/GTIN-001134 (30-day window)
- Contradictions: None — new content consistent with existing wiki
- Key scrape note: 3 shipping lessons had network errors (Creating A Shipping Plan x2, CRITICAL STEP Booking An Inspection) — must be watched directly in Thinkific
- Open questions: Full shipping plan creation steps (errored lessons), Freight Shark pricing, sea vs air decision for first order

---

## [2026-05-24] update | Thinkific scrape completed — Branding 8/8 confirmed, Creating Your First Listing next gate

- Triggered by: Fresh scrape run after Dave's "catch up to where I am" request
- Previous state: Branding On Amazon 1/8, everything else locked
- New state: **Branding On Amazon 8/8 ✅ COMPLETE** — all 8 lessons now accessible and previously ingested
- Creating Your First Listing: Intro lesson accessible, 6 video-only lessons timed out
- Everything from Product Sourcing onwards: still locked — gate is completing Creating Your First Listing
- Pages updated:
  - `wiki/sources/src — LegacyX FBA Full Course (Thinkific).md` — updated completion status, key takeaways, course table, re-ingest plan
- No new wiki content extractable from this scrape — Branding module was already fully ingested this session
- **Next scrape trigger:** Dave completes Creating Your First Listing (6 video lessons: FNSKU Setting Fix, Dummy Listing 2024, Dummy Listing 2025, Trademarking, How & Why of Variations, Creating Product Variations) → then run `python3 /tmp/thinkific_scraper.py`
- Sessions worth ingesting when unlocked: Product Sourcing, Shipping, Listing Creation, PPC (Kunze + Wilco methods)
