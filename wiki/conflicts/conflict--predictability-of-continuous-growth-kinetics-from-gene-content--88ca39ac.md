<!-- tension-hash: 88ca39acfb60b369 -->
# Tension: GC Content as a Confound Versus an Unclear Input in Growth-Kinetics Prediction

The concept [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content]] reports that continuous growth kinetics (growth rate µmax, lag time and yield) could not be predicted from KEGG ortholog (KO) presence/absence or from bulk genome features when whole genera were held out. The ENIGMA report reads this null as biological, not as a data shortfall. [src: genotype_to_phenotype_enigma] Two pieces of evidence complicate that reading. A different project found that GC content (the fraction of G and C bases in a genome) confounds cross-species comparisons, with GC content varying 31–73%. [src: pitfalls] Separately, the ENIGMA report is inconsistent about whether GC% was used at all. The disagreement matters because it leaves open whether a missing or inconsistently handled feature bears on how the null is read. That is an unresolved hypothesis, not an established finding.

## Evidence Sides

**Side A: GC content is a known confound that could matter**

- In cf_formulation_design, cross-species codon usage bias (CUB) comparisons were confounded by GC content, which varied 31–73%. [src: pitfalls]
- CUB is considered meaningful only within species or across species with similar GC content. [src: pitfalls]
- Limit: these claims concern cross-species comparisons in another project. They do not show how GC content would affect the proposed ENIGMA test. [src: pitfalls]

**Side B: the ENIGMA null stands, but its GC% handling is inconsistent**

- GC% is listed among the bulk-feature regression inputs. [src: genotype_to_phenotype_enigma]
- GC% is also described as not computed and available for only 32/727 genomes. [src: genotype_to_phenotype_enigma]
- The report treats the kinetics null across two model types as biological, not as a data shortfall. [src: genotype_to_phenotype_enigma]

## Possible Reconciliations

- **Hypothesis 1:** GC% was effectively absent from the bulk-feature models (32/727 genomes), so the bulk-feature null says little about GC. The KO-based null would be unaffected. This is untested.
- **Hypothesis 2:** GC% was in the regression inputs, and the null holds with it included. The "not computed" statement would then describe a different step or a documentation error. This is untested.
- **Hypothesis 3:** The cross-species GC confound in cf_formulation_design is specific to CUB and does not carry over to growth-kinetics prediction. Under this hypothesis the two sets of claims do not conflict.
- **Hypothesis 4:** Incomplete GC% handling leaves a data gap that partly shapes the null. This is an unresolved possibility, and the ENIGMA report does not support it.

## Resolving Work

- Data: the ENIGMA genome feature tables and notebook logs. Method: audit which genomes have GC% and which regressions used it. Question: was GC% an input, and for how many of the 727 genomes?
- Data: GC% computed from the genome sequences themselves. Method: rerun the bulk-feature regression under cross-genus holdout (whole genera held out) with complete GC%. Question: does the kinetics null persist?
- Data: the same strains' kinetics parameters. Method: test the residuals of the kinetics models for correlation with GC%. Question: does GC content structure the errors?
- Data: the cf_formulation_design CUB analysis. Method: compare it against the ENIGMA feature set. Question: does any feature in the ENIGMA test behave like CUB, which is GC-sensitive?
- Data: only strains with similar GC content. Method: repeat the prediction within that restricted set. Question: does the null hold when the confound is limited?
