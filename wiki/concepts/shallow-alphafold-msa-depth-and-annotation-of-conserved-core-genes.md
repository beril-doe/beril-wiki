---
type: "Concept"
description: "Covers how AlphaFold multiple-sequence-alignment (MSA) depth relates to annotation richness (InterPro hits and families) across pangenome classes, including universally conserved but unannotated core genes with shallow MSAs; stops short of experimental characterisation of function."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/pitfalls.md"]
---
# Shallow AlphaFold MSA depth and annotation of conserved core genes

Across 38,051,842 bacterial gene cluster–UniProt pairs, multiple-sequence-alignment (MSA) depth and domain-hit count are strongly correlated (Spearman ρ = 0.756). [src: alphafold_msa_annotation] Core clusters are deeper than accessory ones. [src: alphafold_msa_annotation] A subset of 415,603 core clusters has msa_depth < 10 and is mostly unannotated. [src: alphafold_msa_annotation] The correlation was computed without subgroup stratification. [src: alphafold_msa_annotation] The source report is summarised in [[summaries/alphafold_msa_annotation__REPORT]].

## MSA depth tracks annotation richness

The full correlation is ρ = 0.7563. [src: alphafold_msa_annotation] This is a [[entities/spearman-rank-correlation]] on [[entities/interproscan-domain-annotation]] hits. The report calls MSA depth and domain hits nearly interchangeable measures of how deeply a protein is embedded in existing knowledge. [src: alphafold_msa_annotation] Its explanation is that MSA depth counts detectable relatives, and those relatives generated the domain profiles in Pfam, Gene3D, SUPERFAMILY and PANTHER. [src: alphafold_msa_annotation] This is an interpretation, not a test.

The report presents AlphaFold MSA depth as conventionally a structural confidence metric, where higher depth gives higher pLDDT. [src: alphafold_msa_annotation] It argues that depth is also a reliable proxy for annotation richness. [src: alphafold_msa_annotation]

Mean domain hits and distinct InterPro (IPR) families rise with core-cluster MSA depth bin:

| MSA depth bin | Core clusters | Mean domain hits | Mean distinct IPR |
|---|---|---|---|
| < 10 | 415,733 | 0.59 | 0.059 [src: alphafold_msa_annotation] |
| 10–99 | 1,143,785 | 0.96 | 0.242 [src: alphafold_msa_annotation] |
| 100–999 | 2,301,137 | 1.95 | 0.852 [src: alphafold_msa_annotation] |
| 1,000–4,999 | 3,126,558 | 3.72 | 1.843 [src: alphafold_msa_annotation] |
| 5,000–9,999 | 2,591,011 | 5.62 | 2.664 [src: alphafold_msa_annotation] |
| ≥ 10,000 | 15,993,075 | 10.83 | 4.601 [src: alphafold_msa_annotation] |

The report describes an 18× span in mean domain hits from the lowest to the highest bin. [src: alphafold_msa_annotation] The monotone relationship holds within core, auxiliary non-singleton and auxiliary+singleton clusters. Core genes show slightly higher domain richness at equivalent depth. [src: alphafold_msa_annotation]

Overall, 111,035,431 bacterial gene clusters (83.8% of all clusters) have at least one domain annotation. [src: alphafold_msa_annotation] Those clusters average 7.5 hits and 3.3 distinct IPR families. [src: alphafold_msa_annotation] The report reads this coverage as higher than the AlphaFold bridge coverage (29.3%). It concludes that sequence-profile domain annotation reaches further into sequence space than structural homology. [src: alphafold_msa_annotation]

## Pangenome classes

Core clusters have a median MSA depth of 15,308. That is 2.89× the auxiliary+singleton median of 5,299 and 2.77× the auxiliary non-singleton median of 5,527. [src: alphafold_msa_annotation] The report takes this as the expected result of long-term purifying selection in core genomes, which gives more relatives and better database representation. [src: alphafold_msa_annotation] The gap is largest at the low end: the 10th-percentile depth is 334 for core genes and 25–32 for accessory genes. [src: alphafold_msa_annotation]

| Class | n clusters | Median depth | p10 | p90 | Very low (< 10) | Hypothetical |
|---|---|---|---|---|---|---|
| Core | 25,571,299 | 15,308 | 334 | 19,500 | 415,733 (1.6%) | 979,912 (3.8%) [src: alphafold_msa_annotation] |
| Aux non-singleton | 5,384,900 | 5,527 | 32 | 19,192 | 245,002 (4.6%) | 622,748 (11.6%) [src: alphafold_msa_annotation] |
| Aux + singleton | 7,095,643 | 5,299 | 25 | 19,203 | 392,959 (5.5%) | 979,300 (13.8%) [src: alphafold_msa_annotation] |

The report separates two drivers of the annotation gap. The MSA-depth-driven gap applies to all classes and explains the 18× span. [src: alphafold_msa_annotation] The pangenome-class gap means accessory and singleton genes carry more hypothetical proteins independent of depth. The report tentatively attributes this to horizontal transfer, rapid evolution and narrow taxonomic distribution. [src: alphafold_msa_annotation] This resolves the apparent contradiction that core genes have lower hypothetical rates yet harbour 415K structurally unprecedented proteins. [src: alphafold_msa_annotation] The depth-driven gap applies strongly to the shallow core subset (68.9% hypothetical) but not to most core genes, which have deep MSAs and rich annotation. [src: alphafold_msa_annotation] See also [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

## Conserved but unannotated: "paradox proteins"

The report calls core genes that are universally conserved yet structurally unprecedented "paradox proteins". [src: alphafold_msa_annotation] The census has 415,603 distinct bacterial core clusters with msa_depth < 10 [src: alphafold_msa_annotation], spanning 14,768 species clades. [src: alphafold_msa_annotation] Their mean and median MSA depth are 4.57 and 4.0. [src: alphafold_msa_annotation] The report states they have msa_depth = 1–9. [src: alphafold_msa_annotation] It calls this its most scientifically actionable finding. [src: alphafold_msa_annotation]

Their annotation is sparse. 286,439 (68.9%) are hypothetical [src: alphafold_msa_annotation], against 3.8% for core genes overall. [src: alphafold_msa_annotation] Only 137 (0.033%) carry EC (Enzyme Commission) annotation [src: alphafold_msa_annotation], and 346 (0.083%) map to KEGG. [src: alphafold_msa_annotation] The report reads this as no function assigned by any standard informatic route. [src: alphafold_msa_annotation]

Several interpretations rest on this census:
- The genes are core in the majority of genomes in each of 14,768 species clades. The report infers strong purifying selection and likely important function. [src: alphafold_msa_annotation]
- Fewer than 10 detectable homologs in the AlphaFold training set means a genuinely unprecedented fold in available databases. [src: alphafold_msa_annotation]
- Unlike typical dark proteins, which may lack relatives through divergence, even deep homology searches find essentially nothing. [src: alphafold_msa_annotation]
- The report calls them structurally isolated from all characterised protein space [src: alphafold_msa_annotation], and says they are conserved across thousands of lineages yet almost unknown at sequence, structure or biochemical level. [src: alphafold_msa_annotation]

The top proteins at msa_depth = 1 come mainly from poorly characterised marine and soil bacteria (*Oceanicoccus*, *Dwaynesavagella*, *CAILRJ01*). [src: alphafold_msa_annotation] Non-hypothetical entries at that depth include an RNA (ribonucleic acid) polymerase ω-subunit family protein [src: alphafold_msa_annotation] and an FXSXX-COOH domain protein. [src: alphafold_msa_annotation] The report describes both as conserved structural components with no solved structure for these lineages. [src: alphafold_msa_annotation] For related dark-gene work, see [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]] and [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]].

## Uses proposed by the report

The report proposes MSA depth as a way to separate tractable high-depth proteins, whose structure predictions are reliable, from novel low-depth ones that most need experimental determination. [src: alphafold_msa_annotation] It prioritises paradox proteins for experimental structural work, because deep conservation implies function, unlike random hypothetical proteins that may be spurious ORFs or species-specific. [src: alphafold_msa_annotation] Its data/paradox_top1000.csv lists core genes with msa_depth = 1–9 for structural genomics consortia such as SGC and JCSG. [src: alphafold_msa_annotation] It names the top candidates as targets for cryo-EM or AlphaFold-guided determination. [src: alphafold_msa_annotation] A separate pitfalls note says about 9% of kescience_alphafold entries have MSA depth < 30 (low-confidence predictions). It recommends filtering by msa_depth for structure-based analyses. [src: pitfalls] See [[entities/alphafold-protein-structure-database]].

## Further analyses the report proposes

The report proposes running the MSA-depth–domain-richness test separately for core, auxiliary and singleton clusters, to see whether the gradient is steeper in one class. [src: alphafold_msa_annotation] It notes that [[entities/esmfold]] does not use MSA depth and so gives an orthogonal structural novelty signal. [src: alphafold_msa_annotation] It proposes comparing ESM pLDDT with AlphaFold MSA depth for the same clusters, to find proteins novel in sequence space but potentially foldable without homologs. [src: alphafold_msa_annotation] It proposes mapping the 415K paradox clusters onto the GTDB phylogeny, to find phyla and families with the highest densities of conserved-yet-novel proteins. [src: alphafold_msa_annotation] It also proposes joining the paradox list to kescience_fitnessbrowser fitness scores, where available. This would find paradox proteins essential for growth in at least one condition, which is experimental evidence of function without annotation. [src: alphafold_msa_annotation]

## Caveats

The ρ = 0.756 was computed on the full 38M-pair dataset without subgroup stratification. [src: alphafold_msa_annotation] The report expects the correlation to differ between core and accessory genes, and between organisms with narrow and broad annotation gaps. [src: alphafold_msa_annotation]

## Open Directions

- Compute per-class correlations (core, auxiliary, singleton) to close the stratification gap in the pooled ρ.
- Compare ESMFold pLDDT with MSA depth on the same clusters to separate sequence novelty from foldability.
- Map the paradox clusters onto GTDB to locate lineages enriched for conserved-yet-novel proteins.
- Join the paradox list to Fitness Browser fitness data to find essential members and give them first functional evidence.
