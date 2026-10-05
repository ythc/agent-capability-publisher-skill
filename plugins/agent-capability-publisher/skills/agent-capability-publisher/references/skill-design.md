# Skill design

## Structure

Prefer:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── scripts/        # deterministic operations
├── references/     # detailed guidance loaded only when needed
└── assets/         # templates/resources used in outputs
```

Not every directory is required.

## SKILL.md as control plane

Keep `SKILL.md` concise and operational. It should contain:

- capability and invariants;
- high-level sequential workflow;
- important decision branches;
- guardrails;
- pointers explaining exactly when to read each reference.

Move long platform instructions, schemas, troubleshooting, and checklists into `references/`.

## Frontmatter

Use only the fields accepted by the target validator. For a portable Skill, default to:

```yaml
---
name: short-hyphen-name
description: What it does. Use when ...
---
```

The description is the activation mechanism. Include what the Skill does and when it should be used.

## Scripts

Use scripts when a step is fragile, deterministic, or repeatedly reimplemented. Give scripts stable CLI interfaces and meaningful `--help` output. Treat them as black boxes first; read or patch implementation only when needed.

Test scripts before packaging. Do not ship placeholders.

## References

Use references for details that are valuable but not always needed. Keep them one level away from `SKILL.md`. Add a table of contents to long references.

## Assets

Use assets for output templates or boilerplate that should be copied rather than reasoned over. Do not put developer documentation in assets just to avoid organizing it.

## Packaging boundary

The Skill bundle is for agent runtime. The GitHub repository is for humans and distribution. README files, demo videos, release notes, and repository badges normally belong outside `skill.zip` unless the Skill itself consumes them.
