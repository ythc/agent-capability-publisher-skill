#!/usr/bin/env python3
"""Check common Skill + Codex Plugin + GitHub release structure."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", required=True)
    p.add_argument("--plugin-name", default="")
    a = p.parse_args()
    root = Path(a.repo_root).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        raise SystemExit(f"Repo root not found: {root}")
    if not (root / "README.md").is_file() and not (root / "README.zh-CN.md").is_file():
        warnings.append("No README found")
    for d in ["render-jobs/current", "tts-jobs/current", ".codebase-video"]:
        if (root / d).exists():
            warnings.append(f"Temporary path still exists: {d}")

    market = root / ".agents/plugins/marketplace.json"
    if market.is_file():
        try:
            m = json.loads(market.read_text(encoding="utf-8"))
        except Exception as e:
            fail(f"Invalid marketplace JSON: {e}", errors)
            m = {}
        for entry in m.get("plugins", []):
            path = entry.get("source", {}).get("path", "")
            if not path.startswith("./"):
                fail(f"Marketplace source.path must start with ./: {path}", errors)
            if path:
                resolved = (root / path[2:]).resolve()
                if not resolved.exists():
                    fail(f"Marketplace path does not exist: {path}", errors)
    elif a.plugin_name:
        fail("Missing .agents/plugins/marketplace.json", errors)

    if a.plugin_name:
        plugin = root / "plugins" / a.plugin_name
        pm = plugin / "plugin.json"
        if not pm.is_file():
            fail(f"Missing {pm.relative_to(root)}", errors)
        else:
            try:
                data = json.loads(pm.read_text(encoding="utf-8"))
            except Exception as e:
                fail(f"Invalid plugin.json: {e}", errors)
                data = {}
            if data.get("name") != a.plugin_name:
                fail("plugin.json name mismatch", errors)
            if not re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("version", ""))):
                fail("plugin.json version must be strict semver x.y.z", errors)
            interface = data.get("extensions", {}).get("com.openai", {}).get("interface", {})
            short = interface.get("shortDescription", "")
            if short and len(short) > 30:
                fail("shortDescription exceeds 30 characters", errors)
            if not data.get("author", {}).get("name"):
                warnings.append("plugin.json has no author.name")

        skills = plugin / "skills"
        entries = list(skills.glob("*/SKILL.md")) if skills.exists() else []
        if not entries:
            fail(f"No skills/*/SKILL.md under plugins/{a.plugin_name}", errors)
        for md in entries:
            txt = md.read_text(encoding="utf-8")
            match = re.match(r"^---\n(.*?)\n---", txt, re.S)
            if not match:
                fail(f"Invalid frontmatter: {md}", errors)
            elif "name:" not in match.group(1) or "description:" not in match.group(1):
                fail(f"Missing skill name/description: {md}", errors)

    print("Release check")
    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
