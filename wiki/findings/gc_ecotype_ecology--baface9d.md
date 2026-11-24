---
type: "Finding"
description: "Adding latitude and longitude to ANI-cluster control retained isolation-category effects at p < 0.05 in 12 (75%) of 16 species with \u2265 30 geo-bearing genomes."
finding_id: "gc_ecotype_ecology--baface9d"
result: "observation"
source: "gc_ecotype_ecology"
quantities: [{"value": "12", "what": "species remaining significant", "unit": "species", "denominator": "16 species with \u2265 30 geo-bearing genomes", "scope": ""}, {"value": "75%", "what": "share remaining significant", "unit": "", "denominator": "16 species", "scope": ""}]
caveat: "Geographic sensitivity was tested for only 16 of 40 species; the remaining 24 had < 30 genomes with parseable lat_lon."
first_added: "2026-11-24"
source_hash: "f773608a1dd497c1ffa1608a83b6cc60f67d2e65041b491508a5d0dcc30163d6"
---
# Geographic covariates leave most isolation-category GC effects intact

Adding latitude and longitude to ANI-cluster control retained isolation-category effects at p < 0.05 in 12 (75%) of 16 species with ≥ 30 geo-bearing genomes. [src: gc_ecotype_ecology]

## Key figures

- **12 species**: species remaining significant (denominator 16 species with ≥ 30 geo-bearing genomes) [src: gc_ecotype_ecology]
- **75%**: share remaining significant (denominator 16 species) [src: gc_ecotype_ecology]

## Evidence

> - **Geographic-bias sensitivity** (`gc ~ C(ani_cluster) + lat + lon + C(iso_category)` vs `gc ~ C(ani_cluster) + lat + lon`): of 16 species with ≥ 30 geo-bearing genomes, **12 (75%) remain p < 0.05**. The within-species iso_category effect is not just a proxy for geographic structure. [src: gc_ecotype_ecology]

From the report [[summaries/gc_ecotype_ecology__REPORT]].

## Caveat

Geographic sensitivity was tested for only 16 of 40 species; the remaining 24 had < 30 genomes with parseable lat_lon. [src: gc_ecotype_ecology]

> **Geographic sensitivity tested only on 16 of 40 species** — the remaining 24 species had < 30 genomes with parseable lat_lon, so the lat/lon-controlled test could not be run. [src: gc_ecotype_ecology]

## Other caveats in this report

- The report states that prior within-species testing has been rare because it requires many genomes per species, genome-level environmental metadata and intra-species phylogenetic control. [src: gc_ecotype_ecology]
- The report dropped 7 species whose genomes collapsed to a single ANI cluster, and 108 species produced valid p-values. [src: gc_ecotype_ecology]
- One primary-significant species had insufficient phylogenetic coverage for the phylogenetic-regression robustness test. [src: gc_ecotype_ecology]
- The report attributes the largest partial R² values to species with many small ANI clusters, where phylogenetic control consumes most degrees of freedom and leaves small but well-determined residual variance, exemplified by Aeromonas veronii with 87 clusters of 122 genomes. [src: gc_ecotype_ecology]
- The proposed mechanistic explanations for ecological GC shifts were not directly tested in this report. [src: gc_ecotype_ecology]
