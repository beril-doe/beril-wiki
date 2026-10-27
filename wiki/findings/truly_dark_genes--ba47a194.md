---
type: "Finding"
description: "The four annotation tiers contain 246 (3.8%) no-clue genes, 3,867 (60.2%) with sequence identifiers only, 711 (11.1%) with partial function, and 1,603 (24.9%) with phenotype-only signal."
finding_id: "truly_dark_genes--ba47a194"
result: "observation"
source: "truly_dark_genes"
quantities: [{"value": "246", "what": "truly dark genes with no clues (Tier 1)", "unit": "genes", "denominator": "", "scope": ""}, {"value": "3,867", "what": "truly dark genes with sequence identifiers only (Tier 2)", "unit": "genes", "denominator": "", "scope": ""}, {"value": "711", "what": "truly dark genes with partial function (Tier 3)", "unit": "genes", "denominator": "", "scope": ""}, {"value": "1,603", "what": "truly dark genes with phenotype-only signal (Tier 4)", "unit": "genes", "denominator": "", "scope": ""}]
caveat: "Some bakta hypothetical-protein calls may be false negatives, being genes with known functions that did not match bakta's PSC database at the version tested (v6.0)."
first_added: "2026-10-23"
source_hash: "c3c61898305ee30bac02c9a1ff4d8c27bd21313ee4b736ea0055ea6d9014adf0"
---
# Most truly dark genes carry some clue; few are completely dark

The four annotation tiers contain 246 (3.8%) no-clue genes, 3,867 (60.2%) with sequence identifiers only, 711 (11.1%) with partial function, and 1,603 (24.9%) with phenotype-only signal. [src: truly_dark_genes]

## Key figures

- **246 genes**: truly dark genes with no clues (Tier 1) [src: truly_dark_genes]
- **3,867 genes**: truly dark genes with sequence identifiers only (Tier 2) [src: truly_dark_genes]
- **711 genes**: truly dark genes with partial function (Tier 3) [src: truly_dark_genes]
- **1,603 genes**: truly dark genes with phenotype-only signal (Tier 4) [src: truly_dark_genes]

## Evidence

> | Tier 1: No clues | 246 | 3.8% | Completely dark — no sequence IDs, no hits, no phenotype | | Tier 2: Minimal | 3,867 | 60.2% | Sequence identifiers only (UniRef50/RefSeq) | | Tier 3: Partial function | 711 | 11.1% | Pfam, COG, or eggNOG functional description | | Tier 4: Phenotype only | 1,603 | 24.9% | Fitness/essential/module signal but no functional annotation | [src: truly_dark_genes]

From the report [[summaries/truly_dark_genes__REPORT]].

## Caveat

Some bakta hypothetical-protein calls may be false negatives, being genes with known functions that did not match bakta's PSC database at the version tested (v6.0). [src: truly_dark_genes]

> - **Bakta false negatives**: Some "hypothetical protein" calls may be bakta false negatives — genes with known functions that didn't match bakta's PSC database at the version tested (v6.0). [src: truly_dark_genes]

## Other caveats in this report

- Extrapolating the 16.3% truly-dark rate to 17,479 unlinked genes yields an estimated ~2,841 additional truly dark genes, including 2,208 with strong fitness phenotypes; the ranked list is estimated to cover ~69% of the total population. [src: truly_dark_genes]
- The report interprets shorter length, accessory-genome enrichment, GC deviation, mobile-element proximity, and narrow taxonomic breadth as consistent with recent acquisition and rapid evolution; this is an inference rather than a direct transfer measurement. [src: truly_dark_genes]
- The 41% hypothetical-neighbor pattern suggests genomic dark islands; recent acquisition, phage derivation, and species-specific neighborhoods are proposed origins, not demonstrated ones. [src: truly_dark_genes]
- Inter-species interaction, novel metabolism, and community-specific behavior are hypotheses proposed to explain community/nutrient enrichment, not established gene functions. [src: truly_dark_genes]
- 17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta; ~2,841 potentially truly dark genes among them are extrapolated, yielding a stated 31% prioritization coverage gap. [src: truly_dark_genes]
