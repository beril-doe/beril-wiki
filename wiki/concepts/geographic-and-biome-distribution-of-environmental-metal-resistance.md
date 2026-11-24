---
type: "Concept"
description: "Where metal-resistance genes are enriched or depleted across environmental genomes, by grid cell and by biome; stops at causes of the patterns."
sources: ["summaries/metal_resistance_global_biogeography__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
---
# Geographic and biome distribution of environmental metal resistance

Metal-resistance genes are rare across georeferenced environmental metagenome assembled genomes (MAGs), but they cluster in specific grid cells and biomes. [src: metal_resistance_global_biogeography] The evidence comes from one report ([[summaries/metal_resistance_global_biogeography__REPORT]]), with one supporting line from a second. Hotspot patterns are not yet corrected for sampling effort or single-study clustering, so they are descriptive. [src: metal_resistance_global_biogeography]

## Literature Context

Three candidate papers bear on this page, and all three are abstracts only, not full text. The closest is a global study of inland waters. It used 1593 metagenomes to map metal-resistance genes (MRGs) and persistent organic pollutant-transformation genes (POPTGs). The two gene sets co-occurred in a limited number of hosts, mainly Proteobacteria such as Pseudomonas and Acidovorax. That host-restricted pattern covered approximately 3.8% of the total 4129 non-redundant MAGs, even though the genes are ubiquitous in the environment [PMID 42264341](https://pubmed.ncbi.nlm.nih.gov/42264341/). The same paper reports positive correlations between MRG-POPTG co-occurrence and mobile genetic elements. It also generated a global abundance map in which climatic and anthropogenic factors explained hot spots in South Asia, Southeast Asia and South America [PMID 42264341](https://pubmed.ncbi.nlm.nih.gov/42264341/).

Two other papers report metal-resistance genes only incidentally. A catalogue of 998 ruminant gut archaeal genomes found that archaea potentially carry antibiotic and metal resistance genes and mobile genetic elements [PMID 39505912](https://pubmed.ncbi.nlm.nih.gov/39505912/). Stingray epidermal microbiome MAGs all had a high abundance of heavy metal and antibiotic resistance genes. The authors suggest this reflects competition in mucus-supported, fast-growing communities [PMID 36937279](https://pubmed.ncbi.nlm.nih.gov/36937279/). Both reports are host-associated and neither quantifies prevalence by grid cell or biome, so they offer only loose context for the hub's environmental comparisons.

The corpus finding that metal-resistance genes are rare (2.8% of 22,356 georeferenced MAGs) but clustered is consistent in kind with the inland-water result. There, the genes are widespread in the environment but confined to a small fraction of MAGs (approximately 3.8%) [PMID 42264341](https://pubmed.ncbi.nlm.nih.gov/42264341/). The two figures come from different datasets, definitions and habitats, so they should not be treated as a replication. The hub's grid-cell hotspots are the Atacama/Andean region of Chile (OR=9.83), the eastern and central USA, and East/Southeast Asia. The East and Southeast Asia cluster partly overlaps the regions that the inland-water paper links to climatic and anthropogenic drivers. That overlap is suggestive only, because the inland-water map is built on a different dataset. The hub explicitly stops short of causes, and sampling effort and single-study clustering are still unchecked. The overlap therefore cannot be read as support for an anthropogenic explanation.

The hub's biome contrasts are not covered by these candidates. The contrasts are soil enrichment (prevalence 5.8%, OR=5.05), marine depletion (prevalence 1.2%, OR=0.20) and a non-significant rhizosphere difference (OR=0.66, q=0.30). No candidate paper compares soil, marine and rhizosphere prevalence, so these results extend the literature here and are novel within this evidence set. The hub's finding that metal resistance is not uniformly co-distributed with horizontal gene transfer machinery (2.8% metal resistance versus 21.8% type IV secretion system) sits in some tension with the inland-water report. That report links MRG-POPTG co-occurrence to mobile genetic elements, although it addresses a different gene pairing and habitat [PMID 42264341](https://pubmed.ncbi.nlm.nih.gov/42264341/). The tension is unresolved.

## Overall prevalence

In the georeferenced set, 2.8% of 22,356 MAGs with coordinates carry at least one metal resistance type. [src: metal_resistance_global_biogeography] The report says this is substantially lower than implied by reporting on the 30,497 filtered MAG set. [src: metal_resistance_global_biogeography] It also contrasts this figure with 21.8% type IV secretion system (T4SS) prevalence. It concludes that metal-resistance genes (called with [[entities/amrfinderplus]]) and horizontal gene transfer (HGT) machinery are distinct features that are not uniformly co-distributed. [src: metal_resistance_global_biogeography] See also [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]]. The report states that metal-resistant genomes are not uniformly distributed. [src: metal_resistance_global_biogeography]

## Grid-cell hotspots

The analysis used a 5° grid with 289 cells containing at least 5 MAGs. It applied Fisher's exact test with Benjamini–Hochberg (BH) false discovery rate (FDR) correction. [src: metal_resistance_global_biogeography] It found 11 significant hotspots (odds ratio, OR, above 2, q<0.05). [src: metal_resistance_global_biogeography] It also found 3 coldspots (OR below 0.5, q<0.05). [src: metal_resistance_global_biogeography]

- The top hotspot is the Atacama/Andean region of Chile (lat=-25°, lon=-70°). It has 21.8% prevalence, OR=9.83, q=7.6e-12 and n=101 MAGs. [src: metal_resistance_global_biogeography]
- Clusters in the eastern and central USA (lat=40°, lon=-80° and -90°) have OR=7.9 and 6.3. [src: metal_resistance_global_biogeography]
- An East/Southeast Asia cluster (lat=25-30°, lon=105-120°) has OR=4.4–5.9. [src: metal_resistance_global_biogeography]

## Biome contrasts

Biome prevalence was tested against the global baseline with Fisher's exact test and BH FDR correction. [src: metal_resistance_global_biogeography] Soil is significantly enriched (n=7,939 MAGs, prevalence 5.8%, OR=5.05, q=1.8e-82). [src: metal_resistance_global_biogeography] Marine is significantly depleted (n=13,995, prevalence 1.2%, OR=0.20, q=9.2e-80). [src: metal_resistance_global_biogeography] Rhizosphere does not differ significantly from the baseline (n=422, prevalence 1.9%, OR=0.66, q=0.30, not significant). [src: metal_resistance_global_biogeography]

A separate report used biome-stratified phylogenetic generalized least squares (PGLS). It found distinct metal–COG relationships in soil, marine and wastewater. It reads this as environment-specific functional responses, not a universal resistance programme. [src: soil_metal_functional_genomics] See [[summaries/soil_metal_functional_genomics__REPORT]].

## Caveats

The report says hotspot identification and sampling-effort correction are required before regional patterns can be interpreted. [src: metal_resistance_global_biogeography] Expedition-level clustering checks are still pending for the Atacama and USA clusters. [src: metal_resistance_global_biogeography] The report plans to test whether the Atacama hotspot (OR=9.8) and USA clusters are single-study artefacts by checking distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography] Hotspots have not yet been confirmed to persist after normalising by log(n_MAGs). [src: metal_resistance_global_biogeography]

## Open Directions

- Count distinct sample_accession prefixes per hotspot, to test whether the Atacama and USA clusters are single-study artefacts.
- Re-run the grid test with sampling-effort normalisation by log(n_MAGs), to see which hotspots and coldspots survive.
- Check whether the soil enrichment holds within grid cells, to separate biome effects from geography.
- Check how metadata gaps shape the cohort (see [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]]).
