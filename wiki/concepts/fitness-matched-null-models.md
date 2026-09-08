---
type: Concept
description: How fitness-matched nulls distinguish functional enrichment from shared
  fitness behavior
sources:
- id: amr_cofitness_networks
  resource: ../summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
- id: fitness_effects_conservation
  resource: ../summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: conservation_fitness_synthesis
  resource: ../summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
- id: module_conservation
  resource: ../summaries/module_conservation__REPORT.md
  title: module conservation
- id: fitness_modules
  resource: ../summaries/fitness_modules__REPORT.md
  title: fitness modules
title: Fitness-Matched Null Models for Functional Enrichment
---
# Fitness-Matched Null Models for Functional Enrichment

Functional enrichment in cofitness neighborhoods can arise from genuine shared regulation or from genes having similar fitness behavior under the assay conditions. A fitness-matched null model tests these explanations by comparing AMR-associated neighborhoods with random non-AMR genes whose mean-fitness distribution is matched, rather than matching only conservation class. [^amr_cofitness_networks]

This problem connects [condition-specific-fitness](condition-specific-fitness.md) with [cofitness-network-architecture](cofitness-network-architecture.md): cofitness measures similarity in fitness phenotypes, not direct transcriptional control, so enrichment requires a null model that reproduces the relevant fitness structure. [^amr_cofitness_networks] Evidence from a 43-bacterium comparison **supports** this concern: fitness importance was positively but weakly associated with core status, so conservation class does not fully capture fitness behavior. [^fitness_effects_conservation] The same evidence **refines** the proposed control: fitness breadth and condition-specific effects may also need consideration alongside mean fitness. [^fitness_effects_conservation] A broader synthesis further **supports** this limitation: essential genes were 82% core whereas always-neutral genes were 66% core, while core genes were 1.78x more likely to have strong condition-specific phenotypes. [^conservation_fitness_synthesis]

## Why conservation-matched nulls are insufficient

The AMR cofitness analysis used a permutation that matched conservation class but not mean fitness level. [^amr_cofitness_networks] The report identifies this mismatch as the key unresolved limitation because AMR genes, flagellar genes, and amino acid-biosynthesis genes may all be dispensable in shaken laboratory cultures or in media containing amino acid supplements. [^amr_cofitness_networks]

The observed enrichment included flagellum-dependent cell motility in 5 organisms with mean odds ratio (OR) 4.7, flagellum assembly in 5 organisms with mean OR 5.3, histidine biosynthesis in 3 organisms with mean OR 5.3, and tryptophan biosynthesis in 3 organisms with mean OR 5.3. [^amr_cofitness_networks] These signals therefore do not by themselves distinguish shared regulation from shared dispensability. [^amr_cofitness_networks]

Evidence consistent with a dispensability-driven signal includes the absence of energy-metabolism enrichment in 0/25 organisms, with a permutation-test fold of 0.91. [^amr_cofitness_networks] The report also notes that Pearson correlation removes each gene’s mean fitness before correlating profiles, but genes with similar condition-responsive dispensability can still have correlated fitness patterns without direct co-regulation. [^amr_cofitness_networks]

The broader fitness-conservation analysis **supports** treating conservation matching as incomplete: essential genes were 82% core whereas always-neutral genes were 66% core, but the association between fitness breadth and core status was weak (Spearman rho=0.086, p=8.1e-230). [^fitness_effects_conservation] It also found that strong condition-specific effects were enriched among core genes (77.3% core versus 70.3% without specific phenotypes), so conservation class cannot be treated as a proxy for either dispensability or condition dependence. [^fitness_effects_conservation] The synthesis **refines** this point by showing that core genes were also more likely to be burdensome in laboratory conditions: 24.4% had positive fitness when deleted versus 19.9% of accessory genes, and core genes were 1.29x more likely to be important in some conditions but burdensome in others. [^conservation_fitness_synthesis]

## Proposed null model

The primary proposed test is to draw random non-AMR genes while matching the AMR genes’ mean-fitness distribution, including the reported −0.05 to +0.05 range. [^amr_cofitness_networks] The resulting randomized neighborhoods should be analyzed with the same cofitness thresholds, module assignments, and enrichment procedure as the observed AMR neighborhoods so that differences reflect AMR association rather than changes in analysis scale. [^amr_cofitness_networks]

A useful implementation would preserve conservation class while additionally matching mean fitness, because the existing analysis already matched conservation class and the unresolved confound is the lack of mean-fitness matching. [^amr_cofitness_networks] Repeating the enrichment tests across many such permutations would provide a null distribution for odds ratios, enriched-term counts, and the number of organisms sharing each term. [^amr_cofitness_networks]

The broader synthesis reported 86% of fitness-module genes as core versus an 81.5% baseline, with OR=1.46 and p=1.6e-87. [^conservation_fitness_synthesis] The module-level analyses **support and refine** this design: independent component analysis (ICA), a decomposition method for coordinated fitness modules, identified 1,116 modules across 32 organisms, with 94.2% showing significantly elevated within-module cofitness and module genes showing 22.7x genomic-adjacency enrichment. [^fitness_modules] Module genes were 86.0% core versus 81.5% for all genes (OR=1.46, p=1.6e-87). [^module_conservation] Thus, conservation matching alone may leave structured module composition in the null, while module-level matching is constrained because essential genes are absent from these insertion-based modules. [^module_conservation] The new module evidence **refines** rather than replaces gene-level matching: ICA modules represent process-level co-regulation, not reliable gene-level molecular-function assignments; in held-out benchmarking, Module-ICA had <1% strict KEGG KO precision and 23.3% coverage, whereas ortholog transfer achieved 95.8% strict precision and 91.2% coverage. [^fitness_modules]

The new comparison also **supports** testing module structure as a sensitivity factor rather than treating it as a direct functional label: module sizes had a median range of 7-50 genes and within-module mean |r| was 0.34 versus 0.12 in the background, a 2.8x enrichment. [^fitness_modules] The core genes showed heavier tails in both negative and positive fitness effects, while singleton genes had near-zero mean fitness that may reflect poor transposon coverage rather than true neutrality. [^fitness_effects_conservation] Where data permit, the null should therefore assess fitness-effect breadth or coverage in addition to mean fitness, or explicitly test whether those features alter the enrichment result. [^fitness_effects_conservation]

The null should be evaluated at more than one cofitness threshold because the mean support network contained 233 genes at |r| > 0.3, 110 at |r| > 0.4, and 71 at |r| > 0.5. [^amr_cofitness_networks] The report specifically recommends confirmation at |r| > 0.4 because the |r| > 0.3 networks include many weak associations. [^amr_cofitness_networks]

## Interpreting possible outcomes

If flagellar motility and amino acid-biosynthesis enrichment remains stronger than the fitness-matched null, the result would support—but would not by itself prove—shared condition-dependent regulation or another structured biological association. [^amr_cofitness_networks] If the enrichment disappears after matching mean fitness, the evidence would favor shared dispensability under the laboratory conditions as the explanation for the original signal. [^amr_cofitness_networks]

The distinction matters because the original InterProScan analysis found 35/3,193 significant tests at FDR (false discovery rate) < 0.05, whereas the old SEED/KEGG analysis found 0/280 significant tests at FDR < 0.05. [^amr_cofitness_networks] Improved annotation can expose real functional structure, but it can also make it more important to use a null model that controls the fitness properties of the compared genes. The ICA benchmark **supports** retaining this caution: its module-level predictions were weak for exact KEGG assignments despite identifying coherent fitness modules, so enrichment surviving a module-aware null should still not be interpreted as proof of a specific molecular function. [^fitness_modules]

The fitness-matched test should not be used to reinterpret every result in the analysis: AMR-containing ICA modules had median size 46 genes versus 27 genes for non-AMR modules, with Mann–Whitney U (MWU) p = 1.7×10⁻⁸, and the report treats this module-size result as robust to the shared-dispensability concern. [^amr_cofitness_networks] Likewise, support-network size was not correlated with AMR fitness cost (Spearman rho = −0.006, p = 0.87, N = 769), although limited variation in fitness cost may reduce the ability to detect such a relationship. [^amr_cofitness_networks]

## Relation to organism-specific network structure

A fitness-matched null is mainly needed to interpret functional enrichment, not to erase the observed organism-specific organization of support networks. [^amr_cofitness_networks] Different AMR mechanisms within the same organism had mean Jaccard similarity 0.375, compared with 0.207 for the same mechanism across organisms, with MWU p = 4.3×10⁻¹³. [^amr_cofitness_networks] The report describes this relative comparison as robust to the dispensability confound because it tests how support networks are organized within and across organisms rather than relying only on the presence of individual enriched categories. [^amr_cofitness_networks]

The planned null model therefore complements [cofitness-network-architecture](cofitness-network-architecture.md): it asks whether particular functional categories are overrepresented beyond expected fitness similarity, while the network-organization comparison asks whether organism context structures support relationships more strongly than AMR mechanism. [^amr_cofitness_networks] The 156 cross-organism ICA module families, including one spanning 21 organisms, **support** testing whether such conserved process-level structure also contributes to enrichment, while the benchmark **refines** interpretation by showing that conservation of a module does not establish identical molecular functions for every member. [^fitness_modules]

## Evidence status

The need for a fitness-matched null is a methodological conclusion supported by a specific unresolved confound, not evidence that the observed enrichment is artifactual. [^amr_cofitness_networks] The current data support the hypothesis that flagellar, chemotaxis, and amino acid-biosynthesis enrichment may reflect shared dispensability, while leaving genuine co-regulation as an alternative explanation. [^amr_cofitness_networks] The fitness-conservation comparison **supports** the need to control assay-visible fitness structure, but its weak conservation association and coverage caveat mean that it does not establish that mean-fitness matching alone is sufficient. [^fitness_effects_conservation] The synthesis **supports** retaining this cautious interpretation: its costly-and-conserved category is evidence for, rather than a direct measurement of, natural-environment purifying selection. [^conservation_fitness_synthesis] The module-conservation result **supports** adding module composition to the sensitivity analysis, but its ICA modules exclude essential genes and therefore cannot establish how essential-gene structure would affect the null. [^module_conservation] The fitness-modules benchmark **refines** the evidence standard: module coherence and cross-organism conservation can support process-level structure, but exact gene-function claims require stronger sequence-based evidence. [^fitness_modules]

The source reports are summarized at [amr_cofitness_networks__REPORT](../summaries/amr_cofitness_networks__REPORT.md), [fitness_effects_conservation__REPORT](../summaries/fitness_effects_conservation__REPORT.md), [conservation_fitness_synthesis__REPORT](../summaries/conservation_fitness_synthesis__REPORT.md), [module_conservation__REPORT](../summaries/module_conservation__REPORT.md), and [fitness_modules__REPORT](../summaries/fitness_modules__REPORT.md).

## Open Directions

- Use the existing AMR and non-AMR fitness matrices, conservation classes, and mean-fitness values to run conservation- and fitness-matched permutations; test whether flagellar and amino acid-biosynthesis enrichment remains significant. [^amr_cofitness_networks]
- Recompute cofitness separately for antibiotic-exposure and standard-growth conditions, then apply the matched null; ask whether enrichment is specific to resistance-relevant conditions or persists under general laboratory growth. [^amr_cofitness_networks]
- Compare observed odds ratios and enriched-term counts with null distributions at |r| > 0.3, |r| > 0.4, and |r| > 0.5; ask whether the functional signal survives removal of weaker associations. [^amr_cofitness_networks]
- Measure mean fitness directly for flagellar knockouts and other conditionally dispensable gene classes, then use those distributions in the null; ask whether their observed neighborhoods are predictable from dispensability alone. [^amr_cofitness_networks]
- Extend the matched-null analysis to phage-defense and secondary-metabolite genes; ask whether enrichment of other conditionally dispensable classes is similarly explained by fitness structure. [^amr_cofitness_networks]
- Replace the operon-exclusion row-index heuristic with coordinate-based genomic filtering before permutation testing; ask whether local-gene structure changes the enrichment estimates. [^amr_cofitness_networks]
- Add fitness breadth, condition-specific-effect status, and transposon-callability measures to the matching or stratification scheme; ask whether the enrichment survives controls motivated by the weak conservation–fitness association and possible singleton coverage bias. [^fitness_effects_conservation]
- Test whether the 1,116 conservation-enriched fitness modules alter functional-enrichment null distributions when module composition, rather than only gene-level conservation and mean fitness, is matched. [^conservation_fitness_synthesis][^fitness_modules]
- Re-run the module-composition sensitivity analysis on the 29/32 organisms with pangenome links, and separately assess whether exclusion of essential genes changes enrichment conclusions. [^module_conservation]
- Compare enrichment against nulls that preserve ICA module membership but randomize within module, then test whether surviving terms remain process-level associations rather than exact KEGG KO predictions. [^fitness_modules]

[^amr_cofitness_networks]: [amr cofitness networks](../summaries/amr_cofitness_networks__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../summaries/fitness_effects_conservation__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../summaries/conservation_fitness_synthesis__REPORT.md)
[^fitness_modules]: [fitness modules](../summaries/fitness_modules__REPORT.md)
[^module_conservation]: [module conservation](../summaries/module_conservation__REPORT.md)
