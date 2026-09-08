---
type: Organism
description: Microbacterium, an informative genus for model-error follow-up
sources:
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
title: Microbacterium
---
# Microbacterium

## Identity

**Canonical name:** Microbacterium. [^genotype_to_phenotype_enigma]

**Known aliases:** No alternative name or abbreviation was reported in the source document. [^genotype_to_phenotype_enigma]

**Stable external identifier:** No stable external identifier was reported in the source document. [^genotype_to_phenotype_enigma]

Microbacterium is a bacterial genus represented in the ENIGMA genome-by-condition prediction analysis. [^genotype_to_phenotype_enigma]

## Evidence from genotype_to_phenotype_enigma

Microbacterium was one of the genus × condition-class cells in which confident prediction errors were concentrated. [^genotype_to_phenotype_enigma]

The audit covered 42,771 genus-blocked holdout predictions and found 65.1% overall accuracy, 7,844 false positives, and 7,101 false negatives. [^genotype_to_phenotype_enigma]

High-confidence errors were defined as predictions with |p − 0.5| > 0.25; this filter identified 1,276 errors concentrated in several genus × condition-class cells, including Microbacterium on nucleosides. [^genotype_to_phenotype_enigma]

Microbacterium showed growth in 23% of its tested conditions and was selected, alongside [prescottella](prescottella.md), as an especially informative genus for follow-up experiments. [^genotype_to_phenotype_enigma]

The active-learning framework ranked 343 conditions using error rate, model uncertainty, and field relevance, then proposed 50 next experiments; these proposed experiments corresponded to 7,844 current prediction failures. [^genotype_to_phenotype_enigma]

The Microbacterium error pattern supports investigating condition-specific growth capability rather than assuming that genome content alone predicts every phenotype; this relates to [condition-specific-fitness](../concepts/condition-specific-fitness.md). [^genotype_to_phenotype_enigma]

The source document does not report a formal retrospective comparison between the active-learning selections and random selection, so the value of prioritizing Microbacterium for new measurements remains to be tested. [^genotype_to_phenotype_enigma]

## Related source

The full analysis is summarized in [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md). [^genotype_to_phenotype_enigma]

[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
