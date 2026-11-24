---
type: "Finding"
description: "The overall correlation between pangenome openness and AMR count is near zero (rho=0.006), indicating phylogeny dominates the signal."
finding_id: "amr_pangenome_atlas--012985a7"
result: "null result"
source: "amr_pangenome_atlas"
quantities: [{"value": "rho=0.006", "what": "overall correlation of openness with AMR count", "unit": "", "denominator": "", "scope": ""}]
caveat: "The per-gene and per-phylum tests are exploratory and should be interpreted as hypothesis-generating."
first_added: "2026-11-24"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# Pangenome openness does not correlate with AMR count overall

The overall correlation between pangenome openness and AMR count is near zero (rho=0.006), indicating phylogeny dominates the signal. [src: amr_pangenome_atlas]

## Key figures

- **rho=0.006**: overall correlation of openness with AMR count [src: amr_pangenome_atlas]

## Evidence

> The overall correlation is near zero (rho=0.006), indicating phylogeny dominates the signal. [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

The per-gene and per-phylum tests are exploratory and should be interpreted as hypothesis-generating. [src: amr_pangenome_atlas]

> The per-gene and per-phylum tests are exploratory and should be interpreted as hypothesis-generating [src: amr_pangenome_atlas]

## Other caveats in this report

- Of 14,723 AMR-carrying bacterial species, 7,838 (53.2%) had non-Other/Unknown environment classifications, and the Kruskal-Wallis test used only these species across 6 categories. [src: amr_pangenome_atlas]
- The Other/Unknown environment bin contains 46.8% of AMR-carrying species, reflecting sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- The 100% identity threshold avoids paralog confusion but may undercount fitness effects of closely related variants such as alleles differing by a single synonymous substitution. [src: amr_pangenome_atlas]
- Fitness Browser organisms are predominantly environmental isolates with intrinsic resistance, so fitness costs of recently acquired mobile resistance in clinical pathogens may differ substantially. [src: amr_pangenome_atlas]
- The 22.2% Other/Unclassified category includes products not matching keyword sets, including non-standard ribosomal protection names and novel resistance mechanisms. [src: amr_pangenome_atlas]
