# Codex Plugin publishing

Use current official OpenAI documentation before release because Plugin formats and install surfaces can evolve.

## Skills-only Plugin

A Plugin can contain only Skills. An MCP server is optional and should be omitted when the workflow needs only packaged instructions/resources.

Recommended portable shape:

```text
my-plugin/
├── plugin.json
└── skills/
    └── my-capability/
        ├── SKILL.md
        ├── agents/
        ├── scripts/
        ├── references/
        └── assets/
```

A root `.codex-plugin/plugin.json` compatibility manifest may also be present when useful.

## Repository marketplace

A repository can expose one or more plugins through:

```text
.agents/plugins/marketplace.json
```

Marketplace `source.path` values resolve from the marketplace/repository root, not from `.agents/plugins/`.

Typical repository:

```text
repo/
├── .agents/plugins/marketplace.json
└── plugins/
    └── my-plugin/
        ├── plugin.json
        └── skills/
            └── my-capability/
                └── SKILL.md
```

## Installation verification

Before placing commands in README, check the current OpenAI documentation. For a GitHub-backed marketplace, current Codex CLI supports a pattern like:

```text
codex plugin marketplace add owner/repo --ref main
codex plugin marketplace list
```

Then users can browse/install through the supported Plugin UI/surface. Do not assume a command remains valid forever; verify it at release time.

## Public directory vs repo marketplace

Treat these as separate distribution modes:

- **Repo/local marketplace**: useful for authoring, testing, team/private distribution.
- **Universal public directory**: requires the current OpenAI submission flow and publication metadata.

Do not claim a GitHub marketplace automatically publishes to the universal directory.

## Sync rule

Maintain one canonical Skill source during development. Before release, mirror the validated Skill into the plugin's `skills/<skill-name>/` directory with `scripts/sync_codex_plugin.py` or an equivalent deterministic step. Verify the copy matches the canonical Skill.
