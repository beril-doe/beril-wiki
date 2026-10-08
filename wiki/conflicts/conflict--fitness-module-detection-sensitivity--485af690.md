<!-- tension-hash: 485af690b3df249c -->
# Do Fitness-Defined Gene Sets Skew Toward the Conserved Core, or Is the Fitness–Conservation Link Weak?

Two projects relate fitness data to pangenome conservation and appear to disagree. The core fraction is the share of genes in the core genome, meaning genes present in nearly all genomes of a species. One project finds that genes in fitness modules are enriched for core genes. [src: module_conservation] The other finds only a weak association between fitness importance and conservation, and warns that measurement gaps may hide part of the signal. [src: fitness_effects_conservation] The answer matters for [[concepts/fitness-module-detection-sensitivity]]. If module membership tracks conservation, then module detection could be partly shaped by which genes the method is able to measure, and not only by biology.

## Evidence Sides

**Module genes are enriched in the core genome**

The module-conservation analysis found an 86.0% core fraction for module genes, against 81.5% for all genes. [src: module_conservation] Modules here come from independent component analysis (ICA), a statistical decomposition that groups genes with coordinated fitness patterns across experiments. [src: module_conservation] The estimate depends on three conditions: genes must be detected, they must be non-essential module members, and the result holds only under the selected module thresholds. [src: module_conservation]

**Fitness importance is only weakly associated with conservation**

The genome-wide fitness-conservation analysis found only a weak association between fitness importance and conservation. [src: fitness_effects_conservation] It spans broader fitness categories and approximately 194,000 genes. [src: fitness_effects_conservation] It also cautions that novel singleton genes may appear neutral because of poor transposon coverage. Singleton genes are genes found in a single genome. Transposon coverage refers to how many mutant insertions land in a gene. [src: fitness_effects_conservation]

## Possible Reconciliations

- *Hypothesis:* The two results measure different estimands, meaning different quantities being estimated, and so need not conflict. One is conditional on detected, non-essential module members and chosen thresholds. The other spans broader fitness categories. [src: module_conservation] [src: fitness_effects_conservation]
- *Hypothesis:* Poor transposon coverage of novel singleton genes could weaken the genome-wide association, because such genes would be miscounted as neutral. The same coverage problem could also keep them out of modules, which would inflate the modules' core fraction. [src: fitness_effects_conservation]
- *Hypothesis:* The module-membership thresholds may change which genes count as module members, and so may change the measured core fraction. [src: module_conservation]

## Resolving Work

- Re-run the module-conservation comparison across a range of ICA membership thresholds. This would show whether module enrichment for core genes holds or disappears as the thresholds change.
- Restrict the genome-wide fitness-conservation analysis to non-essential genes with adequate transposon coverage. This would show whether the weak association strengthens once essential and poorly covered genes are removed, though it would still not match the module analysis's conditioning on detected module membership and selected thresholds.
- Stratify both analyses by insertion density per gene. This would show whether singleton genes are under-represented among measurable genes, and whether that alone explains the different core fractions.
- Compute both statistics on a single shared gene set, fitness-category definition and module-membership rule. This would show whether the disagreement remains once the estimands are aligned.
