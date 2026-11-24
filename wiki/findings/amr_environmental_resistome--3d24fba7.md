---
type: "Finding"
description: "Species from clinical sources have a median of 5 AMR gene clusters, compared to 2 for soil, aquatic, and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4\u00d710\u207b\u00b9\u2076\u2077, \u03b7\u00b2 = 0.056)."
finding_id: "amr_environmental_resistome--3d24fba7"
result: "observation"
source: "amr_environmental_resistome"
quantities: [{"value": "5", "what": "median AMR gene clusters in clinical species", "unit": "clusters", "denominator": "", "scope": "clinical species"}, {"value": "2", "what": "median AMR gene clusters in soil, aquatic, and host-associated species", "unit": "clusters", "denominator": "", "scope": "soil, aquatic, host-associated species"}, {"value": "\u03b7\u00b2 = 0.056", "what": "Kruskal-Wallis effect size", "unit": "", "denominator": "", "scope": ""}]
caveat: "Clinical isolates are massively overrepresented in NCBI and soil and aquatic species are undersampled, so the finding partly reflects that clinical species get sequenced because they have AMR."
first_added: "2026-11-24"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Clinical species carry more AMR gene clusters than environmental species

Species from clinical sources have a median of 5 AMR gene clusters, compared to 2 for soil, aquatic, and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056). [src: amr_environmental_resistome]

## Key figures

- **5 clusters**: median AMR gene clusters in clinical species (scope clinical species) [src: amr_environmental_resistome]
- **2 clusters**: median AMR gene clusters in soil, aquatic, and host-associated species (scope soil, aquatic, host-associated species) [src: amr_environmental_resistome]
- **η² = 0.056**: Kruskal-Wallis effect size [src: amr_environmental_resistome]

## Evidence

> Species from clinical sources have a median of **5 AMR gene clusters**, compared to 2 for soil, aquatic, and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056). [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

Clinical isolates are massively overrepresented in NCBI and soil and aquatic species are undersampled, so the finding partly reflects that clinical species get sequenced because they have AMR. [src: amr_environmental_resistome]

> Clinical isolates are massively overrepresented in NCBI. The "clinical species carry more AMR" finding partly reflects that clinical species are the ones that get sequenced because they have AMR. Soil and aquatic species are undersampled. [src: amr_environmental_resistome]

## Other caveats in this report

- Mechanism fractions exclude 18.7% of AMR clusters (15,550) that could not be classified from gene names or product annotations. [src: amr_environmental_resistome]
- The clinical-exposure analysis is a species-level proxy, not a true per-genome within-species comparison, which the report says would require billion-row joins. [src: amr_environmental_resistome]
- The report says the continuous AlphaEarth analysis confirms discrete environment results but adds limited interpretability because its dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- The report did not test nucleotide identity between soil and clinical resistance genes, although its pangenome framework could identify shared clusters. [src: amr_environmental_resistome]
- In the environmental resistome analysis, environment and phylogeny remain deeply entangled despite family-level control, and some families, including many Enterobacteriaceae, are almost entirely clinical. [src: amr_environmental_resistome]
