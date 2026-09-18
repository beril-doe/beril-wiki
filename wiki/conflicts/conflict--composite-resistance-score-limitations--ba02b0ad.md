<!-- tension-hash: ba02b0ad0a27488e -->
# Are Metal Genes 87.4%, 84.8%, or 92.0/91.0/89.8% Core? Three Estimates That Do Not Line Up

Three projects in this corpus each report how much of the "metal gene" repertoire sits in the core genome — the fraction of genes present in essentially all sampled genomes rather than in the variable accessory portion — and they report different numbers: 87.4% for broad metal-important genes [src: metal_fitness_atlas], 84.8% pooled for metal-specific genes [src: metal_specificity], and a tiered 92.0%/91.0%/89.8% gradient in the cross-resistance analysis [src: metal_cross_resistance]. The directions are compatible; the quantities may not be. This matters because [[concepts/composite-resistance-score-limitations]] treats composite tolerance signals as a mixture of general stress response and metal-specific mechanism, and that two-tier reading is only as sharp as the comparability of the core fractions used to support it. Averaging the three figures would manufacture a precision none of the projects claims.

## Evidence Sides

**Broad metal-important genes: 87.4% core.** The atlas's genome-wide result gives an 87.4% core fraction for broad metal-important genes, and this result is directionally consistent with the existing two-tier interpretation. [src: metal_fitness_atlas]

**Metal-specific genes, pooled: 84.8% core.** A pooled core fraction of 84.8% is reported for metal-specific genes — a narrower gene set under a different specificity definition. The tension text states explicitly that this figure is not directly interchangeable with the atlas's 87.4%. [src: metal_specificity]

**Tiered cross-resistance gradient: 92.0%/91.0%/89.8%.** The cross-resistance analysis reports core fractions as three tiers, 92.0%/91.0%/89.8%, again over its own gene set and conservation definition, and likewise not directly interchangeable with either single-number estimate. [src: metal_cross_resistance]

## Possible Reconciliations

- **Hypothesis: the gap is definitional, not biological.** The three estimates may be numerically different readings of one underlying conservation pattern, produced by different locus sets, different conservation definitions, and different metal-specificity thresholds; under a common set they would converge. This is the explanation the tension text itself favours as the resolution path. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance]

- **Hypothesis: breadth of the gene set drives the difference.** A broad metal-important set may include more core cellular machinery than a specificity-filtered set, so 87.4% and 84.8% would differ systematically by how aggressively pleiotropic loci are excluded, rather than by any disagreement about conservation. [src: metal_fitness_atlas] [src: metal_specificity]

- **Hypothesis: single numbers hide a gradient.** If conservation varies continuously across specificity tiers, as the 92.0%/91.0%/89.8% tiers suggest, then any single pooled figure is a set-composition average and will move with the mix of tiers included. [src: metal_cross_resistance]

## Resolving Work

- Re-derive all three estimates over a single common locus set, and ask whether the spread between 87.4%, 84.8%, and the 92.0%/91.0%/89.8% tiers survives.
- Fix one conservation definition (a single core-membership rule) across the three projects' genome collections and recompute core fractions, asking how much of the spread is definitional.
- Apply one metal-specificity threshold to the fitness data underlying all three projects and re-tier the genes, asking whether the tier ordering is threshold-stable.
- Add a matched non-metal control gene set under the same locus set, conservation rule, and threshold, and ask how much of each core fraction is specific to metal biology versus generic to fitness-important genes.
- Report all four harmonised quantities side by side with their denominators rather than as a pooled summary, so downstream composite-score arguments cite a comparable figure.
