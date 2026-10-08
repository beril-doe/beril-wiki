---
type: "Summary"
description: "Summary of the conservation_vs_fitness project, which links Fitness Browser essentiality calls to KBase pangenome clusters across 33 bacteria and finds a modest enrichment of putative essential genes in core clusters."
doc_type: "short"
full_text: "sources/conservation_vs_fitness__REPORT.md"
---
# Conservation vs Fitness — Linking FB Genes to Pangenome Clusters

## Overview

This report links Fitness Browser (FB) gene-level fitness and essentiality data to KBase pangenome clusters, testing whether genes required for viability are preferentially conserved across bacterial species. It mapped 44 of 48 FB organisms to pangenome species clades and analyzed essentiality versus core, auxiliary, and unmapped conservation categories across 33 organisms. [src: conservation_vs_fitness]

## Key Findings

### Pangenome Linkage and Conservation

The Phase 1 link table mapped 44 of 48 FB organisms to pangenome species clades, producing 177,863 gene-to-cluster links with 100.0% median protein identity and 94.2% median gene coverage. Thirty-four organisms had >=90% coverage, and 33 were used for downstream analysis because Dyella79 was excluded for a locus-tag mismatch. Four organisms—Cola, Kang, Magneto, and SB2B—were unmatched because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness]

Of the linked genes, 145,821 (82.0%) were in core clusters and 32,042 (18.0%) were auxiliary; the 7,574 singleton genes were a subset of the auxiliary category. [src: conservation_vs_fitness]

### Essential Genes and Core Conservation

The analysis identified 27,693 putative essential genes among 148,826 protein-coding genes across 33 organisms, representing 18.6% overall and ranging from 12.9-28.9% per organism. Essentiality was inferred from RB-TnSeq, a random-barcode transposon sequencing approach, under the library construction and growth conditions represented in the Fitness Browser. [src: conservation_vs_fitness]

Essential genes were 86.1% core compared with 81.2% for non-essential genes, with a median odds ratio of 1.56 for essential-gene enrichment in the core genome. Eighteen of 33 organisms showed statistically significant enrichment by Fisher's exact test after Benjamini-Hochberg false discovery rate correction (BH-FDR q < 0.05). The strongest signals were Methanococcus maripaludis S2 (OR=5.21), Ralstonia syzygii PSI07 (OR=3.41), and Marinobacter adhaerens (OR=3.08). [src: conservation_vs_fitness]

This result supports the expectation that viability-required genes are generally conserved within species, but the enrichment is modest, consistent with most genes in well-characterized bacteria being core regardless of essentiality. [src: conservation_vs_fitness]

### Functional Profiles by Conservation and Essentiality

The essential-core category contained 22,751 genes, of which 41.9% were enzymes and 13.0% were hypothetical; essential-auxiliary contained 3,683 genes, of which 13.4% were enzymes and 38.2% were hypothetical; essential-unmapped contained 1,259 genes, of which 18.2% were enzymes and 44.7% were hypothetical; and the non-essential category contained 124,744 genes, of which 21.5% were enzymes and 24.5% were hypothetical. [src: conservation_vs_fitness]

Essential-core genes were the most enzyme-rich and best-annotated category, with 87% having known function. Relative to non-essential genes, they were enriched in Protein Metabolism by +13.7 percentage points, Cofactors/Vitamins by +6.2%, Cell Wall by +3.9%, and Fatty Acid biosynthesis by +3.1%; they were depleted in Carbohydrates by -7.9%, Amino Acids by -5.6%, and Membrane Transport by -4.0%. The report infers that these depleted functions tend to be conditionally important rather than universally essential; this is an interpretation, not a separately tested finding. [src: conservation_vs_fitness]

The 3,683 essential-auxiliary genes, which were essential for viability but not present in all strains, were poorly characterized (38.2% hypothetical) and less likely to be enzymes (13.4%). Their leading subsystems included ribosomes, DNA replication, type 4 secretion, and plasmid replication, which the report tentatively interprets as strain-specific variants of core machinery together with mobile genetic elements. [src: conservation_vs_fitness]

The 1,259 essential-unmapped genes, strain-specific essentials with no pangenome cluster match, were the least characterized category, with 44.7% hypothetical. Their known functions included divergent ribosomal proteins L34, L36, S11, and S12, translation factors, transposases, and DNA-binding proteins, consistent with the hypothesis that some are recently acquired or highly divergent variants of core functions. [src: conservation_vs_fitness]

### Validation and Context

Gene-length validation found that essential genes were slightly shorter on average, consistent with insertion bias in transposon data. Clade-size and lifestyle stratification indicated that essential-core enrichment was robust across the diverse genomic contexts examined. [src: conservation_vs_fitness]

The report relates the three categories—essential-core, essential-auxiliary, and essential-unmapped—to the universal-essential, core-strain-specific-essential, and accessory-essential categories described by Rosconi et al. (2022) in 36 Streptococcus pneumoniae strains, while extending the comparison across 33 diverse bacterial species. [src: conservation_vs_fitness]

The finding that 44.7% of essential-unmapped genes were hypothetical parallels the observation from Hutchison et al. (2016) that a designed minimal Mycoplasma genome of 473 genes contained 149 essential genes (31%) with unknown function; the Mycoplasma result is secondary literature context, not a finding of this project. [src: conservation_vs_fitness]

The analysis addresses gene-length bias concerns raised for transposon-based essentiality calls by Goodall et al. (2018), who used TraDIS to define the E. coli K-12 essential genome, uses the genome-wide mutant-fitness data generated by Price et al. (2018), and adds a pangenome-conservation dimension to those fitness measurements. [src: conservation_vs_fitness]

## Caveats

The essential-gene definition is an upper bound: genes without fitness data may lack transposon insertions because they are short, occur in low-complexity regions, or lie at scaffold edges, rather than because they are essential. Gene-length validation found that essential genes were slightly shorter on average, indicating possible insertion bias. [src: conservation_vs_fitness]

Pangenome coverage varies among clades, and clades containing only 2 genomes can have trivially high core fractions because a gene present in both genomes equals 100% core, reducing the discriminative power of the core-versus-auxiliary classification. [src: conservation_vs_fitness]

The main Escherichia coli clade was absent from the pangenome because it contained too many genomes; Keio, an E. coli BW25113 strain, mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness]

Essentiality was measured under a single growth condition represented by the RB-TnSeq library construction conditions, so genes essential only under stress conditions were not captured. [src: conservation_vs_fitness]

Dyella79 was excluded from Phase 2 because the FB gene table used the locus-tag format N515DRAFT_* whereas the protein sequences used ABZR86_RS*, producing a 0% join rate. [src: conservation_vs_fitness]

Ten organisms were excluded from Phase 2 because they had <90% DIAMOND coverage, reducing taxonomic breadth. [src: conservation_vs_fitness]

## Future Directions

The report proposes extending the analysis from binary essentiality to condition-specific fitness, especially genes with fitness < -2 under stress conditions, to test whether conditionally important genes have different conservation patterns. [src: conservation_vs_fitness]

It also proposes using FB ortholog data to identify essential gene families conserved across multiple species, correlating mean fitness effects rather than only essential/non-essential status with core-genome fraction, and characterizing the 3,683 essential-auxiliary genes to determine whether they compensate for missing core functions. [src: conservation_vs_fitness]

## Data Sources and Outputs

The project drew on the Fitness Browser gene table, described as ~221K genes across 48 bacteria (Price et al. 2018); KBase pangenome clusters, described as 132.5M gene clusters across 27,690 species (Parks et al. 2022); DIAMOND blastp, a protein similarity search used for gene-to-cluster mapping (Buchfink et al. 2015); and SEED annotations, which supplied functional-category assignments (Overbeek et al. 2014). [src: conservation_vs_fitness]

The generated essentiality-classification file `data/essential_genes.tsv` is described as containing 153,143 genes. This count differs from the report's 148,826-protein-coding-gene denominator, and the 124,744-gene non-essential row of the category table is also reported separately from that denominator. The report does not reconcile these counts. [src: conservation_vs_fitness]

Figures produced by the project [src: conservation_vs_fitness]:
- `figures/identity_distributions.png` — DIAMOND identity distributions per organism.
- `figures/conservation_breakdown.png` — core, auxiliary, and singleton breakdown per organism.
- `figures/essential_vs_core_forest_plot.png` — forest plot of essential-versus-core odds ratios across organisms.
- `figures/essential_length_validation.png` — gene-length validation of essentiality calls.
- `figures/essential_enrichment_by_context.png` — enrichment stratified by clade size and openness.
- `figures/essential_enrichment_by_lifestyle.png` — essential-core enrichment stratified by lifestyle.
- `figures/essential_enzyme_breakdown.png` — enzyme classification by essentiality/conservation category.
- `figures/essential_seed_toplevel_heatmap.png` — heatmap of top-level SEED functional categories.

## Slots Into

- [[concepts/gene-essentiality]] — links essentiality calls to core, auxiliary, and unmapped pangenome conservation, including the 1.56 median odds ratio and essential-auxiliary category. [src: conservation_vs_fitness]
- [[concepts/pangenome-integration]] — provides a 177,863-link integration between Fitness Browser genes and KBase pangenome clusters, with explicit coverage and unmatched-organism limitations. [src: conservation_vs_fitness]
- [[concepts/genomic-under-representation]] — shows that essential-unmapped genes are 44.7% hypothetical and essential-auxiliary genes are 38.2% hypothetical, identifying poorly characterized essential functions. [src: conservation_vs_fitness]
- [[concepts/pangenome-conservation-fitness-decoupling]] — the essential-core association is real but modest (OR=1.56; 18 of 33 organisms significant), because most genes are core regardless of essentiality. [src: conservation_vs_fitness]
- [[concepts/core-gene-annotation-paradox]] — essential-core genes are the best-annotated category (13.0% hypothetical), while essential-auxiliary genes (38.2% hypothetical) and essential-unmapped genes (44.7% hypothetical) are less well characterized. [src: conservation_vs_fitness]
- [[concepts/transposon-callability-bias]] — the essential-gene definition is an upper bound, and putative essential genes are slightly shorter, consistent with insertion bias. [src: conservation_vs_fitness]
- [[concepts/pangenome-core-boundary-and-clade-size-bias]] — two-genome clades yield trivially high core fractions; the report states that enrichment held across clade-size strata. [src: conservation_vs_fitness]
- [[concepts/essentiality-assay-discordance]] — a gene can lack insertions because it is short, sits in a low-complexity region or lies at a scaffold edge, not only because it is essential. [src: conservation_vs_fitness]
- [[concepts/condition-specific-fitness]] — essentiality calls reflect library-construction conditions and miss genes essential only under stress. [src: conservation_vs_fitness]
- [[concepts/two-speed-bacterial-genome]] — essential-auxiliary genes include ribosome, DNA replication, type 4 secretion, and plasmid-replication subsystems. The report tentatively interprets these as strain-specific variants of core machinery plus mobile elements. [src: conservation_vs_fitness]
