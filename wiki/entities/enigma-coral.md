---
type: Dataset
description: ENIGMA CORAL is an Oak Ridge field-sample dataset for geochemistry and
  microbial communities.
sources:
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: enigma_contamination_functional_potential
  resource: ../summaries/enigma_contamination_functional_potential__REPORT.md
  title: enigma contamination functional potential
- id: enigma_sso_asv_ecology
  resource: ../summaries/enigma_sso_asv_ecology__REPORT.md
  title: enigma sso asv ecology
- id: field_vs_lab_fitness
  resource: ../summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: lab_field_ecology
  resource: ../summaries/lab_field_ecology__REPORT.md
  title: lab field ecology
title: ENIGMA CORAL
---
# ENIGMA CORAL

## What it is

**Canonical name:** ENIGMA CORAL. The source uses `enigma_coral` as the dataset or tenant identifier. No stable external identifier is reported in the document. [^berdl_data_atlas]

**Known aliases:** ENIGMA CORAL; `enigma_coral`. [^berdl_data_atlas]

ENIGMA CORAL is a BERDL field-sample data resource used for environmental and biological observations. [^berdl_data_atlas] The atlas recommends it for field samples and places it within the broader [multi-omics-integration](../concepts/multi-omics-integration.md) and [environmental-resistome](../concepts/environmental-resistome.md) integration landscape. [^berdl_data_atlas] The contamination-gradient study **refines** this characterization by demonstrating a reproducible workflow linking ENIGMA geochemistry and community composition to [kbase-ke-pangenome](kbase-ke-pangenome.md) clades and [eggnog](eggnog.md)-derived functional proxies across 108 samples. [^enigma_contamination_functional_potential]

The SSO subsurface ecology analysis **supports** CORAL’s role as a field-sample resource by using its sediment and groundwater 16S amplicon sequence variant (ASV) observations to resolve community structure across a 3×3 well grid spanning approximately 6 m. [^enigma_sso_asv_ecology] It also **refines** the integration picture: 221 SSO geochemistry sample tubes are registered in CORAL, but the associated metals, ion chromatography/total organic carbon, isotope, ammonia, and nitrite measurements were not loaded in the analyzed dataset. [^enigma_sso_asv_ecology]

The field-versus-lab fitness survey **refines** expectations about CORAL’s current utility for gene-level ecological analysis: its 47 tables contained field geochemistry and community resources but no *Desulfovibrio vulgaris* Hildenborough gene-level fitness data. [^field_vs_lab_fitness] The survey found one TnSeq library for FW300-N2E2 (*Pseudomonas*) and DubSeq libraries for *Escherichia coli*, *Pseudomonas putida*, and *Bacteroides thetaiotaomicron*, so CORAL cannot currently bridge DvH Fitness Browser measurements to field observations. [^field_vs_lab_fitness]

The Oak Ridge field-ecology study **supports** CORAL’s utility for directly comparing field communities with laboratory phenotypes: it linked 16S amplicon profiles and geochemistry across 108 sites to [kescience-fitnessbrowser](kescience-fitnessbrowser.md) metal-tolerance scores. [^lab_field_ecology] Of 26 Fitness Browser genera, 14 were detected; *Sphingomonas*, *Pseudomonas*, and *Caulobacter* occurred at 93%, 91%, and 82% of sites, respectively. [^lab_field_ecology] The aggregate laboratory-tolerance/field-abundance relationship was positive but non-significant (Spearman rho=0.503, p=0.095, n=12), so this result **refines** the earlier cross-tenant limitation: CORAL can support genus-level field-versus-lab tests, but not yet species- or strain-resolved prediction. [^lab_field_ecology]

## Key facts

- The inventory contains 4,346 ENIGMA SDT samples. [^berdl_data_atlas]
- The inventory contains 579 ENIGMA DDT measurement bricks. [^berdl_data_atlas]
- The inventory contains 218,510 ENIGMA SDT amplicon sequence variants (ASVs). [^berdl_data_atlas]
- ENIGMA contains 36% of BERDL tables but appears in 6 of the 66 audited BERIL projects. [^berdl_data_atlas]
- ENIGMA covers 5 biological topics and has a topic-coverage entropy of 0.43. [^berdl_data_atlas]
- The contamination-gradient analysis used a quality-controlled overlap of 108 samples, a geochemistry matrix with shape `(108, 49)`, 41,711 community taxon rows, 212 distinct communities, and 1,392 distinct genera. [^enigma_contamination_functional_potential]
- That analysis **supports** the atlas’s placement of ENIGMA in [multi-omics-integration](../concepts/multi-omics-integration.md): it integrated geochemistry, community composition, pangenome clades, and eggNOG-derived functional features, while documenting incomplete cross-dataset coverage. [^enigma_contamination_functional_potential]
- The genus-level analysis found no robust monotonic association between contamination and broad functional scores in its confirmatory tests; exploratory defense associations were sensitive to coverage, covariate specification, taxonomic resolution, and multiple-testing correction. [^enigma_contamination_functional_potential]
- The SSO analysis measured 23,458 sediment ASVs across 37 sediment core samples aggregated per well and found significant spatial distance-decay, while hydrogeological zone explained 27.5% of community variance (F = 4.05, p = 0.0001). [^enigma_sso_asv_ecology]
- SSO groundwater communities were sampled from 5 of 9 wells, and their well identity explained 49.9% of variance; date explained 0.8% over the 9-day interval. [^enigma_sso_asv_ecology]
- The CORAL survey catalogued 6,705 genomes, 15,015 genes, 4,346 field samples with geochemistry data across 596 Oak Ridge locations, and 213,044 ASVs; these collections support field-context analyses but not DvH gene-level fitness analysis. [^field_vs_lab_fitness]
- In the new 108-site study, five of 11 tested genera had uranium associations after Benjamini–Hochberg false-discovery-rate correction, with both positive and negative directions; this **supports** environmental sorting but **refines** any simple metal-tolerance interpretation because pH, redox, carbon sources, competition, and temporal history were not controlled. [^lab_field_ecology]

## Cross-tenant relevance

The atlas identifies an unused ENIGMA–PhageFoundry bridge with 11 shared schema-level keys for studying subsurface prophages, metal resistance, and the Oak Ridge contamination gradient. [^berdl_data_atlas] This bridge is schema-level only and had zero realized use at audit time; value-space validity requires live-cluster execution. [^berdl_data_atlas] The proposed integration connects ENIGMA CORAL with [phagefoundry](phagefoundry.md) and is relevant to [environmental-resistome](../concepts/environmental-resistome.md). [^berdl_data_atlas]

The contamination-gradient workflow **supports** the environmental-resistome relevance by testing an eight-metal contamination index against inferred community defense and stress potential, but its confirmatory genus-level defense associations were null. [^enigma_contamination_functional_potential] It therefore **refines** the proposed use of ENIGMA for metal-resistance research: broad COG-category proxies did not establish a contamination-linked functional shift, and finer-resolution species, strain, or curated pathway analyses remain necessary. [^enigma_contamination_functional_potential]

The SSO study **supports** investigating contamination-linked spatial structure in CORAL, but **refines** the evidence level: its proposed northeast-to-southwest plume, M5 mixing zone, and inferred redox ladder are hypotheses based on 16S composition and taxonomy-to-trait inference, not direct geochemical measurements. [^enigma_sso_asv_ecology] Loading the registered SSO geochemistry and pairing it with metagenomics, isolate genomes, and repeat seasonal sampling would directly test these interpretations. [^enigma_sso_asv_ecology]

The new field-ecology study **supports** using CORAL to test laboratory-to-field transfer, while its non-significant aggregate tolerance result and bidirectional genus-level uranium associations **contradict** a simple expectation that laboratory metal tolerance alone determines abundance. [^lab_field_ecology] Species- or strain-level matching, multivariate CCA or RDA controlling for pH, redox, and carbon sources, temporal sampling, and metal-specific fitness scores are proposed to resolve this limitation. [^lab_field_ecology]

The absence of DvH fitness data **refines** the cross-tenant roadmap: CORAL’s field geochemistry and community collections could eventually be linked to Fitness Browser data, but that analysis requires a different ENIGMA organism with both environmental observations and gene-level fitness measurements, or newly loaded DvH data. [^field_vs_lab_fitness]

## Source

- [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md) — BERDL inventory, topic map, cross-tenant bridges, and realized-use audit. [^berdl_data_atlas]
- [enigma_contamination_functional_potential__REPORT](../summaries/enigma_contamination_functional_potential__REPORT.md) — ENIGMA contamination-gradient analysis linking geochemistry, community composition, pangenome clades, and functional proxies. [^enigma_contamination_functional_potential]
- [enigma_sso_asv_ecology__REPORT](../summaries/enigma_sso_asv_ecology__REPORT.md) — SSO subsurface ASV ecology, spatial structure, hydrogeological gradients, and missing geochemical validation. [^enigma_sso_asv_ecology]
- [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md) — DvH field-versus-lab fitness analysis and ENIGMA CORAL data-availability survey. [^field_vs_lab_fitness]
- [lab_field_ecology__REPORT](../summaries/lab_field_ecology__REPORT.md) — Oak Ridge field ecology linked to Fitness Browser laboratory metal-tolerance measurements. [^lab_field_ecology]

[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
[^enigma_contamination_functional_potential]: [enigma contamination functional potential](../summaries/enigma_contamination_functional_potential__REPORT.md)
[^enigma_sso_asv_ecology]: [enigma sso asv ecology](../summaries/enigma_sso_asv_ecology__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
[^lab_field_ecology]: [lab field ecology](../summaries/lab_field_ecology__REPORT.md)
