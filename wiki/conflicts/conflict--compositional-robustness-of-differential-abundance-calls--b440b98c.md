<!-- tension-hash: b440b98caa706d9d -->
# Within-ecotype differential abundance: an unusable 3-taxon survivor set, or a design-controlled 51 and 40?

Differential abundance (DA) — testing which taxa differ in abundance between sample groups — was run within ecotype strata (E1 and E3, community-type clusters), and two analyses of those strata leave incompatible target lists. The cross-project digest reports 33 within-ecotype candidates that collapse to 3 under a stricter agreement filter and declares the list not usable [src: discoveries]; a revised meta-analysis — combining evidence across strata and sub-studies rather than testing one pooled set — reports 51 E1 candidates and 40 provisional E3 candidates [src: ibd_phage_targeting]. The disagreement matters because the two versions differ not only in size but in verdict: one declares the within-ecotype list not usable [src: discoveries], the other reports replacement candidate counts [src: ibd_phage_targeting]. The tension is carried by [[concepts/compositional-robustness-of-differential-abundance-calls]].

## Evidence Sides

**Side A — the digest: within-ecotype calls do not survive agreement filtering.** Within-ecotype DA yielded 33 candidates across both E1 and E3, and a stricter filter requiring both within-substudy agreement and agreement with LinDA — a linear-model DA method for compositional (sum-constrained) count data — left 3, in E3 only; on that basis the within-ecotype list was declared not usable [src: discoveries]. The operative claim here is a usability verdict under a stated threshold, not a count offered for comparison: 3 is what remains after the filter, and the conclusion drawn is negative.

**Side B — the revised meta-analysis: the design-controlled count supersedes it.** A within-ecotype × within-substudy meta-analysis — stratifying by ecotype and by sub-study jointly before combining — instead reports 51 E1 candidates across two eligible sub-studies and 40 provisional E3 candidates from one [src: ibd_phage_targeting]. This side does not average with Side A: the later, design-controlled count replaces the earlier one, with E3 explicitly provisional pending a second eligible sub-study [src: ibd_phage_targeting]. That same provisionality is flagged as bearing on whether the ecotype partition itself is stable [src: ibd_phage_targeting].

## Possible Reconciliations

- *Hypothesis (nesting order):* the digest applied within-substudy agreement as a post-hoc filter on a pooled within-ecotype test, while the revision made sub-study a design level before testing; if so, 3 [src: discoveries] and 51/40 [src: ibd_phage_targeting] count different quantities rather than conflicting estimates of one.
- *Hypothesis (eligibility gate):* the two eligible E1 sub-studies and the single eligible E3 sub-study [src: ibd_phage_targeting] may be a subset of what the digest pooled, so the eligibility screen could remove heterogeneity that the LinDA-agreement filter was absorbing.
- *Hypothesis (E3 asymmetry):* the digest's 3 survivors were E3 only [src: discoveries] while the 40 E3 candidates remain provisional on one sub-study [src: ibd_phage_targeting], suggesting E3 is the stratum most sensitive to how sub-study structure is handled — possibly because the E3 partition is itself unstable.

## Resolving Work

- Re-run both pipelines on an identical sample set, varying only whether sub-study enters as a pre-test design level or a post-hoc agreement filter: does ordering alone reproduce 3 versus 51/40?
- Cross-tabulate the 3 surviving candidates against the 51 E1 and 40 E3 lists: is the survivor set contained in the larger lists, or disjoint from them?
- Add a second eligible E3 sub-study and repeat the within-ecotype × within-substudy meta-analysis: do the 40 provisional E3 candidates replicate when E3 is no longer single-sub-study?
- Hold the design fixed and swap only the test (LinDA versus the meta-analysis statistic) on the same strata: is the gap method-driven or design-driven?
- Re-derive ecotype labels under perturbed clustering and recount candidates per stratum: how much of the 51/40 depends on the E1/E3 partition itself?
