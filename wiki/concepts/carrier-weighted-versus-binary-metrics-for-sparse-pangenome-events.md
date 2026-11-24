---
type: "Concept"
description: "Choice of metric for rare multi-copy events in pangenome data, comparing binary any-multi-copy flags to cluster-carrier-weighted rates and their effect on detected effect sizes."
sources: ["summaries/gene_copy_number_variation__REPORT.md"]
---
# Carrier-weighted versus binary metrics for sparse pangenome events

The choice between a binary any-multi-copy flag and a cluster-carrier-weighted rate changed the detected effect size several-fold in one bacterial pangenome project (gene_copy_number_variation). The evidence comes from a single report on one dataset, with its pilot and scaled analyses. The report's wider claim, that the principle extends to other sparse events, is a proposal and was not tested here. [src: gene_copy_number_variation] See also [[summaries/gene_copy_number_variation__REPORT]] and [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

## Metric definitions

The binary metric flags a gene cluster if it is multi-copy in at least one genome. [src: gene_copy_number_variation] The weighted metric is the cluster-carrier-weighted multi-copy rate, SUM(multicopy) / SUM(carriers). [src: gene_copy_number_variation] The report describes it as SUM(multicopy_genomes) / SUM(carrier_genomes), and calls it robust to the sparse, rare-event nature of paralog expansion in bacterial pangenomes. [src: gene_copy_number_variation]

## Effect on detected effect size

The same data gave a 1.4× effect with the binary flag in pilot NB01 (cell 15). The weighted rate gave 3.3× in NB01b (cell 9) and 8.1× at scale in NB03 (cell 6). [src: gene_copy_number_variation] In the pilot, the binary metric showed the expected direction in 5/5 species but a weak effect, and this triggered a plan revision. [src: gene_copy_number_variation] The report says binary flags underestimate the class effect by ~6× at pilot scale. [src: gene_copy_number_variation]

NB01b switched to the weighted rate. It also refined the functional category split: F and H as housekeeping, L, V, M and K as adaptive, and C and J as mixed and tracked separately. [src: gene_copy_number_variation] Two changes were made together, so the 3.3× result reflects both the metric and the category split. The refined pilot gave a pooled ratio of 3.3× and a [[entities/mann-whitney-u-test|Mann-Whitney]] test on cluster CVs (cross-validation) of p = 1.6 × 10⁻⁷. It passed all 4 pre-registered gates. [src: gene_copy_number_variation] Categories are described in [[entities/clusters-of-orthologous-groups-functional-categories]].

## Why the binary flag fails

The report warns that the binary flag is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation] Weighting by carriers keeps such clusters from outweighing clusters where multi-copy status recurs across carrier genomes. This is an interpretation of the caveat, not a separate measurement.

## Proposed general rule

The report proposes that any binary presence/absence flag whose biological signal lies in degree, not just presence, should be replaced by a carrier-weighted rate when the target event is sparse. [src: gene_copy_number_variation]

## Open Directions

- Re-run the pilot with the binary flag and the weighted rate under the same category split. This would separate the metric's effect from the category refinement's effect.
- Apply carrier-weighted rates to another sparse pangenome event, such as rare gene gains, to test whether the principle generalises beyond copy number.
- Compare binary and weighted effect sizes across increasing genome counts. This would show whether the 1.4×, 3.3× and 8.1× progression comes from scale or from the metric.
- Test sensitivity to a minimum-carrier threshold on clusters, to quantify how much the rare accidental clusters drive the binary result.
