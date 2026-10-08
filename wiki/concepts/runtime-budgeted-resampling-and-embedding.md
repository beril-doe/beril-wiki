---
type: "Concept"
description: "How resampling and dimension-reduction steps in corpus analyses are run under explicit compute budgets, trading exactness for feasibility, and why that trade should be declared."
sources: ["summaries/pitfalls.md"]
---
# Resampling and Embedding Analyses Are Budgeted, Not Exact

The central pitfalls digest treats compute budgets for some analysis steps as a deliberate method choice. These steps are not always run to exact or exhaustive completion. For bootstrap uncertainty estimation, the digest gives a recommended budget (bootstrap means repeated resampling with replacement to estimate confidence intervals). It does not show that the notebook models actually used that budget. For nonlinear embedding with [[entities/umap]] (Uniform Manifold Approximation and Projection, a dimension-reduction method), it reports one analysis where the run was approximated so it could finish on the available hardware [src: pitfalls].

## Bootstrap Budgets

For the notebook models, the digest recommends moderate bootstrap sizes (for example 250-400) with fixed seeds for reproducibility. It also recommends limiting confidence-interval estimation to key coefficients or endpoints. Its reason is that this keeps runtime practical while still giving uncertainty intervals for interpretation. This is guidance, not a record of what the models ran, and not a measured comparison of how stable the intervals are across bootstrap sizes [src: pitfalls].

## Embedding Budgets

The embedding budget comes from a null result. Running `umap.UMAP(metric='cosine')` on 83K genomes with 64 dimensions took >60 minutes and did not complete on a single-CPU JupyterHub pod. The digest blames the cosine metric, which needs pairwise precomputation that is O(n^2) [src: pitfalls].

The reported fix had two parts. First, the embeddings were L2-normalized and run with `metric='euclidean'`. For L2-normalized vectors, Euclidean distance is monotonically related to cosine distance (`||a-b||^2 = 2(1-cos(a,b))`), so the digest calls the UMAP topology equivalent. Second, UMAP was fit on a 20K subsample and then used to transform the full dataset. Together these cut runtime from >60 min to ~7 min in the reported analysis. The metric swap rests on an exact identity. The subsample fit, however, is an approximation, and the source does not measure its effect on the final layout. The runtime figure comes from a single reported run [src: pitfalls].

## Why the Trade Should Be Declared

These records suggest the hypothesis that bootstrap intervals and UMAP layouts made with these shortcuts include an approximation component. Intervals may cover only selected coefficients, and embeddings may depend on which subsample was used for fitting. The digest itself states the shortcuts openly. It supports the feasibility side of the trade (runtime) but does not measure the accuracy cost. It also does not establish whether individual source projects reported their settings. Analyses that use these shortcuts should therefore state the bootstrap size, seed, subsample size and metric [src: pitfalls].

## Open Directions

- Re-run a corpus bootstrap analysis twice with the same fixed seed: once at the recommended 250-400 resamples and once at a larger size. Compare interval endpoints for the key coefficients to measure whether the budget changes any interpretation [src: pitfalls].
- Fit UMAP on several independent 20K subsamples of the 83K-genome embedding set. Compare how well the transformed full set preserves neighborhoods across fits, to quantify the layout variance the subsample shortcut adds [src: pitfalls].
- Audit the source projects behind concept pages that rely on UMAP layouts or bootstrap intervals. Check whether those projects report subsample size, seed and metric; the digest does not settle this [src: pitfalls].
