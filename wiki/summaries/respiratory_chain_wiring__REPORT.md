---
type: "Summary"
description: "Summary of the project Condition-Specific Respiratory Chain Wiring in ADP1."
doc_type: "short"
full_text: "sources/respiratory_chain_wiring__REPORT.md"
---
# Condition-Specific Respiratory Chain Wiring in ADP1

This report asks how the branched respiratory chain of Acinetobacter baylyi ADP1 is wired for different carbon sources. Its main answer is that ADP1 uses qualitatively different respiratory configurations per substrate, not a quantitative gradient. [src: respiratory_chain_wiring] The ADP1 results rest on growth data for 36 of 62 respiratory genes, theoretical stoichiometry and proteomics. [src: respiratory_chain_wiring] The cross-species test of NDH-2 compensation was a null result. [src: respiratory_chain_wiring] The report also lists several caveats: identification of NDH-2 by text matching, a small comparison group, and an untested pangenome analysis. [src: respiratory_chain_wiring]

## Key Findings

### Condition-specific wiring
- ADP1's branched respiratory chain has 62 genes across 8 subsystems. [src: respiratory_chain_wiring]
- The subsystems are Complex I (13 genes), NDH-2 (1), NADH-flavin oxidoreductases (5), cytochrome bo3 (4), cytochrome bd (5), Complex II/SDH (5), ATP synthase (9) and other respiratory components (20). [src: respiratory_chain_wiring]
- The chain is wired in a condition-dependent manner. [src: respiratory_chain_wiring]
- The report claims the first systematic demonstration that a single bacterium uses qualitatively different respiratory configurations for different carbon sources. [src: respiratory_chain_wiring]
- The branching is functionally specialized by substrate, not just structural redundancy. [src: respiratory_chain_wiring]
- This is consistent with Melo & Teixeira (2016), who described bacterial respiratory supercomplexes with multiple entry and exit points for electrons. [src: respiratory_chain_wiring]

| Carbon source | Required | Dispensable |
|---|---|---|
| Quinate | Complex I only [src: respiratory_chain_wiring] | Cyt bo3, Cyt bd, SDH, all others [src: respiratory_chain_wiring] |
| Acetate | Complex I, Cyt bo3, ACIAD3522 and more; most demanding [src: respiratory_chain_wiring] | None [src: respiratory_chain_wiring] |
| Lactate | Cyt bo3 [src: respiratory_chain_wiring] | Complex I (mild), Cyt bd [src: respiratory_chain_wiring] |
| Glucose | None specifically [src: respiratory_chain_wiring] | All (full redundancy) [src: respiratory_chain_wiring] |
| Urea | Everything (generally demanding) [src: respiratory_chain_wiring] | None [src: respiratory_chain_wiring] |

### Three parallel NADH dehydrogenases
- ADP1 has three parallel NADH dehydrogenases with distinct condition profiles. [src: respiratory_chain_wiring]
- Their non-overlapping condition requirements demonstrate metabolic division of labor in electron transport. [src: respiratory_chain_wiring]
- Complex I (NDH-1) has 13 subunits and pumps 4 H⁺/NADH. [src: respiratory_chain_wiring]
- Complex I growth ratios are 0.37 on quinate (essential), 1.44 on glucose (dispensable) and 0.49 on acetate (defect). [src: respiratory_chain_wiring]
- ACIAD3522 (NADH-FMN OR) has 1 subunit and does not pump protons. [src: respiratory_chain_wiring]
- ACIAD3522 growth ratios are 1.39 on quinate (dispensable), 1.39 on glucose (dispensable) and 0.013 on acetate (lethal). [src: respiratory_chain_wiring]
- The report suggests that ACIAD3522's acetate-lethality and FMN cofactor imply a specific role in acetate catabolism that deserves further investigation. [src: respiratory_chain_wiring]
- However, ACIAD3522 may not be a true respiratory NADH dehydrogenase, because its "NADH-FMN oxidoreductase" annotation could indicate other metabolic functions. [src: respiratory_chain_wiring]
- NDH-2 has 1 subunit and does not pump protons. [src: respiratory_chain_wiring]
- NDH-2 is ACIAD_RS16420, with KEGG ortholog (KO) K03885. [src: respiratory_chain_wiring]
- NDH-2 is TnSeq-dispensable. [src: respiratory_chain_wiring]
- NDH-2 is missing from the deletion collection, so it has no growth data. [src: respiratory_chain_wiring]
- NDH-2 is a standalone gene, not in a respiratory operon, and is core genome. [src: respiratory_chain_wiring]
- NDH-2 is a low-capacity backup for Complex I. [src: respiratory_chain_wiring]
- ADP1 has both systems, with Complex I as the high-capacity primary one. [src: respiratory_chain_wiring]
- This is consistent with Lencina et al. (2018), who showed NDH-2 can be the sole NADH dehydrogenase in some organisms (S. agalactiae). [src: respiratory_chain_wiring]

### Rate versus yield
- Quinate produces fewer NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50). [src: respiratory_chain_wiring]
- Yet Complex I is more essential on quinate. [src: respiratory_chain_wiring]
- The report resolves this paradox by NADH flux rate, with a concentrated TCA burst on quinate versus distributed production on glucose. [src: respiratory_chain_wiring]
- Aromatic ring cleavage via the β-ketoadipate pathway produces succinyl-CoA and acetyl-CoA simultaneously. [src: respiratory_chain_wiring]
- This creates a concentrated NADH burst in the tricarboxylic acid (TCA) cycle that exceeds NDH-2's reoxidation capacity. [src: respiratory_chain_wiring]
- Glucose distributes NADH production across Entner-Doudoroff pathway steps plus TCA, staying within NDH-2's capacity. [src: respiratory_chain_wiring]
- The report proposes that this principle should apply to any substrate whose catabolism produces concentrated reducing equivalents. [src: respiratory_chain_wiring]
- On quinate, cytochrome bo3 and bd are dispensable because the terminal oxidase step is not the bottleneck; NADH reoxidation is. [src: respiratory_chain_wiring]
- On acetate, direct TCA entry gives continuous NADH production requiring all available dehydrogenases, with cytochrome bo3 as the primary terminal oxidase. [src: respiratory_chain_wiring]
- On lactate, Complex I is only mildly important (0.77), suggesting NDH-2 partially compensates. [src: respiratory_chain_wiring]
- The flux-rate hypothesis predicts higher NADH/NAD⁺ ratios in quinate-grown cells than glucose-grown cells, and the report proposes metabolomics as a direct test. [src: respiratory_chain_wiring]

| Substrate | Total NADH | NADH/carbon | Production | Complex I growth |
|---|---|---|---|---|
| Quinate | 4 | 0.57 | Concentrated TCA burst | 0.37 (essential) [src: respiratory_chain_wiring] |
| Glucose | 9 | 1.50 | Distributed (ED + TCA) | 1.44 (dispensable) [src: respiratory_chain_wiring] |
| Acetate | 3 | 1.50 | All through TCA | 0.49 (defect) [src: respiratory_chain_wiring] |
| Lactate | 5 | 1.67 | Pyruvate + TCA | 0.77 (mild) [src: respiratory_chain_wiring] |

### Flux balance analysis misses this
- Flux balance analysis (FBA) predicts zero flux through NDH-2 on all standard carbon sources, routing all NADH through Complex I. [src: respiratory_chain_wiring]
- The model predicts zero flux through NDH-2 and ACIAD3522 on all standard media. [src: respiratory_chain_wiring]
- FBA optimizes for growth rate and routes NADH through Complex I, which generates more ATP (adenosine triphosphate) per NADH. [src: respiratory_chain_wiring]
- This is the fundamental reason FBA models fail to predict condition-specific respiratory requirements. [src: respiratory_chain_wiring]
- They assume the optimal pathway is always used and miss capacity constraints that force suboptimal pathways under high flux. [src: respiratory_chain_wiring]

### Expression: passive wiring
- Under standard growth conditions, Complex I has mean protein expression 27.6 (66th percentile). [src: respiratory_chain_wiring]
- NDH-2 has 27.0 (59th percentile). [src: respiratory_chain_wiring]
- ACIAD3522 has 26.2 (48th percentile). [src: respiratory_chain_wiring]
- The genome median is 26.4. [src: respiratory_chain_wiring]
- The spread is only 1.4 units. [src: respiratory_chain_wiring]
- NDH-2 is not repressed but constitutively co-expressed with Complex I. [src: respiratory_chain_wiring]
- Wiring operates at the metabolic level: all three dehydrogenases are present, and which one becomes limiting depends on NADH flux from the carbon source. [src: respiratory_chain_wiring]
- The cell uses a passive, flux-based wiring system rather than an active transcriptional switch. [src: respiratory_chain_wiring]

### Cross-species NDH-2 compensation (null result)
- After filtering likely false positives, 5 of 14 organisms have validated NDH-2. [src: respiratory_chain_wiring]
- The filter kept organisms with 1-2 NDH-2 hits and excluded those with more than 2 hits, which likely represent misannotated Complex I subunits. [src: respiratory_chain_wiring]
- Organisms with NDH-2 show larger Complex I aromatic deficits (mean = -0.297) than those without (mean = -0.156). [src: respiratory_chain_wiring]
- This is the opposite of the compensation prediction, and it is not significant (p = 0.52). [src: respiratory_chain_wiring]
- NDH-2 presence does not predict whether Complex I is dispensable on aromatics. [src: respiratory_chain_wiring]
- The compensation is likely ADP1-specific, not a general cross-species pattern. [src: respiratory_chain_wiring]
- The comparison has only 4 organisms without NDH-2, which the report calls insufficient for statistical significance. [src: respiratory_chain_wiring]
- The P. putida aromatic fitness data align with published knowledge of Pseudomonas aromatic catabolism. [src: respiratory_chain_wiring]
- P. putida KT2440 is a well-studied aromatic degrader that channels diverse aromatic compounds through the β-ketoadipate pathway. [src: respiratory_chain_wiring]

## Data and Methods
The analysis was run in notebooks for the respiratory chain map, indirect NDH-2 analysis, stoichiometry, cross-species respiratory comparison and proteomics expression. [src: respiratory_chain_wiring]
ADP1 growth ratios, FBA predictions and reaction stoichiometry come from the user-provided SQLite database berdl_tables.db (tables genome_features, gene_phenotypes, gene_reaction_data, genome_reactions). [src: respiratory_chain_wiring]
Cross-species aromatic experiments and Complex I/NDH-2 fitness come from the Fitness Browser (FB) database kescience_fitnessbrowser (tables experiment, gene, genefitness). [src: respiratory_chain_wiring]

## Caveats and Open Work
- Of the 62 respiratory genes, 36 have growth data and 26 do not, including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]
- NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be tested directly. [src: respiratory_chain_wiring]
- The stoichiometry uses theoretical pathway biochemistry, not measured flux distributions. [src: respiratory_chain_wiring]
- The ADP1 wiring pattern may be species-specific rather than a general rule. [src: respiratory_chain_wiring]
- The NDH-2 gene search in FB organisms may miss orthologs because of variable annotation. [src: respiratory_chain_wiring]
- NDH-2 identification in NB04 uses gene-description text matching, which likely produces false positives for organisms with incompletely annotated Complex I subunits. [src: respiratory_chain_wiring]
- An example is pseudo3_N2E3, whose 8 putative NDH-2 hits are probably a Complex I operon. [src: respiratory_chain_wiring]
- The report considers KO-based identification (K03885) more reliable. [src: respiratory_chain_wiring]
- The planned pangenome KO co-occurrence analysis was not performed, so NDH-2/Complex I co-occurrence across Acinetobacter species remains untested. [src: respiratory_chain_wiring]
- Proposed next step: construct an ADP1 NDH-2 knockout, the definitive experimental test of the prediction that NDH-2 deletion makes Complex I essential on glucose. [src: respiratory_chain_wiring]
- Proposed next step: measure NADH/NAD⁺ ratios per carbon source by metabolomics. [src: respiratory_chain_wiring]
- Proposed next step: query the full KBase Data Lakehouse pangenome for NDH-2 (K03885) and Complex I (K00330-K00343) co-occurrence across 27K species, for a much larger sample. [src: respiratory_chain_wiring]
- Proposed next step: characterize ACIAD3522 to determine whether it is a true respiratory NADH dehydrogenase or a metabolic enzyme. [src: respiratory_chain_wiring]
- Proposed next step: reanalyze respiratory chain proteins in the quinate-versus-succinate proteomics of Stuani et al. (2014), to test whether ADP1 upregulates Complex I on aromatics and NDH-2 on glucose. [src: respiratory_chain_wiring]
