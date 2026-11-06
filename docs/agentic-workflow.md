# Subscription-backed wiki curator

The Claude Agent SDK runs bounded page sessions, planning and topic-proposal
jobs, and the Codex app server runs extraction and review jobs, under a fixed
Python schedule. Python enforces source coverage, dependencies,
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
Individual jobs have `--max-turns` (default 12, applying to tool-using jobs
other than page sessions), `--timeout` (600 seconds), and `--max-output-tokens`
(32,768). A page session is bounded by its brief instead: 20 turns plus one per
20,000 characters of brief, at most 60; a USD ceiling of 1 plus 1 per 40,000
characters, at most 20; and a one-hour clock. A stage can require multiple
specialist jobs per page. Inside each
stage, page jobs and extraction chunks run in a worker pool (`--workers`, default
4), each worker holding its own runtime because a ledger connection belongs to one
thread, and evidence is assembled in source order so a chunk finishing first never
changes an id or a digest; the ledger's
serialized admission holds headroom for every job in flight, and per-page state
files are written atomically so a killed worker cannot leave a truncated
`state/*.json`. `--strict-pages` turns a page whose session fails into a run
stop instead of a recorded failure. `--pass-records` (default 60, 0 for one
write) bounds the records a page writer integrates at once, and `--write-effort`
sets the page writers' reasoning effort when no [step effort](#per-step-models)
names one for `pages` (default: the model's own). The committed policy names
`medium` for `pages`, so `--write-effort` takes effect only with `--model` or a
replacement file that omits it.
Each stage subprocess is bounded by `--stage-timeout` (default 14,400 seconds,
four hours). A job killed by either clock is charged automatically from its
saved transcript (the terminal result if one arrived, otherwise the summed
model turns, otherwise the reservation) before the next stage starts, so a
kill never leaves a pending row that needs manual reconciliation.

`--max-tokens` is an admission ceiling in **effective tokens**, not a hard
provider token cap. The ledger records raw input, output, cache-write and
cache-read counts for every job, and admits on a weighted figure: input and
output count once, 5-minute cache writes 1.25 times, 1-hour cache writes twice,
cache reads 0.1 times. The CLI writes 1-hour caches; a usage that reports its
`cache_creation` split by lifetime is weighted that way, and one without the
split counts every write at 1.25. The weights follow the provider's relative
prices, so the effective figure tracks spend while the raw count stays the
audit record. Before each job the ledger reserves headroom (`--reserve-tokens`,
default 50,000) for every job still in flight; an in-flight job can exceed its
reservation, and subsequent jobs stop. `--stage-max-tokens` adds a per-stage
effective ceiling (0, the default, applies only the run ceiling). Two optional
caps per ledger run are kept in the units a person approves: `max_usd` on the
SDK's cost estimate for Claude jobs and `max_codex_tokens` on raw Codex tokens.
A capped run counts each finished job at its recorded charge and each pending one
at a hold: a page session holds its whole session USD ceiling, any other Claude job
USD 2, a Codex job 400,000 tokens. A job is admitted only if its hold still fits,
and one that ends without a reported cost (a kill, a timeout) keeps its hold, so an
interrupted job still counts. Only the `pilot` command sets them
(`--max-usd`, `--max-codex-tokens`); `run` has no flag for them. `status` and
the run summary print the raw total, the effective total and the sum of the SDK's own `total_cost_usd` estimates. None of
these measure remaining subscription allowance. Account billing settings remain
provider-owned; the runner does not purchase credits.

### Per-step models

Runs automatically load [`agentic.yaml`](../agentic.yaml) from the repository
selected by `--root`. The committed policy explicitly assigns every role:

| Role | Model | Effort | Jobs |
| --- | --- | --- | --- |
| `extraction` | GPT-6.1 Sol (Codex) | default | Extract source evidence, retaining scientific qualifiers. Applies to reports extracted from now on; evidence already extracted by GPT-6 Sol stays. |
| `planning` | Sonnet 5.5 | `high` | Plan evidence integration and propose topic groups. |
| `pages` | Haiku 5.5 | `medium` | Write the concept, entity and summary pages integration produces: one page session per `write/` pass. Applies to pages written from now on; pages already accepted stay. |
| `writing` | Sonnet 5.5 | `medium` | Derived pages (conflicts, topics, literature, authors) as page sessions, home and entity merges; default for other generation jobs. Applies to pages written from now on. |
| `review` | GPT-6 Luna (Codex) | `high` | All separate scientific reviews and verifications, including extraction and the reviews a page session asks for. |
| `queries` | GPT-6.1 Sol (Codex) | default | Construct literature search queries. |
| `figures` | GPT-6.1 Sol (Codex) | default | Select figure placements. |

This is a deliberate hybrid, not a measured optimum: Claude plans and writes,
a GPT model extracts and reviews, so no page is checked by the family that wrote
it. Two pilots (September 2026) measured GPT writing at a third to a tenth of
Claude's tokens but preferred Claude's prose four pages to one, and GPT
extraction at a higher finding yield with fewer review repairs. The bounded
selection tasks, queries and figures, run on GPT-6.1 Sol, the extraction model.
An Effort of `default` is the backend's own, which is `high` for Codex.
Integrated pages moved to Sonnet 5.5 in October 2026. On nine pilot pages (11 to
319 records) it cost a third of the Opus writers, half the job time, and refused
none of the pages Opus 5.5 had refused. A blind GPT judge, both orders, scored its
fidelity equal or higher on every page it judged and its clarity about a point
lower. One 197-record page lost two of its four passes where Opus kept all four.
Derived pages moved to Sonnet 5.5 after the October pilot described under
[Pilots](#pilots). The later model-mix pilot, also under [Pilots](#pilots),
moved integrated pages to Haiku 5.5, review to GPT-6 Luna and planning to
Sonnet 5.5, and set the efforts above. The
former `curator` role is gone: the schedule below is fixed code, so
no model chooses actions any more. No model comparison run is required.
The full IDs are `claude-sonnet-5-5`, `claude-haiku-5-5`, `gpt-6.1-sol` and
`gpt-6-luna`. The file's default `model`, `claude-opus-5-5`, supplies no role
while every role is pinned. The Claude IDs match Anthropic's
[model catalog](https://platform.claude.com/docs/en/models/overview).
Opus 5.5 was verified on
[Claude Code](https://code.claude.com/docs/en/model-config) 2.1.280 and Sonnet 5.5 on 2.1.293. Availability still depends
on the authenticated account. Fable is not selected because SDK usage can draw
on additional usage credits, depending on the plan.

`--model-config PATH` loads a replacement YAML file (relative to `--root`, or
absolute). The file accepts only `model`, `step_models` and `step_efforts`, using
the same shape as the committed policy. `model` is required and supplies any omitted role.
`--model MODEL_ID` replaces the entire file policy with one model for all roles;
then repeat `--step-model ROLE=MODEL_ID` for individual overrides. Without
`--model`, individual overrides modify the loaded policy. For example:

```sh
# Keep the repository policy, changing only scientific review.
uv run python -m beril_wiki.agentic run --step-model review=MODEL_ID \
  --max-tokens 500000 --max-jobs 40 --checkout /path/to/BERIL-research-observatory
```

`step_efforts` maps a role to a reasoning effort (`low`, `medium`, `high`,
`xhigh` or `max`); a role it omits runs at the backend's default, which is `high`
for Codex. `run` and `pilot` take a repeatable `--effort ROLE=LEVEL` that
overrides the file per role, and `--model` drops the file's efforts with its
models. Claude jobs pass the effort to the SDK and Codex jobs to the Codex turn.

The CLI prints the resolved model policy before execution. Invalid file shapes,
unknown roles, duplicate CLI role overrides, empty model IDs, a `step_efforts`
that is not a map, and an unknown effort role or level are rejected before the
runner starts. An explicitly named file must exist and validate even
when `--model` replaces its policy. A checkout
without the default file requires `--model`. Budgets remain required CLI flags.

A page session runs on its page's role (`pages` for `write/` steps, `writing`
for derived pages), and repairs and the API pipeline's paragraph patches keep
the original role's model; every job ending in `/review`, `/science-review` or
`/verify` uses `review`.
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
them. Model roles are forward-only: no model identity is part of the scientific
revision or of any derived stage's revision, so changing any role's model
applies to pages written from then on, accepted pages stay, and neither
integration nor any derived stage reruns because of it. An extraction change
likewise applies only to reports extracted from then on. To rewrite accepted
pages with a new model, bump the stage's constant in `STAGE_REVISIONS`
(`agentic/curator.py`) or `INTEGRATION_REVISION` (`agentic/batch.py`); to
measure a new model on a few named pages first, run a [pilot](#pilots).

## Pilots

A pilot measures another model on named pages against the accepted ones before a
policy changes, as a tracked operation (`agentic/pilot.py`):

```sh
# Freeze the starting trees and copy the ledger the pilot charges to.
uv run python -m beril_wiki.agentic pilot setup --scratch /path/to/scratch \
  --store .agentic --before COMMIT --checkout /path/to/BERIL-research-observatory

# One cell: one model policy over one set of pages, under spend caps.
uv run python -m beril_wiki.agentic pilot cell --scratch /path/to/scratch \
  --name der-sonnet --kind derived --pages conflicts/SLUG,topics/SLUG,index.md \
  --step-model writing=claude-sonnet-5-5 --run pilot \
  --max-usd 30 --max-codex-tokens 15000000

# Blind comparison with the accepted pages, then every cell in one report.
uv run python -m beril_wiki.agentic pilot judge --scratch /path/to/scratch \
  --name der-sonnet --run pilot --max-usd 30 --max-codex-tokens 15000000
uv run python -m beril_wiki.agentic pilot report --scratch /path/to/scratch
```

The caps are illustrations, not measured requirements; `cell` and `judge` refuse
to start without both. `setup` needs a scratch directory that does not exist yet.
It exports the tracked wiki, state and contract at `--before` (the tree
integrated, routing and extraction cells start from) and at `HEAD` (the tree derived cells start from),
copies the ledger, saved plan and evidence from `--store`, and applies concept
decisions, extras and naming as a run would. Each `cell` runs on its own copy of
a tree and writes `cells/NAME/manifest.json` with its usage and each page's
outcome as the host recorded it (written, salvaged, failed or unchanged):

- `integrated` writes the named concept, entity or summary pages from the saved plan.
- `derived` rewrites named pages (`conflicts/SLUG`, `topics/SLUG`, `lit/STEM`,
  `authors/STEM`, `index.md`). The stage modules' `--pages a,b` flag rewrites
  exactly those pages whatever their cache says and retires none.
- `routing` routes the first records of the saved plan (the count is the one
  `--pages` value, default 240) and compares their placements with the plan's.
- `grouping` reruns the topic proposal and compares its groups with the accepted
  ones.
- `extraction` extracts the named staged sources (`--pages
  core_gene_tradeoffs__REPORT.md`) from the `--before` tree with the cell's
  `extraction` and `review` models, and writes `cells/NAME/evidence.json`. Its
  `detail` compares each source with the accepted extraction: `quote_recall` and
  `quote_precision` measure the quoted source characters both share, and
  `number_recall` is the share of numbers in accepted claims that the new claims
  also state. Its outcomes are per chunk, keyed `extract/SOURCE/START`, and each
  is extracted, gap or empty. The cell refuses a source that the saved plan
  holds no accepted extraction of, as after an incremental run, and saves its
  evidence source by source, so a failure keeps the sources finished before it.

Cells run one at a time on the scratch ledger, under a lock on the scratch
directory, so the caps hold across every cell of one `--run` and cached baseline
jobs cost nothing. A cell that fails still writes its manifest with the error, and
a named page no writer was given is reported as `not run`. A cell's policy is
the scratch tree's `agentic.yaml` with its `--step-model` and `--effort`
overrides, and its manifest records the models and `step_efforts`. A cell's usage
excludes `pilot/judge/` rows, so a judge running beside it is not charged to it. Each
writer's input is kept per page under `cells/NAME/packs/`, and `judge` gives the
review model exactly that input with the accepted and the new page, in both
orders; a page it refuses or cannot score is recorded as unjudged, never scored.
On an extraction cell the judge reads each chunk's passage with the accepted and
the new records, and scores precision instead of clarity (`EXTRACTION_RUBRIC`);
a chunk whose records match the accepted ones is not judged.
Judge jobs are in the `review` role, so `--effort review=LEVEL` sets the judge's effort.
`report` writes `report.json`, merging a cell rerun on the pages a stopped cell
did not reach (named with a one-letter suffix, such as `int-sonnet-b`) into one
view per model.

The October 2026 pilot moved derived pages to Sonnet 5.5. Against the accepted
Opus pages the judge scored Sonnet's fidelity +1.83 (+0.70 excluding one
literature outlier) and its clarity +1.00, with 0 refusals against 4 by Opus 5.5,
at USD 0.75 of Claude spend against USD 20.53. Its integrated-page comparison of
page sessions with the earlier pipeline is under [Page sessions](#page-sessions).
That pilot also tried Haiku 5.5 for pages, routing and topic grouping and adopted
it for no role: it dropped records on pages Opus kept whole and twice overran the
output cap.

The October 20 model-mix pilot set the current policy. Four model mixes
rewrote the same 13 integrated and 6 derived pages, each starting from the plan
Opus wrote. Haiku 5.5 at `medium` effort with GPT-6 Luna reviewing wrote the
integrated pages for USD 2.36, against USD 21.25 for the Sonnet 5.5 reference,
and dropped no records. Its judge scores sat within the judge's noise of the
reference, about 0.9 points per axis. With GPT-6.1 Sol reviewing, Sonnet pages
lost 262 records to salvage because their reviews did not close within four
calls. Haiku planning shared a concept with the accepted plan on about two thirds
of records, where Sonnet reached 90%, so Sonnet plans. No single run combined
Sonnet planning with Haiku writing. A separate extraction pilot found that GPT-6
Luna and Haiku 5.5 extraction lost coverage against GPT-6.1 Sol, so extraction
stays on GPT-6.1 Sol.

## Editorial schedule and required work

The runner executes a fixed schedule over the stage dependency table. Each stage
runs only when its input or output fingerprint is stale, and a stale stage makes
every stage that depends on it stale as well:

| Stage | Work and completion condition |
|---|---|
| Integrate | Runs first when sources changed: extract changed reports, route every evidence record to concept pages, group edits by destination, validate and review pages; resolve entities and refresh deterministic metadata. A writer receives the evidence assigned to its page with quotes packed, not every finding its sources yielded; an existing entity with nothing assigned and no revised source is skipped. It accounts for each assigned record by the index of the paragraph carrying it, not by repeating the paragraph, since a page assigned three hundred records could not otherwise finish its answer; the validator resolves the index against every paragraph of the body, including Open Directions, and the reviewer sees the resolved text. Each write is one page session (see [Page sessions](#page-sessions)): the page, absorbed pages and quotes are packed into its system prompt, the writer edits `page.md` and fills `meta.json` (the description and the `accounted_evidence` map), may read and search `staging/` and `wiki/`, and calls the host's `check`, `review` and `submit` tools. A page assigned more than `--pass-records` records is written in near-equal passes in evidence-id order, each its own page session over its slice against the page the previous pass left, so no single session integrates hundreds of records; the retention gate keeps every earlier pass's citations and figures. A pass that will not converge is dropped rather than the page, which keeps every accepted pass; its records, objections and job keys go to `.agentic/salvaged.json`, as a salvaged derived page's paragraphs do. At nine passes in ten accepted in the pilot, a seven-pass page failing whole would publish under half the time. Only a page whose every pass fails keeps its previous version. |
| Conflicts | Reconcile tensions after integration. |
| Topics | Choose concept groups and titles, then write hubs/home after conflicts are current. Every concept must occur exactly once. |
| Literature | Add supported external context after topics are current. |
| Authors | Update contributions from current summaries and metadata; independent of topics. |

Before writing hundreds of planned pages, measure a few: `--write-only
concepts/a.md,summaries/b.md` writes only those pages and then stops before any
source is recorded as integrated, so the ledger shows what an accepted page
costs and the work tree holds the pages for inspection. A partial run must never
mark the corpus integrated, or the next run would believe the work done.

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

After the editorial stages and before naming, the deterministic `titles` stage
(`beril_wiki.stages.titles`) writes the planner's title as the H1 of any page
that lacks one. It reads titles from `.agentic/last-plan.json` in the curator
store and makes no model call. Without an H1 a page publishes under its slug,
as 31 pages from the October 2026 compile did. The batch writer also inserts the
planned title when a candidate has no H1, and `beril_wiki.check` fails on any
generated page still without one. `scripts/run_pipeline.sh` runs the same
stage before `names`.

## Evidence, correction and token reuse

Changed reports are extracted in bounded overlapping ranges with exact quotes and
offsets, including null results and caveats. Coverage spans the entire source.
Routing places every evidence record. Routing jobs (`plan/route/N`, 120 records
each, one turn, no tools) run in parallel, each with the concept and entity
dictionary as its cached system prefix. A lexical shortlist of concepts per
record was measured and dropped: TF-IDF over the existing pages ranked the
previous planner's concept first for 31% of records and within five for 59%. A job gives every
record its concepts, a summary-only reason, or a `new_topic` naming a concept the
dictionary lacks, and lists new entities with the records that describe them.
The `new_topic` leftovers go to a few proposal jobs (`plan/propose/N`) in
sequence, each told what the earlier ones proposed, which turn them into new
concept pages or summary-only rows. An entity named by fewer than two records,
or, when the update spans several projects, by records from only one of them,
gets no page, and an existing entity is only rechecked when its sources change.
The router proposes no merges; concept identity decisions stay in
`contract/concept-decisions.yaml`. The planner this replaced read the inventory
of every page planned so far, so 103 batches ran one after another for 10 to 14
hours. The host combines the routes into one plan, validates it as before and
passes each concept's assignments to its writer. Summaries receive all
assignments from their own source, and a new entity the records naming it.
Candidates map every assigned ID to an exact paragraph citing that source; the
host validates this mapping. The scientific reviewer checks that the mapped text preserves each
claim, caveat and null result. A session's page is validated as a full rewrite
against the base hash of the page it started from.
Deterministic checks retain citations and quantities from unchanged sources,
including absorbed pages and paragraphs citing both revised and unchanged sources.
Quantities in those mixed-source paragraphs are retained conservatively; separate
scientific review assesses support and lost
meaning. Review is useful evidence, not a guarantee of scientific correctness.

The bulk of a job's context is sent as a system message so the CLI caches it as a
prefix and the jobs that follow read it instead of writing it again at full price:
a page's existing text, absorbed pages and assigned evidence form the system
prompt of its page session, whose later turns read the cached conversation and
write only what is new (cache reads ran about 9.6 times cache writes in the
pilot), and its review and verify jobs share them; the concept and entity dictionary is
shared by every routing and proposal job. Review and verify nest only a task's user messages, and the
reviewer receives each cited paragraph once, indexed by the evidence map. The
tool-turn budget is stated by the runtime in the system prompt, not in any job's
text, so changing `--max-turns` does not re-key cached work. Measured before this
on the heaviest pilot page: review and verify each rewrote 400K tokens of context,
three times the write prompt, and the evidence map alone repeated 53 paragraphs
311 times.

Page sessions and the integration path use tools; routing jobs have none.
Extraction and its review get bounded `read_evidence`, as do the reviewer's
reviews and verifications of an integrated page; the topic proposal also gets
literal `search_evidence`. A page session has the tools listed under
[Page sessions](#page-sessions) and no in-session validation tool: one made the
writer emit its whole candidate twice, once to check and once to answer, while
`check` reads the file the writer already edited. The final
candidate must pass the host checks and independent scientific review before it
is written. Extraction and retrieval both decode UTF-8 with
replacement for invalid bytes; offsets refer to that decoded text. Original
report bytes remain unchanged. No shell, filesystem writes outside a session's
`page.md` and `meta.json`, skill discovery or unrelated tools are exposed.
Source text is evidence, never an instruction authority.

### Page sessions

In the agentic runtime every integrated page write or pass and every derived page
is one Claude SDK session (`agentic/page_agent.py`). It replaced a fixed
choreography that sent a page's draft, each repair and each patch as a separate
query, re-sending the packed evidence every time, with Python deciding when to
repair. The writer works in a scratch directory under `.agentic/pages/`. It edits
`page.md` (and, for an integrated page, `meta.json`) with the CLI's Edit and
Write tools, may Read, Grep and Glob that directory and, for an integrated page,
`staging/` and `wiki/`, and calls three host tools:

- `check` runs the host gates on the current files and writes nothing: the
  integrated-page validator for a `write/` pass; for a derived page, the stage's
  normalization, the shared prose gates and the stage's own extra gates.
- `review` asks the GPT reviewer about text that has passed `check`: one open
  review of the whole page, then closed verifications of the objections it
  raised, with the review, verification and progress rules the stage already
  applied. A verification is told which paragraphs changed since the reviewer
  last saw the page, and a new objection counts only against those.
- `submit` is accepted only when the latest passing check and the latest review
  both cover the exact current text and that review left nothing open; any edit
  after an approval, or an objection from a later review, needs a new check and
  review.

Python sets the bounds: turns and a USD ceiling scaled to the brief (see
[Commands and limits](#commands-and-limits)), at most four reviewer calls per
session (one review and three verifications, each retried once when the verdict
is malformed), a loop guard that denies re-reading content still in context
(keyed by content hash and cleared by an edit or a context compaction), and one
blocked attempt to stop before submitting. An integrated pass keeps its progress
rule: after the first verification, a further round is allowed once, and only
when that verification closed most objections (two or fewer left, at most half
of what it answered); otherwise the session stops. In the first full compile 23
of 24 failed pages were such near misses, and the heaviest page once spent USD 25
on rounds without converging.

A session that ends without an accepted submission is handled by what it is. An
integrated pass is dropped, as above. A derived page with no full review fails; one
whose reviewer returned no usable verdict fails closed; one with a full review
publishes the reviewed text intact when the open objections are presentation only,
and is otherwise salvaged or failed as described under derived prose. A crashed or
killed session is charged from its transcript; the next attempt is a new session
under a new key, which resumes from the scratch files only when they match the
check the host last recorded for the same task, and starts fresh otherwise. The
scratch state belongs to one task (the page's brief, starting text, model and
contract): new evidence starts fresh, and so does a retry after a session that
ended on its own terms (submitted, spent its reviews, stopped), so a retry never
inherits an approval or an exhausted review count. Resuming continues from the
files, not from the SDK conversation: the session starts a new conversation with
the brief and a note of the open objections, and the reviewer gives the resumed
text a fresh open review. A page whose text has started 20 sessions is recorded as
failed rather than stopping the run. Reviews run on a fresh Codex thread per call,
as other jobs do; a thread kept per page, which the plan proposed, was not built.

The pilot that preceded the cutover ran 13 integrated pages through both paths on
Sonnet 5.5: the page sessions cost USD 12.60 of Claude spend against USD 21.08
for the pipeline, and 8.72M Codex tokens against 9.76M. Against the accepted Opus
pages a blind judge scored the sessions +0.38 on fidelity and -0.81 on clarity,
where the pipeline at the same model scored +0.64 and -0.04, so clarity is the
measured cost of the change.

Page sessions fan out across `--workers` threads, each with its own runtime. A page
whose session fails is recorded in `.agentic/failures.json` and the batch goes on.
The next run writes it again without being asked, up to two retries per page: with
no changed source, a run that finds failed concept, entity or summary pages reuses
the saved plan (`.agentic/last-plan.json` and the evidence it names), marks the
pages' jobs for re-issue and writes only those pages, then runs the later stages,
the check and promotion as usual. It never routes again: once a compile is promoted, routing
prompts carry the new concept dictionary and every write carries its page's new
text, so replaying integration would re-plan and rewrite the corpus to re-draft a
handful of pages. A page that fails its retries waits for a person. `--strict-pages`
stops the run instead.

### Derived prose: packed evidence, page sessions, closed verification

Conflict pages, topic hubs, the home page, literature sections and author
contributions are each written in a page session whose evidence is packed;
figure placements are one-turn jobs without tools. Code packs each
job's complete evidence into the prompt: the tension paragraph(s) with their
`[src:]` tags, concept leads and the source paragraphs that state the tension's
own figures for a conflict page; member concept pages (truncated with an explicit
marker under a 110KB budget) and the leads of the conflict pages linking those
concepts for a hub; hub text and PubMed abstracts for a literature section; the
author's project summaries for a contributions section. A derived page's session
may read only its own scratch directory, so its cache keys on the packed prompt
alone and no dependency on a file read can invalidate it later. The rules and the
pack travel as the session's system prompt, which the CLI caches: the session's
later turns and its review and verify jobs read that prefix, so only the task,
candidate or issues are fresh input.

Each stage defines one rule list (`Contract` in `agentic/prose.py`, instantiated
in the stage module) that is injected verbatim into the writer, the API
pipeline's patcher and the reviewer: word range, required sections, figures only from the input,
`[src:]` tags as the input gives them, directions and denominators as stated,
jargon defined at first use, lead figures cited, no preamble, no legacy platform
names. Deterministic gates, behind the session's `check` tool, report issues by
paragraph index and category: length (with 10% slack), missing headings, preamble, figures
absent from the input, invalid `[src:]` ids, figures without a tag, and figures
absent from their cited sources. Dead wikilinks and legacy platform names are
repaired in code. Only a candidate that passes every gate reaches the reviewer,
which receives exactly the writer's evidence pack and rules plus the numbered
candidate and returns one JSON verdict listing issues with a paragraph index, a
category (number, direction, denominator, caveat, citation, length, format,
unsupported) and a quote. An issue saying the evidence does not support a claim
is an instruction to delete it, not to reword it.

The first review reads the whole page, and no page publishes without one. Every
later `review` call is a **verification**, not a second review: the reviewer
receives the issues it raised and the revised page, and answers whether each is
closed and whether the revision introduced a factual error. An objection it already
raised stays open whatever its category; a newly introduced one counts only when it
touches what the page claims. The open list can therefore shrink or hold but never
grow on settled text. A session gets one review and at most three verifications.

A session that ends with objections still open after a full review is
**salvaged, not dropped**, unless every open objection is presentation only
(the `format` or `length` categories), in which case the reviewed text publishes intact.
Salvage works on the text the reviewer last saw: the paragraphs still objected to
are removed, an editorial note naming the categories takes their place, and the
rest of the page publishes. Headings are never removed, and
a removal that would break a gate other than length, or leave no prose behind, is
refused; only then does the page fail. A session with no full review fails, and a
reviewer that twice returned no usable verdict fails the page closed. Salvages are listed in
`.agentic/salvaged.json`, failures in `.agentic/failures.json`, both with issues and
job keys. A failed page keeps the previously accepted version or is skipped, and the
stage continues. Promotion proceeds with failures reported unless `--strict-pages` is
set, in which case a stage with failures stops the run. The API pipeline
(`scripts/run_pipeline.sh`) has no page sessions and no model reviewer: it drafts
once and patches what the gates report, replacing paragraphs by index against the
candidate's base hash, for at most five rounds.

Topic proposals get **at most one correction**. Every other model job states its
objections once and then only verifies them: a rewrite is asked whether those
objections are closed, never invited to find something new, because a reviewer
asked twice will answer twice and the page never converges. An invalid plan and an extraction
chunk get three, and after its one open review each repair is only verified
against the objections it was meant to close, the same closed question derived
pages get, so the reviewer cannot object to something new each round. The
reviewer sees the host-located findings the chunk owns, so offsets and the
next chunk's overlap are never objections. A chunk whose corrections run out keeps the evidence it did
supply, since those quotes are valid and what the reviewer still wants is
evidence the model would not add; the objections are written to
`.agentic/extraction-gaps.json` and the run continues, as a salvaged page
does. A chunk that validated no evidence at all, unknown usage,
authentication failures, a reply that reached the output cap and other
operational errors still stop the run. The CLI returns the tail of an answer
that ran past `--max-output-tokens` with a successful stop reason, so the cap
is checked against reported usage; otherwise the only symptom is text that
begins mid-sentence and fails to parse far from its cause. A refusal is different: the CLI
would answer on another model for the rest of the session, and the ledger row
and the job's cache key name the configured model, so accepting that answer
would credit the work, and every cached reuse of it, to a model that did not
do it. The refusal is recorded against the configured model and the job is
re-issued on the model the CLI named, keyed and billed to it, so the ledger
always says which model wrote what. That record is a rejected candidate, not
a failure, so it never blocks a later run, and it remembers which model
answered. A safeguard refuses a body of text rather than one prompt, so every
later job carrying that text, the rest of a source's chunks or a page's later
review jobs, goes straight to the model that answered instead of buying the
same refusal again, unless the configured model already answered that job, whose
result stands rather than being discarded and bought again. A refused page session
is recorded the same way and re-run whole on the model that answers. The GPT reviewer has
the same arrangement: a GPT turn the server refuses as possible biological
risk, which reports no usage, is charged the reservation, recorded as a refusal and
answered on GPT-5.6 Sol, and refusal memory sends the rest of that page's review jobs
there. A refusal stated in prose, or a refused GPT turn, goes to a fixed fallback
(`REFUSAL_FALLBACK` in `agentic/runtime.py`): Opus 5.5 and Sonnet 5.5 to Opus 5,
Haiku 5.5 to Sonnet 5.5, and GPT-6.1 Sol, GPT-6 Sol and GPT-6 Luna to GPT-5.6 Sol.
A fallback that refuses again follows its own entry, so a Haiku page goes to
Sonnet 5.5 and then to Opus 5. A Codex fallback fires only on a turn that failed
for biological risk. The memory is per backend, so a refused Claude writer never redirects the
GPT reviewer of the same page or the reverse. It also counts only refusals by the
model about to be asked, so a page Opus 5.5 refused is offered to a new page
writer before any fallback. On this corpus refused attempts were a fifth of extraction
spend, and a flagged report cost five to ten times an ordinary one. A derived
page's worst case is one session and four reviewer calls, each retried once when
its verdict is malformed.

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

A job key holds explicit revisions, not source code or wording. The instructions
for extraction, review, verification and repair are registered under a tag
(`extract@1`, `review@1`, ...), and the key replaces each with its tag at every
JSON escape depth, so a review that quotes the task it checks keys the same way.
A wording fix that keeps the tag keeps cached work. Bump the tag, or
`TOOLS_REVISION` or `CODEX_REVISION` in `agentic/runtime.py` for a tool profile or
the Codex adapter, when a change should re-key what it shaped. A job's key includes
its reasoning effort only when one is set, and a Codex key treats `high` as unset, so
cached jobs keep their keys when no effort is configured; a job whose key includes
an effort never replays an answer cached under the legacy formula below. A page session's
key covers its brief, its starting page, its model, the writer's effort when one
is set, the reviewer's model and effort (so a session another reviewer approved
re-runs), the contract and `AGENT_REVISION` in `agentic/page_agent.py`, and the
files and search inventories the writer read are recorded and revalidated before a
cached session is reused, as tool jobs' reads are; bump that revision when a change to
the session's prompt, tools or acceptance rule should re-key every session. Keys used to hash
`Runtime._query` and the whole Codex adapter, so an edit to either re-bought
every planning batch or every Codex job, extraction included. Work cached under
that older formula is still found: a versioned key with no row falls back to the
legacy key, and a hit is recorded in the ledger's `aliases` table, so one replay
carries the cache over with no duplicated rows or charges.

Scientific compiler or contract changes and manual edits to core pages
conservatively revisit staged sources; model changes do not. The runner compares a
manifest of `wiki/concepts`,
`wiki/entities` and `wiki/summaries` with the one it accepted, so any edit there
outside a curator run, including one by a deterministic stage run by hand, makes
the next run re-integrate every source. The title backfill ran through the
curator for this reason. Code is not hashed for this: what integration means is one
explicit revision, `INTEGRATION_REVISION` in `agentic/batch.py`, bumped when a change
should re-integrate every source. Hashing `batch.py`, `compiler.py` and `check.py`
did so on any edit, which with routing re-plans and rewrites the corpus. A state
accepted under another revision scheme (`REVISION_SCHEME` in `agentic/runner.py`) is
adopted once and recorded under the current scheme at the next promotion. Scheme 5
took model identities out of the scientific revision and out of the derived stage
revisions, which are now the named constants in `STAGE_REVISIONS`
(`agentic/curator.py`) plus the contract; stage code is not hashed either, so bump a
stage's constant when a change should rewrite its pages. When a scheme-4 state is
adopted, each derived stage whose recorded inputs and outputs still match is
re-stamped under the new formula instead of rewritten (`adopt_editorial` in
`agentic/runner.py`), and figures are not forced by the changed figure revision
alone. From scheme 5 an accepted state records its contract, and adoption applies
only when that contract is still the one in force. A scheme-4 state recorded none,
so adopting it assumes the contract is unchanged: edit the contract in a run of its
own, not in the run that first adopts a scheme-4 state. A source
is recorded as integrated even when one of its pages fails, since the page's retry,
not a second integration of the source, is what writes it again. Deleted sources require a separate scientific retraction;
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

`status` lists the failed pages beside the totals. Failed integrated pages are
retried automatically, as above. For a derived page, `retry --page` and
`retry --all-failed` mark every job a failed page used as rejected and drop the
owning stage from the accepted state, so the next run (which would otherwise
report "unchanged") re-runs that stage, issues the page a new session (resuming
from its scratch files under `.agentic/pages/` only when they match the check the
host last recorded) and leaves every other cached page untouched. A pass that records any failure retires no pages,
so a failed replacement's predecessor stays published under its old slug.

Use `retry` only after inspecting a saved failed/rejected job. Malformed figure
JSON/indices and entity retention-gate refusals stop the run and need inspection
before explicitly retrying the affected job. A derived page whose session failed
does not stop the run; its issues and job keys are in `.agentic/failures.json`. A
failed session is not replayed from the ledger: whenever its stage runs again, the
page gets a new session, which spends again. Excess valid figure placements are trimmed to the page's cap. Completed editorial results remain cached; stopping
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
With `CBORG_API_KEY` set, it also embeds the sections that have no vector yet.
Then run `uv run python -m beril_wiki.publish.search_data push` before opening
the pull request: the vectors live on the `search-data` branch, and a pull
request whose sections lack vectors fails its build.
The curator does not commit, push or deploy. Do not publish concurrently with
promotion.

## Development verification

Offline tests exercise the actual subprocess pipeline with recorded model and
PubMed replies: the stage schedule, dependency enforcement, gates, the API
pipeline's paragraph patches, closed verification, salvage, recorded page
failures, errata placement, topic decisions, cache invalidation, scheme-4
adoption, subscription setup and promotion recovery. In those tests a page
session is a replay of recorded writer replies through the stage's own check
and review callbacks; the session itself (submit acceptance, the review limit,
the path and loop-guard hooks, resume from scratch) and the pilot's outcomes
and judge have their own unit tests. They do not establish model quality or real subscription
savings. The tests workflow runs them, with ruff and ty, on every pull request
and on `main`; the publish workflow validates the committed wiki, renders it and
type-checks the theme, and neither needs a key or an observatory checkout. The
curator has not yet been accepted through a real source update. MCP remains below
version 2 for the SDK's in-process tool compatibility.

Specs, plans and review dispositions are local gitignored files under
`docs/superpowers/`. Independent Claude Code reports are retained outside the
checkout. A representative capped live update remains the acceptance step before
using this for a large production compilation.
