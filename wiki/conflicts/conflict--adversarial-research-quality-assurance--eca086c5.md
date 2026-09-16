<!-- tension-hash: eca086c5366a0bb3 -->
# Conflict: Is the susceptibility matrix 188 strains × 96 phages = 17,672 pairs, or does a 94-phage denominator apply?

Two projects in this corpus describe the same *E. coli* phage-susceptibility screen, and the matrix dimensions they state do not reconcile with the pair count they state. The defense-system project states 188 strains × 96 phages = 17,672 binary infection outcomes, and that stated multiplication is internally inconsistent [src: snipe_defense_system]; the same inventory appears in the phage-targeting project, where a 94-phage denominator — the phage count serving as the base for a percentage — is used elsewhere [src: ibd_phage_targeting, snipe_defense_system]. This is a provenance and arithmetic-audit problem of exactly the kind [[concepts/adversarial-research-quality-assurance]] exists to catch. No product is computed on this page; the figures are retained as each report states them.

## Evidence Sides

**The stated 96-phage matrix.** The defense-system project reports 188 *E. coli* strains (ECOR collection, NILS collection, clinical/environmental isolates) × 96 phages (41 Podoviridae, 32 Myoviridae, 23 Siphoviridae) = 17,672 binary infection outcomes — each outcome scoring one strain–phage pair as infected or not — and that stated multiplication is internally inconsistent; the figures are retained as stated and no product is computed here. [src: snipe_defense_system]

**The 94-phage denominator.** The same 96-phage × 188-strain × 17,672-pair inventory appears in the phage-targeting project, where a 94-phage denominator is used elsewhere, so the inconsistency is shared across reports rather than local to one. [src: ibd_phage_targeting, snipe_defense_system]

## Possible Reconciliations

- *Hypothesis: a curation drop.* Two phages may have been excluded after the matrix was assembled (e.g. failed quality control or duplicate isolates), leaving an inventory header at 96 and working denominators at 94, with the pair count inherited from whichever stage was authoritative.
- *Hypothesis: incomplete screening.* Not every strain may have been tested against every phage, so the pair count could be an observed-pair tally rather than a full grid, making the written "=" a transcription convenience rather than a computed product.
- *Hypothesis: shared upstream copy.* Both reports may have inherited the header from one common dataset description, in which case the mismatch is a single upstream error replicated twice, not independent corroboration.

## Resolving Work

- Retrieve the raw susceptibility table and count distinct phage identifiers, distinct strain identifiers, and non-null cells directly: which of the stated counts is the data's own?
- Cross-tabulate phage identifiers against the 41/32/23 family assignments to test whether the family sums or the headline phage total is the discrepant figure. [src: snipe_defense_system]
- Diff the phage identifier lists backing the 96- and 94-phage usages to name the specific phages present in one and absent from the other. [src: ibd_phage_targeting, snipe_defense_system]
- Trace both reports' inventory text to its upstream source record to determine whether the mismatch is one inherited error or two independent ones.
- Recompute every published rate under each candidate denominator to establish which conclusions, if any, are denominator-sensitive.
