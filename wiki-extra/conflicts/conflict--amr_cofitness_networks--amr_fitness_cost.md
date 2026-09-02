<!-- tension-hash: 2c74743ca1f6619f -->
# AMR Fitness Effects: Broad Signals, Specific Validation, and Mechanistic Interpretation

The [[concepts/antimicrobial-resistance-fitness-cost]] evidence contains several tensions about how broadly AMR fitness effects generalize and what biological processes explain them. A strong signal appears when genes are evaluated against any antibiotic, but the class-matched validation is weaker; mechanism is unrelated to baseline cost yet strongly associated with conservation; and AMR-associated cofitness enrichment may reflect either mechanistic interactions or shared dispensability. These tensions matter because they determine whether the observed patterns support a general causal model of AMR burden and benefit, or instead reflect study design, genomic distribution, or laboratory-condition effects.

## Evidence Sides

### **Broad any-antibiotic signal versus weaker class-matched validation**

The any-antibiotic analysis found a **57.0%** flip rate for **N = 797** genes with **p = 0.0001**, whereas the class-matched analysis found a **54.8%** flip rate for **157** pairs with **p = 0.14**. [src: amr_fitness_cost] The stronger result therefore comes from broad condition coverage, while the class-matched result provides weaker statistical support under antibiotic-specific matching. [src: amr_fitness_cost]

### **No mechanism effect on baseline cost versus strong conservation association**

Mechanism was not associated with baseline cost (**H = 0.65, p = 0.89**) but was strongly associated with conservation status (**χ² = 69.3, p = 1.4×10⁻¹³**). [src: amr_fitness_cost] The evidence supports different roles for mechanism in fitness and pangenome distribution rather than a single mechanism-to-cost-to-retention pathway. [src: amr_fitness_cost]

### **Mechanistic cofitness enrichment versus shared dispensability**

Flagellar motility, chemotaxis, and amino acid biosynthesis were enriched in AMR support neighborhoods, but the cofitness analysis identifies shared dispensability under laboratory conditions as an alternative explanation and reports no network-size relationship with cost. [src: amr_cofitness_networks] This limits the inference that cofitness-network structure explains the measured AMR fitness burden, even though it does not contradict the measured AMR fitness burden or antibiotic-dependent benefit. [src: amr_cofitness_networks]

## Possible Reconciliations

- **Hypothesis — sample size and design:** The **57.0%** and **54.8%** estimates may be compatible if class matching reduces the effective sample size or excludes informative gene–antibiotic combinations; the difference in **p** values may therefore reflect power and design rather than opposing effects.
- **Hypothesis — distinct biological roles:** Mechanism may influence whether genes are retained or lost across genomes without determining their baseline laboratory fitness cost, producing conservation differences independently of measured cost.
- **Hypothesis — condition-dependent cofitness:** AMR support neighborhoods may be enriched because genes are jointly dispensable under laboratory conditions, while their relationships become mechanistic only under particular antibiotics or environmental stresses.

## Resolving Work

- Reanalyze the any-antibiotic and class-matched datasets with identical genes, antibiotic classes, and coverage; test whether the flip-rate difference persists after matching sample size and design.
- Fit hierarchical models with gene, antibiotic, and class effects; ask whether antibiotic-class specificity explains the stronger result better than broader condition coverage.
- Test mechanism, baseline cost, and conservation jointly using regression or stratified analyses; ask whether conservation remains associated with mechanism after controlling for cost and genomic covariates.
- Measure cofitness and fitness across antibiotic exposures and relevant environmental conditions; ask whether neighborhood enrichment predicts interaction-specific effects beyond shared dispensability.
- Test the relationship between network size and cost with uncertainty estimates and preregistered controls; ask whether the reported absence of a relationship is robust to network definition.
