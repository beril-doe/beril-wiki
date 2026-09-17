<!-- tension-hash: 52cc7c498f332f18 -->
# Do Cofitness Modules Generalize Better Than Cofit Gene Pairs?

Two analyses of the same question — whether laboratory cofitness predicts that genes co-occur across genomes — disagree about the unit at which the signal is real. Measured pair by pair, the co-occurrence effect is weak and does not survive an across-organism test; measured at the level of ICA modules (independent component analysis, a decomposition that groups genes with correlated fitness profiles into co-regulated units), the effect is several times larger, and largest of all for accessory modules. Whether modules are the stronger unit of shared dispensability, or whether the module-level effect is an artifact of small, unrepresentative subsets, determines how much of this corpus's module architecture can be read as genome-wide biology.

## Evidence Sides

**Modules are the stronger unit.** Pairwise cofit pairs had a mean delta phi (phi is the binary co-occurrence correlation coefficient; delta phi is the cofit-minus-random difference) of +0.011 across organisms, but an aggregate delta of only +0.003 and a Wilcoxon signed-rank test (a paired non-parametric test, here across organisms) p=0.13 — a null result at the across-organism level. ICA modules, by contrast, showed delta phi=+0.053 overall and accessory modules +0.108. [src: cofitness_coinheritance] On this reading the module is the coherent unit and pairwise measurement dilutes it.

**The module advantage does not generalize.** The same project reports that Korea had no significant modules because all its modules were >90% core with prevalence near 1.0, and that the accessory-versus-core difference was only near significant (p=0.051) — a trend, not a crossed threshold. [src: cofitness_coinheritance] Independently, only 5% of mapped modules were accessory, so accessory-module advantages cannot be generalized. [src: module_conservation]

## Possible Reconciliations

- *Hypothesis: aggregation, not biology.* Pooling co-occurrence over the many gene pairs inside a module suppresses pair-level noise, so the module delta could be the same weak pairwise signal measured with less error, not a larger one.
- *Hypothesis: prevalence range restriction.* Both the pairwise null result and Korea's absent modules may reflect near-saturated prevalence, where phi cannot move; the accessory-module effect would then be the only regime with measurable variance rather than a privileged one.
- *Hypothesis: selection on the accessory subset.* Because accessory modules are a small minority of mapped modules, the +0.108 figure may describe a self-selected set of unusually mobile gene blocks rather than accessory modules in general.

## Resolving Work

- Recompute the pairwise delta phi restricted to gene pairs that both fall inside the same ICA module, against the same prevalence-matched null: is the module advantage present at the pair level once module membership is conditioned on?
- Stratify both pairwise and module analyses by cluster prevalence bins and re-test: does the across-organism Wilcoxon null result persist within bins where phi has room to vary?
- Expand the accessory-module set beyond 5% of mapped modules by adding organisms with deeper pangenomes, then re-run the accessory-versus-core comparison: does p=0.051 move with n, or is the difference genuinely absent?
- Permute module membership within organisms while holding module size fixed: how much of delta phi=+0.053 is attributable to aggregation over gene sets of that size rather than to fitness coherence?
- Re-analyze Korea with a prevalence-relaxed module definition to test whether its lack of significant modules is a measurement ceiling or a real organism-level exception.

Tension recorded from [[concepts/cofitness-network-architecture]].
