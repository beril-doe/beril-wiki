# The stateful pipeline

`beril-wiki` is a second way to maintain the wiki. It sits beside the curator's runtime
in `src/beril_wiki/agentic/` and imports the curator's stage modules
(`src/beril_wiki/stages/`) for their checks and page layouts. The curator treats pages as build
outputs and reschedules work when an input hash changes. This pipeline treats an
accepted page as state: it changes when a report gives it a reason to, and at no other
time.

It has four parts, and an agent of any vendor uses the same four.

| Part | Where | What it is |
| --- | --- | --- |
| Records | `knowledge/`, `wiki/` | Git text: claims with their quotes, and which claims each page section rests on |
| Tools | `src/beril_wiki/kb/tools.py` | every read and every gated write an agent may make, served over MCP and the command line |
| Skills | `skills/wiki-*/SKILL.md` | the instructions for each role, in Markdown, with no SDK detail |
| Runners | `src/beril_wiki/kb/agents.py` | two adapters that start a vendor harness on a skill: the Codex app server and the Claude Agent SDK |

## What starts model work

Three things, and nothing else:

1. A report in `corpus/` whose content hash is not the one recorded in
   `knowledge/sources.jsonl`. `beril-wiki plan` lists it as `ingest` or `revise`.
2. A claim that a revised report changed or no longer supports. `revise` edits the
   sections that rest on that claim.
3. An operator naming sections and a reason: `beril-wiki refresh SECTION... --why TEXT`.

A fourth command, `beril-wiki compile`, builds every page from the reports in one run.
It is for an empty wiki (see "Compiling the whole wiki"); once it has finished, the
three triggers above are again the only ones.

Editing a skill, the tools, `wiki.yaml`, the contract or a wiki page schedules nothing.
`beril-wiki plan --json` prints `{"tasks": []}` after any of them. A rule change reaches
accepted prose only through `refresh`, on the sections you name.

## Records

```
knowledge/sources.jsonl            one row per report: the content hash last ingested
knowledge/claims/<report>.jsonl    one claim per line
knowledge/pages/<kind>/<slug>.json which claims each section of a page rests on
knowledge/backlog/<report>.jsonl   findings queued because a cap was reached
knowledge/log/<run>.jsonl          one line per accepted edit: base, result, writer, reviewer
knowledge/topics.json              the fixed topic list: slug, title, scope
knowledge/catalog.json             the page list a compile settled: kind, title, scope, topic or type, aliases
knowledge/routes/<report>.jsonl    which page each claim was routed to, and by which step
knowledge/glossary.json            one reviewed expansion per abbreviation
```

Files are split by report, page and run, so two machines that ingest different reports
touch different files and Git merges them.

A claim is one statement a report makes: `id`, `kind` (`finding`, `null`, `caveat`,
`entity`, `figure`), `text`, the verbatim `quote` behind it with its character span, the
report heading it sits under, a hash of that block of the report, and `status`
(`active`, `recheck`, `retracted`). Ids never change.

A page sidecar maps each section to its claims, and labels how each link was made:
`edit` (an editor used the claim and a reviewer accepted the text), or `number`,
`overlap` and `plan` (inferred by the one-time import; see below). A section is the
lead of a page or one H2 with its body, addressed as `concepts/<slug>#<anchor>`.

`.agentic/index.db` is a SQLite view of all of this (sections, claims, links, aliases,
FTS5 search). It is gitignored. Any command rebuilds it in about a second when a file
it reads has changed, so a fresh clone or a `git pull` needs no step.

### Importing the legacy evidence

```sh
uv run beril-wiki import-evidence --from /path/to/old/.agentic
```

Writes `knowledge/` from the old runtime's evidence store and last plan, with no model
call. It refuses to run when `knowledge/` already holds records, because a second
import would replace claims, links and review stamps accepted since. On the 75-report corpus it imports 8,006 claims; every quote was found at its
recorded span in `corpus/`. It links each claim to the page the old plan routed it to,
and to a section where a paragraph citing the claim's report repeats its figures or
most of its words. Measured against the old plan's own routing on concept pages, a
looser rule (half the words) agreed 27% of the time and the adopted rule 53%, so
imported links are advisory. `revise` therefore also scans for stale figures (below).

## Tools

`beril-wiki tool list` prints them. Every tool returns JSON with `ok`.

| Tool | Roles | What it does |
| --- | --- | --- |
| `search(query, kind, limit)` | read | sections about a topic, with snippets; a page by title or alias |
| `catalog(kind, topic, offset)` | read | every page of a kind with a one-line description |
| `outline(page)` | read | a page's sections: size, cited reports, linked claims, opening words |
| `read_section(section)` | read | one section in full, its `sha`, and the claims it rests on |
| `claims(source, section, ids, query, quotes)` | read | claims, with quotes on request |
| `neighbors(page)` | read | links in and out, topic membership, conflict pages |
| `read_source(source, start, end)` | read | up to 12,000 characters of a report |
| `submit_claims(claims)` | extract | records claims; rejects a quote that is not in the report verbatim |
| `propose_plan(targets, skipped)` | curate | places every new claim; enforces the page caps and queues the overflow |
| `edit_section(section, base_sha, body, claims, declined, dropped)` | edit | stages one section; see the gate below |
| `review(section, sha, verdict, objections)` | review | accept, or revise with objections that quote the new text |
| `finish(note)` | all | ends the session |

| `submit_record(record)` | record | one structured record, checked by its stage's own code |
| `write_page(body, declined)` | page | a whole page written from a pack of claims; see "The page gate" |

An agent never writes a file. A write tool stages a result in the run folder; the host
applies it after review.

### Packed sessions

Three roles have exactly one tool and no read tools: `record` (`submit_record`),
`verdict` (`review`) and `page` (`write_page`). The task message carries everything the
work rests on: the claims with their verbatim quotes, the text under review, the pages
that may be linked. The session ends when its one call is accepted. The host stops the
harness there (a turn interrupt on the Codex app server, a `PostToolUse` hook on the
Claude Agent SDK), so no turn is spent on `finish` or a closing remark.

This is what bounds a session. In the first pilots a reviewer with read tools used
110,000 to 150,000 tokens to judge a record a few hundred characters long, because each
tool turn sent the whole context again; three quarters of all tokens were such re-sent
context. A packed review of a page uses about 13,000. Every record stage and every
compile step runs packed. The section tools above remain for the one-report workflows
and for a person driving a harness by hand.

### The section gate

`edit_section` refuses an edit, and says why, when any of these holds:

- `base_sha` is not the section's current hash (someone else changed it).
- The body contains an H1 or H2, exceeds `max(1500, words before + 400)` words, or
  changes any section after it (an unclosed code fence does).
- A `[src: id]` names a report that does not exist, or a `[[link]]` a page that does not.
- A listed claim is unknown or retracted, or its report is never cited.
- An assigned claim is neither used nor declined with a reason.
- A figure or a cited report in the accepted text is missing and not listed in
  `dropped`. A claim the report withdrew takes its figures with it.
- A paragraph the edit wrote or changed states a figure that is in no report the
  paragraph cites (the rule `check` applies). Paragraphs carried over word for word
  are not re-judged, and neither are the forward-looking sections `check` exempts.
- In a revision, the text still states a figure the revised report no longer contains.
- The text carries line breaks written as the two characters backslash and n, which is
  what a doubly escaped tool argument looks like. Unchecked, a ten-paragraph section
  is published as one paragraph.

`submit_claims` likewise rejects a claim whose quote is not in the assigned part of the
report verbatim, or whose text states a figure the quote lacks. `propose_plan` rejects
a claim placed twice, a section targeted twice, a summary or new conflict page as a
target, and a new page whose supporting claims from a second project it cannot find.

`finish` is refused once to a writer with no accepted record, a reviewer with no
verdict and a curator with no plan, so a session cannot leave beside a rejection it has
not read.

Three refusals end the section for that session. A session also has a call budget and a
reading budget; when either is spent the read tools refuse and tell the agent to
submit what it has. That is what bounds a loop.

| Role | Tool calls | Reading (characters) |
| --- | --- | --- |
| extract | 40 | 400,000 |
| curate | 30 | 96,000 |
| edit | 30 | 160,000 |
| review | 12 | 120,000 |

### The page gate

`write_page` takes a whole page. The writer cites claims by the tags of its task
message, `[C4]` or `[C4, C9]`; the host turns each tag into its report (`[src: id]`)
when it publishes, and the sidecar records which claims each section rests on. The
gate refuses a page, and says why, when:

- a tag is not in the claim list, or the body writes `[src: ...]` itself;
- a claim given to the writer is neither cited nor declined with a reason;
- a claim an earlier pass cited is no longer cited;
- a paragraph or list item that states a figure, or runs to 14 words or more, carries
  no tag (the forward-looking sections `check` exempts are skipped);
- a statement states a figure that the reports of its tags do not contain;
- a wikilink points outside the list of pages the task message allows;
- the lead is missing, a heading repeats, a required closing section is missing
  (`Open Directions` on a concept, `Key Findings` on a summary), a section exceeds
  1,500 words, or the text carries escaped line breaks.

## Skills

`skills/wiki-extract`, `wiki-curate`, `wiki-edit` and `wiki-review` each hold one
`SKILL.md`: what the role is for, the tools it has, the procedure, the editorial rules
and when to stop. Each record stage has its own (`wiki-findings`, `wiki-gists`,
`wiki-novelty`, `wiki-links`, `wiki-directions` and so on), and `wiki-card-review` is
the reviewer's for all of them. A compile adds `wiki-glossary`, `wiki-propose`,
`wiki-consolidate`, `wiki-route` and `wiki-page`, with `wiki-glossary-review`,
`wiki-consolidate-review` and `wiki-page-review` for their second opinions. A runner sends the skill, then the "Domain Rules" and "Integration
Rules" of `contract/AGENTS.md`, as the agent's instructions. Nothing in a skill names a
vendor, so the same file drives both harnesses, and editing one changes the next run
without scheduling any work.

## Runners and models

`wiki.yaml` names a model for each role as `model@effort`. A model named `gpt-*` runs
on the Codex app server through the `openai-codex` SDK; `claude-*` runs on the Claude
Agent SDK. Both get the skill as instructions and one loopback MCP URL that lists only
the tools of that session's role. Shell, file, web, plugin and app tools are off, and
each Codex thread runs in its own `CODEX_HOME`.

| Role | Default | Writes |
| --- | --- | --- |
| `extract` | `gpt-6.1-sol` | claims from a report |
| `curate` | `claude-sonnet-5-5` | where the claims belong; which topic a new concept joins |
| `edit` | `claude-haiku-5-5` | existing sections of concept, entity and summary pages |
| `write` | `claude-sonnet-5-5` | new pages (a report's summary, a new concept or entity), conflict pages, hub sections, author contributions, literature context |
| `cards` | `claude-sonnet-5-5` | findings, plain summaries, literature labels, directions, links, shared results |
| `labels` | `claude-haiku-5-5` | result types and follow-up needs |
| `queries`, `figures` | `gpt-6.1-sol` | PubMed queries; figure placements |
| `review`, `card_review` | `gpt-6-luna` | the second opinion on sections and records |
| `findings_review` | `gpt-6.1-sol` | the second opinion on findings and guarded literature labels |

This is the curator's own policy (`agentic.yaml`): Claude plans and writes, GPT
extracts and reviews. One difference: a page that does not exist yet goes to `write`,
because the first full pilot had `claude-haiku-5-5` write a new summary that the
reviewer refused twice for wrong definitions and miscounts.

- A writing role and the role that reviews it must be on different vendors. A run
  refuses to start otherwise.
- A vendor that reports a usage or rate limit stops the run at once. Nothing is
  retried on another model or vendor. The run says which vendor and model, and the
  same command resumes it when the quota is back. With `--quota-wait SECONDS` (a
  compile left to run overnight) the run waits instead and asks the same model again.
  A spent allowance ("usage limit", "resets at") is asked again every 15 minutes. A
  request turned away as one too many ("429 Too Many Requests") is asked again after
  about a minute, then two, doubling up to 15, until the wait is used up.
- A vendor does not say how many sessions it takes at once. Each model starts at
  `jobs`; a refusal lowers its limit to the number of sessions it was running, and
  each run of that many successes raises the limit by one. `notes.log` in the run
  folder records every change.
- A vendor that answers "at capacity", "overloaded" or "routing discovery timed
  out" gets the same session again after 45 seconds, up to six times with a longer
  pause each time, on the same model.
- A vendor that answers "Not logged in" stops the run at the first such session. Sign
  in again and the same command resumes it.
- Ten sessions in a row that fail for any other reason stop the run.
- Both harnesses use the subscription login by default. `BERIL_WIKI_AUTH=api` keeps
  `OPENAI_*` and `ANTHROPIC_*` in the child environment so each bills its API key. The
  API mode has not been exercised yet.
- `BERIL_WIKI_CODEX_BIN=/path/to/codex` runs a Codex binary other than the one the SDK
  bundles. The bundled 0.159.3 rejects `gpt-6.2-sol` on a ChatGPT login; the installed
  0.171.0 accepts it.

## Workflows

```sh
uv run beril-wiki plan                       # what would run, and why; no model call
uv run beril-wiki ingest <report>            # a report the wiki has not read
uv run beril-wiki revise <report>            # a report whose content changed
uv run beril-wiki refresh <section>... --why "state the reason"
uv run beril-wiki impact --source <report>   # sections that rest on a report or --claim
uv run beril-wiki lint                       # free checks on claims, links, backlog
uv run beril-wiki runs                       # past runs with their spend
```

`ingest` runs only on a report `plan` lists as new, and `revise` only on one it lists
as changed; either refuses a report that is current. Each run pins the report's hash
at its start and stops if the file changes underneath it. One run at a time owns a
checkout: the commands take the same lock file as the curator (`.agentic/lock`).

`ingest`: one extract session reads the report and records claims. The session must
finish and must have read every character it was assigned; otherwise nothing is
recorded. Its call budget grows with the report (two calls per 12,000 characters). One curate session
reads the wiki through the tools and proposes where the claims belong: at most 3
concept pages, 1 topic hub, 3 entity pages and 2 conflict pages, plus the report's own
summary page. A new concept or entity page needs claims from two projects. Each target
section then gets an edit session and a review session by the other vendor, at most
`rounds` (2) times. An accepted edit is written to the page, its sidecar and the log; a
rejected one leaves the page untouched and queues its claims. If the report's summary
page is not accepted, the run stops before the record stages, because findings, author
pages and data pages link to it; the same command tries the summary again.

`revise`: claims whose quote and whose block of the report are unchanged carry forward
with no model call. Changed blocks are extracted again. A re-extracted claim with the
same quote and the same figures confirms the old claim, which keeps its id. Claims
nothing confirms are retracted, and each section linked to one gets an edit, a hub or
entity lead included. A re-extracted claim confirms an old one only when its kind,
quote and wording are the same; the extractor is shown the old claims and told to
repeat those that still hold. Code cannot tell a paraphrase from a reversed result, so
a reworded claim is treated as new and the old one as withdrawn. A section that cites the
report and appears to state a retracted claim (same figures, a third of its words) is
edited too, linked or not. At most `max_sections` sections per run. A correction that
could not be applied (over the cap, rejected, unreviewed, or with no section found)
stays in the backlog marked `withdrawn`, and `plan` lists its section under
`corrections_owed` until `refresh` settles it. Every correction is queued before the
first edit starts and cleared when its section's edit is accepted, so a run that dies,
or a later revision that supersedes it, cannot lose one. A correction owed on a page as
a whole stays listed until you remove its row by hand.

After the section edits, `ingest` and `revise` run the record stages for the report,
each a module under `src/beril_wiki/kb/jobs/` with its own skill:

| Stage | Owed for | Stored in |
| --- | --- | --- |
| `findings` | the report: up to 6 headline findings | `wiki/findings/`, `state/headlines.json` |
| `gists` | each of its findings: a plain summary | `state/gists.json` |
| `outcomes` | each listed finding: its result type | `state/outcomes.json` |
| `novelty` | each finding: PubMed queries, a label, an other-vendor check on a novelty or tension claim | `state/novelty.json` |
| `topics` | a concept page created in this run: which hub it joins | `state/curator-topics.json`, the hub's member list |
| `links` | result pairs and references that involve the report | `state/links.json` |
| `shared` | groups of linked results that include one of its findings | `state/shared.json` |
| `conflicts` | a multi-project paragraph in a `Tensions` section edited in this run, with no page yet | `wiki/conflicts/` |
| `directions` | the one topic the report feeds most: accepted directions kept, at most 2 added | `wiki/directions/`, `state/directions.json` |
| `followups` | each direction written in this run | `state/followups.json` |
| `literature` | a hub edited in this run that has no literature context | the hub page, `state/litcontext.json` |
| `authors` | the report's authors: their contributions section | `wiki/authors/`, `state/authors.json` |
| `figures` | a summary, hub or conflict page this run created or changed | `state/figures-placements.json` |

A record is owed when its report is ingested or revised and the record is missing or
rests on a withdrawn claim. It is never asked again because a prompt, a model or code
changed; the curator's hash keys are gone. A revision also removes what it makes false,
whether or not a replacement is accepted:

- A headline whose claim was withdrawn loses its page. Its plain summary, result type,
  literature label and links go with it, and with any finding whose wording changed.
- A direction that builds on a removed finding or conflict is retired, in any topic.
- A conflict page whose paragraph an edit reworded is retired once its replacement is
  accepted.
- A figure the report no longer embeds is taken off the pages it was placed on.
- A project reference is asked again when the sentences it was judged from change.
- An author removed from the report gets a contributions section written without it. Each stage keeps the curator's own checks
and file formats, imported from `beril_wiki.stages`, so `publish` reads the results
unchanged. A record is written by one session with a single gated tool
(`submit_record`) and, where the curator had a reviewer, checked by the other vendor.
The curator's deterministic stages (author and data stubs, titles, the platform's
name, errata) run before the record stages and again before figures.

`refresh`: re-edits the sections you name with the instruction you give, places any
findings queued for them and applies any correction owed there.

Every run stops starting sessions at `--max-tokens` or `--max-usd`. Tokens (250,000) and
USD 0.30 are held for each session before it starts, so parallel sessions cannot both
spend the same remainder. The caps bound admission: a session in flight ends at its own
tool-call budget and timeout, and only the Claude harness is also given the remaining
USD as a hard limit, so a run can pass a cap by what its running sessions use beyond
their holds. `--max-usd` needs a price in `wiki.yaml` for every Codex model. A stopped
or crashed run resumes from its first unfinished step when you run the same command
again on the same report revision; finished steps are not repeated, a section refused
for budget is tried again with the reviewer's last objections, and an accepted edit
that a crash left half written is completed from its journal before any writer is
admitted. A failed session that reported no usage is charged what was held for it. A record
job whose session failed or gave no verdict leaves the run stopped, not done, and the
report unread, so the same command retries it; a record a reviewer refused twice is
dropped and the run finishes. A record keeps its reviewer's last objections across a
stop, and one accepted just before a crash is stored on resume without a new session. Run state lives in `.agentic/runs/<run>/` and is disposable once the run is
done, because accepted results are already in Git text.

## Compiling the whole wiki

```sh
uv run beril-wiki compile --jobs 8 --quota-wait 43200
uv run beril-wiki compile --sources a,b,c --pages-only   # a pilot on some reports
uv run beril-wiki compile --claims-only    # stop when the reports are read into claims
uv run beril-wiki compile --routes-only    # stop when the page list and routes are settled
```

`ingest` reads one report into a wiki that exists. Run once per report on an empty
wiki, it would rewrite a shared page each time another report touched it, and the page
list would depend on the order the reports arrived in. `compile` does each kind of work
once, from the reports in `corpus/` and the topic list in `knowledge/topics.json`:

1. **Extract.** Every report becomes claims, in parallel. A report is cut at its
   headings, and inside a long section at its paragraph breaks, into parts of about
   8,000 characters. Each part is read by its own session, which gets the part, the
   report's outline and its opening in the task message and records the claims in one
   call.
2. **Glossary.** One session proposes the expansion of each abbreviation the claims
   use, with the expansions the reports themselves give; the other vendor reviews the
   list. Writers expand a term only from this list and reviewers accept it, so a term
   reads the same on every page.
3. **Propose.** For each report, one session proposes the concept and entity pages its
   claims belong on: a title, a one-sentence scope, a topic or an entity type, and the
   claims.
4. **Consolidate.** The proposals of all reports are merged into one page list: the
   same question or the same thing under two names becomes one page. The session
   lists only the pages it merges or renames; a candidate it leaves out stays a page of
   its own. The other vendor reviews the list. If the list is still refused after the
   second round, the merges the reviewer faulted are undone and the rest are kept.
   Entities with the same name are merged in code first. Over 220 candidates, concepts
   are merged topic by topic and entities type by type.
5. **Route.** With the list settled, each report's claims are offered to every page, so
   a claim reaches a page another report proposed. A claim sits on at most three pages.
6. **Write.** Each page is written once from every claim routed to it, 60 claims to a
   pass, and each pass is reviewed by the other vendor. A concept needs three claims.
   An entity needs two claims from two reports, because the site shows an entity page
   only when two reports speak of the entity. Thinner pages are not written; their
   claims stay in the summaries and are listed in `knowledge/routes/unwritten.json`.
   After the pages are written, `knowledge/routes/uncited.json` lists for each report
   the claims that no page cites, read from the pages as published.
   A report's summary is written from all of its claims. Up to 180 claims that is one
   page in passes, like any other. A longer report is summarised in parts: one session
   writes the opening (lead, Key Findings, Caveats and Open Work) from what the report
   says under its own summary headings, and one session for each part of the report, of
   at most 50 claims and cut at the report's headings, writes that part's section from
   every claim in it. Each is reviewed on its own, the sections are written side by
   side, and code puts them together in the report's order. No session rewrites the
   page, so a refused part leaves the others standing.
7. **Records.** Findings, plain summaries, result types and literature labels run per
   report. Topic hubs, the home page, links, shared results, conflict pages, research
   directions, follow-ups, literature context, author pages and figures then run once
   for the corpus.

A pass has at most two writer sessions and two reviewer sessions. A writer has three
attempts at the page checks in a session. On the third, a page whose every statement
passes is taken even if it leaves some of the pass's claims out; those claims are
recorded as not placed, and for a concept or entity page they go to the backlog. If the
reviewer still faults statements after the second round, the host removes exactly those
sentences or list items, records their claims as declined, and checks the page again;
what is published is text the reviewer did not fault. A page therefore always ends
accepted or rejected, and no page is rewritten because another one changed. A published
page cites each sentence after its closing period, as the rest of the wiki does.

A topic hub or the home page that is still refused after the second round is written
by code instead: the topic's scope and its concept pages, without a narrative. The wiki
cannot be read without those pages, so they do not stay missing.

Every step is recorded in the run, and each step writes its files before it is
recorded. The same command resumes a stopped compile and pays for nothing twice. A
second `compile` of reports that were already compiled refuses to start. A compile
that stops where `--claims-only`, `--routes-only` or `--pages-only` asked it to exits 0
and leaves the run open for the next command. A part of a long summary is reused only
for the claims it was written from, so a part cut differently on a later run is
written again.

### Watching a run

```sh
uv run beril-wiki status              # the newest run, on one screen
uv run beril-wiki status --watch 600  # return when it needs someone, ends, or after 600 s
```

`status` reads the run's `run.json`: the stage and how far it is, sessions open and
waiting on a vendor, failures among the last twenty, spend, and a verdict. It exits 0
for `ok` and `done` and 3 for a verdict that needs someone:

| Verdict | Meaning |
| --- | --- |
| `ok` | sessions are finishing; a vendor pause under five minutes counts as working |
| `waiting` | a session waits more than five minutes on a vendor limit |
| `failing` | half of the last twenty sessions failed for a reason other than a vendor refusal |
| `stuck` | a session has run past its timeout |
| `idle` | no session is open and none has finished for ten minutes |
| `dead` | the record says running and the process is gone; run the same command again |
| `stopped`, `done` | the run ended, with its reason |

A compile also stops itself when its pages go wrong. Once ten pages have been written
in a run, more than half of the last twenty ending refused or failed stops it, so a
fault in a skill or a check costs about twenty pages and not the page list. Fix the
cause and run `beril-wiki compile --retry-rejected`, which writes the refused pages
again; without the flag a refused page is not asked for twice.

## By hand

The same tools serve a person working in any MCP client.

```sh
uv run beril-wiki mcp            # read-only tools over stdio
uv run beril-wiki mcp --write    # also edit_section, gated, applied without review
uv run beril-wiki tool search '{"query": "lanthanide methanol dehydrogenase"}'
```

Claude Code picks the server up from `.mcp.json` in this repository. For Codex:
`codex mcp add wiki -- uv run beril-wiki mcp`. Point the client at a skill file when
you want it to follow a role's procedure.

## Beside the curator

Until the nightly job is switched over, one pipeline owns writes to a checkout.

- An accepted edit to a concept, entity or summary page updates that page's hash in
  `state/agentic.json`, so the curator does not read it as a hand edit and re-integrate
  every report.
- Figure placements in `state/figures-placements.json` follow their paragraphs through
  an edit, so `publish` keeps a page's figures, and the placements file's hash is
  updated in the curator's `figure_outputs` so its figure stage is not forced.
- This pipeline now produces everything the curator does for a report. The curator's
  stage modules remain as the library of checks, page layouts and state formats the
  record stages import, and its runtime (`agentic/`) is still what the nightly job
  runs until that job is switched to `beril-wiki plan` and `ingest`.
- Do not run `agentic run` on a checkout after `beril-wiki ingest` has added a report
  there: the curator would see a new report and integrate it a second time.
- `publish` lists the findings queued for a page under "Queued findings" at the end of
  that page. With an empty backlog, as on the current corpus, pages are unchanged.

## Pilots

Run on 2026-11-23 on scratch copies of the wiki, with subscription logins. The four
pilots below ran before the independent review; the reruns after them ran on the
reviewed code. Costs for
Codex are API-equivalent estimates from the prices in `wiki.yaml`; Claude costs are
what the SDK reported. Each pilot ran once.

**One skill set on both vendors (held-out ingest).** The report
`cazyme_pangenome_ecology` (19.6 KB, never ingested) was ingested twice from the same
skills and tools, with the vendors swapped.

| | Codex writes, Claude reviews | Claude writes, Codex reviews |
| --- | --- | --- |
| Models | `gpt-6.1-sol` extract, curate, edit; `claude-haiku-5-5` review | `claude-haiku-5-5` extract; `claude-sonnet-5-5` curate, edit; `gpt-6.1-sol` review |
| Claims extracted | 96 | 59 |
| Sections accepted | 5 of 5, each in round 1 | 5 of 5, one in round 2 |
| Sessions, summed session time | 12, 431 s | 14, 341 s |
| Tokens (share cached) | 1.11 M (76%) | 1.20 M (72%) |
| Cost | USD 0.46 estimated | USD 0.85 (0.56 reported by Claude, 0.29 estimated) |
| `check` on the result | 0 errors | 0 errors |

Both curators chose the same two concept pages. The Codex reviewer returned one
section for stating a phenotype the evidence did not measure; the editor fixed it in
round 2. Two blind judges (Gemini 4 Neon, GPT-6.2 Astra) scored the one section both
runs edited: clarity 5 for the accepted text, 4 for the Codex edit, 6 for the Claude
edit, with both judges giving the same three numbers; fidelity 9 and 10 for the Codex
edit, 8 and 8 for the Claude edit. The Claude edit copied a p-value bound from the
report's prose that the report's own table contradicts, which no gate catches because
the figure is in the report.

**Structured tools against raw Markdown.** The curate task was repeated with the
harness's own file tools on `wiki/` in place of the read tools; `propose_plan` stayed.

| Model | Read path | Tokens | Time | Sections targeted |
| --- | --- | --- | --- | --- |
| `gpt-6.1-sol` | wiki tools | 195 K | 49 s | 2 concept pages, 1 entity |
| `gpt-6.1-sol` | shell on Markdown | 385 K | 75 s | the same 2 concept pages, 1 entity |
| `claude-sonnet-5-5` | wiki tools | USD 0.108 | 30 s | 3 concept pages, 1 entity |
| `claude-sonnet-5-5` | Read, Grep, Glob | USD 0.112 | 29 s | 2 entities, 1 topic hub, no concept page |

On Codex the raw path cost twice the tokens for the same answer. On Claude it cost the
same and found less: the agent read two entity pages and never opened a concept page.

**Revision.** In the Codex-written copy, three figures in the report were changed
(a correlation, a test statistic and a percentage), touching 7 of its 26 blocks.
`revise` carried 71 claims forward with no model call, re-extracted the 7 blocks,
confirmed 22 claims, retracted exactly the 3 whose figures changed, and edited the 3
sections that rested on them. Every other section of those pages was byte-identical,
no old figure remained in the wiki, and `check` reported 0 errors. 734 K tokens,
USD 0.34 estimated, 7 sessions.

**Harness isolation.** With Codex apps enabled, `gpt-6.1-sol` answered a request to
call `search` by calling the ChatGPT GitHub connector's `search`. The runner now turns
off `apps`, `plugins`, `multi_agent` and `image_generation`; the same probe then used
the wiki tools and its input fell from 97 K to 39 K tokens.

**Reruns after the first two reviews.** The same held-out ingest with Codex writing, the
default at that time,
accepted 3 of 4 sections; the fourth lost its verdict because the reviewer wrote
"accept" with a qualification and then finished, which the `review` and `finish` tools
now refuse. `refresh` on that section placed its queued findings in round 2, after the
reviewer objected that two results used different openness metrics (470 K tokens,
USD 0.14). The same three-figure revision then edited 1 section and left 2 listed under
`corrections_owed`: the test edit had changed "71%" in one of three places, and the
reviewer refused text built on a report that contradicts itself (1.67 M tokens,
USD 0.58). After the second review's fixes, a different held-out report
(`thermodynamic_impact`, 20.9 KB) was ingested: 147 claims, 3 of 4 sections accepted,
one refused after two rounds, no session failed (1.54 M tokens, USD 0.67).
`check --strict` reported 0 errors on each result. Across all runs the pilots cost
about USD 4.0 API-equivalent, of which Claude reported USD 0.80.

**The whole pipeline on two held-out reports.** With the default models (Sonnet and
Haiku write, `gpt-6.1-sol` extracts, `gpt-6-luna` reviews), `gc_ecotype_ecology` and
then `thermodynamic_impact` were ingested into one scratch copy, every record stage
included.

| | `gc_ecotype_ecology` | `thermodynamic_impact` |
| --- | --- | --- |
| Claims extracted | 93 | 145 |
| Sections accepted | 5 of 5 (four concept, entity and conflict sections, the summary) | 3 of 4; one entity section refused after two rounds, its claims queued |
| Finding pages | 4, each with a plain summary | 5, each with a plain summary |
| Result types | 3 accepted, 1 refused twice | 5 |
| Literature labels | 4, all "Insufficient literature evidence" | 5, all "Insufficient literature evidence" |
| Links | 1 project reference | none owed |
| Research directions | 1 added to the 6 accepted for its topic, with its follow-up need | 2 added, one follow-up need accepted and one refused twice |
| Author pages | 1 rewritten, 1 created | 1 rewritten |
| Sessions, failed | 56, 0 | 64, 0 |
| Tokens (with cached input) | 6.10 M | 5.71 M |
| Cost | USD 2.19 | USD 1.73 |

`check --strict` on the result: 0 errors. `beril-wiki plan` then listed no task. Of the
USD 3.92, Claude reported 2.86 and the rest is the Codex estimate.

A first attempt at the same two runs (USD 3.21) found four defects, fixed before the
runs above:

- A section edit arrived with its line breaks escaped, and a ten-paragraph `Tensions`
  section was published as one paragraph. No check caught it. The gate now rejects it.
- A writer called `finish` beside a rejected `submit_record` and left with no record on
  file, twice. `finish` is now refused once to a writer with no accepted record.
- `claude-haiku-5-5` wrote a new summary with wrong definitions of two terms and a
  miscount, and the reviewer refused it twice. A new page now goes to the `write`
  role, and the skill forbids a definition its report does not give.
- A reviewer refused a new research direction that the rules allow. The rule is now
  part of the input both models read.

Two things the full pilot showed and nothing here changes. PubMed returned no abstract
for 6 of the 9 findings, so every label is "Insufficient literature evidence"; in the
curator's stored labels that happened for 21 of 342 findings. The queries and the
retrieval code are the curator's, and the cause of the gap is not established on a
sample this small. And the planner is not repeatable: the two attempts placed the same
report's claims on different concept pages, and both sets passed review.

## Compile pilots

Run on 2026-11-23 and 24 on scratch copies that started from an empty wiki, with the
default models and subscription logins. Costs for Codex are API-equivalent estimates
from the prices in `wiki.yaml`; Claude costs are what the SDK reported.

| | Pilot 1 | Pilot 2 |
| --- | --- | --- |
| Sources | 5 reports | 8: 7 reports, one of 297,000 characters, and the discoveries digest |
| Claims | 984 | 4,172 |
| Pages | 83 accepted, 1 refused | 101 accepted, 2 refused; 43 of the 138 listed pages too thin to write |
| Sessions, failed | 794, 62 (60 of them "429 Too Many Requests") | 1,290, 11 (10 of them "429") |
| Most turns in one session | 10 | 4 |
| Tokens | 12.5 M | 30.1 M |
| Cost, every stage | USD 15.59 | USD 43.80 |
| `check --strict` | 0 errors | 0 errors |

In pilot 2 the page writer cost USD 22.45 of the 43.80 (238 sessions, 29,000 tokens
each), the page reviewer USD 0.97, extraction USD 3.03, and the record stages the
rest. Pilot 1 read each report in one long session of 119,000 tokens; pilot 2 read
reports in parts at 20,100 tokens a session and found 27% more claims on the four
reports both read. Each pilot ended `stopped` with one or two record jobs failed (a
research direction in pilot 1; one findings and one literature job in pilot 2), which
the same command would ask for again.

**Blind judging.** Gemini 4 Neon, a model outside both vendors, scored pages from 0 to
10 without knowing which version it saw. For a summary it saw the deployed page and
the new page side by side with the full report, in both orders, each order sent to a
different judge. A page with one altered or unsupported number scores at most 4 on
fidelity. Each cell below is the mean of two judgements.

| Summary of | New: fidelity, coverage, clarity, synthesis | Deployed | Preferred in both orders |
| --- | --- | --- | --- |
| `ecotype_analysis` | 10.0, 9.5, 8.0, 7.0 | 10.0, 9.5, 9.0, 8.0 | deployed |
| `field_vs_lab_fitness` | 9.5, 10.0, 9.0, 7.0 | 10.0, 9.0, 6.0, 9.0 | new |
| `metal_fitness_atlas` | 9.0, 9.0, 8.0, 8.0 | 4.0, 8.5, 6.0, 8.0 | new |
| `pangenome_openness` | 10.0, 9.0, 9.0, 8.0 | 9.0, 9.0, 7.5, 8.0 | new |
| `pgp_pangenome_ecology` | 10.0, 9.5, 8.0, 8.0 | 10.0, 9.0, 6.5, 9.0 | one each |
| `discoveries` (digest, 802 claims) | 9.5, 9.0, 5.0, 4.0 | 3.0, 8.5, 6.0, 8.0 | new |
| `ibd_phage_targeting` (1,897 claims) | 4.0, 9.0, 4.0, 3.5 | 9.5, 9.0, 4.0, 7.0 | deployed |
| `plant_microbiome_ecotypes` (790 claims) | 3.0, 8.0, 4.0, 2.5 | 9.5, 9.0, 6.0, 8.5 | deployed |
| Mean of the 16 judgements | 8.12, 9.12, 6.88, 6.00 | 8.12, 8.94, 6.38, 8.19 | new 4, deployed 3 |

The first five rows are the second judging round; the three long sources are the third,
after their summaries were rewritten in parts. In the second round those three scored
4 to 5 on fidelity and 6 to 7 on coverage, because the summary was written from a
sample of 480 claims and patched in eight passes.

For concept and entity pages, judged against the full text of the reports they cite:
the new pages scored 8.75 on fidelity with 4 of 495 statements unsupported (16 pages),
the deployed pages 6.67 with 16 of 112 unsupported (9 pages). In both wikis every
number in a cited statement is found in the report it cites, 100% in the new pages and
99.7 to 100% in the deployed ones.

**What the pilots show.**

- For a report of up to 180 claims the new summary is as faithful as the deployed one
  and easier to read, and it says less about what the results mean together.
- A long report with several phases is the weak case. The summary written in parts
  carries the report's content (coverage 8 to 9) and each number is in the report, but
  it is about as long as the report, repeats a result in each place the report repeats
  it, and in the plant report states five results as current that a later phase of the
  same report replaced. A part is written from its own claims and does not know what a
  later part revises. Giving each part the report's own conclusions as context was
  tried and judged: fidelity moved from 3.0 to 4.0 on one report and not at all on the
  other, one section invented a revision the report does not make, and 14 of 136
  writers answered in text without submitting the page. It was taken out again.
- Concept and entity pages hold fewer unsupported statements than the deployed ones,
  and relate evidence across reports about as well.

**Defects the pilots found, all fixed before the full compile.**

- A vendor's "429 Too Many Requests" was treated as a spent allowance and waited on
  for 15 minutes at a time; pilot 1 stood still for 80 minutes. Bursts are now asked
  again after a minute and each model's session limit adapts.
- The entity page list was refused twice at 33,000 output tokens. The list now holds
  only merges and renames, and unfaulted merges survive a refusal.
- Three summaries were refused because the writer left claims out on every attempt.
  The third attempt now takes a page whose statements all pass and records what it
  left out.
- A long-running process imported a module that had changed on disk since it started
  and crashed. Long runs now start from a copy of the source.
- The merge of a short last part into the one before it dropped a part and wrote the
  last one twice. Found by reading a page, fixed, and covered by a test.
- An expired Claude login failed 12 sessions before the page breaker stopped the run.
  The first "Not logged in" now stops it.

## Not built yet

- Regrouping topics across the whole corpus, and rewriting a hub's prose when its
  membership changes. Membership only grows here; hub prose changes as a section edit.
- Re-judging a literature label because it is old.
- A command that fills in one missing record. A record a reviewer refused twice stays
  missing until its report is revised.
- A run on the real `wiki/`. Every run so far used a scratch copy.
- Switching the nightly job. The curator's runtime is not deleted.
- API-key mode has not been run. The `gpt-6.2-sol` path was probed once.
- A report replaced while its first `ingest` was unfinished: the older run is closed,
  but claims it had already recorded from the older text are not re-checked.
- A sign is not part of a figure: a claim that turns `-0.42` into `0.42` passes the
  quote check.
