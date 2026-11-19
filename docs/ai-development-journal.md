# AI Development Journal

Use this journal to make AI-assisted development visible and reproducible.

For each substantial AI-assisted change, record:

- the goal and relevant context provided to the tool
- the suggestions or code produced
- what you accepted, changed, or rejected
- tests and other verification performed
- limitations, risks, or follow-up work

## 2026-11-18: Documentation templates

- **Goal and context:** Expand the starter's brief documentation prompts into
  simple SRS and architecture templates so students can focus on requirements
  quality and architectural reasoning during the holiday-week milestone.
- **AI assistance:** Codex proposed and drafted structured Markdown sections,
  requirement and decision tables, traceability prompts, and editable Mermaid
  diagrams. It also linked the templates from the README.
- **Review decisions:** The existing `docs/requirements.md` and
  `docs/architecture.md` locations were retained as the single, obvious places
  for evolving project documentation. The templates use optional prompts and
  stable identifiers without prescribing a student project's features or
  schema. No new documentation tooling or dependency was added.
- **Verification:** Markdown structure, internal links, placeholder consistency,
  whitespace, and Python source compilation were checked. The existing test
  suite was also attempted, but `pytest` was not installed in the available
  environment.
- **Limitations and follow-up:** Each team must replace the example content,
  remove sections that do not apply, keep requirements measurable, and update
  architecture decisions and traceability as implementation evolves.
