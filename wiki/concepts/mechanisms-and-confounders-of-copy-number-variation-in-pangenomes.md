---
type: "Concept"
description: "Alternative explanations (transposase-driven expansion, dosage selection, neutral tolerance) and technical caveats (paralog clustering threshold, assembly quality, sampling) for observed multi-copy rates; stops at proposed tests."
sources: ["summaries/gene_copy_number_variation__REPORT.md"]
---
# Mechanisms and confounders of copy-number variation in pangenomes

This page covers alternative explanations and technical caveats for observed multi-copy rates in bacterial pangenomes, and it stops at proposed tests. Adaptive COGs (clusters of orthologous groups), especially L (repair/mobile) with species-level median 1.12%, showed 20–30× the housekeeping multi-copy rate. [src: gene_copy_number_variation] The report did not test any mechanism directly, so the explanations below are interpretive. See [[summaries/gene_copy_number_variation__REPORT]] and [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

## Alternative explanations

- COG L contains transposases, integrases and IS elements, which the report says are known to expand in bacterial pangenomes. [src: gene_copy_number_variation] See [[entities/cog-category-l-replication-recombination-and-repair]] and [[entities/insertion-sequence-elements]].
- The report reads its L-dominance and adaptive-accessory enrichment as consistent with the same transposable-element expansion mechanism operating across the bacterial tree of life. [src: gene_copy_number_variation]
- Sotiropoulos et al. 2026 reported high levels of TE insertion driving accessory-gene copy-number variation in wheat pathogens. [src: gene_copy_number_variation]
- If the effect concentrates in IS elements, the story becomes transposition-mediated CNV rather than adaptive paralogy, which matters for the dosage-balance interpretation. [src: gene_copy_number_variation]
- The report reads adaptive-accessory clusters being the primary site of copy-number variation as consistent with dosage-driven amplification of environmentally responsive genes. [src: gene_copy_number_variation]
- Elliott, Cuff & Neidle 2013 discussed positive selection for gene dosage in microbial genome amplification. [src: gene_copy_number_variation]
- The report does not test direct positive selection on copy number. Its observations fit purifying selection against dosage imbalance for housekeeping paralogs, neutral tolerance for adaptive paralogs plus positive selection on some of them, or mechanistic bias from adaptive genes sitting near mobile elements. [src: gene_copy_number_variation]
- Distinguishing these would require dN/dS on paralog pairs and mobile-element context data. [src: gene_copy_number_variation]

## Technical caveats

- The gene clusters come from motupan at 90% AAI. Recent paralogs diverged <10% merge into one cluster, and ancient paralogs diverged >10% appear as separate clusters, so counts capture operationally recognized paralogs only. [src: gene_copy_number_variation]
- Fragmented MAGs (metagenome assembled genomes) can split a paralog family across contigs, which inflates multi-copy counts, or merge it, which deflates them. Contig artifacts enter the metrics linearly. [src: gene_copy_number_variation] See also [[concepts/genome-type-and-sampling-bias-in-metagenome-assembled-genome-surveys]].
- The report does not condition on checkm_completeness or contig N50, and says a robustness pass on the tightest-quality genome subset would strengthen the claim. [src: gene_copy_number_variation]
- Borreliella burgdorferi was retained but flagged as a multi-partite-genome outlier. Plasmid-borne duplication raises its housekeeping and adaptive rates together and breaks the direction test. [src: gene_copy_number_variation]
- The rate metric is between-genome. [src: gene_copy_number_variation] For scope limits, see [[concepts/sampling-scope-and-generalizability-of-pangenome-wide-tests]].

## Proposed tests

- The report proposes splitting COG L clusters into IS-element loci versus true DNA repair loci (recA, mutL, uvr*), using bakta_amr or genomad_mobile_elements cross-references if available in the current KBase Data Lakehouse migration state. [src: gene_copy_number_variation]
- The report proposes restricting to checkm_completeness ≥ 95 and checkm_contamination ≤ 2 and rerunning NB03 to see whether fragmented assemblies inflate the L effect. [src: gene_copy_number_variation]
- The report proposes using ~30 [[entities/fitness-browser]]–pangenome-linked species to ask whether paralog copy count correlates with fitness in relevant conditions for expanded clusters. [src: gene_copy_number_variation]
- This would connect the CNV story to the dosage-selection story discussed by Elliott, Cuff & Neidle 2013. [src: gene_copy_number_variation]

## Open Directions

- Split COG L into IS-element and true DNA repair loci to test whether the L signal is transposase-driven.
- Rerun NB03 on high-quality genomes (checkm_completeness ≥ 95, checkm_contamination ≤ 2) to test assembly inflation.
- In species with 200+ high-quality genomes, compare copy-count distributions conditional on cluster presence between adaptive and housekeeping clusters, to look for heavier tails.
- Correlate paralog copy count with fitness across the ~30 Fitness Browser-linked species.
- Compute dN/dS on paralog pairs with mobile-element context to separate purifying selection, neutral tolerance and mechanistic bias.
