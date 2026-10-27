---
type: "Finding"
description: "Among 823 species with \u22655 genomes in \u22652 environments, clinical-genome fraction correlates with AMR-cluster count (Spearman rho = 0.465, p = 2.2\u00d710\u207b\u2074\u2075), clinical-dominated species have 4.4\u00d7 more AMR clusters (mean 72.9 vs 16.4, MWU p = 2\u00d710\u207b\u00b9\u2078), and the continuous correlation of clinical fraction with % accessory is borderline (rho = 0.065, p = 0.064)."
finding_id: "amr_environmental_resistome--96de8ae3"
result: "observation"
source: "amr_environmental_resistome"
quantities: [{"value": "rho = 0.465", "what": "Spearman correlation of clinical-genome fraction with total AMR cluster count", "unit": "", "denominator": "823 species", "scope": "species with \u22655 genomes in \u22652 environments"}, {"value": "72.9 vs 16.4", "what": "mean AMR clusters, clinical-dominated vs environmental-dominated species", "unit": "clusters", "denominator": "", "scope": "4.4\u00d7 difference"}, {"value": "rho = 0.065", "what": "correlation of clinical fraction with % accessory AMR", "unit": "", "denominator": "823 species", "scope": "p = 0.064, borderline"}]
caveat: "This is a species-level proxy analysis, not a true per-genome within-species comparison, which the report says would require billion-row joins."
first_added: "2026-10-27"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Clinical-dominated species carry several-fold more AMR clusters than environmental-dominated ones

Among 823 species with ≥5 genomes in ≥2 environments, clinical-genome fraction correlates with AMR-cluster count (Spearman rho = 0.465, p = 2.2×10⁻⁴⁵), clinical-dominated species have 4.4× more AMR clusters (mean 72.9 vs 16.4, MWU p = 2×10⁻¹⁸), and the continuous correlation of clinical fraction with % accessory is borderline (rho = 0.065, p = 0.064). [src: amr_environmental_resistome]

## Key figures

- **rho = 0.465**: Spearman correlation of clinical-genome fraction with total AMR cluster count (denominator 823 species; scope species with ≥5 genomes in ≥2 environments) [src: amr_environmental_resistome]
- **72.9 vs 16.4 clusters**: mean AMR clusters, clinical-dominated vs environmental-dominated species (scope 4.4× difference) [src: amr_environmental_resistome]
- **rho = 0.065**: correlation of clinical fraction with % accessory AMR (denominator 823 species; scope p = 0.064, borderline) [src: amr_environmental_resistome]

## Evidence

> Among 823 species with genomes in ≥2 environments (≥5 genomes each), the fraction of genomes from clinical sources strongly predicts total AMR cluster count (Spearman rho = 0.465, p = 2.2×10⁻⁴⁵). Clinical-dominated species have **4.4× more AMR clusters** (mean 72.9 vs 16.4, MWU p = 2×10⁻¹⁸) and a higher fraction of accessory AMR in a grouped comparison (93.6% vs 81.7%, MWU p = 0.004). The continuous correlation of clinical fraction with % accessory is borderline (rho = 0.065, p = 0.064). [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

This is a species-level proxy analysis, not a true per-genome within-species comparison, which the report says would require billion-row joins. [src: amr_environmental_resistome]

> **Note**: This is a species-level proxy analysis, not a true per-genome within-species comparison (which would require billion-row joins). We test whether species whose genomes are predominantly from clinical sources carry more AMR than species whose genomes are predominantly from environmental sources. [src: amr_environmental_resistome]

## Other caveats in this report

- The report interprets core AMR as chromosomally encoded/intrinsic and accessory AMR as mobile/acquired by analogy to Jiang et al. (2024); it does not establish those mechanisms for every cluster here. [src: amr_environmental_resistome]
- The report proposes niche-specific selection and links it to amr_fitness_cost (metal 44% accessory versus efflux 13% core); the proposed ecological cause is an interpretation rather than a direct test here. [src: amr_environmental_resistome]
- 15,550 AMR clusters (18.7%) could not be assigned a mechanism from gene name or product annotation and were excluded from mechanism fractions. Tetracycline genes were divided between efflux tet(A-E,K,L) and target modification tet(M,O,Q,W). [src: amr_environmental_resistome]
- AlphaEarth analysis has limited interpretability because embedding dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- This interpretation calls soil and aquatic metal-resistance genes more often core, whereas an earlier passage calls metal resistance accessory; the conflict is unresolved. [src: amr_environmental_resistome]
