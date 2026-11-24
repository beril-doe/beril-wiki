---
type: "Finding"
description: "All 10 target species (\u226550 genomes, \u226515 variable pathways) showed meaningful metabolic clustering (all silhouette scores > 0.2)."
finding_id: "metabolic_capability_dependency--94b74df5"
result: "observation"
source: "metabolic_capability_dependency"
quantities: [{"value": "10", "what": "target species with metabolic clustering", "unit": "", "denominator": "", "scope": "\u226550 genomes, \u226515 variable pathways"}, {"value": "> 0.2", "what": "silhouette score for all species", "unit": "", "denominator": "", "scope": ""}]
caveat: "The ecotype analysis is observational, and the environment-cluster correlations in Salmonella and Phenylobacterium may be confounded by phylogenetic structure without explicit phylogenetic correction."
first_added: "2026-11-24"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# All ten target species show distinct metabolic ecotype clustering

All 10 target species (≥50 genomes, ≥15 variable pathways) showed meaningful metabolic clustering (all silhouette scores > 0.2). [src: metabolic_capability_dependency]

## Key figures

- **10**: target species with metabolic clustering (scope ≥50 genomes, ≥15 variable pathways) [src: metabolic_capability_dependency]
- **> 0.2**: silhouette score for all species [src: metabolic_capability_dependency]

## Evidence

> All 10 target species (≥50 genomes, ≥15 variable pathways) showed meaningful metabolic clustering (all silhouette scores > 0.2). [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

The ecotype analysis is observational, and the environment-cluster correlations in Salmonella and Phenylobacterium may be confounded by phylogenetic structure without explicit phylogenetic correction. [src: metabolic_capability_dependency]

> - **Ecotype analysis is observational**: the environment-cluster correlations in *Salmonella* and *Phenylobacterium* suggest causal links to ecological selection, but confounding by phylogenetic structure is possible without explicit phylogenetic correction. [src: metabolic_capability_dependency]

## Other caveats in this report

- Varying the active threshold ±25% (1.5–2.5) and latent threshold ±25% (0.75–1.25) gave latent fractions of 4.7% to 21.1% (SD = 5.9 percentage points across 16 threshold combinations). [src: metabolic_capability_dependency]
- The report states that the large intermediate zone (32.3%) makes the latent fraction moderately sensitive to threshold tightening. [src: metabolic_capability_dependency]
- GapMind deoxyribonate and myoinositol pathways lacked matching SEED subsystem role descriptions and were absent from all analyses. [src: metabolic_capability_dependency]
- Full-name GapMind phenylalanine and tyrosine entries lacked SEED coverage, but their phe and tyr equivalents were included through abbreviation-based matching. [src: metabolic_capability_dependency]
- Alanine appeared in fitness metrics but was excluded from classification for all organisms because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]
