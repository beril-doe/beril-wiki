---
type: "Finding"
description: "nifH showed no significant association with ipdC (OR = 1.13, q = 0.54)."
finding_id: "pgp_pangenome_ecology--7e9e60f9"
result: "null result"
source: "pgp_pangenome_ecology"
quantities: [{"value": "OR = 1.13", "what": "nifH \u00d7 ipdC odds ratio", "unit": "", "denominator": "", "scope": ""}, {"value": "q = 0.54", "what": "BH-FDR q-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Only 214/11,272 species (1.9%) carry ipdC, limiting statistical power for the H4 stratified analysis."
first_added: "2026-11-24"
source_hash: "8319f0fcf3c6f5a2997e4444496c7d59bb5d956e8bfc9aab5ed472003d02a946"
---
# nifH shows no association with ipdC

nifH showed no significant association with ipdC (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology]

## Key figures

- **OR = 1.13**: nifH × ipdC odds ratio [src: pgp_pangenome_ecology]
- **q = 0.54**: BH-FDR q-value [src: pgp_pangenome_ecology]

## Evidence

> In contrast, nifH (nitrogen fixation) was significantly **negatively** associated with both hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19), and showed no significant association with ipdC (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology]

From the report [[summaries/pgp_pangenome_ecology__REPORT]].

## Caveat

Only 214/11,272 species (1.9%) carry ipdC, limiting statistical power for the H4 stratified analysis. [src: pgp_pangenome_ecology]

> Only 214/11,272 species (1.9%) carry ipdC, limiting statistical power for the H4 stratified analysis. [src: pgp_pangenome_ecology]

## Other caveats in this report

- The phylum-plus-soil logistic Model 3 failed because ipdC rarity across phyla (214 species, 1.9%) caused quasi-complete separation, so conclusions rely on Model 1 (trp only) and Model 2 (trp + is_soil). [src: pgp_pangenome_ecology]
- The RESEARCH_PLAN estimated ~1,913 nifH clusters, whereas the actual count was 2,756 (43% higher), attributed to incremental growth of the GTDB r214 pangenome; the report states that this discrepancy does not affect any analysis and is documented in NB01 cell 4. [src: pgp_pangenome_ecology]
- The report considers the acdS and pqqC rhizosphere enrichment effects (ORs of 7.0 and 2.9) likely underestimates because many soil isolates have broader environmental labels. [src: pgp_pangenome_ecology]
- pqqD is an outlier to the predominantly core PGP pattern, with 55.5% core versus 63–81% for other PGP genes and the highest singleton fraction of 27.5%, suggesting occasional horizontal spread as a standalone gene. [src: pgp_pangenome_ecology]
- The PGP H4 tyrosine negative control failed, with OR = 3.62 comparable to trp OR = 2.81. [src: pgp_pangenome_ecology]
