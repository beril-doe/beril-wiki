---
type: "Concept"
description: "How the dominance of human clinical and gut genomes in public genome sets skews environment-genome analyses; stops at specific downstream models."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Clinical and human-associated sampling bias in genome collections

Human clinical and gut genomes are heavily represented in the genome sets these projects analysed. In the AlphaEarth subset 38% of genomes are human-associated. [src: env_embedding_explorer] Several projects measured the skew directly, and others flagged it as a caveat on AMR (antimicrobial resistance), plant growth promoting (PGP) and ecotype analyses. [src: amr_pangenome_atlas, pgp_pangenome_ecology] The 38% figure describes one subset and may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer] The counts are well documented. The effect on downstream conclusions is mostly argued rather than tested, and one reanalysis found the skew did not explain a weak signal. [src: ecotype_env_reanalysis]

## How large the skew is

Human-associated sources make up 38% of the 83,287 genomes with AlphaEarth embeddings. They split into human clinical (16,390; 20%), human gut (13,466; 16%) and human other (1,669; 2%). [src: env_embedding_explorer] Environmental categories are much smaller: soil (6,073; 7%), marine (5,850; 7%) and freshwater (5,840; 7%). [src: env_embedding_explorer] A further 13,944 genomes (17%) fall in "Other". This class includes site-specific labels, generic terms and clinical sites the keywords missed. [src: env_embedding_explorer]

The species-level picture agrees. Of 224 species selected for ecotype analysis, 106 (47%) were majority human-associated and 47 (21%) majority environmental. The other 71 (32%) were mixed/other. [src: ecotype_env_reanalysis]

Within a genus the pattern repeats. Pseudomonas aeruginosa makes up 53% of all Pseudomonas genomes (6,760/12,732), while many environmental species have fewer than 10 sequenced genomes. [src: pseudomonas_carbon_ecology] Clinical isolation accounts for 4,197 Pseudomonas genomes (33.0%) and human (other) for 1,659 (13.0%). [src: pseudomonas_carbon_ecology] Across all GTDB genomes, Pseudomonas is 37.8% clinical, driven by P. aeruginosa, against 12.9% soil/plant and 9.4% aquatic. [src: genotype_to_phenotype_enigma] A separate dataset shows the same imbalance: 57K clinical genomes against 384 plant_microbiome genomes. [src: gc_ecotype_ecology]

## Why it arises

The env_embedding_explorer report attributes the AlphaEarth skew to NCBI's bias toward pathogen sequencing. It adds that clinical isolates tend to have good geographic metadata from epidemiological tracking, so they receive embeddings. [src: env_embedding_explorer] It cites Saha et al., 2023 for public databases being heavily skewed toward pathogens and clinical isolates. [src: env_embedding_explorer] It describes the bias as known in general but not previously quantified for satellite-derived embeddings. [src: env_embedding_explorer] Coverage is also selective: AlphaEarth covers only 28.4% of all genomes, biased toward those with valid latitude/longitude. [src: env_embedding_explorer]

## Consequences for analyses

The pooled AlphaEarth geographic-distance curve has a 2.0x ratio. It blends environmental and human-associated signals and is dominated by the 38% human-associated fraction. [src: env_embedding_explorer] The report attributes the homogeneity of human-associated embeddings to hospitals and clinics worldwide sharing similar urban satellite imagery. [src: env_embedding_explorer]

env_embedding_explorer hypothesizes that the clinical bias may partly explain the weak environment–gene content signal. Its reasoning is that 38% of compared genomes come from interchangeable hospital environments, which would dilute the relationship. [src: env_embedding_explorer] The ecotype reanalysis confirmed the strong clinical bias but found that it does not account for the weak environment signal. [src: ecotype_env_reanalysis] That reanalysis therefore does not support the dilution hypothesis. [src: ecotype_env_reanalysis, env_embedding_explorer]

Genome databases over-represent clinical pathogens, which inflates AMR counts for human-associated species. [src: amr_pangenome_atlas] The AMR environmental resistome report says that clinical species carry more AMR partly because clinical species get sequenced because they have AMR, and that soil and aquatic species are undersampled. [src: amr_environmental_resistome] The PGP analysis notes that NCBI is heavily biased toward clinical and host-associated isolates, and that its ncbi_isolation_source labels are noisy. [src: pgp_pangenome_ecology]

The ENIGMA report concludes that its subsurface field isolates occupy environmental niches underrepresented in the NCBI genome collection. [src: genotype_to_phenotype_enigma] It also warns that transfer learning from clinical phenotype databases may be biased. [src: genotype_to_phenotype_enigma]

## Tensions

- The env_embedding_explorer report proposes that clinical bias may partly explain the weak environment signal. [src: env_embedding_explorer] The ecotype reanalysis finds the bias does not account for it. [src: ecotype_env_reanalysis]
- The 38% human figure describes the AlphaEarth subset and may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer] The Pseudomonas figures describe one genus. [src: genotype_to_phenotype_enigma, pseudomonas_carbon_ecology]

## Open Directions

- Rerun the environment–gene content comparison with human-associated genomes removed or downweighted, and with matched sample sizes per environment class. This would test directly whether the dilution hypothesis holds. See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]].
- Compare the human fraction in the AlphaEarth subset with the fraction in all NCBI genomes using one classification scheme. This would show whether the 38% is specific to the subset.
- Reclassify the 17% "Other" genomes with expanded keywords. This would show how many are hidden clinical genomes.
- Estimate AMR prevalence per species after stratifying or reweighting by sampling intensity. This would separate true clinical enrichment from sequencing preference.
