---
type: "Concept"
description: "How species selection, phylum coverage and functional-class coverage limit extrapolation of pangenome-wide copy-number results."
sources: ["summaries/gene_copy_number_variation__REPORT.md"]
---
# Sampling scope and generalizability of pangenome-wide tests

This page covers how species selection, phylum coverage and functional-class coverage limit extrapolation of pangenome-wide copy-number results. All the evidence comes from the caveats of one report, [[summaries/gene_copy_number_variation__REPORT]]. Its tested effect is real for the rows it tested, but the report itself says the reach to all bacteria is limited. [src: gene_copy_number_variation]

## Species and phylum scope

The report selected 24 bacterial species for 50–300-genome coverage. This oversamples clinically important and well-studied taxa. [src: gene_copy_number_variation]

The five phyla covered are Pseudomonadota, Bacillota, Bacteroidota, Actinomycetota and Campylobacterota. They are the top 5 by candidate count. This coverage set leaves out CPR (candidate phyla radiation), Patescibacteria, Spirochaetota and archaea. [src: gene_copy_number_variation]

Spirochaetota has one exception to that exclusion. The pilot species *Borreliella burgdorferi* was retained but flagged as a multi-partite-genome outlier. Plasmid-borne duplication in this species affects housekeeping and adaptive categories together, which raises the housekeeping rate and breaks the direction test. [src: gene_copy_number_variation]

## Functional-class coverage

The coarse partition covers little of the data. Housekeeping = {F, H} covers ~5% of species-level rows, and adaptive = {L, V, M, K} covers ~15%. [src: gene_copy_number_variation] Roughly 80% of clusters fall into "other" (poorly annotated, mixed or intermediate function) and are excluded from the primary test. The class effect is real for the tested rows, but extrapolating to "all bacterial genes" is not automatic. [src: gene_copy_number_variation] The report gives the row percentages and the cluster percentage separately, so this page does not combine them into one tested fraction. [src: gene_copy_number_variation]

## Cluster definition and genome quality

The gene clusters come from motupan at 90% AAI. Recent paralogs diverged <10% merge into one cluster, so only their copy number is counted. Ancient paralogs diverged >10% appear as separate clusters, and their functional relatedness is lost. [src: gene_copy_number_variation] The counts therefore reflect operationally recognized paralogs, not phylogenetically complete ones. [src: gene_copy_number_variation]

The analysis does not condition on `checkm_completeness` or contig N50. The report says a robustness pass on the tightest-quality genome subset would strengthen the claim. [src: gene_copy_number_variation]

For related material, see [[concepts/mechanisms-and-confounders-of-copy-number-variation-in-pangenomes]], [[concepts/paralog-expansion-and-gene-copy-number-constraint]] and [[concepts/genome-type-and-sampling-bias-in-metagenome-assembled-genome-surveys]].

## Open Directions

- Repeat the copy-number test on the tightest-quality genome subset, filtered by checkm_completeness and contig N50. This would close the gap left by the missing quality conditioning. [src: gene_copy_number_variation]
- Add species from CPR, Patescibacteria, Spirochaetota and archaea, and test whether the direction of the class effect holds. This would address the phylum gap.
- Sample less-studied taxa alongside the clinically important ones, to check whether the species-selection bias changes the effect.
- Refine the functional partition so that some of the "other" clusters can be tested. This would show whether the effect extends beyond the classes now tested.
- Compare results at clustering thresholds other than 90% AAI. This would show how much the merging of recent paralogs shapes the counts.
