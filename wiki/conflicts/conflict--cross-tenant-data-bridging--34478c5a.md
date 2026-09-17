<!-- tension-hash: 34478c5a941127d4 -->
# When a Near-Perfect Correlation Meets a Zero-Transfer Score: Is the IBD Bridging Result Under-Validated or Structurally Unidentifiable?

Two readings of the same IBD bridging evidence sit side by side in [[concepts/cross-tenant-data-bridging]]. One treats the strong association as a real signal that has simply not yet been taken to clinical validation; the other holds that the pooled design cannot estimate a diagnosis effect at all, so no amount of further validation would rescue it. The distinction matters because it determines whether cross-tenant IBD bridges are a maturity problem (more cohorts, more assays) or a design problem (the contrast is not identified and must be rebuilt).

## Evidence Sides

**Strong association, explicitly self-limited to hypothesis generation [src: ibd_phage_targeting]**
The IBD canonical correlation analysis (CCA — a method that finds the linear combinations of two variable blocks with maximal correlation) returned r=0.964, and PhageFoundry coverage was reported alongside it; the project labels both as hypothesis-generating rather than clinical validation. The same project supplies its own limits: HMP2/FRANZOSA clustering had cross-cohort LOSO (leave-one-study-out) ARI (adjusted Rand index, a cluster-agreement statistic scored against chance) = 0.000, and the cocktail covered only tested strains. On this reading the shortfall is one of scope and validation stage. [src: ibd_phage_targeting]

**The pooled contrast is not identifiable to begin with [src: pitfalls]**
In the ecotype analyses, pooled diagnosis was structurally unidentifiable: 45 sub-studies had at least 10 HC (healthy control) samples, 5 had at least 10 CD (Crohn's disease) samples, and 0 had at least 10 of both. With no sub-study populating both arms at that threshold, diagnosis is confounded with study identity. Selection-on-outcome leakage — choosing candidates using the outcome they are then tested against — reduced independent Tier-A candidates from 33 to 3. On this reading the defect is in the design, not the validation stage. [src: pitfalls]

## Possible Reconciliations

- **Hypothesis: different estimands.** r=0.964 and ARI=0.000 may measure distinct quantities — within-analysis association versus cross-cohort cluster transfer — so both can hold simultaneously, and the dispute is over which statistic should carry the claim. [src: ibd_phage_targeting]
- **Hypothesis: composition drives both numbers.** The 45 / 5 / 0 sub-study imbalance may mean any pooled axis recovered by CCA tracks study identity rather than diagnosis, which would also explain zero cross-cohort transfer. [src: pitfalls, ibd_phage_targeting]
- **Hypothesis: leakage is a matter of degree.** The 33 → 3 reduction may indicate that a small transferable core survives outcome-blind selection, making the two positions endpoints of one severity scale rather than opposed verdicts. [src: pitfalls]

## Resolving Work

- Ingest a cohort that populates both arms at the stated threshold, then recompute cross-cohort LOSO ARI: does cluster agreement rise above 0.000 when diagnosis is no longer confounded with study? [src: ibd_phage_targeting, pitfalls]
- Re-fit CCA within individual sub-studies holding study identity constant: is r=0.964 preserved, or does it collapse toward the pooled-design artifact? [src: ibd_phage_targeting]
- Audit every sub-study for simultaneous ≥10 CD and ≥10 HC counts — currently 0 — to establish whether the identifiability precondition can be met at all in existing data. [src: pitfalls]
- Re-derive Tier-A candidates under outcome-blind selection and test whether the 3 independent survivors replicate out-of-cohort. [src: pitfalls]
- Assay the cocktail against strains outside the tested set: does coverage extend beyond tested strains, or is it definitionally bounded by them? [src: ibd_phage_targeting]
