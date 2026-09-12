# Gazi S. Mahmud

ORCID: [0009-0006-4046-889X](https://orcid.org/0009-0006-4046-889X)

## Contributions

The [[summaries/alphafold_msa_annotation__REPORT]] evaluated AlphaFold multiple-sequence-alignment (MSA) depth as a proxy for functional annotation richness across bacterial pangenome gene clusters by joining `kbase_ke_pangenome`, `bakta_annotations`, `interproscan_domains`, and `kescience_alphafold`. [src: alphafold_msa_annotation] It found that 38,804,903 of 132,531,501 gene clusters (29.3%) had a real UniProt accession and 38,051,842 (28.7%) bridged successfully to AlphaFold MSA depths, while 70.7% lacked UniRef100 identifiers or an AlphaFold entry. [src: alphafold_msa_annotation] The project also found that 111,035,431 clusters (83.8%) had at least one InterProScan domain annotation, exceeding AlphaFold bridge coverage. [src: alphafold_msa_annotation]

The [[summaries/alphafold_msa_annotation__REPORT]] compared MSA depth and annotation patterns across pangenome classes and found median depths of 15,308 for core clusters, 5,299 for auxiliary+singleton clusters, and 5,527 for auxiliary non-singleton clusters. [src: alphafold_msa_annotation] It found hypothetical-protein rates of 3.8% in core clusters, 11.6% in auxiliary non-singleton clusters, and 13.8% in auxiliary+singleton clusters, with chi-square statistics above 500,000 and odds ratios of 0.25 for core versus auxiliary+singleton and 0.31 for core versus auxiliary non-singleton. [src: alphafold_msa_annotation] Across 38,051,842 gene cluster–UniProt pairs, the project reported a Spearman correlation of ρ = 0.7563 between MSA depth and domain-hit count, with mean domain hits increasing from 0.59 at MSA depth < 10 to 10.83 at MSA depth ≥ 10,000. [src: alphafold_msa_annotation]

The [[summaries/alphafold_msa_annotation__REPORT]] identified 415,603 distinct core clusters with MSA depth < 10 across 14,768 species clades and found that 286,439 (68.9%) were hypothetical, while 137 (0.033%) were EC-annotated and 346 (0.083%) were KEGG-mapped. [src: alphafold_msa_annotation] It interpreted these clusters as candidates for experimental structural characterization because they were conserved by pangenome classification but isolated from characterized sequence space, while explicitly treating that interpretation as a prioritization hypothesis rather than direct experimental validation. [src: alphafold_msa_annotation]

## Projects (1)

- [[summaries/alphafold_msa_annotation__REPORT|alphafold_msa_annotation]]
