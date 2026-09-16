---
type: "Concept"
description: "Interactive notebook kernels are an unreliable container for long-running analyses, so long jobs need explicit timeouts, detached script execution and on-disk checkpointing."
sources: ["summaries/pitfalls.md"]
---
# Long-Running Analyses Outlive the Interactive Sessions That Launch Them

The corpus's central pitfalls digest reports a recurring operational pattern: analyses that run longer than an interactive session tolerates can be lost. The losses are often silent. The reported remedies all move the long job out of the interactive kernel or make its progress recoverable from disk [src: pitfalls]. This evidence is an operational report from a single cross-project digest, not a measured benchmark. The specific thresholds below should be read as observed behaviour of one environment, not fixed platform guarantees [src: pitfalls].

## The Failure Mode

In the KBase Data Lakehouse JupyterHub environment, kernels that have received no user activity for ~17–25 minutes can be idle-timed out [src: pitfalls]. Long-running notebook cells were silently killed mid-execution. These were Spark jobs that take 30+ min, such as NB10 KO atlas construction or NB10b M22 attribution at 17M events. Spark is the distributed query engine behind the lakehouse. The kernel disappeared with no error message [src: pitfalls]. Because no error appears, a killed run can look abandoned rather than failed. This **supports** the broader corpus concern with failures that produce no signal (see [[concepts/silent-failure-modes-in-distributed-queries]]) [src: pitfalls].

Headless execution through `nbconvert` has its own limit. The kernel spawned by `nbconvert` has `get_spark_session()` available, but long-running notebooks may time out, so `--ExecutePreprocessor.timeout` must be set appropriately [src: pitfalls]. The digest does not say whether `nbconvert` kernels are also subject to the JupyterHub idle termination described above. Whether headless notebook execution avoids that failure mode is therefore an untested hypothesis, not an established finding [src: pitfalls].

## Reported Workarounds

The digest's workaround pattern for the idle-timeout problem includes the following steps [src: pitfalls]:
1. Convert the long-running notebook to a standalone `.py` script, for example `jupytext --to py 10_p2_ko_atlas.ipynb` [src: pitfalls].
2. Run it via `nohup python3 -u <script>.py > /tmp/<name>.log 2>&1 &` from a terminal. The digest explicitly says not to run it from a JupyterHub kernel [src: pitfalls].
3. Write intermediate Parquet files (a columnar on-disk table format) at each stage, so that partial results are recoverable from disk [src: pitfalls].
4. Provide `_finalize.py` recovery scripts that load the intermediates and complete the work from where the killed run stopped. The NB10 atlas construction needed `10_finalize.py` and `10_finalize2.py`, and the NB10b M22 attribution needed `10b_finalize.py` [src: pitfalls].

A complementary design tip covers long pipelines in general: build notebooks with checkpointing, meaning they save intermediate files and skip steps that already have output. This lets a pipeline be re-run after an interruption without repeating completed work [src: pitfalls]. The tip and steps 3–4 above support a narrower claim than uninterrupted execution. Durable intermediate state makes partial results recoverable and avoids redoing completed stages. It does not guarantee that a long run will finish [src: pitfalls]. This connects to the corpus's emphasis on recoverable, inspectable outputs (see [[concepts/analysis-provenance-and-reproducible-outputs]]) [src: pitfalls].

## Interpretation

Taken together, these reports suggest the hypothesis that interactive notebook kernels should be treated as a launching surface rather than an execution container for jobs whose runtime approaches or exceeds session idle limits [src: pitfalls]. The evidence comes from one digest and named cases rather than a systematic test of timeout behaviour. The claim is therefore best graded as well-documented practice rather than a quantified finding [src: pitfalls]. Related runtime constraints on large analyses are discussed in [[concepts/runtime-budgeted-resampling-and-embedding]] and [[concepts/execution-environment-dependent-access-paths]].

## Open Directions

- Run a controlled idle-timeout test in the JupyterHub environment. It would log kernel liveness for cells of increasing duration, with and without user activity, to pin down the reported ~17–25 minute range and whether it varies by configuration [src: pitfalls].
- Audit existing long-running project notebooks for stage-level checkpoint files and `_finalize.py`-style recovery scripts. This would identify which pipelines cannot currently resume after a silent kernel loss [src: pitfalls].
- Compare `nbconvert` runs that set an explicit `--ExecutePreprocessor.timeout` against `nohup` script runs for the same long Spark job. This would test whether headless notebook execution avoids idle termination and can substitute for the terminal-script workaround [src: pitfalls].
