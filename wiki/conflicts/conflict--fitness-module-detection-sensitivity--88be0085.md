<!-- tension-hash: 88be0085639ed538 -->
# Does Module z-Scoring Reveal or Suppress Metal-Responsive Fitness Modules?

Two analyses of metal responses in fitness modules disagree about what z-scoring does. A z-score expresses a value as standard deviations from a reference mean, and |z| is its absolute magnitude. A fitness module is a group of genes with coordinated fitness patterns across experiments. One analysis reports that z-scored profiles identified many metal-responsive module records. The other reports that per-module z-normalization produced sub-threshold |z| for most metal experiments and found no metal-specific modules. [src: metal_fitness_atlas, metal_specificity] The corpus also describes the Atlas procedure in two different ways. This matters because, as [[concepts/fitness-module-detection-sensitivity]] argues, module discovery depends on thresholds and normalization choices. The opposing module-level results may therefore reflect procedure as well as biology. The discrepancy is documented but not explained. [src: pitfalls, metal_fitness_atlas]

## Evidence Sides

**Side A: z-scored profiles identify metal-responsive modules**

The Metal Fitness Atlas reports that z-scored profiles identified 600 responsive records. [src: metal_fitness_atlas, metal_specificity] The Atlas report itself credits per-experiment profiles with z-normalization for this result. [src: pitfalls, metal_fitness_atlas]

**Side B: per-module z-normalization yields no metal-specific modules**

The metal-specificity analysis reports that per-module z-normalization (standardizing each module's activity across that organism's experiments) produced max |z| < 2.0 for most metal experiments. It found 0 metal-specific modules. [src: metal_fitness_atlas, metal_specificity]

**Side C: the pitfalls digest's account of the Atlas procedure**

The pitfalls digest describes the Atlas z-scores as standardized per module across all experiments. It attributes the difference between the two analyses to precomputed versus recomputed z-scores. [src: pitfalls, metal_fitness_atlas] This description of the Atlas normalization does not match the Atlas report's own attribution to per-experiment profiles. The corpus therefore gives two accounts of how the positive result was produced. [src: pitfalls, metal_fitness_atlas]

## Possible Reconciliations

- *Hypothesis:* The two analyses normalized along different axes, per experiment in one and per module in the other. Under this hypothesis, the same underlying activity scores could produce responsive records in one analysis and sub-threshold |z| in the other.
- *Hypothesis:* The pitfalls digest attributes the difference to precomputed versus recomputed z-scores. [src: pitfalls, metal_fitness_atlas] One proposed explanation is that the two sets differ in scale or reference set, which would make the disagreement a pipeline artifact rather than a biological difference.
- *Hypothesis:* "Responsive records" (Side A) and "metal-specific modules" (Side B) are different targets. A module can respond to metals without being specific to them, so the two counts may not be directly comparable.

The corpus documents the procedural discrepancy but does not explain it. [src: pitfalls, metal_fitness_atlas] The tension is recorded, not resolved.

## Resolving Work

- **Data:** the Atlas precomputed module z-scores and the metal-specificity recomputed z-scores for the same organisms. **Method:** a record-by-record comparison of the two sets. **Question:** do the two sets of values agree, and where do they diverge?
- **Data:** the Atlas notebook code and the module activity tables. **Method:** reconstruct the exact normalization axis, per experiment or per module. **Question:** which description, the Atlas report's or the pitfalls digest's, matches what was actually run?
- **Data:** the module activity profiles. **Method:** rerun the metal-specificity test under both normalizations at the same |z| cutoff. **Question:** does the count of metal-specific modules change with the normalization alone?
- **Data:** the Atlas responsive records. **Method:** apply the metal-specificity criterion to those records. **Question:** how many responsive records also qualify as metal-specific, which would separate "responsive" from "specific"?
