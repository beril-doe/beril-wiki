---
title: Core-Gene Enrichment vs. Burden and Neutrality — What Does Missing Perturbation
  Coverage Mean?
type: Conflict
sources:
- id: adp1_deletion_phenotypes
  resource: ../../wiki/summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: core_gene_tradeoffs
  resource: ../../wiki/summaries/core_gene_tradeoffs__REPORT.md
  title: core gene tradeoffs
- id: fitness_effects_conservation
  resource: ../../wiki/summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: costly_dispensable_genes
  resource: ../../wiki/summaries/costly_dispensable_genes__REPORT.md
  title: costly dispensable genes
---
<!-- tension-hash: 213388fd2f328aad -->
# Core-Gene Enrichment vs. Burden and Neutrality — What Does Missing Perturbation Coverage Mean?

The disagreement concerns how to interpret the association between perturbation coverage, annotation, and pangenome-core status. One body of evidence finds successful coverage enriched among core genes, while related analyses show that core genes can carry substantial laboratory burden and that singleton genes may appear near-neutral under tested conditions. The tension matters because collection coverage and measured fitness effects may reflect biological conservation, technical construction or measurement difficulty, annotation errors, or combinations of these factors rather than a single evolutionary mechanism.

## Evidence Sides

**Coverage is enriched among core genes, but the mechanism is unresolved.** The observed association between perturbation coverage, annotation, and pangenome-core status could reflect biological conservation, technical difficulty in constructing or measuring mutants, misclassified gene fragments, or some combination of these factors. The report does not establish which mechanism causes the missing-data pattern, so the association should not be interpreted as proof that evolutionary conservation directly determines deletion-mutant recovery. [^adp1_deletion_phenotypes] This evidence is discussed on [genetic-perturbation-coverage-bias](../../wiki/concepts/genetic-perturbation-coverage-bias.md).

**Core genes can still impose laboratory burden and condition-specific costs.** The ADP1 collection indicates that successful coverage is enriched among core genes, whereas the broader trade-off analysis shows that core genes can carry substantial laboratory burden and condition-specific costs. This is not a direct contradiction because the studies measure different outcomes, but it creates a boundary on interpretation: core enrichment in a collection cannot by itself establish either low burden or universal essentiality. [^adp1_deletion_phenotypes][^core_gene_tradeoffs] The relevant trade-off framing appears on [genetic-perturbation-coverage-bias](../../wiki/concepts/genetic-perturbation-coverage-bias.md).

**Singleton near-neutrality may be biological or technical.** The Fitness Browser result that singleton genes were near-neutral under tested conditions creates a related interpretive tension: neutrality may represent genuine lack of measured effect or inadequate transposon coverage, and the analysis does not distinguish these explanations. [^fitness_effects_conservation] This issue is also recorded on [genetic-perturbation-coverage-bias](../../wiki/concepts/genetic-perturbation-coverage-bias.md).

**Costly, poorly conserved genes may be mobile-element-rich, but absence from collections is not established.** The costly–dispensable analysis classified burden using max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and the result is sensitive to fitness-data noise; its 90% identity DIAMOND threshold may also miss recently acquired genes with low sequence similarity. [^costly_dispensable_genes] Thus, mobile-element enrichment and poor annotation narrow the biological interpretation of costly non-conserved genes toward horizontally acquired DNA, but do not establish that such genes are systematically absent from perturbation collections. [^costly_dispensable_genes]

## Possible Reconciliations

- **Hypothesis — outcome differences:** successful mutant recovery, laboratory burden, condition-specific fitness cost, and near-neutrality measure different outcomes, so the apparent conflict may be only partial.
- **Hypothesis — technical missingness:** difficult mutant construction, inadequate transposon coverage, misclassified gene fragments, or poor annotation could produce both coverage gaps and apparently neutral or non-conserved categories.
- **Hypothesis — conditional biology:** core genes may be easier to recover overall while still imposing substantial costs in particular laboratory conditions.
- **Hypothesis — classification sensitivity:** max_fit > 1 in any experiment and the 90% identity DIAMOND threshold may amplify or obscure associations through noise and missed sequence similarity.

## Resolving Work

- Compare successful deletion recovery, transposon insertion density, annotation quality, and pangenome-core status in the same genes; test whether technical variables explain the coverage association after controlling for core status.
- Re-measure singleton and core-gene fitness across multiple conditions with matched transposon coverage; ask whether near-neutrality persists when inadequate coverage is excluded.
- Reanalyze costly-gene classifications using replicate-aware fitness estimates rather than max_fit > 1 in any experiment; test whether the core/non-core pattern survives measurement-noise correction.
- Repeat homology classification with thresholds below and above the 90% identity DIAMOND threshold and with gene-family or synteny evidence; ask whether recently acquired genes change the inferred mobile-element enrichment.
- Jointly model recovery probability, fitness burden, annotation confidence, and sequence conservation; test whether any single mechanism accounts for the missing-data pattern.

[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../../wiki/summaries/adp1_deletion_phenotypes__REPORT.md)
[^core_gene_tradeoffs]: [core gene tradeoffs](../../wiki/summaries/core_gene_tradeoffs__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../../wiki/summaries/fitness_effects_conservation__REPORT.md)
[^costly_dispensable_genes]: [costly dispensable genes](../../wiki/summaries/costly_dispensable_genes__REPORT.md)
