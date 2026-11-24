# Gazi S. Mahmud

ORCID: [0009-0006-4046-889X](https://orcid.org/0009-0006-4046-889X)

## Contributions

The project [[summaries/alphafold_msa_annotation__REPORT]] examined whether AlphaFold multiple sequence alignment (MSA) depth tracks bacterial annotation richness. It used 132,531,501 gene clusters from the KBase Data Lakehouse table kbase_ke_pangenome.gene_cluster. [src: alphafold_msa_annotation] Of these, 38,051,842 (28.7%) bridge to kescience_alphafold.alphafold_msa_depths. The report notes that this subset is biased toward well-studied taxa. [src: alphafold_msa_annotation]

Core genes had deeper MSAs than accessory genes. The core median was 15,308 (n = 25,571,299), against 5,299 for auxiliary+singleton clusters (n = 7,095,643) and 5,527 for auxiliary non-singleton clusters (n = 5,384,900). [src: alphafold_msa_annotation] The 10th-percentile depth was 334 for core genes and 25–32 for accessory genes. [src: alphafold_msa_annotation] Hypothetical rates were 3.8% for core, 11.6% for auxiliary non-singleton and 13.8% for auxiliary+singleton clusters. [src: alphafold_msa_annotation]

MSA depth correlated with domain annotation richness across 38,051,842 gene cluster–UniProt pairs (Spearman ρ = 0.756). This was computed without subgroup stratification. [src: alphafold_msa_annotation] Among core clusters, mean domain hits rose from 0.59 for depth < 10 to 10.83 for depth ≥ 10,000. The report describes this as an 18× span. [src: alphafold_msa_annotation] Overall, 111,035,431 clusters (83.8%) had at least one domain annotation. [src: alphafold_msa_annotation]

The project also counted "paradox proteins", which are conserved core clusters with msa_depth < 10. The census found 415,603 distinct clusters spanning 14,768 species clades. Of these, 286,439 (68.9%) were hypothetical, 137 (0.033%) were EC-annotated and 346 (0.083%) were KEGG-mapped. [src: alphafold_msa_annotation] Chi-square tests gave odds ratios of 0.25 (core vs. aux+singleton) and 0.31 (core vs. aux non-singleton) for being hypothetical. The report says this appears to contradict hypothesis H2 as literally stated, and that the paradox census resolves the tension. [src: alphafold_msa_annotation] Its caveats are that MSA depth was looked up for the cluster representative only, and that the attribution of the accessory excess to horizontal transfer is tentative. [src: alphafold_msa_annotation]

## Projects (1)

- [[summaries/alphafold_msa_annotation__REPORT|alphafold_msa_annotation]]
