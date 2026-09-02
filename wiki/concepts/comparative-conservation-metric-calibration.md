---
type: "Concept"
description: "How conservation metrics affect prioritization of unknown bacterial genes"
sources: ["summaries/functional_dark_matter__REPORT.md"]
---
# Calibrating Conservation Metrics for Unknown Bacterial Genes

Conservation metrics are not interchangeable: the apparent priority of an unknown bacterial gene depends on how ortholog breadth is defined, how species and taxonomic coverage are counted, and whether the metric distinguishes broad conservation from annotation or database-coverage artifacts. [src: functional_dark_matter]

The [[summaries/functional_dark_matter__REPORT]] provides a direct calibration case by comparing an eggNOG-based ortholog-group breadth ranking with a species-count variant and a larger GTDB r214 pangenome analysis. [src: functional_dark_matter]

## Why Metric Choice Matters

The initial analysis mapped 30,756 dark-gene clusters across 27,690 species. [src: functional_dark_matter] The eggNOG ortholog-group breadth classification assigned 30,721 of 30,756 clusters (99.9%) to universal breadth, making that category poorly discriminative for ranking unknown genes. [src: functional_dark_matter] Species counts in this analysis ranged from 1 to 33, with median 1 and mean 2.2. [src: functional_dark_matter]

Replacing the original breadth score with a species-count scoring variant produced Spearman ρ = 0.982 with the original ranking, but top-50 overlap was 62% and top-100 overlap was 58%. [src: functional_dark_matter] This **refines** the interpretation of rank correlation: a high global correlation did not imply stable membership among the highest-priority candidates. [src: functional_dark_matter]

## Expanded GTDB Calibration

The full GTDB r214 pangenome analysis queried 93.5M gene-cluster annotations and propagated ortholog-group identifiers, expanding conservation coverage from 32,791 (57.5%) to 37,997 (66.6%) dark genes and recovering 5,206 additional dark genes. [src: functional_dark_matter] The expanded analysis changed the species-count distribution to a range of 1 to 27,482, with median 135 and mean 2,128, showing that the expanded reference space substantially altered the scale of observed conservation. [src: functional_dark_matter]

Among 11,774 root ortholog groups, 55.9% were kingdom-level, 11.0% class-level, 10.5% family-level, 6.9% genus-level, 6.5% mobile, 4.8% phylum-level, 3.9% order-level, and 0.5% species-level. [src: functional_dark_matter] These taxonomic tiers provide a more graduated representation of conservation than the initial near-universal eggNOG classification. [src: functional_dark_matter]

The expanded result **supports** using broader and more explicitly taxonomic reference data when the goal is to separate widely conserved unknown genes from narrowly distributed ones, but it does not establish that broad conservation alone predicts gene function. [src: functional_dark_matter] The report classified 6.0% of dark genes as strong testable hypotheses, 52.5% as weak leads, and 41.5% as true knowledge gaps under a conservation-by-ignorance scheme. [src: functional_dark_matter]

## Conservation and Experimental Prioritization

The conservation-weighted covering set selected 42 organisms covering 95.6% of importance-weighted priority across 28,584 high-priority dark genes. [src: functional_dark_matter] A separate darkness-spectrum analysis selected 42 organisms from 28 genera to cover 95% of scored priority, with 32 organisms sufficient for 80% coverage. [src: functional_dark_matter] These results **support** using conservation metrics not only to rank individual genes but also to design organism panels that maximize coverage of experimentally actionable unknowns. [src: functional_dark_matter]

Conservation was one of six axes in the prioritization score, alongside fitness importance, inference quality, pangenome distribution, biogeographic signal, and experimental tractability. [src: functional_dark_matter] Overall rank correlations remained ρ > 0.93 across six alternative configurations, but only 64% of the original fitness-active top 50 remained under conservation-dominant or drop-tractability settings. [src: functional_dark_matter] Essential-gene top-50 retention was 36% when tractability was dropped and 48% when neighbor context was dropped. [src: functional_dark_matter] These sensitivity results **qualify** conservation-weighted ranking as a useful prioritization input rather than a uniquely correct ordering. [src: functional_dark_matter]

## Tensions

The initial eggNOG metric suggested near-universal breadth for 99.9% of clusters, whereas the GTDB r214 analysis resolved root ortholog groups across kingdom, phylum, class, order, family, genus, species, and mobile categories. [src: functional_dark_matter] This **tension** indicates that apparent conservation can depend strongly on reference-database composition, ortholog-group propagation, and the taxonomic level used for scoring. [src: functional_dark_matter]

The species-count variant was highly correlated with the original ranking at the global level, with Spearman ρ = 0.982, yet its top-50 and top-100 overlaps were only 62% and 58%, respectively. [src: functional_dark_matter] Thus, rank correlation and decision stability answer different questions and should be reported together when conservation metrics guide experimental selection. [src: functional_dark_matter]

## Relation to Other Concepts

This concept **refines** [[concepts/pangenome-integration]] by focusing on how pangenome reference breadth and ortholog-group propagation change conservation estimates rather than on pangenome integration generally. [src: functional_dark_matter]

It **supports** [[concepts/comparative-conservation-metric-calibration]] as a framework for testing whether conservation scores are discriminative, stable at decision thresholds, and appropriate for experimental design. [src: functional_dark_matter]

It also connects to [[concepts/fitness-importance-and-pangenome-conservation]] because conservation was combined with fitness importance in candidate prioritization, while the sensitivity analysis showed that changing conservation emphasis altered high-priority membership. [src: functional_dark_matter]

## Open Directions

- Recalculate the same dark-gene rankings with matched reference sets and identical ortholog-group definitions, then test whether the 62% top-50 and 58% top-100 overlap values improve when database breadth is held constant. [src: functional_dark_matter]
- Compare kingdom-, phylum-, class-, family-, genus-, and species-level conservation scores against independent fitness measurements to test which taxonomic resolution best predicts experimentally measurable phenotypes. [src: functional_dark_matter]
- Use bootstrap resampling of species and phyla in the 93.5M gene-cluster reference to quantify confidence intervals for conservation ranks and identify candidates whose priority is database-sensitive. [src: functional_dark_matter]
- Re-run the 42-organism covering-set optimization under alternative conservation metrics and compare coverage of the 28,584 high-priority dark genes, asking whether the selected experimental panel is robust to metric choice. [src: functional_dark_matter]
- Test whether conservation-weighted candidates outperform fitness-only candidates in CRISPRi or RB-TnSeq follow-up, separating broad conservation from experimentally validated functional importance. [src: functional_dark_matter]
