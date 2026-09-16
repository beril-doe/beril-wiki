# Markus de Raad

ORCID: [0000-0001-8263-9198](https://orcid.org/0000-0001-8263-9198)

## Contributions

[[summaries/lignin_community_enrichment__REPORT]] used user-provided 16S V3–V4 and ITS2 amplicon data from 21 samples (7 groups × 3 replicates) to test how lignin enrichment, labile-carbon co-supplementation and sequential passaging restructure bacterial and fungal communities. The project reported Q30 > 0.94 for all libraries. Its data-quality section counts 84 paired-end FASTQ libraries, while its Sources table lists 42 (21 samples x 2 markers), and the report leaves that discrepancy unresolved. The project clustered reads into 97% OTUs (operational taxonomic units) and compared communities with Bray–Curtis distances, PCoA (principal coordinates analysis, an ordination of the distance matrix) and PERMANOVA (a permutation-based test of community-composition differences). [src: lignin_community_enrichment]

The project found that one round of lignin enrichment turned a base community with Pseudomonas below 0.1% into one dominated by Pseudomonas (39.3%) and Acinetobacter (25.2%). Over the same round, Shannon diversity fell from 6.46 to 3.16 and observed OTUs fell from 1,594 to 163, a 90% reduction. The Base-versus-Round-1 PERMANOVA gave R²=0.992, p=0.008. The global seven-group PERMANOVA gave R²=0.979, p=0.001, and the report notes that this global result is not a Base-versus-L test. [src: lignin_community_enrichment]

The report infers lignin-aromatic catabolic capacity from taxonomy rather than measuring it. [src: lignin_community_enrichment]

Adding labile carbon (LC) produced a different bacterial assemblage. Acinetobacter rose to 41.7%, Pseudomonas fell to 23.0% and Aeromonas rose from 0.1% to 20.2%. Shannon diversity fell from 3.16 to 2.41 and Pielou's evenness from 0.62 to 0.49. The report presents its copiotrophic explanation for this shift as an interpretation, not a measured mechanism. [src: lignin_community_enrichment]

Flavobacterium rose from 0.1% to 14.1% under lignin but declined to 1.4% under LC, with a CLR effect (centered log-ratio difference, a compositional effect size) of +11.2 for Base versus L. The report tentatively reads this pattern as indicating a lignin-aromatic specialist. Comamonas rose from 0.1% to 3.6–5.1% in Round-2 groups. The report also states a 17–51x enrichment for Comamonas that does not match those abundances, and it leaves the two figures unreconciled. [src: lignin_community_enrichment]

In bacterial 16S data, [[summaries/lignin_community_enrichment__REPORT]] found that Round-1 carbon history persisted into Round 2. Lignin-history groups were Pseudomonas-dominated (52–53%), while labile-history groups were Acinetobacter-dominant (31–34%). In the Round-2 factorial PERMANOVA, Round-1 history explained 58.9% of variance (F=14.31, R²=0.589, p=0.002). The current carbon source explained 32.7% (F=4.85, R²=0.327, p=0.018). [src: lignin_community_enrichment]

Communities with different histories did not converge under identical Round-2 conditions. Mean Bray–Curtis distances were 0.507 and 0.486 for different-history pairs, compared with 0.441 and 0.306 for same-history pairs. The project reported a memory index of ~0.50. Across passages, 81% (L to L-L) and 91% (LC to LC-LC) of Round-1 OTUs were retained. The report frames this persistence as community-level priming, which it presents as a hypothesis, and it notes that lignin degradation itself was not measured. [src: lignin_community_enrichment]

The project found strong but poorly reproducible fungal responses. Fusarium (43.4%) and Fusicolla (30.3%) dominated under lignin, and Chrysosporium (61.4%) and Aspergillus (27.2%) dominated under LC. In Round 2, Malassezia dominated in L-L (63.4%) and LC-L (50.0%), and Pleurotus reached 50.0% in LC-LC. The report flags that the Pleurotus result rests on ITS data with poor replicate consistency. [src: lignin_community_enrichment]

ITS richness collapsed from 253 OTUs to 3–8 per group. Within-group Bray–Curtis distance was 0.65 for ITS, reaching 0.99–1.00 in Round-2 groups, against 0.09 for 16S. The ITS global PERMANOVA was significant (F=3.02, R²=0.582, p=0.001). However, the ITS Round-2 model detected neither a history effect (F=1.49, R²=0.142, p=0.090) nor a labile-carbon effect (F=1.71, R²=0.160, p=0.090), so ecological memory was not statistically detectable in fungi. The preregistered Procrustes concordance analysis was not completed. The report does not establish low sequencing depth or any assembly mechanism as the cause of the fungal stochasticity. [src: lignin_community_enrichment]

## Projects (1)

- [[summaries/lignin_community_enrichment__REPORT|lignin_community_enrichment]]
