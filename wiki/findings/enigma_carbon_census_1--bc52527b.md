---
type: "Finding"
description: "Phenylethylamine enters the phenylacetyl-CoA (paa) ring-cleavage route, whereas xanthine is a purine (nitrogen) pathway compound mis-included here, so the headline count of carbon-callable compounds is overstated."
finding_id: "enigma_carbon_census_1--bc52527b"
result: "correction"
source: "enigma_carbon_census_1"
quantities: []
caveat: "The carbon-callable set is effectively 8, and the NB03 carbon allowlist has since been corrected to exclude R02107, but the committed tables still list xanthine because they predate that fix and were not regenerated."
first_added: "2026-10-27"
source_hash: "62204d5c4271f61cef9bd5c3aee8b1410bebd0a60d508276d2875691a7194f49"
---
# Xanthine was mis-included as a carbon-catabolic callable compound

Phenylethylamine enters the phenylacetyl-CoA (paa) ring-cleavage route, whereas xanthine is a purine (nitrogen) pathway compound mis-included here, so the headline count of carbon-callable compounds is overstated. [src: enigma_carbon_census_1]

## Evidence

> phenylethylamine enters the phenylacetyl-CoA (*paa*) ring-cleavage route, and xanthine is a purine (nitrogen) pathway mis-included here. [src: enigma_carbon_census_1]

From the report [[summaries/enigma_carbon_census_1__REPORT]].

## Caveat

The carbon-callable set is effectively 8, and the NB03 carbon allowlist has since been corrected to exclude R02107, but the committed tables still list xanthine because they predate that fix and were not regenerated. [src: enigma_carbon_census_1]

> The carbon-callable set is effectively 8 (see Limitations). The NB03 carbon allowlist has since been corrected to exclude R02107; the committed tables still list xanthine because they predate that fix and were not regenerated. [src: enigma_carbon_census_1]

## Other caveats in this report

- Lauric acid's measured-fitness organism is a reference bacterium, not an ENIGMA isolate. [src: enigma_carbon_census_1]
- Resource darkness is not evidence of biological absence; a shallow PubMed title screen yielded zero literature rescues. [src: enigma_carbon_census_1]
- Xanthine's R02107 reaction reflects purine nitrogen acquisition, not carbon catabolism; the effective carbon-callable count is 8 rather than 9. [src: enigma_carbon_census_1]
- The class-gradient analysis is underpowered and confounded by uneven annotation coverage. [src: enigma_carbon_census_1]
- Because rare capacities compress the φ coefficient, the reanalysis used Haldane-corrected odds ratios with 95% confidence intervals and Jaccard indices from saved 2×2 counts. [src: enigma_carbon_census_1]
