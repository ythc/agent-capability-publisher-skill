# GitHub release workflow

## Repository content

A polished Skill repository usually needs:

- concise README in the user's preferred language(s);
- canonical Skill source;
- optional Codex Plugin/marketplace packaging;
- `.gitignore` for generated artifacts;
- license when the user chooses one;
- optional demo media when it demonstrates the finished capability.

## README order

Prefer this order:

1. one-sentence positioning;
2. demo or proof, when useful;
3. installation;
4. usage examples;
5. capabilities and outputs;
6. package/repository structure only if it helps users;
7. update instructions;
8. safety/limitations.

Avoid narrating the internal development history unless the user explicitly wants a changelog or engineering write-up.

## GitHub operations

When a GitHub connector is available:

1. inspect the target repository and permissions;
2. read current files before patching;
3. apply coherent updates;
4. verify the resulting tree/README from GitHub after writing;
5. preserve commit history by default.

Ask before:

- creating a new repository if the target is ambiguous;
- changing visibility;
- deleting branches/tags/releases;
- force-pushing or rewriting history;
- removing user content that is not clearly generated/staging material.

## Demo media

A demo produced by the capability itself is strong evidence. Describe it as a finished-output example, not as a story of how development happened.

## Generated files

Ignore or remove temporary working paths such as:

```text
.codebase-video/
render-jobs/current/
tts-jobs/current/
node_modules/
out/
__pycache__/
```

Keep reusable workflow templates; remove one-off workflow files created solely for a single render/test unless the repository intentionally uses them as permanent CI.
