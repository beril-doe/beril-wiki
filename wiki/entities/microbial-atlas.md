---
type: "Dataset"
description: "Global environmental 16S dataset for habitat and genomic-representation analysis"
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/soil_frontier_genomics__REPORT.md"]
---
# Microbial Atlas

## What this entity is

**Canonical name:** Microbial Atlas. [src: genotype_to_phenotype_enigma]

**Known aliases:** MicrobeAtlas; Microbial Atlas 16S data. [src: genotype_to_phenotype_enigma]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: genotype_to_phenotype_enigma]

Microbial Atlas is a global environmental [[entities/16s-amplicon-sequencing]] dataset used to profile genus distributions and habitat associations in the [[summaries/genotype_to_phenotype_enigma__REPORT]] study. [src: genotype_to_phenotype_enigma] The newer [[summaries/microbeatlas_metal_ecology__REPORT]] study used the same 464,000-sample atlas to estimate genus-level ecological niche breadth and relate it to metal-resistance diversity inferred from [[entities/amrfinderplus]] annotations. [src: microbeatlas_metal_ecology]

The [[summaries/soil_frontier_genomics__REPORT]] analysis **extends** this environmental-coverage role to 5,441 soil samples containing clay content, mine proximity, nighttime lights, uranium, and functional-gene counts. [src: soil_frontier_genomics] It introduced a Genomic Discovery Index (GDI), defined as OTU richness divided by mean genome completeness plus 1, to characterize spatial gaps in genomic representation at 1° spatial bins. [src: soil_frontier_genomics]

## Use in the ENIGMA genotype-to-phenotype study

The dataset was used for genus-level environmental profiling of the 14 genera represented in the ENIGMA analysis. [src: genotype_to_phenotype_enigma]

The 14 ENIGMA genera occurred in 4,086–288,686 of 464,000 global 16S samples. [src: genotype_to_phenotype_enigma]

[[entities/caulobacter-crescentus|Caulobacter]] occurred in 289K samples, [[entities/rhodanobacter|Rhodanobacter]] occurred in 228K samples, and [[entities/pseudomonas-fluorescens|Pseudomonas]] occurred in 206K samples. [src: genotype_to_phenotype_enigma]

Globally sampled [[entities/pseudomonas-fluorescens|Pseudomonas]] was 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic, whereas all ENIGMA Pseudomonas belonged to the environmental Pseudomonas_E fluorescens/protegens clade. [src: genotype_to_phenotype_enigma]

[[entities/rhodanobacter|Rhodanobacter]] was 55% aquatic, 10% contaminated, and 0% clinical in the analyzed environmental profiles. [src: genotype_to_phenotype_enigma]

## Habitat associations and niche partitioning

Global environmental data supported a pH-driven niche-partition hypothesis when combined with local Oak Ridge co-occurrence data. [src: genotype_to_phenotype_enigma]

Across 464K global 16S samples, Cluster A averaged pH 6.78 and 15.7°C, while Cluster B averaged pH 5.43 and 22.6°C, giving a difference of 1.35 pH units and 6.9°C. [src: genotype_to_phenotype_enigma]

Cluster A comprised Brevundimonas, [[entities/caulobacter-crescentus|Caulobacter]], [[entities/sphingomonas|Sphingomonas]], Variovorax, and Sphingobium, while Cluster B comprised [[entities/rhodanobacter|Rhodanobacter]], Ralstonia, Dyella, Serratia, and Comamonas. [src: genotype_to_phenotype_enigma]

The local comparison covered 587 100-Well-Survey communities, and two anti-correlated genus clusters produced 47 significant pairs with |rho| > 0.2 and p < 0.01. [src: genotype_to_phenotype_enigma]

The source notes that Spearman co-occurrence measures correlation rather than causation and recommends SparCC analysis on the full 100WS ASV matrix as a stronger test of the niche-partition result. [src: genotype_to_phenotype_enigma]

The metal-ecology analysis **refines** these habitat-association uses by treating atlas detection as an inferred niche-breadth proxy rather than confirmed geographic range: Levins' B_std was phylogenetically conserved across 1,264 bacterial genera (Pagel's λ = 0.787), but sampling intensity, primer bias, and heterogeneous environment coverage remain limitations. [src: microbeatlas_metal_ecology]

Across 606 genera with AMR data, phylogenetic generalized least squares (PGLS) found that metal type diversity, rather than total AMR cluster count or core AMR fraction, was associated with broader inferred niche breadth (β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴). [src: microbeatlas_metal_ecology] This **supports** using Microbial Atlas to test links between environmental distribution and gene-content variation, while the cross-sectional result does not establish whether resistance broadens habitat range or broad range promotes resistance acquisition. [src: microbeatlas_metal_ecology]

The independent analysis also found positive, but non-specific, groundwater prevalence association (Spearman ρ = +0.112, p = 0.0019); groundwater-specific fold-enrichment was not significant (ρ = +0.042, p = 0.242). [src: microbeatlas_metal_ecology]

## Soil genomic-representation gaps

The soil-frontier analysis **supports** using Microbial Atlas-derived environmental observations to identify coverage gaps, reporting GDI = 902.36 for forest, 890.82 for cropland, 503.42 for grassland, and 525.13 for wetland. [src: soil_frontier_genomics] Forest and cropland were therefore jointly identified as the highest-GDI biomes, not as meaningfully ordered ranks. [src: soil_frontier_genomics]

Frontier areas with GDI > 1000 had mean pH = 6.74 versus 5.94 in mapped areas, a +0.8 pH unit gap; the report interprets this as systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics] This **refines** the existing sampling-intensity limitation: the gap may reflect fewer 16S samples from those pH ranges rather than greater difficulty assembling or annotating alkaline-soil genomes. [src: soil_frontier_genomics]

The GDI is a novel index and can equal 902 even when there are zero genomes because completeness = 0 makes its denominator 1; it also conflates OTU richness with completeness. [src: soil_frontier_genomics] Rarefaction-corrected GDI, separate richness and completeness reporting, bootstrap 95% CIs, and control for 16S sample counts per pH bin are required before treating biome rankings or the pH gap as definitive. [src: soil_frontier_genomics]

## Limitations

Microbial Atlas profiling was performed at genus level, while species-level biogeography was available for only 20 pangenome-linked strains with verified GTDB matches. [src: genotype_to_phenotype_enigma]

The dataset therefore supports broad environmental distribution and habitat-association analyses, but the report does not establish species-level habitat assignments for all ENIGMA strains. [src: genotype_to_phenotype_enigma]

The metal-ecology report **reinforces** this limitation: genus aggregation can make a broad score reflect different species occupying different habitats rather than one organism being a generalist, and the strict 5% within-environment prevalence analysis reduced the PGLS sample from 606 to 379 genera and yielded β = +0.0166, SE = 0.0099, p = 0.092. [src: microbeatlas_metal_ecology]

The soil-frontier report **reinforces** the need for provenance-aware interpretation: its three global model families had negative out-of-sample R², but spatial distributional shift, outlier leverage, and genuine unpredictability were not separated. [src: soil_frontier_genomics] Spatial blocking and re-analysis from the BERIL Observatory 16S tables and `kbase_ke_pangenome` completeness data are needed to determine whether the result reflects modelling failure or biological unpredictability. [src: soil_frontier_genomics]

## Related pages

- [[concepts/environment-embedding-geography]] — environmental distributions, co-occurrence, pH, temperature, groundwater associations, and spatial prediction. [src: genotype_to_phenotype_enigma, soil_frontier_genomics]
- [[concepts/ecotype-environment-gene-content]] — links between environmental distribution, metabolic guilds, and gene content. [src: genotype_to_phenotype_enigma]
- [[concepts/environmental-resistome]] — environmental occurrence data integrated with metal-resistance annotations. [src: microbeatlas_metal_ecology]
- [[concepts/metal-cross-resistance]] — metal type diversity and inferred ecological breadth. [src: microbeatlas_metal_ecology]
- [[concepts/genomic-under-representation]] — genomic under-representation in forest and cropland soils and the alkaline-soil sampling gap. [src: soil_frontier_genomics]
- [[concepts/provenance-aware-resource-discovery]] — distinguishing database sampling gaps from assembly or annotation gaps. [src: soil_frontier_genomics]
- [[concepts/cross-tenant-data-bridging]] — integration of environmental profiles with ENIGMA and BERDL data. [src: genotype_to_phenotype_enigma]
- [[entities/gtdb]] — source of verified taxonomic assignments for species-level linkages. [src: genotype_to_phenotype_enigma]
- [[entities/16s-amplicon-sequencing]] — sequencing approach underlying the environmental profiles. [src: genotype_to_phenotype_enigma]
- [[summaries/genotype_to_phenotype_enigma__REPORT]] — source-project summary. [src: genotype_to_phenotype_enigma]
- [[summaries/microbeatlas_metal_ecology__REPORT]] — metal-resistance ecology analysis using the atlas. [src: microbeatlas_metal_ecology]
- [[summaries/soil_frontier_genomics__REPORT]] — soil genomic-representation and clay-shield analysis. [src: soil_frontier_genomics]
