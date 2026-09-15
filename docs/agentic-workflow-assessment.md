# Agentic wiki workflow assessment (historical)

**September 13 update:** The fixed scheduling recommendation below is superseded
by the implemented [bounded curator](agentic-workflow.md). The Claude Agent SDK
choice and token-efficiency rationale remain. The curator now selects editorial
actions and topic membership; code enforces coverage, dependencies, budgets and
promotion. This document preserves the earlier research and baseline observations,
not a description of the current implementation or current validation results.

Assessed September 12, 2026, against `bafdfe9` on `feat/agentic-workflow`.
This supersedes the earlier recommendation to start with interactive CLI skills.

**Build a Python workflow using the Claude Agent SDK, authenticated through the
maintainer's Claude subscription. Optimize the workflow around accepted scientific
changes per unit of subscription allowance.** Keep deterministic scheduling,
validation, state, and publishing in code. Use bounded agents for evidence
extraction, editorial planning, page edits, and scientific review.

The priority is token efficiency and maintainability, not avoiding custom code.
Choose this architecture now. Do not fund a succession of alternative runtimes
or full-corpus compilations to decide between them. No implementation or model
generation has been performed as part of this assessment.

Why this SDK

Claude's SDK supports a custom system prompt and a minimal default, unlike the
normal Claude Code CLI prompt. We can load the wiki contract explicitly and omit
unrelated coding instructions. This is a concrete way to control recurring
context overhead. A custom prompt must retain the necessary source-trust,
tool-use, and permission instructions.
[System prompt documentation](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts).

Its Python in-process MCP tools can expose existing validation and source
retrieval functions without a separate tool service. Sessions, structured
results, hooks, and turn limits provide programmatic control.
[Custom tools](https://code.claude.com/docs/en/agent-sdk/custom-tools),
[Python SDK](https://code.claude.com/docs/en/agent-sdk/python).

Codex SDK is a capable alternative, including a Python implementation. There is
no evidence here that Claude's models inherently use fewer tokens or produce
better science. Claude is the architectural choice because its documented
custom-prompt and in-process Python-tool path directly fits this non-coding
compiler. Codex app-server's direct dynamic-tool protocol is currently
experimental; Codex can also use MCP, so that is not a general capability gap.
Do not implement both backends now.
[Codex SDK](https://developers.openai.com/codex/sdk),
[Codex app-server](https://developers.openai.com/codex/app-server).

Skills can hold optional authoring guidance, but the SDK runner should explicitly
load the required contract and enforce completion. Skill discovery and a
conversation's assertion of success should not control the pipeline.

The SDK does not intrinsically make an equivalent model run cheaper. It makes
context, tools, stopping conditions, and accepted outputs controllable. The
largest expected savings come from reorganizing work, not changing the client.

What the code inspection establishes

The package has 5,847 lines of Python. The inspected corpus has 75 source
documents, 75 summaries, 92 concepts, 335 entities, nine hubs, 41 conflicts,
19 author pages, and 15 data pages, including some collection indexes. Reports
reach about 300 KB and concept/entity pages reach roughly 55–62 KB.

- [compiler.py](../src/beril_wiki/compiler.py) plans per document and rewrites
  each affected page in full. Multiple new reports can repeatedly rewrite the
  same large page. Its resume guard uses source membership, which does not
  establish that a changed version of that source was integrated.
- [enrich.py](../src/beril_wiki/stages/enrich.py) encourages concept creation
  after compilation discourages it; [consolidate.py](../src/beril_wiki/stages/consolidate.py)
  then judges overlap and back-merges evidence. These editorial obligations can
  be planned together instead of automatically running compensating generation
  passes over the corpus.
- Topics truncate concept input at 7,000 characters. Literature generation
  currently receives titles and bibliographic metadata, not paper content.
  Smaller context is not useful if it removes the evidence needed for correctness.
- Topics, conflicts, and figures have separate completion calls. Embeddings
  are another API dependency. Changing only `compiler.llm()` would not complete
  a subscription migration.
- The current dollar tripwire is process-local and bypassed by some stages.
  Consolidation computes embeddings before candidate-level skips. Put
  invalidation and accounting ahead of all inference.
- Existing checks protect citations, selected numbers, links, and some merge
  retention, but do not establish semantic correctness, units, direction,
  denominators, or complete retention of caveats.

The previous inspection in this session ran all 50 tests successfully and the
strict corpus check returned zero errors and eight warnings over 571 pages.
These results were not rerun for this documentation revision. No full build,
paid generation, embedding call, or account-usage measurement was performed.

The proposed workflow

1. **Compute the work in Python.** Hash source revisions and relevant configuration,
   compare them with accepted outputs, and identify changed/deleted inputs.
   An unchanged run stops before invoking a model. Track prompt, schema, model,
   tool, and dependency revisions so stale results cannot masquerade as a hit.
2. **Extract reusable evidence once per changed report.** Save a compact structured
   record of findings, exact supporting source spans, caveats, null results,
   entities, and figure references. Process long reports in explicit sections
   with a coverage manifest; do not silently truncate them. Validate quoted spans
   against source bytes. These records support summaries and integration rather
   than duplicating a separate expensive extraction for every downstream writer.
3. **Plan integration for the update batch.** Supply compact existing page briefs
   and evidence records to a bounded editorial planner. It chooses affected pages,
   missing concepts, identity questions, and potential conflicts. Code groups
   proposed changes by destination page. Retain the existing concept-decisions
   manifest and deterministic candidate signals.
4. **Update each affected page once per batch.** Give its writer the existing page
   and all relevant new evidence. Return section replacements or anchored patches
   when practical, rather than re-emitting unchanged prose. A new page or genuine
   structural rewrite can still require a full output. Code verifies the base
   hash and patch anchors, reconstructs the page, and validates the complete result.
5. **Review the changed science and finish affected outputs.** Review changed and
   deleted claims against their source evidence, including unsupported inferences,
   lost caveats, and contradictions. Preserve deterministic checks over the whole
   corpus. Generate dependent hubs, literature, figures, author contributions,
   and indexes after their inputs settle; then render with the existing tools.

For illustration only, if ten new reports affect a page, the existing organization
can trigger ten full-page rewrites. The proposed organization schedules one
combined page update. That is a reduction in planned rewrite operations, not a
measured tenfold saving: extraction, planning, review, and actual output size
still contribute tokens.

Do not merge every stage into one endless autonomous conversation. Let Python
dispatch known work; let agents make scientific and editorial decisions within
that work. The approach follows the distinction between predictable workflows
and tasks that benefit from flexible model decisions.
[Anthropic's workflow guidance](https://www.anthropic.com/engineering/building-effective-agents).

Token controls that belong in the implementation

| Control | Purpose |
| --- | --- |
| Persistent accepted evidence and output caches | Avoid repeated extraction, generation, and failed-work replay across runs. |
| Page-level batching | Avoid repeated large rewrites when several sources affect the same page. |
| Stable, compact instructions and tool schemas | Reduce recurring prompt overhead and make repeated prefixes cacheable. |
| Bounded source retrieval | Return exact passages with identifiers and offsets; expose an explicit expansion path when context is insufficient. |
| Short job sessions | Resume the same unfinished job; start a clean session for unrelated work instead of inheriting the entire run history. |
| Explicit tools and permissions | Expose source retrieval, candidate submission, and validation; avoid generic repo exploration, incidental tools, or agent modification of acceptance rules. |
| Targeted scientific review | Review each substantive change with supporting evidence; avoid blanket rereads of all unchanged pages by multiple agents. |
| Whole-run accounting and bounded retries | Stop scheduling before the remaining budget is exhausted; preserve completed work on limits and failures. |

Use one strong model for scientific generation initially. Lower-quality routing
is not assumed to reduce total consumption once retries and corrections are
included. Use code for mechanical tasks, and bound effort and turns for the
remaining model jobs. Do not default to recursive delegation or multiple agents
debating every page. Independent review remains warranted for substantive
scientific changes, especially merges and deletions, with more context supplied
when a narrow diff is insufficient.

The SDK automatically uses prompt caching and exposes cache-read/write tokens.
Its dollar costs are estimates, not a subscription quota meter. Track input,
cache, output, and any reported reasoning usage, plus the account's actual
allowance consumption when available. Provider caching is an additional
optimization; durable output caches are what prevent a repeated call altogether.
Do not promise a particular subscription discount from API cache pricing.
[Usage and caching documentation](https://code.claude.com/docs/en/agent-sdk/cost-tracking).

A turn limit is not a hard token cap. Account for all jobs in the runner, reserve
headroom for an in-flight response and validation/repair, and treat unavailable
usage as unknown rather than zero. Stop on exhausted subscription limits without
automatic API fallback or extra-credit purchases.

Maintainability and preserved behavior

Keep this as an extension of the existing Python package: an SDK integration,
explicit job scheduling and persisted results, and reusable existing helpers.
Use one documented task/result format. Do not introduce a general workflow
framework, a custom chat client, or parallel provider implementations.

Keep source synchronization, ORCID/author joins, data metadata, naming, metadata
serialization, link maintenance, indexes, figure insertion, provenance, and
Quartz rendering deterministic. The SDK replaces every generative call site,
not just the main compiler. Keep embeddings as a separately cached and accounted
retrieval dependency where justified; subscription generation does not supply an
embedding endpoint. NCBI retrieval also remains an external data operation.

Retain all existing workflow obligations: summaries, concept coverage,
consolidation, entity resolution, contradictions, topics, literature, figures,
author contributions, data pages, opportunities, negative results, naming,
repair, checks, and publishing. Reorganize when inference happens, without
dropping those outputs.

Treat raw reports and retrieved papers as evidence, never as tool instructions.
Keep source originals and validation code outside the writing agent's writable
area. Commit accepted outputs through code with recoverable state. Session
resume preserves conversation history, not a transactional filesystem snapshot.
[Session semantics](https://code.claude.com/docs/en/agent-sdk/sessions).

Subscription qualification and validation boundary

The current Anthropic support page says the announced SDK billing change was
paused: Agent SDK and `claude -p` still draw from subscription limits.
This supports the proposed maintainer-operated SDK workflow today; it is not a
promise of unlimited capacity or permanent pricing.
[Current subscription guidance](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan).
A service using pooled credentials for collaborators is a different deployment
and is not part of this recommendation.
[Credential rules](https://code.claude.com/docs/en/legal-and-compliance).

Build the selected architecture, verify mechanics with saved responses and
deterministic tests, then perform one explicitly capped acceptance run on a
representative source update and its affected pages. Include a large page and
an evidence-preservation case. Confirm authentication, actual instruction/tool
loading, token reporting, output validity, and recovery before authorizing a
large run. This is a release check for the chosen implementation, not a bake-off
between approaches or repeated wiki rebuilds.

No research can establish the exact least-token runtime or best scientific model
for this corpus without measurements. The recommendation is nevertheless
actionable: Claude Agent SDK in Python, code-controlled scheduling, cached
evidence, batched page edits, and targeted review. This directly addresses the
visible sources of token waste while retaining the working pipeline's useful
guarantees.
