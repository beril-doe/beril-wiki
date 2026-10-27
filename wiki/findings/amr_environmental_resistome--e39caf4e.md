---
type: "Finding"
description: "Clinical species have 68% accessory (acquired) AMR versus 43% accessory in soil species (Kruskal-Wallis H = 506.0, p = 4\u00d710\u207b\u00b9\u2070\u2077, \u03b7\u00b2 = 0.036)."
finding_id: "amr_environmental_resistome--e39caf4e"
result: "observation"
source: "amr_environmental_resistome"
quantities: [{"value": "68%", "what": "accessory (acquired) share of AMR in clinical species", "unit": "%", "denominator": "", "scope": "clinical species"}, {"value": "43%", "what": "accessory share of AMR in soil species", "unit": "%", "denominator": "", "scope": "soil species"}, {"value": "\u03b7\u00b2 = 0.036", "what": "Kruskal-Wallis effect size", "unit": "", "denominator": "", "scope": "H = 506.0"}]
caveat: "The 95% prevalence threshold for core depends on species genome count, and many species have few genomes, making core/accessory labels imprecise."
first_added: "2026-10-27"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Clinical species' resistomes are mostly accessory, soil's less so

Clinical species have 68% accessory (acquired) AMR versus 43% accessory in soil species (Kruskal-Wallis H = 506.0, p = 4×10⁻¹⁰⁷, η² = 0.036). [src: amr_environmental_resistome]

## Key figures

- **68%**: accessory (acquired) share of AMR in clinical species (scope clinical species) [src: amr_environmental_resistome]
- **43%**: accessory share of AMR in soil species (scope soil species) [src: amr_environmental_resistome]
- **η² = 0.036**: Kruskal-Wallis effect size (scope H = 506.0) [src: amr_environmental_resistome]

## Evidence

> The composition of the resistome differs qualitatively across environments. **Clinical species: 68% accessory (acquired) AMR** vs **soil species: 43% accessory** (Kruskal-Wallis H = 506.0, p = 4×10⁻¹⁰⁷, η² = 0.036). A clear gradient emerges: [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

The 95% prevalence threshold for core depends on species genome count, and many species have few genomes, making core/accessory labels imprecise. [src: amr_environmental_resistome]

> 5. **Core/accessory precision**: The 95% prevalence threshold for "core" depends on species genome count. Many species have few genomes, making core/accessory labels imprecise. [src: amr_environmental_resistome]

## Other caveats in this report

- The report interprets core AMR as chromosomally encoded/intrinsic and accessory AMR as mobile/acquired by analogy to Jiang et al. (2024); it does not establish those mechanisms for every cluster here. [src: amr_environmental_resistome]
- The report proposes niche-specific selection and links it to amr_fitness_cost (metal 44% accessory versus efflux 13% core); the proposed ecological cause is an interpretation rather than a direct test here. [src: amr_environmental_resistome]
- 15,550 AMR clusters (18.7%) could not be assigned a mechanism from gene name or product annotation and were excluded from mechanism fractions. Tetracycline genes were divided between efflux tet(A-E,K,L) and target modification tet(M,O,Q,W). [src: amr_environmental_resistome]
- H4 is a species-level proxy, not a per-genome within-species comparison; the report says the latter would require billion-row joins. [src: amr_environmental_resistome]
- AlphaEarth analysis has limited interpretability because embedding dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
