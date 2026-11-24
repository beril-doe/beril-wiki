---
type: "Concept"
description: "Whether habitat type (Soil vs Freshwater) structures community-weighted pathway completeness, and which pathway classes drive the separation; stops at genome-predicted potential."
sources: ["summaries/discoveries.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
# Ecosystem differentiation of community metabolic potential

Habitat type structures community-weighted pathway completeness in the NMDC (National Microbiome Data Collaborative) samples. Soil and Freshwater communities separate almost completely in principal component analysis (PCA) of genome-predicted pathway completeness, and carbon utilization pathways drive the separation. The evidence comes from one dataset analysed in two sources, and it stops at genome-predicted potential, not measured activity. [src: discoveries, nmdc_community_metabolic_ecology]

## Cohort and PCA structure

The PCA used a 220-sample × 80-pathway completeness matrix. [src: nmdc_community_metabolic_ecology] The cohort held 126 Soil samples, 33 Freshwater samples and 61 samples with unrecorded ecosystem type. [src: nmdc_community_metabolic_ecology] Principal component 1 (PC1) explained 49.4% of variance and PC2 explained 16.6%. The first five components together explained 83.0%. [src: nmdc_community_metabolic_ecology]

Both components differed across the three ecosystem types by Kruskal-Wallis (KW) test: PC1 H = 52.98 and PC2 H = 123.74, both p < 0.0001. [src: nmdc_community_metabolic_ecology] Soil and Freshwater occupied nearly non-overlapping regions of PC space. [src: nmdc_community_metabolic_ecology]

The pairwise Soil vs Freshwater PC1 separation was extreme: Mann-Whitney U = 3,674, p < 0.0001, with median PC1 of +3.86 for Soil and −6.28 for Freshwater. [src: discoveries, nmdc_community_metabolic_ecology] See [[entities/mann-whitney-u-test]] for the test.

## Which pathways drive the separation

Carbon utilization pathways, not amino acid pathways, dominate PC1. [src: discoveries, nmdc_community_metabolic_ecology] The top positive loadings, in the Soil direction, were glucuronate (0.146), fumarate (0.144), succinate (0.143), lysine (0.140) and cellobiose (0.139). [src: nmdc_community_metabolic_ecology] Galactose is also named among the dominant carbon pathways. [src: nmdc_community_metabolic_ecology]

The report reads these near-uniform positive loadings as higher predicted carbon metabolic diversity in Soil than in Freshwater communities. [src: nmdc_community_metabolic_ecology] It suggests that carbon substrate availability is the primary axis separating community metabolic type, with amino acid biosynthesis secondary at PC2. [src: nmdc_community_metabolic_ecology]

Amino acid pathways load more strongly on PC2, which separates communities within the Soil cluster. [src: discoveries, nmdc_community_metabolic_ecology]

## Amino acid pathways across ecosystems

Per-pathway KW tests with Benjamini-Hochberg false discovery rate (BH-FDR) correction found 17 of 18 amino acid pathways differed across ecosystem types (q < 0.05). [src: discoveries, nmdc_community_metabolic_ecology] The strongest differences were glycine (H = 92.98, q = 1.2×10⁻¹⁹), asparagine (H = 66.19, q = 3.8×10⁻¹⁴) and cysteine (H = 62.66, q = 1.5×10⁻¹³). [src: nmdc_community_metabolic_ecology] The exception was [[entities/tyrosine-biosynthesis|tyrosine]], with q = 0.71. [src: nmdc_community_metabolic_ecology]

This does not make amino acid biosynthesis the main driver. The discoveries digest states that the primary driver is carbon substrate availability, not biosynthesis capacity. [src: discoveries] The nmdc_community_metabolic_ecology report notes the 17/18 result is consistent with Ramoneda et al. (2023). [src: nmdc_community_metabolic_ecology]

## Interpretation and limits

The report reads the strong separation as consistent with a metabolic niche hypothesis. Under that hypothesis, aquatic versus terrestrial physicochemistry selects different community metabolic configurations, not just different taxa. [src: nmdc_community_metabolic_ecology] It describes the result as extending meta-metabolome ecology to genome-predicted potential: what resident taxa are capable of making clusters strongly by ecosystem. [src: nmdc_community_metabolic_ecology] It also suggests freshwater taxa may face different selective pressures on retaining amino acid biosynthesis than soil taxa. [src: nmdc_community_metabolic_ecology] These are interpretations, not tested results.

The discoveries digest warns that carbon substrate range is the dominant axis of community metabolic potential. It can confound amino acid pathway analyses, so it recommends PC1-residualized or ecosystem-stratified Black Queen Hypothesis tests. [src: discoveries] Related issues appear in [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]].

The 61 "Unknown" samples likely mix soil subtypes or sediment environments, so the Soil/Freshwater contrast rests on 159 classified samples. [src: nmdc_community_metabolic_ecology] The report proposes resolving their habitat identity via NMDC Environment Ontology (ENVO) annotations or study-level metadata, which could improve power and reveal finer-scale metabolic niche structure. [src: nmdc_community_metabolic_ecology]

## Open Directions

- Resolve the habitat of the 61 Unknown samples using ENVO annotations or study-level metadata, then test whether finer niche structure appears.
- Re-run the amino acid pathway comparisons after residualizing PC1, or within ecosystem strata. This would show whether the 17/18 differences survive control for carbon range.
- Test whether PC2 sub-clusters within Soil correspond to soil subtypes. This would give the amino acid loadings an ecological label.
- Compare genome-predicted completeness with measured metabolites or activity in the same samples. This would address the limit that the analysis stops at predicted potential.
