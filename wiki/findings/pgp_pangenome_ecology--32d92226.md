---
type: "Finding"
description: "The strongest positive focal PGP gene association was pqqC \u00d7 acdS (OR = 7.24, n = 286 co-occurring species, q = 1.2e-83)."
finding_id: "pgp_pangenome_ecology--32d92226"
result: "observation"
source: "pgp_pangenome_ecology"
quantities: [{"value": "OR = 7.24", "what": "odds ratio of pqqC \u00d7 acdS co-occurrence", "unit": "", "denominator": "", "scope": "species with at least one PGP gene"}, {"value": "n = 286", "what": "co-occurring species", "unit": "species", "denominator": "", "scope": ""}, {"value": "q = 1.2e-83", "what": "BH-FDR q-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The report proposes examining whether pqqC and acdS are physically co-located or occupy separate loci to distinguish operon linkage from independent co-selection."
first_added: "2026-11-24"
source_hash: "8319f0fcf3c6f5a2997e4444496c7d59bb5d956e8bfc9aab5ed472003d02a946"
---
# pqqC and acdS strongly co-occur across PGP-carrying species

The strongest positive focal PGP gene association was pqqC × acdS (OR = 7.24, n = 286 co-occurring species, q = 1.2e-83). [src: pgp_pangenome_ecology]

## Key figures

- **OR = 7.24**: odds ratio of pqqC × acdS co-occurrence (scope species with at least one PGP gene) [src: pgp_pangenome_ecology]
- **n = 286 species**: co-occurring species [src: pgp_pangenome_ecology]
- **q = 1.2e-83**: BH-FDR q-value [src: pgp_pangenome_ecology]

## Evidence

> The strongest positive association was **pqqC × acdS** (OR = 7.24, n = 286 co-occurring species, q = 1.2e-83), indicating that phosphate solubilization (PQQ cofactor biosynthesis) and ethylene reduction (ACC deaminase) are nearly always found together when either is present. [src: pgp_pangenome_ecology]

From the report [[summaries/pgp_pangenome_ecology__REPORT]].

## Caveat

The report proposes examining whether pqqC and acdS are physically co-located or occupy separate loci to distinguish operon linkage from independent co-selection. [src: pgp_pangenome_ecology]

> 1. **Operonic context of pqqC–acdS co-occurrence**: Determine whether pqqC and acdS are physically co-located on the chromosome (same genomic island or operon) or co-occur between separate loci, distinguishing functional operon linkage from independent co-selection. [src: pgp_pangenome_ecology]

## Other caveats in this report

- The phylum-plus-soil logistic Model 3 failed because ipdC rarity across phyla (214 species, 1.9%) caused quasi-complete separation, so conclusions rely on Model 1 (trp only) and Model 2 (trp + is_soil). [src: pgp_pangenome_ecology]
- The RESEARCH_PLAN estimated ~1,913 nifH clusters, whereas the actual count was 2,756 (43% higher), attributed to incremental growth of the GTDB r214 pangenome; the report states that this discrepancy does not affect any analysis and is documented in NB01 cell 4. [src: pgp_pangenome_ecology]
- The report considers the acdS and pqqC rhizosphere enrichment effects (ORs of 7.0 and 2.9) likely underestimates because many soil isolates have broader environmental labels. [src: pgp_pangenome_ecology]
- pqqD is an outlier to the predominantly core PGP pattern, with 55.5% core versus 63–81% for other PGP genes and the highest singleton fraction of 27.5%, suggesting occasional horizontal spread as a standalone gene. [src: pgp_pangenome_ecology]
- The PGP H4 tyrosine negative control failed, with OR = 3.62 comparable to trp OR = 2.81. [src: pgp_pangenome_ecology]
