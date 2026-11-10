---
type: "Finding"
description: "The tyrosine pathway, intended as a negative control, also predicted ipdC presence at a similar effect size (OR = 3.62, p = 2.3e-11)."
finding_id: "pgp_pangenome_ecology--ac2bd4ee"
result: "null result"
source: "pgp_pangenome_ecology"
quantities: [{"value": "3.62", "what": "odds ratio of tyrosine pathway completeness predicting ipdC", "unit": "odds ratio", "denominator": "", "scope": "negative control"}, {"value": "2.3e-11", "what": "p-value for tyrosine\u2013ipdC", "unit": "", "denominator": "", "scope": ""}]
caveat: "trp and tyr completeness scores are both proxies for overall metabolic pathway completeness, so genome size or total pathway count would need controlling to isolate specific coupling."
first_added: "2026-10-27"
source_hash: "8319f0fcf3c6f5a2997e4444496c7d59bb5d956e8bfc9aab5ed472003d02a946"
---
# Negative-control pathway also predicts ipdC, undermining tryptophan specificity

The tyrosine pathway, intended as a negative control, also predicted ipdC presence at a similar effect size (OR = 3.62, p = 2.3e-11). [src: pgp_pangenome_ecology]

## Key figures

- **3.62 odds ratio**: odds ratio of tyrosine pathway completeness predicting ipdC (scope negative control) [src: pgp_pangenome_ecology]
- **2.3e-11**: p-value for tyrosine–ipdC [src: pgp_pangenome_ecology]

## Evidence

> However, the tyrosine pathway (negative control) also predicts ipdC presence at similar effect size (OR = 3.62, p = 2.3e-11). [src: pgp_pangenome_ecology]

From the report [[summaries/pgp_pangenome_ecology__REPORT]].

## Caveat

trp and tyr completeness scores are both proxies for overall metabolic pathway completeness, so genome size or total pathway count would need controlling to isolate specific coupling. [src: pgp_pangenome_ecology]

> 5. **GapMind confound**: trp and tyr completeness scores are both proxies for overall metabolic pathway completeness. Controlling for genome size or total pathway count would be needed to isolate specific biochemical coupling. [src: pgp_pangenome_ecology]

## Other caveats in this report

- The reported ranking is internally awkward: pqqC + acdS is called most common at n = 153, while nifH + pqqC is called next at n = 225. [src: pgp_pangenome_ecology]
- The report gives pqqC–acdS co-occurrence as n = 286 in one section but pqqC + acdS as n = 153 in its trait-combination section; it does not explain the differing counts. [src: pgp_pangenome_ecology]
- The report attributes overall soil depletion of nifH partly to database composition: most nitrogen fixers represented are aquatic/marine, including cyanobacteria and Azotobacter, or host-associated rhizobia. [src: pgp_pangenome_ecology]
- The proposed plant-exudate explanation for the soil-specific trp–ipdC reversal is explicitly speculative. [src: pgp_pangenome_ecology]
- The phylum-plus-soil logistic model failed because of quasi-complete separation; ipdC occurred in 214 species (1.9%), so conclusions rely on simpler models. [src: pgp_pangenome_ecology]
