---
type: "Organism"
description: "Firmicutes model proposed as top new organism for transposon library construction, though not selected by conservation covering-set analysis."
sources: ["summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/thermodynamic_impact__REPORT.md"]
aliases: ["B. subtilis"]
---
# Bacillus subtilis 168

Bacillus subtilis 168 (also B. subtilis) is a Firmicutes model listed with a GramPos template. [src: thermodynamic_impact] The functional_dark_matter report calls it the best-studied Gram-positive model organism and proposes it as the top new organism for library construction, but the covering-set analysis did not select it. [src: functional_dark_matter] In the thermodynamic_impact comparison, Marvin and OPAM2 pKa sources gave 0 flux differences under TMFA (thermodynamics-based metabolic flux analysis) for this organism. [src: thermodynamic_impact]

## Key facts

- The model has 1,033 genes, 1,345 reactions and growth 0.5000. [src: thermodynamic_impact]

## Library construction priority

The functional_dark_matter report ranks B. subtilis 168 as priority 1 among new organisms for library construction. The stated reasons are established RB-TnSeq (random barcode transposon sequencing) protocols and the chance to compare Gram-positive and Gram-negative organisms for DUF484, DUF971 and EamA. The existing Fitness Browser (FB) strain BFirm gave only 5 top-500 genes, and the report suggests a purpose-built library with broader condition screening could expand this. [src: functional_dark_matter]

## Not selected by the covering set

The covering-set algorithm did not pick B. subtilis or Staphylococcus aureus, because their ortholog groups (OGs) are subsets of the coverage already provided by Pseudomonadota. [src: functional_dark_matter, discoveries] The report still says both remain valuable for studying genes in native Gram-positive genomic context. [src: functional_dark_matter] See [[entities/staphylococcus-aureus]] and [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]]. The ranking and the covering-set result thus point in different directions. [src: functional_dark_matter]

## Thermodynamic flux analysis

In the thermodynamic_impact report, B. subtilis showed no Marvin-versus-OPAM2 flux differences. See [[concepts/effect-of-pka-source-on-flux-predictions-across-diverse-organisms]] and thermodynamic constraint formulation in flux balance models. [src: thermodynamic_impact]

- Flux variability analysis (FVA) with hard cutoffs reported 1,337 blocked reactions for each pKa source, with 0 newly blocked and 0 newly unblocked reactions. [src: thermodynamic_impact]
- Growth was 0.5000 unconstrained, 0.5000 with TMFA plus Marvin, and 0.5000 with TMFA plus OPAM2, with 941 constrained reactions. [src: thermodynamic_impact]
- The TMFA impact table reports 1,345 reactions, 941 constrained, 0 flux-changed, 0 newly blocked, 0 newly active, 0 reversed and 0 Marvin-versus-OPAM2 differences. [src: thermodynamic_impact]
- B. subtilis shows 0 flux differences, so the OPAM2 pKa changes do not affect its optimal flux distribution. [src: thermodynamic_impact]

### Carbon-source phenotype predictions

Marvin and OPAM2 gave identical, much lower accuracy than the unconstrained model. [src: thermodynamic_impact] Counts are CP, CN, FP, FN as given in the report.

| Condition | CP | CN | FP | FN | Accuracy |
|---|---|---|---|---|---|
| Unconstrained | 7 | 2 | 1 | 2 | 75.0% [src: thermodynamic_impact] |
| Marvin | 0 | 3 | 0 | 9 | 25.0% [src: thermodynamic_impact] |
| OPAM2 | 0 | 3 | 0 | 9 | 25.0% [src: thermodynamic_impact] |

## Open Directions

- Build a B. subtilis 168 library and test whether DUF484, DUF971 and EamA families show different phenotypes from Gram-negative organisms, which would close the Gram-positive gap.
- Test whether the covering-set analysis changes if native genomic context is weighted, which would show whether Bacillota deserve selection.
