---
type: "Finding"
description: "AMR genes are significantly less conserved than the pangenome average: only 30.3% are core vs 46.8% baseline (OR=0.49, chi-squared=23,117, p\u22480)."
finding_id: "amr_pangenome_atlas--51bb47e1"
result: "observation"
source: "amr_pangenome_atlas"
quantities: [{"value": "30.3%", "what": "share of AMR genes that are core", "unit": "percent", "denominator": "", "scope": ""}, {"value": "46.8%", "what": "baseline core share", "unit": "percent", "denominator": "", "scope": ""}, {"value": "OR=0.49", "what": "odds ratio of AMR being core", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 83K AMRFinderPlus hits are not all antibiotic resistance, because the scope includes mercury and arsenic stress-response genes."
first_added: "2026-11-24"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# AMR genes are depleted from the core genome across the atlas

AMR genes are significantly less conserved than the pangenome average: only 30.3% are core vs 46.8% baseline (OR=0.49, chi-squared=23,117, p≈0). [src: amr_pangenome_atlas]

## Key figures

- **30.3%**: share of AMR genes that are core [src: amr_pangenome_atlas]
- **46.8%**: baseline core share [src: amr_pangenome_atlas]
- **OR=0.49**: odds ratio of AMR being core [src: amr_pangenome_atlas]

## Evidence

> AMR genes are significantly less conserved than the pangenome average: only **30.3% are core** vs 46.8% baseline (OR=0.49, chi-squared=23,117, p≈0). [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

The 83K AMRFinderPlus hits are not all antibiotic resistance, because the scope includes mercury and arsenic stress-response genes. [src: amr_pangenome_atlas]

> **AMRFinderPlus scope**: Includes stress response genes (mercury, arsenic) alongside classical antibiotic resistance — the 83K hits are not all "antibiotic" resistance per se [src: amr_pangenome_atlas]

## Other caveats in this report

- Of 14,723 AMR-carrying bacterial species, 7,838 (53.2%) had non-Other/Unknown environment classifications, and the Kruskal-Wallis test used only these species across 6 categories. [src: amr_pangenome_atlas]
- The Other/Unknown environment bin contains 46.8% of AMR-carrying species, reflecting sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- The 100% identity threshold avoids paralog confusion but may undercount fitness effects of closely related variants such as alleles differing by a single synonymous substitution. [src: amr_pangenome_atlas]
- Fitness Browser organisms are predominantly environmental isolates with intrinsic resistance, so fitness costs of recently acquired mobile resistance in clinical pathogens may differ substantially. [src: amr_pangenome_atlas]
- The 22.2% Other/Unclassified category includes products not matching keyword sets, including non-standard ribosomal protection names and novel resistance mechanisms. [src: amr_pangenome_atlas]
