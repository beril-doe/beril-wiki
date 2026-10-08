---
type: "Concept"
description: "What counts as a reproducible analysis record in this corpus: committed figures and data files are not enough without committed code history and retained execution outputs."
sources: ["summaries/pitfalls.md"]
---
A project can look reproducible while lacking the record that would let anyone rerun it. The central pitfalls digest documents two separate failures. In the first, outputs were committed while the code that produced them was not. In the second, the notebook executor reported success while saving no outputs. Both rest on single documented incidents rather than a corpus-wide audit, so their frequency across projects is not established [src: pitfalls]. Related execution-side failures are covered in [[concepts/long-running-analysis-execution-reliability]] and [[concepts/silent-failure-modes-in-distributed-queries]]. The digest itself is summarized in [[summaries/pitfalls]].

## Committed Outputs Without Committed Code

Analyses run interactively in a Claude Code session, as a pure Python REPL rather than a committed `.ipynb`, can produce figures and data files that get staged and committed while the generating code lives only in the session transcript [src: pitfalls]. The project then *looks* reproducible. The README references NB08/NB09/NB10, the runtime tables list them and the REPORT cites their findings, yet `git log` finds no notebook history for those names [src: pitfalls]. Downstream reviewers who read the plan and REPORT at face value miss the gap [src: pitfalls]. Committed artifacts and prose citations therefore do not establish provenance on their own [src: pitfalls].

The documented scale is a single project. Three "notebooks", NB08, NB09 and NB10, which made up the entire Act II/III closing, existed only as outputs [src: pitfalls]. Once the gap was identified, reconstruction took a few hours. The source notes it would have been far cheaper to write `.ipynb` cells in the first place [src: pitfalls].

## Executor Success Without Retained Outputs

On this JupyterHub, `jupyter nbconvert --to notebook --execute --inplace ...` can exit with code 0 but leave the notebook file on disk with **zero cell outputs** [src: pitfalls]. A successful exit status is therefore not evidence that an executed notebook records what it computed [src: pitfalls].

The source recommends not relying on `--inplace` to capture outputs. It gives two alternatives: write to a separate file via `--output`, or, for long-running production ingests, run the equivalent logic as a standalone Python script so that stdout/stderr stream to a log file [src: pitfalls].

## Synthesis: A Working Standard

Taken together, the two incidents suggest the hypothesis that a reproducible analysis record needs two things beyond committed artifacts. The first is version-controlled code history for every analysis the REPORT cites. The second is outputs saved by a method that is checked separately from the executor's exit status. The source documents each failure once and does not test this standard across projects [src: pitfalls]. The standard **refines** the reviewer-facing checks discussed in [[concepts/adversarial-research-quality-assurance]]: a review that reads only the plan and REPORT can miss missing notebook history [src: pitfalls].

## Open Directions

- Audit cited notebooks against git history. For every notebook name cited in project REPORTs and READMEs, check whether `git log` shows committed history. This would establish whether the outputs-only gap documented for NB08/NB09/NB10 is isolated or recurrent [src: pitfalls].
- Flag committed notebooks that lack outputs. Scan committed `.ipynb` files for notebooks that have execution metadata but zero cell outputs, and treat the hits only as candidates for investigation. The scan alone cannot show which executor or options were used, or why the outputs are missing. Attributing any case to the `--inplace` failure would need execution logs or a controlled rerun of that notebook [src: pitfalls].
- Compare the two recommended alternatives. Run the same notebooks with `--output` to a separate file and as logged standalone scripts. This would confirm that both alternatives retain outputs in this environment [src: pitfalls].
