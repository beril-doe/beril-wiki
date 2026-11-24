---
type: "Concept"
description: "How OTU versus exact-variant clustering and choice of 16S/ITS reference databases limit taxonomic assignment in amplicon studies."
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md"]
---
# Taxonomic resolution and reference database limits in amplicon profiling

Two projects show how clustering method and reference database limit taxonomic assignment in amplicon profiling. In the SSO (sediment) ASV study, species-level classification was near zero and genus-level classification was partial. [src: enigma_sso_asv_ecology] In the lignin-enrichment study, 97% OTU clustering and incomplete reference databases limited resolution. [src: lignin_community_enrichment] The evidence comes from two projects' own caveats, not from a direct test of alternatives. See [[summaries/enigma_sso_asv_ecology__REPORT]] and [[summaries/lignin_community_enrichment__REPORT]].

## Literature Context

The candidate papers show that taxonomic resolution in amplicon profiling depends heavily on the reference database, the marker region and the clustering or denoising method. A bladder-microbiota study evaluated combinations of reference database, 16S variable region and classification algorithm. It found that species-level identification is possible, and that the reference database was the most important component, followed by the variable region sequenced [PMID 34519534](https://pubmed.ncbi.nlm.nih.gov/34519534/). Ecosystem-specific databases give similar gains. A custom soil database built from 987,353 full-length 16S rRNA genes increased genus- and species-level classification compared with commonly used universal databases [PMID 36406450](https://pubmed.ncbi.nlm.nih.gov/36406450/). TaxAss paired SILVA with a curated freshwater database. It increased the share of reads classified by as much as 11 to 40% of total reads across the freshwater datasets, most at family to species level. A control mouse gut dataset showed no similar increase [PMID 30185512](https://pubmed.ncbi.nlm.nih.gov/30185512/). A targeted seafloor-sediment database (AQUAeD-DB, 14,545 16S sequences clustered at 95% identity) likewise gave more consistent Illumina and Nanopore assignments than a standard database. The median correlation was only 0.50 [PMID 40852940](https://pubmed.ncbi.nlm.nih.gov/40852940/).

The papers also show that exact-variant methods and longer or more variable markers improve resolution. Combining the 16-23S intergenic spacer with DADA2 denoising gave a 5.2-fold increase in community resolution over reference-based 16S analysis. This was shown in longitudinal subgingival plaque samples from an oral microbiome study [PMID 30185233](https://pubmed.ncbi.nlm.nih.gov/30185233/). Full-length 16S sequencing with Emu was proposed to reach species-level resolution while compensating for incomplete reference databases [PMID 38511467](https://pubmed.ncbi.nlm.nih.gov/38511467/). Serovar prediction from full-length 16S reached over 89% accuracy for Salmonella on in silico data, but it is less accurate than whole-genome sequencing of isolates [PMID 38319092](https://pubmed.ncbi.nlm.nih.gov/38319092/). Shotgun metagenomics also relies on incomplete reference databases and has high cost [PMID 40666886](https://pubmed.ncbi.nlm.nih.gov/40666886/).

The corpus's findings are consistent with this literature. The SSO sediment study reports near-zero species-level classification and genus-level classification for only 44% of reads. This matches the point that general-purpose databases classify poorly in under-characterised environments. The seafloor and soil database studies suggest the hypothesis that an environment-specific database could raise that fraction. The corpus did not test this, and the hub's open direction of comparing a second database is the right test. The lignin-enrichment report's caveat that 97% OTU clustering may merge closely related species is consistent with the gains from DADA2 exact variants. It is also consistent with the finer resolution of the intergenic-spacer approach. Its 86.5% (16S) and 81.2% (ITS) genus-level assignment is higher than the SSO figure. Because the two studies differ in environment, database and method, the gap cannot be assigned to one cause. The lignin report's recommendation to obtain UNITE for environmental fungi parallels the literature's case for targeted databases. The cited papers address bacterial 16S, so they give no direct evidence on ITS fungal databases. The corpus's observations come from its own stated caveats, not from direct tests of alternatives. They add no new method, and they extend the literature only by documenting these limits in two environmental datasets.

## Resolution limits in the SSO sediment study

Species-level classification is ~0%, and genus-level classification covers only 44% of sediment reads. [src: enigma_sso_asv_ecology] The report states that 56% of reads lack genus-level classification. [src: enigma_sso_asv_ecology] This matters because functional inferences there rest on taxonomy-to-trait mapping [src: enigma_sso_asv_ecology]; see [[concepts/taxonomy-based-functional-inference-of-biogeochemical-processes-and-the-redox-ladder]]. The report proposes shotgun metagenomics to capture these reads. [src: enigma_sso_asv_ecology]

## Clustering choice in the lignin-enrichment study

Reads were processed through vsearch with 97% OTU clustering (operational taxonomic unit) and de novo chimera removal. [src: lignin_community_enrichment] This was used instead of ASV-level resolution with DADA2 because of environment constraints, and it may merge closely related species. [src: lignin_community_enrichment] The report recommends installing DADA2 (R) for exact sequence variant analysis, which would give finer resolution than 97% OTUs. [src: lignin_community_enrichment]

## Reference databases

16S taxonomy used SILVA 138.2 NR99, with 510,495 SSU rRNA reference sequences, assigned by vsearch sintax at 80% confidence. [src: lignin_community_enrichment] ITS (internal transcribed spacer) taxonomy used NCBI ITS_RefSeq_Fungi, with 19,375 curated fungal ITS sequences, assigned by BLASTn. [src: lignin_community_enrichment]

Genus-level assignment was 86.5% for 16S and 81.2% for ITS. [src: lignin_community_enrichment] For ITS, some assignments may be imprecise, and genus level is more reliable. [src: lignin_community_enrichment] The standard ITS database UNITE could not be downloaded. The NCBI RefSeq approach gives reliable genus-level classification but may miss rare or novel taxa. [src: lignin_community_enrichment] The database may underrepresent environmental taxa. [src: lignin_community_enrichment] The report recommends obtaining UNITE to improve fungal taxonomy, particularly for environmental taxa missed by the NCBI approach. [src: lignin_community_enrichment]

## Related limit: phylogeny

The report also proposes building a 16S phylogenetic tree for Faith's PD and weighted and unweighted UniFrac distances. [src: lignin_community_enrichment]

## Open Directions

- Re-run the lignin-enrichment data with DADA2 exact variants and compare genus assignments to the 97% OTU results. This would show how many OTUs merge distinct species.
- Reclassify the ITS OTUs against UNITE and compare with the NCBI ITS_RefSeq_Fungi assignments. This would test how many environmental taxa the NCBI database misses.
- Run shotgun metagenomics on the SSO samples at the same spatial resolution. This would test taxonomy-based functional inferences and cover the reads lacking genus assignment.
- Compare 16S genus assignment against a second reference database for the SSO reads. This would show whether the 44% genus coverage reflects the database or the short amplicon.
