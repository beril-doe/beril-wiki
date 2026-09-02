---
type: "Dataset"
description: "Groundwater and field-occurrence dataset used in ENIGMA subsurface ecology studies."
sources: ["summaries/enigma_carbon_census_1__REPORT.md", "summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# SSO

## What this entity is

SSO is the groundwater and field-occurrence dataset used in the ENIGMA Carbon Census. [src: enigma_carbon_census_1]

- **Canonical name:** SSO. [src: enigma_carbon_census_1]
- **Known aliases:** SSO. [src: enigma_carbon_census_1]
- **Stable external identifier:** None was reported in the source document. [src: enigma_carbon_census_1]

## Key facts from the ENIGMA Carbon Census

SSO supplied 59 of the 83 enrichment compounds analyzed in the census, with the remaining 24 compounds coming from necromass. [src: enigma_carbon_census_1]

The census detected 62 implicated utilizer genera in the SSO field atlas at genus resolution. [src: enigma_carbon_census_1]

Top field prevalences in the SSO atlas were approximately 0.7–0.9, and utilizers associated with 3-hydroxybenzoic acid reached a field prevalence of 0.90. [src: enigma_carbon_census_1]

The SSO field atlas provided occurrence context for predicted utilizers, but it did not measure compound degradation or catabolic activity. [src: enigma_carbon_census_1]

The ENIGMA Carbon Census could not statistically test groundwater-versus-necromass source tracking because only 2 of the 8 ENIGMA-isolate-callable compounds were necromass-sourced, and both were phthalate-class aromatics. [src: enigma_carbon_census_1]

## Subsurface community ecology

The SSO ecology analysis **refines** the field-atlas occurrence context with 16S amplicon sequencing across 9 wells in a 3×3 grid spanning approximately 6 m, where sediment communities comprised 23,458 ASVs and showed significant distance-decay (Mantel Spearman ρ = 0.323, p = 0.029). [src: enigma_sso_asv_ecology] Hydrogeological zone explained 27.5% of sediment community variance (PERMANOVA F = 4.05, p = 0.0001), while well identity explained 19.2% and was not significant (F = 0.80, p = 0.979), supporting an environment-linked interpretation of SSO community structure. [src: enigma_sso_asv_ecology]

Groundwater and sediment communities from the same wells differed substantially (median Bray–Curtis dissimilarity = 0.424), with groundwater enriched in Rhodanobacter, Gallionella, and Sideroxydans and sediment enriched in Anaeromyxobacter, Arcobacter, and Ca. Methanoperedens. [src: enigma_sso_asv_ecology] Groundwater community rankings remained nearly unchanged over 9 days (Mantel ρ = 0.867, p = 0.001), but the sediment–groundwater comparison is confounded by an 18-month sampling offset. [src: enigma_sso_asv_ecology]

The proposed northeast-to-southwest contamination plume and inferred redox gradients are hypotheses, not direct measurements: 221 SSO geochemistry sample tubes are registered in CORAL, but the relevant measurements were not loaded. [src: enigma_sso_asv_ecology] This **qualifies** any interpretation linking SSO occurrence patterns to contamination or catabolic activity. [src: enigma_sso_asv_ecology]

The MicrobeAtlas metal-ecology analysis **supports** using SSO well data as environmental occurrence context: across 133 samples, community-weighted mean metal-type diversity differed among 8 wells (Kruskal–Wallis H = 29.10, p = 0.0001), increased with time point (Spearman ρ = +0.383, p < 0.0001), and increased within FW216 (ρ = +0.576, p = 0.0001). [src: microbeatlas_metal_ecology] However, Sulfurimonas abundance decreased with time (ρ = −0.323, p = 0.0002), **qualifying** any inference that changing community composition was generally driven by metal resistance rather than electron-acceptor availability. [src: microbeatlas_metal_ecology] Only 16.8% of reads were joinable to genus-level GTDB metal-diversity data, so these community-weighted values require coverage-bias diagnostics. [src: microbeatlas_metal_ecology]

SSO-related findings are summarized in [[summaries/enigma_carbon_census_1__REPORT]], [[summaries/enigma_sso_asv_ecology__REPORT]], and [[summaries/microbeatlas_metal_ecology__REPORT]] and contribute to [[concepts/ecotype-environment-gene-content]], [[concepts/cross-tenant-data-bridging]], [[concepts/environmental-resistome]], and [[concepts/multi-omics-integration]]. [src: enigma_carbon_census_1, enigma_sso_asv_ecology, microbeatlas_metal_ecology]
