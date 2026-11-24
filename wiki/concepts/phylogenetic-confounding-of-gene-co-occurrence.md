---
type: "Concept"
description: "How shared ancestry inflates co-occurrence of gene pairs and how distance stratification limits separating functional coupling from phylogenetic signal."
sources: ["summaries/cofitness_coinheritance__REPORT.md"]
---
# Phylogenetic confounding of gene co-occurrence

This page covers how shared ancestry inflates co-occurrence of gene pairs, and how distance stratification limits separating functional coupling from phylogenetic signal. In the cofitness_coinheritance report, near genomes showed higher pair phi than medium genomes, as expected from shared ancestry. [src: cofitness_coinheritance] Stratification only partly addressed this, because most species had no genomes in the far stratum. [src: cofitness_coinheritance] The evidence comes from one report. See [[summaries/cofitness_coinheritance__REPORT]] and [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]].

## Literature Context

The candidate papers address a related but distinct problem from the hub's. They ask whether taxon-level co-occurrence is associated with horizontal gene transfer (HGT, the movement of genes between lineages). They do not treat gene-pair co-occurrence in general, and they do not test fitness-based coupling. Their starting point is that co-occurring taxa have long been appreciated to undergo HGT more often, and that phylogenetic relatedness, among other factors, confounds this association. The study analyzed 15,339 marine prokaryotic genomes, mainly bacteria, together with metagenomic reads from 1,862 ocean samples. The same abstract appears under two PMIDs: [PMID 41279647](https://pubmed.ncbi.nlm.nih.gov/41279647/) and [PMID 41378915](https://pubmed.ncbi.nlm.nih.gov/41378915/).

The authors report an expected negative association between HGT rates and phylogenetic distance. They detected an association between co-occurrence and phylogenetic distance only for closely related taxa. They present this as refining an earlier reported trend, which they restrict to closely related taxa rather than a pattern across all taxonomic levels, at least within marine environments. The co-occurrence–HGT association remained significant after controlling for phylogenetic distance and measured environmental variables ([PMID 41279647](https://pubmed.ncbi.nlm.nih.gov/41279647/); [PMID 41378915](https://pubmed.ncbi.nlm.nih.gov/41378915/)). These are abstract-level findings from marine data, so they do not transfer automatically to the species-level pangenomes in the hub.

The hub's findings are broadly consistent with this literature in one respect and extend it in another. The cofitness_coinheritance report found higher cofit pair phi among near genomes (mean=0.102) than medium genomes (mean=0.067), and it attributed the difference to shared ancestry. That is directionally consistent with the marine result that the phylogeny–co-occurrence link is concentrated in closely related taxa. The comparison is loose, though. The marine study measures taxon co-occurrence across samples, and the hub measures gene-pair co-inheritance within species. The hub's distance strata are also defined differently, by branch distance within species.

The hub's limitation is not addressed by the candidate papers. Distance stratification was computed for only 7 of 9 organisms, and most species had no genomes in the far stratum (>0.05 branch distance). The hub therefore cannot fully separate functional coupling from phylogenetic signal. The marine study shows that an association can survive explicit control for phylogenetic distance. The hub has not shown the equivalent for fitness-measured coupling, so that question remains open. The Coinfinder comparison proposed in the hub's open directions would be a more direct test. The candidates give no evidence on Coinfinder, on co-fitness, or on near-clonal species such as Ddia6719, so those parts of the hub are neither supported nor contradicted by them.

## Evidence that ancestry inflates co-occurrence

Cofit pair phi was higher among near genomes (mean=0.102) than medium genomes (mean=0.067). The report describes this as expected from shared ancestry. [src: cofitness_coinheritance]

Coinfinder, developed by Whelan et al. (2020), detects pangenome gene associations while controlling for phylogeny. The report asks whether fitness-measured coupling predicts those associations (PMID: 32100706). [src: cofitness_coinheritance]

## Signal in near-clonal species

Low genome diversity does not rule out detecting co-inheritance. Ddia6719 had the strongest pairwise co-inheritance signal (delta=+0.093), although it is near-clonal (ANI 99.47%, average nucleotide identity), because it retained sufficient accessory gene variation. [src: cofitness_coinheritance] Ddia6719 and pseudo3_N2E3 both had enough accessory-gene variation to detect co-inheritance despite low overall genome diversity. [src: cofitness_coinheritance]

## Limits of distance stratification

Phylogenetic distance stratification was computed for 7 of 9 organisms. Most species lacked genomes in the far stratum (>0.05 branch distance). [src: cofitness_coinheritance] Without a far stratum, the report cannot fully separate functional coupling from phylogenetic signal. [src: cofitness_coinheritance] The report proposes resolving the reference-genome mapping to enable phylogenetic distance stratification. [src: cofitness_coinheritance]

## Open Directions

- Resolve the reference-genome mapping so that distance stratification can be computed for all 9 organisms, closing the gap left by the 2 organisms without it.
- Add genomes from more distant relatives for species lacking a far stratum, then test whether the near-versus-medium drop in phi continues into the far stratum.
- Run Coinfinder, which controls for phylogeny, on the same pairs. Compare its associations with fitness-measured coupling.
