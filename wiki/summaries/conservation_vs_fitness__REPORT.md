---
type: "Summary"
description: "Summary of the project Conservation vs Fitness -- Linking FB Genes to Pangenome Clusters."
doc_type: "short"
full_text: "sources/conservation_vs_fitness__REPORT.md"
---
# Conservation vs Fitness -- Linking FB Genes to Pangenome Clusters

This report asks whether genes that are essential in Fitness Browser (FB) mutant screens are more likely to sit in the core genome of their species' pangenome. It links FB genes to pangenome clusters, then compares essential and non-essential genes. Essential genes are modestly more often core (86.1% vs 81.2%), and the enrichment is significant in 18 of 33 organisms. The report also lists several limits on how essentiality was defined. [src: conservation_vs_fitness]

## Key Findings

### Linking FB genes to pangenome clusters

The mapping covered most FB organisms and produced a large link table. 44 of 48 FB organisms mapped to pangenome species clades. [src: conservation_vs_fitness] The mapping produced 177,863 gene-to-cluster links at 100.0% median protein identity and 94.2% median gene coverage. [src: conservation_vs_fitness] Four organisms did not match: Cola, Kang, Magneto and SB2B, because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness]

Of the mapped organisms, 34 have >=90% coverage and 33 were used downstream. Dyella79 was excluded for a locus tag mismatch. [src: conservation_vs_fitness] The mismatch was between FB gene-table tags N515DRAFT_* and protein-sequence tags ABZR86_RS*, which gave a 0% join rate. [src: conservation_vs_fitness] The linked genes comprise 145,821 core (82.0%) and 32,042 auxiliary (18.0%) genes. That count includes 7,574 singletons, which are a subset of the auxiliary genes. [src: conservation_vs_fitness] See [[concepts/linking-fitness-assay-genes-to-pangenome-clusters]].

### Essential genes are modestly enriched in the core genome

The report found 27,693 putative essential genes. This is 18.6% of 148,826 protein-coding genes across 33 organisms, with a per-organism range of 12.9-28.9%. [src: conservation_vs_fitness] Essential genes are 86.1% core, against 81.2% for non-essential genes. [src: conservation_vs_fitness] The median odds ratio (OR) is 1.56, so essential genes are 1.56x more likely to be in the core genome. [src: conservation_vs_fitness] Enrichment was significant in 18 of 33 organisms by Fisher's exact test with Benjamini-Hochberg false discovery rate (BH-FDR) q < 0.05. [src: conservation_vs_fitness]

The strongest signals were in *Methanococcus maripaludis* S2 (OR=5.21), *Ralstonia syzygii* PSI07 (OR=3.41) and *Marinobacter adhaerens* (OR=3.08). [src: conservation_vs_fitness] Stratifying by clade size and lifestyle shows the enrichment is robust across diverse genomic contexts. [src: conservation_vs_fitness] The report reads the modest size of the effect as showing that most genes in well-characterized bacteria are core regardless of essentiality. [src: conservation_vs_fitness] See [[concepts/essential-genes-and-core-genome-conservation]].

### Function of essential-core, essential-auxiliary and essential-unmapped genes

Genes fall into four categories that differ sharply in enzyme content and annotation.

- Essential-core: 22,751 genes, 41.9% enzymes, 13.0% hypothetical. [src: conservation_vs_fitness]
- Essential-auxiliary: 3,683 genes, 13.4% enzymes, 38.2% hypothetical. [src: conservation_vs_fitness]
- Essential-unmapped: 1,259 genes, 18.2% enzymes, 44.7% hypothetical. [src: conservation_vs_fitness]
- Non-essential: 124,744 genes, 21.5% enzymes, 24.5% hypothetical. [src: conservation_vs_fitness]

Essential-core genes are the most enzyme-rich category and the best annotated, with 87% having known function. [src: conservation_vs_fitness] Against non-essential genes they are enriched in Protein Metabolism (+13.7 percentage points), Cofactors/Vitamins (+6.2%), Cell Wall (+3.9%) and Fatty Acid biosynthesis (+3.1%). [src: conservation_vs_fitness] They are depleted in Carbohydrates (-7.9%), Amino Acids (-5.6%) and Membrane Transport (-4.0%). The report describes these functions as tending to be conditionally important rather than universally essential. [src: conservation_vs_fitness] Functional categories come from SEED annotations. [src: conservation_vs_fitness]

Essential-auxiliary genes are essential for viability but not present in all strains. [src: conservation_vs_fitness] Their top subsystems are ribosomes, DNA replication, type 4 secretion and plasmid replication. The report suggests this reflects strain-specific variants of core machinery plus mobile genetic elements. [src: conservation_vs_fitness]

Essential-unmapped genes are strain-specific essentials with no pangenome cluster match, and are the least characterized category. [src: conservation_vs_fitness] Known functions include divergent ribosomal proteins L34, L36, S11 and S12, translation factors, transposases and DNA-binding proteins. The report interprets these as likely recently acquired or highly divergent variants of core functions. [src: conservation_vs_fitness]

### Relation to published work

The report cites Rosconi et al. (2022), who studied essentiality across 36 *S. pneumoniae* strains and found that the pan-genome makes essentiality strain-dependent. [src: conservation_vs_fitness] Their "universal essential", "core strain-specific essential" and "accessory essential" classes parallel the report's three essential categories. The report says it extends the concept across 33 diverse bacterial species. [src: conservation_vs_fitness] It also cites Hutchison et al. (2016), a minimal *Mycoplasma* genome of 473 genes in which 149 essential genes (31%) had unknown function. [src: conservation_vs_fitness] Goodall et al. (2018) used TraDIS to define the *E. coli* K-12 essential genome and noted that gene-length biases can affect transposon-based essentiality calls. [src: conservation_vs_fitness] Price et al. (2018) generated the FB data used here, demonstrating genome-wide mutant fitness across 32 bacteria. [src: conservation_vs_fitness]

## Data and Methods

The inputs were the FB gene table (~221K genes across 48 bacteria, Price et al. 2018) and KBase pangenome clusters (132.5M gene clusters across 27,690 species, Parks et al. 2022). [src: conservation_vs_fitness] Genes were mapped to clusters with DIAMOND blastp (Buchfink et al. 2015). [src: conservation_vs_fitness] See [[entities/diamond]] and [[entities/fitness-browser]]. The outputs were an organism mapping covering 44 organisms, a link table of 177,863 rows and essentiality classifications for 153,143 genes. [src: conservation_vs_fitness] The final link table is data/fb_pangenome_link.tsv with 177,863 rows, and the essentiality classification file is data/essential_genes.tsv with 153,143 genes. [src: conservation_vs_fitness]

## Caveats and Open Work

- The essential-gene definition is an upper bound. Genes without fitness data may lack insertions because they are short, in low-complexity regions or at scaffold edges, not because they are essential. [src: conservation_vs_fitness] Essential genes are also slightly shorter on average, consistent with some transposon insertion bias. [src: conservation_vs_fitness] See [[concepts/limits-of-transposon-based-essentiality-calls]].
- Essentiality from random barcode transposon sequencing (RB-TnSeq) is defined under the library-construction conditions. Genes essential only under stress would be missed. [src: conservation_vs_fitness]
- Clades with only 2 genomes have trivially high core fractions, which reduces core/auxiliary discrimination. [src: conservation_vs_fitness]
- *E. coli* was excluded because its main clade was absent from the pangenome (too many genomes). Keio (E. coli BW25113) mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness]
- Phase 2 excluded 10 organisms with <90% DIAMOND coverage, which reduced taxonomic breadth. [src: conservation_vs_fitness]
- The enrichment is modest (median OR 1.56) and significant in only 18 of 33 organisms. [src: conservation_vs_fitness]

Proposed next steps:
- Test whether genes important under specific stress conditions (fitness < -2) show different conservation patterns. [src: conservation_vs_fitness]
- Use FB ortholog data to find essential gene families conserved across species. [src: conservation_vs_fitness]
- Correlate mean fitness effect with core-genome fraction, rather than using only the essential/non-essential split. [src: conservation_vs_fitness]
- Characterize the 3,683 essential-auxiliary genes more deeply, asking whether they compensate for missing core functions. [src: conservation_vs_fitness]

## Slots Into

- [[concepts/essential-genes-and-core-genome-conservation]]: essential genes are 86.1% core vs 81.2% for non-essential genes, with a median OR of 1.56. [src: conservation_vs_fitness]
- [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality]]: essential-core genes are 41.9% enzymes, while essential-auxiliary and essential-unmapped genes are 38.2% and 44.7% hypothetical. [src: conservation_vs_fitness]
- [[concepts/linking-fitness-assay-genes-to-pangenome-clusters]]: 44 of 48 organisms mapped, giving 177,863 links. [src: conservation_vs_fitness]
- [[concepts/limits-of-transposon-based-essentiality-calls]]: the essential definition is an upper bound, and essential genes are slightly shorter. [src: conservation_vs_fitness]
