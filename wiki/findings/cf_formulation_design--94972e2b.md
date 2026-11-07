---
type: "Finding"
description: "In the strict-safety k=3 formulation (M. luteus + N. mucosa + S. salivarius), modeled PA niche coverage rises from 18% to 100%, because M. luteus grows on 9 of PA14's 11 preferred substrates; the 75% figure is the mean of member inhibitions used in formulation scoring under an additive assumption, not inhibition measured for the combined formulation."
finding_id: "cf_formulation_design--94972e2b"
result: "observation"
source: "cf_formulation_design"
quantities: [{"value": "100%", "what": "modeled PA niche coverage of the k=3 formulation", "unit": "%", "denominator": "", "scope": "strict-safety k=3"}, {"value": "9 of PA14's 11", "what": "preferred substrates on which M. luteus grows", "unit": "substrates", "denominator": "11 preferred substrates", "scope": "M. luteus ASMA-2965"}, {"value": "75%", "what": "mean of member inhibitions used in formulation scoring (not measured for the combination)", "unit": "%", "denominator": "", "scope": "k=3"}, {"value": "0.140", "what": "engraftability of the k=3 formulation", "unit": "", "denominator": "", "scope": "k=3"}]
caveat: "Formulation scoring assumes additive inhibition, so the combination's effect equals the mean of its members; if members synergize the score underestimates, and if they antagonize it overestimates."
first_added: "2026-10-27"
source_hash: "06931c95e1ee4b3b3a4a95563e11b057ffbada9817b91426fd15b4be9ef75bfe"
---
# Adding Micrococcus luteus lifts modeled niche coverage to full

In the strict-safety k=3 formulation (M. luteus + N. mucosa + S. salivarius), modeled PA niche coverage rises from 18% to 100%, because M. luteus grows on 9 of PA14's 11 preferred substrates; the 75% figure is the mean of member inhibitions used in formulation scoring under an additive assumption, not inhibition measured for the combined formulation. [src: cf_formulation_design]

## Key figures

- **100%**: modeled PA niche coverage of the k=3 formulation (scope strict-safety k=3) [src: cf_formulation_design]
- **9 of PA14's 11 substrates**: preferred substrates on which M. luteus grows (denominator 11 preferred substrates; scope M. luteus ASMA-2965) [src: cf_formulation_design]
- **75%**: mean of member inhibitions used in formulation scoring (not measured for the combination) (scope k=3) [src: cf_formulation_design]
- **0.140**: engraftability of the k=3 formulation (scope k=3) [src: cf_formulation_design]

## Evidence

> **k=3** — *M. luteus* [ASMA-2965] + *N. mucosa* [ASMA-3643] + *S. salivarius* [ASMA-737]: composite 0.562, **100% PA niche coverage**, 75% mean inhibition, engraftability 0.140. **The minimum viable formulation** — first size to achieve full niche coverage. The dramatic 18% → 100% coverage jump occurs because *M. luteus* grows on 9 of PA14's 11 preferred substrates (including proline, histidine, glutamate, aspartate, arginine, and glucose), covering the amino acid substrates that *N. mucosa* and *S. salivarius* do not reach individually. Its uniquely broad carbon utilization profile — the widest among all strict-safe candidates — closes every remaining PA substrate gap in a single addition. [src: cf_formulation_design]

From the report [[summaries/cf_formulation_design__REPORT]].

## Caveat

Formulation scoring assumes additive inhibition, so the combination's effect equals the mean of its members; if members synergize the score underestimates, and if they antagonize it overestimates. [src: cf_formulation_design]

> **Rationale**: Our formulation scoring assumes additive inhibition — the combination's effect equals the mean of its members. If members synergize, we're underestimating; if they antagonize, we're overestimating. The competition assay tested 3 commensal pairs against PA14 at multiple inoculation densities. [src: cf_formulation_design]

## Other caveats in this report

- Competitive metabolic exclusion is the study's working theory; the listed CF-sputum amino acids are proposed shared resources. [src: cf_formulation_design]
- Selective prebiotic biomass pre-loading is explicitly a hypothesis. [src: cf_formulation_design]
- GTDB taxonomy is used; Pseudomonas_E is a non-aeruginosa clade and should not be merged with P. aeruginosa. [src: cf_formulation_design]
- The three named organisms have the largest reported isolate counts; pathogen oversampling limits interpretation of collection frequencies as natural prevalence. [src: cf_formulation_design]
- Acinetobacter baumannii and Klebsiella pneumoniae are other named reporter pathogens; their distinct profiles limit generalization of the PA14-targeted formulation. [src: cf_formulation_design]
