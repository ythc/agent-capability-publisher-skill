#!/usr/bin/env python3
"""Mirror a validated Skill into a skills-only Codex Plugin + repo marketplace."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

EXCLUDES = {"__pycache__", ".git", "node_modules", "out", ".codebase-video"}


def ignore(_dir: str, names: list[str]) -> set[str]:
    return {n for n in names if n in EXCLUDES or n.endswith(".pyc")}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--skill-dir", required=True)
    p.add_argument("--repo-root", required=True)
    p.add_argument("--plugin-name", required=True)
    p.add_argument("--version", default="0.1.0")
    p.add_argument("--description", required=True)
    p.add_argument("--display-name", required=True)
    p.add_argument("--short-description", default="")
    p.add_argument("--long-description", default="")
    p.add_argument("--default-prompt", default="")
    p.add_argument("--author-name", required=True)
    p.add_argument("--repository-url", default="")
    p.add_argument("--marketplace-name", default="")
    p.add_argument("--category", default="Developer Tools")
    p.add_argument("--force", action="store_true")
    a = p.parse_args()

    skill = Path(a.skill_dir).resolve()
    repo = Path(a.repo_root).resolve()
    if not (skill / "SKILL.md").is_file():
        raise SystemExit(f"SKILL.md not found: {skill}")
    if not repo.is_dir():
        raise SystemExit(f"Repo root not found: {repo}")

    short = a.short_description or a.description
    if len(short) > 30:
        raise SystemExit("--short-description must be at most 30 characters")

    skill_name = skill.name
    plugin = repo / "plugins" / a.plugin_name
    dest = plugin / "skills" / skill_name
    if dest.exists():
        if not a.force:
            raise SystemExit(f"Destination exists: {dest}; use --force")
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill, dest, ignore=ignore)

    interface = {
        "displayName": a.display_name,
        "shortDescription": short,
        "longDescription": a.long_description or a.description,
        "developerName": a.author_name,
        "category": a.category,
        "capabilities": ["Read", "Write"],
    }
    if a.default_prompt:
        interface["defaultPrompt"] = a.default_prompt

    root_manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": a.plugin_name,
        "version": a.version,
        "description": a.description,
        "author": {"name": a.author_name},
        "extensions": {"com.openai": {"interface": interface}},
    }
    if a.repository_url:
        root_manifest["homepage"] = a.repository_url
        root_manifest["repository"] = a.repository_url
    plugin.mkdir(parents=True, exist_ok=True)
    (plugin / "plugin.json").write_text(
        json.dumps(root_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    compat = {
        "name": a.plugin_name,
        "version": a.version,
        "description": a.description,
        "author": {"name": a.author_name},
        "skills": "./skills/",
        "interface": interface,
    }
    if a.repository_url:
        compat["homepage"] = a.repository_url
        compat["repository"] = a.repository_url
    compat_dir = plugin / ".codex-plugin"
    compat_dir.mkdir(exist_ok=True)
    (compat_dir / "plugin.json").write_text(
        json.dumps(compat, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    market_name = a.marketplace_name or a.plugin_name
    market = {
        "name": market_name,
        "interface": {"displayName": a.display_name},
        "plugins": [
            {
                "name": a.plugin_name,
                "source": {"source": "local", "path": f"./plugins/{a.plugin_name}"},
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                    "products": ["CODEX"],
                },
                "category": a.category,
            }
        ],
    }
    market_dir = repo / ".agents" / "plugins"
    market_dir.mkdir(parents=True, exist_ok=True)
    (market_dir / "marketplace.json").write_text(
        json.dumps(market, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Plugin: {plugin}")
    print(f"Skill mirror: {dest}")
    print(f"Marketplace: {market_dir / 'marketplace.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
