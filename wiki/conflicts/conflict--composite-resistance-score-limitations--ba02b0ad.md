<!-- tension-hash: ba02b0ad0a27488e -->
# Is the core-genome enrichment of metal-fitness genes one estimate or several incomparable ones?

Three projects report core-genome fractions for metal-fitness genes. The core genome is the set of genes shared by nearly all genomes in a species' pangenome, which is the full gene repertoire across those genomes. Read side by side, the projects appear to give competing values for one quantity, but they use different gene sets and definitions. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance] This matters for [[concepts/composite-resistance-score-limitations]]. If the estimates are treated as interchangeable, a gap between them could be misread as evidence for or against the two-tier interpretation, in which general-stress genes are more core than metal-specific resistance genes. The open question is whether the agreement in direction can become a quantitative comparison.

## Evidence Sides

**Side A: genome-wide metal-important genes (broad set)**
The atlas reports a genome-wide core-enrichment result in which broad metal-important genes have an 87.4% core fraction. [src: metal_fitness_atlas] This result is directionally consistent with the existing two-tier interpretation. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance]

**Side B: metal-specific genes (pooled)**
The specificity analysis reports an 84.8% pooled core fraction for metal-specific genes. [src: metal_specificity] "Pooled" means one fraction computed over all genes from all organisms combined, rather than a mean of per-organism fractions. This gene set and its definitions differ from Side A's. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance]

**Side C: cross-resistance tiers**
The cross-resistance analysis reports tiered core fractions of 92.0%/91.0%/89.8%. [src: metal_cross_resistance] These tiers also rest on gene sets and definitions that differ from those of Sides A and B. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance]

**Why the sides cannot be directly compared**
The 87.4% value is not directly interchangeable with the 84.8% pooled value or with the 92.0%/91.0%/89.8% tiers, because the sources use different gene sets and definitions. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance] This tension should not be resolved by averaging the estimates.

## Possible Reconciliations

- **Hypothesis 1 (definitional):** The differences reflect only which genes enter each denominator and how "core" is defined. Under a shared definition, the three sources might show the same ordering with no real conflict.
- **Hypothesis 2 (aggregation):** Pooled and per-organism summaries weight organisms differently. Some of the apparent spread may therefore come from the aggregation method rather than from biology.
- **Hypothesis 3 (substantive gradient):** After harmonization, a real gradient may remain, with broader-acting genes more core than metal-specific ones. That would support the two-tier interpretation quantitatively rather than only in direction.

## Resolving Work

- **Common locus set:** Using the fitness data from all three projects, re-derive core fractions for one shared set of loci. This tests whether the values converge once the denominators match.
- **Common conservation definition:** Apply one pangenome core threshold to all three gene partitions. This tests whether differences in the definition of "core" drive the spread.
- **Common metal-specificity threshold:** Re-classify genes as broad, shared or metal-specific with one threshold applied across projects. This tests whether Side B's and Side C's specific categories describe the same genes.
- **Common non-metal control set:** Compare every category against the same non-metal baseline. This tests whether the enrichment over baseline, rather than the raw core fraction, agrees across sources.
- **Pooled versus per-organism reporting:** Report both summaries for each harmonized category. This tests Hypothesis 2 directly.
