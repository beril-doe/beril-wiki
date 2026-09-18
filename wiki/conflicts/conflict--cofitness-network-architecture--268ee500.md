<!-- tension-hash: 268ee5009f8c7655 -->
# Uniform AMR Knockout Cost Versus Mechanism-Structured Response

Two analyses of antimicrobial-resistance (AMR) genes read the same uniformity differently. One reports that the cost of carrying an AMR gene — the fitness shift when the gene is knocked out — is flat across every axis tested, including the size of a gene's cofitness support network, and that the uniform cost of +0.086 is not explained by neighborhood size [src: amr_cofitness_networks]. The other reports the same pooled shift of +0.086 and the same null results for mechanism, conservation and annotation tier, but finds that mechanism does separate genes once antibiotic exposure is taken into account [src: discoveries]. The disagreement is whether mechanism is an explanatory axis for AMR cost at all, and it matters because "irreducible, uniform cost" and "mechanism-conditional cost" imply different models of how resistance genes are retained. This tension comes from [[concepts/cofitness-network-architecture]].

## Evidence Sides

**Cost is uniform and unexplained by co-regulatory neighborhood or mechanism.** There is no correlation between cofitness support network size and AMR gene fitness cost: Spearman rho (a rank-based correlation coefficient) = −0.006, p = 0.87, N = 769. The null holds within each mechanism stratum — rho = −0.049 for efflux, +0.038 for enzymatic resistance, and −0.031 for metal resistance, all p > 0.4 — so it is a null result at every stratum, not a weak trend in one. Uniform resistance cost was +0.086 and was not explained by neighborhood size. [src: amr_cofitness_networks]

**Cost is uniform in level, but mechanism separates the antibiotic-dependent response.** Across 801 AMR genes and 25 organisms, pooled knockout fitness shift was +0.086 [+0.074, +0.098]; cost was mechanism-independent by Kruskal–Wallis (a nonparametric test of equal distributions across three or more groups), KW p=0.89, conservation-independent (p=0.33), and tier-independent (p=0.26). Yet efflux genes showed a stronger antibiotic-dependent flip than enzymatic inactivation genes, +0.094 versus −0.001, by Mann–Whitney U (a two-group rank test), MWU p=0.007. [src: discoveries]

## Possible Reconciliations

- *Hypothesis:* the two sides estimate different quantities — a pooled level averaged over conditions versus a contrast between antibiotic-present and antibiotic-absent conditions — so a flat level and a mechanism-dependent contrast can both hold without either being wrong.
- *Hypothesis:* the network-size test is underpowered by restricted variance in cost across genes, so a real structural effect could be masked while the mechanism contrast, computed on a different comparison, survives.
- *Hypothesis:* the gene sets differ (N = 769 genes with network sizes versus 801 AMR genes across 25 organisms), and the mechanism-dependent flip is carried by genes absent from the network-size denominator.

## Resolving Work

- Recompute the network-size correlation on the same gene set used for the antibiotic-dependent flip, stratified by antibiotic presence: does the −0.006 null persist when cost is measured as a condition contrast rather than a pooled level?
- Run a null-distribution permutation of network size against fitness cost at more than one correlation cutoff: is the null stable to the threshold used to define a support network?
- Fit the efflux-versus-enzymatic flip with organism as a random effect across the 25 organisms: is MWU p=0.007 driven by a subset of organisms or shared across them?
- Estimate the detectable effect size for the N = 769 test given the observed spread in cost: could a mechanism-sized effect have been detected at all?
