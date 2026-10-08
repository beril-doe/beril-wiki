<!-- tension-hash: eb662e5692a5b406 -->
# 54 % of what? Competing denominators for the Kuehl–training feature overlap

Two documents in this corpus report the overlap between the Kuehl sample set and a training feature space — the fixed list of species a model was fitted on — and they frame the same comparison on different denominators. One states that 54 % of Kuehl feature rows fell outside the training feature space; the other states that Kuehl detects only 54 % of training species and that 70 % of training species have no Kuehl detection [src: ibd_phage_targeting, discoveries]. The disagreement matters because an overlap quoted per-feature-row and an overlap quoted per-training-species answer different questions: a reader who treats them as the same number will mis-state how much of either set the other covers. The discrepancy is recorded rather than resolved; this page comes from [[concepts/classifier-database-compatibility-in-taxonomic-quantification]].

## Evidence Sides

**The project report: 54 % of Kuehl feature rows fall outside the training feature space.** Here the denominator is Kuehl feature rows — observations in the Kuehl table — and the direction is exclusion: a majority-adjacent share of what Kuehl measured has no counterpart among the features the model knows [src: ibd_phage_targeting, discoveries].

**The discoveries digest: Kuehl detects 54 % of training species, and 70 % of training species have no Kuehl detection.** Here the denominator is training species — the model's own feature list — and the digest reports both a detection share and a non-detection share. The tension record notes that these two percentages are not obviously compatible with each other, so the digest side is internally unsettled as stated, not merely different from the report side [src: ibd_phage_targeting, discoveries].

## Possible Reconciliations

- **Hypothesis: the two 54 % figures are coincidental and measure different objects** — rows absent from the training space versus species present in Kuehl — in which case neither corrects the other and both must be quoted with their denominators.
- **Hypothesis: the digest's two percentages are computed over different training-species subsets** (for example, all training species versus those retained after a prevalence or abundance filter), which would explain their apparent incompatibility without either being wrong.
- **Hypothesis: one figure is a transcription of the other with the denominator lost**, i.e. a single underlying overlap statistic restated against the wrong population during digest writing.

## Resolving Work

- Recompute overlap directly from the Kuehl feature table and the stored training feature list on the KBase Data Lakehouse, reporting four numbers separately: rows in/out of the training space, and training species detected/undetected.
- Publish the exact filter chain (prevalence, abundance, rank) applied before each percentage, and re-derive the digest's two figures under each chain to test the differing-subset hypothesis.
- Recover the provenance of the digest sentence — which notebook cell emitted each percentage — to test the transcription hypothesis.
- Re-express overlap as a rank-matched comparison (species-level only, same taxonomy version) and ask whether any denominator choice still leaves the two documents disagreeing.
