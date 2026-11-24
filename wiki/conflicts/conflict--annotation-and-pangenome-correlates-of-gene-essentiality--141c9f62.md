<!-- tension-hash: 141c9f62b6a70884 -->
# Modest Core Enrichment Versus Unexplained Strain-Specific Essential Genes

This page records a tension in how essential genes (genes required for growth in a transposon sequencing, or TnSeq, screen) relate to the core genome (genes shared by the strains compared). One reading is that the core enrichment of essential genes is modest. The other concerns the essential-auxiliary and essential-unmapped genes, which sit outside that simple core signal and are explained only partly. It matters because the correlates may describe essentiality without explaining why conserved genes are essential. The concept page is [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality]].

## Evidence Sides

**Side A: core enrichment is modest**
- The core fractions are 86.1% versus 81.2%, and the penetrance correlation is weak. Together these show modest core enrichment. [src: conservation_vs_fitness, essential_genome]
- The TENSION text gives no direction for the penetrance correlation beyond calling it weak. Penetrance means how consistently a gene is essential across strains. The two core fractions are as the sources report them, and the denominators are not restated here.

**Side B: strain-specific genes are explained only partly**
- For essential-auxiliary genes only, the report links the top subsystems to strain-specific variants of core machinery and mobile genetic elements. [src: conservation_vs_fitness]
- For essential-unmapped genes, the claims say only that they are strain-specific and the least characterized. [src: conservation_vs_fitness]
- No mechanism is given for why these genes are essential.

## Possible Reconciliations

- **Hypothesis 1:** Modest enrichment may result from mixing categories. Core essential genes may be pulled toward the core, while auxiliary and unmapped essential genes pull away from it. This has not been tested.
- **Hypothesis 2:** The weak penetrance correlation may reflect annotation gaps in the unmapped class rather than real biology. Better annotation would then sharpen the signal.
- **Hypothesis 3:** Strain-specific variants of core machinery may be functionally equivalent to core genes. If so, a core definition based on function would raise the enrichment.

## Resolving Work

- Data: the essential-auxiliary and essential-unmapped gene sets from the conservation analysis. Method: split the core fraction by category. Question: does each category differ from the 81.2% non-essential core fraction?
- Data: the penetrance values from the essential-genome analysis. Method: report the correlation's direction with a confidence interval. Question: is the weak correlation distinguishable from zero?
- Data: the mobile genetic element annotations for essential-auxiliary genes. Method: an enrichment test against non-essential genes. Question: are mobile elements specifically overrepresented?
- Data: the essential-unmapped genes. Method: re-annotate them with sequence and structure homology searches. Question: do they resolve into known functions or remain uncharacterized?
- Data: variants of core machinery across strains. Method: functional-equivalence grouping of the variants. Question: does grouping them with core genes change the enrichment?
