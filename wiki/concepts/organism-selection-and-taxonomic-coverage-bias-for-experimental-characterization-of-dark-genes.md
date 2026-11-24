---
type: "Concept"
description: "How set-cover optimization chooses organisms for experiments, how the Proteobacteria-heavy Fitness Browser limits conclusions, and how adding tractable non-Fitness-Browser organisms changes coverage."
sources: ["summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md"]
---
# Organism selection and taxonomic coverage bias for experimental characterization of dark genes

This page covers how set-cover optimization picks organisms for experiments on dark genes, how the Proteobacteria-heavy Fitness Browser (FB) limits the conclusions, and how adding tractable non-FB organisms changes coverage. The evidence comes from the functional dark matter analysis ([[summaries/functional_dark_matter__REPORT]]) and its digest in discoveries ([[summaries/discoveries]]). The FB-only result is clearly biased toward Gammaproteobacteria, and the extended set widens phylum coverage. [src: functional_dark_matter] The FB has 37 of 48 organisms in Pseudomonadota and no Bacillota, Actinomycetota or Campylobacterota. Adding 25 literature-curated organisms raises phylum coverage from 4 to 6, with caveats on how coverage was estimated. [src: functional_dark_matter]

## How set-cover selection works

The report ranked organism-condition pairs by the number of top-500 dark-gene candidates each would address, then applied greedy set-cover optimization (see [[entities/greedy-weighted-set-cover-organism-selection]]). [src: functional_dark_matter] Ten RB-TnSeq (random barcode transposon sequencing) experiments cover 45% of the top 500 dark genes. [src: functional_dark_matter] The first roadmap entry is [[entities/shewanella-oneidensis-mr-1]] under stress, with 57 dark genes addressed (10.7% of the top 500). [src: functional_dark_matter] Three MR-1 experiments (stress, nitrogen, carbon) would cover 111 top-500 candidates (20.8%), which makes MR-1 the highest-value single organism. [src: functional_dark_matter, discoveries] The evidence-weighted roadmap achieves 45% coverage of the top 300 candidates with 4 experiments. [src: functional_dark_matter]

Across organisms, greedy weighted set-cover over 16,488 scored dark genes picks 42 organisms from 28 genera covering 95% of total priority value. [src: functional_dark_matter] MR-1 ranks first with 587 genes, and 32 organisms suffice for 80% coverage. [src: functional_dark_matter] The evidence-weighted roadmap also ranks MR-1 first, with 61 candidates (47 fitness-active, 14 essential), 83 synteny-validated pairs and 31 cofit-validated pairs. [src: functional_dark_matter] In the discoveries digest, MR-1 contributes 25/100 top fitness-active candidates. [src: discoveries] It also has 587 scored dark genes. [src: discoveries] The report attributes this to 121 conditions of coverage, a large dark gene complement and 142 genes with |fit| >= 4. [src: discoveries]

## Two routes give different top organisms

Route A and Route B favour different organisms but largely overlap. This is the report's own comparison. [src: functional_dark_matter]

- Route A is evidence-weighted. It scores each dark gene on 6 dimensions using the 48 FB organisms. [src: functional_dark_matter] It optimizes Σ(composite_score) × tractability × phylo_diversity. [src: functional_dark_matter] It selects 42 organisms from 28 genera covering 95% of composite priority. [src: functional_dark_matter]
- Route B is conservation-weighted. It queries the full 27,690-species GTDB r214 pangenome and ranks by conservation × ignorance. [src: functional_dark_matter] It optimizes Σ(importance) × tractability × phylo_bonus, where phylo_bonus penalizes genus-redundant selections. [src: functional_dark_matter] It selects 42 organisms from 28 genera covering 95.6% of importance-weighted priority. [src: functional_dark_matter]
- The routes share 39 organisms. Route A alone selects Dda3937, Ddia6719 and Miya. Route B alone selects Kang, Methanococcus_JJ and Methanococcus_S2. [src: functional_dark_matter, discoveries] The report calls the routes complementary: Route A gives mechanistic insights for genes with hypotheses, and Route B discovers functions for broadly conserved true knowledge gaps. [src: functional_dark_matter]

Route A puts MR-1 first for deep condition evidence. Route B puts [[entities/sinorhizobium-meliloti]] first for the most kingdom-level gaps. [src: discoveries] In Route B, S. meliloti has 1,630 genes and 195 kingdom-level gaps. [src: functional_dark_matter, discoveries] P. putida follows with 1,043 genes and 172 kingdom gaps. [src: functional_dark_matter] MR-1 has 805 genes and 105 kingdom gaps. [src: functional_dark_matter] [[entities/bacteroides-thetaiotaomicron]] has the highest raw count of kingdom gaps (267, with 1,382 genes), but a tractability of 0.3 deprioritizes it. [src: functional_dark_matter] The first 10 organisms cover 31% of priority. [src: functional_dark_matter]

The report recommends Route A for targeted experiments where convergent evidence gives a testable hypothesis and predicted conditions. [src: functional_dark_matter] It recommends Route B for discovery experiments on broadly conserved genes with the least functional knowledge. [src: functional_dark_matter] Route A's strength is condition-specific protocols. Route B's strength is finding broadly conserved gaps that evidence-based scoring cannot see. [src: functional_dark_matter] The practical split is targeted RB-TnSeq under predicted conditions for Route A and broad phenotypic screens for Route B. [src: functional_dark_matter] The digest says the two routes allow both kinds of work from largely the same organism set. [src: discoveries]

## Proteobacteria-heavy Fitness Browser coverage

The [[entities/fitness-browser]] is heavily skewed toward Gammaproteobacteria, with 21 of 48 organisms and 78% of top-500 dark genes. [src: functional_dark_matter] Both dark-gene covering sets draw only from the 48 FB organisms, of which 37/48 (77%) are Pseudomonadota. Bacteroidota (4), Cyanobacteriota (1) and Halobacteriota (2) are the only other phyla represented. [src: functional_dark_matter] Bacillota (Firmicutes), Actinomycetota (Actinobacteria) and Campylobacterota have zero FB representation. [src: functional_dark_matter] As a result, kingdom-level OGs (ortholog groups), which make up 55.9% of dark gene OGs and occur across multiple phyla, cannot be tested in their non-Proteobacterial hosts using FB organisms alone. [src: functional_dark_matter]

The report grades gaps by clade, as the table shows. [src: functional_dark_matter]

| Clade | FB organisms | Top-500 genes | Gap |
|---|---|---|---|
| Gammaproteobacteria | 21 | 417 | Saturated |
| Betaproteobacteria | 8 | 10 | Moderate |
| Alphaproteobacteria | 5 | 71 | Low |
| Deltaproteobacteria | 5 | 17 | Low |
| Bacteroidetes | 5 | 12 | Low |
| Firmicutes | 1 | 5 | Critical |
| Cyanobacteria | 1 | 2 | Moderate |
| Archaea | 2 | 0 | Severe |
| Actinobacteria | 0 | not given | Critical |
| Epsilonproteobacteria | 0 | not given | High |

The report proposes that organisms from missing phyla would allow cross-phylum concordance tests of widespread dark domain families. [src: functional_dark_matter] It ranks candidate new RB-TnSeq organisms by phylogenetic gap filled, laboratory tractability, overlap with widespread dark gene families, and environmental or biomedical relevance. [src: functional_dark_matter]

## Extending the candidate pool beyond the Fitness Browser

Adding non-FB organisms increases phylum breadth and early coverage. The report curated an extended list of 73 organisms: the 48 FB organisms plus 25 literature-curated organisms with published TnSeq (transposon sequencing) or CRISPRi (CRISPR interference) resources. [src: functional_dark_matter] The 25 added organisms fall into four groups. [src: functional_dark_matter]

- Bacillota (6): B. subtilis 168, S. aureus USA300, S. pneumoniae TIGR4, C. difficile R20291, E. faecium and L. monocytogenes EGD-e, with TnSeq + CRISPRi resources. [src: functional_dark_matter]
- Actinomycetota (2): M. tuberculosis H37Rv and C. glutamicum ATCC 13032, with TnSeq + CRISPRi resources. [src: functional_dark_matter]
- Campylobacterota (2): C. jejuni NCTC 11168 and H. pylori 26695, with TnSeq resources. [src: functional_dark_matter]
- Pseudomonadota (15): including P. aeruginosa PAO1, Salmonella 14028s, V. cholerae N16961, A. baumannii 17978 and 11 others, with TnSeq/CRISPRi resources. [src: functional_dark_matter]

A Spark query (NB11c) mapped genus-level OG membership for 25 non-FB organisms: 24 genera and 53,970 genus-OG pairs, in 2.9 min. [src: functional_dark_matter] Using this, the extended covering set incorporates the 25 non-FB organisms and expands phylum coverage from 4 to 6. [src: functional_dark_matter]

- With all 73 candidates, the conservation-weighted set has 50 organisms covering 98.7% of OGs across 6 phyla. FB-only selection has 41 organisms across 4 phyla, and the digest reports it as covering 100%. [src: functional_dark_matter, discoveries]
- Of the 50 selected organisms, 16 are non-FB, led by [[entities/pseudomonas-aeruginosa-pao1]] (3,713 OGs, tractability 0.8), with C. jejuni selected at #48. [src: functional_dark_matter, discoveries]
- [[entities/mycobacterium-tuberculosis]] ranks #6, the first Actinomycetota. [src: discoveries]
- At N=5 organisms, coverage reaches 57.7%, against 38.1% for FB-only, a reported +19.6%. [src: functional_dark_matter]

[[entities/bacillus-subtilis-168]] and [[entities/staphylococcus-aureus]] are not selected. Their kingdom-level OGs are already covered by selected Pseudomonadota, so the algorithm skips them despite their value for studying genes in native Gram-positive contexts. [src: discoveries, functional_dark_matter]

The report proposes that including these organisms in Route B would enable experimental characterization of kingdom-level dark gene OGs in native Gram-positive, Actinobacterial and Campylobacterial genomic contexts. [src: functional_dark_matter] This is a proposal. It requires a Spark query mapping each non-FB genome to dark gene root_ogs via the pangenome, extending the NB11b pipeline. [src: functional_dark_matter]

### Limits on the extended set

- Non-FB OG coverage is estimated at genus level (any species in the genus has the OG), which overestimates individual-organism coverage. [src: functional_dark_matter]
- Non-FB organisms lack FB condition profiling, so their dark genes can be assigned only broad phenotypic screens, not condition-specific experiments. [src: functional_dark_matter]

## Open Directions

- Rerun the extended covering set with an objective that rewards cross-phylum concordance, so that Bacillota such as B. subtilis are selected. This would test whether the unique-OG criterion undervalues Gram-positive organisms.
- Redo the non-FB OG mapping at species or strain level rather than genus level. This would show how much the 98.7% coverage is overestimated.
- Check the tractability weights, such as 0.3 for B. thetaiotaomicron, by sensitivity analysis. This would show how far the rankings depend on those values.
- Test the roadmap's ~100 universal dark gene families in B. subtilis and S. coelicolor RB-TnSeq libraries. This would show whether the cross-phylum predictions hold.
- Compare Route A and Route B picks against later reannotation, as in [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]]. This would show whether Route B finds genes that are truly unannotatable.
