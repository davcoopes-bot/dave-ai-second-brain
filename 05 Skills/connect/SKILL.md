---
name: connect
description: Connect Claude to external apps and services — Gmail, Slack, Google Calendar, GitHub and 1000+ others — using Composio. Enables Claude to take real actions (send emails, create tasks, post alerts, read calendar) instead of just generating text. Use when Dave says "connect [app]", "set up Gmail", "wire up [service]", "I want Claude to email me alerts", "connect Composio", or when setting up a new external integration for the vault or remote agents.
---

# Connect — External App Integration

To wire any external service into Claude so it can take real actions, not just describe them. The core integration layer is **Composio** — it handles OAuth, tokens, and the actual API calls so Claude doesn't have to.

---

## Status

| What | Status |
|------|--------|
| `composio` Python package | ✅ Installed (`pip3 install composio`) |
| Composio API key | ⏳ Needed — see Step 1 |
| Gmail | ⏳ Not connected |
| Google Calendar | ⏳ Not connected |
| GitHub | ⏳ Not connected |

---

## Step 1 — Get API Key (One-Time)

1. Go to [platform.composio.dev](https://platform.composio.dev) → sign up free
2. Copy the API key from Settings
3. Set it permanently in the shell:

```bash
echo 'export COMPOSIO_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

4. Also add it as a GitHub Secret for remote agents:
   - Go to the vault repo → Settings → Secrets → Actions
   - Add secret named `COMPOSIO_API_KEY`

---

## Step 2 — Connect an App

Run the connect flow from Terminal. Composio opens a browser OAuth window:

```bash
python3 -c "
from composio import Composio
import os

composio = Composio(api_key=os.environ['COMPOSIO_API_KEY'])

# Replace 'gmail' with: slack, github, googlecalendar, notion, etc.
url = composio.get_auth_url('gmail', user_id='dave')
print('Open this URL to connect Gmail:', url)
"
```

After authorizing in the browser, connection persists. No need to re-auth each session.

**Supported apps (key ones for this vault):**

| App | Use case |
|-----|----------|
| `gmail` | Email alerts when FBA agent finds a GO verdict |
| `googlecalendar` | Read/create calendar events |
| `github` | Read commits, create issues, check CI |
| `slack` | Send stock alerts or FBA updates to a channel |
| `notion` | Sync vault summaries to Notion (if needed) |

---

## Step 3 — Use Composio in a Skill or Script

Once connected, call it from any Python script:

```python
from composio import Composio
from composio.tools import Action
import os

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])

# Example: Send an email
result = composio.execute(
    action=Action.GMAIL_SEND_EMAIL,
    params={
        "to": "davcoopes@gmail.com",
        "subject": "FBA Alert — Green Light: Cable Management Box",
        "body": "The overnight agent found a GO verdict on cable management box. Score: 78/100.\n\nCheck the vault for details."
    },
    user_id="dave"
)
print(result)
```

---

## Step 4 — Use in Remote Agents (Rube MCP)

For remote CCR agents running in Anthropic's cloud, use Rube MCP (no code required):

1. Connect at [rube.app/mcp](https://rube.app/mcp) — OAuth connects your Composio account
2. Add Rube as an MCP connector in the routine via the Claude.ai UI
3. Agent prompt references the integration directly:

```
After research is complete, if any niche scores above 70/100, 
use the Gmail MCP tool to email davcoopes@gmail.com with a 
subject "FBA Alert — GO Verdict" and a summary of the findings.
```

---

## Vault-Specific Use Cases

### FBA Research Alerts
- FBA agent finds GO verdict → email Dave immediately (don't wait for next vault pull)
- Agent reaches 10 researched niches → email a digest

### Stock Monitoring Alerts
- Stock agent detects >10% move on EXR or NBIS → immediate email alert
- Weekly stock summary every Friday afternoon

### Calendar Integration
- Read Dave's calendar before scheduling anything
- Add reminders for sample order follow-ups

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `COMPOSIO_API_KEY not set` | Run `source ~/.zshrc` or set key manually |
| Auth required message | Open the URL Composio prints, authorize, re-run |
| Action failed | Check permissions in target app settings |
| Tool not found | Use the exact action name from Composio docs |

---

## Security Rules

- The API key gives access to connected apps — keep it out of commits and wiki pages
- Store in `~/.zshrc` locally and GitHub Secrets for remote agents
- Set minimum permissions on connected apps (read-only where possible)
- Name connections clearly in the Composio dashboard so they're auditable

---

## References

- Composio dashboard: [platform.composio.dev](https://platform.composio.dev)
- Rube MCP: [rube.app/mcp](https://rube.app/mcp)
- Composio Python docs: `pip3 show composio` for local version
