# Parity Report — first-party compiler vs OpenKB reference

**Date**: 2026-09-01 · **Model**: `openai/claude-sonnet-5` via CBORG ·
**Spend**: est **$5.07** (685,578 in / 200,601 out tokens at Sonnet list price;
the budget tripwire stopped the run at the $5 cap) · **Verdict: architecture
validated, run incomplete — see recommendation.**

## Protocol

Per DESIGN.md: the three held-out projects (`metal_specificity`,
`bacdive_phenotype_metal_tolerance`, `prophage_amr_comobilization`) were
compiled INTO a copy of the reference corpus (`parity/ours`), with their
summary pages removed and all other docs pre-marked done. `parity/ref` is the
pristine benchmark. Artifacts: `parity/`, `parity_run.log`,
`parity/wiki_check.{ours,ref}.txt`. Reproduce with
`uv run python pipeline/parity_run.py`.

## Results

| Criterion | Reference | Ours | Verdict |
|---|---|---|---|
| `wiki_check` errors | 0 | 0 | ✅ pass |
| `wiki_check` warnings | 28 | 28 — **byte-identical warning set** (our pages added zero) | ✅ pass (≤ reference required) |
| Citation / number fidelity | post-hoc audit only | enforced at write time; validator flagged 8 pages pre-publication, retry fixed 4, rejected the rest instead of publishing them | ✅ pass — this is the designed upgrade over OpenKB working |
| Extend-vs-duplicate | — | **0 new concept pages** across all three docs; every concept touch was an update. 5 new entity pages (see caveats) | ✅ pass |
| Merge quality (side-by-side read) | — | Existing claims/numbers preserved, typed relations in prose (**supports/refines/echoes**), a genuine `## Tensions` section that refuses to average, Open Directions extended with data+method+question entries | ✅ pass, one caveat below |
| Integration completeness | 3/3 docs | 1/3 full, 2/3 partial — 13 merge-rewrites lost to the 8192-token output cap | ❌ incomplete |

**Placement agreement.** The planner independently targeted the same hub pages
the reference chose for these projects (`phylogenetic-confounding`,
`method-concordance`, `core-accessory-resistance`, `pangenome-integration`,
`mobile-genetic-elements`, `horizontal-gene-transfer`) — the lost merges are
cap casualties, not planning misses. The showcase merge that did land
(`concepts/environmental-metal-tolerance`, integrating
`bacdive_phenotype_metal_tolerance`) reads at or above reference quality:
it distinguishes the two BacDive linkage studies' coverage figures explicitly
instead of reconciling them, and records a cited two-sided tension.

## What went wrong (and is already fixed in code, unspent)

1. **8192-token output cap truncated full-page merge-rewrites** of the
   corpus's longest concept pages (8–10k tokens each). The fail-safe held —
   truncated pages were rejected, old versions kept, nonzero exit — but 13
   attempts burned ~$2.3 of the budget for nothing and the cap tripped
   mid-third-doc. Fixed: `MAX_TOKENS = 16384` (commit `70a08ad`).
2. **Docs with rejected pages were marked done**, so a re-run would have
   skipped their lost merges. Fixed: a doc now stays dirty until all its pages
   land (same commit).
3. **Entity pages missing an H1 title** (prompt omission). Fixed
   (commit `f2ee990`).

## Caveats worth a human eye

- **One number lost in one merge**: `25,089` (linked strains with
  isolation-source metadata) was dropped from
  `concepts/environmental-metal-tolerance.md` during section reorganization,
  despite the preserve-all instruction. ~30 other numbers on that page
  survived exactly. If this matters, the merge prompt could gain an explicit
  post-merge number-diff check (code, not prompt) — not built yet.
- **Finer entity grain than the reference**: the plan paged each studied metal
  (`copper`, `cobalt`, `nickel`, `zinc`) as `compound` entities where the
  reference paged only `iron`. The contract explicitly classes metals as
  compound entities, so this follows the rulebook more literally than OpenKB
  did — but it is a sharding tendency to watch at full-corpus scale.
- **One page legitimately rejected by the validator** (`entities/yebc`): the
  retry could not fix a citation-format violation, so the page was not
  created. Correct behavior; the evidence still lives in the summary.

## Per-doc status

| Doc | Summary | Plan | Pages written | Pages lost to cap |
|---|---|---|---|---|
| `bacdive_phenotype_metal_tolerance` | ✅ | ✅ | env-metal-tolerance, bacdive, azospirillum-brasilense | phylogenetic-confounding, metal-resistance-breadth, method-concordance, metal-fitness-atlas, gtdb |
| `metal_specificity` | ✅ | ✅ | gene-co-inheritance, metal-fitness-atlas, iron, ucp030820, copper, cobalt, zinc, nickel | condition-dependent-essentiality, core-accessory-resistance, env-metal-tolerance, annotation-gap, method-concordance, fitness-browser (+yebc rejected by validator) |
| `prophage_amr_comobilization` | ✅ | ✅ | (none) | mobile-genetic-elements, core-accessory-resistance; phylogenetic-amr-structure aborted at budget cap |

## Recommendation — needs your go/no-go (price-tagged)

The compiler architecture is sound: identical wiki_check profile to the
reference, correct extend-don't-duplicate behavior, and write-time validation
demonstrably catching what OpenKB only warned about after the fact. What's
missing is a clean completeness demonstration with the fixed 16k cap.

**Option A (recommended): fresh parity re-run** with the fixed compiler —
clean protocol, no double-merge risk, directly comparable. Est. **~$6**
(needs the cap raised, suggest `COMPILE_BUDGET_USD=8`):
`rm -rf parity && COMPILE_BUDGET_USD=8 uv run python pipeline/parity_run.py`

**Option B: accept parity on current evidence** and spend nothing more now;
the completeness fix gets proven implicitly on the first real incremental run.

**Not started, per the house rules**: the full 73-doc rebuild
(est. **$40–60** at the observed ~$1.5–2/doc — noticeably above the DESIGN.md
$5–10 guess, driven by long-page merge-rewrites; gpt-5.6-luna for the bulk
backfill would cut this ~10x at known quality cost). Awaiting an explicit
go-ahead on any of the above.
