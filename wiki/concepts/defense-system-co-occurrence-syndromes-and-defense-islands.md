---
type: "Concept"
description: "Whether anti-phage defense systems co-occur in species more than expected under a phylum-preserving null, including the R-M Type II × Gabija pairing; stops at mechanism."
sources: ["summaries/phage_defense_arsenal__REPORT.md"]
---
# Defense-system co-occurrence syndromes and defense islands

Defense systems in bacteria co-occur in species far more often than a phylum-preserving null predicts. In the one report behind this page, 27 of 28 tested pairs were significant, and R-M Type II × Gabija was the strongest. The evidence comes from a single pan-bacterial analysis ([[summaries/phage_defense_arsenal__REPORT]]), and its mechanistic reading is a hypothesis. [src: phage_defense_arsenal]

## Literature Context

The one candidate paper bears on this page only indirectly, but it does address the co-occurrence logic the page relies on. Using a co-occurrence analysis of VSP genes in >200,000 bacterial genomes, the authors built gene networks to infer the functions encoded in the Vibrio cholerae El Tor genomic islands VSP-1 and VSP-2 [PMID 35817890](https://pubmed.ncbi.nlm.nih.gov/35817890/). The network showed that dncV, a component of the anti-phage system CBASS (cyclic-oligonucleotide-based anti-phage signalling system), co-occurs with an uncharacterized gene. They renamed that gene avcD, for anti-viral cytidine deaminase [PMID 35817890](https://pubmed.ncbi.nlm.nih.gov/35817890/). They showed that AvcD is a deoxycytidylate deaminase. A non-coding RNA named AvcI inhibits its activity post-translationally. AvcID and its bacterial homologues protect bacterial populations against phage invasion by depleting free deoxycytidine nucleotides during infection, which decreases phage replication [PMID 35817890](https://pubmed.ncbi.nlm.nih.gov/35817890/). The abstract reports this as a defense mechanism. It does not test a phylum-preserving null or pairwise syndromes.

This paper is consistent with the corpus's broad premise that defense genes are non-randomly associated and that co-occurrence can point to function. It places a defense gene in a genomic island and finds the gene through co-occurrence with another defense system. That fits the defense-island framing the hub cites from Rocha and Bikard and from Tesson et al. The fit is conceptual. The paper does not test any of the pairs in the hub's table, and it does not use species-level counts.

The paper is also relevant to the hub's mechanistic hypothesis for R-M Type II × Gabija. The hub notes that Gabija is triggered by nucleotide-pool depletion, and it proposes layered defense. The candidate paper shows that depleting deoxynucleotides is a defense strategy in its own right [PMID 35817890](https://pubmed.ncbi.nlm.nih.gov/35817890/). That gives some plausibility to nucleotide-pool-based defenses, but it does not bear on the R-M Type II pairing itself. It does not mention Gabija or restriction-modification in its abstract. The corpus's findings are therefore novel relative to this candidate. The 27 of 28 significant pairs, the R-M Type II × Gabija pairing (OR = 24, z = 46), and the CRISPR-Cas × CBASS null result (z = 0.21) are neither confirmed nor contradicted by it. The layered-defense reading stays a hypothesis, and the phage-challenge experiments the report proposes would still be needed to test it. The CBASS link in the candidate also does not conflict with the CRISPR-Cas × CBASS null. The candidate describes co-occurrence of dncV with avcD, not with CRISPR-Cas.

## Background: defense islands

Rocha and Bikard proposed defense islands as the ecological unit of defense diversity. [src: phage_defense_arsenal] Tesson et al. reported that defense systems tend to co-cluster in prokaryotic genomes. [src: phage_defense_arsenal] The report reads its 27/28 significant pairs at pan-bacterial scale as direct support for this framework. [src: phage_defense_arsenal]

## Pairwise co-occurrence under a phylum-stratified null

Under a phylum-stratified column-permutation null (N = 1,000 permutations), 27 of 28 tested defense-system pairs showed significant positive co-occurrence at BH-FDR (Benjamini-Hochberg false discovery rate) q < 0.05. [src: phage_defense_arsenal]

| Pair | Observed | Null mean | z | OR | Claim |
|---|---|---|---|---|---|
| R-M Type II × Gabija | 2,429 | 1,555 | 46.1 | 24.0 | [src: phage_defense_arsenal] |
| BREX × DISARM | 4,968 | 4,629 | 31.1 | 8.2 | [src: phage_defense_arsenal] |
| BREX × Retron | 5,021 | 4,681 | 29.7 | 8.6 | [src: phage_defense_arsenal] |
| DISARM × Retron | 4,280 | 3,844 | 28.4 | 5.2 | [src: phage_defense_arsenal] |
| R-M Type I × DISARM | 4,970 | 4,673 | 27.5 | 8.4 | [src: phage_defense_arsenal] |
| R-M Type I × BREX | 5,963 | 5,732 | 26.9 | 8.7 | [src: phage_defense_arsenal] |
| R-M Type II × DISARM | 3,424 | 2,981 | 24.4 | 4.1 | [src: phage_defense_arsenal] |
| R-M Type II × BREX | 3,929 | 3,637 | 23.0 | 6.4 | [src: phage_defense_arsenal] |
| R-M Type I × R-M Type II | 3,948 | 3,665 | 22.5 | 7.6 | [src: phage_defense_arsenal] |

The report calls the BREX × DISARM syndrome (OR = 8.2) consistent with the defense-island pattern documented by Doron et al. (2018) and Tesson et al. (2022). It also calls it consistent with the Rocha and Bikard framework, which predicts co-clustering of defense systems on mobile genetic elements. [src: phage_defense_arsenal]

The one null result is CRISPR-Cas × CBASS (z = 0.21, p_emp = 0.98). These two systems have the largest prevalence gap (96 % vs 7 %), and CBASS is essentially independent of CRISPR-Cas presence. [src: phage_defense_arsenal]

## R-M Type II × Gabija

The report describes this as its strongest syndrome (OR = 24, z = 46) and, to its knowledge, a novel pan-bacterial finding at this scale. [src: phage_defense_arsenal] The two systems co-occur in 2,429 of 4,096 R-M Type II-carrying species (59 %), against an expected 1,555 (38 %). [src: phage_defense_arsenal]

This page stops at mechanism. The report notes that both systems act on double-stranded DNA (deoxyribonucleic acid). Type II R-M uses sequence-specific cleavage. Gabija uses a nuclease/helicase pair triggered by nucleotide-pool depletion. [src: phage_defense_arsenal] It hypothesizes that the pairing may reflect complementary layered defense against different phage life-cycle stages. [src: phage_defense_arsenal]

The report proposes mechanistic follow-up: identify species carrying only R-M Type II versus both systems, then run phage-challenge experiments in E. coli or B. subtilis to test whether adding Gabija gives a quantitative fitness advantage. [src: phage_defense_arsenal]

## Open Directions

- Run the proposed comparison of R-M Type II-only species against species with both systems, then phage-challenge experiments in E. coli or B. subtilis. This would test the layered-defense hypothesis.
- Check whether the co-occurring pairs sit physically near each other in genomes. Species-level co-occurrence does not show co-location, so this would link the syndromes to defense islands.
- Repeat the CRISPR-Cas × CBASS test at finer taxonomic levels. This would show whether the lack of association holds beyond phylum-level stratification.
