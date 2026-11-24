---
type: "Concept"
description: "How n=3 per group caps pairwise PERMANOVA and rank-test significance, how pooled and factorial designs recover power, and how replicate variability, low diversity and shallow depth limit ITS amplicon inference."
sources: ["summaries/lignin_community_enrichment__REPORT.md"]
---
# Small-sample limits in community amplicon statistics

This page covers small-sample limits in community amplicon statistics. In the lignin-enrichment study, n=3 per group sets a permutation floor on pairwise tests. [src: lignin_community_enrichment] Pooled and factorial designs recover significance. [src: lignin_community_enrichment] Fungal internal transcribed spacer (ITS) data add replicate noise, low diversity and shallow depth. [src: lignin_community_enrichment] The evidence comes from one study, so these limits are specific to that dataset. See [[summaries/lignin_community_enrichment__REPORT]].

## The n=3 permutation floor

With n=3 per group, pairwise tests cannot reach significance. The report names this floor as its primary statistical limitation. [src: lignin_community_enrichment] Pairwise Mann-Whitney U tests have a minimum achievable p-value of 0.10, because only 10 permutations are possible for 3 vs 3. This makes false discovery rate (FDR)-corrected significance impossible for individual operational taxonomic units (OTUs). [src: lignin_community_enrichment] No individual OTU reached FDR significance. [src: lignin_community_enrichment] Pairwise PERMANOVA (permutational multivariate analysis of variance) with 3 vs 3 samples has the same floor of p~0.10. [src: lignin_community_enrichment] The report recommends n>=5 per group for pairwise significance testing. [src: lignin_community_enrichment] See also [[entities/permanova]] and [[entities/clr-based-differential-abundance-analysis]].

## How pooled and factorial designs recover power

Global tests pool more samples and achieve significance. These are Kruskal-Wallis across all 7 groups and global PERMANOVA. [src: lignin_community_enrichment] The factorial PERMANOVA (M2, n=12 for Round 2) is the most powerful test available. [src: lignin_community_enrichment] For bacteria it gave group F=41.12, R²=0.939, p=0.001. [src: lignin_community_enrichment] The report states that effect sizes (centered log-ratio, CLR, differences and R² values) stay interpretable when p-values are constrained. [src: lignin_community_enrichment]

Significant permutational analysis of multivariate dispersions (PERMDISP) results limit these PERMANOVA results. Dispersion differs between groups for both markers (16S p=0.0004; ITS p=0.0001). [src: lignin_community_enrichment] PERMANOVA therefore captures both location and dispersion effects. [src: lignin_community_enrichment] The report says the group separation is real, but dispersion differences contribute to the signal. [src: lignin_community_enrichment]

## Fungal ITS: the same design gives weaker inference

Fungal ITS communities show extreme replicate variability. Within-group Bray-Curtis (BC) is 0.65, and it reaches 0.99–1.00 for Round 2 groups. [src: lignin_community_enrichment] The report gives 0.09 for 16S. [src: lignin_community_enrichment] This limits ITS inference. The ITS PERMANOVA R² is 0.582, against 0.979 for bacteria. [src: lignin_community_enrichment]

R1 history gave F=1.49, R²=0.142, p=0.090. [src: lignin_community_enrichment] R2 labile C gave F=1.71, R²=0.160, p=0.090. [src: lignin_community_enrichment] Ecological memory is therefore not statistically detectable in ITS. [src: lignin_community_enrichment] The bacterial factorial test gave significant R1-history (p=0.002) and R2-carbon-source (p=0.018) results. [src: lignin_community_enrichment] The fungal comparison relates to [[concepts/ecological-memory-and-historical-contingency-in-serially-passaged-communities]] and [[concepts/fungal-community-responses-to-lignin-and-labile-carbon]].

Consequences the report draws:
- The pre-registered Procrustes analysis was not completed. Near-1.0 Round 2 variability would give poor fit whatever the biological concordance. [src: lignin_community_enrichment]
- At this sample size and depth, fungal communities are dominated by stochastic variation. Formal bacterial–fungal concordance testing is uninformative. [src: lignin_community_enrichment]
- ITS findings should be considered preliminary. [src: lignin_community_enrichment]
- The report proposes that reproducible bacterial effects versus extreme fungal stochasticity suggest different community-assembly mechanisms. This is a proposal, not a tested result. [src: lignin_community_enrichment]

## Candidate causes of ITS noise

The report names several possible contributors to the poor ITS replicate consistency.
- **Depth:** ITS was rarefied to 5,900 reads against 24,000 for 16S. [src: lignin_community_enrichment] Raw ITS depth varied from 6,953–200,902 reads per sample, which contributes to replicate variability even after rarefaction. [src: lignin_community_enrichment]
- **Low diversity:** Enriched groups held only 3–8 OTUs, so composition is sensitive to stochastic variation. [src: lignin_community_enrichment]
- **Sample loss:** Sample LL_1 was excluded (74 reads after filtering), which reduces L-L to n=2. [src: lignin_community_enrichment]
- **Batch effects:** Extraction and library-preparation batch metadata are missing, so batch effects cannot be assessed formally. [src: lignin_community_enrichment]

The report also recommends re-sequencing the ITS libraries at higher depth to improve replicate consistency in Round 2 groups. [src: lignin_community_enrichment]

## Open Directions

- Collect n>=5 per group in a repeat enrichment. This would test whether pairwise PERMANOVA and OTU-level tests can pass the permutation floor.
- Re-sequence the ITS libraries at higher depth. Compare Round 2 within-group BC before and after, to separate depth from true stochasticity.
- Record extraction and library-preparation batches. This would let batch effects be modeled in the next run.
- Rerun the Procrustes concordance test once ITS replicate BC drops well below 1.0.
- Test dispersion separately from location, to split the two components of the PERMANOVA signal.
