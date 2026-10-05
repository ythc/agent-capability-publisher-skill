# Agent Capability Publisher

[English] | [简体中文](README.zh-CN.md)

**Agent Capability Publisher** is a Codex plugin that bundles an Agent Skill for turning requirements, examples, or an iterative workflow into a production-quality Skill, validating it, packaging it, documenting it, and preparing GitHub and Codex distribution.

Give Codex a workflow or a conversation that has already been refined over multiple turns. The Skill extracts the durable specification, designs the Skill structure, tests deterministic helpers, packages `skill.zip`, prepares human-facing documentation, and can wrap the result as a skills-only Codex Plugin.

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

## GitHub Connector authorization

When ChatGPT/Codex publishes through a GitHub Connector backed by a GitHub App, a newly created repository may still need to be explicitly added to that App's repository access.

If the App uses **Selected repositories**, use:

```text
GitHub
→ Settings
→ Applications
→ Installed GitHub Apps
→ current GitHub App
→ Configure
→ Repository access
→ Selected repositories
→ add the new repository
→ Save
```

After that, re-check the repositories visible to the installation before retrying the write.

If a repository exists but writes fail with:

```text
403 Resource not accessible by integration
```

check the GitHub App repository selection first.

## What it does

- **Requirements intake** — extracts the durable workflow from goals, examples, accepted decisions, constraints, and definition of done.
- **Skill design** — keeps `SKILL.md` compact, moves conditional detail into `references/`, and puts deterministic work into tested `scripts/`.
- **Validation and packaging** — uses the target validator/packager when available and produces a complete `skill.zip` when requested.
- **Codex packaging** — mirrors the finished Skill into a skills-only Plugin with a portable `plugin.json`, optional compatibility manifest, and repository marketplace entry.
- **GitHub release preparation** — creates product-facing README documentation, checks connector authorization, and applies release hygiene rules.
- **Verification** — checks plugin paths, manifests, temporary files, GitHub App repository access, and actual test status.

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

## Update

```bash
codex plugin marketplace upgrade agent-capability-publisher
```

Then start a new Codex session.

## Safety and release policy

The Skill does not rewrite Git history, force-push, change repository visibility, or publish secrets without explicit authorization. It treats syntax validation, script tests, GitHub upload, GitHub App repository authorization, and end-to-end Codex installation as separate states and reports them accurately.
