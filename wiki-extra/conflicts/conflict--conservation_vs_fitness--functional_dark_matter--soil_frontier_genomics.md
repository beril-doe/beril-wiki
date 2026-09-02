<!-- tension-hash: b5ec41b8a9188ac1 -->
# Is microbial “darkness” a sampling gap, a recovery gap, or a biological novelty gap?

The tension in [[concepts/functional-dark-matter]] is whether apparent under-representation reflects where researchers sampled, how successfully genomes were assembled and annotated, or genuinely unknown biology. The GDI pattern, dark-gene results, conservation analysis, and functional-priority rankings each identify gaps, but they measure different stages of the evidence pipeline and may not support the same interpretation.

## Evidence Sides

**GDI as evidence of under-representation**

The GDI pattern is consistent with under-representation of alkaline-soil microbiomes, but reverse causality remains unresolved because lower genome representation could result from fewer 16S samples rather than from assembly or annotation difficulty. [src: soil_frontier_genomics] The report therefore does not establish whether the observed gap is primarily a sampling gap, a genome-recovery gap, or an annotation gap. [src: soil_frontier_genomics] The GDI formulation can identify locations combining high OTU richness with low mean completeness, but its value is not a pure measure of discovery deficit because richness and completeness are combined in one ratio. [src: soil_frontier_genomics]

**Residual unknown genes as evidence of an annotation gap**

Among linked dark genes, 6,427 remained hypothetical after Bakta, but 17,479 unlinked genes could not be assessed, and Bakta can produce false-negative functional calls. [src: truly_dark_genes] Thus, the measured residual annotation gap is not interchangeable with the total biological novelty in public genomes. [src: truly_dark_genes]

**Fitness and functional-priority results as coverage-limited evidence**

Essentiality calls come from RB-TnSeq, a random-barcode transposon sequencing approach, under represented library-construction and growth conditions, and pangenome coverage varies among clades. [src: conservation_vs_fitness] Essential-unmapped genes may therefore reflect missing linkage or divergent core functions, but the analysis cannot distinguish these explanations universally. [src: conservation_vs_fitness] In addition, 37 of 48 Fitness Browser organisms were Pseudomonadota, and none of the top 500 candidates came from Archaea, Actinobacteria, or Epsilonproteobacteria. [src: functional_dark_matter] The extended 50-organism covering set reached 98.7% of ortholog groups across 6 phyla but lacked Fitness Browser condition profiles for its non-Fitness-Browser organisms. [src: functional_dark_matter]

## Possible Reconciliations

- **Hypothesis — layered gaps:** Sampling scarcity, genome-recovery failure, and annotation failure may all contribute, with their relative importance varying by habitat and clade.
- **Hypothesis — metric decomposition:** High GDI may identify a combination of ecological richness and incomplete genomic coverage without being a direct measure of biological novelty.
- **Hypothesis — linked-versus-unlinked bias:** The 6,427 assessed hypothetical genes and 17,479 unassessed unlinked genes may represent different evidence regimes rather than additive measures of darkness.
- **Hypothesis — condition-dependent function:** Fitness priorities may be real under tested conditions while remaining unrepresentative of dark biology in taxa lacking Fitness Browser profiles.

## Resolving Work

- Pair 16S sampling density, isolate/metagenome availability, assembly statistics, and annotation quality by site to test which component explains GDI differences.
- Reassemble and reannotate the same genomes with multiple assemblers and annotation pipelines to separate genome-recovery gaps from false-negative functional calls.
- Link the 17,479 unlinked genes through improved assemblies, synteny, and pangenomes, then compare their functional resolution with the 6,427 linked genes.
- Repeat RB-TnSeq or complementary perturbation assays across additional growth conditions and clades to test whether essential-unmapped status is stable.
- Expand Fitness Browser condition profiles beyond the 37 of 48 Pseudomonadota-heavy organisms and evaluate whether the top 500 candidates change with broader taxonomic coverage.
