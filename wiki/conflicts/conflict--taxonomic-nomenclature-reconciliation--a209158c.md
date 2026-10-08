<!-- tension-hash: a209158cffc68459 -->
# Does GTDB suffix removal reconcile species names or merge distinct clades?

This page records a disagreement over how BacDive species names should be matched to GTDB (Genome Taxonomy Database) species. It belongs to [[concepts/taxonomic-nomenclature-reconciliation]]. One project strips GTDB suffixes so that more BacDive strains link to GTDB species [src: bacdive_metal_validation]. Another project warns that GTDB-specific names denote clades distinct from the similarly named NCBI (National Center for Biotechnology Information) taxon [src: cf_formulation_design]. The disagreement matters because suffix stripping may merge GTDB-separated clades, so any trait linked through a suffix-stripped match, such as metal tolerance, may be attributed to the wrong clade [src: bacdive_metal_validation]. A join that succeeds syntactically could then spread error into downstream analyses without any visible failure.

## Evidence Sides

**Side A: suffix removal increases matches**

GTDB suffix removal increases matches by treating BacDive "Pseudomonas fluorescens" and GTDB "Pseudomonas fluorescens A" as the same species [src: bacdive_metal_validation]. The suffix-fallback step accounts for 8,692 matches [src: bacdive_metal_validation].

**Side B: GTDB-specific names mark distinct clades**

The cf_formulation_design report warns that GTDB-specific names such as *Pseudomonas_E* denote clades distinct from the similarly named NCBI taxon [src: cf_formulation_design].

**Unmeasured overlap**

Suffix stripping may therefore merge GTDB-separated clades. How many of the 8,692 suffix-fallback matches do so has not been measured [src: bacdive_metal_validation]. This is an open question, not a finding that merging occurs at any particular rate.

## Possible Reconciliations

- **Hypothesis 1: the answer depends on the suffix type.** Species-level letter suffixes, such as "fluorescens A", and genus-level suffixes, such as *Pseudomonas_E*, may differ in how often they split organisms that BacDive labels identically. Both sides could then hold for different subsets of names.
- **Hypothesis 2: the answer depends on which suffixed clade is involved.** When a BacDive name maps to only one suffixed GTDB clade, stripping may be harmless. When the base name is split across several suffixed clades, stripping may merge them.
- **Hypothesis 3: the answer depends on the analysis.** Suffix-level merging may be acceptable for coarse summaries but not for clade-specific trait inference. Under this hypothesis, the disagreement is about which use is fit for purpose rather than about which matching rule is correct.

## Resolving Work

- **Count ambiguous base names.** Using GTDB species lists, count how many suffix-fallback base names map to more than one suffixed GTDB species. This tests whether stripping is ambiguous for the 8,692 fallback matches [src: bacdive_metal_validation].
- **Check strain-level placement.** For BacDive strains that have genome accessions, place each genome in GTDB and compare its assigned clade with the clade chosen by suffix stripping. This tests whether stripping assigns strains to the correct GTDB-separated clade.
- **Stratify by suffix type.** Split the fallback matches into letter-suffixed species and underscore-suffixed genera such as *Pseudomonas_E*, then compare their mismatch rates. This tests Hypothesis 1.
- **Measure sensitivity of downstream results.** Rerun the metal-tolerance linkage with exact matches only and compare the results with and without suffix-fallback strains. This tests whether any merged clades change the conclusions.
