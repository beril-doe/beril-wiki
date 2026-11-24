---
type: "Organism"
description: "Bacterial phylum with the most GH-skewed CAZyme profiles; soil members carry the highest GH counts."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md"]
aliases: ["Bacteroidetes"]
---
# Bacteroidota

This page covers Bacteroidota (also known as Bacteroidetes), a bacterial phylum with the most GH-skewed CAZyme profiles, where soil members carry the highest GH counts. [src: cazyme_pangenome_ecology]

## Key facts

- The AMR pangenome atlas lists 1,835 Bacteroidota species with antimicrobial resistance (AMR), 5,458 total AMR, a mean of 3.0 AMR per species, and 50.6% of species with AMR. [src: amr_pangenome_atlas]
- The gene-flow report's Bacteroidota set has 2,581 species, 8.4× the 309 species of Cyanobacteriia. [src: gene_function_ecological_agora]

## CAZymes and soil specialization

Soil Bacteroidota carried a mean of 65.3 GH genes. This is the highest phylum–biome combination in the report and 2.8× the Bacteroidota average across biomes. [src: cazyme_pangenome_ecology] The report says this fits Bacteroidota's established role as primary polysaccharide degraders, but that the magnitude of soil enrichment had not been quantified at genome-resolved scale. [src: cazyme_pangenome_ecology] It also claims the figure quantifies this specialization at pan-bacterial scale for the first time. [src: cazyme_pangenome_ecology] It presents the work as extending a single-clade, single-biome study to a pan-bacterial, multi-biome comparison. [src: cazyme_pangenome_ecology] See [[entities/glycoside-hydrolases]] and [[concepts/biome-level-carbohydrate-active-enzyme-repertoire-differentiation]].

The report cites outside work consistent with this role:
- Huang et al. (2023) showed a successional role in paddy-soil straw polymer decomposition, with the highest proportion of total GHs and the most CAZyme gene clusters. [src: cazyme_pangenome_ecology]
- Nweze et al. (2024) found Bacteroidota to be the primary agents of complex carbon degradation in arthropod gut microbiomes. [src: cazyme_pangenome_ecology]
- Pudlo et al. (2022) showed wide carbohydrate-utilization variation across 354 gut Bacteroidetes isolates, with CAZyme repertoire diversity driving within-species phenotypic diversification. [src: cazyme_pangenome_ecology]

## CAZymes and pangenome openness

Within Bacteroidota, the CAZy–pangenome openness correlation across 1,618 species was significant (Spearman ρ = 0.147, BH-adjusted p = 1.3 × 10^-8). [src: cazyme_pangenome_ecology] The report describes the correlation between CAZyme density and pangenome openness as weak but real. It suggests that CAZymes are part of the accessory gene pool in particular lineages, especially [[entities/bacillota-a]] and Bacteroidota. [src: cazyme_pangenome_ecology] See [[concepts/pangenome-openness-and-its-correlates]] and [[entities/spearman-rank-correlation]].

## Polysaccharide utilization loci, gene flow and phenotypes

The Phase 1B hypothesis that Bacteroidota are Innovator-Exchange on polysaccharide utilization loci (PULs) received a qualified pass. Deep-rank absolute-zero was falsified, the Sankoff diagnostic recovers, and atlas d=0.15 in NB08c. [src: gene_function_ecological_agora] Bacteroidota (n=2,581) were 36.1% gut/rumen versus 25.8% of the atlas, a 1.40× enrichment with Fisher p < 10⁻³⁵. [src: gene_function_ecological_agora] Across 439,968 Bacteroidota genus × candidate-KO tuples, M26 labels 56.5% (248,581) Open-Innovator, 4.5% (19,663) Broker, 5.4% (23,612) Sink and 33.7% (148,112) Insufficient. [src: gene_function_ecological_agora] See [[concepts/clade-level-innovation-signals-and-their-rank-dependence]] and [[concepts/ecological-and-phenotypic-grounding-of-gene-flow-signatures]].

The BacDive phenotype check (NB24, n=577 species) matches PUL biology: [src: gene_function_ecological_agora]
- Gram stain was negative for 339 records and positive for 4. [src: gene_function_ecological_agora]
- 33.2% were anaerobes versus 22.0% atlas-wide (1.5× enriched, despite type-strain culture bias toward aerobes), and 48.7% were aerobes. [src: gene_function_ecological_agora]
- Maltose (230+), raffinose (155+), esculin (228+), cellobiose, glucose and lactose were utilized. The report calls this the strongest available BacDive anchor for the Phase 1B PUL Innovator-Exchange finding. [src: gene_function_ecological_agora]
- The top enzymes were leucyl-aminopeptidase (415), β-galactosidase (391), α-galactosidase (340), β-glucosidase (339) and β-N-acetylhexosaminidase (299), a glycoside-hydrolase-rich profile. [src: gene_function_ecological_agora]

In NB25, Bacteroidota (n_AE=729) were spread across clusters 0/1/3 (~18% each). The report interprets this as diverse environment occupation matching a wide gut and marine niche range. [src: gene_function_ecological_agora]

Summaries: [[summaries/amr_pangenome_atlas__REPORT]], [[summaries/cazyme_pangenome_ecology__REPORT]], [[summaries/gene_function_ecological_agora__REPORT]].
