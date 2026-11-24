<!-- tension-hash: c44f44dce8ee4372 -->
# Tension: High-Scoring Pathobiont Targets Versus Phage Availability and Replication Limits

The ibd_phage_targeting project ranked candidate pathobionts (disease-associated gut bacteria) for phage therapy in Crohn's disease (CD) using a scoring step called NB05. The highest NB05 scorers have the weakest phage availability, and a separate per-ecotype repair (three evidence filters applied within each gut-microbiome ecotype) passed few candidates. Both findings bear on which targets deserve experimental effort and on how far cocktail drafts can be trusted. This page records the disagreement without choosing a side. It draws on [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

## Evidence Sides

**Side A: scores favour some targets, but phage availability is weakest for them**
- The top NB05 scorers, H. hathewayi (4.0) and M. gnavus (3.8), have the weakest phage availability. [src: ibd_phage_targeting]
- H. hathewayi and F. plautii are both Pillar-4 GAP, meaning the phage-targetability evidence has a coverage gap for them. [src: ibd_phage_targeting]
- NB05 scored H. hathewayi 4.0, E. coli 3.6 and E. lenta 3.3 among its actionable targets. [src: ibd_phage_targeting]

**Side B: the per-ecotype repair passed few candidates, and replication is weak**
- The repair passed 3 of 15 E3 candidates and 0 of 18 E1 candidates. [src: discoveries]
- Weak cross-cohort replication makes Tier-A candidates, especially E3, hypotheses for experimental validation. UC Davis cocktail drafts inherit this limit. [src: ibd_phage_targeting]

**What is not established**
- The NB05 scores and the repair results are reported separately. The claims do not say how the NB05 list maps onto the repair filters, so the two are not compared here. M. gnavus and F. plautii appear in both. [src: discoveries, ibd_phage_targeting]
- Related context on portability: [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

## Possible Reconciliations

- **Hypothesis 1:** The NB05 score and the repair filters measure different properties, so a high score and a low repair pass count need not conflict. This is untested, because the mapping between the lists is not given.
- **Hypothesis 2:** The phage-availability gap for top scorers reflects missing database coverage, not true absence of phages. This is untested.
- **Hypothesis 3:** Weak cross-cohort replication, especially for E3, explains why Tier-A candidates should be treated as hypotheses whichever list they come from. This is untested.

## Resolving Work

- Data: the NB05 candidate list and the per-ecotype repair outputs. Method: map each candidate across both lists by species. Question: which NB05 targets pass or fail each repair filter, including M. gnavus and F. plautii?
- Data: external phage databases. Method: query them for H. hathewayi and F. plautii. Question: is the Pillar-4 GAP a coverage artifact or a real lack of phages?
- Data: additional independent cohorts. Method: repeat the E3 candidate analysis. Question: does E3 replicate beyond its current evidence?
- Data: NB05 scoring components. Method: rescore with phage availability included or excluded. Question: does the ranking of H. hathewayi (4.0) and M. gnavus (3.8) change?
- Data: experimental phage susceptibility assays. Method: test Tier-A candidates directly. Question: do cocktail drafts act on candidates that survive validation?
