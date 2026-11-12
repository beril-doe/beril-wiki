---
type: "Research direction"
description: "Are Oak Ridge groundwater communities stable over days because the hydrology is steady, and do they shift only when water level or flow changes?"
hypothesis: "Community change between sampling dates grows with the preceding change in water level and rainfall, so the nine-day stability reflects a quiet hydrologic period rather than an intrinsically stable community."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Sensor and weather tables are listed, but the number of amplicon dates spanning a recharge event was not visible in the catalog."
databases: ["enigma.continuous_monitoring", "enigma.coral", "enigmay12.weather"]
tables: ["enigma.continuous_monitoring.hazen_aquatroll600_sso_l7_sz1", "enigma.continuous_monitoring.hazen_aquatroll600_sso_l9_sz1", "enigmay12.weather.ddt_weather_hourly_temperature_rain", "enigma.coral.ddt_brick0000476", "enigma.coral.sdt_sample"]
findings: ["enigma_sso_asv_ecology--6ee64744", "enigma_sso_asv_ecology--ab22d581"]
conflicts: []
papers: ["34130083", "38755262", "39998254"]
builds_on: ["findings/enigma_sso_asv_ecology--6ee64744", "findings/enigma_sso_asv_ecology--ab22d581"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does groundwater community turnover occur only after recharge events changing water level?

Are Oak Ridge groundwater communities stable over days because the hydrology is steady, and do they shift only when water level or flow changes?

## Hypothesis

Community change between sampling dates grows with the preceding change in water level and rainfall, so the nine-day stability reflects a quiet hydrologic period rather than an intrinsically stable community.

## Why it matters

The nine-day data show spatial ordering of wells preserved and no date effect, whereas other aquifers shift with recharge. A hydrologic trigger would reconcile the two and tell monitoring programs when to sample.

## How to test it

Pair multi-date amplicon samples from the SSO wells with well-sensor water-level and conductivity records and hourly rainfall, and test whether community dissimilarity between dates rises with water-level change and rainfall in the interval.

## What would support or refute it

Support: dissimilarity between dates increases with recharge-related change. Refute: dissimilarity is unrelated to hydrologic change even across large events, indicating inherent stability or other drivers.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Sensor and weather tables are listed, but the number of amplicon dates spanning a recharge event was not visible in the catalog.

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--6ee64744|Groundwater spatial patterns are stable over nine days]] (Extends retrieved work)
- Finding: [[findings/enigma_sso_asv_ecology--ab22d581|No detectable groundwater community change over nine days]] (Extends retrieved work)

## Closest published work

- [PMID 34130083](https://pubmed.ncbi.nlm.nih.gov/34130083/) Groundwater bacterial communities evolve over time in response to recharge.
- [PMID 38755262](https://pubmed.ncbi.nlm.nih.gov/38755262/) Revealing the hierarchical structure of microbial communities.
- [PMID 39998254](https://pubmed.ncbi.nlm.nih.gov/39998254/) Minimal changes in microbial abundances and diversity over 7 years of emplacement for modules of compacted bentonite exposed to natural groundwater.

PMID 34130083 shows groundwater communities shifting with recharge and 38755262 relates community hierarchy to time and space; neither tests water-level change as the trigger at a contaminated site.
