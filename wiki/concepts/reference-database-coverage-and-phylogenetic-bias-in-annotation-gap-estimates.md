---
type: "Concept"
description: "How over-representation of well-studied taxa, representative-only sampling and reference-genome annotation quality bias estimates of the bacterial annotation gap and its resolution across organisms; stops at the specific analyses' caveats."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Reference-database coverage and phylogenetic bias in annotation-gap estimates

Estimates of the bacterial annotation gap depend on which organisms the reference databases cover well. Three reports describe biases of this kind. The alphafold_msa_annotation report says UniProt over-represents well-studied organisms and that the gap for the uncovered clusters is likely larger. [src: alphafold_msa_annotation] The annotation_gap_discovery report notes that 12 of 14 organisms are Proteobacteria. [src: annotation_gap_discovery] The functional_dark_matter report finds uneven hypothetical-gene fractions across organisms, which it attributes to annotation depth. [src: functional_dark_matter]

## Coverage of the pangenome by UniProt and AlphaFold

Under a third of bacterial gene clusters could be linked to AlphaFold. The analysis used 132,531,501 gene clusters in kbase_ke_pangenome.gene_cluster. [src: alphafold_msa_annotation] Of these, 38,804,903 (29.3%) have a real UniProt accession via bakta_annotations.uniref100. [src: alphafold_msa_annotation] Also, 38,051,842 (28.7%) bridge to kescience_alphafold.alphafold_msa_depths. [src: alphafold_msa_annotation] The remaining 70.7% lack UniRef100 IDs, or carry UniParc-only (UPI-prefixed) identifiers with no AlphaFold entry. [src: alphafold_msa_annotation] (Here ID means identifier, and MSA means multiple sequence alignment.)

The report says this coverage is not random. Well-characterised organisms with reference proteomes, such as E. coli, Pseudomonas and Bacillus, are over-represented in UniProt. [src: alphafold_msa_annotation] It therefore suggests the annotation gap for the remaining 70.7% is likely larger. [src: alphafold_msa_annotation] The 71% without AlphaFold entries skews toward poorly characterised organisms. [src: alphafold_msa_annotation] Only clusters with a non-UPI UniProt accession are included. [src: alphafold_msa_annotation]

Sampling adds further bias. The 293K genomes are phylogenetically imbalanced, with Pseudomonas and E. coli over-represented, which influences core gene counts and MSA depth distributions. [src: alphafold_msa_annotation] MSA depth is also looked up only for each cluster's representative sequence. That ignores within-cluster diversity, and the representative may be higher or lower than the typical member. [src: alphafold_msa_annotation] The AlphaFold database is a single version-6 snapshot, so newly deposited UniProt entries may change MSA depths. [src: alphafold_msa_annotation]

## Resolution varies with phylogeny and reference quality

Organisms with better-annotated reference genomes and stronger Fitness Browser coverage had higher resolution rates. [src: annotation_gap_discovery]

| Organism | Gaps | Resolved | Rate |
|---|---|---|---|
| K. michiganensis (Koxy) | 7 | 5 | 71.4% [src: annotation_gap_discovery] |
| Marinobacter (Marino) | 12 | 8 | 66.7% [src: annotation_gap_discovery] |
| Azospirillum brasilense (azobra) | 21 | 13 | 61.9% [src: annotation_gap_discovery] |
| Herbaspirillum seropedicae (HerbieS) | 17 | 10 | 58.8% [src: annotation_gap_discovery] |
| E. coli Keio (Keio) | 7 | 4 | 57.1% [src: annotation_gap_discovery] |
| B. thetaiotaomicron (Btheta) | 15 | 3 | 20.0% [src: annotation_gap_discovery] |

The report links the lowest resolution to the divergent Bacteroidetes metabolism of B. thetaiotaomicron and its phylogenetic distance from the proteobacterial majority. [src: annotation_gap_discovery] This is a single clade, so it is a suggestion. The sole Bacteroidetes had the lowest rate, which suggests the approach may work less well for distant clades with divergent metabolism. [src: annotation_gap_discovery] The selection is also biased: 12 of 14 organisms are Proteobacteria, which limits generalizability. [src: annotation_gap_discovery] Gene fitness significance depends on the |fitness| threshold and experiment count, and organisms with fewer carbon source experiments have less statistical power. [src: annotation_gap_discovery] The report proposes that extending the pipeline to all 48 Fitness Browser organisms would increase statistical power for pangenome co-occurrence analysis and may resolve additional gaps through phylogenetic proximity. [src: annotation_gap_discovery]

## Dark genes and database representation

Dark-gene burden also tracks annotation depth. Some Fitness Browser species have >35% hypothetical genes and others <15%. The report attributes this to annotation depth rather than true functional content. [src: functional_dark_matter] The 24.9% dark gene fraction aligns with published estimates of 25–40% hypothetical genes in typical bacterial genomes. [src: functional_dark_matter] The dark-gene count (57,011) likely overestimates uncharacterized genes, because databases not checked may annotate some of them. [src: functional_dark_matter] Some bakta hypothetical-protein calls may be false negatives that failed to match the PSC database version tested (v6.0). [src: truly_dark_genes]

Truly dark genes are concentrated in a few organisms. Methanococcus strains S2 and JJ account for 55% of truly dark genes. [src: truly_dark_genes] The report attributes this to archaeal proteins being systematically underrepresented in reference databases compared to bacteria. [src: truly_dark_genes] It argues that even the annotation-lag category underestimates true novelty in archaea. [src: truly_dark_genes] See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]] for that distinction.

## Open Directions

- Re-estimate the gap with genomes resampled to equal taxa (for example one per genus). This would show how far Pseudomonas and E. coli over-representation shifts core gene counts and MSA depth.
- Compare annotation and MSA depth for clusters with and without UniProt accessions, stratified by phylum. This would test whether the uncovered 70.7% really has a larger gap.
- Extend the resolution pipeline to all 48 Fitness Browser organisms and add non-Proteobacteria. This would test whether the low Bacteroides rate reflects phylogenetic distance.
- Compute MSA depth for several members per cluster, not only the representative. This would measure the representative bias.
- Re-check "hypothetical" calls against UniProt, InterPro and newer Bakta databases. This would measure over-counting of dark genes, especially in archaea.
