---
type: "Dataset"
description: "16S OTU profiles across samples, held as arkinlab_microbeatlas."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
aliases: ["arkinlab_microbeatlas"]
---
# MicrobeAtlas

MicrobeAtlas is a collection of 16S OTU (operational taxonomic unit) profiles across samples, held in the KBase Data Lakehouse as `arkinlab_microbeatlas`. It holds 463,972 16S samples, 98,919 OTUs and 260,831,135 OTU-count rows. [src: berdl_data_atlas] Reports use it as a prevalence and biogeography baseline [src: discoveries], and for niche-breadth estimates. [src: comprehensive_metal_ecology] The report-level caveats below limit how far those estimates can be trusted. See [[entities/kbase-data-lakehouse]] for the platform.

## Key facts

- The tables `otu_counts_long`, `otu_metadata` and `sample_metadata` supply the MicrobeAtlas 16S OTU profiles. [src: berdl_data_atlas]
- The Lakehouse holds 261M MicrobeAtlas OTU-count rows. [src: berdl_data_atlas]
- One report describes the collection as 464K global 16S samples, useful as a prevalence and biogeography baseline. [src: discoveries]
- In the ENIGMA study, the collection also includes `enriched_metadata_gee` and supplies global 16S biogeography, co-occurrence and environmental metadata. [src: genotype_to_phenotype_enigma] That report cites 464K samples and 260M OTU counts. [src: genotype_to_phenotype_enigma]
- In the niche-breadth work, the tables supply niche breadth and taxonomy for 98,919 OTUs × 463,972 samples. [src: microbeatlas_metal_ecology] `sample_metadata` also supplies pH, temperature and biome for confounder checks. [src: comprehensive_metal_ecology]
- The metal-ecology report also describes an OTU × sample abundance matrix reached through MicrobeAtlas from `kescience_mgnify`. [src: comprehensive_metal_ecology] See [[entities/kescience-mgnify]].

## Use in niche-breadth analyses

The metal-ecology reports used MicrobeAtlas to compute [[entities/levins-niche-breadth]] from its Env_Level_1 habitat categories rather than soil chemistry. This keeps the niche-breadth and metal-concentration axes independent. [src: comprehensive_metal_ecology] One report calls this the first global-scale, phylogenetically controlled link between genus-level metal type diversity (AMRFinderPlus annotations across 6,789 GTDB species) and niche breadth from the 464,000-sample atlas. [src: microbeatlas_metal_ecology] A pangenome database of 6,789 species was joined to the atlas of 98,919 OTUs × 463,972 samples. [src: microbeatlas_metal_ecology] The per-genus trait table has 2,851 rows. [src: comprehensive_metal_ecology] See [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]].

An abundance filter excluded OTUs with mean relative abundance < 0.01%. That removed 66% of OTUs and kept 34% = 33,676 OTUs. [src: microbeatlas_metal_ecology] A strict ≥5% prevalence threshold left 10,433 OTUs, against 98,919 in the original analysis. [src: microbeatlas_metal_ecology]

### Robustness to sample-count thresholds

Restricting the primary bacterial PGLS (phylogenetic generalized least squares) to genera seen in at least 10, 20 or 50 MicrobeAtlas samples gave the same estimate, β = −0.021, at all three thresholds [src: comprehensive_metal_ecology]:

| Minimum samples | Genera | SE | p |
|---|---|---|---|
| ≥10 | 1,572 | 0.00368 | 1.38×10⁻⁸ [src: comprehensive_metal_ecology] |
| ≥20 | 1,570 | 0.00368 | 1.69×10⁻⁸ [src: comprehensive_metal_ecology] |
| ≥50 | 1,559 | 0.00370 | 2.22×10⁻⁸ [src: comprehensive_metal_ecology] |

The report cautions that genera detected in fewer samples may have less reliable niche-breadth estimates. [src: comprehensive_metal_ecology] See [[concepts/robustness-and-replication-of-niche-breadth-associations]].

### Environment-category sensitivity

Excluding "aquatic" is the most heterogeneous and over-represented category (40,353 OTUs; 40.8% of the dataset). It gave the weakest model: β fell from +0.021 to +0.0085 (−59%), with p = 0.031. [src: microbeatlas_metal_ecology] The three least-sampled environments were flower (898 OTUs, 0.9%), leaf (1,298 OTUs, 1.3%) and plant (2,647 OTUs, 2.7%). [src: microbeatlas_metal_ecology]

## Co-occurrence

An exploratory prokaryotic co-occurrence analysis used MicrobeAtlas networks of 3,149–3,389 genera. It used hypergeometric tests (Veech 2013, FDR (false discovery rate) < 5%) with phi coefficients. [src: comprehensive_metal_ecology] The strata were all samples (n = 462,716), environmental (n = 382,483) and soil (n = 162,022). [src: comprehensive_metal_ecology] See [[concepts/co-occurrence-network-structure-and-metal-tolerance-guilds]].

## Genus prevalence for ENIGMA

All 14 ENIGMA genera are globally ubiquitous. They were detected in 4,086-288,686 of 464,000 samples. [src: genotype_to_phenotype_enigma] Caulobacter is the most widespread (289K samples). [src: genotype_to_phenotype_enigma] [[entities/rhodanobacter]] follows with 228K samples [src: genotype_to_phenotype_enigma], then [[entities/pseudomonas]] with 206K. [src: genotype_to_phenotype_enigma]

## Caveats

- Detection across the 13 environment categories confounds habitat use with sampling intensity, V3–V4 or V4 primer bias, and uneven geographic and temporal SRA/ENA contributions. [src: microbeatlas_metal_ecology]
- Dense sampling of soil, marine and plant environments can inflate apparent niche breadth relative to deep subsurface, brine and ice taxa. [src: microbeatlas_metal_ecology]
- The 13 categories lump heterogeneous habitats. "Aquatic" combines marine, freshwater, estuarine, hydrothermal vent and pond environments. [src: microbeatlas_metal_ecology]
- MicrobeAtlas has no finer environment classification, so within-category heterogeneity cannot be tested. Testing it would need niche breadth recomputed with a revised taxonomy. [src: microbeatlas_metal_ecology]
- Levins' B_std from 16S OTUs may carry noise from coarse OTU–genus matching and MicrobeAtlas annotations. [src: comprehensive_metal_ecology]
