---
type: "Method"
description: "Per-species Spark three-way join of gene, junction and cluster tables, run via a resumable standalone script rather than notebook execution."
sources: ["summaries/gene_copy_number_variation__REPORT.md", "summaries/pitfalls.md"]
aliases: ["extract_multi_species.py"]
---
# Spark extraction of per-species pangenome copy counts

`src/extract_multi_species.py` is a resumable standalone Python script. It runs a per-species Spark three-way join of gene, junction and cluster tables, and it replaced the fragile `nbconvert --execute` path used in the initial NB02 attempt of the gene copy number variation project. [src: gene_copy_number_variation]

## Key facts

- The script replaced the fragile `nbconvert --execute` path used in the initial NB02 attempt. [src: gene_copy_number_variation] See [[entities/jupyter-nbconvert]].
- NB02 used it to extract bacterial copy counts for 24 species × 5 phyla, with incremental per-species CSV output. [src: gene_copy_number_variation]
- The join is `gene × gene_genecluster_junction × gene_cluster`, with about 1B rows in each table. [src: gene_copy_number_variation]

## Why a script replaced the notebook

A background nbconvert run of the extraction loop died silently after ~1.5 hr. The notebook file was unchanged and only the intermediate CSV had been written. [src: gene_copy_number_variation]

The standalone script wrote per-species CSVs, so it could resume. It streamed progress via `print(flush=True)` and finished under the same wall-clock budget as the failed notebook execution. [src: gene_copy_number_variation]

The 24 species ran in two batches, 18 and then 6 after a background-task timeout. The resumable-skip logic made that interruption cost-free. [src: gene_copy_number_variation]

## Performance

The per-species join took 140–290 s on species with 50–250 genomes, with a median of ~200 s. [src: gene_copy_number_variation] The report puts the 24-species pilot at ~80 min total. [src: gene_copy_number_variation] It also says the pilot took ~80 min on JupyterHub. [src: gene_copy_number_variation]

The same digest recommends registering target cluster and genome IDs as temporary views and using BROADCAST hints on both filter tables. [src: pitfalls] See also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]] and [[summaries/pitfalls]].

## Scaling

The report recommends CTS batch processing, not a JupyterHub notebook loop, for 100+ species. [src: gene_copy_number_variation] Scaling to 100–200 species would give power for phylum-specific tests. It would also allow decomposing the Pseudomonadota versus Campylobacterota effect-size difference. [src: gene_copy_number_variation]
