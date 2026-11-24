<!-- tension-hash: 168908dee9e8e7f1 -->
# Orthogroup Expansion Versus Absent Pathway Gain: Is Deep-Subsurface Biosynthetic Self-Sufficiency Supported?

Two projects examine deep-clay Bacillota_B genomes and read the evidence differently. One reads an expansion of orthogroups (OGs, groups of related genes across genomes) as consistent with biosynthetic self-sufficiency. The other finds no significant gain in GapMind pathway completeness (GapMind is a tool that predicts whether amino-acid biosynthesis pathways are complete in a genome) in the within-Bacillota_B comparison. It matters because self-sufficiency is proposed as a general deep-subsurface adaptation, and the answer determines whether streamlining or expansion narratives apply to cultivable lineages. See [[concepts/biosynthetic-self-sufficiency-as-a-deep-subsurface-adaptation]].

## Evidence Sides

**Side A: expansion is consistent with self-sufficiency**

- The orthogroup expansion in deep-clay Bacillota_B is read as consistent with self-sufficiency. [src: bacillota_b_subsurface_accessory]
- This is an interpretation of gene-content expansion. It is not a direct measure of pathway completeness.

**Side B: no pathway-completeness gain, and critiques of universal streamlining**

- GapMind pathway completeness in the within-Bacillota_B comparison shows no significant gain. This is a null result. [src: clay_confined_subsurface]
- The negative result agrees with critiques of universal subsurface streamlining or self-sufficiency. Props et al. 2019 is cited as documenting expansion and positive selection in oligotrophic engineered cooling water. Cortez et al. 2022 is cited as showing streamlining is acidophile-specific. [src: clay_confined_subsurface]
- Streamlining in Patescibacteria/CPR (candidate phyla radiation) is reported not to generalize to cultivable subsurface Firmicutes. [src: discoveries]
- It is read as a CPR-specific adaptation to episymbiotic life, with cultivable Firmicutes showing the opposite pattern. [src: discoveries]

## Possible Reconciliations

- **Hypothesis: expansion reflects accessory function, not biosynthesis.** Expanded orthogroups may fall in other categories, so they would not raise amino-acid pathway completeness. This would let both observations stand.
- **Hypothesis: metric limits hide a real signal.** The concept context notes a very small deep cohort and a ceiling in the metric. A null on GapMind completeness may then not exclude self-sufficiency. [src: clay_confined_subsurface]
- **Hypothesis: cultivation bias separates the cohorts.** Self-sufficiency may be real in uncultivated lineages but absent in cultivable ones. This is untested here.

## Resolving Work

- Data: the expanded orthogroups in deep-clay Bacillota_B. Method: annotate each by metabolic function and test overlap with biosynthetic pathways. Question: does the expansion include biosynthesis genes, or other functions?
- Data: GapMind scores for the deep-clay and soil-baseline Bacillota_B genomes. Method: use a metric without a ceiling, such as per-step confidence, with a permutation test. Question: does a gain appear once the ceiling is removed?
- Data: additional deep-subsurface genomes, including metagenome-assembled genomes (MAGs). Method: repeat the within-Bacillota_B comparison with a larger cohort. Question: does the null hold beyond the small cultured cohort?
- Data: Patescibacteria/CPR genomes alongside cultivable Firmicutes. Method: compare pathway completeness within a shared framework. Question: is streamlining specific to episymbiotic lineages?
