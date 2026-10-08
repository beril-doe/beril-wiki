<!-- tension-hash: 268ee5009f8c7655 -->
# AMR Fitness Cost: Uniform and Structure-Independent, or Mechanism-Dependent?

Projects in this corpus disagree on whether the fitness consequences of antimicrobial-resistance (AMR) genes are uniform or shaped by resistance mechanism. One line finds that AMR fitness cost is not explained by cofitness neighborhood size, where cofitness means correlated fitness profiles across experiments [src: amr_cofitness_networks]. It also finds the cost independent of mechanism, conservation and annotation tier [src: discoveries]. The other line finds that efflux genes show a stronger antibiotic-dependent fitness flip than enzymatic inactivation genes [src: discoveries]. The answer decides whether AMR genes can be treated as one class with a common burden, or whether mechanism must be modelled explicitly in [[concepts/cofitness-network-architecture]] analyses.

## Evidence Sides

**Side A: cost is uniform and not explained by neighborhood size or mechanism**

- Support-network size does not explain AMR fitness cost. A Spearman rank correlation (rho, a test of monotonic association) gives rho = −0.006, p = 0.87, N = 769. Here p is the p-value, the chance of an association at least this strong if none existed, and N is the sample size. [src: amr_cofitness_networks]
- The null holds within mechanisms: rho = −0.049 for efflux, +0.038 for enzymatic resistance and −0.031 for metal resistance, all p > 0.4. [src: amr_cofitness_networks]
- The uniform resistance cost was +0.086 and was not explained by neighborhood size. [src: amr_cofitness_networks]
- Across 801 AMR genes and 25 organisms, the pooled knockout fitness shift (the fitness change when the gene is disrupted) was +0.086 [+0.074, +0.098]. [src: discoveries]
- The cost was mechanism-independent by a Kruskal-Wallis (KW) rank test across groups (KW p=0.89). [src: discoveries]
- The cost was also conservation-independent (p=0.33) and tier-independent (p=0.26). [src: discoveries]

**Side B: mechanism predicts antibiotic-dependent fitness behaviour**

- Efflux genes showed a stronger antibiotic-dependent flip than enzymatic inactivation genes: +0.094 versus -0.001. A Mann-Whitney U (MWU) two-group rank test gives p=0.007. [src: discoveries]

The denominators differ. N = 769 is given for the overall network-size correlation [src: amr_cofitness_networks], while the pooled shift uses 801 AMR genes across 25 organisms [src: discoveries]. Denominators for the within-mechanism correlations are not given. This page records the counts as given and does not reconcile them.

## Possible Reconciliations

- **Hypothesis 1: the two sides measure different quantities.** The uniform figure may be a baseline cost of carrying the gene when no antibiotic is present. The efflux-versus-enzymatic contrast is an antibiotic-dependent flip. Mechanism could be irrelevant to the first and relevant to the second.
- **Hypothesis 2: the null may reflect low variance.** If the fitness cost varies little between genes, rank correlations with network size, and KW tests across mechanisms, may have little room to detect structure. A detectable flip contrast would not, on its own, rule this out.
- **Hypothesis 3: mechanism classes differ in breadth of action.** The efflux and enzymatic-inactivation classes may differ in how widely they act. That difference could show up only under antibiotic exposure and not in network neighborhood size.

## Resolving Work

- **Variance check.** Use per-gene AMR knockout fitness from the Fitness Browser matrices. Run variance decomposition and power analysis to ask whether the cost spread is wide enough for the network-size and KW tests to detect a mechanism effect if one existed.
- **Condition-stratified retest.** Use antibiotic and no-antibiotic experiment subsets. Repeat the network-size correlation and the mechanism tests separately in each to ask whether mechanism-independence holds only for baseline cost.
- **Denominator alignment.** Use the gene sets behind N = 769 and the 801-gene meta-analysis. Identify the excluded genes and rerun both analyses on a shared set to ask whether the different denominators change either conclusion.
- **Dispensability control.** Use fitness-matched permutations of non-AMR genes. Compare flip magnitudes to ask whether the efflux contrast exceeds what comparably costly genes show.
