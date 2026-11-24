---
type: "Finding"
description: "In the exploratory ENIGMA relaxed_all_clades coverage-adjusted OLS defense analysis, beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462."
finding_id: "enigma_contamination_functional_potential--394f18d0"
result: "observation"
source: "enigma_contamination_functional_potential"
quantities: [{"value": "beta = 0.000751", "what": "coverage-adjusted OLS defense effect", "unit": "", "denominator": "", "scope": "relaxed_all_clades"}, {"value": "q = 0.0462", "what": "FDR q", "unit": "", "denominator": "", "scope": "relaxed_all_clades"}]
caveat: "Exploratory sensitivity-model significance is concentrated in defense and depends on coverage/covariate specification; broader effect across outcomes is not yet established."
first_added: "2026-11-24"
source_hash: "4dcb3d9608b4e864e109a4e0ca80952e30f26797b2d3de85a58962f773ba79f1"
---
# Coverage-adjusted defense association is positive and survives FDR in relaxed mode

In the exploratory ENIGMA relaxed_all_clades coverage-adjusted OLS defense analysis, beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462. [src: enigma_contamination_functional_potential]

## Key figures

- **beta = 0.000751**: coverage-adjusted OLS defense effect (scope relaxed_all_clades) [src: enigma_contamination_functional_potential]
- **q = 0.0462**: FDR q (scope relaxed_all_clades) [src: enigma_contamination_functional_potential]

## Evidence

> - `relaxed_all_clades`: beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462 [src: enigma_contamination_functional_potential]

From the report [[summaries/enigma_contamination_functional_potential__REPORT]].

## Caveat

Exploratory sensitivity-model significance is concentrated in defense and depends on coverage/covariate specification; broader effect across outcomes is not yet established. [src: enigma_contamination_functional_potential]

> - Exploratory sensitivity-model significance is concentrated in defense and depends on coverage/covariate specification; broader effect across outcomes is not yet established. [src: enigma_contamination_functional_potential]

## Other caveats in this report

- The report cautions that ENIGMA species-proxy high-coverage tests are underpowered (n=1), while coverage-aware models increase effective rows at fraction level. [src: enigma_contamination_functional_potential]
- No ENIGMA species-proxy high-coverage subset test was feasible at mapped_abundance_fraction >= 0.25 because retained coverage was low. [src: enigma_contamination_functional_potential]
- The report suggests that current ENIGMA taxonomy granularity means stricter taxonomic resolution sharply reduces analyzable signal without yet strengthening inference. [src: enigma_contamination_functional_potential]
- The ENIGMA result is compatible with functionally redundant contamination-driven taxonomic turnover or effects at species, strain, or pathway resolution too fine for the mapping. [src: enigma_contamination_functional_potential]
- The ENIGMA bridge and annotation stack depends on GTDB and eggNOG conventions, and genus-level broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential]
