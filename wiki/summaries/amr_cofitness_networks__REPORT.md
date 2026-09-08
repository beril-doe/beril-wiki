---
type: Summary
description: Pan-bacterial AMR cofitness networks reveal organism-specific structure
  and annotation-dependent enrichment.
doc_type: short
full_text: ../sources/amr_cofitness_networks__REPORT.md
title: AMR Co-Fitness Support Networks
sources:
- id: amr_cofitness_networks
  resource: ../sources/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
---
# AMR Co-Fitness Support Networks

## Overview

This report presents a pan-bacterial analysis of antimicrobial-resistance (AMR) gene cofitness support networks across 28 organisms using Fitness Browser fitness matrices, ICA (independent component analysis) fitness modules, AMR catalogs, and InterProScan functional annotations. It identifies organism-specific support-network structure, larger-than-average AMR-containing modules, and enrichment for flagellar motility and amino acid biosynthesis, while emphasizing that enrichment may reflect shared dispensability under laboratory conditions rather than direct co-regulation. [^amr_cofitness_networks]

## Key Findings

### AMR genes occupy large, conserved modules

Of 801 AMR genes with fitness data, 192 (24%) were assigned to ICA fitness modules. AMR-containing modules had a median of 46 genes versus 27 genes in non-AMR modules, a significant difference by MWU (Mann–Whitney U) test (p = 1.7×10⁻⁸). There were 136 unique module families containing AMR genes, and 208/209 (99%) AMR gene-module assignments were in cross-organism conserved module families. Module size did not differ between efflux and enzymatic AMR mechanisms (both median 48, MWU p = 0.91). [^amr_cofitness_networks]

### Cofitness networks are extensive

The analysis included 28 organisms with AMR genes, fitness matrices, and ICA modules. Among 801 AMR genes with fitness data, 769 (96%) had at least one extra-operon cofitness partner at |r| > 0.3. The dataset contained 180,370 total cofitness partners, of which 179,375 were extra-operon; only 0.6% were excluded as near-operon pairs. Mean support-network sizes were 233 genes at |r| > 0.3, 110 at |r| > 0.4, and 71 at |r| > 0.5. [^amr_cofitness_networks]

### InterProScan annotations reveal functional enrichment

Using [interproscan](../entities/interproscan.md) GO (Gene Ontology) annotations, the analysis detected significant enrichment in AMR cofitness neighborhoods. InterProScan provided 68% gene coverage, reported as 3.6× better than the old SEED annotations. Among GO terms enriched in at least 3 organisms at FDR (false discovery rate) < 0.05, the top signals were flagellum-dependent cell motility (GO:0071973; 5 organisms; mean OR 4.7), flagellum assembly (GO:0044780; 5 organisms; mean OR 5.3), bacterial-type flagellum (GO:0009288; 4 organisms; mean OR 4.9), flagellum-dependent swarming (GO:0071978; 4 organisms; mean OR 5.0), histidine biosynthesis (GO:0000105; 3 organisms; mean OR 5.3), and tryptophan biosynthesis (GO:0000162; 3 organisms; mean OR 5.3). [^amr_cofitness_networks]

The old SEED/KEGG annotation analysis found 0/280 significant enrichment tests at FDR < 0.05, whereas InterProScan GO found 35/3,193 significant tests. The report therefore treats annotation quality as critical for genome-wide cofitness functional analysis, while noting that the enrichment categories may be artifacts of shared dispensability under the experimental conditions. [^amr_cofitness_networks]

By mechanism, efflux AMR genes showed the strongest enrichment for amino acid biosynthesis, including histidine biosynthesis in 6 organisms and tryptophan biosynthesis in 5 organisms. Metal-resistance genes showed stronger chemotaxis enrichment in 4 organisms, but no GO term was significantly mechanism-specific after FDR correction. Mechanism-specific GO analyses produced 212 significant results among 9,244 tests. [^amr_cofitness_networks]

### Support networks are more organism-specific than mechanism-specific

Different AMR mechanisms within the same organism shared more support partners than the same mechanism across organisms. The mean Jaccard similarity of GO terms was 0.375 for cross-mechanism comparisons within the same organism and 0.207 for within-mechanism comparisons across organisms; the difference was highly significant (MWU p = 4.3×10⁻¹³). The report interprets this as evidence that each organism’s regulatory, metabolic, and signaling architecture shapes AMR support networks more strongly than resistance-mechanism class. [^amr_cofitness_networks]

The conserved core across mechanisms included transmembrane transport in 87–100% of organisms, signal transduction in 87–100%, transcription regulation in 96–100%, and phosphorelay signaling in 91–100%. Flagellar motility occurred in 53–61% of organisms and amino acid biosynthesis in 30–73%. Histidine biosynthesis showed the only hint of mechanism specificity, with efflux at 68% versus metal resistance at 30% (p = 0.013 uncorrected; q = 0.18 after FDR). [^amr_cofitness_networks]

The annotation comparison strengthened the organism-specificity result: within-mechanism Jaccard similarity increased from 0.069 with old KEGG annotations to 0.207 with InterProScan GO, while cross-mechanism similarity increased from 0.249 to 0.375. The cross-mechanism-versus-within-mechanism comparison had p = 1.0 with old KEGG annotations and p = 4.3×10⁻¹³ with InterProScan GO. [^amr_cofitness_networks]

### Network size does not predict AMR fitness cost

Support-network size was not correlated with AMR gene fitness cost: Spearman rho = −0.006, p = 0.87, N = 769. Within mechanisms, correlations were rho = −0.049 for efflux, rho = +0.038 for enzymatic resistance, and rho = −0.031 for metal resistance; all p > 0.4. The report also states that the uniform resistance cost was +0.086 and was not explained by co-regulatory-neighborhood size. [^amr_cofitness_networks]

### Interpretation of the enrichment signal remains unresolved

The flagellar motility, chemotaxis, and amino acid biosynthesis enrichment supports two interpretations: genuine co-regulation through shared transcription factors or signaling cascades, or shared dispensability under Fitness Browser laboratory conditions. Fitness Browser experiments generally use shaken liquid culture, where flagella and chemotaxis may be unnecessary, and often use rich or defined media with amino acid supplements, where biosynthesis may be redundant; AMR genes are similarly dispensable without antibiotics. [^amr_cofitness_networks]

Evidence favoring the shared-dispensability interpretation includes enrichment for categories expected to be dispensable in shaken-flask culture, absence of energy-metabolism enrichment in 0/25 organisms with a permutation-test fold of 0.91, and the fact that the reported permutation matched conservation class but not mean fitness level. A fitness-matched permutation drawing random non-AMR genes with the same mean-fitness distribution, including the −0.05 to +0.05 range proposed in the report, is identified as the key test. [^amr_cofitness_networks]

Pearson correlation removes each gene’s mean fitness before correlating profiles, so uniformly slightly positive fitness values alone would produce zero correlation. However, dispensable genes can still share condition-responsive patterns, such as greater dispensability under nutrient-rich conditions and lower dispensability under starvation, without being directly co-regulated. [^amr_cofitness_networks]

The organism-specificity result is described as robust to the dispensability confound because the comparison of Jaccard similarities concerns the relative organization of support networks: different mechanisms within one organism shared more partners (J = 0.375) than the same mechanism across organisms (J = 0.207, p = 4.3×10⁻¹³). The report relates this to the contrast between mechanism-dependent conservation and cost: metal resistance was 44% accessory versus 13% for efflux, while mechanism did not explain fitness cost. [^amr_cofitness_networks]

The ICA module-size result is also described as robust: AMR-containing modules had median size 46 versus 27 for non-AMR modules (p = 1.7×10⁻⁸), and ICA decomposition was interpreted as capturing condition-specific co-regulation rather than only shared mean fitness. [^amr_cofitness_networks]

## Caveats and Limitations

- The flagellar and biosynthesis enrichment may reflect shared “useless under laboratory conditions” status rather than mechanistic co-regulation. A permutation matched on mean fitness level, rather than only conservation class, is required to distinguish these explanations. [^amr_cofitness_networks]
- Cofitness is not equivalent to co-regulation: high cofitness indicates shared fitness phenotypes, not direct transcriptional control. Missing fitness values were treated as zero in z-score space through `np.nan_to_num`, which approximates but does not equal pairwise-complete Pearson correlation; the report considers the dense Fitness Browser matrices unlikely to substantially alter conclusions. [^amr_cofitness_networks]
- GO-term granularity may obscure specific signals because broad categories such as transmembrane transport and membrane functions appear in nearly all support networks and genomes. [^amr_cofitness_networks]
- At |r| > 0.3, the mean support network contains 233 genes and therefore includes many weak associations; confirmation at |r| > 0.4 is needed. [^amr_cofitness_networks]
- The null result for the relationship between network size and fitness cost may reflect insufficient variance in fitness cost across genes. [^amr_cofitness_networks]
- The 28 organisms are lab-adapted, phylogenetically biased, include many Pseudomonas organisms, and have limited ecological diversity. [^amr_cofitness_networks]
- The operon-exclusion heuristic uses matrix row index position as a proxy for genomic proximity, although genomic `begin`, `end`, and `strand` columns were available for coordinate-based exclusion. Only 0.6% of pairs were excluded by the current heuristic. [^amr_cofitness_networks]
- The most important follow-up analyses are fitness-matched permutations; cofitness computed separately for antibiotic and standard-growth conditions; direct assessment of mean fitness for flagellar knockouts; Pfam-domain enrichment; and testing other conditionally dispensable gene classes such as phage-defense and secondary-metabolite genes. [^amr_cofitness_networks]

## Slots Into

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — cofitness neighborhoods may capture condition-specific shared dispensability rather than direct co-regulation, and the report specifies fitness-matched and condition-specific tests to resolve this. [^amr_cofitness_networks]
- [gene-essentiality](../concepts/gene-essentiality.md) — AMR, flagellar, and biosynthetic gene fitness phenotypes under laboratory conditions are central to interpreting the enrichment and the null network-size–cost relationship. [^amr_cofitness_networks]
- [pangenome-integration](../concepts/pangenome-integration.md) — InterProScan GO annotation of pangenome cluster representatives improved coverage and transformed legacy annotation null results into detectable functional enrichment. [^amr_cofitness_networks]

[^amr_cofitness_networks]: [amr cofitness networks](../sources/amr_cofitness_networks__REPORT.md)
