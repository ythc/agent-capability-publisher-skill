# Release hygiene

## Product-facing content

The project homepage should answer:

- What is this?
- Who is it for?
- How do I install it?
- How do I use it?
- What does it produce?
- What limitations or safety rules matter?

Keep rejected approaches, debugging chronology, and implementation detours out of the homepage.

## Preserve vs clean

Preserve:

- Git history;
- meaningful architecture decisions encoded in current docs;
- reusable scripts and templates;
- final demo media.

Clean:

- temporary render jobs;
- copied artifacts used only for one test;
- obsolete workflows;
- caches/build outputs;
- stale screenshots or videos replaced by a final version.

## Commit-message presentation

GitHub's file list shows the latest commit touching each path. There is no simple README setting that hides this column.

Do not rewrite history merely to make this column prettier. If the user explicitly wants normalized latest-commit labels while preserving history, explain that Git must touch those paths (or history must be rewritten), and get confirmation before any metadata-only workaround. Always verify final file modes/content after such an operation.

## Release summary

State separately:

- what was created;
- what was validated locally;
- what was tested against GitHub/Codex;
- what remains unverified.

Never turn a syntax check into a claim of end-to-end install success.
