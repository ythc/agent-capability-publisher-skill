# Agent Capability Publisher

**Agent Capability Publisher** is a Codex plugin that bundles an Agent Skill for turning a repeatable workflow into a production-quality Skill, validating it, packaging it, documenting it, and preparing it for GitHub and Codex distribution.

Give Codex a workflow, requirements, examples, or an existing iterative conversation. The Skill extracts a durable specification, designs the Skill structure, tests deterministic helpers, packages `skill.zip`, prepares a human-facing repository, wraps the Skill as a skills-only Codex Plugin when requested, and verifies release structure before handoff.

## Install in Codex

Add this repository as a plugin marketplace:

```bash
codex plugin marketplace add ythc/agent-capability-publisher-skill --ref main
```

Then start Codex:

```bash
codex
```

Open:

```text
/plugins
```

Choose **Agent Capability Publisher**, select **Install plugin**, then start a new Codex session.

## Use it

Examples:

```text
Turn this workflow into a reusable Agent Skill, validate it, package it, and prepare it for GitHub and Codex distribution.
```

```text
We refined this process over several messages. Extract the final requirements, create the Skill, test it, package it, and publish the finished project without putting the development diary in the README.
```

```text
Update this existing Skill, preserve its structure, revalidate it, rebuild the Codex plugin package, and prepare the GitHub release.
```

## What it does

- **Requirements intake** — extracts the durable workflow from goals, examples, accepted decisions, constraints, and definition of done.
- **Skill design** — keeps `SKILL.md` compact, moves conditional detail into `references/`, and puts deterministic work into tested `scripts/`.
- **Validation and packaging** — uses the target validator/packager when available and produces a complete `skill.zip` when requested.
- **Codex packaging** — mirrors the finished Skill into a skills-only Plugin with a portable `plugin.json`, optional compatibility manifest, and repo marketplace entry.
- **GitHub release preparation** — creates concise product-facing README documentation and release hygiene rules.
- **Verification** — checks plugin paths, manifests, temporary files, and clearly separates what was actually tested from what remains unverified.

## Plugin layout

```text
.agents/plugins/marketplace.json

plugins/agent-capability-publisher/
├── plugin.json
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── agent-capability-publisher/
        ├── SKILL.md
        ├── agents/
        ├── scripts/
        └── references/
```

The installable Skill source lives directly under `plugins/agent-capability-publisher/skills/agent-capability-publisher/`. Repository documentation is kept outside the Skill runtime package.

## Update

```bash
codex plugin marketplace upgrade agent-capability-publisher
```

Then start a new Codex session.

## Safety and release policy

The Skill does not rewrite Git history, force-push, change repository visibility, or publish secrets without explicit authorization. It treats syntax validation, local tests, GitHub upload, and end-to-end Codex install verification as separate states and reports them accurately.
