---
type: "Concept"
description: "Whether amino acid biosynthesis is near-universally complete in free-living bacteria per GapMind, including the single serine gap in Desulfovibrio vulgaris; stops short of experimental essentiality."
sources: ["summaries/essential_metabolome__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Conservation of amino acid biosynthesis pathways across bacteria

In a seven-organism GapMind analysis, amino acid biosynthesis is near-universally complete: 17 of 18 pathways are present in every organism, and the one exception is serine in Desulfovibrio vulgaris. [src: essential_metabolome] The evidence is a small, phylogenetically narrow sample and a computational prediction, not an experimental essentiality test. [src: essential_metabolome] See [[summaries/essential_metabolome__REPORT]] for the source report and [[entities/gapmind]] for the tool.

## Literature Context

The most directly relevant candidate is a genome-scale survey of amino acid auxotrophy. It predicted the biosynthetic capabilities of 26,277 unique bacterial genomes spanning 12 phyla, using a metabolic pathway model validated with empirical data [PMID 37993466](https://pubmed.ncbi.nlm.nih.gov/37993466/). Auxotrophy is widespread across phyla, but the authors conservatively estimate that the majority of taxa (78.4%) can synthesize all amino acids. Auxotrophies were more prevalent in obligate intracellular parasites and in free-living taxa with genomic attributes characteristic of 'streamlined' life history strategies. Auxotrophic taxa were more abundant in host-associated environments, including the human oral cavity and gut, and in fermented foods. They were relatively rare in soil and aquatic systems [PMID 37993466](https://pubmed.ncbi.nlm.nih.gov/37993466/). These are computational predictions, not growth tests.

A second candidate is a review of proline biosynthesis. Pathway reconstruction from genome data for hundreds of eubacterial genomes showed that the glutamate-derived route is the most prevalent pathway. It also showed that alternative routes via the arginine pathway intermediate ornithine exist, and that in some organisms they contribute to or could fully account for proline synthesis [PMID 25367752](https://pubmed.ncbi.nlm.nih.gov/25367752/). This shows that a single amino acid can be made by variant routes. That bears on how a reference-based tool might score a pathway as incomplete. The other candidates cover phosphonate natural products, secretion systems, the cytoskeleton, sterol modification, cytochrome P450 and other unrelated topics. They do not bear on this page, so I do not use them.

The hub's seven-organism GapMind result is consistent with the broad survey. In the hub, 17 of 18 pathways are complete in every organism, and the only exception is serine in Desulfovibrio vulgaris. That fits the survey's finding that most bacteria can make all amino acids, and that auxotrophy is rarer in free-living, non-streamlined taxa [PMID 37993466](https://pubmed.ncbi.nlm.nih.gov/37993466/). The hub's own limits still apply. The sample is mostly Proteobacteria plus one Deltaproteobacterium, and the result cannot be generalized pan-bacterially. The larger survey gives a better-powered picture, but the hub does not test it directly.

The serine gap in D. vulgaris is a single observation. It sits comfortably with the survey's link between auxotrophy and particular lifestyles. However, the survey does not examine this organism or serine in the material available here, so I make no claim that it supports the gap. The hub's artefact explanation is a non-canonical or divergent pathway missing from GapMind's reference database. The proline review shows that alternative routes are real for at least one amino acid [PMID 25367752](https://pubmed.ncbi.nlm.nih.gov/25367752/). That makes the artefact explanation plausible, though it remains a hypothesis. The hub's proposed serine-free growth test would extend the literature, because the candidates offer no experimental check of this organism. The hub's remark that completeness is near-universal rather than strictly universal is consistent with the survey's figure of 78.4%, not 100%. The two figures come from very different sample sizes and methods, so they should not be reconciled numerically. The wider pan-bacterial GapMind comparison and the Black Queen link are not addressed by these candidates.

## Completeness across the seven organisms

Six organisms have all 18 pathways complete, and Desulfovibrio vulgaris has 17 of 18. [src: essential_metabolome] The report counts 17 of 18 pathways present in all 7 organisms, which is 100% within the sample. [src: essential_metabolome]

- Caulobacter vibrioides: 18/18, 100% [src: essential_metabolome]
- Shewanella oneidensis: 18/18, 100% [src: essential_metabolome]
- Pseudomonas aeruginosa: 18/18, 100% [src: essential_metabolome]
- Pseudomonas putida: 18/18, 100% [src: essential_metabolome]
- Sinorhizobium meliloti: 18/18, 100% [src: essential_metabolome]
- Azospirillum brasilense: 18/18, 100% [src: essential_metabolome]
- Desulfovibrio vulgaris (DvH): 17/18, 94.4% [src: essential_metabolome]

The conserved complete pathways are arg, asn, chorismate, cys, gln, gly, his, ile, leu, lys, met, phe, pro, thr, trp, tyr and val. [src: essential_metabolome] The report reads this as a minimal metabolic repertoire for independent growth. [src: essential_metabolome] It also reads the 6 of 7 organisms (85.7%) with all 18 pathways as suggesting that amino acid prototrophy is the ancestral state of free-living bacteria. [src: essential_metabolome] Both readings are interpretations drawn from seven genomes.

## The serine exception

Serine biosynthesis is present in only 6 of 7 organisms (85.7%). [src: essential_metabolome] Desulfovibrio vulgaris is the only organism without a complete serine pathway, judged by the GapMind categories complete or likely_complete. [src: essential_metabolome] It lives in anaerobic, organic-rich environments such as sediments and intestinal tracts. [src: essential_metabolome] The report also lists biofilms among its niches. [src: essential_metabolome]

The report offers explanations. They are hypotheses, not findings.

- It may be a genuine auxotrophy, with the organism depending on external serine. [src: essential_metabolome]
- Environmental protein degradation could supply abundant serine. [src: essential_metabolome]
- Dropping biosynthesis could be advantageous when nutrients are abundant. [src: essential_metabolome]
- The loss could be genomic economy, meaning loss of energetically costly genes whose product is freely available. [src: essential_metabolome]
- Auxotrophs in general depend on external nutrients or on symbiotic or commensal lifestyles. [src: essential_metabolome]

The report also gives reasons the gap may be an artefact.

- DvH may use a non-canonical serine pathway that is absent from GapMind's reference database. [src: essential_metabolome]
- The pathway may use divergent enzymes that fall below GapMind's homology threshold. [src: essential_metabolome]
- The genes may be present but unannotated in the assembly. [src: essential_metabolome]

The report proposes three checks. One is to look at lower-confidence GapMind predictions for a serine pathway with "steps_missing" status. [src: essential_metabolome] Another is a literature review of whether serine auxotrophy has been documented experimentally. [src: essential_metabolome] The third is to test DvH growth on serine-free minimal media. [src: essential_metabolome] See [[entities/desulfovibrio-vulgaris-hildenborough]] for the organism.

## Universal or near-universal?

The report revised its original H1, a core set of pathways universally complete across bacteria. [src: essential_metabolome] It judged H1 partially supported with significant caveats. [src: essential_metabolome] The report concludes that completeness is near-universal, not strictly universal. [src: essential_metabolome] It attributes the remaining diversity, even among organisms with experimental essential gene data, to likely ecological adaptation and nutrient availability. [src: essential_metabolome]

## Tensions

- The report states that no pathways are truly universal (100%) even in this small sample. [src: essential_metabolome] Yet it also reports 17 of 18 pathways present in all 7 organisms, "100% within this sample" [src: essential_metabolome], with serine as the single exception. [src: essential_metabolome] The page records both statements as the report gives them and does not reconcile them. The report's own conclusion is "near-universal rather than strictly universal". [src: essential_metabolome]

## Limits

The sample is mostly Proteobacteria plus one Deltaproteobacterium. [src: essential_metabolome] The report states that the result cannot be generalized to a pan-bacterial scale. [src: essential_metabolome]

A separate pan-bacterial GapMind comparison, in [[summaries/pathway_capability_dependency__REPORT]], gives completeness for all genes and for core genes only. [src: pathway_capability_dependency]

| Pathway | All genes | Core only | Gap |
|---|---|---|---|
| Leucine (leu) | 0.614 | 0.468 | 0.146 [src: pathway_capability_dependency] |
| Valine (val) | 0.614 | 0.468 | 0.146 [src: pathway_capability_dependency] |
| Arginine (arg) | 0.613 | 0.472 | 0.141 [src: pathway_capability_dependency] |
| Lysine (lys) | 0.804 | 0.664 | 0.140 [src: pathway_capability_dependency] |
| Threonine (thr) | 0.803 | 0.663 | 0.140 [src: pathway_capability_dependency] |

## Open Directions

- Check lower-confidence GapMind predictions for DvH, to see whether a serine pathway is listed with "steps_missing" status.
- Review the literature to find out whether D. vulgaris serine auxotrophy has been documented experimentally.
- Grow DvH on serine-free minimal media to confirm or refute auxotrophy.
- Repeat the GapMind completeness count on a phylogenetically broader genome set, to test whether 17 of 18 pathways stay near-universal beyond Proteobacteria.
- Relate the serine gap to [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]], which would test the genomic economy explanation.
