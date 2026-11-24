---
type: "Concept"
description: "How a single lignin enrichment round collapses diversity and replaces a base community with a few aromatic-tolerant taxa; limited to bacterial community-level responses."
sources: ["summaries/lignin_community_enrichment__REPORT.md"]
---
# Selective filtering of communities by lignin enrichment

A single round of lignin enrichment replaces a diverse, largely unclassified bacterial base community with a few aromatic-tolerant genera, chiefly [[entities/pseudomonas|Pseudomonas]] and Acinetobacter. The evidence comes from one project (see [[summaries/lignin_community_enrichment__REPORT]]), is limited to bacterial 16S community-level responses, and rests on direct measurement with strong PERMANOVA statistics. The report reads the turnover as lignin acting as a selective filter. [src: lignin_community_enrichment]

## Literature Context

The candidate papers show that lignin and lignin-derived aromatics commonly enrich bacterial consortia, but they are mostly studies of different systems, and none repeats the single-round design of this corpus. Enrichment on lignin as sole carbon source recovered sixteen isolates from decaying Tilia cordata wood, including Pseudomonas, Bacillus, Stenotrophomonas and Enterobacteriaceae, and all of them showed ligninolytic potential in a methylene blue decolorization assay [PMID 41753552](https://pubmed.ncbi.nlm.nih.gov/41753552/). An acetosyringone-enriched consortium was predominantly Pseudomonas rhizophila [PMID 41589901](https://pubmed.ncbi.nlm.nih.gov/41589901/). Kraft lignin enrichment of ruminal bacteria gave consortia enriched in the genus Dickeya [PMID 38850683](https://pubmed.ncbi.nlm.nih.gov/38850683/). Soil microcosms receiving p-hydroxybenzoate or vanillate selected several aromatic degraders. Lignin itself produced more extensive responses in bacterial diversity and composition than its constituents [PMID 37356789](https://pubmed.ncbi.nlm.nih.gov/37356789/). Acinetobacter appears among isolates carrying the aromatic ring-cleavage gene pcaH in salt marsh enrichments [PMID 11722937](https://pubmed.ncbi.nlm.nih.gov/11722937/).

The candidates also indicate that the outcome depends on the substrate. In an in situ coastal enrichment, consortia on woody lignocellulose were more diverse than those on herbaceous substrate, with substrate-dependent taxonomic groups [PMID 37417747](https://pubmed.ncbi.nlm.nih.gov/37417747/). That study also reported increasing alpha diversity over time. Other work on lignin enrichment was done under denitrifying conditions, where metagenomics of eight enrichments on five lignins recovered 62 metagenome-assembled genomes [PMID 41881888](https://pubmed.ncbi.nlm.nih.gov/41881888/). That is a difference between studies, not a tested comparison of oxygen status.

The corpus finding that one lignin round lets Pseudomonas (39.3%) and Acinetobacter (25.2%) replace a base community in which Pseudomonas was below 0.1% is consistent with these reports. Pseudomonas and Acinetobacter are recurrent aromatic-tolerant or aromatic-degrading enrichment taxa [PMID 41753552](https://pubmed.ncbi.nlm.nih.gov/41753552/), [PMID 41589901](https://pubmed.ncbi.nlm.nih.gov/41589901/), [PMID 11722937](https://pubmed.ncbi.nlm.nih.gov/11722937/). The corpus's reading of lignin as a selective filter is therefore plausible. It rests on direct 16S measurement, not on the isolate or functional evidence in those papers.

The corpus extends the literature in the size of the diversity collapse. It reports Shannon diversity falling from 6.46 to 3.16 and observed OTUs falling from 1,594 to 163, a 90% reduction, with PERMANOVA R²=0.979. The candidates give no matching quantification. The coastal study, which reports diversity rising over time, differs in setting and design, so it is not a direct contradiction [PMID 37417747](https://pubmed.ncbi.nlm.nih.gov/37417747/). The lack of Sphingomonas enrichment, despite its known aromatic catabolism, is not addressed by any candidate and is novel here. The soil microcosm study also cautions that effects of lignin may reflect regulation of the wider microbiome, not individual taxa [PMID 37356789](https://pubmed.ncbi.nlm.nih.gov/37356789/). This supports the corpus's open call for isolate growth tests and no-lignin passage controls before taxon-level metabolism is inferred.

## Community turnover

The base community is dominated by unclassified taxa (Incertae Sedis, 44.3%), and Pseudomonas is below 0.1%. [src: lignin_community_enrichment] After one lignin round, Pseudomonas (39.3%) and Acinetobacter (25.2%) together make up more than 64% of 16S reads. [src: lignin_community_enrichment] The report calls this near-complete turnover and takes it as strong support for lignin as a selective filter. [src: lignin_community_enrichment] The shift is consistent across replicates. [src: lignin_community_enrichment]

Mean relative abundances of Pseudomonas, Acinetobacter, Aeromonas, Enterobacter, Flavobacterium and Comamonas, in that order:

- Base: <0.1%, <0.1%, <0.1%, <0.1%, 0.1%, 0.1%. [src: lignin_community_enrichment]
- L: 39.3%, 25.2%, 0.1%, 0.5%, 14.1%, 1.7%. [src: lignin_community_enrichment]

Pseudomonas is absent in base (<0.1%) but dominant in all enriched conditions (23–53%). [src: lignin_community_enrichment]

A separate Base-versus-Lignin differential-abundance table gives these increases:

- Acinetobacter: from <0.1% to 17.0%, centered log-ratio (CLR) effect +12.3. [src: lignin_community_enrichment]
- Pseudomonas: from <0.1% to 7.5%, CLR effect +11.5. [src: lignin_community_enrichment]
- Flavobacterium: from <0.1% to 9.0%, CLR effect +11.2. [src: lignin_community_enrichment]

Sphingomonas does not follow the pattern. It is higher in base (1.74%) than in enriched conditions. This suggests lignin enrichment does not select it, despite its known aromatic catabolism. [src: lignin_community_enrichment] See [[entities/sphingomonas]].

## Diversity collapse

Bacterial diversity falls sharply. Shannon diversity drops from 6.46 (Base) to 3.16 (L), and observed operational taxonomic units (OTUs) drop from 1,594 to 163, a 90% reduction. [src: lignin_community_enrichment] The report reads this as consistent with strong selection for a few taxa able to metabolize lignin-derived aromatics. [src: lignin_community_enrichment] Kruskal-Wallis tests across all 7 groups were significant for all metrics (16S: p=0.006–0.010; ITS: p=0.015–0.041). [src: lignin_community_enrichment]

- Base bacteria: 1,594 ± 12 observed OTUs, Shannon 6.46 ± 0.02, Pielou evenness 0.88 ± 0.00. [src: lignin_community_enrichment]
- L bacteria: 163 ± 3 observed OTUs, Shannon 3.16 ± 0.01, Pielou evenness 0.62 ± 0.00. [src: lignin_community_enrichment]

Fungal communities (internal transcribed spacer, ITS) fell too, from 253 ± 20 observed OTUs and Shannon 3.50 ± 0.33 in Base [src: lignin_community_enrichment] to 8 ± 1 and 1.37 ± 0.49 in L. [src: lignin_community_enrichment] Fungal replicates were far less consistent than bacterial ones (within-group Bray-Curtis 0.65, against 0.09 for 16S), so this page does not rely on them. [src: lignin_community_enrichment]

## Statistical support

Replicate consistency is excellent for 16S, with within-group Bray-Curtis (BC) dissimilarity of 0.09. [src: lignin_community_enrichment] Principal coordinates analysis (PCoA) separates all treatment groups. PC1 and PC2 together explain 81.1% of 16S variance and 34.0% of ITS variance. [src: lignin_community_enrichment] [[entities/permanova]] (permutational multivariate analysis of variance) shows treatment explaining 97.9% of bacterial community variance (R²=0.979, p=0.001). [src: lignin_community_enrichment] The model with all 7 groups gave F=111.35, R²=0.979, p=0.001. [src: lignin_community_enrichment] The Base-versus-R1 comparison gave F=394.42, R²=0.992, p=0.008. [src: lignin_community_enrichment]

## Open Directions

- Test whether the Pseudomonas/Acinetobacter takeover persists or changes over further rounds. Only one round is characterized here, and a multi-round time series would show it.
- Run a no-lignin carrier or passage control to separate lignin selection from selection by serial transfer alone.
- Isolate Pseudomonas, Acinetobacter and Flavobacterium and test growth on lignin-derived aromatics. This would check the inferred aromatic metabolism against [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]].
- Explain why Sphingomonas is not enriched, for example by competition or by growth conditions. Compare with [[concepts/labile-carbon-effects-on-lignin-degrading-community-structure]].
- Reconcile the Lignin-condition percentages in the differential-abundance table with the group L means.
