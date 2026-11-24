---
type: "Concept"
description: "How matrix decomposition yields cofitness gene groups, how thresholds, experiment counts, adjacency and missing-data or operon handling affect their validity; stops at conservation."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/discoveries.md", "summaries/fitness_modules__REPORT.md", "summaries/module_conservation__REPORT.md", "summaries/pitfalls.md"]
---
# Construction and validity of cofitness gene groups

This page covers how cofitness gene groups are built and checked. Robust ICA (independent component analysis, run 30-50 times with DBSCAN clustering) finds 17-52 stable modules per organism across 32 bacteria. [src: discoveries] The membership threshold matters most. [src: pitfalls] Experiment counts and component caps set practical limits. [src: discoveries, fitness_modules] The AMR (antimicrobial resistance) analysis handles operons and missing data only by approximation. [src: amr_cofitness_networks] The page stops before conservation. See [[entities/independent-component-analysis-fitness-modules]] and [[entities/cofitness-analysis]] for background.

## Building groups by matrix decomposition

The fitness ICA decomposition yielded 1,116 stable modules across 32 organisms, all with >=100 experiments. [src: fitness_modules] The work extends the transcriptomic ICA framework of Sastry et al. (2019), who showed that the *E. coli* transcriptome consists largely of independently regulated modules recoverable by ICA. [src: fitness_modules] Cofitness (within-module correlation) is the main validation metric. It builds on Price et al. (2018), who showed that mutant fitness data across thousands of conditions reveals gene function at scale. [src: fitness_modules]

## The membership threshold

Membership selection, not the ICA components, caused the early failure, and an absolute weight threshold fixed it. [src: discoveries, fitness_modules] The initial D'Agostino K-squared approach gave 100-280 genes per module with weak cofitness signal: 59% enriched and 1-17x correlation. [src: discoveries, fitness_modules] The pitfalls report explains why. ICA weights are intentionally heavy-tailed, so the normality test always rejects normality and falls back to a permissive z-threshold of 2.5. [src: pitfalls]

Switching to |Pearson r| ≥ 0.3 with the module profile and a maximum of 50 genes reduced modules to 5-50 genes. [src: discoveries, fitness_modules] Cofitness enrichment rose from 59% to 94.2%. Within-module |r| rose from 0.047 to 0.34, as a mean across 32 organisms. [src: discoveries] The pitfalls report calls this the single most impactful parameter in the pipeline. [src: pitfalls] Median module size was 7-50 genes, described as a biologically correct range. [src: fitness_modules]

The final modules show the following:
- 94.2% have significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05). [src: discoveries, fitness_modules]
- Within-module mean |r| is 0.34 against a background of 0.12, a 2.8x enrichment. [src: discoveries, fitness_modules]
- Genomic adjacency enrichment is 22.7x on average. The reports read this as modules capturing operon-like co-regulated groups. [src: discoveries, fitness_modules]

The threshold also limits downstream use. It decides which genes are "in" a module and could influence conservation composition. [src: module_conservation]

## Experiment counts and component caps

Ponti, with 104 experiments, still produced stable modules. [src: discoveries] The fitness_modules report says organisms with fewer than ~100 experiments produce weaker modules. It cites Caulo as its example. [src: fitness_modules]

Capping ICA components at 40% of experiments avoids FastICA convergence failures and extreme slowness. [src: discoveries] The cap may miss some modules in low-experiment organisms. [src: fitness_modules] Failed runs each reach max_iter, so the pitfalls report recommends n_components ≤ 40% of n_experiments. [src: pitfalls] For 150 experiments, that means at most 60 components. [src: pitfalls]

DBSCAN needs a numerical fix. Cosine distances defined as 1 - |cosine_similarity| can become slightly negative from floating-point error. DBSCAN with a precomputed metric rejects them. [src: pitfalls] The fix is to clip distances to [0, 1] before clustering. [src: pitfalls]

## Essential genes and annotation

No essential gene appears in any module. ICA modules capture only non-essential genes with measurable fitness variation, because essential genes have no fitness data. [src: module_conservation] See [[concepts/limits-of-transposon-based-essentiality-calls]].

Module annotation also depends on a threshold. Using min_annotated=3 with KEGG KOs (~1.2 genes per KO) enriched only 8% of modules. Almost no KEGG term has 3+ genes in a 5-50 gene module. [src: pitfalls] Lowering to 2 with false discovery rate (FDR) correction and adding PFam domains (814 terms with 2+ genes) and TIGRFam (88 terms) raised annotation from 8% to 80%. [src: pitfalls]

## Adjacency, operons and missing data in AMR networks

The AMR cofitness analysis handles operons and missing values with approximations. Its 5-ORF exclusion zone uses matrix row index as a proxy for genomic proximity, which may not reliably reflect chromosomal gene order. [src: amr_cofitness_networks] The annotation data already include begin, end and strand columns that could support coordinate-based exclusion. [src: amr_cofitness_networks] The heuristic excludes only 0.6% of pairs. Of 180,370 total cofitness partners, 179,375 are extra-operon. [src: amr_cofitness_networks]

Missing fitness values are set to zero in z-score space with np.nan_to_num. This approximates but does not equal pairwise-complete Pearson correlation. [src: amr_cofitness_networks] The report considers this unlikely to affect conclusions, because Fitness Browser matrices are relatively dense. [src: amr_cofitness_networks]

The cutoff also changes network size. Mean support-network size is 233 genes at |r|>0.3, 110 at |r|>0.4 and 71 at |r|>0.5. [src: amr_cofitness_networks] At |r|>0.3 the networks include many weak associations, so confirmation at |r|>0.4 is needed. [src: amr_cofitness_networks] See [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]].

## Open Directions

- Replace the row-index operon exclusion with a begin/end/strand-based one. Then test whether the 0.6% excluded fraction and the AMR partner counts change.
- Recompute AMR cofitness with pairwise-complete Pearson correlation on a few organisms. This would check the claim that zero-filling does not affect conclusions.
- Test the 40% component cap on organisms with fewer than ~100 experiments, for example by comparing module recovery at several ratios. This would show how many modules the cap misses.
- Repeat the threshold comparison (|r| ≥ 0.3 against other cutoffs) and record how module membership shifts. This would show how sensitive downstream conservation results are to it.
