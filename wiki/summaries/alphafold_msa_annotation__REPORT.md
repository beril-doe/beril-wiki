---
type: "Summary"
description: "Summary of the project AlphaFold MSA Depth as a Lens on the Bacterial Annotation Gap."
doc_type: "short"
full_text: "sources/alphafold_msa_annotation__REPORT.md"
---
# AlphaFold MSA Depth as a Lens on the Bacterial Annotation Gap

This page summarises a project that asked whether AlphaFold multiple sequence alignment (MSA) depth tracks how well bacterial genes are annotated, and where the gaps lie. The main answer is that MSA depth is a strong proxy for annotation richness. Core genes are far deeper than accessory genes, and a subset of 415,603 core clusters is both conserved and structurally unprecedented. [src: alphafold_msa_annotation] At pangenome scale (293K species, 132M gene clusters), the annotation gap is not uniform. It is concentrated in accessory genes and in a specific subset of highly conserved core genes. [src: alphafold_msa_annotation] The evidence is large-scale and direct, but it covers only the 28.7% of gene clusters that bridge to AlphaFold, which is biased toward well-studied taxa. [src: alphafold_msa_annotation]

## Key Findings

### Core genes have deeper MSAs than accessory genes

Core clusters sit well above accessory clusters in MSA depth, and the gap is largest at the low end. The report reads this as the expected result of long-term purifying selection in core genomes. [src: alphafold_msa_annotation]

- Core: n = 25,571,299 clusters, median 15,308, p10 334, p90 19,500, very low (< 10) 415,733 (1.6%), hypothetical 979,912 (3.8%). [src: alphafold_msa_annotation]
- Aux non-singleton: n = 5,384,900, median 5,527, p10 32, p90 19,192, very low 245,002 (4.6%), hypothetical 622,748 (11.6%). [src: alphafold_msa_annotation]
- Aux + singleton: n = 7,095,643, median 5,299, p10 25, p90 19,203, very low 392,959 (5.5%), hypothetical 979,300 (13.8%). [src: alphafold_msa_annotation]

The core median is 2.89× the auxiliary+singleton median and 2.77× the auxiliary non-singleton median. [src: alphafold_msa_annotation] The 10th-percentile depth is 334 for core genes and 25–32 for accessory genes. [src: alphafold_msa_annotation] The report concludes that even the worst-represented core genes are better characterised than the typical accessory gene. [src: alphafold_msa_annotation] It calls this pattern consistent with the pangenomics view that core genes do housekeeping and accessory genes carry adaptive traits. [src: alphafold_msa_annotation]

### MSA depth tracks domain annotation richness

Across 38,051,842 gene cluster–UniProt pairs, MSA depth and domain hit count correlate strongly (Spearman ρ = 0.756; 0.7563 in the full result). [src: alphafold_msa_annotation] This correlation was computed on the full 38M-pair dataset without subgroup stratification. [src: alphafold_msa_annotation] The report expects it to differ between core and accessory genes, and between organisms with narrow and broad annotation gaps. [src: alphafold_msa_annotation] The report treats the two measures as nearly interchangeable indicators of how deeply a protein is embedded in existing knowledge. [src: alphafold_msa_annotation] It explains this by noting that detectable relatives in sequence databases are the proteins whose study produced the Pfam, Gene3D, SUPERFAMILY and PANTHER domain profiles. [src: alphafold_msa_annotation] The report contrasts this with the conventional view of MSA depth as a structural confidence metric. [src: alphafold_msa_annotation]

Core clusters by MSA depth bin, with mean domain hits and mean distinct IPR families:
- < 10: 415,733 clusters, 0.59 hits, 0.059 IPR. [src: alphafold_msa_annotation]
- 10–99: 1,143,785 clusters, 0.96 hits, 0.242 IPR. [src: alphafold_msa_annotation]
- 100–999: 2,301,137 clusters, 1.95 hits, 0.852 IPR. [src: alphafold_msa_annotation]
- 1,000–4,999: 3,126,558 clusters, 3.72 hits, 1.843 IPR. [src: alphafold_msa_annotation]
- 5,000–9,999: 2,591,011 clusters, 5.62 hits, 2.664 IPR. [src: alphafold_msa_annotation]
- ≥ 10,000: 15,993,075 clusters, 10.83 hits, 4.601 IPR. [src: alphafold_msa_annotation]

The report describes an 18× span in mean domain hits from the lowest to the highest bin, and concludes that MSA depth is a reliable proxy for functional annotation richness. [src: alphafold_msa_annotation] The monotone trend holds within core, auxiliary non-singleton and auxiliary+singleton classes. Core genes show slightly higher domain richness at equivalent depth. [src: alphafold_msa_annotation]

Domain annotation reaches further than the AlphaFold bridge. In all, 111,035,431 clusters (83.8%) have at least one domain annotation, with mean hits of 7.5 and mean distinct IPR families of 3.3. [src: alphafold_msa_annotation] The report reads this as showing that sequence-profile annotation reaches further into sequence space than structural homology. [src: alphafold_msa_annotation]

### Paradox proteins: conserved but structurally unprecedented

The report calls bacterial core genes that are universally conserved yet structurally unprecedented "paradox proteins". [src: alphafold_msa_annotation] The census holds 415,603 distinct core clusters with msa_depth < 10, spanning 14,768 species clades, with mean/median MSA depth 4.57 / 4.0. [src: alphafold_msa_annotation] The report calls this its most scientifically actionable finding. [src: alphafold_msa_annotation]

Few of these proteins have functional assignments [src: alphafold_msa_annotation]:
- 286,439 (68.9%) are hypothetical. [src: alphafold_msa_annotation]
- 137 (0.033%) are EC-annotated (EC = Enzyme Commission). [src: alphafold_msa_annotation]
- 346 (0.083%) are KEGG-mapped. [src: alphafold_msa_annotation]

The 68.9% hypothetical rate compares with 3.8% for core genes overall. [src: alphafold_msa_annotation] The report describes these genes as conserved across thousands of lineages yet almost unknown at sequence, structure or biochemical level. [src: alphafold_msa_annotation]

The report interprets the features this way:
- Presence in the majority of genomes within each clade implies strong purifying selection and likely important function. [src: alphafold_msa_annotation]
- Depth under 10 means fewer than 10 detectable homologs in the AlphaFold training set, so the fold is unprecedented in available databases. [src: alphafold_msa_annotation]
- Their depth of 1–9 sets them apart from typical dark proteins that merely lack relatives through divergence. [src: alphafold_msa_annotation]
- They are structurally isolated from characterised protein space. [src: alphafold_msa_annotation]
- Deep conservation makes them better candidates for experimental structure work than random hypothetical proteins, which may be spurious ORFs or species-specific. [src: alphafold_msa_annotation]

The top-ranked entries at msa_depth = 1 come mainly from poorly characterised marine and soil bacteria (Oceanicoccus, Dwaynesavagella, CAILRJ01). [src: alphafold_msa_annotation] Non-hypothetical entries at that depth include an RNA (ribonucleic acid) polymerase ω-subunit family protein [src: alphafold_msa_annotation] and an FXSXX-COOH domain protein. [src: alphafold_msa_annotation] The report describes both as conserved structural components with no solved structure for these lineages. [src: alphafold_msa_annotation]

The top-1000 list (core genes with msa_depth = 1–9) is offered as a prioritised list for structural genomics consortia such as SGC and JCSG. [src: alphafold_msa_annotation] The report names the top candidates as targets for cryo-EM or AlphaFold-guided experimental determination. [src: alphafold_msa_annotation] More generally, it proposes MSA depth as a way to separate tractable high-depth proteins, whose predictions are reliable, from novel low-depth proteins, whose predictions are uncertain and which most need experimental determination. [src: alphafold_msa_annotation] It frames the need by citing Tunyasuvunakool et al. (2021): only 17% of human protein residues were covered by experimental structures before AlphaFold, and it describes bacteria as similar. [src: alphafold_msa_annotation]

### Resolving the core-versus-accessory tension (H2)

Core genes are less often hypothetical than accessory genes. Chi-square tests give χ² > 500,000 and p ≈ 0, with odds ratios of 0.25 (core vs. aux+singleton) and 0.31 (core vs. aux non-singleton). [src: alphafold_msa_annotation] The report says this appears to contradict H2 as literally stated. It says the paradox census resolves the tension. [src: alphafold_msa_annotation]

Its resolution names two drivers of the annotation gap [src: alphafold_msa_annotation]:
- An MSA-depth-driven gap applies to all classes and explains the 18× span in domain hits. [src: alphafold_msa_annotation]
- A pangenome-class gap means accessory and singleton genes carry more hypothetical proteins independent of depth. The report tentatively attributes this to horizontal transfer, rapid evolution and narrow taxonomic distribution. [src: alphafold_msa_annotation]

Within core genes, the depth-driven gap applies strongly to the paradox subset but not to most core genes, which have high depth and rich annotation. [src: alphafold_msa_annotation] The report reads the structural novelty signal as present within every pangenome class. The cross-class comparison is dominated by core genes' higher average depth. [src: alphafold_msa_annotation]

## Data and Methods

The analysis starts from 132,531,501 gene clusters in kbase_ke_pangenome.gene_cluster. [src: alphafold_msa_annotation] It uses the KBase Data Lakehouse kbase_ke_pangenome tables gene_cluster, bakta_annotations and interproscan_domains for cluster classification, annotation quality, a UniRef100 bridge and domain hits. [src: alphafold_msa_annotation] MSA depth per UniProt accession comes from the kescience_alphafold table alphafold_msa_depths. [src: alphafold_msa_annotation] Of the clusters, 38,804,903 (29.3%) have a real UniProt accession via bakta_annotations.uniref100. [src: alphafold_msa_annotation] A total of 38,051,842 (28.7%) bridge to kescience_alphafold.alphafold_msa_depths. [src: alphafold_msa_annotation] The remaining 70.7% lack UniRef100 identifiers (IDs) or carry UniParc-only UPI-prefixed IDs with no AlphaFold entry. [src: alphafold_msa_annotation] The report says earlier work had not quantified the core–accessory gradient at structural-novelty resolution with 241M AlphaFold entries. [src: alphafold_msa_annotation] It places the work against the AlphaFold Protein Structure Database and its 2025 update, which cover hundreds of millions of predicted structures. [src: alphafold_msa_annotation] It also cites Schaeffer et al. (2026), who found more than 100,000 domains without Pfam mapping in AFDB Swiss-Prot entries. [src: alphafold_msa_annotation]

## Caveats and Open Work

- The 29.3% UniProt coverage is not random. Well-characterised organisms such as E. coli, Pseudomonas and Bacillus are over-represented, so the analysis is biased toward better-studied diversity. [src: alphafold_msa_annotation] Only gene clusters with a non-UPI UniProt accession are included. [src: alphafold_msa_annotation]
- The 71% of clusters without AlphaFold entries skew toward poorly characterised organisms and likely harbour a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation] The report suggests the gap for the remaining 70.7% is likely larger. [src: alphafold_msa_annotation]
- MSA depth is looked up for the cluster representative only, so within-cluster diversity is ignored and the representative may be higher or lower than the typical member. [src: alphafold_msa_annotation]
- The 293K genomes are phylogenetically imbalanced, with Pseudomonas and E. coli over-represented. This influences core gene counts and MSA depth distributions. [src: alphafold_msa_annotation]
- The AlphaFold database in the KBase Data Lakehouse is a single version-6 snapshot, and newly deposited UniProt entries may change MSA depths as databases grow. [src: alphafold_msa_annotation]
- The report's attribution of the accessory hypothetical excess to horizontal transfer, rapid evolution and narrow taxonomic distribution is tentative ("likely"). [src: alphafold_msa_annotation]
- The report calls the paradox proteins prime candidates for experimental structural characterisation. [src: alphafold_msa_annotation]

Next analyses the report proposes:
- Run the MSA-depth–domain-richness test (H3) separately for core, auxiliary and singleton clusters, to see whether the gradient is steeper in one class. [src: alphafold_msa_annotation]
- Compare ESM pLDDT with AlphaFold MSA depth for the same clusters. ESMFold does not use MSA depth, so it gives an orthogonal structural novelty signal. [src: alphafold_msa_annotation] The comparison would find proteins novel in sequence space but potentially foldable without homologs. [src: alphafold_msa_annotation]
- Map the 415K paradox clusters onto the GTDB phylogeny to find the phyla and families with the highest densities of conserved-yet-novel proteins. [src: alphafold_msa_annotation]
- Join the paradox list to kescience_fitnessbrowser fitness scores, where available, to find proteins essential for growth in at least one condition. That would be experimental evidence of function without annotation. [src: alphafold_msa_annotation]

## Slots Into

- [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes]]: the 415,603 paradox clusters have 68.9% hypothetical rate versus 3.8% for core overall. [src: alphafold_msa_annotation]
- [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]]: core median MSA depth is 15,308 against 5,299 for aux+singleton. [src: alphafold_msa_annotation]
- [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]]: only 28.7% of clusters bridge to AlphaFold, biased toward well-studied taxa. [src: alphafold_msa_annotation]
