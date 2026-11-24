---
type: "Organism"
description: "Fitness Browser organism with deep condition coverage that dominates dark-gene prioritization."
sources: ["summaries/discoveries.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
aliases: ["MR-1", "MR1", "Shewanella MR-1"]
---
# Shewanella oneidensis MR-1

Shewanella oneidensis MR-1 (also MR-1, MR1, Shewanella MR-1) is a Fitness Browser organism. Its deep condition coverage makes it dominate dark-gene prioritization in the functional dark matter analysis. The report itself attributes this dominance to coverage depth, not to special biology, so the evidence is a ranking outcome from one analysis. [src: functional_dark_matter, discoveries]

## Key facts

- MR-1 contributes 25/100 top fitness-active dark gene candidates and has 587 scored dark genes. [src: discoveries]
- Three experiments (stress, nitrogen, carbon) would cover 20.8% of the top-500 candidates. The report counts this as 111 candidates and calls MR-1 the single highest-value organism for dark gene characterization. [src: discoveries, functional_dark_matter]
- The report ties this value to 121 conditions, a large dark gene complement, and 142 genes with |fit| >= 4. [src: discoveries, functional_dark_matter]
- The top 100 candidates span 22 organisms, with MR-1 (25), Pseudomonas putida N2C3 (18) and Marinobacter (9) most represented. [src: functional_dark_matter]
- Deutschbauer et al. (2011) pioneered genome-wide fitness profiling for function prediction in MR-1. They used 121 conditions to propose functions for 40 previously hypothetical genes. [src: functional_dark_matter]
- The report calls the 25/100 share consistent with MR-1 being a model organism with extensive condition coverage and many hypothetical genes. [src: functional_dark_matter]
- 544 MR-1 dark genes have specific condition recommendations (stress, nitrogen, carbon). [src: functional_dark_matter]
- The Tier 1 pathway analysis includes MR-1 (abbreviated MR1) among 7 Fitness Browser organisms with GapMind pathway data. [src: pathway_capability_dependency]
- MR1 (Shewanella oneidensis, genome GCF_000146165.2) has 694 GapMind predictions and 18/18 amino acid pathways complete (100%). [src: essential_metabolome]

## Route A versus Route B prioritization

Which route is used changes MR-1's rank. Route A puts MR-1 first for deep condition evidence. Route B puts Sinorhizobium meliloti first for the most kingdom-level gaps. [src: discoveries]

In Route A, MR-1 is selected first with 587 genes, tractability 0.8, and 121 historical conditions. Its dark genes span all tiers, with 172 T5 Dawn and 257 T4 Penumbra genes. [src: functional_dark_matter]

In Route B, MR-1 is third, with 805 OGs (ortholog groups), 105 kingdom gaps and tractability 0.8. The report says Route B weights conservation breadth over condition-specific evidence depth. [src: functional_dark_matter] The conservation-weighted covering set likewise lists 805 genes and 105 kingdom gaps for MR-1. [src: functional_dark_matter] See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]].

## Top-ranked MR-1 dark genes

Top-ranked MR-1 candidates are all core genes. They fall in stress, nitrogen, carbon and motility conditions. [src: functional_dark_matter]

| Rank | Gene | Fit | Condition | Module | Domains | Score |
|---|---|---|---|---|---|---|
| 2 | 202463 | 6.4 | stress | PF01145 | YGGT | 0.698 [src: functional_dark_matter] |
| 3 | 199738 | 5.5 | nitrogen | K03306 | Gcw_chp, TIGR02001 | 0.698 [src: functional_dark_matter] |
| 4 | 203545 | 4.0 | nitrogen | K03306 | DUF4124 | 0.694 [src: functional_dark_matter] |
| 5 | 202450 | 3.9 | nitrogen | K03306 | Gly_transporter | 0.693 [src: functional_dark_matter] |
| 8 | 201124 | 5.0 | nitrogen | PF01144 | HgmA_N, HgmA_C | 0.685 [src: functional_dark_matter] |
| 10 | 203247 | 4.6 | stress | PF01145 | GBBH-like_N | 0.685 [src: functional_dark_matter] |
| 11 | 203720 | 4.5 | nitrogen | none | Ser_hydrolase | 0.680 [src: functional_dark_matter] |
| 13 | 203026 | 3.5 | carbon | none | AFG1_ATPase | 0.677 [src: functional_dark_matter] |
| 15 | 201809 | 4.4 | stress | none | PG_binding_3, Glyco_hydro_108 | 0.674 [src: functional_dark_matter] |
| 16 | 201731 | 4.0 | motility | TIGR00254 | ZapC | 0.674 [src: functional_dark_matter] |
| 18 | 202474 | 7.1 | carbon | PF00460 | YggL_50S_bp | 0.672 [src: functional_dark_matter] |

### Proposed interpretations

These are the report's hypotheses, not tested results.

- Genes 199738, 203545 and 202450 carry K03306 predictions with different domain architectures. The report suggests they are paralogous members of a conserved nitrogen-responsive system. [src: functional_dark_matter] It proposes comparing single and double mutants to test functional redundancy under nitrogen conditions. [src: functional_dark_matter]
- For 203545, a shared module with a different domain from 199738 suggests subfunctionalization. [src: functional_dark_matter] For 202450, the glycine transporter domain suggests a nitrogen/amino acid link. [src: functional_dark_matter]
- Genes 202463 and 203247 predict PF01145 under stress, pointing to a stress-responsive YGGT/GBBH-like membrane protein family. [src: functional_dark_matter] Gene 203631 (|fit|=4.5) also carries a PF01145 prediction. [src: functional_dark_matter]
- Route A ranks 202463 second, with the highest fitness magnitude among top candidates, a YGGT domain and a co-regulated module. [src: functional_dark_matter] The carbon targets 202474 (|fit|=7.1) and 202608 (|fit|=7.3) have the highest fitness magnitudes in the entire top-100. [src: functional_dark_matter]

## Experimental roadmap

The roadmap gives priority 1 to MR-1 under stress. That experiment addresses 57 dark genes, 10.7% of the Top 500. [src: functional_dark_matter]

## Caveats

The 25/100 share reflects condition coverage depth (121 conditions), which the report says is not inherent biology. [src: functional_dark_matter] Route B's lower ranking shows the result depends on the weighting. [src: functional_dark_matter] See also [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]] and [[summaries/functional_dark_matter__REPORT]].
