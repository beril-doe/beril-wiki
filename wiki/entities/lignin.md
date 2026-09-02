---
type: "Compound"
description: "Complex aromatic polymer that selectively restructures microbial communities"
sources: ["summaries/lignin_community_enrichment__REPORT.md"]
---
# Lignin

## What this entity is

**Canonical name:** Lignin. [src: lignin_community_enrichment]

Lignin is a complex aromatic polymer investigated here as a selective carbon source that restructures microbial communities. [src: lignin_community_enrichment]

**Known aliases:** No aliases were reported in the document. [src: lignin_community_enrichment]

**Stable external identifier:** No stable external identifier was reported in the document. [src: lignin_community_enrichment]

## Evidence from the lignin enrichment study

The study analyzed 21 samples across 7 groups, with 3 replicates per group, using 16S V3–V4 bacterial and ITS2 fungal amplicon data to test how lignin enrichment, labile-carbon supplementation, and sequential passaging restructure communities. [src: lignin_community_enrichment] The study is summarized in [[summaries/lignin_community_enrichment__REPORT]].

### Bacterial community selection

After one lignin-enrichment round, [[entities/pseudomonas-aeruginosa|Pseudomonas]] reached 39.3% of 16S reads and [[entities/acinetobacter-baylyi-adp1|Acinetobacter]] reached 25.2%, together comprising more than 64% of reads. [src: lignin_community_enrichment]

Lignin enrichment reduced bacterial Shannon diversity from 6.46 to 3.16 and observed OTUs from 1,594 to 163, a 90% reduction. [src: lignin_community_enrichment]

The global bacterial PERMANOVA, a permutation-based test of community-composition differences, attributed 97.9% of community variance to treatment (R²=0.979, p=0.001), while the Base-versus-Round-1 model gave R²=0.992 and p=0.008. [src: lignin_community_enrichment]

The main Base-versus-Lignin centered-log-ratio effects were +12.3 for [[entities/acinetobacter-baylyi-adp1|Acinetobacter]], +11.5 for [[entities/pseudomonas-aeruginosa|Pseudomonas]], and +11.2 for [[entities/flavobacterium|Flavobacterium]]. [src: lignin_community_enrichment]

[[entities/flavobacterium|Flavobacterium]] increased from 0.1% in the base community to 14.1% under lignin-only enrichment, but declined to 1.4% when labile carbon was added. [src: lignin_community_enrichment]

[[entities/comamonas|Comamonas]] increased from 0.1% in the base community to 3.6–5.1% in Round-2 groups, representing a 17–51× enrichment. [src: lignin_community_enrichment]

### Interaction with labile carbon

Adding labile carbon to lignin increased [[entities/acinetobacter-baylyi-adp1|Acinetobacter]] from 25.2% to 41.7%, reduced [[entities/pseudomonas-aeruginosa|Pseudomonas]] from 39.3% to 23.0%, and increased [[entities/aeromonas|Aeromonas]] from 0.1% to 20.2%. [src: lignin_community_enrichment]

With labile-carbon co-supplementation, bacterial Shannon diversity declined from 3.16 to 2.41 and Pielou’s evenness declined from 0.62 to 0.49. [src: lignin_community_enrichment]

The result supports a shift toward fast-growing copiotrophic taxa alongside lignin-associated organisms rather than a simple increase in lignin-degrader abundance. [src: lignin_community_enrichment]

### Ecological memory after lignin exposure

Round-2 communities retained the effect of their Round-1 carbon history under identical current conditions. [src: lignin_community_enrichment] This finding contributes to [[concepts/ecological-memory]].

In the 12-sample Round-2 factorial PERMANOVA, Round-1 history explained 58.9% of variance (F=14.31, R²=0.589, p=0.002), whereas current Round-2 carbon source explained 32.7% (F=4.85, R²=0.327, p=0.018). [src: lignin_community_enrichment]

The history/Round-2 distance ratios were 1.15 for Round-2 lignin and 1.59 for Round-2 lignin plus labile carbon, indicating stronger historical than current-condition effects. [src: lignin_community_enrichment]

The reported memory index was approximately 0.50, meaning that communities with different histories retained approximately half of the maximum possible divergence under the same current condition. [src: lignin_community_enrichment]

OTU retention was 81% from L to L-L and 91% from LC to LC-LC, with core taxa maintained across the passage series. [src: lignin_community_enrichment]

### Fungal responses

Lignin-only enrichment reduced the fungal community from 253 observed OTUs in the base community to 8 observed OTUs and reduced Shannon diversity from 3.50 to 1.37. [src: lignin_community_enrichment]

Under lignin-only enrichment, [[entities/fusarium|Fusarium]] represented 43.4% of reads and Fusicolla represented 30.3%; with labile carbon, [[entities/chrysosporium|Chrysosporium]] represented 61.4% and Aspergillus represented 27.2%. [src: lignin_community_enrichment]

Fungal replicate consistency was poor, with within-group Bray–Curtis distances reaching 0.99–1.00 for several Round-2 groups compared with 0.09 for 16S data. [src: lignin_community_enrichment]

The ITS global PERMANOVA gave R²=0.582 and p=0.001, but the Round-2 history effect was not statistically detectable (R²=0.142, p=0.090). [src: lignin_community_enrichment]

The document states that functional interpretation of lignin degradation was based on taxonomic associations and literature context, because gene-level pathway enrichment was not directly measured. [src: lignin_community_enrichment]

## Related integration

Lignin enrichment provides condition-specific evidence for [[concepts/condition-specific-fitness]] because carbon regime altered the relative enrichment of [[entities/pseudomonas-aeruginosa|Pseudomonas]], [[entities/acinetobacter-baylyi-adp1|Acinetobacter]], [[entities/aeromonas|Aeromonas]], [[entities/flavobacterium|Flavobacterium]], and [[entities/comamonas|Comamonas]]. [src: lignin_community_enrichment]

The paired bacterial 16S and fungal ITS measurements connect lignin response analysis to [[concepts/multi-omics-integration]], while the poor fungal replicate structure limited formal cross-marker concordance analysis. [src: lignin_community_enrichment]

The study proposed cross-referencing lignin-enriched genera through [[entities/kbase-ke-pangenome|KBase KE Pangenome]] and testing beta-ketoadipate and protocatechuate pathway potential, linking lignin community selection to [[concepts/pangenome-integration]]. [src: lignin_community_enrichment]
