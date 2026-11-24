---
type: "Organism"
description: "Genus that is the most ambiguous in the genus-to-clade bridge, mapping to 433 GTDB clades."
sources: ["summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/lab_field_ecology__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
aliases: ["P. avellanae", "P. fluorescens", "Pseudomonas (GTDB Pseudomonas_E)", "Pseudomonas sensu stricto", "Pseudomonas_E", "pseudomonas"]
---
# Pseudomonas

Pseudomonas is a bacterial genus, also written pseudomonas, Pseudomonas sensu stricto, Pseudomonas_E (GTDB), P. fluorescens or P. avellanae in the reports. It is the most ambiguous genus in the [[entities/genus-to-species-clade-taxonomy-bridge]], mapping to 433 GTDB clades. [src: enigma_contamination_functional_potential]

## Key facts

- The bridge clade-count distribution has a long right tail, with a maximum of 433 clades per genus. [src: enigma_contamination_functional_potential]
- The top ambiguous genera are pseudomonas (433), streptomyces (378), prevotella (358), streptococcus (214) and mycobacterium (186). [src: enigma_contamination_functional_potential]
- One report extracted [[entities/gapmind]] carbon pathway predictions for 12,732 genomes across 433 Pseudomonas species clades defined by GTDB r214. [src: pseudomonas_carbon_ecology] See [[entities/gtdb]].
- In the Microbial Atlas context, Pseudomonas occurs in 206K samples, after Caulobacter (289K) and Rhodanobacter (228K). [src: genotype_to_phenotype_enigma]

## Taxonomy and subgroups

The carbon-ecology report uses Pseudomonas sensu stricto for the P. aeruginosa group and Pseudomonas_E for the P. fluorescens/putida group. [src: pseudomonas_carbon_ecology] The genus spans 5 GTDB subgenera. [src: pseudomonas_carbon_ecology] Pseudomonas s.s. has 19 species and 6,905 genomes, mainly P. aeruginosa. [src: pseudomonas_carbon_ecology] Pseudomonas_E has 398 species and 5,687 genomes from the P. fluorescens, P. putida and P. syringae groups. [src: pseudomonas_carbon_ecology] A plant-microbiome report instead counts 358 species for Pseudomonas_E. [src: plant_microbiome_ecotypes]

## Carbon metabolism

The P. fluorescens/putida group has greater carbon pathway breadth (mean richness 56.1) than P. aeruginosa (mean richness ~50), particularly for sugar and sugar alcohol catabolism. [src: pseudomonas_carbon_ecology] Pseudomonas s.s. shows near-complete loss of plant-derived sugar catabolism compared with Pseudomonas_E. [src: pseudomonas_carbon_ecology] See [[concepts/host-adaptation-pathway-loss-in-pseudomonas-carbon-catabolism]] and [[concepts/carbon-pathway-profiles-as-predictors-of-environment-and-lifestyle]].

Earlier work by Silby et al. (2011) and Loper et al. (2012) highlighted metabolic diversity in P. fluorescens group genomes, with ~54% of the pangenome encoding variable metabolic capabilities. [src: pseudomonas_carbon_ecology] Ghirardi et al. (2012) associated rhizosphere competence in fluorescent pseudomonads with catabolic profile diversity. [src: pseudomonas_carbon_ecology] The report claims to be the first systematic quantification of standardized carbon pathway profiles across the full breadth of Pseudomonas (433 species, 12,732 genomes). [src: pseudomonas_carbon_ecology]

## ENIGMA and field context

All ENIGMA Pseudomonas belong to Pseudomonas_E, the fluorescens/protegens clade, which is environmental rather than clinical. [src: genotype_to_phenotype_enigma] Across all GTDB genomes, Pseudomonas is 37.8% clinical (driven by P. aeruginosa), 12.9% soil/plant and 9.4% aquatic. [src: genotype_to_phenotype_enigma] See [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

ENIGMA Pseudomonas anchor strains show 43-61% growth across conditions and are described as metabolic generalists. [src: genotype_to_phenotype_enigma] The Pseudomonas_E guild has 27 strains and an average of 2,658 KOs (KEGG orthologs). It contains 5 of 7 Fitness Browser (FB) anchor strains and is the best-sampled guild for modeling. [src: genotype_to_phenotype_enigma] See also [[entities/pseudomonas-fluorescens]].

At Oak Ridge, Pseudomonas was detected at 91% of sites. [src: lab_field_ecology] It showed no correlation with uranium (rho=-0.059, p=0.55), despite being an ENIGMA model organism. [src: lab_field_ecology] See [[entities/uranium]]. The report cautions that 16S amplicon data resolve only to genus, while FB organisms are specific strains. Pseudomonas contains thousands of species with vastly different ecologies. [src: lab_field_ecology] See [[concepts/genus-level-amplicon-resolution-and-rare-taxon-limits-in-matching-reference-organisms-to-field-data]].

## Lignin enrichment

Pseudomonas is absent in the base community (<0.1%) but dominant in all enriched bacterial conditions (23–53%). [src: lignin_community_enrichment] After one lignin-enrichment round, Pseudomonas (39.3%) and Acinetobacter (25.2%) together make up >64% of 16S reads. [src: lignin_community_enrichment] In the bacterial Base-versus-Lignin differential-abundance table, Pseudomonas rose from <0.1% to 7.5%, with a centered log-ratio (CLR) effect of +11.5. [src: lignin_community_enrichment] These two lignin-condition figures (39.3% and 7.5%) are stated separately in the cited claims.

Adding labile carbon (group LC) lowers Pseudomonas to 23.0%, against 39.3% with lignin only. [src: lignin_community_enrichment] In Round 2, communities with a lignin history (L-L, L-LC) are Pseudomonas-dominated (52–53%) with low Acinetobacter (<1–20%). [src: lignin_community_enrichment] Group L-L has mean Pseudomonas abundance of 53.3%. [src: lignin_community_enrichment] See [[concepts/labile-carbon-effects-on-lignin-degrading-community-structure]] and selective filtering of communities by lignin enrichment.

Pseudomonas is known for the beta-ketoadipate pathway and protocatechuate catabolism. [src: lignin_community_enrichment] The report links its dominance to Hossain et al. (2024), who found that Pseudomonas and Acinetobacter had the highest diversity of aromatic-degrading enzymes across 26 soil bacterial genomes. [src: lignin_community_enrichment] See [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]].

## Metal ecology

A Pseudomonas OTU (operational taxonomic unit), 97_39338, ranks 8th for microcosm experiments. It has Levins' B 0.999 and 2.1 metal types, and Cu stress is the recommended treatment. [src: microbeatlas_metal_ecology] Pseudomonas has the highest niche breadth of all candidate genera (B_std = 0.999) despite ranking eighth by composite score. [src: microbeatlas_metal_ecology] It carries a complete copA/pco Cu-resistance operon. [src: microbeatlas_metal_ecology]

The report cites Yuan et al. (2020) as showing that copper reduces OTU richness in freshwater microcosms. It interprets this as amplifying the advantage of Cu-resistant taxa such as OTU 97_39338. [src: microbeatlas_metal_ecology] In the ENIGMA candidate table, Pseudomonas has 2.1 metal types but no groundwater prevalence or fold-enrichment estimate, and it is not in the top-15. [src: microbeatlas_metal_ecology] See [[concepts/field-validation-of-metal-diversity-genera-in-contaminated-groundwater]].

## Plant association

Pseudomonas_E is a key dual-nature genus. Its plant growth promoting (PGP) markers are HCN, phenazine and phosphate solubilization. Its pathogenic markers are T2SS, T3SS, T6SS and effectors. [src: plant_microbiome_ecotypes] In the plant-associated genus dossier it has 82 plant-associated species and a PGP ratio of 0.53. Its cluster-robust markers are ACC, cellulase, pectinase, effector, phenazine, phosphate-sol and T3SS, and it has 424 MGnify soil BGCs. [src: plant_microbiome_ecotypes]

Pseudomonas_E is a dominant phyllosphere genus with 13 species. [src: plant_microbiome_ecotypes] It is the only genus with significant presence across all plant compartments. [src: plant_microbiome_ecotypes] It is also a top NRP/siderophore biosynthetic gene cluster (BGC) producer, with 125. [src: plant_microbiome_ecotypes] See [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]].

For P. avellanae, the initial subclade analysis covered 319 genomes, 68 (21%) of them plant-associated, in 3 subclades. [src: plant_microbiome_ecotypes] The scan reports a best subclade of 31% plant, Fisher p = 7.3×10⁻⁴ and BH-FDR q = 0.0031. It passes Bonferroni significance and is Cochran-valid for chi². [src: plant_microbiome_ecotypes] P. avellanae is one of the three most-robust results in the full scan. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

## Open Directions

- Resolve the 433-clade ambiguity by using species-level rather than genus-level bridging for Pseudomonas, then test whether the uranium null result persists. See [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].
- Test whether the lignin-enrichment Pseudomonas dominance belongs to Pseudomonas_E or Pseudomonas s.s. This needs shotgun or species-level data.
- Test the copA/pco Cu-resistance hypothesis for OTU 97_39338 in a Cu-stress microcosm.
