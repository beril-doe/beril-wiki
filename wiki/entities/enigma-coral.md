---
type: "Dataset"
description: "ENIGMA CORAL is an Oak Ridge field-sample dataset for geochemistry and microbial communities."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/lab_field_ecology__REPORT.md"]
---
# ENIGMA CORAL

## What it is

**Canonical name:** ENIGMA CORAL. The source uses `enigma_coral` as the dataset or tenant identifier. No stable external identifier is reported in the document. [src: berdl_data_atlas]

**Known aliases:** ENIGMA CORAL; `enigma_coral`. [src: berdl_data_atlas]

ENIGMA CORAL is a KBase Data Lakehouse field-sample data resource used for environmental and biological observations. [src: berdl_data_atlas] The atlas recommends it for field samples and places it within the broader [[concepts/multi-omics-integration]] and [[concepts/environmental-resistome]] integration landscape. [src: berdl_data_atlas] The contamination-gradient study **refines** this characterization by demonstrating a reproducible workflow linking ENIGMA geochemistry and community composition to [[entities/kbase-ke-pangenome]] clades and [[entities/eggnog]]-derived functional proxies across 108 samples. [src: enigma_contamination_functional_potential]

The SSO subsurface ecology analysis **supports** CORAL’s role as a field-sample resource by using its sediment and groundwater 16S amplicon sequence variant (ASV) observations to resolve community structure across a 3×3 well grid spanning approximately 6 m. [src: enigma_sso_asv_ecology] It also **refines** the integration picture: 221 SSO geochemistry sample tubes are registered in CORAL, but the associated metals, ion chromatography/total organic carbon, isotope, ammonia, and nitrite measurements were not loaded in the analyzed dataset. [src: enigma_sso_asv_ecology]

The field-versus-lab fitness survey **refines** expectations about CORAL’s current utility for gene-level ecological analysis: its 47 tables contained field geochemistry and community resources but no *Desulfovibrio vulgaris* Hildenborough gene-level fitness data. [src: field_vs_lab_fitness] The survey found one TnSeq library for FW300-N2E2 (*Pseudomonas*) and DubSeq libraries for *Escherichia coli*, *Pseudomonas putida*, and *Bacteroides thetaiotaomicron*, so CORAL cannot currently bridge DvH Fitness Browser measurements to field observations. [src: field_vs_lab_fitness]

The Oak Ridge field-ecology study **supports** CORAL’s utility for directly comparing field communities with laboratory phenotypes: it linked 16S amplicon profiles and geochemistry across 108 sites to [[entities/kescience-fitnessbrowser]] metal-tolerance scores. [src: lab_field_ecology] Of 26 Fitness Browser genera, 14 were detected; *Sphingomonas*, *Pseudomonas*, and *Caulobacter* occurred at 93%, 91%, and 82% of sites, respectively. [src: lab_field_ecology] The aggregate laboratory-tolerance/field-abundance relationship was positive but non-significant (Spearman rho=0.503, p=0.095, n=12), so this result **refines** the earlier cross-tenant limitation: CORAL can support genus-level field-versus-lab tests, but not yet species- or strain-resolved prediction. [src: lab_field_ecology]

## Key facts

- The inventory contains 4,346 ENIGMA SDT samples. [src: berdl_data_atlas]
- The inventory contains 579 ENIGMA DDT measurement bricks. [src: berdl_data_atlas]
- The inventory contains 218,510 ENIGMA SDT amplicon sequence variants (ASVs). [src: berdl_data_atlas]
- ENIGMA contains 36% of the KBase Data Lakehouse tables but appears in 6 of the 66 audited BERIL projects. [src: berdl_data_atlas]
- ENIGMA covers 5 biological topics and has a topic-coverage entropy of 0.43. [src: berdl_data_atlas]
- The contamination-gradient analysis used a quality-controlled overlap of 108 samples, a geochemistry matrix with shape `(108, 49)`, 41,711 community taxon rows, 212 distinct communities, and 1,392 distinct genera. [src: enigma_contamination_functional_potential]
- That analysis **supports** the atlas’s placement of ENIGMA in [[concepts/multi-omics-integration]]: it integrated geochemistry, community composition, pangenome clades, and eggNOG-derived functional features, while documenting incomplete cross-dataset coverage. [src: enigma_contamination_functional_potential]
- The genus-level analysis found no robust monotonic association between contamination and broad functional scores in its confirmatory tests; exploratory defense associations were sensitive to coverage, covariate specification, taxonomic resolution, and multiple-testing correction. [src: enigma_contamination_functional_potential]
- The SSO analysis measured 23,458 sediment ASVs across 37 sediment core samples aggregated per well and found significant spatial distance-decay, while hydrogeological zone explained 27.5% of community variance (F = 4.05, p = 0.0001). [src: enigma_sso_asv_ecology]
- SSO groundwater communities were sampled from 5 of 9 wells, and their well identity explained 49.9% of variance; date explained 0.8% over the 9-day interval. [src: enigma_sso_asv_ecology]
- The CORAL survey catalogued 6,705 genomes, 15,015 genes, 4,346 field samples with geochemistry data across 596 Oak Ridge locations, and 213,044 ASVs; these collections support field-context analyses but not DvH gene-level fitness analysis. [src: field_vs_lab_fitness]
- In the new 108-site study, five of 11 tested genera had uranium associations after Benjamini–Hochberg false-discovery-rate correction, with both positive and negative directions; this **supports** environmental sorting but **refines** any simple metal-tolerance interpretation because pH, redox, carbon sources, competition, and temporal history were not controlled. [src: lab_field_ecology]

## Cross-tenant relevance

The atlas identifies an unused ENIGMA–PhageFoundry bridge with 11 shared schema-level keys for studying subsurface prophages, metal resistance, and the Oak Ridge contamination gradient. [src: berdl_data_atlas] This bridge is schema-level only and had zero realized use at audit time; value-space validity requires live-cluster execution. [src: berdl_data_atlas] The proposed integration connects ENIGMA CORAL with [[entities/phagefoundry]] and is relevant to [[concepts/environmental-resistome]]. [src: berdl_data_atlas]

The contamination-gradient workflow **supports** the environmental-resistome relevance by testing an eight-metal contamination index against inferred community defense and stress potential, but its confirmatory genus-level defense associations were null. [src: enigma_contamination_functional_potential] It therefore **refines** the proposed use of ENIGMA for metal-resistance research: broad COG-category proxies did not establish a contamination-linked functional shift, and finer-resolution species, strain, or curated pathway analyses remain necessary. [src: enigma_contamination_functional_potential]

The SSO study **supports** investigating contamination-linked spatial structure in CORAL, but **refines** the evidence level: its proposed northeast-to-southwest plume, M5 mixing zone, and inferred redox ladder are hypotheses based on 16S composition and taxonomy-to-trait inference, not direct geochemical measurements. [src: enigma_sso_asv_ecology] Loading the registered SSO geochemistry and pairing it with metagenomics, isolate genomes, and repeat seasonal sampling would directly test these interpretations. [src: enigma_sso_asv_ecology]

The new field-ecology study **supports** using CORAL to test laboratory-to-field transfer, while its non-significant aggregate tolerance result and bidirectional genus-level uranium associations **contradict** a simple expectation that laboratory metal tolerance alone determines abundance. [src: lab_field_ecology] Species- or strain-level matching, multivariate CCA or RDA controlling for pH, redox, and carbon sources, temporal sampling, and metal-specific fitness scores are proposed to resolve this limitation. [src: lab_field_ecology]

The absence of DvH fitness data **refines** the cross-tenant roadmap: CORAL’s field geochemistry and community collections could eventually be linked to Fitness Browser data, but that analysis requires a different ENIGMA organism with both environmental observations and gene-level fitness measurements, or newly loaded DvH data. [src: field_vs_lab_fitness]

## Source

- [[summaries/berdl_data_atlas__REPORT]] — KBase Data Lakehouse inventory, topic map, cross-tenant bridges, and realized-use audit. [src: berdl_data_atlas]
- [[summaries/enigma_contamination_functional_potential__REPORT]] — ENIGMA contamination-gradient analysis linking geochemistry, community composition, pangenome clades, and functional proxies. [src: enigma_contamination_functional_potential]
- [[summaries/enigma_sso_asv_ecology__REPORT]] — SSO subsurface ASV ecology, spatial structure, hydrogeological gradients, and missing geochemical validation. [src: enigma_sso_asv_ecology]
- [[summaries/field_vs_lab_fitness__REPORT]] — DvH field-versus-lab fitness analysis and ENIGMA CORAL data-availability survey. [src: field_vs_lab_fitness]
- [[summaries/lab_field_ecology__REPORT]] — Oak Ridge field ecology linked to Fitness Browser laboratory metal-tolerance measurements. [src: lab_field_ecology]
