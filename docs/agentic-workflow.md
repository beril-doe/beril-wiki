# Subscription-backed wiki curator

The Claude Agent SDK runs a bounded curator that chooses editorial actions and
topic organization. Python enforces source coverage, dependencies, validation,
usage accounting and recoverable promotion. Existing stage writers remain domain
operations. `scripts/run_pipeline.sh` remains the API-backed entry point.

## Commands and limits

Install with `uv sync` and sign in using `claude auth login` with a direct Claude
subscription. The runner removes inherited API credentials and provider routing;
each SDK job verifies subscription authentication. There is no API fallback.

```sh
# Inspect staged changes, without fetching or inference.
uv run python -m beril_wiki.agentic plan

# Choose a model available to your login and budgets appropriate to the update.
uv run python -m beril_wiki.agentic run \
  --model MODEL_ID --max-tokens 500000 --max-jobs 40 --max-actions 16 \
  --checkout /path/to/BERIL-research-observatory

# Search accepted wiki Markdown without inference.
uv run python -m beril_wiki.agentic search 'carbon yield'
```

These budgets illustrate syntax, not measured requirements for this corpus.
`--root PATH` precedes the subcommand. `--staged` uses current staging; an
observatory checkout is still required for metadata and figure context.
`--max-actions` bounds curator decisions, including rejected and repeated actions;
it does not replace the shared job/token limits. Individual jobs have
`--max-turns` (default 12), `--timeout` (600 seconds), and
`--max-output-tokens` (32,768). An action can require multiple specialist jobs.

`--max-tokens` is an admission ceiling, **not a hard provider token cap**. The
shared ledger reserves headroom before each job (`--reserve-tokens`, default
50,000). An in-flight job can exceed its reservation; subsequent jobs stop.
Accounting includes input, output, cache-write and cache-read tokens from
generation, review and repair. These counts and API-price estimates do not measure
remaining subscription allowance. Account billing settings remain provider-owned;
the runner does not purchase credits.

## Editorial control and required work

The curator receives compact obligations, available actions, collection counts
and its latest receipt. It chooses the next action within these dependencies:

| Action | Work and completion condition |
|---|---|
| Integrate | Extract changed reports, plan complete evidence coverage, group edits by destination, validate and review pages; resolve entities and refresh deterministic metadata. |
| Conflicts | Reconcile tensions after integration. |
| Topics | Choose concept groups and titles, then write hubs/home after conflicts are current. Every concept must occur exactly once. |
| Literature | Add supported external context after topics are current. |
| Authors | Update contributions from current summaries and metadata; independent of topics. |
| Finish | Allowed only when all required input/output fingerprints are current. |

A separate compact topic proposal receives concept identities/descriptions and
existing membership. The accepted decision lives in versioned
`state/curator-topics.json`; stale concept fingerprints, unknown/duplicate/missing
members and colliding title slugs are rejected. Agentic generation uses these
chosen groups directly. The API pipeline retains graph clustering.

The host handles human concept decisions, metadata joins, naming, figure
placement and the final strict check. Figure selection and entity merge prose
still use accounted SDK jobs. The old enrichment/consolidation and blanket repair
sweeps are replaced by integration planning and candidate correction. Outputs
remain compatible with existing provenance and Quartz tools. This is bounded
editorial autonomy; the agent cannot change its acceptance rules or run arbitrary
code.

## Evidence, correction and token reuse

Changed reports are extracted in bounded overlapping ranges with exact quotes and
offsets, including null results and caveats. Coverage spans the entire source.
Planning batches cover every evidence record; the host combines edits to each
page. Writers use base hashes and anchored patches or justified rewrites.
Deterministic checks retain citations and quantities from unchanged sources,
including absorbed pages; separate scientific review assesses support and lost
meaning. Review is useful evidence, not a guarantee of scientific correctness.

SDK tools expose bounded `read_evidence`. Curator, planner and writer jobs also
get literal `search_evidence`; page writers additionally get a host-bound
`validate_candidate`. Tool validation is advisory: the final candidate must pass
the same host checks and independent scientific review before it is written.
Extraction and retrieval both decode UTF-8 with replacement for invalid bytes;
offsets refer to that decoded text. Original report bytes remain unchanged.
This decoder change rotates the evidence-tool cache identity once. Subsequent
unchanged reads reuse their cached results.
No shell, general filesystem writes, skill discovery or unrelated tools are
exposed. Source text is evidence, never an instruction authority.

Invalid plans, topic proposals and page candidates get **at most one correction**.
A repaired scientific candidate receives a fresh review. Derived scientific
completion uses the same bound. Extraction rejection, malformed reviewer output,
unknown usage, authentication failures and other operational errors stop the run.
There is no unbounded correction loop. Legacy topic, conflict, literature and
author validators retain their bounded stage retries for invalid numbers,
citations or author characterizations. Each reissued generation is separately
accounted and scientifically reviewed, but legacy retry steps receive no additional
repair allowance. Worst-case ceilings, including scientific reviews, are ten SDK
jobs per entity merge, eight per topic hub and six per conflict, author or
literature update. Mechanical requests and unrelated pages have separate costs;
the shared job/token limits still apply.

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
transcripts/stage logs to 4MB. Author/topic previews share a 160KB serialized context budget with explicit
retrieval paths. Oversized inventories still stop with saved results. Figure
selection retains the existing candidate caps. Malformed placement JSON or indices
stop the agentic run; per-page chart-review flags survive cached updates and are
removed when their pages are retired. No embedding API is used in this
path; PubMed remains an external data retrieval operation.

## Resume and recovery

Ignored `.agentic/` stores the SQLite ledger, raw results, evidence, plans, paper
snapshots, logs, curator receipts and isolated candidate output. Keep this folder
when retrying so completed work and prior charges survive. Rerun the same command
to reconstruct the candidate from cached results. Changing only `--max-actions`
does not invalidate cached decisions or reset accounting.

```sh
uv run python -m beril_wiki.agentic status
uv run python -m beril_wiki.agentic retry --job FULL_JOB_ID
```

Use `retry` only after inspecting a saved failed/rejected job. Malformed figure
JSON/indices, entity retention-gate refusals and twice-rejected scientific
candidates stop the run and need inspection before explicitly retrying the
affected author job, reviewer job, or both. Excess valid figure placements
are trimmed to the page's cap. Completed editorial results remain cached; stopping
promotion does not discard their paid model outputs. A crash can consume
allowance without returning usage. Pending/unknown usage blocks new calls until
conservatively reconciled; prior charges and outputs remain saved:

```sh
uv run python -m beril_wiki.agentic account --job FULL_JOB_ID --tokens 50000
uv run python -m beril_wiki.agentic retry --job FULL_JOB_ID
```

Premature finish is rejected with remaining obligations; action exhaustion stops
without promotion. A repeated current action returns an unchanged receipt.
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
PubMed replies, alternate action order, dependency enforcement, bounded repair,
topic decisions, cache invalidation, subscription setup and promotion recovery.
They do not establish model quality or real subscription savings. The earlier
SDK smoke used only a tiny synthetic source and reported 2,854 tokens through a
Claude Max login; it did not compile this wiki. The curator changes have not been
accepted through a real source update. MCP remains below version 2 for the SDK's
current in-process tool compatibility.

Specs, plans and review dispositions are local gitignored files under
`docs/superpowers/`. Independent Claude Code reports are retained outside the
checkout. A representative capped live update remains the acceptance step before
using this for a large production compilation.
