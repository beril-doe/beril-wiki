---
type: "Concept"
description: "Covers how many candidate carbon compounds lack a linkable utilization determinant in queried resources, why they are dark, and how to prioritize them; it stops at the claim that dark means unlinked, not unknown to science."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Resource-darkness of compound catabolism

Covers how many candidate carbon compounds lack a linkable utilization determinant in queried resources, why they are dark, and how to prioritize them; it stops at the claim that dark means unlinked, not unknown to science.

## Literature Context

The candidate papers show that bacterial catabolism of unusual organic compounds is often class-specific and is usually resolved compound by compound. Reviews describe dedicated pathways for halogenated organics [PMID 9891928](https://pubmed.ncbi.nlm.nih.gov/9891928/), for dimethylsulfoniopropionate [PMID 28683918](https://pubmed.ncbi.nlm.nih.gov/28683918/), and for s-triazine herbicides [PMID 32408946](https://pubmed.ncbi.nlm.nih.gov/32408946/). Rhodococcus is described as catabolically diverse, with catabolic genes believed to spread through recombination on large plasmids [PMID 29913546](https://pubmed.ncbi.nlm.nih.gov/29913546/). A review of phosphonate and ribonucleotide metabolism reports that pathways for ribosyl 1,5-bisphosphate were found experimentally or by bioinformatic analysis [PMID 30567937](https://pubmed.ncbi.nlm.nih.gov/30567937/).

Phenylpropanoid and lignin-derived aromatics are the closest match to the corpus's dark shikimate/phenylpropanoid class. Several studies resolved previously unknown pathways in single, already isolated organisms. Genome-wide screens identified genes for the β-5 linked dimer dehydrodiconiferyl alcohol in Novosphingobium aromaticivorans, and a comparative genomic analysis predicted the pathway to be common within the order Sphingomonadales [PMID 39012147](https://pubmed.ncbi.nlm.nih.gov/39012147/). A barcoded transposon library identified genes for pinoresinol catabolism in Novosphingobium rhizosphaerae LY [PMID 40990490](https://pubmed.ncbi.nlm.nih.gov/40990490/). Rhodococcus jostii RHA1 catabolism of p-methoxylated aromatics revealed previously unknown roles for known enzymes, including vanillin dehydrogenase and vanillate O-demethylase [PMID 38380926](https://pubmed.ncbi.nlm.nih.gov/38380926/). Sphingobium sp. SYK-6 handles all four β-1-type stereoisomers through multiple dehydrogenases [PMID 37184397](https://pubmed.ncbi.nlm.nih.gov/37184397/). Halomonas isolates carry β-ketoadipate pathway ring-cleaving genes, detected by PCR with degenerate primers [PMID 16329976](https://pubmed.ncbi.nlm.nih.gov/16329976/). These studies report pathway discovery in known strains by genetic screens, not anonymous community enrichment or metagenomics.

The corpus's central claim is that 74 of 83 compounds (89%) are organism-dark, meaning unlinked in the queried resources. This is consistent with the literature above. Catabolic routes for plant-derived phenylpropanoids were still being worked out recently, and the pinoresinol paper itself notes that relatively little is known about β-β-linked compounds [PMID 40990490](https://pubmed.ncbi.nlm.nih.gov/40990490/). The hub's position that dark means unlinked rather than unknown fits reviews showing class-level knowledge for other compound families. It also fits the finding that some enzymes act on several substrates and some steps have several enzymes [PMID 39012147](https://pubmed.ncbi.nlm.nih.gov/39012147/). Such redundancy and promiscuity could hide determinants from annotation-based linking.

The lignin papers support one part of the hub's prioritization: dark compounds in the shikimate/phenylpropanoid class can be resolved by genome-wide genetic screens in organisms known to grow on them. They do not test the hub's proposal to start the 29 fully orphan compounds with anonymous enrichment and metagenomics, so that proposal remains untested here. The candidates do not address the hub's necromass skew (13/24 orphan against 16/59 groundwater), the six biosynthesis-known compounds, or the zero-rescue PubMed-title screen. The hub's alkaloid and terpenoid claims also lack direct support in this set. The remaining candidates (exercise and the gut microbiome, molecular docking, lipid droplets, anaerobes in general) are not relevant.

## How dark is the census

The census labels 74 of 83 compounds (89%) organism-dark. Their genetic determinants of utilization are not linkable through the queried the KBase Data Lakehouse and curated resources. [src: enigma_carbon_census_1] One table lists 75 pre-I1 dark compounds. Lauric acid was later reclassified as callable, which leaves 74 dark in the master table. [src: enigma_carbon_census_1]

## Why compounds are dark

The report sorts the 74 post-I1 dark compounds into four buckets: [src: enigma_carbon_census_1]

| Bucket | Compounds |
|---|---|
| KEGG-linked, no reaction in genomes | 33 [src: enigma_carbon_census_1] |
| Fully orphan (no KEGG link) | 29 [src: enigma_carbon_census_1] |
| Biosynthesis-known, catabolism-unknown | 6 [src: enigma_carbon_census_1] |
| Only generic reactions | 6 [src: enigma_carbon_census_1] |

The six biosynthesis-known compounds are tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid and farnesol. They carry biosynthetic-direction signatures but no catabolic call. [src: enigma_carbon_census_1]

By class, alkaloids, shikimates/phenylpropanoids, terpenoids and fatty acids dominate the dark set, as the report predicted. [src: enigma_carbon_census_1] The fully orphan compounds skew toward necromass: 13/24 necromass compounds are orphan, against 16/59 groundwater compounds. [src: enigma_carbon_census_1]

Darkness tracks chemical class, not sampling source. The dark fraction is 53/59 (90%) in groundwater and 21/24 (88%) in necromass. [src: enigma_carbon_census_1] See also [[concepts/confounding-of-compound-source-with-chemical-class]].

## Dark does not mean unknown

Class-level catabolic literature exists for monoterpenes and for alkaloids such as nicotine. [src: enigma_carbon_census_1] The census's literature-rescue channel (NB02b) returned zero rescues. It used only a PubMed-title screen, which the report calls a method floor, not evidence of absence. [src: enigma_carbon_census_1] The report expects a PaperBLAST or abstract-level pass to reclassify part of the dark set. [src: enigma_carbon_census_1]

## Prioritizing dark compounds

It ranks the 74 compounds as discovery-mode enrichment targets by why they are dark. [src: enigma_carbon_census_1]

- Start the 29 fully orphan compounds, especially the necromass-heavy alkaloids and terpenoids, with anonymous community enrichment and metagenomics. [src: enigma_carbon_census_1]
- Send the 6 biosynthesis-known compounds to a separate MIBiG/biosynthetic-literature consult before wet-lab work. That consult is external, because MIBiG was not queried in the KBase Data Lakehouse. [src: enigma_carbon_census_1]
- Mine the literature with targeted PaperBLAST/PubMed searches for alkaloid and terpenoid catabolic enzymes, then search the hits back into the genomes. This would promote some compounds from Tier 5 to Tier 3 (callable) without new experiments. [src: enigma_carbon_census_1]

## Open Directions

- Run an abstract-level PaperBLAST pass on the 74 dark compounds, starting with the alkaloids and terpenoids. This tests how many the title-only screen missed.
- Query MIBiG for the six biosynthesis-known compounds. This would show whether any has a known catabolic route.
- For the 33 KEGG-linked compounds with no reaction in genomes, search for homologs of reactions in the linked KEGG entries. This would show whether the gap lies in the genomes or in the annotation.
- Test whether the necromass skew in the orphan bucket holds once chemical class is controlled for.
