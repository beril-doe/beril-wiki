---
type: "Concept"
description: "Covers short-term temporal versus spatial and filter-size variation in groundwater communities, and the lack of temporal replication in sediments."
sources: ["summaries/discoveries.md", "summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Temporal stability of groundwater communities

Groundwater communities at the Subsurface Observatory (SSO) were stable over a 9-day window, and well identity explained far more variation than sampling date. [src: discoveries, enigma_sso_asv_ecology] The evidence is one two-date comparison at 5 wells. [src: enigma_sso_asv_ecology] Sediments have no temporal replication at all. [src: enigma_sso_asv_ecology]

## Literature Context

The candidate papers come from other habitats: geothermal springs, rivers and the hyporheic zone. None of them studies groundwater communities at a contaminated subsurface site. They give indirect context on how temporal and spatial structure trade off in aquatic microbial communities.

A 34-month study of 115 water column samples from 31 geothermal ecosystems found that community abundances changed more readily than composition. A substantial physicochemical disturbance was needed to shift community structure at the phylum level, and communities returned to their pre-disturbance state once conditions re-established [PMID 37020721](https://pubmed.ncbi.nlm.nih.gov/37020721/). In the Dunk River watershed, a metagenomic study of four tributaries found no significant spatial variation in taxonomic composition, and temporal factors were the main identifiable driver. Even so, a substantial majority of the variance was unexplained, which the authors attribute to stochasticity in open riverine systems. The authors suggest that mass effects from water dispersal may override local selection [PMID 42971771](https://pubmed.ncbi.nlm.nih.gov/42971771/). In the Ciliwung River, dry-season groundwater was tightly coupled to the river. Contamination hotspots were more active in the wet season, when hydrological connectivity was higher, so contaminant pathways and microbial source signals varied with season [PMID 31125752](https://pubmed.ncbi.nlm.nih.gov/31125752/). In the hyporheic zone, groundwater-surface water mixing shifted ecological assembly from stochastic to deterministic processes [PMID 27052662](https://pubmed.ncbi.nlm.nih.gov/27052662/).

The corpus finding is that well identity explained R² = 49.9% (p = 0.001) of groundwater community variation at the Subsurface Observatory, while date explained R² = 0.8% (p = 0.998). This rests on one two-date comparison, 9 days apart, at 5 wells. The result is consistent with the geothermal finding that communities are resilient and stable when conditions persist [PMID 37020721](https://pubmed.ncbi.nlm.nih.gov/37020721/). It is also consistent with the idea that persistent environmental conditions drive deterministic structure [PMID 27052662](https://pubmed.ncbi.nlm.nih.gov/27052662/). It differs from the Dunk River results, where space was weak and time was the main identifiable driver [PMID 42971771](https://pubmed.ncbi.nlm.nih.gov/42971771/). That contrast may reflect the open, mixed nature of rivers compared with isolated wells, but this is a hypothesis and the corpus did not test it.

The corpus's reading of the stability as persistent plume-maintained geochemistry is an interpretation, not a direct test. The geothermal study covered 34 months, and the Ciliwung study found seasonal shifts in contamination pathways [PMID 31125752](https://pubmed.ncbi.nlm.nih.gov/31125752/). Both suggest that a 9-day window may miss seasonal change. The corpus's lack of temporal replication in sediments, and its 18-month offset between sediment and groundwater sampling, has no counterpart in these papers. That gap is novel to this corpus and is not addressed by the candidate literature.

## Short-term stability in groundwater

Groundwater communities at 5 wells sampled 9 days apart (Sep 9 vs Sep 18, 2024) showed short-term stability. [src: enigma_sso_asv_ecology] Well identity explained R² = 49.9% (p = 0.001), so spatial identity dominates. [src: enigma_sso_asv_ecology, discoveries] Date explained R² = 0.8% (p = 0.998), with no detectable temporal change. [src: enigma_sso_asv_ecology, discoveries] Depth (SZ) explained R² = 2.5% (p = 0.430), a minor SZ1 vs SZ2 effect in groundwater. [src: enigma_sso_asv_ecology]

## Temporal versus filter-size and spatial variation

The variation hierarchy was temporal (median Bray-Curtis, BC, = 0.351) < filter (0.750) < spatial (0.917). The report reads this as confirming that spatial patterns are temporally stable at the 9-day scale. [src: enigma_sso_asv_ecology] The [[entities/mantel-test]] correlation between date-1 and date-2 distance matrices was ρ = 0.867 (p = 0.001). Which wells are most similar to each other was nearly identical across the two dates. [src: enigma_sso_asv_ecology]

## Interpretation

The report says the spatial signal overwhelms temporal noise at this timescale. It reads this as persistent geochemical conditions rather than stochastic assembly. [src: enigma_sso_asv_ecology] It also says the stability strengthens the plume model: the spatial patterns are persistent environmental structure maintained by the contamination plume, not transient fluctuations. [src: enigma_sso_asv_ecology] This is an interpretation, not a direct test. See [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].

## Sediments lack temporal replication

Sediment cores were collected once per well (Feb-Mar 2023), with no within-well temporal replication. [src: enigma_sso_asv_ecology] A single core sampling event means plume dynamics and community response over time cannot be assessed. [src: enigma_sso_asv_ecology] Sediment (2023) and groundwater (2024) sampling were 18 months apart, so seasonal or plume dynamics could confound the comparison. [src: enigma_sso_asv_ecology] This offset confounds material type with time, so cross-material temporal comparisons need this caveat. [src: enigma_sso_asv_ecology] See also [[concepts/attached-versus-planktonic-communities-in-groundwater-and-sediment]].

## Open Directions

- Resample the same wells over months to years. This would test whether the 9-day stability holds across seasons and plume shifts.
- Collect repeat sediment cores from the same wells. This would give within-well temporal variance for sediment, which is currently missing.
- Sample sediment and groundwater in the same campaign. This would remove the 18-month confound between material type and time.
- Repeat the Mantel and variance-partitioning analysis with more than two dates. This would show whether the between-well similarity pattern persists.
