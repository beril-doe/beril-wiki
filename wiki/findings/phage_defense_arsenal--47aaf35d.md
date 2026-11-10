---
type: "Finding"
description: "Across the 7,323 species in the analysis set (species with at least five sequenced genomes), the Spearman correlation between per-species defense-system count and n_prophage_clusters is \u03c1 = 0.609, and the partial \u03c1 remains 0.301 after residualizing on log\u2081\u2080(median genome size) and phylum; this is an association, not a direct measurement of phage pressure."
finding_id: "phage_defense_arsenal--47aaf35d"
result: "observation"
source: "phage_defense_arsenal"
quantities: [{"value": "0.609", "what": "Marginal Spearman \u03c1 between defense-system count and n_prophage_clusters", "unit": "", "denominator": "7,323 species", "scope": "species with at least five sequenced genomes"}, {"value": "0.301", "what": "Partial \u03c1 after residualizing on log\u2081\u2080(median genome size) and phylum", "unit": "", "denominator": "", "scope": "n = 7,323 species"}, {"value": "1.6 \u00d7 10\u207b\u00b9\u2075\u00b3", "what": "p-value of the partial correlation", "unit": "", "denominator": "", "scope": ""}]
caveat: "Phylum is controlled only categorically, not finer phylogenetic structure, so the results are consistent with but not a formal test of a phylogenetically independent arms race."
first_added: "2026-11-09"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# Defense-system count tracks prophage burden beyond genome size and phylum

Across the 7,323 species in the analysis set (species with at least five sequenced genomes), the Spearman correlation between per-species defense-system count and n_prophage_clusters is ρ = 0.609, and the partial ρ remains 0.301 after residualizing on log₁₀(median genome size) and phylum; this is an association, not a direct measurement of phage pressure. [src: phage_defense_arsenal]

## Key figures

- **0.609**: Marginal Spearman ρ between defense-system count and n_prophage_clusters (denominator 7,323 species; scope species with at least five sequenced genomes) [src: phage_defense_arsenal]
- **0.301**: Partial ρ after residualizing on log₁₀(median genome size) and phylum (scope n = 7,323 species) [src: phage_defense_arsenal]
- **1.6 × 10⁻¹⁵³**: p-value of the partial correlation [src: phage_defense_arsenal]

## Evidence

> Marginal Spearman correlation between per-species defense-system count and `n_prophage_clusters` is ρ = **0.609** (p ≈ 0, n = 7,323). After residualizing on log₁₀(median genome size) and phylum, partial ρ remains **0.301** (p = 1.6 × 10⁻¹⁵³) — a moderate effect that survives the two strongest known confounders. [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

Phylum is controlled only categorically, not finer phylogenetic structure, so the results are consistent with but not a formal test of a phylogenetically independent arms race. [src: phage_defense_arsenal]

> - **No phylogenetically-corrected regression** — partial correlation and neg-binom GLM control for phylum categorically, but not for finer phylogenetic structure. A phylogenetic mixed-effects model with the GTDB tree as the covariance structure would be a stronger arms-race test. The current results should be interpreted as consistent with, but not as a formal test of, a phylogenetically-independent arms race. [src: phage_defense_arsenal]

## Other caveats in this report

- Arms-race and syndrome tests use species with at least five sequenced genomes. [src: phage_defense_arsenal]
- The DISARM accessory-enrichment estimate is likely affected by nonspecific PF00176 DrmB/SNF2 helicase detection. [src: phage_defense_arsenal]
- The report argues that the DISARM per-cluster caveat does not undermine its species-level arms-race and syndrome results. [src: phage_defense_arsenal]
- The arms-race association varies by phylum; the Actinomycetota effect is described as roughly threefold weaker than the Campylobacterota effect. [src: phage_defense_arsenal]
- CRISPR-Cas prevalence is method-dependent: eggNOG description matching gives 96 %, versus ~55 % with Cas1 PF01867. [src: phage_defense_arsenal]
