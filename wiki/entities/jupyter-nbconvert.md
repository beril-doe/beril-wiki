---
type: "Method"
description: "Headless notebook execution tool used for long pipelines, with timeout and in-place output-loss caveats."
sources: ["summaries/discoveries.md", "summaries/ecotype_functional_differentiation__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md", "summaries/pitfalls.md"]
aliases: ["nbconvert"]
---
# jupyter nbconvert

This page covers jupyter nbconvert (also called nbconvert), the headless notebook execution tool used for long pipelines. Notebooks can be executed headlessly with it, and the kernel it spawns has `get_spark_session()` available. [src: pitfalls] The evidence comes from project reports and the pitfalls digest. It documents separate failure modes: silent death of a long background run, kernel death on large `toPandas()` results, and output loss with `--inplace`. [src: gene_copy_number_variation, discoveries, pitfalls]

## Key facts

The documented command is `jupyter nbconvert --to notebook --execute notebook.ipynb --output notebook_executed.ipynb --ExecutePreprocessor.timeout=7200`. [src: pitfalls]

## Failure modes

- **Timeouts.** Long-running notebooks may time out, so `--ExecutePreprocessor.timeout` must be set appropriately. [src: pitfalls] For presence-matrix extraction, the report recommends `ExecutePreprocessor.timeout=3600`. [src: pitfalls]
- **Silent death.** During bacterial pangenome extraction, a background nbconvert run of the long Spark loop died silently after ~1.5 hr. The notebook file was unchanged and only the intermediate CSV had been written. [src: gene_copy_number_variation]
- **Dead kernels.** Running `jupyter nbconvert --execute` on notebooks that call `spark.sql(...).toPandas()` on large result sets kills the kernel with a DeadKernelError. [src: discoveries]

### Output loss with --inplace

The genome_depot_enigma project reports that on its JupyterHub, `jupyter nbconvert --to notebook --execute --inplace ...` can exit with code 0 yet leave the notebook on disk with zero cell outputs. The kernel runs the cells successfully, but the outputs are never written back. [src: pitfalls] Even with `--allow-errors`, outputs may still not be persisted. [src: pitfalls] This is particularly problematic when a pre-flight cell raises an intentional `RuntimeError` (the `CONFIRMED = False` pattern used by `/berdl-ingest`), because the plan output meant for inspection is lost. [src: pitfalls]

## Workarounds

- Do not rely on `--inplace`. Write to a separate file with `--output`. For long production ingests, run the equivalent logic as a standalone Python script that streams stdout and stderr to a log file. [src: pitfalls]
- Add cache-check logic to Spark cells: load the CSV if the path exists, otherwise run Spark. nbconvert can then run the notebook locally from cached CSVs after the initial JupyterHub run. Capture the live Spark outputs interactively on JupyterHub, not through nbconvert. [src: discoveries]

## Use in projects

- In ecotype_functional_differentiation, `src/run_clustering.py` is a standalone Spark-query script for ecotype clustering and COG (clusters of orthologous groups) profiling. It runs outside nbconvert because of long execution times. [src: ecotype_functional_differentiation] See [[summaries/ecotype_functional_differentiation__REPORT]].
- In gene_copy_number_variation, `src/extract_multi_species.py` is a resumable standalone Python script for per-species Spark extraction. It replaces the fragile `nbconvert --execute` path used in the initial NB02 attempt. [src: gene_copy_number_variation] See [[summaries/gene_copy_number_variation__REPORT]] and [[entities/spark-extraction-of-per-species-pangenome-copy-counts]].

Related: [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]], [[summaries/pitfalls]], [[summaries/discoveries]].
