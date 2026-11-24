---
type: "Concept"
description: "Whether amino acid pathway completeness depends on accessory genes and community metabolite sharing, as Black Queen gene loss predicts; stops at genomic and NMDC soil evidence."
sources: ["summaries/discoveries.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md"]
---
# Black Queen dynamics in amino acid biosynthesis

Whether amino acid pathway completeness depends on accessory genes and community metabolite sharing, as Black Queen gene loss predicts; stops at genomic and NMDC soil evidence.

## Literature Context

The one candidate paper bears on the Black Queen idea that biosynthetic genes can be lost when the nutrient is available from the environment. It analysed 949 metabolic networks and found that auxotrophies are likely highly prevalent in both symbiotic and free-living bacteria [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/). That finding is a genome-scale inference from metabolic networks. It does not measure auxotrophy directly.

The same study tested whether selection could explain such loss. It competed 20 auxotrophic mutants of Escherichia coli and Acinetobacter baylyi against the prototrophic wild type, with the focal nutrient present. The mutants covered amino acids, vitamins and nucleobases. Virtually all of them showed a concentration-dependent growth advantage of around 13% [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/). The fitness effect depended on which gene in a pathway was deleted. It also differed between the two species for the same gene [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/). The authors conclude that adaptive benefits could drive the loss of conditionally essential biosynthetic genes. This is laboratory evidence from two species. The abstract does not report tests in communities or natural environments.

The corpus's genomic results are consistent with this picture. In the pan-bacterial GapMind comparison, amino acid pathways showed the largest gaps between all-genes and core-only completeness, about 0.14 for leucine, valine, arginine, lysine and threonine. This means completeness depends on genes that are not universally present within a species. That is a precondition for loss, but it does not show the selective advantage the candidate paper measured. The corpus supplies variation across strains in nature. The candidate paper supplies a possible mechanism for losing a gene in the laboratory. The corpus does not test that mechanism.

The NMDC soil result is also directionally consistent with environmental supply favouring loss. Community pathway completeness tended to be lower where ambient amino acid intensity was higher, with 11 of 13 pathways negative (sign test p = 0.011). Only leucine and arginine passed FDR correction. This extends the candidate paper's nutrient-dependence from single-species competition to community-weighted soil data. The extension is weak, because the dataset is nearly single-study and it is correlational. The paper's costly-loss logic fits the leucine and arginine signals, but the paper does not compare costs across amino acids. The corpus's energy-cost reading is therefore its own interpretation. The soil ipdC–tryptophan reversal (OR = 0.30, p = 0.02), which the report calls hypothesis-generating, is likewise compatible with exudate-supplied nutrients relaxing selection. It is untested against the candidate paper's mechanism. Nothing in the candidate paper conflicts with the corpus.

## Genomic evidence: accessory genes and variable pathways

The genome-level results show that accessory genes contribute directly to pathway completeness. They give a precondition for Black Queen dynamics, not a direct test of them. [src: pathway_capability_dependency]

The pan-bacterial GapMind comparison uses sequence_scope = 'core' (core pangenome genes only) against sequence_scope = 'all' (all genes) to identify accessory genome contributions to pathway completeness. [src: pathway_capability_dependency] The pathways with the greatest accessory dependence are all amino acid biosynthesis routes. [src: pathway_capability_dependency] Amino acid pathways consistently show the largest gaps, meaning their completeness depends on genes not universally present within a species. [src: pathway_capability_dependency]

| Pathway | All-genes completeness | Core-only completeness | Gap |
|---|---|---|---|
| leucine (leu) | 0.614 | 0.468 | 0.146 [src: pathway_capability_dependency] |
| valine (val) | 0.614 | 0.468 | 0.146 [src: pathway_capability_dependency] |
| arginine (arg) | 0.613 | 0.472 | 0.141 [src: pathway_capability_dependency] |
| lysine (lys) | 0.804 | 0.664 | 0.140 [src: pathway_capability_dependency] |
| threonine (thr) | 0.803 | 0.663 | 0.140 [src: pathway_capability_dependency] |

- For the top 5 accessory-dependent pathways (leucine, valine, arginine, lysine, threonine), approximately 14% of species-level pathway completeness comes from accessory genes. [src: pathway_capability_dependency]
- The discoveries digest reports the same five pathways with the largest accessory dependence gap (~0.14). [src: discoveries]
- The report concludes that for a substantial fraction of bacteria, amino acid biosynthesis completeness depends on accessory pangenome genes. [src: pathway_capability_dependency]
- It calls this direct evidence for Black Queen dynamics, with synthesis capacity distributed across strains within a species rather than universally maintained. [src: pathway_capability_dependency] This is the report's interpretation. The page treats the gaps as a precondition, not a test of gene loss. [src: pathway_capability_dependency]
- Carbon source utilization pathways tend to show smaller gaps. The report suggests this may be because carbon catabolism genes are universally present or universally absent rather than variably distributed. [src: pathway_capability_dependency]
- The report reads strain differences in biosynthetic capability within a species as a precondition for metabolic functions becoming community-level public goods. [src: pathway_capability_dependency]
- It names the branched-chain amino acids (leucine, valine) and the basic amino acids (arginine, lysine) as the most common candidates for community-level metabolic sharing. [src: pathway_capability_dependency]
- Across 2,810 species with 10+ genomes, species with more variable pathways have significantly more open pangenomes (partial Spearman rho=0.530, p=2.83e-203, controlling for genome count). The report considers this consistent with the BQH prediction that pathway gene loss is ongoing. [src: pathway_capability_dependency]
- The report reframes the BQH as a continuum of pathway dependency that varies with environmental context, not a binary of needed versus genomic baggage. [src: pathway_capability_dependency]
- It also proposes that gene loss may be constrained by the breadth of environmental conditions a species meets, not only by mean fitness under one condition. [src: pathway_capability_dependency]

This genomic picture sits alongside a constraint on loss. Among 735 amino acid biosynthesis pathway-organism pairs, 467 (63.5%) were active, 220 (29.9%) intermediate and 48 (6.5%) latent. [src: metabolic_capability_dependency] The report interprets these pathways as largely essential, because organisms cannot scavenge all amino acids in all growth conditions tested. [src: metabolic_capability_dependency]

## Environmental evidence from soil plant-growth-promoting bacteria

Within soil/rhizosphere species (n = 1,039), the association between tryptophan completeness and ipdC reversed (OR = 0.30, p = 0.02). Tryptophan-complete soil species were less likely to carry ipdC. [src: pgp_pangenome_ecology] The report hypothesizes that soil-associated PGPB obtain tryptophan from root exudates. That would relax selection for autonomous biosynthesis, while ipdC is retained for IAA production from plant-supplied substrate. [src: pgp_pangenome_ecology] It calls this consistent with soil PGPB obtaining aromatic amino acids from plant exudates rather than synthesizing them de novo. [src: pgp_pangenome_ecology] The report says this reversal is hypothesis-generating, not conclusive. [src: pgp_pangenome_ecology]

## Community evidence in NMDC soil samples

Across NMDC samples, community pathway completeness tends to be lower where ambient amino acid intensity is higher. This is the direction BQH predicts. [src: nmdc_community_metabolic_ecology] Eleven of 13 testable pathways were negative, with binomial sign test p = 0.011. [src: discoveries, nmdc_community_metabolic_ecology] The report calls this weak but consistent support for community-scale Black Queen dynamics. [src: nmdc_community_metabolic_ecology] It describes the analysis as extending the hypothesis to community-weighted scores at landscape scale across diverse NMDC soil samples. [src: nmdc_community_metabolic_ecology]

Two pathways pass Benjamini-Hochberg (BH) false discovery rate (FDR) correction. [src: nmdc_community_metabolic_ecology]

| Pathway | Spearman r | q (BH) | n |
|---|---|---|---|
| leucine | −0.390 | 0.022 | 62 [src: discoveries, nmdc_community_metabolic_ecology] |
| arginine | −0.297 | 0.049 | 80 [src: discoveries, nmdc_community_metabolic_ecology] |

The report describes both as energetically expensive to synthesise (leucine 37 ATP equivalents, arginine 26 ATP equivalents). ATP is adenosine triphosphate. It reads this as consistent with the BQH prediction that costly functions are most likely to be lost when environmental supply is reliable. [src: discoveries, nmdc_community_metabolic_ecology]

The other pathways were not significant after FDR correction:

| Pathway | r | q (BH) | n |
|---|---|---|---|
| methionine | −0.496 | 0.117 | 18 [src: nmdc_community_metabolic_ecology] |
| tryptophan | −0.294 | 0.136 | 44 [src: nmdc_community_metabolic_ecology] |
| threonine | −0.271 | 0.393 | 23 [src: nmdc_community_metabolic_ecology] |
| phenylalanine | −0.159 | 0.303 | 88 [src: nmdc_community_metabolic_ecology] |
| valine | −0.151 | 0.446 | 54 [src: nmdc_community_metabolic_ecology] |
| serine | −0.061 | 0.762 | 59 [src: nmdc_community_metabolic_ecology] |
| asparagine | −0.061 | 0.762 | 73 [src: nmdc_community_metabolic_ecology] |
| isoleucine | −0.057 | 0.823 | 18 [src: nmdc_community_metabolic_ecology] |
| chorismate | −0.038 | 0.823 | 65 [src: nmdc_community_metabolic_ecology] |
| glycine | +0.081 | 0.562 | 114 [src: nmdc_community_metabolic_ecology] |
| tyrosine | +0.419 | 0.117 | 26 [src: nmdc_community_metabolic_ecology] |

Methionine has the largest effect but is underpowered. [src: discoveries, nmdc_community_metabolic_ecology] The report predicts a larger metabolomics dataset would likely reach significance for it. [src: nmdc_community_metabolic_ecology]

### Robustness

- Leucine is unchanged under soil-only stratification (q = 0.022) and study-level blocking, in a dataset that is 95% single-study. [src: discoveries]
- In the soil-only test, leucine is identical to the full cohort because all leucine samples are Soil. [src: nmdc_community_metabolic_ecology]
- Arginine loses FDR significance in the soil-only test (r = −0.264, q = 0.117, n = 78) but stays directionally consistent. [src: nmdc_community_metabolic_ecology]
- Excluding the 6-sample second study gives arginine r = −0.264, p = 0.019 (n = 78). The report reads this as showing the signal is not driven by the minor study. [src: nmdc_community_metabolic_ecology]
- The soil-only sign test is unchanged at 11/13 negative, p = 0.011. [src: nmdc_community_metabolic_ecology]

## Tensions and caveats

- Tyrosine is a non-significant outlier in the anti-BQH direction (r = +0.42). The report hypothesizes alternative sources such as phenylalanine hydroxylation. [src: discoveries, nmdc_community_metabolic_ecology] Phenylalanine biosynthesis is not captured by the tyrosine completeness score, so such communities may still supply tyrosine. [src: nmdc_community_metabolic_ecology]
- Chorismate (r = −0.038) should be read cautiously. Its proxies are upstream intermediates that reflect precursor availability, not chorismate pool size. [src: nmdc_community_metabolic_ecology]
- Cysteine, histidine and lysine are untestable because the compounds were not detected. KEGG compound annotation in the NMDC data is sparse (2%). [src: nmdc_community_metabolic_ecology]
- Glutamine (n = 4) and proline (n = 9) were skipped. [src: nmdc_community_metabolic_ecology]
- All 33 Freshwater samples lacked paired metabolomics, so the test is soil-only. Freshwater Black Queen dynamics are untested. [src: nmdc_community_metabolic_ecology]
- The report reads the results as suggesting community metabolic potential predicts ecosystem chemistry beyond taxonomic composition. This is an interpretation, not a direct test. [src: nmdc_community_metabolic_ecology]
- The report itself proposes two next steps: replicating in additional NMDC studies with paired taxonomy and metabolomics, and obtaining metabolomics for the 33 Freshwater samples. [src: nmdc_community_metabolic_ecology]

## Open Directions

- Replicate the analysis in additional NMDC studies with paired taxonomy and metabolomics. This would test whether the leucine and arginine signals generalise beyond the current, nearly single-study cohort.
- Obtain or generate metabolomics for the 33 Freshwater NMDC samples, to test whether BQH dynamics differ between aquatic and terrestrial communities.
- Expand metabolomics coverage to power methionine and isoleucine, which have n = 18.
- Score phenylalanine and tyrosine biosynthesis jointly, to test whether hydroxylation explains the tyrosine outlier.
- Link strain-level accessory pathway variation to the community signals, for example for leucine and arginine, using the GapMind core-versus-all gaps.
- Test whether the soil ipdC reversal reflects exudate-supplied tryptophan, by pairing species-level tryptophan completeness with measured root exudate or soil tryptophan.
