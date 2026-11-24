---
type: "Summary"
description: "Summary of the project SSO Subsurface Community Ecology — Spatial Structure, Functional Gradients, and Hydrogeological Drivers."
doc_type: "short"
full_text: "sources/enigma_sso_asv_ecology__REPORT.md"
---
# SSO Subsurface Community Ecology — Spatial Structure, Functional Gradients, and Hydrogeological Drivers

This page summarises the SSO subsurface community ecology project. It asks how sediment and groundwater microbial communities across a 3×3 well grid (~6 m span) are structured in space, by depth, by function and over time. The report finds significant distance-decay of similarity [src: enigma_sso_asv_ecology] and hydrogeological-zone structure in sediment. [src: enigma_sso_asv_ecology] Groundwater communities at 5 wells were stable over 9 days, with well identity dominating and date not detectable. [src: enigma_sso_asv_ecology] The report interprets the functional pattern as following a contamination plume and a redox ladder. [src: enigma_sso_asv_ecology] The spatial alignment tests are marginal or null [src: enigma_sso_asv_ecology], and the functional results are inferred from taxonomy with partial coverage. [src: enigma_sso_asv_ecology] No SSO geochemistry has been loaded into the KBase Data Lakehouse, so all environmental inferences rest on community composition and the plume model awaits geochemical confirmation. [src: enigma_sso_asv_ecology]

## Key Findings

### Spatial structure

Mean Bray-Curtis (BC) dissimilarity is 0.747, from 0.558 for U3–M6 to 0.872 for U3–L9. [src: enigma_sso_asv_ecology] The spatial analysis used 9 wells, 23,458 ASVs (amplicon sequence variants) and 37 sediment core samples aggregated per well. [src: enigma_sso_asv_ecology] It reported significant distance-decay (Mantel ρ = 0.323, p = 0.029). [src: enigma_sso_asv_ecology] NMDS stress is low (0.067) [src: enigma_sso_asv_ecology], but Procrustes correspondence with the physical grid is only marginal (m² = 0.379, p = 0.080). [src: enigma_sso_asv_ecology] Turnover is not aligned with the hillslope (uphill-downhill Mantel ρ = −0.049, p = 0.580). [src: enigma_sso_asv_ecology] The report instead links it to the east-west axis (column Mantel ρ = 0.227, p = 0.092) and reads this as a lateral structuring force rather than topography-driven hydrology. [src: enigma_sso_asv_ecology] The east-west result is not significant at 0.05. [src: enigma_sso_asv_ecology] The report calls meter-scale turnover noteworthy, since most subsurface distance-decay studies operate at kilometer scales, and concludes that plumes can structure communities at sub-decameter resolution. [src: enigma_sso_asv_ecology] See [[concepts/meter-scale-spatial-structure-and-distance-decay-of-subsurface-communities]].

### Plume-aligned corridor

Wells U3, M6 and L7 are far more similar to one another than their distances predict. [src: enigma_sso_asv_ecology] The U3-M6-L7 corridor had the 3 most negative residuals. [src: enigma_sso_asv_ecology] The pairs are U3–M6 (BC = 0.558, residual = −0.170, the most similar pair in the grid) [src: enigma_sso_asv_ecology], M6–L7 (BC = 0.615, residual = −0.154) [src: enigma_sso_asv_ecology] and U3–L7 (BC = 0.646, residual = −0.133). [src: enigma_sso_asv_ecology] The report interprets this diagonal corridor from northeast to southwest as shared exposure to a plume from the Area 3 source. [src: enigma_sso_asv_ecology] Area 3 is described as uphill and northeast of the SSO, with high nitrate, low pH and heavy metals. [src: enigma_sso_asv_ecology] The report places the source at Oak Ridge Reservation Area 3, delivering water with uranium, chromium and nickel. [src: enigma_sso_asv_ecology] The largest dissimilarity, U3–M4 (BC = 0.871, residual = +0.105), is described as spanning the plume entry point to the well farthest from the plume core. [src: enigma_sso_asv_ecology] U3–M4 and U3–L9 had the most positive residuals. [src: enigma_sso_asv_ecology]

The report's overall explanatory model is a plume entering from the northeast and flowing southwest through the saturated zone. [src: enigma_sso_asv_ecology] In that model the plume enters near U3 and flows diagonally toward L7, creating the Column 3 corridor. [src: enigma_sso_asv_ecology] It explains greater east-west turnover by a lateral plume edge, with communities tracking contamination rather than topography. [src: enigma_sso_asv_ecology] It says U3-M6-L7 share composition because they intercept the flow path and share geochemical exposure. [src: enigma_sso_asv_ecology] The report states that the corridor, identified purely from Bray-Curtis patterns, aligns with the expected plume trajectory and shows that 16S similarity can map hydrology at meter scale. [src: enigma_sso_asv_ecology] See [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].

### Depth and hydrogeological zone

In [[entities/permanova]] (permutational multivariate analysis of variance) on 37 sediment core segments, hydrogeological zone (VZ/VSZ/SZ1/SZ2) explains 27.5% of community variance (F = 4.05, p = 0.0001). [src: enigma_sso_asv_ecology] The samples were classified by depth and description into VZ (33), VSZ (25), SZ1 (54) and SZ2 (45). [src: enigma_sso_asv_ecology] Well identity explains 19.2% but is not significant (F = 0.80, p = 0.979, NS). [src: enigma_sso_asv_ecology] Same-well, different-depth samples are nearly maximally dissimilar (median BC = 0.977), while same-depth-zone samples from different wells are more similar (median BC = 0.835). [src: enigma_sso_asv_ecology] The report calls this consistent with plume travel through the saturated zone, with depth controlling plume intersection and horizontal position secondary. [src: enigma_sso_asv_ecology] In its plume model, deep samples are affected and shallow samples represent background. [src: enigma_sso_asv_ecology] It reads the vertical zonation as reflecting plume confinement to the saturated zone, not just generic depth gradients. [src: enigma_sso_asv_ecology] It also asserts that communities above the water table are unaffected by contamination. [src: enigma_sso_asv_ecology]

Ten of 12 dominant phyla show significant depth associations (p < 0.05). [src: enigma_sso_asv_ecology] Shallow-enriched (vadose, oxic) phyla are Chloroflexi (ρ = −0.73) [src: enigma_sso_asv_ecology], Patescibacteria (ρ = −0.70) [src: enigma_sso_asv_ecology], Myxococcota (ρ = −0.54) [src: enigma_sso_asv_ecology] and Spirochaetota (ρ = −0.53). [src: enigma_sso_asv_ecology] Deep-enriched (saturated, anoxic) phyla are Firmicutes (ρ = +0.76) [src: enigma_sso_asv_ecology], WPS-2 (ρ = +0.52) [src: enigma_sso_asv_ecology], Bacteroidota (ρ = +0.50) [src: enigma_sso_asv_ecology] and Proteobacteria (ρ = +0.49). [src: enigma_sso_asv_ecology] See [[concepts/depth-and-hydrogeological-zonation-of-subsurface-microbial-communities]].

### Functional inference and the redox ladder

Multi-resolution functional inference maps processes onto the grid (class level: 22 classes, 78% coverage; genus level: 65 annotated genera, 21% coverage). [src: enigma_sso_asv_ecology] The class-level redox index ranged from 0.047 at M6 to 0.227 at U3. [src: enigma_sso_asv_ecology] The report interprets the spatial distribution of processes as recapitulating the thermodynamic redox ladder expected along a plume. [src: enigma_sso_asv_ecology] It describes the sequence O₂ → NO₃⁻ → Fe(III) → SO₄²⁻ → fermentation running from oxidative U3 through denitrifying M5 to fermentative L9. [src: enigma_sso_asv_ecology] It claims the first spatially explicit mapping of biogeochemical process distributions across the SSO 3×3 grid, inferred from 16S at phylum, class and genus resolution. [src: enigma_sso_asv_ecology] See [[concepts/taxonomy-based-functional-inference-of-biogeochemical-processes-and-the-redox-ladder]].

| Process | Peak well (share) | Genera | Report's interpretation |
|---|---|---|---|
| Denitrification | M5 (7.7%) | Rhodanobacter | Plume mixing zone, NO₃⁻ meets organic C [src: enigma_sso_asv_ecology] |
| Iron oxidation | U3 (2.8%) | Sideroxydans | Plume entry, Fe²⁺ meets O₂ [src: enigma_sso_asv_ecology] |
| Nitrification | U3 (2.3%) | Ca. Nitrosotalea | Plume entry, NH₄⁺ meets O₂ [src: enigma_sso_asv_ecology] |
| Iron reduction | U1 (2.3%) | Anaeromyxobacter | Suboxic, Fe(III) available [src: enigma_sso_asv_ecology] |
| Sulfur oxidation | M4 (1.9%) | Arcobacter, Thiobacillus | Sulfide meets oxygen [src: enigma_sso_asv_ecology] |
| Methanotrophy | M4 (1.9%) | Ca. Methanoperedens | Methane flux from deep zones [src: enigma_sso_asv_ecology] |
| Fermentation | L9 (5.3%) | Spirochaeta, Paenisporosarcina | Terminal reduction, all electron acceptors depleted [src: enigma_sso_asv_ecology] |

Inferred denitrification ranged from 1.9–7.7%, peaking at M5 [src: enigma_sso_asv_ecology], and fermentation from 2.0–5.3%, peaking at L9. [src: enigma_sso_asv_ecology] The central well M5 hosts the highest denitrification potential, which the report calls consistent with nitrate-rich groundwater meeting native organic carbon. [src: enigma_sso_asv_ecology] In the plume model M5 is a mixing zone where nitrate-rich plume water meets native organic carbon. [src: enigma_sso_asv_ecology] The report calls this a prediction awaiting validation once SSO geochemistry is loaded into CORAL. [src: enigma_sso_asv_ecology] The denitrification and iron oxidation hotspot interpretations are based on sediment, and the report says groundwater validation at these wells would substantially strengthen the plume model. [src: enigma_sso_asv_ecology] The report identifies [[entities/rhodanobacter]] as the hallmark denitrifier of the ORR contaminated subsurface, citing Green et al. 2012. [src: enigma_sso_asv_ecology] It states that Rhodanobacter denitrificans reaches 7.7% relative abundance at M5. [src: enigma_sso_asv_ecology] Green et al. (2012) is cited for Rhodanobacter making up to 45% of 16S sequences in low-pH, high-nitrate wells. [src: enigma_sso_asv_ecology] The report reads 7.7% at M5 as moderate plume influence, below the most contaminated Area 2 wells but above background. [src: enigma_sso_asv_ecology] M6 is consistently lowest for iron oxidation, sulfur oxidation and nitrification, and the report characterizes it as an anaerobic dead zone where the plume core has consumed all terminal electron acceptors. [src: enigma_sso_asv_ecology] In the plume model, M6 lies downstream of M5 with denitrification having consumed nitrate, so only fermentative metabolism persists. [src: enigma_sso_asv_ecology]

### Testable predictions of the plume model

The report lists four predictions that would test the plume model. When SSO geochemistry is loaded into CORAL, nitrate, pH and metal levels should show a NE→SW gradient, with highest contamination at U3/M6 and lowest at M4/U1. [src: enigma_sso_asv_ecology] Metals in nearby EU/ED wells (100WS/27WS bricks, 90–120 m NE of SSO) should confirm a plume approaching from the northeast, with concentrations decreasing toward SSO. [src: enigma_sso_asv_ecology] Pump test groundwater in Brick 460-462 (wells L8/M5/U2) should have Rhodanobacter highest at M5, the mixing zone, and lower at L8 and U2. [src: enigma_sso_asv_ecology] The 18 SSO isolate genomes from M6-C2 should encode anaerobic metabolisms, including fermentation and sulfate reduction, consistent with M6's position in the plume core. [src: enigma_sso_asv_ecology]

## Groundwater versus sediment

Groundwater and sediment communities at the same well are substantially different (median BC = 0.424). [src: enigma_sso_asv_ecology] Across the 5 wells with both materials, within-well BC was 0.364–0.450. [src: enigma_sso_asv_ecology] The table gives sediment and groundwater values for selected genera as reported.

| Genus | Process | Sediment | Groundwater | Groundwater enrichment |
|---|---|---|---|---|
| Rhodanobacter | Denitrification | 1.23 | 3.62 | 2.9× [src: enigma_sso_asv_ecology] |
| Gallionella | Iron oxidation | 0.01 | 0.14 | 8.9× [src: enigma_sso_asv_ecology] |
| Sideroxydans | Iron oxidation | 0.01 | 0.06 | 7.0× [src: enigma_sso_asv_ecology] |
| Geobacter | Iron reduction | 0.00 | 0.01 | 5.5× [src: enigma_sso_asv_ecology] |
| Anaeromyxobacter | Iron/U reduction | 1.24 | 0.03 | 0.02× [src: enigma_sso_asv_ecology] |
| Arcobacter | Sulfur oxidation | 0.54 | 0.00 | 0× [src: enigma_sso_asv_ecology] |
| Ca. Methanoperedens | Methane oxidation | 0.42 | 0.00 | 0× [src: enigma_sso_asv_ecology] |

The report interprets the groundwater enrichment of Rhodanobacter, Gallionella and Sideroxydans as organisms thriving in flowing, metal-rich plume water. [src: enigma_sso_asv_ecology] In the plume model, flowing water carries plume-adapted denitrifiers and iron oxidizers while sediment-attached anaerobes remain in biofilms. [src: enigma_sso_asv_ecology] It reads the depletion of sediment-attached anaerobes in groundwater as distinct attached and planktonic communities rather than simple detachment. [src: enigma_sso_asv_ecology] Anaeromyxobacter dehalogenans, at 1.3% mean abundance in SSO sediments, is described as a model ENIGMA organism for iron and uranium reduction. [src: enigma_sso_asv_ecology] Its 41× higher abundance in sediment than groundwater is read as consistent with a biofilm-forming, surface-attached lifestyle. [src: enigma_sso_asv_ecology] The report says its 16S findings complement MRA 2025 work generating 77 sediment and 33 groundwater metagenomes from the ORR. [src: enigma_sso_asv_ecology] See [[concepts/attached-versus-planktonic-communities-in-groundwater-and-sediment]].

## Temporal stability of groundwater

Groundwater communities at 5 wells sampled 9 days apart (Sep 9 vs Sep 18, 2024) showed short-term stability. [src: enigma_sso_asv_ecology] Well identity explained R² = 49.9% (p = 0.001) [src: enigma_sso_asv_ecology] and filter size explained 10.1% (p = 0.001), indicating distinct free-living and particle-associated communities. [src: enigma_sso_asv_ecology] Depth explained 2.5% (p = 0.430) [src: enigma_sso_asv_ecology], and date explained 0.8% (p = 0.998), with no detectable temporal change. [src: enigma_sso_asv_ecology] The variation hierarchy was temporal median BC = 0.351 < filter 0.750 < spatial 0.917. [src: enigma_sso_asv_ecology] Distance matrices from the two dates had Mantel ρ = 0.867 (p = 0.001). [src: enigma_sso_asv_ecology] The report says this strengthens the plume model, indicating persistent environmental structure rather than transient fluctuation. [src: enigma_sso_asv_ecology] It also reads it as persistent geochemical conditions rather than stochastic assembly. [src: enigma_sso_asv_ecology] See [[concepts/temporal-stability-of-groundwater-communities]].

## Guild co-occurrence

Assigning 65 annotated genera to 11 metabolic guilds reveals distinct functional assemblages at each well. [src: enigma_sso_asv_ecology] Across the 9 wells:
- Nitrifiers and iron oxidizers co-occur strongly (ρ = +0.95), both concentrated at U3. [src: enigma_sso_asv_ecology] The report describes them as chemolithotrophs exploiting plume-borne NH₄⁺ and Fe²⁺ [src: enigma_sso_asv_ecology], and as part of a functional network overlaying the redox gradient. [src: enigma_sso_asv_ecology]
- Syntrophs and fermenters co-occur (ρ = +0.55), read as anaerobic food web coupling. [src: enigma_sso_asv_ecology] Fermenters produce organic acids and H₂ that syntrophs consume in obligate partnerships with sulfate reducers or methanogens. [src: enigma_sso_asv_ecology] The report calls this consistent with syntrophic theory, in which syntrophic fatty acid degradation requires H₂, acetate and formate kept at low concentrations. [src: enigma_sso_asv_ecology]
- Fermenters and Bdellovibrio co-occur (ρ = +0.85), read as predators tracking prey biomass. [src: enigma_sso_asv_ecology]
- Denitrifiers and syntrophs show ρ = −0.67, read as mutual exclusion across the redox gradient. [src: enigma_sso_asv_ecology] Denitrifiers thrive where nitrate is available, whereas syntrophs require strictly anaerobic conditions. [src: enigma_sso_asv_ecology] The report says this maps onto canonical contaminated-aquifer redox zonation. [src: enigma_sso_asv_ecology]
- Sulfate reducers and aerobic heterotrophs show ρ = −0.75, read as redox separation at opposite ends of the electron acceptor hierarchy. [src: enigma_sso_asv_ecology]

See [[concepts/metabolic-guild-co-occurrence-and-redox-driven-segregation]].

## Data and Methods

The study uses sediment communities from 9 wells on a 3×3 grid (~6 m span). [src: enigma_sso_asv_ecology] It uses 37 sediment core segments for PERMANOVA [src: enigma_sso_asv_ecology] and compares groundwater and sediment communities at the same well. [src: enigma_sso_asv_ecology] Groundwater stability used 5 wells sampled on two dates. [src: enigma_sso_asv_ecology] Analyses include Mantel tests, Procrustes analysis, NMDS ordination and PERMANOVA. [src: enigma_sso_asv_ecology] Function is inferred from taxonomy at class and genus level. [src: enigma_sso_asv_ecology] The 16S ASV data, sample metadata and well coordinates come from the enigma_coral collection tables sdt_sample, sdt_location, sdt_community, ddt_ndarray, ddt_brick0000457-459 and ddt_brick0000477-479. [src: enigma_sso_asv_ecology]

## Caveats and Open Work

- The Procrustes result (p = 0.080) and the east-west column Mantel (p = 0.092) are marginal and not significant at 0.05. [src: enigma_sso_asv_ecology]
- The hillslope alignment is null [src: enigma_sso_asv_ecology], and well identity is not significant. [src: enigma_sso_asv_ecology]
- Genus-level functional annotation covers only 21% of total reads (65 of 1,038 genera), so process abundance estimates are lower bounds. [src: enigma_sso_asv_ecology] The unclassified 56% of reads could harbor additional functional capacity. [src: enigma_sso_asv_ecology]
- The report recommends assessing this gap by comparing genus-level patterns with class-level traits (78% coverage), which show consistent redox patterns. [src: enigma_sso_asv_ecology]
- Species-level classification is ~0%, and genus level covers only 44% of sediment reads. [src: enigma_sso_asv_ecology]
- Functional inference relies on literature-based trait assignments rather than direct genomic evidence. [src: enigma_sso_asv_ecology] Phylum/class-level trait scores are consensus estimates, not empirical measurements for these populations. [src: enigma_sso_asv_ecology]
- The plume explanations for the corridor, depth pattern and process peaks are the report's interpretations. [src: enigma_sso_asv_ecology] The M5 mixing-zone claim awaits geochemistry validation. [src: enigma_sso_asv_ecology]
- No direct geochemistry is available: 221 SSO sample tubes are registered in CORAL but not loaded. [src: enigma_sso_asv_ecology]
- Sediment cores were collected once per well (Feb-Mar 2023), with no within-well temporal replication. [src: enigma_sso_asv_ecology] A single core sampling event cannot show temporal plume dynamics or community response. [src: enigma_sso_asv_ecology]
- The 18-month offset between sediment (2023) and groundwater (2024) confounds material type with time, limiting cross-material temporal comparisons. [src: enigma_sso_asv_ecology] Seasonal or plume dynamics could confound the comparison. [src: enigma_sso_asv_ecology]
- Only 5 of 9 wells have groundwater ASV data (L7, L9, M4, M6, U2), missing M5 (denitrification hotspot) and U3 (plume entry). [src: enigma_sso_asv_ecology]
- Depth and date effects in groundwater were null (p = 0.430 and p = 0.998). [src: enigma_sso_asv_ecology]

### Proposed next analyses

- Load the 221 registered geochemistry samples (metals, IC/TOC, isotopes, NH₃/NO₂) into CORAL to correlate community composition directly with environmental measurements and validate or refute the plume model. [src: enigma_sso_asv_ecology]
- Extract pump test ASV data from Brick 460-462 (wells L8/M5/U2) [src: enigma_sso_asv_ecology] as a third temporal snapshot (Mar 2024) to test the M5 denitrification hotspot prediction and add temporal resolution. [src: enigma_sso_asv_ecology]
- Use the actual 16S sequences in Bricks 457/460/477 for weighted UniFrac, which may be more sensitive to plume effects than Bray-Curtis on ASV counts. [src: enigma_sso_asv_ecology]
- Run shotgun metagenomics at the same spatial resolution to confirm functional inferences currently based on taxonomy-to-trait mapping [src: enigma_sso_asv_ecology] and to capture the 56% of reads without genus-level classification. [src: enigma_sso_asv_ecology]
- Repeat 16S profiling across seasons and plume dynamics to test whether community structure tracks plume fluctuations in real time. [src: enigma_sso_asv_ecology]

## Slots Into

- [[concepts/meter-scale-spatial-structure-and-distance-decay-of-subsurface-communities]]: significant distance-decay at ~6 m (ρ = 0.323, p = 0.029). [src: enigma_sso_asv_ecology]
- [[concepts/depth-and-hydrogeological-zonation-of-subsurface-microbial-communities]]: hydrogeological zone explains 27.5% of variance, but well identity is not significant. [src: enigma_sso_asv_ecology]
- [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]]: the U3–M6–L7 corridor is read as shared plume exposure [src: enigma_sso_asv_ecology], and the geochemical gradient predictions remain untested. [src: enigma_sso_asv_ecology]
- [[concepts/taxonomy-based-functional-inference-of-biogeochemical-processes-and-the-redox-ladder]]: inferred process peaks are read as following the redox ladder [src: enigma_sso_asv_ecology], with 21% genus read coverage limiting them. [src: enigma_sso_asv_ecology]
- [[concepts/attached-versus-planktonic-communities-in-groundwater-and-sediment]]: median BC = 0.424 between groundwater and sediment at the same well. [src: enigma_sso_asv_ecology]
- [[concepts/metabolic-guild-co-occurrence-and-redox-driven-segregation]]: nitrifier × iron oxidizer ρ = +0.95 and denitrifier × syntroph ρ = −0.67. [src: enigma_sso_asv_ecology]
- [[concepts/temporal-stability-of-groundwater-communities]]: well R² = 49.9% versus date R² = 0.8% over 9 days. [src: enigma_sso_asv_ecology]
- [[concepts/taxonomic-resolution-and-reference-database-limits-in-amplicon-profiling]]: species-level classification is ~0% and genus level covers 44% of sediment reads. [src: enigma_sso_asv_ecology]
