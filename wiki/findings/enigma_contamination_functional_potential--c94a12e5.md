---
type: "Finding"
description: "Mean ENIGMA mapped abundance fraction was 0.031 in species-proxy mode versus 0.343 in strict/relaxed modes."
finding_id: "enigma_contamination_functional_potential--c94a12e5"
result: "observation"
source: "enigma_contamination_functional_potential"
quantities: [{"value": "0.031", "what": "mean mapped abundance fraction, species-proxy", "unit": "", "denominator": "", "scope": "ENIGMA"}, {"value": "0.343", "what": "mean mapped abundance fraction, strict/relaxed", "unit": "", "denominator": "", "scope": "ENIGMA"}]
caveat: "Species-proxy high-coverage tests are underpowered (n=1), while coverage-aware models increase effective rows at fraction level."
first_added: "2026-11-24"
source_hash: "4dcb3d9608b4e864e109a4e0ca80952e30f26797b2d3de85a58962f773ba79f1"
---
# Species-proxy mode retains far less abundance coverage

Mean ENIGMA mapped abundance fraction was 0.031 in species-proxy mode versus 0.343 in strict/relaxed modes. [src: enigma_contamination_functional_potential]

## Key figures

- **0.031**: mean mapped abundance fraction, species-proxy (scope ENIGMA) [src: enigma_contamination_functional_potential]
- **0.343**: mean mapped abundance fraction, strict/relaxed (scope ENIGMA) [src: enigma_contamination_functional_potential]

## Evidence

> - Mean mapped abundance fraction in species-proxy mode: 0.031 (vs 0.343 in strict/relaxed) [src: enigma_contamination_functional_potential]

From the report [[summaries/enigma_contamination_functional_potential__REPORT]].

## Caveat

Species-proxy high-coverage tests are underpowered (n=1), while coverage-aware models increase effective rows at fraction level. [src: enigma_contamination_functional_potential]

> This keeps exploratory interpretation calibrated: coverage-aware models increase effective rows (fraction-level), while species-proxy high-coverage tests are underpowered (`n=1`). [src: enigma_contamination_functional_potential]

## Other caveats in this report

- No ENIGMA species-proxy high-coverage subset test was feasible at mapped_abundance_fraction >= 0.25 because retained coverage was low. [src: enigma_contamination_functional_potential]
- The report suggests that current ENIGMA taxonomy granularity means stricter taxonomic resolution sharply reduces analyzable signal without yet strengthening inference. [src: enigma_contamination_functional_potential]
- The ENIGMA result is compatible with functionally redundant contamination-driven taxonomic turnover or effects at species, strain, or pathway resolution too fine for the mapping. [src: enigma_contamination_functional_potential]
- The ENIGMA bridge and annotation stack depends on GTDB and eggNOG conventions, and genus-level broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential]
- ENIGMA taxonomy table ddt_brick0000454 provides labels only through Genus, preventing direct true species-level bridge testing in this dataset slice. [src: enigma_contamination_functional_potential]
