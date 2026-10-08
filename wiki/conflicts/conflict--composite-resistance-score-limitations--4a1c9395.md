<!-- tension-hash: 4a1c939511a5523d -->
# Diverging BacDive-to-GTDB Bridge Totals Across Two Metal-Tolerance Analyses

Two projects link BacDive strains to genome-based metal-tolerance scores at the species level, and they report different totals for that link. Species are defined by GTDB (the Genome Taxonomy Database). The phenotype analysis reports 37,368 matched strains across 5,647 GTDB species [src: bacdive_phenotype_metal_tolerance]. The isolation-environment analysis reports 42,227 matched strains across 6,426 GTDB species [src: bacdive_metal_validation]. The difference matters because both analyses feed arguments on [[concepts/composite-resistance-score-limitations]]. Until the gap is explained, their coverage estimates cannot be treated as interchangeable. Results from one cannot be assumed to describe the same strain or species population as the other.

## Evidence Sides

**Phenotype analysis (smaller bridge)**
The project that tests BacDive phenotypes as predictors of metal tolerance reports a bridge of 37,368 matched strains spanning 5,647 GTDB species [src: bacdive_phenotype_metal_tolerance].

**Isolation-environment analysis (larger bridge)**
The project that compares metal-tolerance scores across BacDive isolation environments reports a bridge of 42,227 matched strains spanning 6,426 GTDB species [src: bacdive_metal_validation].

Both sides describe the same kind of object: a species-level bridge of BacDive strains matched to GTDB species [src: bacdive_phenotype_metal_tolerance] [src: bacdive_metal_validation]. The gap is attributed only tentatively: it "may reflect different matching or filtering pipelines" [src: bacdive_phenotype_metal_tolerance] [src: bacdive_metal_validation].

## Possible Reconciliations

- **Hypothesis: different name-matching rules.** One pipeline may accept matches the other rejects. For example, one may add a fallback that strips GTDB species suffixes while the other requires exact name agreement. That would inflate one bridge relative to the other without either being in error.
- **Hypothesis: different downstream filters.** One count may be taken after an extra requirement, such as the presence of a valid metal score or of the analysis-specific metadata. Under this explanation the smaller total would be a filtered subset of a common bridge, not a competing estimate.
- **Hypothesis: different input snapshots.** The projects may have drawn on different versions of BacDive or of the GTDB-linked score tables. The totals would then differ because the inputs differ, not because the methods do.

The supplied evidence does not resolve any of these. Each remains a candidate explanation, not a resolution.

## Resolving Work

- **Strain-level join of the two bridges.** Join each project's matched-strain file on BacDive strain identifier. This asks whether the smaller set is a strict subset of the larger one, or whether each contains strains the other lacks.
- **Match-rule audit.** Re-run both matching procedures on a single shared BacDive export. Tabulate the matches each rule accepts, to test whether suffix-removal fallback or exact-only matching accounts for the extra strains and species.
- **Filter-stage waterfall.** For each project, record strain and species counts after every filtering step. This identifies the step at which the totals diverge.
- **Sensitivity of downstream results.** Restrict each analysis to the intersection of the two bridges and re-run it. This tests whether the phenotype associations and the environment comparisons change when both rest on an identical strain set.
