<!-- tension-hash: e8c99f99e98abece -->
# Clade-Level Versatility Versus Lignin Enrichment Winners: A Tension in Aromatic Catabolism

Two projects describe which bacteria handle aromatic compounds, and their taxa do not line up neatly. A genome-based census (the ENIGMA Carbon Census) calls versatility a Burkholderiales clade trait. [src: enigma_carbon_census_1] A lignin enrichment experiment raised Pseudomonas, Acinetobacter and Flavobacterium strongly. [src: lignin_community_enrichment] The census also finds sphingomonads with 4-hydroxybenzaldehyde capacity at ~92–100% of called genomes [src: enigma_carbon_census_1], yet Sphingomonas was not selected by lignin enrichment. [src: lignin_community_enrichment] This matters because [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]] rests on a clade pattern inferred from genomes and taxonomy, and it is unclear how far that pattern predicts which organisms win in real communities.

## Evidence Sides

**Genome-called capacity (census)**

- The census calls versatility a Burkholderiales clade trait. [src: enigma_carbon_census_1]
- Sphingomonads carry 4-hydroxybenzaldehyde capacity at ~92–100% of called genomes. [src: enigma_carbon_census_1]
- The denominator differs from the enrichment data, so this is a contrast and not a contradiction. [src: enigma_carbon_census_1]

**Community enrichment (lignin)**

- Lignin enrichment raised Pseudomonas, Acinetobacter and Flavobacterium strongly. [src: lignin_community_enrichment]
- Sphingomonas was not selected by lignin enrichment. This is an absence of selection in 16S abundance (16S rRNA gene sequencing of community composition), not a measured lack of capacity. [src: lignin_community_enrichment]

The two datasets measure different things, genome-called capacity versus 16S abundance, so they are not directly comparable.

## Possible Reconciliations

- **Hypothesis: capacity is not enrichment fitness.** Having a catabolic gene set may not make a taxon win in lignin culture, where growth rate, tolerance of toxic intermediates or cross-feeding could matter more. Neither source tests this.
- **Hypothesis: lignin selects different substrates than the census scores.** Lignin breakdown may release aromatics outside the capacities the census calls, favouring Pseudomonas, Acinetobacter and Flavobacterium.
- **Hypothesis: denominator artefact.** The sphingomonad fraction is taken over called genomes, so it may not reflect absolute prevalence. Sphingomonas may be rare in the starting community.

None of these is preferred here, and the two sides are not averaged.

## Resolving Work

- Score the genomes of the enriched Pseudomonas, Acinetobacter and Flavobacterium taxa with the census capacity-calling pipeline. Question: do they carry called aromatic capacity, and is it counted as clade-level versatility?
- Use 16S taxonomy to estimate how many Sphingomonas are in the unenriched lignin community. Question: was Sphingomonas absent or too rare to be selected?
- Run a shotgun metagenome of the lignin-enriched communities and call aromatic pathways. Question: does community capacity match genome-called capacity by clade?
- Culture sphingomonad and Burkholderiales isolates on lignin or 4-hydroxybenzaldehyde. Question: does predicted capacity translate into growth under lignin conditions?
- Recompute census conservation fractions over all genomes of each genus, not only called genomes. Question: does the sphingomonad pattern hold with a common denominator?
