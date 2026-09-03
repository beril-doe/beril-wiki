<!-- tension-hash: b5ec41b8a9188ac1 -->
# Is the apparent genomic dark matter a sampling gap or a biological/annotation gap?

The disagreement concerns what the observed under-representation of microbial genomes actually measures. The [[concepts/functional-dark-matter]] material reports patterns consistent with missing alkaline-soil microbiomes and taxonomic coverage gaps, while also warning that the same patterns may arise from incomplete sampling, genome recovery, annotation, or the construction of the GDI metric itself. This matters because prioritizing “dark” biology depends on distinguishing genuinely undiscovered functions from artifacts of where organisms were sampled, how genomes were assembled, and which organisms have experimental fitness data.

## Evidence Sides

**Sampling and coverage side**

The GDI pattern is consistent with under-representation of alkaline-soil microbiomes, but reverse causality remains unresolved because lower genome representation could result from fewer 16S samples rather than from assembly or annotation difficulty. [src: soil_frontier_genomics] The functional-dark-matter analysis also found that 37 of 48 Fitness Browser organisms were Pseudomonadota, and none of the top 500 candidates came from Archaea, Actinobacteria, or Epsilonproteobacteria. [src: functional_dark_matter] This supports concern that apparent functional priorities may reflect condition and taxonomic coverage rather than the distribution of dark biology across microbes. [src: functional_dark_matter]

**Recovery, annotation, and metric side**

The report does not establish whether the observed gap is primarily a sampling gap, a genome-recovery gap, or an annotation gap. [src: soil_frontier_genomics] Although the GDI formulation can identify locations combining high OTU richness with low mean completeness, its value is not a pure measure of discovery deficit because richness and completeness are combined in one ratio. [src: soil_frontier_genomics] The truly dark gene analysis found that 6,427 remained hypothetical after Bakta, but 17,479 unlinked genes could not be assessed, and Bakta can produce false-negative functional calls. [src: truly_dark_genes] The conservation analysis further reports that essentiality calls come from RB-TnSeq under represented library-construction and growth conditions, while pangenome coverage varies among clades. [src: conservation_vs_fitness]

## Possible Reconciliations

- **Measurement hypothesis:** GDI may correctly flag locations with high richness and low completeness without being a direct measure of biological novelty; reporting richness and completeness separately could make both interpretations compatible. [src: soil_frontier_genomics]
- **Scope hypothesis:** A sampling gap may dominate alkaline-soil patterns, while annotation or genome-recovery gaps dominate the residual dark-gene set. The 6,427 hypothetical linked genes and 17,479 unlinked genes need not represent the same phenomenon. [src: truly_dark_genes]
- **Coverage hypothesis:** The 50-organism covering set reached 98.7% of ortholog groups across 6 phyla, but lacked Fitness Browser condition profiles for its non-Fitness-Browser organisms. Thus broad sequence coverage and narrow experimental coverage can coexist. [src: functional_dark_matter]
- **Definition hypothesis:** Essential-unmapped genes may reflect missing linkage or divergent core functions, but RB-TnSeq conditions and uneven pangenome coverage prevent universal distinction. [src: conservation_vs_fitness]

## Resolving Work

- Assemble and annotate matched samples from alkaline and non-alkaline soils at equal 16S depth; test whether the GDI gap persists after sampling effort is standardized.
- Recalculate GDI while reporting OTU richness, mean completeness, and their ratio separately; test which component predicts genome recovery and functional novelty.
- Apply multiple annotation tools and manual or transcript-supported validation to the 6,427 hypothetical genes, while separately tracking the 17,479 unlinked genes; measure false-negative and linkage effects.
- Expand Fitness Browser experiments across the missing taxa and conditions; test whether candidate rankings remain stable beyond Pseudomonadota and the existing condition profiles.
