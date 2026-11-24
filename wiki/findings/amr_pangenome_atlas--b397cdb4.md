---
type: "Finding"
description: "In the Fitness Browser cross-reference, AMR genes show slightly less fitness cost than the non-AMR baseline (median fitness -0.007 vs -0.012, Mann-Whitney p=3.7e-6)."
finding_id: "amr_pangenome_atlas--b397cdb4"
result: "observation"
source: "amr_pangenome_atlas"
quantities: [{"value": "-0.007", "what": "median fitness of AMR genes", "unit": "", "denominator": "", "scope": ""}, {"value": "-0.012", "what": "median fitness of non-AMR baseline", "unit": "", "denominator": "", "scope": ""}]
caveat: "Fitness Browser organisms are predominantly environmental isolates where intrinsic resistance predominates, so the cost of recently acquired mobile resistance in clinical pathogens may differ substantially."
first_added: "2026-11-24"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# AMR genes carry slightly less lab fitness cost than other genes

In the Fitness Browser cross-reference, AMR genes show slightly less fitness cost than the non-AMR baseline (median fitness -0.007 vs -0.012, Mann-Whitney p=3.7e-6). [src: amr_pangenome_atlas]

## Key figures

- **-0.007**: median fitness of AMR genes [src: amr_pangenome_atlas]
- **-0.012**: median fitness of non-AMR baseline [src: amr_pangenome_atlas]

## Evidence

> Surprisingly, AMR genes show **slightly less fitness cost** than the non-AMR baseline (median fitness -0.007 vs -0.012, Mann-Whitney p=3.7e-6). [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

Fitness Browser organisms are predominantly environmental isolates where intrinsic resistance predominates, so the cost of recently acquired mobile resistance in clinical pathogens may differ substantially. [src: amr_pangenome_atlas]

> Furthermore, the Fitness Browser organisms are predominantly environmental isolates where intrinsic resistance predominates; the fitness cost of recently acquired mobile resistance elements in clinical pathogens may differ substantially. [src: amr_pangenome_atlas]

## Other caveats in this report

- Of 14,723 AMR-carrying bacterial species, 7,838 (53.2%) had non-Other/Unknown environment classifications, and the Kruskal-Wallis test used only these species across 6 categories. [src: amr_pangenome_atlas]
- The Other/Unknown environment bin contains 46.8% of AMR-carrying species, reflecting sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- The 100% identity threshold avoids paralog confusion but may undercount fitness effects of closely related variants such as alleles differing by a single synonymous substitution. [src: amr_pangenome_atlas]
- The 22.2% Other/Unclassified category includes products not matching keyword sets, including non-standard ribosomal protection names and novel resistance mechanisms. [src: amr_pangenome_atlas]
- Genome databases over-represent clinical pathogens, inflating AMR counts for human-associated species. [src: amr_pangenome_atlas]
