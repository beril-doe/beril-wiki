---
type: "Concept"
description: "Null models that match fitness to test functional enrichment fairly"
sources: ["summaries/amr_cofitness_networks__REPORT.md"]
---
# Fitness-Matched Null Models for Functional Enrichment

Functional enrichment in cofitness neighborhoods can arise from genuine shared regulation or from genes having similar fitness behavior under the assay conditions. A fitness-matched null model tests these explanations by comparing AMR-associated neighborhoods with random non-AMR genes whose mean-fitness distribution is matched, rather than matching only conservation class. [src: amr_cofitness_networks]

This problem connects [[concepts/condition-specific-fitness]] with [[concepts/cofitness-versus-coregulation]]: cofitness measures similarity in fitness phenotypes, not direct transcriptional control, so enrichment requires a null model that reproduces the relevant fitness structure. [src: amr_cofitness_networks]

## Why conservation-matched nulls are insufficient

The AMR cofitness analysis used a permutation that matched conservation class but not mean fitness level. [src: amr_cofitness_networks] The report identifies this mismatch as the key unresolved limitation because AMR genes, flagellar genes, and amino acid-biosynthesis genes may all be dispensable in shaken laboratory cultures or in media containing amino acid supplements. [src: amr_cofitness_networks]

The observed enrichment included flagellum-dependent cell motility in 5 organisms with mean odds ratio (OR) 4.7, flagellum assembly in 5 organisms with mean OR 5.3, histidine biosynthesis in 3 organisms with mean OR 5.3, and tryptophan biosynthesis in 3 organisms with mean OR 5.3. [src: amr_cofitness_networks] These signals therefore do not by themselves distinguish shared regulation from shared dispensability. [src: amr_cofitness_networks]

Evidence consistent with a dispensability-driven signal includes the absence of energy-metabolism enrichment in 0/25 organisms, with a permutation-test fold of 0.91. [src: amr_cofitness_networks] The report also notes that Pearson correlation removes each gene’s mean fitness before correlating profiles, but genes with similar condition-responsive dispensability can still have correlated fitness patterns without direct co-regulation. [src: amr_cofitness_networks]

## Proposed null model

The primary proposed test is to draw random non-AMR genes while matching the AMR genes’ mean-fitness distribution, including the reported −0.05 to +0.05 range. [src: amr_cofitness_networks] The resulting randomized neighborhoods should be analyzed with the same cofitness thresholds, module assignments, and enrichment procedure as the observed AMR neighborhoods so that differences reflect AMR association rather than changes in analysis scale. [src: amr_cofitness_networks]

A useful implementation would preserve conservation class while additionally matching mean fitness, because the existing analysis already matched conservation class and the unresolved confound is the lack of mean-fitness matching. [src: amr_cofitness_networks] Repeating the enrichment tests across many such permutations would provide a null distribution for odds ratios, enriched-term counts, and the number of organisms sharing each term. [src: amr_cofitness_networks]

The null should be evaluated at more than one cofitness threshold because the mean support network contained 233 genes at |r| > 0.3, 110 at |r| > 0.4, and 71 at |r| > 0.5. [src: amr_cofitness_networks] The report specifically recommends confirmation at |r| > 0.4 because the |r| > 0.3 networks include many weak associations. [src: amr_cofitness_networks]

## Interpreting possible outcomes

If flagellar motility and amino acid-biosynthesis enrichment remains stronger than the fitness-matched null, the result would support—but would not by itself prove—shared condition-dependent regulation or another structured biological association. [src: amr_cofitness_networks] If the enrichment disappears after matching mean fitness, the evidence would favor shared dispensability under the laboratory conditions as the explanation for the original signal. [src: amr_cofitness_networks]

The distinction matters because the original InterProScan analysis found 35/3,193 significant tests at FDR (false discovery rate) < 0.05, whereas the old SEED/KEGG analysis found 0/280 significant tests at FDR < 0.05. [src: amr_cofitness_networks] Improved annotation can expose real functional structure, but it can also make it more important to use a null model that controls the fitness properties of the compared genes. [src: amr_cofitness_networks]

The fitness-matched test should not be used to reinterpret every result in the analysis: AMR-containing ICA modules had median size 46 genes versus 27 genes for non-AMR modules, with Mann–Whitney U (MWU) p = 1.7×10⁻⁸, and the report treats this module-size result as robust to the shared-dispensability concern. [src: amr_cofitness_networks] Likewise, support-network size was not correlated with AMR fitness cost (Spearman rho = −0.006, p = 0.87, N = 769), although limited variation in fitness cost may reduce the ability to detect such a relationship. [src: amr_cofitness_networks]

## Relation to organism-specific network structure

A fitness-matched null is mainly needed to interpret functional enrichment, not to erase the observed organism-specific organization of support networks. [src: amr_cofitness_networks] Different AMR mechanisms within the same organism had mean Jaccard similarity 0.375, compared with 0.207 for the same mechanism across organisms, with MWU p = 4.3×10⁻¹³. [src: amr_cofitness_networks] The report describes this relative comparison as robust to the dispensability confound because it tests how support networks are organized within and across organisms rather than relying only on the presence of individual enriched categories. [src: amr_cofitness_networks]

The planned null model therefore complements [[concepts/cofitness-network-architecture]] and [[concepts/cofitness-versus-coregulation]]: it asks whether particular functional categories are overrepresented beyond expected fitness similarity, while the network-organization comparison asks whether organism context structures support relationships more strongly than AMR mechanism. [src: amr_cofitness_networks]

## Evidence status

The need for a fitness-matched null is a methodological conclusion supported by a specific unresolved confound, not evidence that the observed enrichment is artifactual. [src: amr_cofitness_networks] The current data support the hypothesis that flagellar, chemotaxis, and amino acid-biosynthesis enrichment may reflect shared dispensability, while leaving genuine co-regulation as an alternative explanation. [src: amr_cofitness_networks]

The source report is summarized at [[summaries/amr_cofitness_networks__REPORT]]. [src: amr_cofitness_networks]

## Open Directions

- Use the existing AMR and non-AMR fitness matrices, conservation classes, and mean-fitness values to run conservation- and fitness-matched permutations; test whether flagellar and amino acid-biosynthesis enrichment remains significant. [src: amr_cofitness_networks]
- Recompute cofitness separately for antibiotic-exposure and standard-growth conditions, then apply the matched null; ask whether enrichment is specific to resistance-relevant conditions or persists under general laboratory growth. [src: amr_cofitness_networks]
- Compare observed odds ratios and enriched-term counts with null distributions at |r| > 0.3, |r| > 0.4, and |r| > 0.5; ask whether the functional signal survives removal of weaker associations. [src: amr_cofitness_networks]
- Measure mean fitness directly for flagellar knockouts and other conditionally dispensable gene classes, then use those distributions in the null; ask whether their observed neighborhoods are predictable from dispensability alone. [src: amr_cofitness_networks]
- Extend the matched-null analysis to phage-defense and secondary-metabolite genes; ask whether enrichment of other conditionally dispensable classes is similarly explained by fitness structure. [src: amr_cofitness_networks]
- Replace the operon-exclusion row-index heuristic with coordinate-based genomic filtering before permutation testing; ask whether local-gene structure changes the enrichment estimates. [src: amr_cofitness_networks]
