# Requirements intake

Use this before implementation. Ask only for details that are missing and material.

## Minimum contract

Resolve these fields:

| Field | What to capture |
| --- | --- |
| User goal | The repeatable outcome the Skill should deliver |
| Inputs | Files, URLs, repos, prompts, records, or connected-app data |
| Outputs | Artifacts, actions, edits, summaries, reports, videos, etc. |
| Trigger examples | Direct and indirect requests that should activate the Skill |
| Non-trigger examples | Adjacent requests that should not activate it |
| Tools/connectors | GitHub, Drive, Slack, MCP, browser, local filesystem, etc. |
| Constraints | Security, language, format, latency, cost, environment, permissions |
| Definition of done | How the user will judge the workflow successful |

## Concrete examples

Collect 2–5 examples. For each example, capture:

1. user request;
2. available context/input;
3. expected behavior;
4. expected output;
5. important failure/edge cases.

## Avoid redundant questions

If the conversation already established the input, output, connectors, or constraints, summarize them and proceed. Ask only when ambiguity would change implementation.

## Convert conversation history into requirements

Long iterative conversations often contain the best specification. Extract:

- decisions the user accepted;
- rejected approaches and why;
- quality problems discovered during real use;
- defaults that repeatedly worked;
- final product positioning;
- distribution expectations.

Do not copy the whole development story into the new Skill. Convert lessons into durable rules.
