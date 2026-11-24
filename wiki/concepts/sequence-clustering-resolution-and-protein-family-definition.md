---
type: "Concept"
description: "How clustering thresholds (90/50/30% identity) shape the redundancy and family structure of a protein sequence collection, including the arbitrariness of cutoffs."
sources: ["summaries/paperblast_explorer__REPORT.md"]
---
# Sequence clustering resolution and protein family definition

Clustering a protein collection at 90%, 50% and 30% identity gives three views of its redundancy and family structure. In the PaperBLAST collection, as analysed in the paperblast_explorer report, most clusters are singletons even at 30% identity. [src: paperblast_explorer] The 50% "protein family" cutoff is conventional, not a biological boundary. [src: paperblast_explorer] The evidence comes from one dataset and one clustering tool. See [[summaries/paperblast_explorer__REPORT]] for the full report.

## Literature Context

The candidate papers show that identity thresholds are widely used to define protein groupings, and that the thresholds are chosen by convention and differ between fields. One paper states that classification of proteins in general is bedevilled with the need for subjective thresholds to define group membership, and that this arbitrariness has practical consequences, for example in choosing structural genomics targets [PMID 11391012](https://pubmed.ncbi.nlm.nih.gov/11391012/). It describes an alternative that clusters proteins without an a priori threshold, using dynamic programming. Separately, it investigated the relationship between sequence weights and sequence identity for 168 HOMSTRAD families. Only an abstract was available, so the detail of that analysis is not assessed here.

The other papers show the same dependence on cutoffs in specific families. In cytochrome P450s, families are defined by amino acid identity thresholds, with thresholds as low as 40% in some families. Inter-family identities below 30% give poor alignments and weakly supported phylogenies [PMID 40973623](https://pubmed.ncbi.nlm.nih.gov/40973623/). In the plant MATE transporters, subgroups were assigned by a four-step process that used 60% protein sequence identity, with a threshold of 1E-05 and different sequence-length conditions, or retention in similar synteny blocks [PMID 35371145](https://pubmed.ncbi.nlm.nih.gov/35371145/). In a study of an arylsulfatase and phosphonate monoester hydrolase family, sequence networks allowed the identity threshold to be chosen, which clustered members that presumably have more similar functions [PMID 34727710](https://pubmed.ncbi.nlm.nih.gov/34727710/). Taxonomic work also uses ad hoc cutoffs. One study proposed 70% amino acid identity as a genus boundary in Erythrobacteraceae [PMID 32726199](https://pubmed.ncbi.nlm.nih.gov/32726199/). Another cited a genus demarcation range of 60-85% [PMID 40833889](https://pubmed.ncbi.nlm.nih.gov/40833889/). Virus reports likewise rely on species demarcation thresholds, which differ by family [PMID 36653663](https://pubmed.ncbi.nlm.nih.gov/36653663/), [PMID 39636458](https://pubmed.ncbi.nlm.nih.gov/39636458/), [PMID 31784911](https://pubmed.ncbi.nlm.nih.gov/31784911/).

The corpus's caution that the 50% identity "protein family" cutoff is conventional and not a biological boundary is consistent with this literature. The cutoffs in the candidate papers range from 40% (some P450 families) to 70% (the Erythrobacteraceae genus boundary), so no single value is universal. The corpus's counts are descriptive of one dataset and one tool. MMseqs2 clustered 815,571 PaperBLAST sequences into 628K clusters at 90%, 345K at 50% and 215K at 30% identity. Singletons made up 83.3%, 67.5% and 62.8% of clusters at those thresholds. None of the candidates measure singleton shares or cluster counts in a comparable sequence collection, so those figures are novel here and cannot be checked against these papers.

The corpus does not test the threshold-free approach described in [PMID 11391012](https://pubmed.ncbi.nlm.nih.gov/11391012/). Its open directions, which include re-clustering at intermediate thresholds and comparing 50% clusters with curated family databases, would address the arbitrariness problem that paper raises. They would extend it to a large, mostly singleton collection.

## Cluster counts at three thresholds

[[entities/mmseqs2|MMseqs2]] clustered 815,571 PaperBLAST protein sequences at three identity thresholds. [src: paperblast_explorer] The cluster count falls as the threshold loosens:

| Identity | Clusters | Interpretation in the report | Cluster-size file rows |
|---|---|---|---|
| 90% | 628K (77%) | low strain-level redundancy [src: paperblast_explorer] | 628,441 [src: paperblast_explorer] |
| 50% | 345K | protein family level [src: paperblast_explorer] | 344,981 [src: paperblast_explorer] |
| 30% | 215K | superfamily level [src: paperblast_explorer] | 214,534 [src: paperblast_explorer] |

## Singletons and large clusters

Most clusters are singletons at every threshold, and the share falls only slowly as the threshold loosens. At 90% identity, 83.3% of clusters are singletons. The report reads this as most PaperBLAST sequences already being non-redundant at the strain level. [src: paperblast_explorer] At 50% identity 67.5% of clusters are singletons, and at 30% identity 62.8%. [src: paperblast_explorer]

The largest 90% cluster is actin, with 212 members. [src: paperblast_explorer] The largest families at 50% identity are housekeeping proteins: HSP70/BiP with 650 members, GAPDH with 609, enolase with 552 and GroEL with 443. [src: paperblast_explorer] At 30% identity, cumulative capture curves show that a relatively small number of large superfamily clusters capture a substantial fraction of all sequences. The long tail of singleton families accounts for the remainder. [src: paperblast_explorer]

## Arbitrariness of cutoffs

The report cautions that the 50% identity cutoff for "protein family" is conventional. It does not match a universal biological boundary. [src: paperblast_explorer] The counts above are therefore descriptive of these thresholds, not of fixed family units. Related work on unstudied families is in [[concepts/unstudied-protein-families-and-the-literature-defined-dark-proteome]].

## Open Directions

- Re-cluster at intermediate thresholds (for example 40% and 70%) and plot cluster count against identity. This would show whether any threshold marks a natural break, which tests the arbitrariness caveat.
- Compare 50% clusters with curated family databases such as Pfam. This would show how often the cutoff splits or merges real families.
- Repeat the singleton analysis with a different clustering tool or coverage setting. This would show how much of the 62.8–83.3% singleton share depends on the method.
- Test whether the unstudied-family conclusions change when the family threshold moves from 50% to 30%.
