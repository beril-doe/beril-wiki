<!-- tension-hash: eca086c5366a0bb3 -->
# Conflict: Is the *E. coli* × phage susceptibility matrix 96 phages wide, 94 phages wide, or 17,672 pairs deep?

Two projects describe the same experimental phage-susceptibility matrix — a 96-phage × 188-strain × 17,672-pair inventory of binary infection outcomes (one susceptible/resistant call per strain–phage pair) [src: ibd_phage_targeting, snipe_defense_system]. In the defense-system project the stated multiplication is internally inconsistent [src: snipe_defense_system], while the phage-targeting project uses a 94-phage denominator (the count placed under the division bar when a proportion of phages is reported) elsewhere [src: ibd_phage_targeting, snipe_defense_system]. Because the inconsistency is shared across reports rather than local to one, it cannot be read as a single report's slip, and the inventory line cannot be taken as read wherever either report reuses it [src: ibd_phage_targeting, snipe_defense_system]. The tension is recorded under [[concepts/adversarial-research-quality-assurance]]; no product is computed here, and the reported figures are retained exactly as stated.

## Evidence Sides

**The 96-phage inventory as stated (defense-system project).** The defense-system project reports 188 *E. coli* strains (ECOR collection, NILS collection, clinical/environmental isolates) × 96 phages (41 Podoviridae, 32 Myoviridae, 23 Siphoviridae) = 17,672 binary infection outcomes, and that stated multiplication is internally inconsistent; the figures are retained as stated and no product is computed here. [src: snipe_defense_system]

**The shared inventory with a 94-phage denominator (phage-targeting project).** The same 96-phage × 188-strain × 17,672-pair inventory appears in the phage-targeting project, where a 94-phage denominator is used elsewhere, so the inconsistency is shared across reports rather than local to one. [src: ibd_phage_targeting, snipe_defense_system]

## Possible Reconciliations

- **Hypothesis: 17,672 counts assayed pairs, not the full crossing.** If some strain–phage combinations were never tested or failed quality control, the pair count would be a tested-pairs tally and the "=" a reporting shorthand rather than arithmetic.
- **Hypothesis: a filtering step separates 96 from 94.** The two phage denominators may refer to different stages — phages deposited versus phages surviving a downstream filter — in which case each is correct for its own scope.
- **Hypothesis: a single transcription error propagated by reuse.** If one report's inventory line was copied into the other, the two reports are not independent confirmations of the same count, and the agreement between them carries no evidential weight.
- **Hypothesis: the strain count, not the phage count, is the discrepant term.** The inconsistency could sit on the 188 side rather than on the phage width of the matrix.

## Resolving Work

- Query the underlying susceptibility table directly in the KBase Data Lakehouse and count distinct phage identifiers, distinct strain identifiers, and non-null pair rows separately. Question: which of the three reported quantities, if any, does the stored data reproduce?
- Group the stored pair rows by phage and by strain and inspect the per-phage and per-strain row counts for ragged margins — that is, uneven row or column coverage where some phages or strains carry fewer calls than others. Question: is the matrix complete, or are missing cells the source of the pair count?
- Trace provenance of both report lines back to the upstream susceptibility experiment release and compare release dates and record counts. Question: did the phage inventory change between the versions the two projects read?
- Recompute every proportion each report derives from this matrix under each candidate denominator and record the range rather than a point estimate. Question: which downstream claims are denominator-sensitive and which survive all candidates?
- Check whether the per-family phage counts form a partition of the stated phage total in the stored taxonomy. Question: is the family breakdown consistent with either denominator?
