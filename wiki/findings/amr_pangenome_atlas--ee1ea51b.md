---
type: "Finding"
description: "Within phyla, pangenome openness positively correlates with AMR count in 8/10 tested phyla (Bacillota rho=0.219, p=1.0e-16; Bacillota_C rho=0.374, p=3.1e-5), although the overall correlation is near zero (rho=0.006), which the report takes to indicate that phylogeny dominates the signal."
finding_id: "amr_pangenome_atlas--ee1ea51b"
result: "observation"
source: "amr_pangenome_atlas"
quantities: [{"value": "0.006", "what": "overall correlation between openness and AMR count", "unit": "rho", "denominator": "", "scope": ""}, {"value": "8/10", "what": "tested phyla with positive openness\u2013AMR correlation", "unit": "phyla", "denominator": "10 tested phyla", "scope": ""}, {"value": "0.374", "what": "openness\u2013AMR correlation in Bacillota_C", "unit": "rho", "denominator": "", "scope": "p=3.1e-5"}]
caveat: "No Bonferroni or FDR correction was applied, and the per-gene and per-phylum tests are exploratory and should be interpreted as hypothesis-generating."
first_added: "2026-10-27"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# Overall openness–AMR correlation hides positive within-phylum associations

Within phyla, pangenome openness positively correlates with AMR count in 8/10 tested phyla (Bacillota rho=0.219, p=1.0e-16; Bacillota_C rho=0.374, p=3.1e-5), although the overall correlation is near zero (rho=0.006), which the report takes to indicate that phylogeny dominates the signal. [src: amr_pangenome_atlas]

## Key figures

- **0.006 rho**: overall correlation between openness and AMR count [src: amr_pangenome_atlas]
- **8/10 phyla**: tested phyla with positive openness–AMR correlation (denominator 10 tested phyla) [src: amr_pangenome_atlas]
- **0.374 rho**: openness–AMR correlation in Bacillota_C (scope p=3.1e-5) [src: amr_pangenome_atlas]

## Evidence

> Within phyla, pangenome openness positively correlates with AMR count in 8/10 tested phyla, strongest in Bacillota (rho=0.219, p=1.0e-16) and Bacillota_C (rho=0.374, p=3.1e-5). The overall correlation is near zero (rho=0.006), indicating phylogeny dominates the signal. [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

No Bonferroni or FDR correction was applied, and the per-gene and per-phylum tests are exploratory and should be interpreted as hypothesis-generating. [src: amr_pangenome_atlas]

> - **Multiple testing**: The six hypotheses involve many individual tests (per-mechanism binomial tests, per-phylum correlations, per-environment comparisons). Formal Bonferroni or FDR correction was not applied because the primary test p-values are extreme (many < 1e-100) and correction would not change any conclusion. The per-gene and per-phylum tests are exploratory and should be interpreted as hypothesis-generating [src: amr_pangenome_atlas]

## Other caveats in this report

- Environment classification is limited by sparse and inconsistent BioSample isolation-source metadata; 46.8% of species fall in Other/Unknown. [src: amr_pangenome_atlas]
- The 100% identity link threshold may miss close variants, and fitness findings from predominantly environmental Fitness Browser organisms may not generalize to recently acquired mobile resistance in clinical pathogens. [src: amr_pangenome_atlas]
- Mechanism labels were assigned by product-description keywords, not by CARD Antibiotic Resistance Ontology terms. [src: amr_pangenome_atlas]
- The 22.2% unclassified fraction partly reflects keyword-match failures; CARD ARO cross-reference mapping is proposed as a more systematic alternative. [src: amr_pangenome_atlas]
- The authors propose, rather than directly establish, that greater niche breadth enables AMR accumulation through more opportunities for horizontal transfer. [src: amr_pangenome_atlas]
