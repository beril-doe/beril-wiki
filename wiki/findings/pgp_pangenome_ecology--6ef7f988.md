---
type: "Finding"
description: "acdS enrichment in soil/rhizosphere species survives phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61) and holds in a strict rhizosphere-only sensitivity analysis using genomes with \"rhizosphere\" or \"root nodule\" in their isolation source (OR = 10.6, q = 7.6e-38)."
finding_id: "pgp_pangenome_ecology--6ef7f988"
result: "observation"
source: "pgp_pangenome_ecology"
quantities: [{"value": "6.98", "what": "odds ratio for acdS soil enrichment with phylum-level fixed effects", "unit": "odds ratio", "denominator": "", "scope": "logistic regression, soil/rhizosphere vs other species"}, {"value": "10.6", "what": "odds ratio for acdS in strict rhizosphere/root-nodule sensitivity analysis", "unit": "odds ratio", "denominator": "", "scope": "genomes with \"rhizosphere\" or \"root nodule\" in isolation source"}, {"value": "4.8e-61", "what": "p-value of the phylum-controlled model", "unit": "", "denominator": "", "scope": ""}]
caveat: "Environment classification relies on noisy ncbi_isolation_source metadata and a clinically and host-biased NCBI sample, with only 5.9% of species soil/rhizosphere-dominant, so the soil enrichment effects are likely underestimates."
first_added: "2026-10-27"
source_hash: "8319f0fcf3c6f5a2997e4444496c7d59bb5d956e8bfc9aab5ed472003d02a946"
---
# ACC deaminase gene strongly enriched in soil species, surviving phylum controls

acdS enrichment in soil/rhizosphere species survives phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61) and holds in a strict rhizosphere-only sensitivity analysis using genomes with "rhizosphere" or "root nodule" in their isolation source (OR = 10.6, q = 7.6e-38). [src: pgp_pangenome_ecology]

## Key figures

- **6.98 odds ratio**: odds ratio for acdS soil enrichment with phylum-level fixed effects (scope logistic regression, soil/rhizosphere vs other species) [src: pgp_pangenome_ecology]
- **10.6 odds ratio**: odds ratio for acdS in strict rhizosphere/root-nodule sensitivity analysis (scope genomes with "rhizosphere" or "root nodule" in isolation source) [src: pgp_pangenome_ecology]
- **4.8e-61**: p-value of the phylum-controlled model [src: pgp_pangenome_ecology]

## Evidence

> The acdS enrichment is particularly striking: ACC deaminase is 7× more prevalent in soil/rhizosphere species than in other environments and the effect survives phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61). The enrichment also holds in a strict rhizosphere-only sensitivity analysis using only genomes with "rhizosphere" or "root nodule" in their isolation source (acdS OR = 10.6, q = 7.6e-38). [src: pgp_pangenome_ecology]

From the report [[summaries/pgp_pangenome_ecology__REPORT]].

## Caveat

Environment classification relies on noisy ncbi_isolation_source metadata and a clinically and host-biased NCBI sample, with only 5.9% of species soil/rhizosphere-dominant, so the soil enrichment effects are likely underestimates. [src: pgp_pangenome_ecology]

> 1. **Environment classification**: Only 5.9% of species are soil/rhizosphere-dominant. ncbi_isolation_source is noisy and NCBI is heavily biased toward clinical and host-associated isolates. The soil enrichment effects are likely underestimates. [src: pgp_pangenome_ecology]

## Other caveats in this report

- The reported ranking is internally awkward: pqqC + acdS is called most common at n = 153, while nifH + pqqC is called next at n = 225. [src: pgp_pangenome_ecology]
- The report gives pqqC–acdS co-occurrence as n = 286 in one section but pqqC + acdS as n = 153 in its trait-combination section; it does not explain the differing counts. [src: pgp_pangenome_ecology]
- The report attributes overall soil depletion of nifH partly to database composition: most nitrogen fixers represented are aquatic/marine, including cyanobacteria and Azotobacter, or host-associated rhizobia. [src: pgp_pangenome_ecology]
- The proposed plant-exudate explanation for the soil-specific trp–ipdC reversal is explicitly speculative. [src: pgp_pangenome_ecology]
- The phylum-plus-soil logistic model failed because of quasi-complete separation; ipdC occurred in 214 species (1.9%), so conclusions rely on simpler models. [src: pgp_pangenome_ecology]
