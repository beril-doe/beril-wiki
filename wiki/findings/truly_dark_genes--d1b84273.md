---
type: "Finding"
description: "Methanococcus strains (S2 and JJ) account for 55% of all truly dark genes, and across organisms 4\u201396% of dark genes resist bakta annotation, with archaeal organisms at the high end."
finding_id: "truly_dark_genes--d1b84273"
result: "observation"
source: "truly_dark_genes"
quantities: [{"value": "55%", "what": "share of all truly dark genes in Methanococcus strains S2 and JJ", "unit": "percent", "denominator": "all truly dark genes", "scope": "Fitness Browser"}, {"value": "4\u201396%", "what": "range across organisms of dark genes resisting bakta annotation", "unit": "percent", "denominator": "dark genes per organism", "scope": "across organisms"}]
caveat: "Some bakta hypothetical-protein calls may be false negatives, being genes with known functions that did not match bakta's PSC database at the version tested (v6.0)."
first_added: "2026-10-23"
source_hash: "c3c61898305ee30bac02c9a1ff4d8c27bd21313ee4b736ea0055ea6d9014adf0"
---
# Archaeal Methanococcus strains dominate the truly dark gene set

Methanococcus strains (S2 and JJ) account for 55% of all truly dark genes, and across organisms 4–96% of dark genes resist bakta annotation, with archaeal organisms at the high end. [src: truly_dark_genes]

## Key figures

- **55%**: share of all truly dark genes in Methanococcus strains S2 and JJ (denominator all truly dark genes; scope Fitness Browser) [src: truly_dark_genes]
- **4–96%**: range across organisms of dark genes resisting bakta annotation (denominator dark genes per organism; scope across organisms) [src: truly_dark_genes]

## Evidence

> Truly dark genes are concentrated in specific organisms: Methanococcus strains (S2 and JJ) account for 55% of all truly dark genes, reflecting the underrepresentation of archaea in annotation databases. Across organisms, 4–96% of dark genes resist bakta annotation, with archaeal organisms at the high end. [src: truly_dark_genes]

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
