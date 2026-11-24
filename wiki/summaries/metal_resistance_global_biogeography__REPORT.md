---
type: "Summary"
description: "Summary of the project Global Biogeography of Environmental Bacterial Metal Resistance."
doc_type: "short"
full_text: "sources/metal_resistance_global_biogeography__REPORT.md"
---
# Global Biogeography of Environmental Bacterial Metal Resistance

Later spatial results are reported, but the sampling-effort correction and the single-study checks are still pending. [src: metal_resistance_global_biogeography]

## Key Findings

### Data coverage

The report extracted 260,652 environmental MAGs from MGnify, and 30,497 remained after filtering host-associated biomes. [src: metal_resistance_global_biogeography] Of these, 22,356 MAGs have usable coordinates, which is 73.3% coverage. [src: metal_resistance_global_biogeography] ENA batch application programming interface (API) retrieval returned 24,511 sample records, and 16,964 (69.2%) have valid latitude/longitude pairs. [src: metal_resistance_global_biogeography]

The report first read the 30.8% gap as evidence of substantial geographic blind spots for any public-archive global map of metal resistance. [src: metal_resistance_global_biogeography] The spatial analysis corrects this reading. Of 532 MAG grid cells, 0 lack ENA coordinate coverage, so the ENA file covers all areas represented in the MAG coordinate dataset. [src: metal_resistance_global_biogeography] The 30.8% gap (16,964/24,511 valid pairs) is per-sample, not geographic: it reflects samples without coordinates, not grid cells with no samples. [src: metal_resistance_global_biogeography] Which biomes are most underrepresented in geospatial metadata remains an open question. [src: metal_resistance_global_biogeography]

### Global prevalence

Among the 22,356 MAGs with coordinates, 2.8% carry at least one metal resistance type. The report calls metal resistance rare in the global environmental MAG pool. [src: metal_resistance_global_biogeography] It states this is substantially lower than implied by reporting on the 30,497 filtered MAG set. [src: metal_resistance_global_biogeography]

The report contrasts this 2.8% with a 21.8% type IV secretion system (T4SS) prevalence. It concludes that AMRFinderPlus metal-resistance genes and T4SS horizontal-gene-transfer machinery are distinct features that are not uniformly co-distributed. [src: metal_resistance_global_biogeography] See [[entities/amrfinderplus]] and [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]].

### Geographic hotspots

Metal-resistant genomes are not uniformly distributed. [src: metal_resistance_global_biogeography] The regional results below are provisional: the report requires hotspot identification and sampling-effort correction before regional patterns can be interpreted, and it has not yet confirmed that hotspots persist after normalising by log(n_MAGs). [src: metal_resistance_global_biogeography] The hotspot analysis used a 5° grid with 289 cells containing at least 5 MAGs. It applied Fisher's exact test with Benjamini–Hochberg (BH) false discovery rate (FDR) correction. [src: metal_resistance_global_biogeography] It found 11 significant hotspots (odds ratio, OR>2, q<0.05) and 3 coldspots (OR<0.5, q<0.05). [src: metal_resistance_global_biogeography]

- Top hotspot: the Atacama/Andean region of Chile (lat=-25°, lon=-70°), with 21.8% prevalence, OR=9.83, q=7.6e-12, n=101 MAGs. [src: metal_resistance_global_biogeography]
- Eastern and central USA clusters (lat=40°, lon=-80° and -90°): OR=7.9 and 6.3. [src: metal_resistance_global_biogeography]
- East/Southeast Asia cluster (lat=25-30°, lon=105-120°): OR=4.4–5.9. [src: metal_resistance_global_biogeography]

### Biome differences

Biome-stratified prevalence was tested against the global baseline with Fisher's exact test and BH FDR. [src: metal_resistance_global_biogeography] Soil is significantly enriched and marine significantly depleted. Rhizosphere is not significantly different from baseline. [src: metal_resistance_global_biogeography]

| Biome | MAGs | Prevalence | OR | q |
|---|---|---|---|---|
| Soil | 7,939 | 5.8% | 5.05 | 1.8e-82 [src: metal_resistance_global_biogeography] |
| Rhizosphere | 422 | 1.9% | 0.66 | 0.30 (not significant) [src: metal_resistance_global_biogeography] |
| Marine | 13,995 | 1.2% | 0.20 | 9.2e-80 [src: metal_resistance_global_biogeography] |

See [[concepts/geographic-and-biome-distribution-of-environmental-metal-resistance]].

## Data and Methods

The data are environmental MAGs from MGnify ([[entities/kescience-mgnify]]) joined to ENA sample coordinates. [src: metal_resistance_global_biogeography] The drafted global map uses geopandas and matplotlib. It shows metal-resistant MAGs (n_metal_types > 0) against susceptible MAGs, coloured by metal diversity. [src: metal_resistance_global_biogeography]

## Caveats and Open Work

- Regional patterns cannot be interpreted until hotspot identification and sampling-effort correction are done. [src: metal_resistance_global_biogeography]
- Expedition-level clustering checks are pending for the Atacama and USA clusters. [src: metal_resistance_global_biogeography] The report plans to test whether the Atacama hotspot (OR=9.8) and the USA clusters are single-study artefacts by checking distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography]
- The report has not yet confirmed that hotspots persist after normalising by log(n_MAGs). [src: metal_resistance_global_biogeography]
- The map cell has a NameError from a missing import of matplotlib.pyplot. [src: metal_resistance_global_biogeography] Fixing it in the NB01 map cell remains pending for the production figure. [src: metal_resistance_global_biogeography]
- Which biomes are most underrepresented in geospatial metadata is unresolved. [src: metal_resistance_global_biogeography]

## Slots Into

- [[concepts/geographic-and-biome-distribution-of-environmental-metal-resistance]]: soil is enriched (5.8%, OR=5.05), marine is depleted (1.2%, OR=0.20), and 11 hotspots and 3 coldspots appear on the 5° grid, pending sampling-effort correction. [src: metal_resistance_global_biogeography]
- [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]]: the 30.8% ENA gap is per-sample, not geographic, and 73.3% of the environmental MAGs have coordinates. [src: metal_resistance_global_biogeography]
- [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]]: 2.8% metal-resistance prevalence against 21.8% T4SS prevalence shows the two features are not uniformly co-distributed. [src: metal_resistance_global_biogeography]
