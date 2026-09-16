<!-- tension-hash: e503d1e436885118 -->
# Does pangenome conservation track fitness importance, or are the two decoupled?

> **Editorial note.** Text was removed here after scientific review (citation). The removed material and the objection are recorded in the run's salvage ledger.

## Evidence Sides

**Side A: AMR-specific decoupling (null result)**

**Side B: A modest genome-wide association between conservation and importance**

- Across a 33-organism integration, putative essential genes (called from an absence of transposon insertions) are 86.1% core versus 81.2% for non-essential genes, with a median odds ratio (the factor by which the odds of being core rise for essential genes) of 1.56. This is the same directional association with a smaller effect, and it does not resolve the tension [src: conservation_vs_fitness]. "Core" means present across nearly all sampled genomes of a species.
- The synthesis supports a modest genome-wide gradient but shows that core genes can be more burdensome in the laboratory, so conservation, essentiality and laboratory cost should not be treated as interchangeable [src: conservation_fitness_synthesis].
- Genes in independent component analysis (ICA) modules, statistically derived sets of genes with coordinated fitness profiles, are 86.0% core versus 81.5% of all genes. This is directionally consistent with enrichment of conserved, coordinated fitness units [src: module_conservation]. However, ICA modules exclude essential genes and summarize module membership rather than AMR baseline means, so this does not resolve the AMR-specific null [src: module_conservation].

## Possible Reconciliations

- *Hypothesis:* AMR biology differs. Resistance genes may be conditionally useful, so baseline fitness cost decouples from prevalence even though conservation and essentiality are associated genome-wide.
- *Hypothesis:* Averaging hides heterogeneity. A modest pooled gradient could coexist with null subsets such as AMR genes.
- *Hypothesis:* Differences in organism composition, essentiality definitions or pangenome sampling between projects produce the apparent disagreement.
- *Hypothesis:* Module-callability matters. Module analyses cannot include essential genes, so they test a different gene population than either the essentiality comparison or the AMR comparison.

Resolving the tension requires matched, condition-specific comparisons.

## Resolving Work

- Restrict the essential-versus-non-essential conservation comparison to the organisms used in the AMR analysis. Re-test the AMR null within that matched set to ask whether organism composition explains the difference.
- Stratify fitness-browser fitness effects by condition, separating antibiotic-relevant conditions from baseline. Compare AMR genes against non-AMR genes of matched conservation class, and ask whether the decoupling is specific to the condition.
- Reanalyze per gene rather than through averaged baseline means. Use per-organism odds ratios for AMR versus non-AMR genes to ask whether averaging masks a gradient within AMR genes.
- Apply a single shared essentiality definition and a single pangenome core threshold across all projects. Rerun both comparisons to ask whether definitional choices drive the disagreement.
- Compare AMR genes that are callable in ICA modules with those that are not. This would show whether module-callability selects a gene subset with a different conservation profile.
