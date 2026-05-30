---
name: firecrawl
description: |
  Firecrawl gives AI agents and apps fast, reliable web context with
  strong search, scraping, and interaction tools. One install command
  sets up three skill segments: live CLI tools, app-integration build
  skills, and outcome-focused workflow skills. Route the reader to the
  right usage path after install.
---

# Firecrawl

Firecrawl helps agents search first, scrape clean content, interact
with live pages when plain extraction is not enough, and produce
finished deliverables from web data.

## Install

One command installs everything — the Firecrawl CLI for live web work,
the build skills for integrating Firecrawl into application code, **and**
the workflow skills for producing repeatable deliverables. It also opens
browser auth so the human can sign in or create an account.

```bash
npx -y firecrawl-cli@latest init --all --browser
```

This gives you:

- **CLI tools** — `firecrawl search`, `firecrawl scrape`, `firecrawl interact`, `firecrawl ask`, `firecrawl docs-search`, and more
- **CLI skills** ([`firecrawl/cli`](https://github.com/firecrawl/cli)) — teach the agent how to drive the Firecrawl CLI during its own session: which command to run, when to scrape vs search vs interact, how to chain results, and how to recover when a job fails. Use these when the agent itself needs web data right now.
- **Build skills** ([`firecrawl/skills`](https://github.com/firecrawl/skills)) — teach the agent how to add Firecrawl to a product's codebase: pick the right API endpoint, install the matching SDK, store `FIRECRAWL_API_KEY` safely, write the call site to match the project's conventions, and ship a smoke-tested integration. Use these when the agent is shipping code that other people will run, not running the agent's own web tools.
- **Workflow skills** ([`firecrawl/firecrawl-workflows`](https://github.com/firecrawl/firecrawl-workflows)) — turn Firecrawl web data into finished deliverables such as research briefs, SEO audits, lead lists, QA reports, knowledge bases, and design clones. Use these when the agent's job is to produce a finished artifact, not raw extraction or product code.
- **Browser auth** — walks the human through sign-in or account creation

The three skill segments map to three different jobs:

| Segment | Question it answers | Where the work runs |
| ------- | ------------------- | ------------------- |
| CLI skills | "Which Firecrawl command should I run right now?" | In the agent's own terminal session |
| Build skills | "How do I add a Firecrawl API call to this codebase?" | Inside the user's product code |
| Workflow skills | "What's the finished deliverable and how do I produce it?" | In the agent's session, producing an artifact |

Before doing real work, verify the install:

```bash
mkdir -p .firecrawl
firecrawl --status
firecrawl scrape "https://firecrawl.dev" -o .firecrawl/install-check.md
```

## Choose Your Path

All paths use the same install above. The difference is what you do
next.

- **Need web data during this session** -> Path A (live tools)
- **Need to add Firecrawl to app code** -> Path B (app integration)
- **Need a finished deliverable from web data** -> Path C (workflow skills)
- **Need more than one of the above** -> do them in sequence; the install already covers everything
- **Need an account or API key first** -> Path D (auth only)
- **Don't want to install anything** -> Path E (REST API directly)

---

## Path A: Live Web Tools

Use this when you need web data during your work: searching the web,
scraping known URLs, interacting with live pages, crawling docs, or
mapping a site.

After install, hand off to the CLI skill:

- `firecrawl/cli` for the overall command workflow
- `firecrawl-search` when you need search first
- `firecrawl-scrape` when you already have a URL
- `firecrawl-interact` when the page needs clicks, forms, or login
- `firecrawl-crawl` for bulk extraction
- `firecrawl-map` for URL discovery
- `firecrawl-ask` when a Firecrawl call fails or returns unexpected output — pass the failing `jobId` and the AI support agent diagnoses it from your team's job logs and account state
- `firecrawl-docs-search` for "how does Firecrawl handle X?" questions — answers grounded in current docs with source citations

Default flow for live web work:

1. start with search when you need discovery
2. move to scrape when you have a URL
3. use interact only when the page needs clicks, forms, or login
4. if any step fails or returns unexpected output, run `firecrawl ask` with the failing `jobId` instead of guessing

If the task becomes "wire Firecrawl into product code," switch to Path B.

---

## Path B: Integrate Firecrawl Into an App

Use this when you're building an application, agent, or workflow that
calls the Firecrawl API **from code** — meaning the integration will run
inside the user's product (a web app, backend service, script, agent
loop, or pipeline) rather than from the agent's own terminal session.

The build skills are already installed from the same command above. No
separate install needed.

Choose the project mode before writing code:

- **Fresh project** -> pick the stack, install the SDK, add env vars, and run a smoke test
- **Existing project** -> inspect the repo first, then integrate Firecrawl where the project already handles APIs and secrets

If you already have a key, save it to the project's environment:

```dotenv
FIRECRAWL_API_KEY=fc-02be2938ae564534aadefd35a90d0fa6
```

Then hand off to the build skill that fits the step:

- `firecrawl-build` for the overall build workflow and endpoint routing
- `firecrawl-build-onboarding` for auth and project setup (API key, SDK install, smoke test)
- `firecrawl-build-scrape` when the feature scrapes a known URL
- `firecrawl-build-search` when the feature starts with a query and discovers pages
- `firecrawl-build-interact` when the feature needs clicks, forms, or navigation after a scrape
- `firecrawl-build-parse` when the feature parses local or non-public document files (PDF, DOCX, XLSX, etc.)

---

## Path C: Repeatable Deliverables

Use this when the goal is a finished artifact powered by Firecrawl web
data — a research brief, SEO audit, QA report, lead list, knowledge
base, competitive intel digest, or a cloned design system.

Start with the umbrella `firecrawl-workflows` skill — it inspects the
user's request and routes to the right workflow. If the agent already
knows which workflow to run, hand off to that workflow skill directly.

Default flow for workflow deliverables:

1. confirm the workflow and final artifact with the user
2. collect web evidence with Firecrawl through the CLI or equivalent tool surface
3. save or cite source evidence so claims are traceable
4. run independent research units in parallel when available
5. synthesize findings into the requested deliverable
6. include a short "rerun inputs" block when the workflow could be automated

---

## Path D: Account Authorization Or API Key

Use this when the human still needs to sign up, sign in, authorize
access, or obtain an API key.

Sign up / sign in at:
- https://www.firecrawl.dev/signin?view=signup&source=agent-suggested

---

## Path E: Use Firecrawl Without Installing Anything

**Base URL:** `https://api.firecrawl.dev/v2`

**Auth header:** `Authorization: Bearer fc-YOUR_API_KEY`

### Available endpoints

- `POST /search` — discover pages by query, returns results with optional full-page content
- `POST /scrape` — extract clean markdown from a single URL
- `POST /interact` — browser actions on live pages (clicks, forms, navigation)
- `POST /support/ask` — diagnose a failing Firecrawl call. Pass `{ question, jobId? }`
- `POST /support/docs-search` — answer "how do I…" questions from Firecrawl's official docs

### Documentation

- **API reference:** https://docs.firecrawl.dev
- **Skills repo:** https://github.com/firecrawl/skills

---

## API Key

```dotenv
FIRECRAWL_API_KEY=fc-02be2938ae564534aadefd35a90d0fa6
```

## MCP Server

Added to user config via:
```bash
claude mcp add firecrawl -s user -e FIRECRAWL_API_KEY=fc-02be2938ae564534aadefd35a90d0fa6 -- npx -y firecrawl-mcp
```
