---
type: "Finding"
description: "AlphaEarth embedding analysis (2,684 species with \u22653 genomes and embeddings) reveals that environmental diversity strongly predicts AMR count (Spearman rho=0.466, p=1.6e-144)."
finding_id: "amr_pangenome_atlas--ccd6e57f"
result: "observation"
source: "amr_pangenome_atlas"
quantities: [{"value": "rho=0.466", "what": "Spearman correlation of environmental diversity with AMR count", "unit": "", "denominator": "", "scope": ""}, {"value": "2,684", "what": "species analysed", "unit": "species", "denominator": "", "scope": ""}]
caveat: "Only 28% of genomes have AlphaEarth embeddings, biased toward genomes with geographic metadata."
first_added: "2026-11-24"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# Environmental diversity strongly predicts AMR count per species

AlphaEarth embedding analysis (2,684 species with ≥3 genomes and embeddings) reveals that environmental diversity strongly predicts AMR count (Spearman rho=0.466, p=1.6e-144). [src: amr_pangenome_atlas]

## Key figures

- **rho=0.466**: Spearman correlation of environmental diversity with AMR count [src: amr_pangenome_atlas]
- **2,684 species**: species analysed [src: amr_pangenome_atlas]

## Evidence

> **AlphaEarth embedding analysis** (2,684 species with ≥3 genomes and embeddings) reveals that **environmental diversity strongly predicts AMR count** (Spearman rho=0.466, p=1.6e-144). [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

Only 28% of genomes have AlphaEarth embeddings, biased toward genomes with geographic metadata. [src: amr_pangenome_atlas]

> **AlphaEarth coverage**: Only 28% of genomes have embeddings, biased toward genomes with geographic metadata [src: amr_pangenome_atlas]

## Other caveats in this report

- Of 14,723 AMR-carrying bacterial species, 7,838 (53.2%) had non-Other/Unknown environment classifications, and the Kruskal-Wallis test used only these species across 6 categories. [src: amr_pangenome_atlas]
- The Other/Unknown environment bin contains 46.8% of AMR-carrying species, reflecting sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- The 100% identity threshold avoids paralog confusion but may undercount fitness effects of closely related variants such as alleles differing by a single synonymous substitution. [src: amr_pangenome_atlas]
- Fitness Browser organisms are predominantly environmental isolates with intrinsic resistance, so fitness costs of recently acquired mobile resistance in clinical pathogens may differ substantially. [src: amr_pangenome_atlas]
- The 22.2% Other/Unclassified category includes products not matching keyword sets, including non-standard ribosomal protection names and novel resistance mechanisms. [src: amr_pangenome_atlas]
