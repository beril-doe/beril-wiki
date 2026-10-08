<!-- tension-hash: 40968e6d1aaf9b90 -->
# Does the BacDive Evidence Validate Genome-Based Metal-Tolerance Prediction Over Phenotype-Based Screening?

The disagreement is about how far the BacDive analyses can be taken. The cross-project discoveries digest frames the BacDive result as validating genome-based prediction from the Metal Fitness Atlas over phenotype-based screening, but the direct evidence is weaker than that framing. [src: discoveries, bacdive_phenotype_metal_tolerance, bacdive_metal_validation] The corpus supports lineage confounding of the composite score, without establishing that phenotype-based screening fails against measured metal tolerance. In lineage confounding, an apparent association reflects which lineages are sampled rather than a relationship that holds within lineages. [src: bacdive_phenotype_metal_tolerance, bacdive_metal_validation] This matters for [[concepts/phenotype-database-coverage-bias]]. If the stronger framing is accepted, a comparative claim about screening strategies would rest on predictions rather than measurements.

## Evidence Sides

**Side 1: The digest framing (genome-based prediction validated over phenotype-based screening)**

The discoveries digest frames the BacDive result as validating genome-based prediction, represented by the Metal Fitness Atlas, over phenotype-based screening. [src: discoveries, bacdive_phenotype_metal_tolerance, bacdive_metal_validation] As stated, this is a comparative claim: one approach is said to outperform the other.

**Side 2: The direct evidence (lineage confounding, no demonstrated failure of phenotype screening)**

The direct evidence is weaker than the digest framing, for three reasons. [src: discoveries, bacdive_phenotype_metal_tolerance, bacdive_metal_validation]

- The Metal Fitness Atlas scores are themselves genome-based predictions, not measured tolerance. [src: discoveries, bacdive_phenotype_metal_tolerance, bacdive_metal_validation]
- The direct Fitness Browser–BacDive set lacked balanced phenotype contrasts. [src: discoveries, bacdive_phenotype_metal_tolerance, bacdive_metal_validation]
- The only BacDive metal-utilization comparison was underpowered. A Mann-Whitney test (a rank-based, non-parametric two-group comparison) gave p=0.14, with 8 positive and 16 negative results. Here p is the p-value: the probability of a difference at least this large if no true difference existed. The result is non-significant and inconclusive. [src: discoveries, bacdive_phenotype_metal_tolerance, bacdive_metal_validation]

On this reading, the corpus supports lineage confounding of the composite score. In lineage confounding, an apparent association reflects which lineages are sampled rather than a relationship that holds within lineages. The corpus does not establish that phenotype-based screening fails against measured metal tolerance. [src: bacdive_phenotype_metal_tolerance, bacdive_metal_validation]

## Possible Reconciliations

- *Hypothesis:* The digest may be summarizing a lineage-level pattern that genome-based scores capture, and treating that pattern as a head-to-head validation. If so, both sides describe the same data at different strengths of inference.
- *Hypothesis:* Genome-based prediction may truly outperform phenotype-based screening, but the current corpus lacks a measured-tolerance benchmark that could show it. If so, the digest claim is premature rather than wrong.
- *Hypothesis:* Phenotype-based screening may perform comparably once lineage composition is controlled. If so, the digest's superiority claim would not hold, though no reverse superiority would follow.

## Resolving Work

- **Measured benchmark:** Identify an explicitly validated, measured strain metal-tolerance endpoint. Score both the genome-based Metal Fitness Atlas predictions and BacDive phenotype features against it. Question: does either approach predict measured tolerance better?
- **Balanced phenotype contrasts:** Assemble a Fitness Browser–BacDive strain set with balanced positive and negative phenotype classes. Question: does phenotype-based screening separate tolerant from sensitive strains once class imbalance is removed?
- **Power for metal utilization:** Expand the BacDive metal-utilization records through additional strain matching, then repeat the Mann-Whitney comparison with an a priori power calculation. Question: is the non-significant result a true absence of signal or a sample-size artifact?
- **Within-lineage tests:** Apply class-stratified or phylogenetically controlled models to both predictor types. Question: does any advantage of genome-based prediction survive control for lineage composition?
