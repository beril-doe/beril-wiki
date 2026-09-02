---
type: "Summary"
description: "Spatial and functional analysis maps a contamination plume across the SSO subsurface grid."
doc_type: "short"
full_text: "sources/enigma_sso_asv_ecology__REPORT.md"
---
# SSO Subsurface Community Ecology — Spatial Structure, Functional Gradients, and Hydrogeological Drivers

## Overview

This report analyzes sediment and groundwater 16S amplicon sequence variant (ASV) communities from the SSO subsurface site to test spatial structure, hydrogeological zonation, inferred biogeochemical functions, groundwater–sediment differentiation, guild associations, and short-term temporal stability. The central interpretation is that a contamination plume entering from the northeast and moving southwest through the saturated zone structures microbial communities at meter scale, although this plume model remains unconfirmed because direct SSO geochemistry has not yet been loaded. [src: enigma_sso_asv_ecology]

## Key Findings

### Spatial structure and the U3–M6–L7 corridor

Across 9 wells arranged in a 3×3 grid spanning approximately 6 m, the sediment dataset contained 23,458 ASVs and 37 sediment core samples aggregated per well. Mean Bray–Curtis dissimilarity was 0.747, ranging from 0.558 for U3–M6 to 0.872 for U3–L9. A Mantel test, which correlates ecological and geographic distance matrices, detected significant distance-decay of community similarity (Spearman ρ = 0.323, p = 0.029, 9,999 permutations). NMDS (non-metric multidimensional scaling) had stress = 0.067, while Procrustes correspondence between community ordination and the physical grid was marginal (m² = 0.379, p = 0.080). [src: enigma_sso_asv_ecology]

Community turnover was not aligned with the uphill–downhill direction (Mantel ρ = −0.049, p = 0.580), but showed a stronger, though non-significant, association with the east–west axis (column Mantel ρ = 0.227, p = 0.092). The U3–M6–L7 pairs had the three most negative distance residuals: U3–M6 had Bray–Curtis = 0.558 and residual = −0.170, M6–L7 had Bray–Curtis = 0.615 and residual = −0.154, and U3–L7 had Bray–Curtis = 0.646 and residual = −0.133. U3–M4 had the largest positive residual (Bray–Curtis = 0.871, residual = +0.105). These results identify a northeast-to-southwest diagonal corridor whose shared community composition is interpreted as consistent with a contamination-plume flow path, but the hydrological explanation remains a testable inference rather than a direct measurement. [src: enigma_sso_asv_ecology]

### Hydrogeological depth zonation

PERMANOVA (permutational multivariate analysis of variance) on 37 sediment core segments found that hydrogeological zone explained 27.5% of community variance (F = 4.05, p = 0.0001), whereas well identity explained 19.2% and was not significant (F = 0.80, p = 0.979). Samples from the same well but different depths had median Bray–Curtis dissimilarity = 0.977, while samples from the same depth zone in different wells had median Bray–Curtis dissimilarity = 0.835. The report interprets this pattern as evidence that depth and saturated-zone plume intersection dominate horizontal well identity. [src: enigma_sso_asv_ecology]

The depth classifications were VZ (33 samples), VSZ (25), SZ1 (54), and SZ2 (45). Ten of 12 dominant phyla had significant depth associations at p < 0.05. Shallow-enriched groups included Chloroflexi (Spearman ρ = −0.73), Patescibacteria (−0.70), Myxococcota (−0.54), and Spirochaetota (−0.53); deep-enriched groups included Firmicutes (ρ = +0.76), WPS-2 (+0.52), Bacteroidota (+0.50), and Proteobacteria (+0.49). [src: enigma_sso_asv_ecology]

### Inferred biogeochemical gradients

Multi-resolution functional inference covered 22 classes at 78% coverage and 65 annotated genera at 21% coverage. The class-level redox index ranged from 0.047 at M6 to 0.227 at U3. Genus-level inference covered 12 biogeochemical process categories and mapped process hotspots onto the grid, producing a spatial pattern interpreted as an inferred redox ladder rather than direct geochemical measurement. [src: enigma_sso_asv_ecology]

Denitrification ranged from 1.9–7.7%, peaking at M5 with 7.7% and *Rhodanobacter* as the key genus. Iron oxidation peaked at U3 at 2.8%, with *Sideroxydans*; nitrification also peaked at U3 at 2.3%, with *Ca. Nitrosotalea*; iron reduction peaked at U1 at 2.3%, with *Anaeromyxobacter*; sulfur oxidation peaked at M4 at 1.9%, with *Arcobacter* and *Thiobacillus*; methanotrophy peaked at M4 at 1.9%, with *Ca. Methanoperedens*; and fermentation peaked at L9 at 5.3%, with *Spirochaeta* and *Paenisporosarcina*. [src: enigma_sso_asv_ecology]

M5 is interpreted as a plume mixing zone where nitrate-rich contaminated groundwater meets native organic carbon, while M6 is interpreted as an anaerobic dead zone with the lowest inferred iron oxidation, sulfur oxidation, and nitrification. The report places oxidative processes near U3, denitrification near M5, and fermentation near L9 along an inferred sequence of O₂ → NO₃⁻ → Fe(III) → SO₄²⁻ → fermentation. These environmental assignments are hypotheses based on taxonomy-to-trait inference and await geochemical validation. [src: enigma_sso_asv_ecology]

### Groundwater versus sediment communities

Groundwater and sediment communities collected at the same well differed substantially, with median Bray–Curtis dissimilarity = 0.424 and within-well values ranging from 0.364–0.450 across 5 wells. Groundwater was enriched in *Rhodanobacter* (sediment 1.23%, groundwater 3.62%, 2.9×), *Gallionella* (0.01%, 0.14%, 8.9×), and *Sideroxydans* (0.01%, 0.06%, 7.0×), while sediment was enriched in *Anaeromyxobacter* (1.24%, 0.03%, 0.02× in groundwater), *Arcobacter* (0.54%, 0.00%, 0×), and *Ca. Methanoperedens* (0.42%, 0.00%, 0×). *Geobacter* was 0.00% in sediment and 0.01% in groundwater, reported as 5.5× enriched in groundwater. [src: enigma_sso_asv_ecology]

The report interprets groundwater enrichment in denitrifiers and iron oxidizers as a plume-associated planktonic assemblage, while sediment enrichment in anaerobic taxa indicates attached and planktonic communities are distinct rather than representing simple detachment. [src: enigma_sso_asv_ecology]

### Metabolic guild associations

Across 9 wells, 65 annotated genera were assigned to 11 metabolic guilds. Guild co-occurrence analysis found nitrifier × iron oxidizer correlation ρ = +0.95, syntroph × fermenter ρ = +0.55, fermenter × predator (*Bdellovibrio*) ρ = +0.85, denitrifier × syntroph ρ = −0.67, and sulfate reducer × aerobic heterotroph ρ = −0.75. These associations are interpreted as inferred functional coupling or spatial separation across the redox gradient, not as direct interaction measurements. [src: enigma_sso_asv_ecology]

### Groundwater temporal stability

Groundwater communities from 5 wells sampled 9 days apart, on September 9 and September 18, 2024, showed well identity explaining 49.9% of variance (p = 0.001), filter size explaining 10.1% (p = 0.001), depth within the saturated zone explaining 2.5% (p = 0.430), and date explaining 0.8% (p = 0.998). Median Bray–Curtis variation was 0.351 temporally, 0.750 between filter sizes, and 0.917 spatially. The date-1 versus date-2 distance matrices had Mantel ρ = 0.867 (p = 0.001), indicating that well-to-well similarity rankings were nearly unchanged over the 9-day interval. [src: enigma_sso_asv_ecology]

This result supports persistent spatial structure at the 9-day groundwater timescale, but it does not establish long-term stability or resolve sediment temporal dynamics. Sediment cores were collected once per well during February–March 2023, and groundwater was sampled in September 2024, creating an 18-month material-and-time offset. [src: enigma_sso_asv_ecology]

## Caveats and Testable Predictions

Direct SSO geochemistry is unavailable in the analyzed dataset: 221 geochemistry sample tubes are registered in CORAL, but metals, ion chromatography/total organic carbon, isotopes, ammonia, and nitrite measurements have not been loaded. Consequently, the proposed northeast-to-southwest plume, the M5 mixing-zone interpretation, the M6 plume-core interpretation, and the inferred redox ladder are environmental hypotheses based on community composition and trait inference. [src: enigma_sso_asv_ecology]

Groundwater ASV coverage exists for only 5 of 9 wells—L7, L9, M4, M6, and U2—and excludes the critical inferred hotspot wells M5 and U3. Pump-test ASV data from Brick 460-462 for L8, M5, and U2 remains available for future extraction. The predicted groundwater pattern is that *Rhodanobacter* will be highest at M5 and lower at L8 and U2. [src: enigma_sso_asv_ecology]

Genus-level functional annotation covered only 21% of total reads, with 65 of 1,038 genera annotated; the report therefore treats process abundance estimates as lower bounds. Genus-level taxonomy covered 44% of sediment reads, species-level classification was approximately 0%, and 56% of reads remained outside the genus-level inference. Class-level traits had 78% coverage and showed consistent redox patterns, but the report recommends sensitivity analysis against the lower-coverage genus-level results. [src: enigma_sso_asv_ecology]

Trait scores at phylum and class levels are consensus estimates rather than empirical measurements of the specific SSO populations, and functional assignments are based on literature-linked taxonomy rather than direct genomic evidence. Metagenomics at the same spatial resolution is proposed to test these assignments and recover functional capacity from reads not classified at genus level. [src: enigma_sso_asv_ecology]

The sediment–groundwater comparison is confounded by the 18-month sampling offset, sediment has no within-well temporal replication, and seasonal or plume dynamics could affect the comparison. The report also notes that the single sediment timepoint cannot assess temporal dynamics, while the 9-day groundwater result cannot establish stability across seasons or longer plume fluctuations. [src: enigma_sso_asv_ecology]

The most direct resolving analyses are to load the 221 SSO geochemistry samples into CORAL; test whether nitrate, pH, and metal concentrations form the predicted northeast-to-southwest gradient; examine nearby EU/ED well metals from the 100WS/27WS bricks; extract pump-test ASVs from Brick 460-462; analyze the 18 M6-C2 isolate genomes for anaerobic metabolisms; perform weighted UniFrac using ASV sequences from Bricks 457/460/477; and repeat 16S profiling across seasons. [src: enigma_sso_asv_ecology]

## Slots Into

- [[concepts/ecotype-environment-gene-content]] — supports an environment-linked community-structure model in which hydrogeological zone, depth, spatial arrangement, and inferred plume exposure differentiate microbial assemblages. [src: enigma_sso_asv_ecology]
- [[concepts/subsurface-bacillota-specialization]] — contributes depth-associated enrichment of Firmicutes and a subsurface redox-gradient interpretation, while emphasizing that the functional assignments are inferred rather than directly measured. [src: enigma_sso_asv_ecology]
- [[concepts/environmental-resistome]] — provides a contamination-plume framework linking metal-rich groundwater, spatial microbial turnover, and plume-associated taxa, without direct resistome measurements. [src: enigma_sso_asv_ecology]
- [[concepts/multi-omics-integration]] — identifies the missing geochemistry, metagenomics, isolate-genome, and phylogenetic community data needed to validate 16S-based functional inference. [src: enigma_sso_asv_ecology]
