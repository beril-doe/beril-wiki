---
type: "Finding"
description: "Among 823 species with genomes in \u22652 environments (\u22655 genomes each), the fraction of genomes from clinical sources predicts total AMR cluster count (Spearman rho = 0.465, p = 2.2\u00d710\u207b\u2074\u2075)."
finding_id: "amr_environmental_resistome--8ab4f4eb"
result: "observation"
source: "amr_environmental_resistome"
quantities: [{"value": "rho = 0.465", "what": "Spearman correlation of clinical fraction with total AMR clusters", "unit": "", "denominator": "", "scope": "823 species"}, {"value": "823", "what": "qualifying species", "unit": "species", "denominator": "", "scope": ""}]
caveat: "This is a species-level proxy analysis, not a true per-genome within-species comparison, which would require billion-row joins."
first_added: "2026-11-24"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Clinical genome fraction predicts species AMR cluster count

Among 823 species with genomes in ≥2 environments (≥5 genomes each), the fraction of genomes from clinical sources predicts total AMR cluster count (Spearman rho = 0.465, p = 2.2×10⁻⁴⁵). [src: amr_environmental_resistome]

## Key figures

- **rho = 0.465**: Spearman correlation of clinical fraction with total AMR clusters (scope 823 species) [src: amr_environmental_resistome]
- **823 species**: qualifying species [src: amr_environmental_resistome]

## Evidence

> Among 823 species with genomes in ≥2 environments (≥5 genomes each), the fraction of genomes from clinical sources strongly predicts total AMR cluster count (Spearman rho = 0.465, p = 2.2×10⁻⁴⁵). [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

This is a species-level proxy analysis, not a true per-genome within-species comparison, which would require billion-row joins. [src: amr_environmental_resistome]

> **Note**: This is a species-level proxy analysis, not a true per-genome within-species comparison (which would require billion-row joins). [src: amr_environmental_resistome]

## Other caveats in this report

- Mechanism fractions exclude 18.7% of AMR clusters (15,550) that could not be classified from gene names or product annotations. [src: amr_environmental_resistome]
- The report says the continuous AlphaEarth analysis confirms discrete environment results but adds limited interpretability because its dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- The report did not test nucleotide identity between soil and clinical resistance genes, although its pangenome framework could identify shared clusters. [src: amr_environmental_resistome]
- In the environmental resistome analysis, environment and phylogeny remain deeply entangled despite family-level control, and some families, including many Enterobacteriaceae, are almost entirely clinical. [src: amr_environmental_resistome]
- The report regards the 14% of families with significant within-family environment effects as its most convincing evidence, but most families span too few environments for testing. [src: amr_environmental_resistome]
