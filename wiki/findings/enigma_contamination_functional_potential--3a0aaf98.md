---
type: "Finding"
description: "ENIGMA mapping yielded 150 unique-clade genera versus 530 mapped genera total."
finding_id: "enigma_contamination_functional_potential--3a0aaf98"
result: "observation"
source: "enigma_contamination_functional_potential"
quantities: [{"value": "150", "what": "unique-clade genera", "unit": "genera", "denominator": "530 mapped genera total", "scope": "ENIGMA"}]
caveat: "862/1,392 observed genera were unmapped to current pangenome bridge."
first_added: "2026-11-24"
source_hash: "4dcb3d9608b4e864e109a4e0ca80952e30f26797b2d3de85a58962f773ba79f1"
---
# Most ENIGMA genera lack a unique clade mapping

ENIGMA mapping yielded 150 unique-clade genera versus 530 mapped genera total. [src: enigma_contamination_functional_potential]

## Key figures

- **150 genera**: unique-clade genera (denominator 530 mapped genera total; scope ENIGMA) [src: enigma_contamination_functional_potential]

## Evidence

> - Unique-clade genera: 150 (vs 530 mapped genera total) [src: enigma_contamination_functional_potential]

From the report [[summaries/enigma_contamination_functional_potential__REPORT]].

## Caveat

862/1,392 observed genera were unmapped to current pangenome bridge. [src: enigma_contamination_functional_potential]

> - 862/1,392 observed genera were unmapped to current pangenome bridge. [src: enigma_contamination_functional_potential]

## Other caveats in this report

- The report cautions that ENIGMA species-proxy high-coverage tests are underpowered (n=1), while coverage-aware models increase effective rows at fraction level. [src: enigma_contamination_functional_potential]
- No ENIGMA species-proxy high-coverage subset test was feasible at mapped_abundance_fraction >= 0.25 because retained coverage was low. [src: enigma_contamination_functional_potential]
- The report suggests that current ENIGMA taxonomy granularity means stricter taxonomic resolution sharply reduces analyzable signal without yet strengthening inference. [src: enigma_contamination_functional_potential]
- The ENIGMA result is compatible with functionally redundant contamination-driven taxonomic turnover or effects at species, strain, or pathway resolution too fine for the mapping. [src: enigma_contamination_functional_potential]
- The ENIGMA bridge and annotation stack depends on GTDB and eggNOG conventions, and genus-level broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential]
