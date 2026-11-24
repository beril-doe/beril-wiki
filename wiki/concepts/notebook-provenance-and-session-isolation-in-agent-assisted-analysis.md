---
type: "Concept"
description: "Covers how interactive agent sessions, shared git clones, in-place notebook execution and review workflows can leave results without reproducible code history; stops at data-access issues."
sources: ["summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Notebook provenance and session isolation in agent-assisted analysis

This page covers notebook provenance and session isolation in agent-assisted analysis. Interactive REPL work can leave committed results without committed producing code. [src: pitfalls] In-place notebook execution can lose outputs. [src: pitfalls] Concurrent sessions in a shared clone can remove files and redirect commits. [src: pitfalls] The evidence comes from the pitfalls digest. See also [[summaries/pitfalls]].

## Results without producing code

Interactive Claude Code REPL analyses can commit figures and data while the producing code lives only in the session transcript. The project then looks reproducible: the README, runtime tables and REPORT cite notebooks, but git log shows no history for them. [src: pitfalls] Downstream reviewers who take the plan and report at face value miss the gap. [src: pitfalls]

In genotype_to_phenotype_enigma, three notebooks existed only as outputs: NB08, NB09 and NB10, the entire Act II/III closing. [src: pitfalls] Reconstruction took a few hours once the gap was found. Writing `.ipynb` cells in the first place would have been far cheaper. [src: pitfalls] The report says this is especially easy late in a project, when the user is synthesizing and no longer creating fresh notebooks for each step. [src: pitfalls]

Recommended practice:
- Move figure-building logic from a REPL into a numbered notebook before saving results. [src: pitfalls]
- Before `/submit` or any milestone commit, run `git log --all --oneline -- projects/{project_id}/notebooks/NB*.ipynb`. This checks that every NBxx referenced in the README or plan has notebook history. [src: pitfalls]
- For an inherited project with the gap, reconstruct the notebooks from the committed artifacts. Record this in the RESEARCH_PLAN.md revision history, so reviewers can tell "interactive original" counts from "reproducible re-run" counts. [src: pitfalls]

### Empty or invalid notebooks

Prototyping as Python scripts can lead to notebooks committed with empty output cells, as in env_embedding_explorer. This defeats their role as audit trail and methods documentation. [src: pitfalls] The `/synthesize` skill reads notebook outputs to extract results. The `/submit` reviewer checks outputs to verify claims. Human readers use them to follow the analysis without rerunning it. Empty notebooks fail all three uses. [src: pitfalls] The fix is to execute notebooks before committing. Expensive steps such as UMAP (uniform manifold approximation and projection) should load cached results when they exist. [src: pitfalls]

Editing can also break notebooks. Replacing a code cell with NotebookEdit can produce a cell without the required `outputs` and `execution_count` fields. Then `jupyter nbconvert --execute` fails with `NotebookValidationError: 'outputs' is a required property`. [src: pitfalls] The suggested check fills missing code-cell `outputs` with an empty list and `execution_count` with None. [src: pitfalls]

Two further notebook-level errors are recorded:
- In metal_specificity, generic variable names such as `odds, p = stats.fisher_exact(table)` were reused across sequential tests. The second test overwrote the first, and a summary cell printed wrong values under wrong labels. [src: pitfalls] The fix is a descriptive variable name for each test. [src: pitfalls]
- In plant_microbiome_ecotypes, the NB04 genus-level logistic-regression cell called bare `logit(...)` although the import was `statsmodels.formula.api as smf`. The cell became a markdown reroute to NB14's cluster-robust generalized linear model (GLM), the canonical answer. The original code was kept verbatim for chronology. [src: plant_microbiome_ecotypes] See [[summaries/plant_microbiome_ecotypes__REPORT]].

## In-place execution that loses outputs

In genome_depot_enigma, `jupyter nbconvert --to notebook --execute --inplace` on JupyterHub could exit with code 0 yet leave zero cell outputs on disk. The kernel ran the cells, but the outputs were never written back. [src: pitfalls] This is a problem when a `/berdl-ingest` pre-flight cell raises an intentional `RuntimeError` (the `CONFIRMED = False` pattern), because the plan meant for inspection is lost. [src: pitfalls] Even `--allow-errors` may not persist outputs. [src: pitfalls] The recommended fix is to write to a separate file with `--output`. For long production ingests, run the logic as a standalone Python script with stdout and stderr logged. [src: pitfalls] See [[entities/jupyter-nbconvert]].

## Shared clones and concurrent sessions

Two agent sessions in one clone share a `.git` directory and working tree. A checkout in one session silently removes branch-specific files from the other's tree. Later commits land on whichever branch HEAD points at. [src: pitfalls]

On 2026-04-24, during ibd_phage_targeting NB00 work, a second `claude` process (PID 22230) ran `git checkout projects/plant_microbiome_ecotypes` during a long `nbconvert --execute` run. The first session's next commit landed on the plant-microbiome branch. The user saw README.md and RESEARCH_PLAN.md "missing" from the ibd project directory. [src: pitfalls] Both files were still safe in git on the ibd branch. [src: pitfalls] The report says a file that seems missing right after the agent believed it committed it is almost always a wrong-branch commit or background checkout, not a deletion. [src: pitfalls]

Mitigations in the report:
- Capture the intended branch at session start. Run `git branch --show-current` before every commit, and investigate if it differs. [src: pitfalls]
- To recover a wrong-branch commit, cherry-pick it onto the correct branch, then reset the stray branch with `git branch -f <stray> origin/<stray>`. No data is lost while the commit is recoverable via `git reflog`. [src: pitfalls]
- Use git worktrees. Each has its own HEAD and working-tree state but shares one object store, so a checkout in one does not affect another. [src: pitfalls]

## Review and synthesis workflows

Review and synthesis tooling adds further file-placement and reliability problems.

- In fitness_effects_conservation, the `/submit` reviewer subprocess may write REVIEW.md to `projects/{id}/projects/{id}/REVIEW.md`. This happens if it resolves the path relative to its own working directory rather than the repo root. [src: pitfalls]
- In cofitness_coinheritance, computed phi coefficients and summary tables went into `data/results/`. The BERIL pattern keeps data flat in `data/`, with subdirectories only for extracted data categories. [src: pitfalls]
- In the same project, `/synthesize` told the agent to put detailed findings in README.md. That conflicts with the observatory's three-file structure and makes the README too long. [src: pitfalls] The structure is README (concise overview with links), RESEARCH_PLAN (hypothesis and approach) and REPORT (full findings and interpretation). essential_genome is the canonical example. [src: pitfalls]
- The corrected workflow puts Key Findings, Results, Interpretation, Literature Context, Limitations, Future Directions, Visualizations and Data Files in REPORT.md. [src: pitfalls] README.md keeps a Status line, an Overview paragraph, Quick Links and project metadata. [src: pitfalls]

### Reviewer CLI reliability

Running `codex exec` in a restricted sandbox can fail with DNS or connection errors, such as `chatgpt.com` resolution failures, because network egress is disabled. [src: pitfalls] The fix is to run with network-enabled permissions and first try a smoke test, `codex exec "Reply with exactly: ok"`. [src: pitfalls] Long inline system prompts can make `codex exec` unstable or intermittently failing. [src: pitfalls] A compact prompt that points to an on-disk prompt file and writes to `projects/{id}/REVIEW.md` has been more reliable in BERIL submit workflows. [src: pitfalls] For review discipline more broadly, see [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## Open Directions

- Audit all projects with `git log --all -- projects/*/notebooks/NB*.ipynb` against the NB references in their READMEs and plans. This would show how common the missing-history gap is beyond genotype_to_phenotype_enigma.
- Add a pre-commit check that flags committed notebooks with empty outputs. This would catch both the script-prototyping and the `--inplace` loss cases.
- Compare notebook outputs before and after `--inplace` and `--output` runs on JupyterHub. This would show when `--inplace` drops outputs, since only one project reported it.
- Test whether per-session git worktrees remove the wrong-branch commits, by logging branch mismatches at commit time across concurrent sessions.
- Test the `/submit` reviewer with an absolute repo-root path. This would confirm whether it stops the nested REVIEW.md.
