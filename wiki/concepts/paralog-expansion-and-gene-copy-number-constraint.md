---
type: "Concept"
description: "Whether housekeeping categories stay near single-copy while adaptive categories expand into paralogs, how core/accessory status modulates this, and whether the Alm 2006 histidine kinase expansion result reproduces at other scales."
sources: ["summaries/gene_copy_number_variation__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md"]
---
# Paralog expansion and gene copy-number constraint

Adaptive COG (clusters of orthologous groups) categories show higher multi-copy rates than housekeeping categories in all 24 bacterial species tested. [src: gene_copy_number_variation] This pattern is concentrated in accessory clusters, not core ones. [src: gene_copy_number_variation] The Alm 2006 histidine kinase expansion correlation (r ≈ 0.74) did not reproduce at the scale of 18,989 species representatives, with r=0.10–0.29. [src: gene_function_ecological_agora] The qualitative recent-skew of two-component-system (TCS) histidine kinases (HK) does hold at architectural resolution, with consumer-side concordance r = 0.67. [src: gene_function_ecological_agora] The copy-number evidence comes from one report ([[summaries/gene_copy_number_variation__REPORT]]), and the Alm test comes from another ([[summaries/gene_function_ecological_agora__REPORT]]).

## Literature Context

The one candidate paper is about human paralogs, not bacterial copy number, so it bears on this page only indirectly. It reports a CRISPR screen of 678 human paralog pairs to identify pairs with negative genetic interactions (nGIs) or compensatory paralogs. The authors combined the screen with four other studies into two resources, the 2168-pair Union dataset and the 4859-pair Ito dataset [PMID 42953730](https://pubmed.ncbi.nlm.nih.gov/42953730/). They classified paralogs as core (broadly compensating), conditional or non-interacting. Core nGI pairs showed prenatal co-expression, depletion of disease genes and enrichment for upregulation after paralog loss in cancer. The authors say these signals were often moderate, and they conclude that paralogous compensation is moderately prevalent in vivo in humans [PMID 42953730](https://pubmed.ncbi.nlm.nih.gov/42953730/).

The paper also reports evolutionary results. Similar fractions (∼2%) of core compensators were found among ancient and young paralogs. Ancient pairs retain overlaps likely under pleiotropic and dosage constraints [PMID 42953730](https://pubmed.ncbi.nlm.nih.gov/42953730/). Only the abstract was available, and the work is in humans.

The corpus findings concern bacteria and a different question, so they cannot be called consistent or inconsistent with this paper in any direct sense. The corpus reports that adaptive COG categories L, V, M and K have higher multi-copy rates than housekeeping categories F and H in 24 of 24 species, and that this effect is concentrated in accessory clusters. Core clusters are near-uniformly single-copy whatever their category. The human paper does not test this. It does mention dosage constraint on ancient pairs, which loosely echoes the corpus's dosage-balance reading of single-copy housekeeping genes. That echo is only a thematic parallel, because the human data concern functional compensation between paralog pairs, not copy-number rates across pangenome clusters.

The corpus's Alm 2006 histidine kinase tests (r = 0.10–0.29 at 18,989 species representatives, against Alm's r ≈ 0.74, and the absent UniRef50 producer signal) have no counterpart in the candidate. On these points the corpus is novel relative to the supplied evidence. The abstract supports only the general view that paralog retention is shaped by several forces, and it gives no evidence for or against the bacterial two-component expansion results. Searching for bacterial paralog-expansion literature would fill this gap.

## Housekeeping versus adaptive categories

Adaptive COG categories L, V, M and K have higher cluster-carrier-weighted multi-copy rates than housekeeping categories F and H in 24 of 24 species. The species span 5 phyla with 50–249 genomes each. The median species-level ratio is 8.14× (paired Wilcoxon signed-rank, p = 5.96 × 10⁻⁸). [src: gene_copy_number_variation] All 8 pairwise F/H × L/V/M/K comparisons are significant at BH-FDR (Benjamini-Hochberg false discovery rate) < 0.01. The smallest adjusted p is 4.8 × 10⁻⁷, for F–L and H–L. [src: gene_copy_number_variation]

Species-level medians are L 1.12%, V 0.11%, M 0.11% and K 0.12%. Housekeeping medians are F 0.062% and H 0.041%. [src: gene_copy_number_variation] The report reads the housekeeping rates as fixation, since 0.06% and 0.04% sit three orders of magnitude below the ~5% pseudogene or rare-variant background expected under neutral drift. [src: gene_copy_number_variation] It describes adaptive COGs, especially L at 1.12%, as showing 20–30× the housekeeping rate, and considers its hypothesis H1 strongly supported on all three sub-claims. [src: gene_copy_number_variation] It reports housekeeping clusters as near-uniformly single-copy per genome, consistent with the dosage-balance hypothesis and with earlier microbial reports. [src: gene_copy_number_variation] The direction was unanimous across 5 phyla and 24 species. [src: gene_copy_number_variation]

Ratios by phylum (mean housekeeping % → mean adaptive %):

| Phylum | Species | Housekeeping % | Adaptive % | Ratio |
|---|---|---|---|---|
| [[entities/pseudomonadota|Pseudomonadota]] | 5 | 0.034 | 0.528 | 15.4× [src: gene_copy_number_variation] |
| Bacillota | 5 | 0.061 | 0.570 | 9.4× [src: gene_copy_number_variation] |
| Actinomycetota | 5 | 0.078 | 0.705 | 9.0× [src: gene_copy_number_variation] |
| Bacteroidota | 5 | 0.172 | 0.871 | 5.1× [src: gene_copy_number_variation] |
| Campylobacterota | 4 | 0.077 | 0.309 | 4.0× [src: gene_copy_number_variation] |

The effect varies about 4-fold across phyla but keeps its direction. [src: gene_copy_number_variation] The report links the variation to accessory-genome dynamics. Pseudomonadota has the largest and most mobile accessory genomes, and Campylobacterota has the smallest and most streamlined. [src: gene_copy_number_variation] This is the report's interpretation, not a separate test.

## Core versus accessory status

The class effect is mostly a core/accessory effect. Core clusters are copy-number-constrained whatever their category. The adaptive-core median is 0.06% and the housekeeping-core median is 0.03%, only 2× apart (p = 4.9 × 10⁻⁴). [src: gene_copy_number_variation] The 8× species-level effect collapses to 2× among fixation-level clusters. [src: gene_copy_number_variation] Within accessory clusters the effect returns: adaptive is 1.55% and housekeeping is 0.29%, 5× higher (p = 3.3 × 10⁻⁶). [src: gene_copy_number_variation]

Adaptive accessory clusters (median 1.55%) are 25× above adaptive core clusters (0.06%; p = 5.96 × 10⁻⁸). Housekeeping accessory clusters (0.29%) are 10× above housekeeping core (0.03%; p = 1.2 × 10⁻⁴). [src: gene_copy_number_variation] The report also states the interaction as 25× against 5×, but its own numbers give 10× for housekeeping. I report both as written. [src: gene_copy_number_variation] All four one-sided Wilcoxon tests in the 2×2 class × core-status analysis were significant. [src: gene_copy_number_variation]

The report concludes that paralog expansion happens in accessory clusters, preferentially in L, V, M and K. [src: gene_copy_number_variation] It also concludes that core clusters are near-uniformly single-copy across categories (median rates 0.03–0.06%). [src: gene_copy_number_variation] It reads the class effect as being about which clusters expand into paralogy, not which genes tolerate it at fixation. [src: gene_copy_number_variation] It sees this as consistent with dosage-driven amplification of environmentally responsive genes. [src: gene_copy_number_variation] It advises stratifying by is_core before inferring functional constraint. [src: gene_copy_number_variation] See also [[entities/cog-category-l-replication-recombination-and-repair]] and [[concepts/mechanisms-and-confounders-of-copy-number-variation-in-pangenomes]].

## Classifying translation and energy categories

Category J (translation) behaves as mixed, not housekeeping. A pilot found J at 2.07% multi-copy, 5th of 21 categories, driven by ribosomal protein paralogs, tRNA duplications and rRNA operon multiplicity. [src: gene_copy_number_variation] J was moved to mixed alongside C (energy production), which has the same problem through cytochrome paralogs. The report calls this essential to a tight test. [src: gene_copy_number_variation] Housekeeping = {F, H} is therefore much stricter than the textbook informational-versus-operational divide. [src: gene_copy_number_variation]

## Scope limits

The partition is coarse. Housekeeping covers ~5% of species-level rows and adaptive ~15%. [src: gene_copy_number_variation] About 80% of clusters fall into "other" and are excluded from the primary test, so extrapolating to all bacterial genes is not automatic. [src: gene_copy_number_variation] The report claims the first pangenome-scale systematic test across bacterial phyla. It also claims the first demonstration that the effect concentrates in accessory clusters. [src: gene_copy_number_variation] Earlier work tested related-bacterium pairs or single organisms. [src: gene_copy_number_variation] See also [[concepts/sampling-scope-and-generalizability-of-pangenome-wide-tests]].

## Alm 2006 histidine kinase expansion

The Alm 2006 result did not reproduce at larger scale. The P4-D3 test joined per-genome histidine protein kinase (HPK) counts, from PF00512 hits, to M22 recent lineage-specific-expansion (LSE) fractions across 18,989 species representatives. [src: gene_function_ecological_agora] Correlations were significant but modest, r = 0.10–0.29, against Alm's r ≈ 0.74 in 207 genomes. The verdict was "NOT REPRODUCED". [src: gene_function_ecological_agora] The report says the point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora] It names three mechanisms: substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity. [src: gene_function_ecological_agora]

| Comparison | Pearson r | Spearman r |
|---|---|---|
| HPK count vs recent TCS (two-component system) gains, genus rank | 0.288 [src: gene_function_ecological_agora] | 0.333 [src: gene_function_ecological_agora] |
| HPK count vs recent-LSE fraction per gene cluster | 0.157 [src: gene_function_ecological_agora] | 0.222 [src: gene_function_ecological_agora] |
| HPK count vs recent-LSE per TCS HK (histidine kinase) KO (KEGG ortholog) | 0.100 [src: gene_function_ecological_agora] | 0.152 [src: gene_function_ecological_agora] |
| Alm-style HPK fraction vs recent-LSE fraction | 0.105 [src: gene_function_ecological_agora] | 0.106 [src: gene_function_ecological_agora] |

The report offers two explanations. The first is dilution. Alm used 207 mostly cultivated, well-annotated genomes. The new set spans GTDB, including DPANN, CPR (candidate phyla radiation) and weakly annotated lineages with sparse HPK detection. [src: gene_function_ecological_agora] See [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]]. The second is a difference in metric. M22 uses Sankoff-parsimony recent-rank gain attribution, which misses expansions within a single recent species. It measures a phenomenon that overlaps with, but differs from, Alm's per-genome paralog counts. [src: gene_function_ecological_agora] "Recent" in M22 means leaf-adjacent gains, which capture within-genus diversification. Alm counted expansion at any depth, so the definitions diverge for older expansions. [src: gene_function_ecological_agora]

### What the report carries over from Alm 2006

The report concludes that its lineage is methodological generalization of Alm, not point-estimate reproduction. [src: gene_function_ecological_agora] Methodology generalization holds, with NB17 architectural concordance r = 0.67, while point-estimate reproduction does not. [src: gene_function_ecological_agora] The qualitative TCS HK recent-skew generalizes at architectural resolution. [src: gene_function_ecological_agora] The report itself still lists TCS architectural concordance as mixed. [src: gene_function_ecological_agora]

The NB17 architectural backtest found the canonical PF00512 + PF02518 HK architecture concentrated at recent ranks. [src: gene_function_ecological_agora] That architecture (HisKA + HATPase_c) has 25,462 gain events. [src: gene_function_ecological_agora] The report gives its profile as 44.7% recent and 4.5% ancient, consistent with Alm 2006's lineage-specific-expansion finding. [src: gene_function_ecological_agora] The Response_reg + Trans_reg_C architecture PF00072_PF00486 has 76,212 gain events. [src: gene_function_ecological_agora] NB17 framed the consumer concordance as the analog of Denise 2019's claim that modular systems exchange more. [src: gene_function_ecological_agora]

The concordance is asymmetric. Phase 3 closed at gate verdict PASS_MIXED, with consumer r=0.67 (confirmatory) and producer r=0.09 (exploratory). [src: gene_function_ecological_agora] At family rank the consumer correlation was r = 0.673, above the 0.6 threshold. [src: gene_function_ecological_agora] The producer correlation was r = 0.093, below it. [src: gene_function_ecological_agora] The report attributes the producer loss to paralog count being a per-KO quantity that does not map cleanly onto per-architecture aggregation. [src: gene_function_ecological_agora] It says the consumer signal survives because cross-clade dispersion is a property of where an architecture lives in the tree. [src: gene_function_ecological_agora]

### Phase 1A: no signal at UniRef50

At UniRef50 resolution, Phase 1A did not reproduce Alm 2006 TCS HK paralog expansion. The report deferred reproduction to Phases 2 and 3 under its v2 plan. [src: gene_function_ecological_agora] TCS HK UniRef50 clusters have mean producer z ≈ −0.2 across all ranks, with only 4–11% above zero. [src: gene_function_ecological_agora]

| Rank | TCS UniRefs scored | Positive z | Above 2σ | Mean producer z |
|---|---|---|---|---|
| genus | 73 [src: gene_function_ecological_agora] | 8 (11%) [src: gene_function_ecological_agora] | 2 [src: gene_function_ecological_agora] | −0.10 [src: gene_function_ecological_agora] |
| family | 124 [src: gene_function_ecological_agora] | 8 (6%) [src: gene_function_ecological_agora] | 2 [src: gene_function_ecological_agora] | −0.16 [src: gene_function_ecological_agora] |
| order | 157 [src: gene_function_ecological_agora] | 7 (4%) [src: gene_function_ecological_agora] | 3 [src: gene_function_ecological_agora] | −0.19 [src: gene_function_ecological_agora] |
| class | 174 [src: gene_function_ecological_agora] | 9 (5%) [src: gene_function_ecological_agora] | 2 [src: gene_function_ecological_agora] | −0.23 [src: gene_function_ecological_agora] |
| phylum | 186 [src: gene_function_ecological_agora] | 9 (5%) [src: gene_function_ecological_agora] | 2 [src: gene_function_ecological_agora] | −0.23 [src: gene_function_ecological_agora] |

Low power does not explain this. A one-sided t-test at α=0.05 had minimum detectable d at 80% power of 0.29 at genus (n = 73), 0.23 at family (n = 124), 0.20 at order (n = 157), 0.19 at class (n = 174) and 0.18 at phylum (n = 186). [src: gene_function_ecological_agora] Power for d=0.3 ranged from 0.81 at genus to 0.99 at class and phylum, and power for d=0.5 was 0.99 at genus and 1.00 at the other ranks. [src: gene_function_ecological_agora] The report concludes that the UniRef50 signal is genuinely absent and slightly negative. [src: gene_function_ecological_agora]

The report first read this as a negative result at sequence-cluster resolution, not a methodology failure. It argued that Alm measured distinct HK genes per genome at HK-family level, and that each UniRef50 typically matches a single HK protein variant and cannot aggregate to the family. [src: gene_function_ecological_agora] It said the result rules out the idea that any sequence-cluster-level method would reproduce Alm. [src: gene_function_ecological_agora] It said the pilot validates the v2 substrate hierarchy, with reproduction pre-registered for Phase 2 KO aggregation (KEGG ko02020) and Phase 3 Pfam multidomain architecture census. [src: gene_function_ecological_agora]

### Tension: what resolution Alm 2006 used

A later close reading of Alm 2006 contradicts the family-resolution argument above. It found that Alm worked at single-domain level (IPR005467 / COG4582), comparable to UniRef50 and not family aggregation. [src: gene_function_ecological_agora] It also found that Alm used phylogenetic-tree-aware reconciliation, not parent-rank dispersion. [src: gene_function_ecological_agora] Alm reported r = 0.74 between HPK count and recent-LSE fraction and never named producer/consumer or four-quadrant categories. [src: gene_function_ecological_agora] The four-quadrant framework is the project's own construction. [src: gene_function_ecological_agora] The project had framed its Open/Broker/Sink/Closed Innovator framework as a generalization of an Alm producer/consumer asymmetry. [src: gene_function_ecological_agora] The report says its claim that Phase 2 KO aggregation would recover Alm-style signal rested on a misreading. [src: gene_function_ecological_agora] Milestone M14 reframed the project as "Alm-2006-inspired" rather than generalizing the paper. [src: gene_function_ecological_agora] The report does not reconcile the earlier family-level explanation with the close reading.

## Open Directions

- Rerun the HPK correlation on a subset of well-annotated cultivated genomes of about 207. This would test whether annotation density and taxonomic breadth explain the drop from r ≈ 0.74.
- Count per-genome HPK paralogs directly, as Alm did, and compare with M22 gains. This would separate the metric difference from the scale difference.
- Apply a tree-aware reconciliation such as Sankoff parsimony to the UniRef50 and architecture data. This would test whether the absent UniRef50 producer signal reflects the metric rather than the substrate.
- Extend the core/accessory stratification to the "other" 80% of clusters and to categories J and C. This would show whether near-single-copy core and expanding accessory hold beyond the F, H, L, V, M, K partition.
- Test whether phylum-level ratios (4.0× to 15.4×) track measured accessory-genome size across more species per phylum. The report only interprets this link.
