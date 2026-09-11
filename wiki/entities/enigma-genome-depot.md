---
type: "Dataset"
description: "Dataset linking ENIGMA isolates, genomes, annotations, and utilization phenotypes"
sources: ["summaries/enigma_carbon_census_1__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# ENIGMA Genome Depot

## What this entity is

**Canonical name:** ENIGMA Genome Depot  
**Known aliases:** ENIGMA genome-depot; genome-depot  
**Stable external identifier:** No stable external identifier was reported in the source. [src: enigma_carbon_census_1]

ENIGMA Genome Depot is a genome resource used in the ENIGMA Carbon Census to connect compound-utilization predictions with genome annotations and ENIGMA-isolate records. [src: enigma_carbon_census_1] The newer genotype-to-phenotype study **supports** this role by integrating the Depot with ENIGMA growth curves, pangenome data, Fitness Browser RB-TnSeq data, Web of Microbes exometabolomics, Carbon Source Phenotypes, and global 16S environmental data for genome-by-condition phenotype modeling. [src: genotype_to_phenotype_enigma]

## Key facts from the ENIGMA Carbon Census

The census integrated ENIGMA Genome Depot with PubChem, KEGG, ModelSEED, the Fitness Browser, GTDB, SSO, NMDC, and Planet Microbe in a tiered compound-to-environment workflow. [src: enigma_carbon_census_1]

The analysis evaluated 83 enrichment compounds across 3109 genomes and identified 8 compounds with ENIGMA-isolate utilization calls. [src: enigma_carbon_census_1]

The ENIGMA-isolate deliverable contained 569 utilization-prediction rows across the 8 ENIGMA-isolate-callable compounds. [src: enigma_carbon_census_1]

The utilization predictions included 129 strains for salicylic acid, 127 for 3-hydroxybenzoic acid, 125 for 4-hydroxybenzaldehyde, 36 for phthalic acid, 34 for terephthalic acid, 28 for phenylethylamine, 13 for xanthine, and 2 for abscisic acid. [src: enigma_carbon_census_1]

The census placed 494 strain records representing 359 distinct strains on GTDB taxonomy, including 64 high-certainty records based on gene-complete Tier-2 pathways, 387 medium-certainty records based on Tier-2 pathways, and 43 medium-certainty records based on Tier-3 signature enzymes. [src: enigma_carbon_census_1]

Utilizer predictions were concentrated in Pseudomonadota and Burkholderiales, with additional compound-specific contributions from Pseudomonadales and Sphingomonadales; 47 Sphingomonadales strains were associated with 4-hydroxybenzaldehyde. [src: enigma_carbon_census_1]

Terephthalic acid had 34/34 high-certainty records, although the source identified this as a possible single-reaction-signature artifact rather than evidence of complete pathway coverage. [src: enigma_carbon_census_1]

The source cautioned that certainty was calculated from the raw number of carried signature reactions divided by required reactions and was not directly comparable across compounds with different signature lengths. [src: enigma_carbon_census_1]

## Integration and linkage validation

The new study **refines** the Depot’s cross-resource role by placing its genome and annotation records in a combined modeling corpus of 46,389 genome-by-condition pairs spanning 727 genomes, 363 conditions, and 4,293 shared [[entities/kegg]] orthologs (KOs). [src: genotype_to_phenotype_enigma]

It also identifies a data-integration hazard: matching ENIGMA strains to the KBase Data Lakehouse pangenome through short identifiers such as MT20 caused 12 of 32 genus-level mismatches, including a Rhodanobacter glycinis–[[entities/streptococcus-pneumoniae]] collision that introduced 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma] Using CORAL brick 522 GTDB-Tk assignments and genus-consistency checks reduced verified linkages from 32 to 20 and eliminated all false matches, **supporting** stricter identity validation for Depot-linked analyses. [src: genotype_to_phenotype_enigma]

## Related pages

The dataset contributes to [[concepts/pangenome-integration]] by linking genome annotations across 3109 genomes to isolate-level utilization predictions and GTDB strain placements. [src: enigma_carbon_census_1]

It participates in [[concepts/cross-tenant-data-bridging]] alongside [[entities/gtdb]], [[entities/kescience-fitnessbrowser]], [[entities/modelseed]], and other cross-resource datasets. [src: enigma_carbon_census_1] The genotype-to-phenotype study **strengthens** this connection by documenting both multi-tenant phenotype integration and the strain-name collision risk. [src: genotype_to_phenotype_enigma]

The source documents are [[summaries/enigma_carbon_census_1__REPORT]] and [[summaries/genotype_to_phenotype_enigma__REPORT]].
