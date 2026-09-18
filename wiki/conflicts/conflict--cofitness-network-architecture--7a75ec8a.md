<!-- tension-hash: 7a75ec8a94aedada -->
# Do Essential Genes Sit Outside Fitness Modules, or Merely Outside What Fitness Assays Can Measure?

Three projects in this corpus place essential genes differently relative to coregulated fitness modules. Module-conservation work reports that zero essential genes appeared in modules derived by independent component analysis (ICA, a blind source-separation method that decomposes fitness matrices into coregulated gene sets); essential-genome work identifies universally and variably essential families; and dark-gene work finds essentiality enriched in the least-annotated gene set. The concept page frames this as a measurement-boundary tension rather than a biological contradiction, and whether that framing holds determines how [[concepts/cofitness-network-architecture]] should treat module membership as evidence of functional importance.

## Evidence Sides

**Modules contain no essential genes.** The module-conservation results introduce a measurement-boundary tension rather than a biological contradiction: zero essential genes appeared in ICA modules. [src: module_conservation; essential_genome] The reported count is zero rather than a small number, and no mechanism for the exclusion is given in the tension text itself.

**Essential families are real and structured.** Essential-genome analyses identify universally and variably essential families. [src: module_conservation; essential_genome] On this side essentiality is a populated, cross-organism category with internal gradation — universally essential versus variably essential — rather than an empty or marginal set.

**Dark genes are enriched for essentiality.** Truly dark genes show the opposite comparison at the gene-set level—18.0% essential versus 13.4% for annotation-lag genes—but short genes and insertion bias complicate interpretation. [src: truly_dark_genes] Here essentiality is measurable and differentially distributed across gene sets, with the enrichment carried by the less-characterized side. The caveat stays unresolved: short genes and insertion bias are named as complications, with no direction stated for their effect. [src: truly_dark_genes]

## Possible Reconciliations

- *Hypothesis:* the zero is definitional. If module assignment requires a fitness profile and essential genes have none, the exclusion is structural and the two sides never test the same population. [src: module_conservation; essential_genome]
- *Hypothesis:* the dark-gene enrichment is partly a length artifact. If short genes are scored essential because insertions are sparse rather than because disruption is lethal, the 18.0% versus 13.4% gap shrinks under length-matched comparison. [src: truly_dark_genes]
- *Hypothesis:* "essential" denotes different thresholds in each analysis, so the essential set entering the module test and the set entering the gene-set comparison are not the same set.

## Resolving Work

- Re-run the ICA module assignment with the essentiality call and its threshold recorded per gene: does any gene classified essential ever receive a fitness profile, or is the zero exact by construction? [src: module_conservation; essential_genome]
- Stratify the 18.0% versus 13.4% essential-fraction comparison by coding length and by insertion count per gene: does the enrichment survive length matching? [src: truly_dark_genes]
- Compare the essentiality definitions and denominators used across the three projects side by side, without merging them, to establish whether one gene set is nested inside another.
- Test whether universally essential and variably essential families differ in having any measurable fitness signal, which would locate the measurement boundary inside the essential category rather than at its edge. [src: module_conservation; essential_genome]
