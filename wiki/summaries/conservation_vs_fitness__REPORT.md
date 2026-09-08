---
type: Summary
description: Links bacterial gene essentiality to pangenome conservation across 33
  organisms.
doc_type: short
full_text: ../sources/conservation_vs_fitness__REPORT.md
title: Conservation vs Fitness — Linking FB Genes to Pangenome Clusters
sources:
- id: conservation_vs_fitness
  resource: ../sources/conservation_vs_fitness__REPORT.md
  title: conservation vs fitness
---
# Conservation vs Fitness — Linking FB Genes to Pangenome Clusters

## Overview

This report links Fitness Browser (FB) gene-level fitness and essentiality data to KBase pangenome clusters, testing whether genes required for viability are preferentially conserved across bacterial species. It mapped 44 of 48 FB organisms to pangenome species clades and analyzed essentiality versus core, auxiliary, and unmapped conservation categories across 33 organisms. [^conservation_vs_fitness]

## Key Findings

### Pangenome Linkage and Conservation

The Phase 1 link table mapped 44 of 48 FB organisms to pangenome species clades, producing 177,863 gene-to-cluster links with 100.0% median protein identity and 94.2% median gene coverage. Thirty-four organisms had >=90% coverage, and 33 were used for downstream analysis because Dyella79 was excluded for a locus-tag mismatch. Four organisms—Cola, Kang, Magneto, and SB2B—were unmatched because their species had too few genomes in GTDB for pangenome construction. [^conservation_vs_fitness]

Of the linked genes, 145,821 (82.0%) were in core clusters and 32,042 (18.0%) were auxiliary; the 7,574 singleton genes were a subset of the auxiliary category. [^conservation_vs_fitness]

### Essential Genes and Core Conservation

The analysis identified 27,693 putative essential genes among 148,826 protein-coding genes across 33 organisms, representing 18.6% overall and ranging from 12.9-28.9% per organism. Essentiality was inferred from RB-TnSeq, a random-barcode transposon sequencing approach, under the library construction and growth conditions represented in the Fitness Browser. [^conservation_vs_fitness]

Essential genes were 86.1% core compared with 81.2% for non-essential genes, with a median odds ratio of 1.56; thus, essential genes were 1.56x more likely to occur in the core genome. Eighteen of 33 organisms showed statistically significant enrichment by Fisher's exact test after Benjamini-Hochberg false discovery rate correction (BH-FDR q < 0.05). The strongest signals were Methanococcus maripaludis S2 (OR=5.21), Ralstonia syzygii PSI07 (OR=3.41), and Marinobacter adhaerens (OR=3.08). [^conservation_vs_fitness]

This result supports the expectation that viability-required genes are generally conserved within species, but the enrichment is modest, consistent with most genes in well-characterized bacteria being core regardless of essentiality. [^conservation_vs_fitness]

### Functional Profiles by Conservation and Essentiality

The essential-core category contained 22,751 genes, of which 41.9% were enzymes and 13.0% were hypothetical; essential-auxiliary contained 3,683 genes, of which 13.4% were enzymes and 38.2% were hypothetical; essential-unmapped contained 1,259 genes, of which 18.2% were enzymes and 44.7% were hypothetical; and the non-essential category contained 124,744 genes, of which 21.5% were enzymes and 24.5% were hypothetical. [^conservation_vs_fitness]

Essential-core genes were the most enzyme-rich and best-annotated category, with 87% having known function. Relative to non-essential genes, they were enriched in Protein Metabolism by +13.7 percentage points, Cofactors/Vitamins by +6.2%, Cell Wall by +3.9%, and Fatty Acid biosynthesis by +3.1%; they were depleted in Carbohydrates by -7.9%, Amino Acids by -5.6%, and Membrane Transport by -4.0%. [^conservation_vs_fitness]

Essential-auxiliary genes were poorly characterized and less likely to be enzymes; their leading subsystems included ribosomes, DNA replication, type 4 secretion, and plasmid replication, suggesting strain-specific variants of core machinery together with mobile genetic elements. [^conservation_vs_fitness]

Essential-unmapped genes were the least characterized category, with 44.7% hypothetical. Their known functions included divergent ribosomal proteins L34, L36, S11, and S12, translation factors, transposases, and DNA-binding proteins, consistent with the hypothesis that some are recently acquired or highly divergent variants of core functions. [^conservation_vs_fitness]

### Validation and Context

Gene-length validation found that essential genes were slightly shorter on average, consistent with insertion bias in transposon data. Clade-size and lifestyle stratification indicated that essential-core enrichment was robust across the diverse genomic contexts examined. [^conservation_vs_fitness]

The report relates the three categories—essential-core, essential-auxiliary, and essential-unmapped—to the universal-essential, core-strain-specific-essential, and accessory-essential categories described by Rosconi et al. (2022) in 36 Streptococcus pneumoniae strains, while extending the comparison across 33 diverse bacterial species. [^conservation_vs_fitness]

The finding that 44.7% of essential-unmapped genes were hypothetical parallels the observation from Hutchison et al. (2016) that 149 of 473 genes in a designed minimal Mycoplasma genome were essential and had unknown function. [^conservation_vs_fitness]

The analysis addresses gene-length bias concerns raised for transposon-based essentiality calls by Goodall et al. (2018), uses the genome-wide mutant-fitness data generated by Price et al. (2018), and adds a pangenome-conservation dimension to those fitness measurements. [^conservation_vs_fitness]

## Caveats

The essential-gene definition is an upper bound: genes without fitness data may lack transposon insertions because they are short, occur in low-complexity regions, or lie at scaffold edges, rather than because they are essential. Gene-length validation found that essential genes were slightly shorter on average, indicating possible insertion bias. [^conservation_vs_fitness]

Pangenome coverage varies among clades, and clades containing only 2 genomes can have trivially high core fractions because a gene present in both genomes equals 100% core, reducing the discriminative power of the core-versus-auxiliary classification. [^conservation_vs_fitness]

The main Escherichia coli clade was absent from the pangenome because it contained too many genomes; Keio, an E. coli BW25113 strain, mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [^conservation_vs_fitness]

Essentiality was measured under a single growth condition represented by the RB-TnSeq library construction conditions, so genes essential only under stress conditions were not captured. [^conservation_vs_fitness]

Dyella79 was excluded from Phase 2 because the FB gene table used the locus-tag format N515DRAFT_* whereas the protein sequences used ABZR86_RS*, producing a 0% join rate. [^conservation_vs_fitness]

Ten organisms were excluded from Phase 2 because they had <90% DIAMOND coverage, reducing taxonomic breadth. [^conservation_vs_fitness]

## Future Directions

The report proposes extending the analysis from binary essentiality to condition-specific fitness, especially genes with fitness < -2 under stress conditions, to test whether conditionally important genes have different conservation patterns. [^conservation_vs_fitness]

It also proposes using FB ortholog data to identify essential gene families conserved across multiple species, correlating mean fitness effects rather than only essential/non-essential status with core-genome fraction, and characterizing the 3,683 essential-auxiliary genes to determine whether they compensate for missing core functions. [^conservation_vs_fitness]

## Slots Into

- [gene-essentiality](../concepts/gene-essentiality.md) — links essentiality calls to core, auxiliary, and unmapped pangenome conservation, including the 1.56 median odds ratio and essential-auxiliary category. [^conservation_vs_fitness]
- [pangenome-integration](../concepts/pangenome-integration.md) — provides a 177,863-link integration between Fitness Browser genes and KBase pangenome clusters, with explicit coverage and unmatched-organism limitations. [^conservation_vs_fitness]
- [functional-dark-matter](../concepts/functional-dark-matter.md) — shows that essential-unmapped genes are 44.7% hypothetical and essential-auxiliary genes are 38.2% hypothetical, identifying poorly characterized essential functions. [^conservation_vs_fitness]

[^conservation_vs_fitness]: [conservation vs fitness](../sources/conservation_vs_fitness__REPORT.md)
