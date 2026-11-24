<!-- tension-hash: ad08f7a444bf9168 -->
# Metal Tolerance Determinants: Specific Mechanisms or Shared Stress and Lineage Confounding?

Projects in the corpus disagree about what metal-fitness and metal-tolerance signals mean. One reading holds that metal-important genes are mostly general stress genes, and that phenotype associations such as urease status come from lineage (shared ancestry) confounding. Another reading holds that metal-specific genes are real metal tolerance determinants. This matters because it decides whether metal fitness data can identify resistance mechanisms or only general stress biology. The concept page is [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]]. NaCl means sodium chloride, used as a control stress. Fitness means growth effect of losing a gene.

## Evidence Sides

**Side A: shared stress and confounding explain much of the signal**

- Urease should confer nickel tolerance because it needs nickel import machinery. [src: bacdive_phenotype_metal_tolerance] The pooled data instead show lower tolerance in urease-positive species. [src: bacdive_phenotype_metal_tolerance] The report resolves this as lineage confounding, with the effect absent within Gammaproteobacteria, Bacilli and other classes. [src: bacdive_phenotype_metal_tolerance]
- Metal-important genes are mostly general stress genes. [src: metal_fitness_atlas]

**Side B: metal-specific determinants are genuine**

- Core enrichment survives NaCl correction for 12 of 14 metals. [src: discoveries] Core means genes shared across a species' genomes.
- The specificity report says metal-specific genes are genuine metal tolerance determinants, enriched for resistance keywords. [src: metal_specificity]

**Internal inconsistency in the specificity report**

- The report's text says general sick genes have higher general-stress keyword enrichment (11.5% vs 13.7%). [src: metal_specificity]
- Its table gives 13.7% for metal-specific genes and 11.5% for general sick genes, the opposite direction. [src: metal_specificity]

The Atlas and specificity claims are stated as the reports give them. This page does not average them or prefer either.

## Possible Reconciliations

- **Hypothesis: two layers.** Metal fitness may combine a large shared-stress component with a smaller metal-specific subset. The NaCl-corrected result (12 of 14 metals) would then reflect the subset. This is untested here.
- **Hypothesis: lineage-level versus gene-level scope.** The urease result concerns species-level phenotypes, while the Atlas and specificity claims concern genes within organisms. They may not conflict directly.
- **Hypothesis: the keyword direction is a transcription error.** The text and table of the specificity report may differ because of a wording slip. The table would then be authoritative, but this needs checking.

## Resolving Work

- Recheck the specificity report's keyword counts, using its source tables, to ask which direction of the 11.5% versus 13.7% comparison is correct.
- Rerun the urease–nickel tolerance comparison within each taxonomic class, using a phylogenetically aware model, to ask whether any within-lineage effect exists.
- Classify metal-important genes using NaCl-corrected fitness data, then ask what fraction are specific and which metals fall outside the 12 of 14 result.
- Compare keyword-based specificity labels with an independent annotation, such as curated metal-resistance gene sets, to ask whether the keyword enrichment is circular.
