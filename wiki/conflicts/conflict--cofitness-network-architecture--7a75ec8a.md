<!-- tension-hash: 7a75ec8a94aedada -->
# Do Essential Genes Sit Outside Fitness Modules, or Merely Outside What Fitness Assays Can Measure?

Three projects position essential genes differently relative to coregulated fitness modules, and the module-conservation results frame this as a measurement-boundary tension rather than a biological contradiction. Module-conservation work reports zero essential genes in modules derived by independent component analysis (ICA, a blind source-separation method that decomposes fitness matrices into coregulated gene sets); essential-genome work identifies universally and variably essential families; dark-gene work finds essentiality enriched in the least-annotated gene set. Whether the zero says something about module membership or about how essentiality is measured determines how [[concepts/cofitness-network-architecture]] should treat module membership as evidence of functional importance.

## Evidence Sides

**Modules contain no essential genes.** The module-conservation results introduce a measurement-boundary tension rather than a biological contradiction: zero essential genes appeared in ICA modules. [src: module_conservation; essential_genome] The count on this side is exactly zero, not a small residual.

**Essential families are real and structured.** Essential-genome analyses identify universally and variably essential families. [src: module_conservation; essential_genome] Essentiality is therefore a populated cross-organism category with internal gradation — universal versus variable. What that gradation implies for module membership is left open here.

**Dark genes are enriched for essentiality.** Truly dark genes show the opposite comparison at the gene-set level—18.0% essential versus 13.4% for annotation-lag genes—but short genes and insertion bias complicate interpretation. [src: truly_dark_genes] Essentiality is measurable and differentially distributed here, with the higher fraction on the less-characterized side; the stated caveats are recorded without a direction and remain unresolved.

## Possible Reconciliations

- *Hypothesis:* the zero is definitional. If module assignment requires a fitness profile and essential genes have none, the exclusion is structural and the two sides never test the same population. [src: module_conservation; essential_genome]
- *Hypothesis:* the dark-gene enrichment is partly a length artifact. If short genes are scored essential because insertions are sparse rather than because disruption is lethal, the 18.0% versus 13.4% gap shrinks under length-matched comparison. [src: truly_dark_genes]
- *Hypothesis:* "essential" denotes different thresholds in each analysis, so the essential set entering the module test and the set entering the gene-set comparison are not the same set.

## Resolving Work

- Re-run the ICA module assignment with the essentiality call and its threshold recorded per gene: does any gene classified essential ever receive a fitness profile, or is the zero exact by construction? [src: module_conservation; essential_genome]
- Stratify the 18.0% versus 13.4% essential-fraction comparison by coding length and by insertion count per gene: does the enrichment survive length matching? [src: truly_dark_genes]
- Compare the essentiality definitions and denominators used across the three projects side by side, without merging them, to establish whether one gene set is nested inside another.
- Test whether universally essential and variably essential families differ in having any measurable fitness signal, which would locate the measurement boundary inside the essential category rather than at its edge. [src: module_conservation; essential_genome]
