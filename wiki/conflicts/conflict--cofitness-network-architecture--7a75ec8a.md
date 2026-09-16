<!-- tension-hash: 7a75ec8a94aedada -->
# Are Essential Genes Absent from Fitness Modules or Measured Outside Them?

The [[concepts/cofitness-network-architecture]] page records a tension about where essential genes sit relative to cofitness structure (cofitness meaning correlated fitness profiles between genes across conditions). One project found zero essential genes in independent component analysis (ICA, a decomposition of fitness profiles into co-varying gene sets, or "modules"). Essential-genome analyses, however, identify gene families that are essential in every organism or only in some. [src: module_conservation; essential_genome] A gene-set comparison of genes of unknown function finds that "truly dark" genes have a higher essential fraction than annotation-lag genes. Short gene length and insertion bias complicate that comparison. [src: truly_dark_genes] This matters because whether module-based architecture claims extend to essential biology depends on whether the absence is biological or comes from how modules and essentiality are measured.

## Evidence Sides

**Side A — ICA modules contain no essential genes**
In the module-conservation results, zero essential genes appeared in ICA modules. [src: module_conservation; essential_genome] The concept page frames this as a measurement-boundary tension, not a biological contradiction. [src: module_conservation; essential_genome]

**Side B — Essential families are widespread and structured**
Essential-genome analyses identify universally essential families, which are essential in all organisms examined. They also identify variably essential families, which are essential in some organisms but not in others. [src: module_conservation; essential_genome]

**Side C — Gene-set comparison points the other way for dark genes**
Truly dark genes show the opposite comparison at the gene-set level. They are 18.0% essential, versus 13.4% for annotation-lag genes. [src: truly_dark_genes] Short genes and insertion bias complicate interpretation. [src: truly_dark_genes]

## Possible Reconciliations

- **Hypothesis (measurement boundary):** ICA modules may be built from fitness variation across conditions. Genes with no measurable fitness values may therefore never enter module inference. If so, the zero would reflect method scope rather than biology.
- **Hypothesis (different units):** Side B describes ortholog families (groups of genes across organisms descended from a common ancestral gene) and Side C describes gene sets. Neither describes module membership directly, so the claims may not conflict.
- **Hypothesis (artifact):** The higher essential fraction among truly dark genes may partly reflect short genes and insertion bias rather than essentiality itself. This would weaken Side C as evidence about essential biology.

## Resolving Work

- **Data:** module_conservation gene-to-module assignments joined to essential_genome essentiality calls. **Method:** check whether essential genes were present in the input matrix used for ICA. **Question:** is the zero an exclusion-by-construction?
- **Data:** truly_dark_genes gene sets with gene length and insertion-density covariates. **Method:** compare essential fractions after stratifying or matching on length and insertion density. **Question:** does the gap between 18.0% and 13.4% persist once these confounders are controlled? [src: truly_dark_genes]
- **Data:** variably essential families from essential_genome. **Method:** test whether non-essential members of these families, in organisms where they are dispensable, join ICA modules. **Question:** do essential families connect to cofitness structure when fitness is measurable?
- **Data:** cofitness networks built without ICA. **Method:** compute correlation-based neighborhoods for genes with partial fitness data near essentiality thresholds. **Question:** does module absence hold under a different module definition?
