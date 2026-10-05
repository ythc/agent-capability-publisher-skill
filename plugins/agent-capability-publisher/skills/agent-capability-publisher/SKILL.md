---
name: agent-capability-publisher
description: Turn a user-described repeatable workflow into a production-quality Agent Skill, validate and package it, document it for humans, optionally wrap it as a skill-only Codex Plugin, and publish or update the project on GitHub. Use when the user asks to create, refine, standardize, package, release, or publish a reusable Skill from requirements, examples, an existing workflow, or an iterative conversation; especially when the expected endpoint is a GitHub repository and Codex-installable plugin rather than only a local SKILL.md.
---

# Agent Capability Publisher

Build a reusable Agent Skill from the user's real workflow, then take it through validation, packaging, GitHub publication, and optional Codex Plugin distribution.

## Principles

- Treat the user's actual goal and examples as the source of truth.
- Separate **Skill behavior** from **repository presentation** and **plugin distribution**.
- Keep `SKILL.md` concise; move detail into `references/`; put deterministic operations in `scripts/`.
- Validate and test before publishing. Never claim an install path works only because its syntax looks plausible.
- Prefer current official platform documentation for Codex/Plugin behavior over memory.
- Keep public README/video content focused on the finished capability, not the development diary.
- Preserve Git history by default. Never rewrite or force-push history without explicit approval.

## Workflow

1. **Understand the workflow.**
   - Read `references/requirements-intake.md`.
   - Identify expected input, expected output, triggering requests, connectors/tools, constraints, and 2–5 concrete examples.
   - Reuse context already established in the conversation; do not re-ask questions that are already answered.

2. **Research the target ecosystem when it matters.**
   - For ChatGPT/Codex/OpenAI Plugin details, verify current official documentation before choosing manifests, install commands, or publication steps.
   - For domain-specific Skills, inspect representative high-quality public Skills only when doing so materially improves the design.
   - Record only stable, task-relevant conventions in the Skill; do not copy repository-specific noise.

3. **Design the Skill.**
   - Read `references/skill-design.md`.
   - Choose a short lowercase hyphenated name; avoid including the word `skill` in a new Skill name unless the ecosystem requires it.
   - Decide which behavior belongs in `SKILL.md`, which detail belongs in `references/`, and which fragile/repeatable operations belong in `scripts/`.
   - Make the frontmatter description describe both capability and triggering conditions.

4. **Initialize and implement.**
   - If an official Skill initializer is available, use it for a new Skill.
   - Remove placeholder files before delivery.
   - Add only resources that improve reliability or reuse.
   - Test every new deterministic script by actually running it. For a family of similar scripts, test a representative sample plus any high-risk branches.

5. **Validate and package the Skill.**
   - Use the official validator/packager when available.
   - Produce a complete archive named exactly `skill.zip` when the user expects a Skill deliverable.
   - Keep the packaged Skill focused on `SKILL.md`, `agents/`, `scripts/`, `references/`, and `assets/` as needed; keep GitHub README/demo material outside the Skill bundle.

6. **Prepare the GitHub repository.**
   - Read `references/github-release.md`.
   - Create concise human-facing README documentation covering: what it is, install/use, examples, outputs, and safety/limitations.
   - Do not write a development diary into the project homepage unless the user explicitly asks for one.
   - Add `.gitignore` entries for generated work products and temporary render/build jobs.
   - Never expose credentials, tokens, `.env` values, private keys, or connector secrets.

7. **Package as a Codex Plugin when installability is a goal.**
   - Read `references/codex-plugin-publishing.md`.
   - Prefer the current portable root `plugin.json` format and `skills/` directory. Add `.codex-plugin/plugin.json` only when compatibility metadata is useful.
   - Use `scripts/sync_codex_plugin.py` to mirror the finished Skill into a plugin package and create a repo marketplace entry.
   - A skills-only plugin does not need an MCP server.
   - Verify the marketplace source path resolves from the marketplace root.

8. **Publish with the GitHub connector or Git.**
   - Create/update files in coherent commits rather than one commit per line-level edit when practical.
   - If the user has not authorized creating a new repository, changing visibility, overwriting a shared file, deleting history, or force-pushing, ask first.
   - After upload, read the repository back and verify required files, paths, README links, and manifests.

9. **Verify installability.**
   - Run `scripts/check_release.py --repo-root <repo>` against a local checkout when available.
   - Confirm current official Codex install commands before putting them in README.
   - For a repo marketplace, verify `.agents/plugins/marketplace.json`, plugin source path, root `plugin.json`, and `skills/<name>/SKILL.md` all resolve correctly.
   - When possible, test discovery/install in a clean Codex session before calling the release complete.

10. **Polish the release.**
    - Read `references/release-hygiene.md`.
    - Keep demos product-focused. A self-generated demo is valuable evidence when it demonstrates the finished capability.
    - Remove one-off TTS/render jobs, temporary workflows, caches, and generated staging directories before final publication unless they are intentionally reusable infrastructure.
    - Preserve historical commits by default. If the user wants GitHub's file-list “latest commit” column normalized, explain that this requires touching those paths or rewriting history and get explicit approval before using either technique.

## Decision tree

```text
User wants a reusable workflow
├─ Requirements/examples incomplete
│  └─ Ask targeted questions
├─ Existing Skill to update
│  └─ Preserve structure → edit → validate → repackage
└─ New Skill
   └─ initialize → implement → test → validate → package

Need GitHub publication?
├─ No
│  └─ deliver skill.zip
└─ Yes
   ├─ Human repo only
   │  └─ README + source + release QA
   └─ Codex-installable
      └─ Skill → Plugin skills/ → marketplace → install verification
```

## Output contract

When the user asks for the complete workflow, aim to deliver:

- a validated Skill source directory;
- `skill.zip` when a standalone Skill package is useful;
- tested helper scripts and focused references;
- a GitHub repository with polished README documentation;
- when requested, a skills-only Codex Plugin package and repo marketplace entry;
- verified installation instructions based on current official documentation;
- a short release summary that distinguishes what was actually tested from what remains unverified.

## Guardrails

- Do not infer missing user requirements when they materially change the Skill's behavior.
- Do not duplicate huge documentation dumps into `SKILL.md`.
- Do not include repository README/demo assets inside `skill.zip` unless the Skill itself needs them at runtime.
- Do not create or publish an MCP server for a skills-only workflow unless the capability actually needs live tools/data.
- Do not create a new public GitHub repository or alter repository visibility without user approval.
- Do not rewrite Git history or force-push by default.
- Do not call a workflow “tested” until its relevant validator/scripts/install path have actually run.

## References

- Read `references/requirements-intake.md` before requirement discovery.
- Read `references/skill-design.md` before structuring a new or heavily revised Skill.
- Read `references/codex-plugin-publishing.md` when Codex installation/distribution is requested.
- Read `references/github-release.md` before creating or updating a GitHub repository.
- Read `references/release-hygiene.md` before final cleanup and handoff.
