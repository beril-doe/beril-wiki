---
type: "Concept"
description: "How T4SS-CAZy co-occurrence is distributed across environmental biomes (marine sediment, crop rhizospheres) and how robust that enrichment is to validation splits and pending null baselines; stops at the biome-level association."
sources: ["summaries/t4ss_cazy_environmental_hgt__REPORT.md"]
---
# Environmental biome enrichment of mobile CAZy gene content

This page covers the environmental biome enrichment of mobile CAZy gene content. Marine sediment and two crop rhizospheres show enrichment of T4SS (type IV secretion system)–CAZy co-occurrence, and the evidence is preliminary. [src: t4ss_cazy_environmental_hgt] The enrichment replicates across a discovery/validation split, but several null and validation checks are still pending. [src: t4ss_cazy_environmental_hgt] See [[summaries/t4ss_cazy_environmental_hgt__REPORT]] for the full report and [[concepts/horizontal-transfer-of-carbohydrate-active-enzymes-via-conjugative-machinery]] for the transfer hypothesis.

## Literature Context

The candidate papers give examples of horizontal gene transfer (HGT) involving carbohydrate-active enzyme (CAZy) genes or carbohydrate-metabolism genes in several organisms and settings. They do not show how often CAZy genes are acquired horizontally in general, and they do not test whether acquisition varies by habitat. In the soil invertebrate Folsomia candida, a glycosyl hydrolase family 43 gene was likely acquired from a bacterial donor. The expressed protein was active against p-nitrophenyl-α-L-arabinofuranoside [PMID 36011312](https://pubmed.ncbi.nlm.nih.gov/36011312/). In rumen protozoa, codon usage analysis suggested that many expressed CAZymes were acquired from rumen bacteria [PMID 32411103](https://pubmed.ncbi.nlm.nih.gov/32411103/). The Entodinium caudatum macronuclear genome likewise contains many CAZymes that were likely acquired through HGT [PMID 33722656](https://pubmed.ncbi.nlm.nih.gov/33722656/). Some catalytic domains of anaerobic fungal cellulosomes also appear to have originated by HGT from gut bacteria [PMID 28555641](https://pubmed.ncbi.nlm.nih.gov/28555641/).

Several studies tie mobile or horizontally acquired content to a particular environment. In pit-mud Clostridium (30 pit mud-associated and 100 non-pit mud-associated strains), GH4 and GH13 genes were enriched in the pit-mud strains. HGT analysis separately found that multiple carbohydrate and amino-acid metabolism genes had moved from Bacillus to Clostridium. The abstract does not say that the enriched CAZymes were the transferred genes [PMID 35491831](https://pubmed.ncbi.nlm.nih.gov/35491831/). A survey of 2458 ruminant metagenomes found 4,764,110 mobile genetic elements. GH1-carrying plasmids predominated in the stomach of a validation cohort and responded to forage-based diets [PMID 40652256](https://pubmed.ncbi.nlm.nih.gov/40652256/). Daqu metagenomes show phage-to-bacteria HGT, but the abstract links it to flavour and community regulation, not to CAZy content [PMID 37814055](https://pubmed.ncbi.nlm.nih.gov/37814055/). In infant guts, acquired resistance genes increased with age alongside more HGT. Shifts in carbohydrate metabolism were reported separately, so the abstract does not show enrichment of horizontally acquired CAZy content [PMID 38882494](https://pubmed.ncbi.nlm.nih.gov/38882494/). Bifidobacterium breve work is a cautionary example. A resistance gene sits in a putative genomic island, yet conjugation experiments detected no transfer in vitro [PMID 29500262](https://pubmed.ncbi.nlm.nih.gov/29500262/).

Against this background, the corpus reports that marine sediment (OR=5.5, q<10⁻⁹⁸), barley rhizosphere (OR=10.4) and maize rhizosphere (OR=4.1) show enriched T4SS-CAZy co-occurrence. This is consistent in general direction with the candidate papers: mobile elements and CAZy-related HGT are linked to specific environments there too. The corpus differs in kind from those studies. It uses a type IV secretion system (T4SS) co-occurrence signal measured across biomes. The candidates mostly use genome comparisons, metagenomic surveys or single-gene functional work, and none addresses T4SS or these biomes. The biome findings therefore go beyond these papers, and the candidate set neither confirms nor contradicts them. The hub's own caveats still apply. The analysis is preliminary and observational. The housekeeping-gene null baseline, the synteny threshold permutation test and the θ factorisation are pending. The 70/30 discovery/validation replication is the only robustness check reported so far.

The ruminant plasmid result is the closest analogue to the hub's mobile-CAZy hypothesis [PMID 40652256](https://pubmed.ncbi.nlm.nih.gov/40652256/). Even there, the evidence is an enrichment pattern in metagenomes. It does not show a transfer mechanism.

## Biome-level enrichment

The report gives odds ratios (OR) for three biomes. Marine sediment has OR=5.5 with q<10⁻⁹⁸. [src: t4ss_cazy_environmental_hgt] Barley rhizosphere has the largest value, OR=10.4. [src: t4ss_cazy_environmental_hgt] Maize rhizosphere has OR=4.1. [src: t4ss_cazy_environmental_hgt] The claims give a q-value only for marine sediment, so I do not compare significance across biomes.

## Robustness

Enrichment patterns replicate across a 70/30 discovery/validation split. The report reads this as confirming robustness. [src: t4ss_cazy_environmental_hgt] The synteny threshold permutation test and the housekeeping gene null baseline are still pending. [src: t4ss_cazy_environmental_hgt]

## Caveats

- The analysis is preliminary. Core analyses (NB01–NB04) are complete, while NB05 threshold validation and NB06 manuscript figures are pending. [src: t4ss_cazy_environmental_hgt]
- All associations are observational. Mechanistic confirmation requires experimental validation. [src: t4ss_cazy_environmental_hgt]
- The synteny threshold permutation test is pending and requires Spark unfiltered data. [src: t4ss_cazy_environmental_hgt]
- A housekeeping gene null baseline is pending. [src: t4ss_cazy_environmental_hgt]
- A biome enrichment factorisation is pending, defined as θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)]. [src: t4ss_cazy_environmental_hgt]

## Open Directions

- Run the housekeeping gene null baseline to test whether biome ORs exceed those expected for non-mobile genes.
- Compute θ for each biome (marine sediment, barley rhizosphere, maize rhizosphere). This would separate joint T4SS-CAZy enrichment from the enrichment of each component alone.
- Run the synteny threshold permutation test on Spark unfiltered data. This would show whether the ORs depend on the threshold chosen.
- Report q-values for the rhizosphere ORs, and compare the pattern with [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]].
