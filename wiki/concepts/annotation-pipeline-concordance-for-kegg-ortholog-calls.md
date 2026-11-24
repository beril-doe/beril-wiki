---
type: "Concept"
description: "How consistent KO assignments are between different annotation pipelines (Genome Depot versus eggNOG-mapper versus bakta) and how that limits cross-cohort comparisons."
sources: ["summaries/oak_ridge_cultivation_gap__REPORT.md"]
---
# Annotation pipeline concordance for KEGG ortholog calls

This page covers annotation pipeline concordance for KEGG ortholog (KO) calls. Pooled across genomes, Genome Depot and eggNOG-mapper agree well on KOs, but per-genome agreement is much lower. [src: oak_ridge_cultivation_gap] The evidence comes from one report, [[summaries/oak_ridge_cultivation_gap__REPORT]], which compared the two pipelines on 147 ENIGMA cultured genomes. [src: oak_ridge_cultivation_gap] It did not compare Genome Depot with bakta directly. [src: oak_ridge_cultivation_gap]

## Pipelines in the cultured–MAG comparison

The two cohorts were annotated by different tools. Cultured genomes were annotated by the ENIGMA Genome Depot pipeline, whose tool version is unknown. MAG (metagenome assembled genome) KOs came from bakta through `kbase_ke_pangenome.bakta_db_xrefs`. [src: oak_ridge_cultivation_gap] The report warns that systematic sensitivity differences between pipelines could bias the cultured–MAG comparison. It considers KO-level comparison more robust than pathway-level comparison. [src: oak_ridge_cultivation_gap] See [[entities/kbase-ke-pangenome]] and [[entities/enigma]].

## Cross-validation of Genome Depot against eggNOG-mapper

The report compared Genome Depot KO calls with the pangenome's eggNOG-mapper annotations. It used 147 ENIGMA cultured genomes matched by GCF/GCA accessions. These came from 153 ENIGMA records, which map to 147 unique pangenome genomes. [src: oak_ridge_cultivation_gap] See also [[entities/eggnog-orthologous-groups]].

Pooled across the 147 genomes, the pipelines agree on 5,751 KOs. There are 1,505 Depot-only and 148 eggNOG-only assignments, and the pooled-set Jaccard similarity is 0.777. [src: oak_ridge_cultivation_gap]

Per-genome agreement is much lower. Per-genome Jaccard similarity has a median of 0.140 and an IQR of 0.057–0.400. [src: oak_ridge_cultivation_gap] The report attributes this to eggNOG calling a narrower KO set per genome. It gives typical sizes of ~1,000–1,800 KOs for eggNOG and ~1,500–2,200 for the Depot, which inflates the per-genome union denominator. [src: oak_ridge_cultivation_gap]

## Interpretation and limits

The report reads the strong pooled agreement as support for using Genome Depot KOs as a reliable reference for cultivation-coverage analysis. [src: oak_ridge_cultivation_gap] It reads the per-genome gap as consistent with documented pipeline sensitivity differences, not systematic disagreement about which functions are present. [src: oak_ridge_cultivation_gap] This is the report's interpretation, not a direct test.

For cross-cohort work, the validation covers only Genome Depot versus eggNOG-mapper in cultured genomes. Bakta-derived MAG calls were not cross-checked in this comparison. [src: oak_ridge_cultivation_gap] Per-genome comparisons are sensitive to pipeline breadth. [src: oak_ridge_cultivation_gap] Related issues are in [[concepts/annotation-source-disagreement-and-coverage]].

## Open Directions

- Run Genome Depot, eggNOG-mapper and bakta on the same genomes, to measure bakta concordance directly. That would close the gap left by the Depot-versus-eggNOG comparison.
- Recompute per-genome concordance with a metric that does not depend on union size, such as recall of Depot KOs by eggNOG. This would test whether the low median Jaccard reflects breadth only.
- Repeat the cultured–MAG comparison after restricting both cohorts to KOs called by both pipelines. This would show how much of the result depends on pipeline sensitivity.
- Characterise the 1,505 Depot-only KOs by pathway. This would show whether the sensitivity differences concentrate in particular functions.
