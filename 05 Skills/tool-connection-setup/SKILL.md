---
name: tool-connection-setup
description: >
  Connect any external tool or data source to Claude via API or MCP. Use this skill when Dave says
  "connect this tool", "add [tool] to the system", "I want Claude to be able to access [tool]",
  "set up the [tool] integration", "wire up [tool]", or any time a new external service needs to be
  reachable. Output is a tested, working connection with documentation saved to the wiki.
---

# Skill: Tool Connection Setup

Wire any tool into the vault properly. API-first — no MCP unless there's no API. Every connection gets documented so it doesn't need to be re-figured out next time.

---

## Before Starting

Run `ai-decision-filter` if there's any question about whether this connection is worth building. Don't spend an hour integrating a tool Dave's going to use twice.

---

## Step 1 — Create a Dedicated API Access Point

In the tool being connected:
- Create a dedicated API key or OAuth token specifically for Claude
- Set the minimum permissions required — read-only if that's all that's needed
- Name it clearly (e.g. "Claude vault integration") so it's obvious what it's for

Do not reuse personal API keys.

---

## Step 2 — Research the API

Search for the tool's official API documentation. Extract and save:
- Authentication method (API key, Bearer token, OAuth)
- The specific endpoints Claude will actually use (not the full API — just what's needed)
- Request and response formats for those endpoints
- Rate limits
- Any common gotchas or auth edge cases

Save this to `06 Wiki/wiki/research/(C) [Tool] API Reference.md`.

Template:
```markdown
# (C) [Tool] API Reference

> **Last updated:** [date]
> **Auth method:** [API key / Bearer / OAuth]
> **Base URL:** [url]

## Endpoints Used

### [Endpoint name]
- **URL:** `[method] /path`
- **Auth:** [how to authenticate]
- **Params:** [key params]
- **Response:** [what comes back]
- **Rate limit:** [limit]

## Gotchas
- [Any known issues]
```

---

## Step 3 — Store Credentials Securely

Do not hardcode API keys in skill files or wiki pages. Instead:
- Note in `CLAUDE.md` that this connection exists and what it's called
- Dave stores the actual key in his environment or password manager
- Reference the key by name in any skill that uses it (e.g. `HELIUM10_API_KEY`)

---

## Step 4 — Test the Connection

Run the simplest possible read operation using the API. Show Dave the raw result.

If it fails:
- Check auth format (Bearer vs. plain key, header name)
- Check rate limits and account tier
- Update the API reference doc with what was learned
- Try again

Don't move on until a successful response is confirmed.

---

## Step 5 — Optimise for Token Efficiency

Once working, identify exactly which endpoints were used. For any skill that calls this tool:
- Embed those endpoint details directly in the skill file
- Don't make Claude re-read the full API reference every session — that's wasteful

---

## Step 6 — Update CLAUDE.md

Add the new connection to `CLAUDE.md` under a connections section:

```markdown
## Active Connections
- **[Tool name]** — [what it can do] — API docs at `06 Wiki/wiki/research/(C) [Tool] API Reference.md`
```

---

## Step 7 — Log It

Append to `06 Wiki/system/log.md`:

```
## [YYYY-MM-DD] | Tool Connected — [Tool Name]
- Auth method: [type]
- Endpoints active: [list]
- Reference doc: wiki/research/(C) [Tool] API Reference.md
- Test result: [passed / notes]
```

---

## Rules

- API first, always — MCP only if no API exists
- Test before declaring it done — an untested connection is a liability
- Document the endpoints actually used, not the entire API
- Minimum permissions only — don't give Claude write access if read is enough
- If the connection fails after 3 attempts, stop and flag it to Dave rather than guessing
