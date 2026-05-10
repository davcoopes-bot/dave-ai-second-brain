#!/usr/bin/env python3
"""
Composio Setup Script for Dave's AI Brain
Wires up Composio API key, tests the connection, and connects key apps.

Usage:
    python3 setup_composio.py --key YOUR_API_KEY
    python3 setup_composio.py --key YOUR_API_KEY --connect gmail googlecalendar
    python3 setup_composio.py --test                    # Test existing connection
    python3 setup_composio.py --list-apps               # List connected apps
    python3 setup_composio.py --help
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


ZSHRC = Path.home() / ".zshrc"
VAULT_DIR = Path(__file__).resolve().parents[3]  # 3 levels up from scripts/
REPO_NAME = "davcoopes-bot/dave-ai-second-brain"


def add_to_zshrc(key: str) -> bool:
    """Permanently add COMPOSIO_API_KEY to ~/.zshrc."""
    marker = "COMPOSIO_API_KEY"

    if ZSHRC.exists():
        content = ZSHRC.read_text()
        if marker in content:
            # Update existing line
            lines = content.splitlines()
            new_lines = []
            for line in lines:
                if line.startswith(f"export {marker}="):
                    new_lines.append(f'export {marker}="{key}"')
                    print(f"✅ Updated existing {marker} in ~/.zshrc")
                else:
                    new_lines.append(line)
            ZSHRC.write_text("\n".join(new_lines) + "\n")
            return True

    # Append new line
    with ZSHRC.open("a") as f:
        f.write(f'\n# Composio — added by setup_composio.py\nexport {marker}="{key}"\n')
    print(f"✅ Added {marker} to ~/.zshrc")
    return True


def add_github_secret(key: str) -> bool:
    """Add COMPOSIO_API_KEY as a GitHub Secret via gh CLI."""
    print(f"\nAdding COMPOSIO_API_KEY to GitHub Secrets ({REPO_NAME})...")

    # Check if gh CLI is available
    result = subprocess.run(["which", "gh"], capture_output=True, text=True)
    if result.returncode != 0:
        print("⚠️  gh CLI not installed — skipping GitHub Secrets")
        print("   Install: brew install gh, then: gh auth login")
        print(f"   Or add manually at: https://github.com/{REPO_NAME}/settings/secrets/actions")
        return False

    # Check if authenticated
    auth_result = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    if auth_result.returncode != 0:
        print("⚠️  gh not authenticated — run: gh auth login")
        print(f"   Then add secret manually at: https://github.com/{REPO_NAME}/settings/secrets/actions")
        return False

    # Add the secret
    proc = subprocess.run(
        ["gh", "secret", "set", "COMPOSIO_API_KEY", "--repo", REPO_NAME, "--body", key],
        capture_output=True,
        text=True
    )
    if proc.returncode == 0:
        print("✅ COMPOSIO_API_KEY added to GitHub Secrets")
        return True
    else:
        print(f"⚠️  GitHub Secrets failed: {proc.stderr.strip()}")
        print(f"   Add manually at: https://github.com/{REPO_NAME}/settings/secrets/actions")
        return False


def test_connection(key: str) -> bool:
    """Test that the Composio API key works."""
    print("\nTesting Composio connection...")
    try:
        import composio
        client = composio.Composio(api_key=key)
        # Try to list connected apps — simplest API call
        apps = client.connected_accounts.get()
        print(f"✅ Connection successful — {len(apps)} apps connected")
        if apps:
            for app in apps:
                print(f"   • {app.app_name or app.id}")
        return True
    except ImportError:
        print("❌ composio not installed — run: pip3 install composio")
        return False
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("   Double-check your API key at platform.composio.dev")
        return False


def connect_app(key: str, app_name: str) -> bool:
    """Connect an app via Composio OAuth."""
    print(f"\nConnecting {app_name}...")
    try:
        import composio
        client = composio.Composio(api_key=key)

        # Check if already connected
        try:
            accounts = client.connected_accounts.get()
            for account in accounts:
                if app_name.lower() in (account.app_name or "").lower():
                    print(f"✅ {app_name} already connected")
                    return True
        except Exception:
            pass

        # Get OAuth URL
        connection_request = client.connected_accounts.initiate(
            app_name=app_name.upper(),
            user_id="dave",
            redirect_url=None
        )

        if hasattr(connection_request, 'redirect_url') and connection_request.redirect_url:
            print(f"\n🔗 Open this URL in your browser to authorize {app_name}:")
            print(f"   {connection_request.redirect_url}")
            print("\nPress Enter after authorizing in the browser...")
            input()

            # Verify connection
            accounts = client.connected_accounts.get()
            for account in accounts:
                if app_name.lower() in (account.app_name or "").lower():
                    print(f"✅ {app_name} connected successfully")
                    return True

            print(f"⚠️  {app_name} connection not detected — try again or check the Composio dashboard")
            return False
        else:
            print(f"⚠️  Could not get OAuth URL for {app_name}")
            return False

    except Exception as e:
        print(f"❌ Failed to connect {app_name}: {e}")
        return False


def list_connected_apps(key: str):
    """List all connected apps."""
    try:
        import composio
        client = composio.Composio(api_key=key)
        accounts = client.connected_accounts.get()

        if not accounts:
            print("No apps connected yet.")
            return

        print(f"\nConnected apps ({len(accounts)} total):")
        for account in accounts:
            name = account.app_name or account.id
            status = account.status or "unknown"
            print(f"  ✅ {name} ({status})")

    except ImportError:
        print("❌ composio not installed — run: pip3 install composio")
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Set up Composio for Dave's AI Brain vault.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 setup_composio.py --key sk_live_xxxx
  python3 setup_composio.py --key sk_live_xxxx --connect gmail googlecalendar
  python3 setup_composio.py --test
  python3 setup_composio.py --list-apps

Priority apps to connect first:
  gmail            → Email alerts for FBA GO verdicts and stock alerts
  googlecalendar   → Calendar read/write
  github           → Repo management (already connected via PAT)
  slack            → Message alerts to a channel (if you use Slack)

Get your API key at: https://platform.composio.dev
        """
    )
    parser.add_argument("--key", help="Composio API key (from platform.composio.dev)")
    parser.add_argument("--connect", nargs="+", metavar="APP",
                        help="Apps to connect via OAuth (e.g. gmail googlecalendar)")
    parser.add_argument("--test", action="store_true", help="Test existing connection")
    parser.add_argument("--list-apps", action="store_true", help="List connected apps")
    parser.add_argument("--skip-github", action="store_true",
                        help="Skip adding to GitHub Secrets")
    args = parser.parse_args()

    # Determine key to use
    key = args.key or os.environ.get("COMPOSIO_API_KEY")

    # List apps mode
    if args.list_apps:
        if not key:
            print("❌ No API key found. Set COMPOSIO_API_KEY or use --key")
            sys.exit(1)
        list_connected_apps(key)
        return

    # Test mode
    if args.test:
        if not key:
            print("❌ No API key found. Set COMPOSIO_API_KEY or use --key")
            sys.exit(1)
        test_connection(key)
        return

    # Full setup mode
    if not args.key:
        print("❌ API key required. Get it at platform.composio.dev then run:")
        print("   python3 setup_composio.py --key YOUR_KEY")
        sys.exit(1)

    print("=" * 55)
    print("Composio Setup — Dave's AI Brain")
    print("=" * 55)

    # Step 1: Add to ~/.zshrc
    print("\n1. Shell environment...")
    add_to_zshrc(args.key)

    # Step 2: Set for this session
    os.environ["COMPOSIO_API_KEY"] = args.key
    print("✅ Set for current session")

    # Step 3: Add to GitHub Secrets
    if not args.skip_github:
        print("\n2. GitHub Secrets...")
        add_github_secret(args.key)
    else:
        print("\n2. GitHub Secrets skipped (--skip-github)")

    # Step 4: Test the connection
    print("\n3. Testing connection...")
    if not test_connection(args.key):
        print("\n⚠️  Setup partially complete. Fix the connection issue and re-run.")
        sys.exit(1)

    # Step 5: Connect apps if requested
    if args.connect:
        print(f"\n4. Connecting apps: {', '.join(args.connect)}")
        for app in args.connect:
            connect_app(args.key, app)
    else:
        print("\n4. No apps requested. To connect Gmail:")
        print("   python3 setup_composio.py --connect gmail googlecalendar")

    print("\n" + "=" * 55)
    print("✅ Composio setup complete!")
    print("\nRestart your terminal or run:")
    print("   source ~/.zshrc")
    print("\nThen test with:")
    print("   python3 setup_composio.py --list-apps")
    print("=" * 55)


if __name__ == "__main__":
    main()
