---
type: "Finding"
description: "acdS prevalence was 15.8% in soil/rhizosphere species versus 2.6% in other environments (Odds Ratio 7.02, q-value 5.1e-62)."
finding_id: "pgp_pangenome_ecology--5c6dd1c3"
result: "observation"
source: "pgp_pangenome_ecology"
quantities: [{"value": "15.8%", "what": "acdS prevalence in soil/rhizosphere species", "unit": "", "denominator": "", "scope": ""}, {"value": "2.6%", "what": "acdS prevalence in other environments", "unit": "", "denominator": "", "scope": ""}, {"value": "7.02", "what": "odds ratio", "unit": "", "denominator": "", "scope": ""}]
caveat: "The report considers the acdS and pqqC rhizosphere enrichment effects (ORs of 7.0 and 2.9) likely underestimates because many soil isolates have broader environmental labels."
first_added: "2026-11-24"
source_hash: "8319f0fcf3c6f5a2997e4444496c7d59bb5d956e8bfc9aab5ed472003d02a946"
---
# acdS is strongly enriched in soil and rhizosphere species

acdS prevalence was 15.8% in soil/rhizosphere species versus 2.6% in other environments (Odds Ratio 7.02, q-value 5.1e-62). [src: pgp_pangenome_ecology]

## Key figures

- **15.8%**: acdS prevalence in soil/rhizosphere species [src: pgp_pangenome_ecology]
- **2.6%**: acdS prevalence in other environments [src: pgp_pangenome_ecology]
- **7.02**: odds ratio [src: pgp_pangenome_ecology]

## Evidence

> | acdS | 15.8% | 2.6% | **7.02** | 5.1e-62 | [src: pgp_pangenome_ecology]

From the report [[summaries/pgp_pangenome_ecology__REPORT]].

## Caveat

The report considers the acdS and pqqC rhizosphere enrichment effects (ORs of 7.0 and 2.9) likely underestimates because many soil isolates have broader environmental labels. [src: pgp_pangenome_ecology]

> The acdS and pqqC enrichment effects (ORs of 7.0 and 2.9) are therefore likely underestimates of the true rhizosphere enrichment, since many soil isolates are deposited under broader "environmental" labels. [src: pgp_pangenome_ecology]

## Other caveats in this report

- The phylum-plus-soil logistic Model 3 failed because ipdC rarity across phyla (214 species, 1.9%) caused quasi-complete separation, so conclusions rely on Model 1 (trp only) and Model 2 (trp + is_soil). [src: pgp_pangenome_ecology]
- The RESEARCH_PLAN estimated ~1,913 nifH clusters, whereas the actual count was 2,756 (43% higher), attributed to incremental growth of the GTDB r214 pangenome; the report states that this discrepancy does not affect any analysis and is documented in NB01 cell 4. [src: pgp_pangenome_ecology]
- pqqD is an outlier to the predominantly core PGP pattern, with 55.5% core versus 63–81% for other PGP genes and the highest singleton fraction of 27.5%, suggesting occasional horizontal spread as a standalone gene. [src: pgp_pangenome_ecology]
- The PGP H4 tyrosine negative control failed, with OR = 3.62 comparable to trp OR = 2.81. [src: pgp_pangenome_ecology]
- The report says a better H4 test requires controlling for overall genome completeness, using size and COG coverage, to separate aromatic-pathway effects from general metabolic capacity. [src: pgp_pangenome_ecology]
