<!-- tension-hash: 3694383936e0c35d -->
# Gene-Count Repertoire Versus Phenotype as Predictor of Metal Tolerance: Conflicting Readings

Two projects disagree about whether the metal resistance genes a genome encodes (its "repertoire") predict how tolerant a bacterium is to metals. The BacDive analysis (BacDive is a database of standardized bacterial phenotype data) favours the gene-count repertoire as a predictor of tolerance scores. The Metal Fitness Atlas reports that its repertoire prediction failed validation. Even inside the BacDive report, a statement about gene content sits uneasily beside its own variance figures, where R² is the share of variance a model explains. This matters because it decides whether genome annotations alone can be used to infer metal tolerance. The source concept is [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]].

## Evidence Sides

**Side A: the gene-count repertoire predicts tolerance (BacDive)**

- The BacDive result favours the gene-count repertoire as the true predictor of tolerance scores. [src: bacdive_phenotype_metal_tolerance, discoveries]
- The report states that gene content explains more variance than all phenotype features. [src: bacdive_phenotype_metal_tolerance]
- Caveat from the concept context: the tolerance scores are themselves genome-derived, so this does not show that gene count predicts directly measured tolerance. [src: bacdive_phenotype_metal_tolerance]
- Within the same report, the gene-count-only R² is 0.063, against a phenotype-only R² of 0.163. [src: bacdive_phenotype_metal_tolerance] That ordering runs against the statement above.

**Side B: presence/absence does not predict tolerance (Metal Fitness Atlas)**

- The report says its repertoire prediction failed validation. It states that simple gene presence/absence does not predict metal tolerance and that a regulatory or expression-based model is needed. [src: metal_fitness_atlas]
- It links the failure to Rosconi et al. (2022): gene essentiality is context-dependent and cannot be predicted from gene presence alone. [src: metal_fitness_atlas]

## Possible Reconciliations

- **Hypothesis 1: circular targets.** BacDive scores are derived from genomes, so gene count may predict them partly by construction, while the Metal Fitness Atlas tested a different, fitness-based target. Under this hypothesis, neither result contradicts the other.
- **Hypothesis 2: statement versus table.** The "gene content explains more variance" wording may refer to gene content together with taxonomy, not gene count alone. The gene-count-only R² of 0.063 would then be consistent with the Atlas's failure.
- **Hypothesis 3: context dependence.** Gene presence may carry signal only when regulation and expression context are modelled, as the Atlas suggests.

## Resolving Work

- Data: BacDive tolerance scores plus directly measured metal tolerance for the same strains. Method: refit the gene-count model against measured values. Question: does gene count still predict tolerance when the target is not genome-derived?
- Data: the BacDive model tables. Method: refit each feature set under phylogenetically blocked cross-validation (holding out whole clades). Question: which wording of the gene-content claim matches the reported R² values?
- Data: Metal Fitness Atlas fitness data. Method: add regulatory or expression features to the repertoire model and validate on held-out organisms. Question: does this rescue the prediction that presence/absence alone failed?
- Data: genomes shared by both projects. Method: compare the repertoire scores each project computes. Question: do the two definitions of repertoire differ enough to explain the disagreement?
