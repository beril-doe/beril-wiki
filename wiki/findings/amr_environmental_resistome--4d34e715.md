---
type: "Finding"
description: "Clinical species have a median of 5 AMR gene clusters versus 2 for soil, aquatic, and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4\u00d710\u207b\u00b9\u2076\u2077, \u03b7\u00b2 = 0.056), human gut species are similar to clinical (median 5), 13 of 15 pairwise environment comparisons are significant after FDR correction, and the largest effect is clinical vs aquatic (rank-biserial r = \u22120.49)."
finding_id: "amr_environmental_resistome--4d34e715"
result: "observation"
source: "amr_environmental_resistome"
quantities: [{"value": "5", "what": "median AMR gene clusters in clinical species", "unit": "clusters", "denominator": "", "scope": "clinical species; soil, aquatic and host-associated median is 2"}, {"value": "\u03b7\u00b2 = 0.056", "what": "Kruskal-Wallis effect size for AMR cluster count across environments", "unit": "", "denominator": "", "scope": "H = 781.9"}, {"value": "13 of 15", "what": "pairwise environment comparisons significant after FDR correction", "unit": "", "denominator": "15 pairwise comparisons", "scope": ""}, {"value": "\u22120.49", "what": "rank-biserial r for clinical vs aquatic, the largest effect", "unit": "", "denominator": "", "scope": ""}]
caveat: "Clinical isolates are massively overrepresented in NCBI, and the clinical enrichment partly reflects that clinical species are the ones that get sequenced because they have AMR, while soil and aquatic species are undersampled."
first_added: "2026-10-27"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Clinical species carry more AMR gene clusters than soil or aquatic species

Clinical species have a median of 5 AMR gene clusters versus 2 for soil, aquatic, and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056), human gut species are similar to clinical (median 5), 13 of 15 pairwise environment comparisons are significant after FDR correction, and the largest effect is clinical vs aquatic (rank-biserial r = −0.49). [src: amr_environmental_resistome]

## Key figures

- **5 clusters**: median AMR gene clusters in clinical species (scope clinical species; soil, aquatic and host-associated median is 2) [src: amr_environmental_resistome]
- **η² = 0.056**: Kruskal-Wallis effect size for AMR cluster count across environments (scope H = 781.9) [src: amr_environmental_resistome]
- **13 of 15**: pairwise environment comparisons significant after FDR correction (denominator 15 pairwise comparisons) [src: amr_environmental_resistome]
- **−0.49**: rank-biserial r for clinical vs aquatic, the largest effect [src: amr_environmental_resistome]

## Evidence

> Species from clinical sources have a median of **5 AMR gene clusters**, compared to 2 for soil, aquatic, and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056). Human gut species are similar to clinical (median 5). Of 15 pairwise environment comparisons, 13 are significant after FDR correction. The largest effect is clinical vs aquatic (rank-biserial r = −0.49). [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

Clinical isolates are massively overrepresented in NCBI, and the clinical enrichment partly reflects that clinical species are the ones that get sequenced because they have AMR, while soil and aquatic species are undersampled. [src: amr_environmental_resistome]

> 2. **NCBI sampling bias**: Clinical isolates are massively overrepresented in NCBI. The "clinical species carry more AMR" finding partly reflects that clinical species are the ones that get sequenced because they have AMR. Soil and aquatic species are undersampled. [src: amr_environmental_resistome]

## Other caveats in this report

- The report interprets core AMR as chromosomally encoded/intrinsic and accessory AMR as mobile/acquired by analogy to Jiang et al. (2024); it does not establish those mechanisms for every cluster here. [src: amr_environmental_resistome]
- The report proposes niche-specific selection and links it to amr_fitness_cost (metal 44% accessory versus efflux 13% core); the proposed ecological cause is an interpretation rather than a direct test here. [src: amr_environmental_resistome]
- 15,550 AMR clusters (18.7%) could not be assigned a mechanism from gene name or product annotation and were excluded from mechanism fractions. Tetracycline genes were divided between efflux tet(A-E,K,L) and target modification tet(M,O,Q,W). [src: amr_environmental_resistome]
- H4 is a species-level proxy, not a per-genome within-species comparison; the report says the latter would require billion-row joins. [src: amr_environmental_resistome]
- AlphaEarth analysis has limited interpretability because embedding dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
