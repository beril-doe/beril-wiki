---
type: "Concept"
description: "Whether genomically complete pathways are actually important for growth in genome-wide fitness data, including how classification thresholds and pathway category change the latent fraction; stops at evolutionary interpretation."
sources: ["summaries/discoveries.md", "summaries/essential_metabolome__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Latent metabolic capability versus fitness dependency

This page covers whether genomically complete pathways are actually important for growth in genome-wide fitness data. Two Fitness Browser (FB) analyses of GapMind pathways find a substantial latent fraction. Genomic completeness alone is an imperfect proxy for functional importance. [src: metabolic_capability_dependency, pathway_capability_dependency]

The size of the latent fraction depends on the classification rules and on pathway category. The 7-organism analysis gives 41.0% latent. [src: discoveries] The 48-organism threshold analysis gives 15.8%. [src: metabolic_capability_dependency] Related background is on [[concepts/metabolic-capability-versus-fitness-dependency]], [[entities/gapmind]] and [[entities/fitness-browser]]. This page stops at the evolutionary interpretation.

## Two classifications, two latent fractions

Both analyses conclude that a complete pathway does not mean the organism depends on it. [src: pathway_capability_dependency]

### Four-category scheme (7 organisms, 23 pathways)

Active Dependency is a complete and important pathway that the organism needs and uses. [src: pathway_capability_dependency] Latent Capability is complete but not important, so encoded but dispensable under tested conditions. [src: pathway_capability_dependency] Incomplete but Important means fitness data detect dependence that GapMind misses, likely because of annotation gaps or salvage routes. [src: pathway_capability_dependency] Missing means neither complete nor important. [src: pathway_capability_dependency]

Of 161 classified organism-pathway pairs, 57 (35.4%) were Active Dependencies. [src: pathway_capability_dependency, discoveries] Latent Capabilities numbered 66 (41.0%), the largest category. [src: pathway_capability_dependency, discoveries] Incomplete but Important numbered 24 (14.9%) [src: pathway_capability_dependency, discoveries], and Missing numbered 14 (8.7%). [src: pathway_capability_dependency, discoveries] The report reads the 41% rate as suggesting that nearly half of complete pathways are conditionally dispensable, but not permanently so. [src: pathway_capability_dependency]

### Threshold scheme (48 organisms)

The wider analysis classed 1,695 pathway-organism pairs. Active meant mean absolute t-score above 2.0 OR more than 20% essential genes. [src: metabolic_capability_dependency] Latent meant mean absolute t-score below 1.0 AND less than 5% essential genes. [src: metabolic_capability_dependency] Intermediate meant between the thresholds. [src: metabolic_capability_dependency] The result was 881 active (51.9%), 547 intermediate (32.3%) and 267 latent (15.8%). [src: metabolic_capability_dependency] The latent fraction per organism ranged 0–31.6%, with mean 15.0%. It was highest in Pseudomonas syringae strains and [[entities/klebsiella-michiganensis]]. [src: metabolic_capability_dependency]

The two latent fractions come from different organism sets and importance definitions, so each stands on its own. [src: discoveries, metabolic_capability_dependency, pathway_capability_dependency]

## Pathway category changes the latent fraction

Pathway category strongly predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴). [src: metabolic_capability_dependency]

| Category | Active | Intermediate | Latent | Total pairs |
|---|---|---|---|---|
| Amino acid biosynthesis | 467 (63.5%) | 220 (29.9%) | 48 (6.5%) | 735 [src: metabolic_capability_dependency] |
| Carbon source utilization | 355 (39.8%) | 320 (35.9%) | 217 (24.3%) | 892 [src: metabolic_capability_dependency] |
| Other | 59 (86.8%) | 7 (10.3%) | 2 (2.9%) | 68 [src: metabolic_capability_dependency] |

Carbon pathways were 3.7× more likely to be latent than amino acid pathways (24.3% vs 6.5%). [src: metabolic_capability_dependency] The report reads amino acid pathways as largely essential, because organisms cannot scavenge all amino acids in all tested conditions. [src: metabolic_capability_dependency] It cautions that condition-dependent carbon pathways, such as deoxyribose or ethanol utilization, may look latent in the laboratory despite ecological importance. [src: metabolic_capability_dependency]

## Sensitivity to thresholds

Varying the active threshold ±25% (1.5–2.5) and the latent threshold ±25% (0.75–1.25) gave latent fractions of 4.7% to 21.1% (SD = 5.9 percentage points across 16 combinations). [src: metabolic_capability_dependency] The report attributes this moderate sensitivity to the large intermediate zone (32.3%). [src: metabolic_capability_dependency] The qualitative conclusion held across the range: a non-trivial fraction of complete pathways are fitness-neutral, with carbon pathways most affected. [src: metabolic_capability_dependency]

## Latent in rich media, important under specific conditions

In the 7-organism analysis, all 66 Latent Capability pairs became fitness-important under at least one condition type. [src: pathway_capability_dependency, discoveries] The stratification separated fitness effects into nitrogen source, carbon source, stress and other conditions. [src: pathway_capability_dependency] Nitrogen limitation and stress were the most frequent triggers. [src: pathway_capability_dependency] One statement of the result adds carbon limitation. [src: pathway_capability_dependency] The report therefore reads "latent" as "conditionally active" rather than "genomic baggage". [src: pathway_capability_dependency] The discoveries digest says this validates the core_gene_tradeoffs finding that laboratory fitness underestimates natural selection on metabolic genes. [src: discoveries]

## Tensions

- The 100% reclassification is partly a threshold effect. The median-based importance threshold splits pathways about 50/50 by construction. [src: pathway_capability_dependency] With enough condition subsets, some pathways will inevitably cross the threshold. [src: pathway_capability_dependency] This limits the reading in [src: discoveries, pathway_capability_dependency] that latent pathways are all truly condition-dependent.
- Calibrating against an independent validation set, such as known essentials from essential_metabolome, would give a more defensible threshold. [src: pathway_capability_dependency]
- Laboratory RB-TnSeq (random barcode transposon sequencing) cannot capture the full range of natural selective pressures. Condition stratification only partly addresses this. [src: pathway_capability_dependency]
- Whether complete pathways are actually essential for viability is left open. [src: essential_metabolome]

## Open Directions

- Calibrate the importance threshold against known essentials from [[summaries/essential_metabolome__REPORT]]. This would replace the median rule that forces a 50/50 split.
- Rerun the condition-type reclassification with a fixed, non-median threshold and a permutation control. This would test whether 100% reclassification exceeds chance.
- Apply the 48-organism threshold scheme to the 7-organism set, and the reverse. This would show how much of 41.0% versus 15.8% is definition rather than data.
- Check whether Incomplete but Important pairs are annotation gaps or salvage routes by targeted gene curation. See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].
