---
type: "Concept"
description: "In which experimental conditions dark genes show strong fitness effects (stress versus nutrient/community), and caveats such as polar effects and operon context."
sources: ["summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Condition-specific fitness of dark genes

This page covers the experimental conditions in which dark genes show strong fitness effects (stress versus nutrient or community), and the caveats of polar effects and operon context. Across dark genes with strong effects, stress conditions dominate. [src: functional_dark_matter] Truly dark genes with strong effects are depleted in stress conditions relative to annotation-lag genes. [src: discoveries, truly_dark_genes] Polar effects may inflate some phenotypes. [src: truly_dark_genes]

## Literature Context

The one candidate paper is a CRISPR interference (CRISPRi, gene repression) screen of the cyanobacterium Synechocystis sp. PCC 6803. It used a pooled library of 21,705 individual mutants, with high redundancy over all open reading frames and noncoding RNAs. The library was screened in 11 bioreactor-controlled conditions that spanned multiple light regimes and carbon sources [PMID 37494719](https://pubmed.ncbi.nlm.nih.gov/37494719/). This is a single-organism study, and only its abstract was available for this section.

The authors report that repressing a gene was beneficial in one condition but generally detrimental in others. This was most visible for light-harvesting and light-conversion genes, such as antenna components at high light and PSII subunits during photoheterotrophy. They interpret this as a tradeoff of reduced growth speed for enhanced robustness to perturbation. The data set also assigns condition-specific importance to many previously unannotated genes, and it points to extra functions for central metabolic enzymes. Phosphoribulokinase, glyceraldehyde-3-phosphate dehydrogenase and the small protein CP12 were critical for mixotrophy and photoheterotrophy [PMID 37494719](https://pubmed.ncbi.nlm.nih.gov/37494719/).

The paper's general point is that unannotated genes can be given a functional context by the conditions in which they matter. This is consistent with the hub's framing of dark genes by condition class. The hub reports that stress conditions dominate among dark genes with strong effects overall. It also reports that truly dark genes are depleted in stress (OR=0.53, p<0.001) relative to annotation-lag genes and are enriched in nutrient, mixed community and iron conditions. The paper does not test the stress-versus-community contrast, and it does not address truly dark genes as a class. It therefore neither supports nor contradicts that result.

The paper does extend the hub in a limited way. It reports that fitness effects can vary in sign across conditions for a single gene, and that this reflects physiological tradeoffs. That makes it a cautionary analogy for how condition-specific phenotypes are read, and it should not be read as a general rule about fitness phenotypes. The paper does not address polar effects or operon context, which are the hub's main caveats, so that caveat has no support or challenge from this literature. The hub's open directions, namely removing genes in operons with strongly fit neighbours and following up with targeted assays, remain untested here. The hub's nutrient and community enrichment of truly dark genes is novel relative to this candidate.

## Stress conditions dominate dark genes overall

Across dark genes with strong fitness effects, stress conditions (metals, oxidative, osmotic) dominate, followed by carbon source and nitrogen source utilization. [src: functional_dark_matter] Within that analysis, stress-condition dark genes were not more accessory than carbon/nitrogen genes. Fisher's exact test (n=7,491) rejected that hypothesis (p=0.013). The direction was opposite: 23.0% of stress genes were accessory versus 25.5% for carbon/nitrogen. [src: functional_dark_matter]

## Truly dark genes shift away from stress

Truly dark genes with strong fitness phenotypes are depleted in stress conditions (OR=0.53, p<0.001), where OR is odds ratio. This is contrary to expectation. [src: discoveries, truly_dark_genes] The comparison is against annotation-lag genes: 28.7% versus 43.2% (|f| ≥ 2). [src: truly_dark_genes] See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]] for the two classes.

These genes are instead enriched in nutrient, mixed community and iron conditions. [src: discoveries, truly_dark_genes] A second profile of the same comparison gives these values:

- Enriched in mixed community: 7.5% versus 0% for annotation-lag genes. [src: truly_dark_genes]
- Enriched in iron: 0.7% versus 0%. [src: truly_dark_genes]
- Enriched in nutrient time-series and rich media. [src: truly_dark_genes]
- Depleted in stress: 43.3% versus 54.7%. [src: truly_dark_genes]
- Depleted in carbon source: 13.7% versus 21.7%. [src: truly_dark_genes]
- Depleted in motility: 1.2% versus 3.2%. [src: truly_dark_genes]

The stress percentages differ between these two profiles (28.7% versus 43.2% [src: truly_dark_genes], and 43.3% versus 54.7% [src: truly_dark_genes]). The claims do not say why, so both are reported.

The reports read this as a hypothesis. Truly dark genes may encode novel metabolic or inter-species interaction functions rather than stress responses. [src: discoveries, truly_dark_genes] They may also reflect community-specific behaviors poorly represented in single-organism annotation databases. [src: truly_dark_genes]

## Candidate examples

Individual candidates show the range of conditions. PV4/5210953 (score 10) has a motility phenotype (|f| = 5.5), sits in an operon with TatC (Sec-independent translocase), and belongs to ICA module M016. ICA is independent component analysis. [src: truly_dark_genes] ANA3/7026383 (score 9) has a nitrogen source phenotype (|f| = 8.6), an operon with an ABC transporter (ATP-binding cassette), and ICA module M018. [src: truly_dark_genes] DvH/206658 (score 9) has a stress phenotype (|f| = 5.4). eggNOG suggests trehalose synthase despite the hypothetical annotation, which may be a mis-annotation or a novel variant. [src: truly_dark_genes]

## Operon context and caveats

Among truly dark genes in ICA organisms, 25.9% show operon-like cofitness (|r| ≥ 0.3) with adjacent genes. [src: truly_dark_genes] 594 genes belong to ICA fitness modules. Guilt-by-association there reveals functions including phage integrases, metal transporters, chemotaxis systems and iron regulation. [src: truly_dark_genes] See [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]].

Some strong phenotypes may reflect polar effects on downstream genes rather than the function of the truly dark gene itself. [src: truly_dark_genes]

## Tensions

- Stress conditions dominate dark genes with strong effects overall. [src: functional_dark_matter] Truly dark genes with strong effects are depleted in stress relative to annotation-lag genes. [src: discoveries, truly_dark_genes] The two claims use different comparisons, so they may not conflict directly.

## Open Directions

- Re-run the condition-class comparison after removing genes in operons with strongly fit neighbours. This would test how much polar effects drive the nutrient, community and iron enrichment.
- Reconcile the two stress percentages by matching gene sets and condition definitions.
- Test the novel-metabolism hypothesis directly. Follow up the nitrogen-source and mixed-community genes with targeted growth or interaction assays.
- Compare the condition profiles of dark genes in ICA modules and outside them, to see whether module membership changes the stress depletion.
