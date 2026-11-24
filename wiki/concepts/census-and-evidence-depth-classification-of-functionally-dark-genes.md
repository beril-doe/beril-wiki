---
type: "Concept"
description: "How many bacterial genes lack functional annotation, how much residual evidence each carries (darkness tiers, partial clues), and how multi-evidence scoring ranks them for follow-up; stops short of the specific inference layers."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Census and evidence-depth classification of functionally dark genes

How many bacterial genes lack functional annotation, how much residual evidence each carries (darkness tiers, partial clues), and how multi-evidence scoring ranks them for follow-up; stops short of the specific inference layers.

## How many genes are dark

Across 48 Fitness Browser organisms (228,709 genes), 57,011 genes (24.9%) lack functional annotation: "hypothetical protein," DUF, or "uncharacterized". [src: functional_dark_matter] See [[entities/fitness-browser]]. The 24.9% fraction aligns with published estimates of 25–40% hypothetical genes in typical bacterial genomes, attributed to Makarova et al. (2019). [src: functional_dark_matter] Among these, 7,787 show strong fitness effects (|fitness| ≥ 2 in at least one condition). [src: functional_dark_matter] Another 9,557 are essential, meaning no viable transposon mutants. [src: functional_dark_matter] Together, 17,344 of the 57,011 have a measurable phenotype of one of these two kinds. [src: functional_dark_matter]

Dark genes are not randomly distributed across organisms. Some species have >35% hypothetical genes and others <15%, which the report attributes to annotation depth rather than true functional content. [src: functional_dark_matter] The report unifies the 57,011 dark genes by integrating fitness, conservation, module, ortholog and domain data from 4 prior observatory projects. [src: functional_dark_matter]

The count probably overestimates the truly uncharacterized genes. Some "hypothetical" genes may be annotated in databases the report did not check (UniProt, InterPro, recent NCBI updates). [src: functional_dark_matter]

Annotation gaps vary by gene class. Among bacterial paradox proteins, 286,439 (68.9%) are hypothetical. [src: alphafold_msa_annotation] The report contrasts this with a global core-gene hypothetical rate of 3.8%. [src: alphafold_msa_annotation]

## Darkness tiers

Most dark genes are not blank. The census assigns all 57,011 dark genes to tiers by evidence depth, using 6 binary evidence flags: domain annotation, ortholog group, function prediction, co-fitness partner, fitness/essentiality phenotype, and pangenome context. [src: functional_dark_matter]

| Tier | Name | Genes | Interpretation |
|---|---|---:|---|
| T1 | Void | 4,273 (7.5%) | No evidence of any kind [src: functional_dark_matter] |
| T2 | Twilight | 12,282 (21.5%) | Single clue (domain or ortholog only) [src: functional_dark_matter] |
| T3 | Dusk | 16,103 (28.2%) | Two converging hints [src: functional_dark_matter] |
| T4 | Penumbra | 22,500 (39.5%) | Substantial evidence, testable hypotheses [src: functional_dark_matter] |
| T5 | Dawn | 1,853 (3.3%) | 5–6 evidence lines, nearly characterized [src: functional_dark_matter] |

Only 7.5% of dark genes sit in T1 Void. [src: discoveries, functional_dark_matter] T4 Penumbra is the largest group, at 39.5%, with 3–4 converging lines of evidence. [src: discoveries, functional_dark_matter] Overall, 92.5% of dark genes have at least some evidence. [src: functional_dark_matter] The digest draws the conclusion that the dark-matter problem is not monolithic. It names targeted experimental validation, not computational inference, as the key bottleneck for most genes. [src: discoveries]

The report uses the tiers to allocate resources: T5 Dawn genes need confirmation, [src: functional_dark_matter] T4 Penumbra genes need targeted experiments, [src: functional_dark_matter] and T1 Void genes need broad screens. [src: functional_dark_matter] It claims this structured framework is absent from prior metagenomic surveys, which typically treat uncharacterized proteins as a single class. [src: functional_dark_matter]

## Residual clues in the truly dark subset

A separate truly_dark_genes analysis supports the same picture. Only 246 of 6,427 truly dark genes (3.8%) have zero annotation clues, found with a 12-dimensional clue matrix. [src: discoveries, truly_dark_genes] The remaining 96.2% have combinations of sequence identifiers, eggNOG hits, orthologs, module membership or fitness phenotypes. [src: truly_dark_genes] Across the truly dark set, 84.7% have database cross-references. [src: discoveries] 43.5% have eggNOG hits, though 55% of COG (clusters of orthologous groups) assignments are "S"/unknown. [src: discoveries] 29.3% have cross-organism orthologs. [src: discoveries] 9.5% are in ICA (independent component analysis) fitness modules. [src: discoveries] The two analyses use different gene sets, so their zero-evidence rates (3.8% and 7.5%) are not directly comparable. [src: discoveries]

The report also catalogs a 41-column annotation clue profile for each truly dark gene. The profile lists all available partial evidence, so hypotheses can be generated even for genes with no product annotation. [src: truly_dark_genes]

### Sparse annotation landscape

The analysis covers 5,870 unique truly dark gene clusters. [src: truly_dark_genes] Despite the "hypothetical" label, 79.4% of truly dark genes have UniRef50 links and 84.7% have database cross-references including RefSeq and UniParc. [src: truly_dark_genes] Cross-references total 26,917 entries for 4,971 clusters (84.7%). They are dominated by SO, UniRef and UniParc identifiers, with only 6 KEGG and 1 EC number. [src: truly_dark_genes]

Standard functional annotation resources add little. Only 4.0% of truly dark genes have Pfam domain hits and only 4.6% have KEGG KOs, which the report reads as resistance to standard annotation methods. [src: truly_dark_genes] Pfam gives 362 hits for 235 clusters (4.0%), with TPR repeats dominating non-DUF hits, and 56 clusters have DUF-only domains. [src: truly_dark_genes] eggNOG-mapper gives partial signal for 43.5% of truly dark clusters, but 55.4% of COG assignments are category S, function unknown. [src: truly_dark_genes] The rest span L, M, K, T, C and J with no dominant functional theme. [src: truly_dark_genes]

The eggNOG count is 2,551 annotations for 2,551 truly dark clusters (43.5%). [src: truly_dark_genes] Across all truly dark clusters, only 17.0% have COG categories and 4.6% have KEGG KOs. [src: truly_dark_genes]

Orthologs add a further line of evidence: 3,449 pairs cover 1,885 truly dark genes (29.3% of TD genes) across 48 Fitness Browser organisms. [src: truly_dark_genes] Among truly dark genes in ICA organisms, 594 belong to ICA fitness modules. Guilt-by-association on these modules reveals functions including phage integrases, metal transporters, chemotaxis systems, and iron regulation. [src: truly_dark_genes]

### Truly dark tiers

| Tier | Genes | Evidence |
|---|---:|---|
| Tier 1: No clues | 246 (3.8%) | No sequence IDs, no hits, no phenotype [src: truly_dark_genes] |
| Tier 2: Minimal | 3,867 (60.2%) | Sequence identifiers only (UniRef50/RefSeq) [src: truly_dark_genes] |
| Tier 3: Partial function | 711 (11.1%) | Pfam, COG or eggNOG description [src: truly_dark_genes] |
| Tier 4: Phenotype only | 1,603 (24.9%) | Fitness/essential/module signal, no functional annotation [src: truly_dark_genes] |

The report prioritizes Tier 3 and Tier 4 genes (2,314 total), because their partial clues can narrow experimental hypotheses. [src: truly_dark_genes]

## Hypothesis status

A separate classification gives each dark gene ortholog group (OG) a hypothesis status. [src: functional_dark_matter] Strong testable hypotheses cover 6.0%. They rest on a module prediction with an EC (Enzyme Commission) number, high cross-organism concordance, a high-confidence GapMind match, or a named domain plus strong fitness. [src: functional_dark_matter] Weak leads cover 52.5%. They rest on a DUF-only domain, a bare module prediction, medium/low GapMind, strong fitness without annotation, or a named domain without fitness. [src: functional_dark_matter] True knowledge gaps cover 41.5% and have zero functional evidence of any kind. [src: functional_dark_matter] The 41.5% gap figure differs from the 7.5% T1 Void share. The two schemes are defined by different criteria, and the cited claims give no reconciliation. [src: discoveries, functional_dark_matter]

Per-organism action plans split genes into 14,450 hypothesis-bearing genes, with specific condition recommendations from fitness data, module prediction or neighbor context, and 2,038 darkest genes that need broad phenotypic screens. [src: functional_dark_matter]

The report treats its hypotheses as partly supported. It judges H1 partially supported and H0 partially rejected, because dark genes with strong fitness effects show non-random patterns across multiple evidence dimensions. [src: functional_dark_matter]

## Multi-evidence ranking

The 17,344 phenotype-bearing genes are called experimentally actionable: genes with clear biological importance but unknown function. [src: functional_dark_matter] They are ranked by a composite score of 6 weighted dimensions, each 0–1. [src: functional_dark_matter] The report describes the scoring as using 6 evidence axes: fitness importance, cross-organism conservation, functional inference quality, pangenome distribution, biogeographic signal, and experimental tractability. [src: functional_dark_matter] A second description of the composite names fitness importance, conservation, module membership, domain annotations, biogeographic signal, and tractability. [src: functional_dark_matter] The report says convergence of independent lines identifies genes that are both important and interpretable. [src: functional_dark_matter] It extends multi-evidence prioritization to 48 organisms with 6 evidence dimensions and adds set-cover organism selection to turn gene-level priorities into an experimental campaign. [src: functional_dark_matter] The result is 100 ranked candidates with specific hypotheses and suggested experiments. [src: functional_dark_matter]

The top 100 candidates score 0.624–0.715 and span 22 organisms. [src: functional_dark_matter] *Shewanella* MR-1 contributes 25, *P. putida* N2C3 contributes 18 and Marinobacter contributes 9. [src: functional_dark_matter] The report attributes MR-1's 25 to its deep coverage of 121 conditions rather than inherent biology. [src: functional_dark_matter] More extensively tested organisms are biased toward higher scores, because conditions differ across the 48 organisms. [src: functional_dark_matter] Of the 100, 82 have high-confidence functional hypotheses supported by 3+ evidence types, and 85 have module-based function predictions. [src: functional_dark_matter] 97 have domain annotations. [src: functional_dark_matter] The report says 82% have testable hypotheses with specific experimental protocols. [src: functional_dark_matter] "High confidence" reflects evidence convergence, not experimental proof. [src: functional_dark_matter] See [[entities/shewanella-oneidensis-mr-1]].

### Weight sensitivity

Rankings are robust overall but not at the level of exact lists. Rank correlations stay high (ρ > 0.93) across 6 alternative weight configurations. [src: functional_dark_matter] Specific top-50 lists are only moderately sensitive, with 64% retention under conservation-dominant weighting. [src: functional_dark_matter] For fitness-active genes in NB05, conservation-dominant and drop-tractability weights each retain only 32/50 original top candidates (64%). [src: functional_dark_matter] In NB10, 18 genes stay in the top 50 [src: functional_dark_matter] and 35 stay in the top 100 [src: functional_dark_matter] across all 6 fitness-active weight configurations. The report calls these "always-top" candidates the most defensible follow-up targets. [src: functional_dark_matter] It advises treating rankings as approximate and focusing on genes in the top tier across weight schemes. [src: functional_dark_matter] Both prioritization frameworks use arbitrary expert-assigned weights. [src: functional_dark_matter]

### Truly dark ranking

A separate multi-criteria system scores all 6,427 truly dark genes on fitness importance, annotation clues, ortholog breadth, genomic context and tractability (max score 12). [src: truly_dark_genes] It identifies 100 top candidates (scores 8–10) across 19 organisms. [src: truly_dark_genes] The 100-candidate ranked list integrates fitness importance, annotation clues, genomic context, ortholog breadth, and experimental tractability, enabling resource-efficient experimental campaigns. [src: truly_dark_genes] The report estimates ~2,841 additional truly dark genes among 17,479 unlinked dark genes at the 16.3% truly-dark rate, including 2,208 with strong fitness phenotypes. [src: truly_dark_genes] The ranked list covers ~69% of the estimated total truly dark population. [src: truly_dark_genes] For these sequences, the report proposes AlphaFold2/ESMFold structure prediction on the top 100 and Foldseek searches for remote structural homologs. [src: truly_dark_genes] It calls this the most promising path to annotation for sequences with no detectable sequence homology. [src: truly_dark_genes] It describes structure prediction (AlphaFold2/ESMFold plus Foldseek) as the next frontier for these candidates. [src: truly_dark_genes]

### Top-ranked candidates

| Rank | Organism | Gene | Top condition (|fit|) | Score |
|---|---|---|---|---:|
| 1 | P. putida N2C3 | AO356_11255 | nitrogen (3.4) | 0.715 [src: functional_dark_matter] |
| 2 | Shewanella MR-1 | 202463 | stress (6.4) | 0.698 [src: functional_dark_matter] |
| 3 | Shewanella MR-1 | 199738 | nitrogen (5.5) | 0.698 [src: functional_dark_matter] |
| 4 | Shewanella MR-1 | 203545 | nitrogen (4.0) | 0.694 [src: functional_dark_matter] |
| 5 | Shewanella MR-1 | 202450 | nitrogen (3.9) | 0.693 [src: functional_dark_matter] |
| 6 | P. putida N2C3 | AO356_18320 | motility (3.8) | 0.689 [src: functional_dark_matter] |
| 7 | P. fluorescens N1B4 | Pf1N1B4_3696 | pH (3.7) | 0.687 [src: functional_dark_matter] |
| 8 | Shewanella MR-1 | 201124 | nitrogen (5.0) | 0.685 [src: functional_dark_matter] |
| 9 | P. putida N2C3 | AO356_15270 | carbon (5.6) | 0.685 [src: functional_dark_matter] |
| 10 | Shewanella MR-1 | 203247 | stress (4.6) | 0.685 [src: functional_dark_matter] |
| 11 | Shewanella MR-1 | 203720 | nitrogen (4.5) | 0.680 [src: functional_dark_matter] |
| 12 | Marinobacter | GFF2506 | stress (3.4) | 0.678 [src: functional_dark_matter] |
| 13 | Shewanella MR-1 | 203026 | carbon (3.5) | 0.677 [src: functional_dark_matter] |
| 14 | Marinobacter | GFF1827 | stress (3.7) | 0.676 [src: functional_dark_matter] |
| 15 | Shewanella MR-1 | 201809 | stress (4.4) | 0.674 [src: functional_dark_matter] |
| 16 | Shewanella MR-1 | 201731 | motility (4.0) | 0.674 [src: functional_dark_matter] |
| 17 | Marinobacter | GFF1367 | stress (5.7) | 0.672 [src: functional_dark_matter] |
| 18 | Shewanella MR-1 | 202474 | carbon (7.1) | 0.672 [src: functional_dark_matter] |
| 19 | P. putida N2C3 | AO356_17245 | stress (3.6) | 0.671 [src: functional_dark_matter] |
| 20 | P. putida N2C3 | AO356_08210 | stress (4.0) | 0.670 [src: functional_dark_matter] |

Some of these have specific hypotheses. Gene 202463 (rank 2) is proposed as a stress-responsive membrane protein (PF01145). It has the highest fitness magnitude among the top candidates, a YGGT domain and a co-regulated module. [src: functional_dark_matter] Genes 199738, 203545 and 202450 form a K03306-family paralog trio with nitrogen as the top condition. [src: functional_dark_matter] Comparing their mutants tests functional redundancy. [src: functional_dark_matter] A shared module with different domains suggests subfunctionalization. [src: functional_dark_matter] The glycine transporter domain of 202450 suggests a nitrogen/amino acid link. [src: functional_dark_matter]

## Open Directions

- Reconcile the T1 Void count (4,273 genes) with the 41.5% "true knowledge gap" share, by cross-tabulating the two schemes over the same 57,011 genes. This would show which evidence types account for the difference.
- Re-estimate the truly dark residual-evidence rates after excluding COG "S" assignments. This would show how much of the 43.5% eggNOG coverage carries real functional information.
- Test the Shewanella K03306 paralog trio (199738, 203545, 202450) with single and combined mutants under nitrogen conditions. This would test the redundancy and subfunctionalization hypotheses.
- Run broad phenotypic screens on the 2,038 darkest genes. This would show whether any gain a testable hypothesis.
- Re-rank the top 100 after normalizing for the number of conditions tested per organism. This would show how much of MR-1's 25 candidates reflects condition depth.
- Re-check the 57,011 dark genes against UniProt, InterPro and current NCBI annotations. This would show how many are already annotated.
- Run AlphaFold2/ESMFold and Foldseek on the 100 top truly dark candidates. This would test whether structure gives annotation clues where sequence homology is absent.
