---
type: Compound
description: Complex aromatic polymer that selectively restructures microbial communities
sources:
- id: lignin_community_enrichment
  resource: ../summaries/lignin_community_enrichment__REPORT.md
  title: lignin community enrichment
title: Lignin
---
# Lignin

## What this entity is

**Canonical name:** Lignin. [^lignin_community_enrichment]

Lignin is a complex aromatic polymer investigated here as a selective carbon source that restructures microbial communities. [^lignin_community_enrichment]

**Known aliases:** No aliases were reported in the document. [^lignin_community_enrichment]

**Stable external identifier:** No stable external identifier was reported in the document. [^lignin_community_enrichment]

## Evidence from the lignin enrichment study

The study analyzed 21 samples across 7 groups, with 3 replicates per group, using 16S V3–V4 bacterial and ITS2 fungal amplicon data to test how lignin enrichment, labile-carbon supplementation, and sequential passaging restructure communities. [^lignin_community_enrichment] The study is summarized in [lignin_community_enrichment__REPORT](../summaries/lignin_community_enrichment__REPORT.md).

### Bacterial community selection

After one lignin-enrichment round, [Pseudomonas](pseudomonas-aeruginosa.md) reached 39.3% of 16S reads and [Acinetobacter](acinetobacter-baylyi-adp1.md) reached 25.2%, together comprising more than 64% of reads. [^lignin_community_enrichment]

Lignin enrichment reduced bacterial Shannon diversity from 6.46 to 3.16 and observed OTUs from 1,594 to 163, a 90% reduction. [^lignin_community_enrichment]

The global bacterial PERMANOVA, a permutation-based test of community-composition differences, attributed 97.9% of community variance to treatment (R²=0.979, p=0.001), while the Base-versus-Round-1 model gave R²=0.992 and p=0.008. [^lignin_community_enrichment]

The main Base-versus-Lignin centered-log-ratio effects were +12.3 for [Acinetobacter](acinetobacter-baylyi-adp1.md), +11.5 for [Pseudomonas](pseudomonas-aeruginosa.md), and +11.2 for [Flavobacterium](flavobacterium.md). [^lignin_community_enrichment]

[Flavobacterium](flavobacterium.md) increased from 0.1% in the base community to 14.1% under lignin-only enrichment, but declined to 1.4% when labile carbon was added. [^lignin_community_enrichment]

[Comamonas](comamonas.md) increased from 0.1% in the base community to 3.6–5.1% in Round-2 groups, representing a 17–51× enrichment. [^lignin_community_enrichment]

### Interaction with labile carbon

Adding labile carbon to lignin increased [Acinetobacter](acinetobacter-baylyi-adp1.md) from 25.2% to 41.7%, reduced [Pseudomonas](pseudomonas-aeruginosa.md) from 39.3% to 23.0%, and increased [Aeromonas](aeromonas.md) from 0.1% to 20.2%. [^lignin_community_enrichment]

With labile-carbon co-supplementation, bacterial Shannon diversity declined from 3.16 to 2.41 and Pielou’s evenness declined from 0.62 to 0.49. [^lignin_community_enrichment]

The result supports a shift toward fast-growing copiotrophic taxa alongside lignin-associated organisms rather than a simple increase in lignin-degrader abundance. [^lignin_community_enrichment]

### Ecological memory after lignin exposure

Round-2 communities retained the effect of their Round-1 carbon history under identical current conditions. [^lignin_community_enrichment] This finding contributes to [ecological-memory](../concepts/ecological-memory.md).

In the 12-sample Round-2 factorial PERMANOVA, Round-1 history explained 58.9% of variance (F=14.31, R²=0.589, p=0.002), whereas current Round-2 carbon source explained 32.7% (F=4.85, R²=0.327, p=0.018). [^lignin_community_enrichment]

The history/Round-2 distance ratios were 1.15 for Round-2 lignin and 1.59 for Round-2 lignin plus labile carbon, indicating stronger historical than current-condition effects. [^lignin_community_enrichment]

The reported memory index was approximately 0.50, meaning that communities with different histories retained approximately half of the maximum possible divergence under the same current condition. [^lignin_community_enrichment]

OTU retention was 81% from L to L-L and 91% from LC to LC-LC, with core taxa maintained across the passage series. [^lignin_community_enrichment]

### Fungal responses

Lignin-only enrichment reduced the fungal community from 253 observed OTUs in the base community to 8 observed OTUs and reduced Shannon diversity from 3.50 to 1.37. [^lignin_community_enrichment]

Under lignin-only enrichment, [Fusarium](fusarium.md) represented 43.4% of reads and Fusicolla represented 30.3%; with labile carbon, [Chrysosporium](chrysosporium.md) represented 61.4% and Aspergillus represented 27.2%. [^lignin_community_enrichment]

Fungal replicate consistency was poor, with within-group Bray–Curtis distances reaching 0.99–1.00 for several Round-2 groups compared with 0.09 for 16S data. [^lignin_community_enrichment]

The ITS global PERMANOVA gave R²=0.582 and p=0.001, but the Round-2 history effect was not statistically detectable (R²=0.142, p=0.090). [^lignin_community_enrichment]

The document states that functional interpretation of lignin degradation was based on taxonomic associations and literature context, because gene-level pathway enrichment was not directly measured. [^lignin_community_enrichment]

## Related integration

Lignin enrichment provides condition-specific evidence for [condition-specific-fitness](../concepts/condition-specific-fitness.md) because carbon regime altered the relative enrichment of [Pseudomonas](pseudomonas-aeruginosa.md), [Acinetobacter](acinetobacter-baylyi-adp1.md), [Aeromonas](aeromonas.md), [Flavobacterium](flavobacterium.md), and [Comamonas](comamonas.md). [^lignin_community_enrichment]

The paired bacterial 16S and fungal ITS measurements connect lignin response analysis to [multi-omics-integration](../concepts/multi-omics-integration.md), while the poor fungal replicate structure limited formal cross-marker concordance analysis. [^lignin_community_enrichment]

The study proposed cross-referencing lignin-enriched genera through [KBase KE Pangenome](kbase-ke-pangenome.md) and testing beta-ketoadipate and protocatechuate pathway potential, linking lignin community selection to [pangenome-integration](../concepts/pangenome-integration.md). [^lignin_community_enrichment]

[^lignin_community_enrichment]: [lignin community enrichment](../summaries/lignin_community_enrichment__REPORT.md)
