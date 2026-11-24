---
type: "Concept"
description: "Covers how proximity thresholds linking environmental measurements to genomes and spatial autocorrelation affect attribution of gene-content associations to measured sites; stops at the sensitivity analyses needed."
sources: ["summaries/soil_metal_functional_genomics__REPORT.md"]
---
# Spatial matching of environmental samples to genomes

This page covers how the distance threshold that links soil samples to genomes affects whether gene-content associations can be attributed to the measured sites. The evidence comes from one report, [[summaries/soil_metal_functional_genomics__REPORT]], on [[entities/copper]]. It is a stated caveat with pending checks. No sensitivity result exists yet. [src: soil_metal_functional_genomics]

## Literature Context

The candidate papers do not test proximity thresholds for linking environmental samples to genomes. They show that soil microbial functional genes are spatially structured and tied to local conditions, which is why the matching distance matters.

At a smelting-affected site in Yunnan, heavy metals and metalloids including copper accumulated with depth. Concentrations were significantly lower at upstream and downstream locations. Resistance and virulence genes were co-enriched at the contaminated sites, which suggests co-selection under prolonged stress [PMID 41011342](https://pubmed.ncbi.nlm.nih.gov/41011342/). At a creosote-contaminated site, microbial diversity and PAH catabolic genotypes were patchily distributed. Their hot and cold spots coincided with those of PAH concentration, and gene abundances correlated positively with PAH concentration [PMID 22940734](https://pubmed.ncbi.nlm.nih.gov/22940734/). Gene content can therefore track contaminant levels at fine spatial scales within a single site. Under that kind of patchiness, a genome found several kilometres from a measurement point may not represent the measured conditions.

Larger-scale studies show that climate and soil chemistry also shape functional gene patterns. In 429 low-arsenic paddy soil samples from 39 fields across four climatic zones in China, arsenic detoxification gene abundance was directly affected by average annual temperature (r = 0.21), pH (r = -0.20) and arsenic content (r = -0.11) [PMID 34186083](https://pubmed.ncbi.nlm.nih.gov/34186083/). A New South Wales β-diversity map was driven mainly by pH, effective cation exchange capacity and land surface temperature cycles, and microbial patterns followed soil classes beyond spatial distance and rainfall [PMID 36862079](https://pubmed.ncbi.nlm.nih.gov/36862079/). Nifh-gene diazotroph communities across six North American forests followed taxa-area relationships and latitudinal gradients [PMID 27085668](https://pubmed.ncbi.nlm.nih.gov/27085668/). These results show that spatial structure and covarying environmental factors can confound a single-metal association. They also support checking residual spatial autocorrelation. Field-scale variation matters even for fluxes: composite diversity metrics explained 19-20% of the spatial variation of H2 flux in a cover crop trial [PMID 35092770](https://pubmed.ncbi.nlm.nih.gov/35092770/).

The corpus's copper analysis matched soil samples to KBase genomes within 10 km. It found 116 COGs at FDR below 0.05 across 7,566 samples. The report itself flags that many nearby genomes may not be co-located with the measurements. This caveat is consistent with the literature above, which shows contaminant-linked gene content varying across depth, across a site about 2 km wide, and within a single site. The papers do not set a threshold, and none tests 5 km or 20 km. The sensitivity analysis the corpus calls for is therefore novel relative to these candidates, and they do not settle it. The pending Moran's I check on residuals, with SEVM if significant, is likewise supported only indirectly. The papers show that spatial structure exists but do not evaluate that remedy. The corpus's copper associations stay unattributed to the measured sites until the reruns are done. See [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]].

## Proximity matching in the copper analysis

The copper-specific analysis matches soil samples to KBase genomes with a 10 km proximity criterion. At that distance, many "nearby" genomes may not be co-located with the copper measurements. [src: soil_metal_functional_genomics] The analysis found 116 clusters of orthologous groups (COGs) at a false discovery rate (FDR) below 0.05. It used 7,566 samples that had nearby KBase genomes at 10 km. [src: soil_metal_functional_genomics] These associations are therefore tied to the 10 km choice. The report says sensitivity analysis at 5 km and 20 km is needed before COG-copper associations can be attributed to the measured sites. [src: soil_metal_functional_genomics] See also [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]].

## Spatial autocorrelation

A second pending validation tests spatial autocorrelation. It applies Moran's I to the model residuals and uses SEVM if the result is significant. [src: soil_metal_functional_genomics] Rerunning the copper analysis at 5 km and 20 km also remains pending. [src: soil_metal_functional_genomics]

## Why the checks are not done

No local CSV output of the Spearman ρ values or model residuals is available. These validations cannot be completed without Spark access. [src: soil_metal_functional_genomics]

## Open Directions

- Rerun the copper analysis at 5 km and 20 km. Compare the 116 COGs and the 7,566-sample set with the 10 km result. This tests whether the associations depend on the threshold.
- Export the Spearman ρ values and model residuals to local files. This removes the Spark dependency that blocks the pending checks.
- Compute Moran's I on the residuals. If it is significant, refit with SEVM and see which COG-copper associations survive.
- Report how the share of genomes truly co-located with copper measurements changes with threshold. This addresses the co-location concern at 10 km.
