---
type: "Concept"
description: "Covers how biome enrichment, BacDive phenotypes and environmental embeddings were used to test whether atlas findings match expected habitats, and the limits of such association evidence."
sources: ["summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md"]
---
# Ecological and phenotypic grounding of gene-flow signatures

This page covers how biome enrichment, BacDive phenotypes and environmental embeddings were used in the gene_function_ecological_agora project to test whether atlas findings match expected habitats. All three pre-registered atlas findings grounded in expected biomes at p < 10⁻¹¹. [src: gene_function_ecological_agora] Two of three were also confirmed by BacDive phenotype anchors, and three of three by AlphaEarth environmental-cluster concentration. [src: gene_function_ecological_agora] The evidence is association only, and coverage differs by substrate. [src: gene_function_ecological_agora] The report itself softens its wording: "ecology grounding" becomes "ecology consistency" or "ecology anchoring", and "grounded in" becomes "consistent with" the expected biome. [src: gene_function_ecological_agora]

## Substrates and coverage

The KBase Data Lakehouse offered several ecological substrates. ncbi_env gave 88.8% biosample geographic coverage. [src: discoveries] kescience_mgnify gave 28.4% categorical biome coverage. [src: discoveries] kescience_bacdive gave 32% phenotype coverage via GCF→GCA fallback. [src: discoveries] kescience_fitnessbrowser gave BBH (bidirectional best hit) coverage for ~30 organisms. [src: discoveries] See [[entities/kbase-data-lakehouse]], [[entities/kescience-mgnify]], [[entities/bacdive]], [[entities/ncbi-env-environmental-metadata]] and [[entities/fitness-browser]].

In the project, AlphaEarth 64-dim satellite-imagery embeddings covered 27% of atlas species. [src: gene_function_ecological_agora] P4-D1 used MGnify biome labels (28% species coverage, 18 biome categories). [src: gene_function_ecological_agora] See [[entities/alphaearth-environmental-embeddings]].

## Convergence of three substrates

Each pre-registered finding (NB12 mycolic, NB16 PSII (photosystem II), Phase 1B Bacteroidota PUL (polysaccharide utilization locus)) had convergent evidence from atlas Cohen's d on Sankoff-derived scores, clade-by-biome Fisher's enrichment (p<10⁻¹¹) and BacDive phenotypes where coverage existed. [src: discoveries] The report argues that this makes a clade-level verdict robust against single-substrate failure. [src: discoveries, gene_function_ecological_agora] It also says a finding in any single layer would be circumstantial. [src: gene_function_ecological_agora] The three-substrate framework (atlas + ecology + phenotype) gives convergent evidence from independent measurement substrates, but it does not establish causation. [src: gene_function_ecological_agora] See [[concepts/clade-level-innovation-signals-and-their-rank-dependence]].

## Biome enrichment

NB23 assigned biomes to 18,989 P1B species representatives, with MGnify first, ENVO (Environment Ontology) second and isolation_source third. It ran one-sided Fisher's exact tests against the atlas distribution. [src: gene_function_ecological_agora] Headline results were Cyanobacteriia 2.77× photic aquatic (p<10⁻⁵²), Mycobacteriaceae 7.88× host-pathogen (p<10⁻⁴⁵) and Bacteroidota 1.40× gut/rumen (p<10⁻³⁵). [src: gene_function_ecological_agora]

| Clade (n) | Biome | Clade | Atlas | Fold | Fisher p |
|---|---|---|---|---|---|
| Cyanobacteriia (309) | photic aquatic | 63.8% | 23.0% | 2.77× | < 10⁻⁵² [src: gene_function_ecological_agora] |
| Cyanobacteriia (309) | marine | 35.3% | 15.1% | 2.33× | < 10⁻¹⁸ [src: gene_function_ecological_agora] |
| Mycobacteriaceae (459) | host-pathogen | 16.6% | 2.1% | 7.88× | < 10⁻⁴⁵ [src: gene_function_ecological_agora] |
| Mycobacteriaceae (459) | soil | 12.9% | 14.5% | 0.88× | 0.87, not enriched [src: gene_function_ecological_agora] |
| Mycobacteriaceae (459) | soil or host-pathogen | 29.0% | 16.4% | 1.76× | < 10⁻¹¹ [src: gene_function_ecological_agora] |
| Bacteroidota (2,581) | gut/rumen | 36.1% | 25.8% | 1.40× | < 10⁻³⁵ [src: gene_function_ecological_agora] |

A phylum-level sanity check matched established ecology. Cyanobacteriota were 33.2% marine and 60.7% photic. [src: gene_function_ecological_agora] Bacillota_A (Clostridia) were 81.0% gut/rumen. [src: gene_function_ecological_agora] Bacteroidota were 36.1% gut/rumen. [src: gene_function_ecological_agora] Verrucomicrobiota were 65.6% photic. [src: gene_function_ecological_agora] Planctomycetota were 38.7% marine. [src: gene_function_ecological_agora] Chloroflexota were 47.0% photic. [src: gene_function_ecological_agora]

### Soil null for mycobacteria

The soil enrichment was null, so the mycolic-acid Innovator-Isolated signature concentrates in host-pathogen mycobacteria, not soil mycobacteria. [src: gene_function_ecological_agora] The MGnify breakdown for [[entities/mycobacteriaceae]] was 53 human-skin, 16 human-vaginal, 15 human-gut and 11 chicken-gut species. [src: gene_function_ecological_agora] The report attributes the failed soil enrichment to clinical-isolate skew among species representatives. [src: gene_function_ecological_agora]

## BacDive phenotype anchors

BacDive anchors confirmed mycobacterial aerobic-rod and Bacteroidota saccharolytic profiles. [src: gene_function_ecological_agora] Coverage was 32% of atlas species. [src: gene_function_ecological_agora] In NB24, the Mycobacteriota mycolic-acid anchors were described as aerobic-rod, Gram+ and catalase (n=318). [src: gene_function_ecological_agora] The Bacteroidota PUL anchors were saccharolytic and GH-rich (n=577). [src: gene_function_ecological_agora]

- Mycobacteriaceae Gram stain was positive 171 / negative 1. [src: gene_function_ecological_agora] Cell shape was rod-shaped 194/216 (95%). [src: gene_function_ecological_agora] Motility was non-motile 195/196 (99%). [src: gene_function_ecological_agora]
- Mycobacteriaceae were 89.4% aerobic-leaning (aerobe 40.9% + obligate aerobe 31.1% + microaerophile 17.4%). [src: gene_function_ecological_agora] Catalase EC (Enzyme Commission) 1.11.1.6 appeared at 317 instances, read as an aerobic marker. [src: gene_function_ecological_agora]
- [[entities/bacteroidota]] were 33.2% anaerobe versus 22.0% atlas-wide, 1.5× enriched despite type-strain culture bias toward aerobes. They were also 48.7% aerobe. [src: gene_function_ecological_agora]
- Bacteroidota utilized maltose (230+), raffinose (155+) and esculin (228+), plus cellobiose, glucose and lactose. The report calls this the strongest available BacDive anchor for the PUL finding. [src: gene_function_ecological_agora]
- Top Bacteroidota enzymes were leucyl-aminopeptidase (415), β-galactosidase (391), α-galactosidase (340), β-glucosidase (339) and β-N-acetylhexosaminidase (299), a glycoside-hydrolase-rich profile. [src: gene_function_ecological_agora]

Cyanobacteriia could not be anchored this way, because BacDive covered only n=4 species. [src: gene_function_ecological_agora] Their anchoring rests on biome association (p < 10⁻⁵²) and environmental-cluster concentration. [src: gene_function_ecological_agora] The Cyanobacteria PSII table lists environmental cluster 0 as marine 35.6% (NB25). [src: gene_function_ecological_agora]

## AlphaEarth environmental clusters

AlphaEarth clustering recovered ecological structure, with focal clades concentrated in expected clusters. [src: gene_function_ecological_agora] Example NB25 clusters:

- Cluster 0 (n=818): marine, sponge tissue and hypoxic seawater. [src: gene_function_ecological_agora]
- Cluster 1 (n=812): chicken-gut, human-gut and activated sludge. [src: gene_function_ecological_agora]
- Cluster 3 (n=684): mouse-gut, pig-gut and groundwater. [src: gene_function_ecological_agora]
- Cluster 4 (n=328): sheep-rumen, stool and rumen. [src: gene_function_ecological_agora]
- Cluster 6 (n=228): hypersaline soda lake sediment and Microcystis lake. [src: gene_function_ecological_agora]
- Cluster 9 (n=203): soil, temperate grassland, groundwater and meadow soil. [src: gene_function_ecological_agora]

Clade placements matched expectations:

- Cyanobacteriia (n_AE=90) had 35.6% in cluster 0 and 17.8% in clusters 5+8. [src: gene_function_ecological_agora]
- Mycobacteriaceae (n_AE=50) had 34.0% in cluster 1 and 20.0% in cluster 3. [src: gene_function_ecological_agora]
- Bacteroidota (n_AE=729) spread across clusters 0/1/3 (~18% each). [src: gene_function_ecological_agora]

Mixed-biome clusters 5 and 8 carried the highest recent-gain density. Cluster 6, a hypersaline/extremophile niche, carried the lowest. [src: gene_function_ecological_agora] The report reads this as consistent with literature that generalists have higher HGT (horizontal gene transfer) rates than extremophile specialists, and with Innovator-Exchange dominance. [src: gene_function_ecological_agora]

## Limits of association evidence

The confirmed hypotheses are anchored to expected biomes at p < 10⁻¹¹. [src: gene_function_ecological_agora] These enrichments show statistical association, not causal mechanisms. The report leaves open whether environment drives innovation, innovation drives niche occupancy, or a third factor drives both. [src: gene_function_ecological_agora] This is why the report prefers "consistent with" to "grounded in". [src: gene_function_ecological_agora] P4-D1 did not query MGnify per-sample taxa-coverage matrices, which the report names as a future direction for finer ecological inference. [src: gene_function_ecological_agora]

## Open Directions

- Query MGnify per-sample taxa-coverage matrices to test the biome associations at finer resolution. This addresses the 28% categorical coverage limit.
- Re-test the mycobacterial soil null with a species set less skewed toward clinical isolates. This would check the explanation given for the failure.
- Add phenotype data for Cyanobacteriia beyond BacDive's n=4 species. This would close the one clade lacking a phenotype anchor.
- Test the direction of causation, for example by comparing gain timing with niche occupancy. This targets the unresolved causal question.
