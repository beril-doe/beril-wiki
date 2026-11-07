---
type: "Finding"
description: "nifH was significantly negatively associated with both hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19)."
finding_id: "pgp_pangenome_ecology--7e9e60f9"
result: "observation"
source: "pgp_pangenome_ecology"
quantities: [{"value": "0.23", "what": "odds ratio of nifH with hcnC co-occurrence", "unit": "odds ratio", "denominator": "", "scope": "pairwise association"}, {"value": "0.57", "what": "odds ratio of nifH with pqqC co-occurrence", "unit": "odds ratio", "denominator": "", "scope": "pairwise association"}, {"value": "5.8e-29", "what": "q-value for nifH\u2013hcnC", "unit": "", "denominator": "", "scope": "BH-FDR"}, {"value": "2.9e-19", "what": "q-value for nifH\u2013pqqC", "unit": "", "denominator": "", "scope": "BH-FDR"}]
caveat: "The nifH analysis has not resolved differences among marine/aquatic, legume-symbiotic, and free-living soil diazotroph guilds in genome structure or plant growth-promoting trait co-occurrence."
first_added: "2026-10-27"
source_hash: "8319f0fcf3c6f5a2997e4444496c7d59bb5d956e8bfc9aab5ed472003d02a946"
---
# Nitrogen fixation gene is negatively associated with other plant-growth genes

nifH was significantly negatively associated with both hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19). [src: pgp_pangenome_ecology]

## Key figures

- **0.23 odds ratio**: odds ratio of nifH with hcnC co-occurrence (scope pairwise association) [src: pgp_pangenome_ecology]
- **0.57 odds ratio**: odds ratio of nifH with pqqC co-occurrence (scope pairwise association) [src: pgp_pangenome_ecology]
- **5.8e-29**: q-value for nifH–hcnC (scope BH-FDR) [src: pgp_pangenome_ecology]
- **2.9e-19**: q-value for nifH–pqqC (scope BH-FDR) [src: pgp_pangenome_ecology]

## Evidence

> In contrast, nifH (nitrogen fixation) was significantly **negatively** associated with both hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19), and showed no significant association with ipdC (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology]

From the report [[summaries/pgp_pangenome_ecology__REPORT]].

## Caveat

The nifH analysis has not resolved differences among marine/aquatic, legume-symbiotic, and free-living soil diazotroph guilds in genome structure or plant growth-promoting trait co-occurrence. [src: pgp_pangenome_ecology]

> 2. **nifH ecological stratification**: The nifH guild analysis deserves deeper investigation — specifically how the marine/aquatic diazotrophs (cyanobacteria, Azotobacter) compare to legume-symbiotic rhizobia vs free-living soil diazotrophs in genome structure and PGP trait co-occurrence. [src: pgp_pangenome_ecology]

## Other caveats in this report

- The reported ranking is internally awkward: pqqC + acdS is called most common at n = 153, while nifH + pqqC is called next at n = 225. [src: pgp_pangenome_ecology]
- The report gives pqqC–acdS co-occurrence as n = 286 in one section but pqqC + acdS as n = 153 in its trait-combination section; it does not explain the differing counts. [src: pgp_pangenome_ecology]
- The report attributes overall soil depletion of nifH partly to database composition: most nitrogen fixers represented are aquatic/marine, including cyanobacteria and Azotobacter, or host-associated rhizobia. [src: pgp_pangenome_ecology]
- The proposed plant-exudate explanation for the soil-specific trp–ipdC reversal is explicitly speculative. [src: pgp_pangenome_ecology]
- The phylum-plus-soil logistic model failed because of quasi-complete separation; ipdC occurred in 214 species (1.9%), so conclusions rely on simpler models. [src: pgp_pangenome_ecology]
