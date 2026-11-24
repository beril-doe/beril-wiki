---
type: "Concept"
description: "Which fungal taxa dominate under lignin versus lignin-plus-labile-carbon enrichment and their known saprotroph or white-rot lifestyles; stops at inference limits from replicate noise."
sources: ["summaries/lignin_community_enrichment__REPORT.md"]
---
# Fungal community responses to lignin and labile carbon

Fungal communities in the lignin enrichment shifted sharply with treatment. Lignin alone favored Fusarium and Fusicolla, and lignin plus labile carbon favored Chrysosporium and Aspergillus. The fungal data come from one report and are very noisy between replicates, so the taxon-level patterns are suggestive rather than well supported statistically. [src: lignin_community_enrichment] See also [[summaries/lignin_community_enrichment__REPORT]] and [[concepts/small-sample-limits-in-community-amplicon-statistics]].

## Literature Context

The candidate papers give only indirect, genus-level context for the lifestyle inferences in this page. None of them studies a lignin enrichment, and none involves Fusarium, Fusicolla, Chrysosporium, Aspergillus, Malassezia or Pleurotus. They concern white-rot and other wood-decay basidiomycetes. A transcriptomic and secretomic study of the saprotrophic white-rot fungus Pycnoporus coccineus found early, coordinated expression of carbohydrate-active enzymes (CAZymes) on lignocellulosic substrates. This included early transcriptional regulation of lignin-active peroxidases and a key role for lytic polysaccharide monooxygenases [PMID 28394946](https://pubmed.ncbi.nlm.nih.gov/28394946/). That paper concerns one fungus, in culture, at two time points. It supports the general idea that white-rot lignin degradation is an enzymatic program, but it does not test the genera in this corpus.

A study of coniferous wood-decay fungi found that Phlebia radiata and Trichaptum abietinum were the strongest producers of lignin-modifying oxidoreductases (laccase and manganese peroxidase), both alone and in co-culture, on two media. Fungal combinations also changed enzyme profiles and acidity in ways that depended on which species were present [PMID 28953947](https://pubmed.ncbi.nlm.nih.gov/28953947/). This is an in vitro study of Agaricomycetes. It suggests that lignin-modifying capacity varies between white-rot species and that community composition can alter degradative outcomes. A stable-isotope survey of boreal forest sporocarps reported that white-rot and brown-rot fungi have similar δ13C. The authors read this as white-rot fungi not using lignin-derived carbon. They also found that litter and wood decay genera differed widely in carbon and nitrogen sources [PMID 31126422](https://pubmed.ncbi.nlm.nih.gov/31126422/). That finding is a caution against assuming that a lignin-degrading lifestyle means lignin is the carbon source.

The corpus's lifestyle reading of its taxa is therefore not directly tested by this literature. The report calls Pleurotus a white-rot lignin degrader and appearing only in LC-LC (lignin plus labile carbon in both rounds). That is consistent in kind with the white-rot enzymology above, because labile carbon plus lignin-active fungi is a plausible pairing. The evidence for it is still a single-group observation with 0.99–1.00 within-group Bray-Curtis distance, so the literature does not strengthen it. The same applies to the soft-rot and opportunistic-saprotroph labels for Fusarium, Fusicolla, Chrysosporium and Aspergillus. These labels extend beyond the candidate papers, which cover different organisms. The corpus's sharp treatment shifts, such as Chrysosporium at 61.4% in LC, are novel observations here, not confirmed or contradicted by these papers.

The main point of contact is the caveat from the isotope work [PMID 31126422](https://pubmed.ncbi.nlm.nih.gov/31126422/). It is consistent with the hub's open direction to add lignin-loss assays, since taxon abundance under lignin does not show lignin use. The co-culture results [PMID 28953947](https://pubmed.ncbi.nlm.nih.gov/28953947/) also suggest that interactions among fungi could shape these enrichments, a possibility the corpus does not address.

## Round 1: which taxa dominate

The report says the fungal community shows more extreme treatment-specific responses than the bacterial community. [src: lignin_community_enrichment] It states that lignin alone selects for Fusarium and Fusicolla, described as soft-rot fungi, while lignin plus labile carbon selects for Chrysosporium and Aspergillus, described as more associated with opportunistic saprotrophic growth. [src: lignin_community_enrichment] The report also considers the dominance of Aspergillus, Fusarium and Chrysosporium consistent with their known saprotrophic capabilities, citing Bouws et al. (2008, PMID: 18636256). [src: lignin_community_enrichment]

| Group | Chrysosporium | Malassezia | Fusicolla | Fusarium | Preussia | Aspergillus | Pleurotus |
|---|---|---|---|---|---|---|---|
| Base | 10.9% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] | 26.5% [src: lignin_community_enrichment] | 0.4% [src: lignin_community_enrichment] | 3.0% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] |
| L | <0.1% [src: lignin_community_enrichment] | 4.0% [src: lignin_community_enrichment] | 30.3% [src: lignin_community_enrichment] | 43.4% [src: lignin_community_enrichment] | 12.9% [src: lignin_community_enrichment] | 2.2% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] |
| LC | 61.4% [src: lignin_community_enrichment] | 6.1% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] | 27.2% [src: lignin_community_enrichment] | <0.1% [src: lignin_community_enrichment] |

- Base is Fusarium-dominated (26.5%) with diverse secondary taxa, 253 OTUs (operational taxonomic units) and Shannon=3.50. [src: lignin_community_enrichment]
- In lignin alone (L), Fusarium persists (43.4%) and Fusicolla emerges (30.3%). [src: lignin_community_enrichment]
- In lignin plus labile carbon (LC), the fungal community is completely replaced, with Chrysosporium at 61.4% and Aspergillus at 27.2%. [src: lignin_community_enrichment]
- ITS (internal transcribed spacer) diversity falls from 253 OTUs in Base to 3–8 OTUs per group after enrichment. [src: lignin_community_enrichment]

## Round 2: Malassezia and Pleurotus

Round 2 groups are dominated by few taxa, with Malassezia prominent in two groups and Pleurotus appearing in one. [src: lignin_community_enrichment]

| Group | Dominant taxa (relative abundance) |
|---|---|
| L-L | Malassezia 63.4% [src: lignin_community_enrichment] |
| LC-L | Malassezia 50.0%, Aspergillus 50.0% [src: lignin_community_enrichment] |
| L-LC | Fusicolla 33.3%, Preussia 33.3% [src: lignin_community_enrichment] |
| LC-LC | Malassezia 50.0%, Pleurotus 50.0% [src: lignin_community_enrichment] |

Pleurotus is described as a known lignin-degrading white-rot fungus. [src: lignin_community_enrichment] The report calls it a white-rot basidiomycete and one of the most efficient known lignin degraders. [src: lignin_community_enrichment] It appears in LC-LC only when labile carbon is available in both rounds, and the report treats this as biologically notable despite the replicate problem. [src: lignin_community_enrichment]

## Inference limits

Replicate noise limits what these data can show. Within-group Bray-Curtis (BC) distance for ITS is 0.65, and it reaches 0.99–1.00 for Round 2 groups. [src: lignin_community_enrichment] For several Round 2 groups this compares with 0.09 for 16S, and the report says this limits statistical inference for ITS. [src: lignin_community_enrichment] Enriched groups have only 3–8 OTUs, so their composition may be highly sensitive to stochastic variation. [src: lignin_community_enrichment] The round-2 percentages, such as the 50.0% and 33.3% values, are therefore weak evidence. The Pleurotus result is a single-group observation, not an established effect.

## Open Directions

- Rerun the Round 2 fungal enrichments with more replicates, to test whether Pleurotus in LC-LC and Malassezia dominance recur. This would address the 0.99–1.00 within-group BC.
- Add a quantitative fungal measure alongside ITS relative abundance, such as qPCR or lignin-loss assays. This would show whether Fusarium and Fusicolla, or Chrysosporium and Aspergillus, actually degrade lignin, rather than inferring lifestyle from genus.
- Sequence deeper or pool replicates to see whether the 3–8 OTU groups reflect real selection or stochastic sampling.
