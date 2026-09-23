# Subscription-backed wiki curator

The Claude Agent SDK runs bounded writer, reviewer and topic-proposal jobs
under a fixed Python schedule. Python enforces source coverage, dependencies,
validation, usage accounting and recoverable promotion. Existing stage writers
remain domain operations. `scripts/run_pipeline.sh` remains the API-backed
entry point.

See the [HTML walkthrough](agentic-workflow.html) for the control flow and the
[wiki-format reference](wiki.md) for page types, citations and rendering.

## Commands and limits

Install with `uv sync` and sign in using `claude auth login` with a direct Claude
subscription. The runner removes inherited API credentials and provider routing;
each SDK job verifies subscription authentication. There is no API fallback.

```sh
# Inspect staged changes, without fetching or inference.
uv run python -m beril_wiki.agentic plan

# Use the committed model policy and explicit budgets appropriate to the update.
uv run python -m beril_wiki.agentic run \
  --max-tokens 500000 --max-jobs 40 \
  --checkout /path/to/BERIL-research-observatory

# Search accepted wiki Markdown without inference.
uv run python -m beril_wiki.agentic search 'carbon yield'
```

These budgets illustrate syntax, not measured requirements for this corpus.
`--root PATH` precedes the subcommand. `--staged` uses current staging; an
observatory checkout is still required for metadata and figure context.
Individual jobs have `--max-turns` (default 12, applying to the tool-using
integration path), `--timeout` (600 seconds), and `--max-output-tokens`
(32,768). A stage can require multiple specialist jobs per page. Inside each
stage, page jobs run in a worker pool (`--workers`, default 4); the ledger's
serialized admission holds headroom for every job in flight, and per-page state
files are written atomically so a killed worker cannot leave a truncated
`state/*.json`. `--strict-pages` turns a page that fails its patch rounds into a
run stop instead of a recorded failure.
Each stage subprocess is bounded by `--stage-timeout` (default 14,400 seconds,
four hours). A job killed by either clock is charged automatically from its
saved transcript (the terminal result if one arrived, otherwise the summed
model turns, otherwise the reservation) before the next stage starts, so a
kill never leaves a pending row that needs manual reconciliation.

`--max-tokens` is an admission ceiling in **effective tokens**, not a hard
provider token cap. The ledger records raw input, output, cache-write and
cache-read counts for every job, and admits on a weighted figure: input and
output count once, cache writes 1.25 times, cache reads 0.1 times. The weights
follow the provider's relative prices, so the effective figure tracks spend
while the raw count stays the audit record. Before each job the ledger reserves
headroom (`--reserve-tokens`, default 50,000) for every job still in flight; an
in-flight job can exceed its reservation, and subsequent jobs stop.
`--stage-max-tokens` adds a per-stage effective ceiling (0, the default, applies
only the run ceiling). `status` and the run summary print the raw total, the
effective total and the sum of the SDK's own `total_cost_usd` estimates. None of
these measure remaining subscription allowance. Account billing settings remain
provider-owned; the runner does not purchase credits.

### Per-step models

Runs automatically load [`agentic.yaml`](../agentic.yaml) from the repository
selected by `--root`. The committed policy explicitly assigns every role:

| Role | Model | Jobs |
| --- | --- | --- |
| `extraction` | Opus 5 | Extract source evidence, retaining scientific qualifiers. |
| `planning` | Opus 5 | Plan evidence integration and propose topic groups. |
| `writing` | Opus 5 | Write and revise pages, derived prose, home and entity merges; default for other generation jobs. |
| `review` | Opus 5 | All separate scientific reviews, including extraction and repaired candidates. |
| `queries` | Sonnet 5 | Construct literature search queries. |
| `figures` | Sonnet 5 | Select figure placements. |

This is a deliberate starting policy, not a measured optimum: protect scientific
fidelity and avoid costly rewrites, while using Sonnet for bounded selection
tasks. The former `curator` role is gone: the schedule below is fixed code, so
no model chooses actions any more. Haiku is not the default because a cheaper
call is not a saving if it causes missed evidence or repeat work. No model comparison run is required.
The full IDs are `claude-opus-5` and `claude-sonnet-5`, matching Anthropic's
[model catalog](https://platform.claude.com/docs/en/models/overview).
[Claude Code requires](https://code.claude.com/docs/en/model-config) version
2.1.219 or later for Opus 5 (Sonnet 5 requires 2.1.197). Availability still depends
on the authenticated account. Fable is not selected because SDK usage can draw
on additional usage credits, depending on the plan.

`--model-config PATH` loads a replacement YAML file (relative to `--root`, or
absolute). The file accepts only `model` and `step_models`, using the same shape
as the committed policy. `model` is required and supplies any omitted role.
`--model MODEL_ID` replaces the entire file policy with one model for all roles;
then repeat `--step-model ROLE=MODEL_ID` for individual overrides. Without
`--model`, individual overrides modify the loaded policy. For example:

```sh
# Keep the repository policy, changing only scientific review.
uv run python -m beril_wiki.agentic run --step-model review=MODEL_ID \
  --max-tokens 500000 --max-jobs 40 --checkout /path/to/BERIL-research-observatory
```

The CLI prints the resolved policy before execution. Invalid file shapes,
unknown roles, duplicate CLI role overrides and empty model IDs are rejected
before the runner starts. An explicitly named file must exist and validate even
when `--model` replaces its policy. A checkout
without the default file requires `--model`. Budgets remain required CLI flags.

Repairs and paragraph patches keep the original role's model; every job ending
in `/review` or `/science-review` uses `review`.
Unspecified roles use the default, with no automatic fallback or escalation.
Use explicit model IDs available to the authenticated subscription; moving
aliases may change their underlying model without changing a cache key.

The ledger records each new job's configured model. `status` returns job rows
as `[key, step, status, tokens, effective, error, model]`; older rows may have a
null model.
Accepted `state/agentic.json` records the effective role-to-model policy.
Every role shares the same token and job ceilings. Changing the policy during
an interrupted run preserves charges for the same input snapshot, including
runs created before model overrides were added.

Job caches use the selected model, so an unrelated override does not invalidate
them. Stage fingerprints include only their relevant roles: figure changes
refresh figures; query changes refresh literature. Extraction, planning,
writing or review changes conservatively recheck core integration as well.

## Editorial schedule and required work

The runner executes a fixed schedule over the stage dependency table. Each stage
runs only when its input or output fingerprint is stale, and a stale stage makes
every stage that depends on it stale as well:

| Stage | Work and completion condition |
|---|---|
| Integrate | Runs first when sources changed: extract changed reports, plan complete evidence coverage, group edits by destination, validate and review pages; resolve entities and refresh deterministic metadata. |
| Conflicts | Reconcile tensions after integration. |
| Topics | Choose concept groups and titles, then write hubs/home after conflicts are current. Every concept must occur exactly once. |
| Literature | Add supported external context after topics are current. |
| Authors | Update contributions from current summaries and metadata; independent of topics. |

Every stage writes a receipt (`.agentic/curator-receipts.json`) with the paths
it changed, so the audit trail of the earlier action loop survives without a
model choosing the order. The only structural model call is the topic proposal.

A separate compact topic proposal receives concept identities/descriptions and
existing membership. The accepted decision lives in versioned
`state/curator-topics.json`; stale concept fingerprints, unknown/duplicate/missing
members and colliding title slugs are rejected. Agentic generation uses these
chosen groups directly. The API pipeline retains graph clustering.

The host handles human concept decisions, metadata joins, naming, errata
(`contract/errata.yaml`, shown beside every claim that repeats a figure a report
got wrong), figure placement and the final strict check. Figure selection and entity merge prose
still use accounted SDK jobs. The old enrichment/consolidation and blanket repair
sweeps are replaced by integration planning and candidate correction. Outputs
remain compatible with existing provenance and Quartz tools. This is bounded
editorial autonomy; the agent cannot change its acceptance rules or run arbitrary
code.

## Evidence, correction and token reuse

Changed reports are extracted in bounded overlapping ranges with exact quotes and
offsets, including null results and caveats. Coverage spans the entire source.
Planning batches cover every evidence record; the host combines edits to each
page and passes each concept's assignments to its writer. Summaries receive
all assignments from their own source. Candidates map every assigned ID to an
exact paragraph citing that source; both tool and final validation check this
mapping. The scientific reviewer checks that the mapped text preserves each
claim, caveat and null result. Writers use base hashes and anchored patches or
justified rewrites.
Deterministic checks retain citations and quantities from unchanged sources,
including absorbed pages and paragraphs citing both revised and unchanged sources.
Quantities in those mixed-source paragraphs are retained conservatively; separate
scientific review assesses support and lost
meaning. Review is useful evidence, not a guarantee of scientific correctness.

Only the integration path uses tools. Extraction and its review get bounded
`read_evidence`; planner and page-writer jobs also get literal `search_evidence`,
and page writers a host-bound `validate_candidate`. Tool validation is advisory:
the final candidate must pass the same host checks and independent scientific
review before it is written. Extraction and retrieval both decode UTF-8 with
replacement for invalid bytes; offsets refer to that decoded text. Original
report bytes remain unchanged. No shell, general filesystem writes, skill
discovery or unrelated tools are exposed. Source text is evidence, never an
instruction authority.

### Derived prose: packed evidence, one-turn review, paragraph patches

Conflict pages, topic hubs, the home page, literature sections, author
contributions and figure placements are written without tools. Code packs each
job's complete evidence into the prompt: the tension paragraph(s) with their
`[src:]` tags, concept leads and the source paragraphs that state the tension's
own figures for a conflict page; member concept pages (truncated with an explicit
marker under a 110KB budget) and the leads of the conflict pages linking those
concepts for a hub; hub text and PubMed abstracts for a literature section; the
author's project summaries for a contributions section. A job runs in one turn,
so its cache keys on the packed prompt alone and no dependency on a
file read can invalidate it later. The rules and the pack travel as the job's
system prompt, which the CLI caches: a page's writer writes that prefix once and
its review and patch jobs read it, so only the task, candidate or issues are
fresh input.

Each stage defines one rule list (`Contract` in `agentic/prose.py`, instantiated
in the stage module) that is injected verbatim into the writer, the patcher and
the reviewer: word range, required sections, figures only from the input,
`[src:]` tags as the input gives them, directions and denominators as stated,
jargon defined at first use, lead figures cited, no preamble, no legacy platform
names. Deterministic gates run before any review and report issues by paragraph
index and category: length (with 10% slack), missing headings, preamble, figures
absent from the input, invalid `[src:]` ids, figures without a tag, and figures
absent from their cited sources. Dead wikilinks and legacy platform names are
repaired in code. Only a candidate that passes every gate reaches the reviewer,
which receives exactly the writer's evidence pack and rules plus the numbered
candidate and returns one JSON verdict listing issues with a paragraph index, a
category (number, direction, denominator, caveat, citation, length, format,
unsupported) and a quote.

A rejected candidate is patched, not rewritten: the writer receives the numbered
candidate, the same pack and the latest issues, and returns replacement paragraphs
keyed by index against the candidate's base hash. An issue saying the evidence does
not support a claim is an instruction to delete it, not to reword it.

The first review reads the whole page, at whichever round the gates first pass, and
no page publishes without one. Every round after it is a **verification**, not
a second review: the reviewer receives the issues it raised and the revised
paragraphs, and answers whether each is closed and whether the revision introduced a
factual error. An objection it already raised stays open whatever its category; a
newly introduced one counts only when it touches what the page claims. The open list
can therefore shrink or hold but never grow on settled text, which is what lets the
budget rise to five patch rounds.

A page that still carries an objection after its rounds is **salvaged, not dropped**:
the paragraphs still objected to are removed, an editorial note naming the categories
takes their place, and the rest of the page publishes. Headings are never removed, and
a removal that would break a gate other than length, or leave no prose behind, is
refused; only then does the page fail. Salvages are listed in
`.agentic/salvaged.json`, failures in `.agentic/failures.json`, both with issues and
job keys. A failed page keeps the previously accepted version or is skipped, and the
stage continues. Promotion proceeds with failures reported unless `--strict-pages` is
set, in which case a stage with failures stops the run. The API pipeline shares
the same gates and patch rounds but has no model reviewer.

Invalid plans, topic proposals and integration candidates get **at most one
correction**, and a repaired candidate receives a fresh review. Extraction
rejection, unknown usage, authentication failures and other operational errors
still stop the run. The worst case for a derived page is twelve jobs: a draft, one
open review, and five patch rounds each with its own verification.

Durable raw job results and evidence avoid repeating accepted inference. Tool
reads track file hashes; searches track searchable inventories, so negative
results invalidate when pages appear or disappear. Unchanged runs make zero model
calls. Changed inputs use stage page caches; edited outputs invalidate only their
own entries. Scientific configuration changes invalidate the relevant caches.
Literature sections are excluded from topic-owned fingerprints to prevent repeat
synthesis. Scheduler-only migration retains successful source integration. The first curator
run, or migration from accepted state without version 2, refreshes all derived
prose once because there is no accepted semantic revision for it yet. Runtime
bookkeeping and authentication edits do not by themselves invalidate stage prose.

Scientific compiler/model changes and manual edits to core pages conservatively
revisit staged sources. Deleted sources require a separate scientific retraction;
they are never silently accepted. Evidence read limits are 24,000 characters per
read and 100KB total tool output per job; requests are limited to 500KB and
transcripts/stage logs to 4MB. Oversized inventories still stop with saved
results. Figure selection retains the existing candidate caps. Malformed
placement JSON or indices stop the agentic run; per-page chart-review flags
survive cached updates and are removed when their pages are retired. No
embedding API is used in this path; PubMed remains an external data retrieval
operation.

## Resume and recovery

Ignored `.agentic/` stores the SQLite ledger, raw results, evidence, plans, paper
snapshots, logs, curator receipts and isolated candidate output. Keep this folder
when retrying so completed work and prior charges survive. Rerun the same command
to reconstruct the candidate from cached results.

```sh
uv run python -m beril_wiki.agentic status
uv run python -m beril_wiki.agentic retry --job FULL_JOB_ID
uv run python -m beril_wiki.agentic retry --page conflicts/conflict--stem--1a2b3c4d
uv run python -m beril_wiki.agentic retry --all-failed
```

For a capped acceptance pass, invoke a stage directly with `--limit N`
(conflicts and topics): it writes at most N new pages and retires none, so a
partial pass never reaps pages it did not get to. Direct stage invocations are
maintenance tools; they do not promote.

`status` lists the failed pages beside the totals. `retry --page` and
`retry --all-failed` mark every job a failed page used as rejected and drop the
owning stage from the accepted state, so the next run (which would otherwise
report "unchanged") re-runs that stage, drafts the page afresh (fresh drafts
converged where repeated repairs did not in the first live run) and leaves every
other cached page untouched. A pass that records any failure retires no pages,
so a failed replacement's predecessor stays published under its old slug.

Use `retry` only after inspecting a saved failed/rejected job. Malformed figure
JSON/indices and entity retention-gate refusals stop the run and need inspection
before explicitly retrying the affected job. A derived page that failed its patch
rounds does not stop the run; its issues and job keys are in
`.agentic/failures.json`, and rerunning the same command replays the cached
verdict for free. Excess valid figure placements are trimmed to the page's cap. Completed editorial results remain cached; stopping
promotion does not discard their paid model outputs. A crash can consume
allowance without returning usage. Jobs interrupted by a timeout or a killed
stage are charged from their transcripts automatically; only a job whose result
carried no usable usage is left `unknown`, which blocks new calls until
conservatively reconciled by hand. Prior charges and outputs remain saved:

```sh
uv run python -m beril_wiki.agentic account --job FULL_JOB_ID --tokens 50000
uv run python -m beril_wiki.agentic retry --job FULL_JOB_ID
```

Promotion starts only after the strict gate and concurrent-input checks pass.
It journals and renames **wiki, state and staging**, retaining originals in
`.agentic/previous`. This is recoverable, not one atomic filesystem operation.

```sh
uv run python -m beril_wiki.agentic recover
```

Search refuses pending promotion and holds the runner lock while reading. Its
JSON contains relative paths, snippets, exact character offsets, page-level source
IDs and match counts. Pass the returned `next_offset` as `--offset` for another
page; this is a file cursor, not a result count. Search is literal and excludes
copied raw sources. This CLI is a retrieval boundary, **not an installed BERIL or
OpenViking integration**.

After local acceptance, `scripts/build_quartz.sh` renders the existing format.
The curator does not commit, push or deploy. Do not publish concurrently with
promotion.

## Development verification

Offline tests exercise the actual subprocess pipeline with recorded model and
PubMed replies: the stage schedule, dependency enforcement, gates, paragraph
patches, closed verification, salvage, recorded page failures, errata
placement, topic decisions, cache invalidation, subscription setup and
promotion recovery. They do not establish model quality or real subscription
savings. The tests workflow runs them, with ruff and ty, on every pull request
and on `main`; the publish workflow validates the committed wiki, renders it and
type-checks the theme, and neither needs a key or an observatory checkout. The
curator has not yet been accepted through a real source update. MCP remains below
version 2 for the SDK's in-process tool compatibility.

Specs, plans and review dispositions are local gitignored files under
`docs/superpowers/`. Independent Claude Code reports are retained outside the
checkout. A representative capped live update remains the acceptance step before
using this for a large production compilation.
