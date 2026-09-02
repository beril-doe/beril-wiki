<!-- tension-hash: bc7b30122a717dcd -->
# Is the genomic dark-matter gap real under-representation or a measurement artifact?
The disagreement concerns what the GDI pattern and related analyses actually demonstrate about genomic under-representation. The [[concepts/functional-dark-matter]] evidence is consistent with alkaline-soil microbiomes being under-represented, but it does not establish whether the gap arises from uneven sampling, difficulty recovering genomes, or limits in annotation. Because GDI combines richness and completeness, and because downstream analyses have their own coverage and assay limitations, interpreting the pattern as biological novelty rather than a measurement artifact remains contested.

## Evidence Sides

**Side 1 — GDI identifies likely under-represented microbiomes**

The GDI pattern is consistent with under-representation of alkaline-soil microbiomes. [src: soil_frontier_genomics] The GDI formulation can identify locations combining high OTU richness with low mean completeness. [src: soil_frontier_genomics] Together, these findings support using GDI to flag locations where observed microbial diversity is poorly represented by available genomes.

**Side 2 — The observed gap cannot yet be assigned to biological under-representation**

Reverse causality remains unresolved because lower genome representation could result from fewer 16S samples rather than from assembly or annotation difficulty. [src: soil_frontier_genomics] The report therefore does not establish whether the observed gap is primarily a sampling gap, a genome-recovery gap, or an annotation gap. [src: soil_frontier_genomics] GDI is not a pure measure of discovery deficit because richness and completeness are combined in one ratio. [src: soil_frontier_genomics] The component measurements therefore need to be reported separately before GDI differences are interpreted as differences in genomic under-representation. [src: soil_frontier_genomics]

The truly dark gene analysis refines rather than resolves this tension: among linked dark genes, 6,427 remained hypothetical after Bakta, but 17,479 unlinked genes could not be assessed, and Bakta can produce false-negative functional calls. [src: truly_dark_genes] The conservation analysis likewise cannot distinguish universally whether essential-unmapped genes reflect missing linkage or divergent core functions, because its essentiality calls come from RB-TnSeq under represented library-construction and growth conditions, and its pangenome coverage varies among clades. [src: conservation_vs_fitness]

## Possible Reconciliations

- **Hypothesis — Sampling and recovery can coexist:** alkaline-soil microbiomes may be genuinely under-represented, while fewer 16S samples and uneven genome recovery inflate or obscure the apparent size of the gap.
- **Hypothesis — GDI is a screening index, not a discovery measure:** high richness combined with low completeness may correctly prioritize locations for study without quantifying biological novelty.
- **Hypothesis — Annotation and linkage capture different deficits:** the 6,427 linked genes remaining hypothetical after Bakta may represent residual annotation difficulty, while the 17,479 unlinked genes reflect unresolved genome-context or recovery problems.
- **Hypothesis — Conservation is conditional:** essential-unmapped genes may be conserved functions missed by linkage, divergent core functions, or artifacts of the tested RB-TnSeq conditions rather than a single universal category.

## Resolving Work

- Compare standardized 16S sampling intensity, metagenome depth, assembly quality, and annotation rates across alkaline and non-alkaline sites; test whether the GDI pattern persists after sampling and sequencing effort are matched.
- Report richness, mean completeness, and their distributions separately, then model each component against GDI; test whether site rankings remain stable without the ratio.
- Reassemble and reannotate the 6,427 linked hypothetical genes and characterize the 17,479 unlinked genes using long reads, improved linkage, and multiple annotation tools; test how many functional calls are recovered.
- Replicate RB-TnSeq essentiality assays across library-construction conditions, growth conditions, and clades; test whether essential-unmapped classifications persist when pangenome coverage and experimental context are controlled.
