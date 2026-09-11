---
type: "Summary"
description: "Lignin enrichment selects communities and reveals strong ecological memory."
doc_type: "short"
full_text: "sources/lignin_community_enrichment__REPORT.md"
---
# Lignin Enrichment and Ecological Memory in Microbial Communities

## Overview

This study used user-provided 16S V3–V4 and ITS2 amplicon data from 21 samples across 7 groups, with 3 replicates per group, to test how lignin enrichment, labile-carbon co-supplementation, and sequential passaging restructure bacterial and fungal communities. The 42 paired-end libraries yielded excellent read quality, with Q30 > 0.94 for all libraries. The analysis used 97% OTU clustering, Bray–Curtis distances, PCoA, and PERMANOVA, a permutation-based test of community-composition differences. [src: lignin_community_enrichment]

## Key Findings

### Lignin is a strong bacterial selective filter

The base bacterial community was dominated by unclassified taxa (Incertae Sedis, 44.3%), while Pseudomonas represented <0.1%. After one lignin-enrichment round, [[entities/pseudomonas-aeruginosa|Pseudomonas]] reached 39.3% and [[entities/acinetobacter-baylyi-adp1|Acinetobacter]] 25.2%, together comprising >64% of 16S reads. Shannon diversity fell from 6.46 to 3.16, and observed OTUs fell from 1,594 to 163, a 90% reduction. Global PERMANOVA attributed 97.9% of community variance to treatment (R²=0.979, p=0.001), while the Base-versus-Round-1 model gave R²=0.992 and p=0.008. [src: lignin_community_enrichment]

### Labile carbon produces a distinct copiotrophic assemblage

Adding labile carbon to lignin increased Acinetobacter from 25.2% in lignin-only communities to 41.7%, reduced Pseudomonas from 39.3% to 23.0%, and increased Aeromonas from 0.1% to 20.2%. Shannon diversity declined from 3.16 to 2.41 and Pielou’s evenness from 0.62 to 0.49. The result supports a shift toward fast-growing copiotrophic taxa alongside lignin-associated organisms, rather than a simple increase in lignin-degrader abundance. [src: lignin_community_enrichment]

### Round-1 carbon history persists into Round 2

Round-2 communities segregated according to their Round-1 history. Lignin-history groups L-L and L-LC were Pseudomonas-dominated at 52–53%, with Acinetobacter below 1–20%; lignin-plus-labile-history groups LC-L and LC-LC were Acinetobacter-dominant at 31–34%, with Pseudomonas at 24–26% and Enterobacter at 2.7–18.1%. In the 12-sample Round-2 factorial PERMANOVA, Round-1 history explained 58.9% of variance (F=14.31, R²=0.589, p=0.002), whereas current Round-2 carbon source explained 32.7% (F=4.85, R²=0.327, p=0.018). The history/Round-2 distance ratios were 1.15 for Round-2 lignin and 1.59 for Round-2 lignin plus labile carbon, indicating stronger historical than current-condition effects. [src: lignin_community_enrichment]

Communities with different Round-1 histories did not converge under identical Round-2 conditions. Mean Bray–Curtis distance was 0.507 for L-L versus LC-L and 0.486 for L-LC versus LC-LC, compared with 0.441 for L-L versus L-LC and 0.306 for LC-L versus LC-LC. The reported memory index was ~0.50, meaning that communities with different histories retained approximately half of the maximum possible divergence under the same current condition. OTU retention was 81% from L to L-L and 91% from LC to LC-LC, with core taxa maintained across the passage series. [src: lignin_community_enrichment]

### Fungal responses are strong but poorly reproducible

The base fungal community contained 253 OTUs and had Shannon diversity 3.50, with Fusarium at 26.5%. Lignin-only enrichment yielded 8 OTUs and Shannon diversity 1.37, with Fusarium at 43.4% and Fusicolla at 30.3%. Lignin plus labile carbon yielded 6 OTUs and Shannon diversity 0.62, with Chrysosporium at 61.4% and Aspergillus at 27.2%. In Round 2, Malassezia reached 63.4% in L-L and 50.0% in LC-L, while Pleurotus reached 50.0% in LC-LC. [src: lignin_community_enrichment]

Fungal replicate consistency was substantially worse than bacterial consistency: within-group Bray–Curtis distances reached 0.99–1.00 for several Round-2 groups, compared with 0.09 for 16S. The ITS global PERMANOVA gave R²=0.582 and p=0.001, and the Round-2 history effect was not statistically detectable (R²=0.142, p=0.090). A preregistered Procrustes analysis, which would formally compare 16S and ITS ordinations, was not completed because the extreme ITS variability would make the rotation uninformative. [src: lignin_community_enrichment]

### Lignin-associated bacterial genera respond conditionally

Pseudomonas increased from <0.1% in the base community to 23–53% across enriched conditions. Flavobacterium increased from 0.1% in the base community to 14.1% under lignin-only enrichment, with a CLR effect of +11.2 in the Base-versus-L comparison, but declined to 1.4% with labile-carbon co-supplementation. Comamonas increased from 0.1% in the base community to 3.6–5.1% in Round-2 groups, representing a 17–51× enrichment. Aminobacter was absent from the base and Round-1 groups but reached 7.6% in L-L and 6.4% in LC-L. Rhodococcus ranged from 0.03–0.67% and was highest in L at 0.67%, while Sphingomonas was higher in the base community at 1.74% than in enriched conditions. [src: lignin_community_enrichment]

The main Base-versus-Lignin CLR effects were +12.3 for Acinetobacter, +11.5 for Pseudomonas, and +11.2 for Flavobacterium. In the L-versus-LC comparison, Aeromonas was enriched in LC with a CLR effect of +6.4, Shewanella with +6.6, while Peredibacter was enriched in L with -7.3 and Comamonas with -6.8. These effect sizes remain interpretable even where small-sample p-values cannot support individual-OTU significance. [src: lignin_community_enrichment]

### Statistical power limits pairwise inference

With n=3 per group, pairwise Mann–Whitney U tests have a minimum achievable p-value of 0.10 because there are only 10 possible permutations for 3-versus-3 comparisons; pairwise PERMANOVA has a permutation floor of approximately p~0.10. Consequently, no individual OTUs reached FDR significance. Global Kruskal–Wallis tests were significant across all 7 groups for all reported metrics, with 16S p=0.006–0.010 and ITS p=0.015–0.041. The Round-2 factorial design with n=12 was the most powered analysis and detected significant effects of both Round-1 history (p=0.002) and Round-2 carbon source (p=0.018). [src: lignin_community_enrichment]

## Data and Processing

The 16S workflow retained 91.2% of reads after primer trimming, 99.8% after quality filtering, and 99.8% after paired-end merging, for approximately 91% total retention. The ITS workflow retained 98.5% after primer trimming, 99.8% after quality filtering, and 99.3% after merging, for approximately 98% total retention. The final data contained 3,392 16S OTUs and 893 ITS OTUs; prevalence and abundance filtering retained 1,793 16S OTUs and 440 ITS OTUs. Per-sample reads ranged from 24,287–88,781 for 16S and 6,953–200,902 for ITS, with genus-level assignment rates of 86.5% and 81.2%, respectively. [src: lignin_community_enrichment]

The 16S alpha-diversity values were: Base, 1,594 ± 12 observed OTUs, Shannon 6.46 ± 0.02, and Pielou 0.88 ± 0.00; L, 163 ± 3, 3.16 ± 0.01, and 0.62 ± 0.00; LC, 133 ± 4, 2.41 ± 0.00, and 0.49 ± 0.00; L-L, 162 ± 3, 3.19 ± 0.10, and 0.63 ± 0.02; LC-L, 178 ± 2, 3.05 ± 0.06, and 0.59 ± 0.01; L-LC, 155 ± 12, 2.85 ± 0.31, and 0.57 ± 0.05; and LC-LC, 153 ± 4, 2.47 ± 0.05, and 0.49 ± 0.01. The corresponding ITS observed-OTU and Shannon values were Base, 253 ± 20 and 3.50 ± 0.33; L, 8 ± 1 and 1.37 ± 0.49; LC, 6 ± 1 and 0.62 ± 0.17; L-L, 6 ± 3 and 0.37 ± 0.50; LC-L, 3 ± 1 and 0.17 ± 0.14; L-LC, 4 ± 3 and 0.05 ± 0.09; and LC-LC, 7 ± 2 and 0.49 ± 0.32. [src: lignin_community_enrichment]

The 3-tier Bray–Curtis PERMANOVA used 999 permutations. For all 7 groups, 16S group separation had F=111.35, R²=0.979, p=0.001, while ITS had F=3.02, R²=0.582, p=0.001. For the Base-versus-Round-1 model, values were 16S F=394.42, R²=0.992, p=0.008, and ITS F=6.92, R²=0.698, p=0.003. For the Round-2 factorial model, group values were 16S F=41.12, R²=0.939, p=0.001, and ITS F=1.72, R²=0.424, p=0.011. PERMDISP was significant for 16S (p=0.0004) and ITS (p=0.0001), indicating heterogeneous dispersions that contribute to the PERMANOVA signal. [src: lignin_community_enrichment]

## Caveats and Limitations

The n=3-per-group design limits statistical power, particularly for pairwise tests; n>=5 per group was proposed for future experiments. The use of 97% vsearch OTUs rather than ASVs may merge closely related organisms. The ITS analysis used NCBI ITS_RefSeq_Fungi with 19,375 reference sequences rather than UNITE, so environmental taxa may be missed and genus-level assignments are more reliable than finer assignments. [src: lignin_community_enrichment]

ITS findings are preliminary because replicate consistency was poor, within-group Bray–Curtis distances approached 1.0 for Round-2 groups, sequencing depth varied from 6,953–200,902 reads per sample before rarefaction, some samples had very low diversity, and sample LL_1 was excluded after retaining 74 reads, reducing L-L to n=2. The fungal memory effect was therefore not statistically detectable, and the notable Pleurotus emergence in LC-LC requires confirmation. [src: lignin_community_enrichment]

PERMDISP was significant for both markers, so PERMANOVA results reflect both differences in group location and differences in dispersion. No technical metadata on extraction or library-preparation batches were available, preventing formal assessment of batch effects. The reported functional interpretation of lignin degradation is based on taxonomic associations and literature context; gene-level pathway enrichment was not directly measured. [src: lignin_community_enrichment]

The planned Procrustes comparison of bacterial and fungal ordinations was not completed because near-random ITS replicate structure would make the fit difficult to interpret. Future work proposed by the document includes larger replication, DADA2 ASV analysis, UNITE-based ITS taxonomy, phylogenetic diversity and UniFrac analyses, KBase Data Lakehouse cross-referencing of Pseudomonas, Acinetobacter, and Comamonas through [[entities/kbase-ke-pangenome|kbase_ke_pangenome]], functional inference of beta-ketoadipate and protocatechuate pathways, deeper ITS sequencing, and intermediate time points to resolve restructuring kinetics. [src: lignin_community_enrichment]

## Slots Into

- [[concepts/ecological-memory]] — the Round-1 history effect, R²=0.589 versus R²=0.327 for current carbon source, and persistent non-convergence provide a quantitative ecological-memory case. [src: lignin_community_enrichment]
- [[concepts/condition-specific-fitness]] — condition-specific enrichment of Pseudomonas, Acinetobacter, Aeromonas, Flavobacterium, and Comamonas links carbon regime to community composition and ecological selection. [src: lignin_community_enrichment]
- [[concepts/multi-omics-integration]] — paired bacterial 16S and fungal ITS profiling provides a cross-marker comparison while demonstrating that poor fungal replicate structure limits concordance analysis. [src: lignin_community_enrichment]
- [[concepts/pangenome-integration]] — the proposed mapping of lignin-enriched genera to gene annotations in [[entities/kbase-ke-pangenome|kbase_ke_pangenome]] creates a direct future bridge from enrichment profiles to pathway content. [src: lignin_community_enrichment]
