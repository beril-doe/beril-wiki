---
type: "Summary"
description: "Summary of the project The 5,526 Costly + Dispensable Genes."
doc_type: "short"
full_text: "sources/costly_dispensable_genes__REPORT.md"
---
# The 5,526 Costly + Dispensable Genes

This report asks what the 5,526 genes are that are costly (fitness improves when deleted) and dispensable (not conserved in the pangenome). Its main answer is that they are overwhelmingly associated with mobile genetic elements. [src: costly_dispensable_genes] It suggests they are mostly mobile-element debris from horizontal gene transfer (HGT), not degrading metabolic pathways. [src: costly_dispensable_genes]

## Key Findings

**Mobile-element identity.** Keyword and SEED enrichment tests agree that costly+dispensable genes are mobile-element related. [src: costly_dispensable_genes] These genes are 7.45x more likely than costly+conserved genes to contain mobile-element keywords such as transposase, integrase, phage, IS element, recombinase and prophage (OR=7.45, p=4.6e-71; OR = odds ratio). [src: costly_dispensable_genes] The SEED category "Phages, Prophages, Transposable elements, Plasmids" is 11.7x enriched (FDR=1.3e-17; FDR = false discovery rate). [src: costly_dispensable_genes] "Virulence" is 26.7x enriched (FDR=5.6e-14). [src: costly_dispensable_genes] This rests on small counts of 21 vs 4 genes. [src: costly_dispensable_genes] In these genes, 14 SEED top-level categories are significantly depleted (FDR < 0.05), including Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response, and RNA Metabolism. [src: costly_dispensable_genes] The report finds that the genes are almost exclusively mobile-element debris rather than degrading metabolic pathways. It suggests that HGT-mediated genome expansion is the primary source of costly non-conserved genes in bacteria. [src: costly_dispensable_genes] It describes them as insertion sequences, prophage remnants, transposases and defense systems. [src: costly_dispensable_genes]

**Hallmarks of recent acquisition.** The report interprets these genes as having the hallmarks of recently acquired DNA (deoxyribonucleic acid). [src: costly_dispensable_genes] It states its hypotheses H2 and H3 as confirmed. [src: costly_dispensable_genes]

- Annotation: 50.8% have SEED annotations vs 74.9% for costly+conserved. [src: costly_dispensable_genes]
- KEGG coverage is 20.0% vs 42.7%. [src: costly_dispensable_genes]
- Orphans: 44.5% are orphan genes (no ortholog group) vs 13.1% for costly+conserved. [src: costly_dispensable_genes]
- Ortholog breadth: the median number of organisms sharing the ortholog group is 15 vs 31 (Mann-Whitney p=4.0e-99, rank-biserial r=0.233). [src: costly_dispensable_genes]
- Singletons: 24.2% are found in only 1 genome, and no costly+conserved genes are singletons. [src: costly_dispensable_genes]
- The singleton contrast is partly structural, because core genes cannot be singletons by definition. [src: costly_dispensable_genes]
- Within dispensable genes, costly genes are only slightly more likely than neutral genes to be singletons (OR=1.09, p=0.02). [src: costly_dispensable_genes]
- Length: median 615 bp vs 765 bp (p=4.2e-75, rank-biserial r=0.170), consistent with IS elements and gene fragments. [src: costly_dispensable_genes]

**Contrast with costly+conserved genes.** The report counts 28,017 costly+conserved genes. [src: costly_dispensable_genes] They are enriched in Protein Metabolism, Respiration and Motility. The report reads these as costly functions kept by purifying selection in natural environments the lab does not capture. [src: costly_dispensable_genes] It also says their lab-measured burden is offset by natural selection. [src: costly_dispensable_genes]

**Per-organism outlier.** *Pseudomonas stutzeri* RCH2 is the organism the report designates psRCH2. [src: costly_dispensable_genes] It has 21.5% of its genes in the costly+dispensable class, above the next organism, *B. thetaiotaomicron*, at 14.0%. [src: costly_dispensable_genes] The report suggests a recent mobile-element invasion or strain-specific genomic expansion. [src: costly_dispensable_genes] It also cautions that this may reflect strain-specific features rather than a general pattern. [src: costly_dispensable_genes] See [[entities/pseudomonas-stutzeri-rch2]].

**Residual phenotypes and fate.** Despite the burden, 14.1% of costly+dispensable genes have condition-specific phenotypes, vs 16.7% for costly+conserved genes. [src: costly_dispensable_genes] Neutral+dispensable genes have 2.7%. The report suggests the costly+dispensable genes are therefore not inert, which may slow their loss. [src: costly_dispensable_genes] It proposes that these genes are candidates for ongoing gene loss unless they give an environment-specific advantage. [src: costly_dispensable_genes] It suggests a subset may persist if the triggering conditions are met often enough. [src: costly_dispensable_genes] It also suggests they may be early stages of genome degradation. [src: costly_dispensable_genes] Armitage et al. (2025) documented extreme pseudogenization and gene loss in symbiotic cyanobacteria, with genome degradation accompanying relaxed selection. [src: costly_dispensable_genes] The report treats the genes as Black Queen candidates, but they are mostly selfish elements, not metabolic genes, and may precede actual gene loss. [src: costly_dispensable_genes] The Black Queen Hypothesis (Morris et al. 2012) describes loss of costly genes whose functions community members supply as public goods. [src: costly_dispensable_genes]

**Novelty claims.** The report claims the first systematic characterization of genes that are both burdensome and not pangenome-conserved. [src: costly_dispensable_genes] It claims novelty in its scale of 142,190 genes across 43 bacteria and in its pangenome dimension. [src: costly_dispensable_genes] Price et al. (2018) generated the Fitness Browser data used here. [src: costly_dispensable_genes] The report adds pangenome conservation to separate evolutionarily stable from transient phenotypic genes. [src: costly_dispensable_genes] It cites Rosconi et al. (2022) for strain-dependent gene essentiality in *S. pneumoniae*, with the accessory genome modulating which genes are required. [src: costly_dispensable_genes]

## Data and Methods

The analysis uses the KBase Data Lakehouse collections kescience_fitnessbrowser (genefitness, gene, exps) [src: costly_dispensable_genes] and kbase_ke_pangenome (gene_cluster, gene_genecluster_junction, eggnog_mapper_annotations). [src: costly_dispensable_genes] The resulting table, gene_quadrants.tsv, has 142,190 genes with fitness statistics, conservation status and quadrant assignment. [src: costly_dispensable_genes] See [[entities/gene-quadrant-dataset]].

## Caveats and Open Work

Caveats:

- Burden is defined as max_fit > 1 in any experiment, so one experiment can classify a gene as burdensome, which makes the result sensitive to noise. [src: costly_dispensable_genes]
- SEED/KEGG annotations cover only 56-79% of genes, and unannotated genes may differ functionally. [src: costly_dispensable_genes]
- The core/auxiliary classification is binary. [src: costly_dispensable_genes]
- The 90% identity DIAMOND threshold for linking may miss recently acquired genes with low similarity. [src: costly_dispensable_genes]
- Ortholog groups use bidirectional best hit (BBH) across 48 organisms, so genes with orthologs outside the set would be misclassified as orphans. [src: costly_dispensable_genes]
- Condition-specific phenotype data are biased toward lab-testable conditions. [src: costly_dispensable_genes]

Proposed next analyses:

- Explain the psRCH2 outlier, which has 21.5% costly+dispensable genes. [src: costly_dispensable_genes]
- Ask whether it is a recent phage invasion, IS element expansion, or genomic island acquisition. [src: costly_dispensable_genes]
- Test whether these genes cluster in genomic islands, near tRNA genes or at scaffold edges, which are hallmarks of HGT. [src: costly_dispensable_genes]
- Track the genes across multiple sequenced strains and close relatives to see whether they are being lost. [src: costly_dispensable_genes]
- Use ENIGMA CORAL community data to test whether organisms with more of these genes co-occur with organisms that could supply the lost functions. [src: costly_dispensable_genes]
- Replace the binary classification with the fraction of species genomes carrying each gene cluster. [src: costly_dispensable_genes]

## Slots Into

- mobile element origin of costly non conserved genes: costly+dispensable genes are enriched for mobile-element keywords (OR=7.45) and the SEED phage/transposon category (11.7x). [src: costly_dispensable_genes]
- [[concepts/gene-loss-and-black-queen-hypothesis-tests]]: the genes are proposed as candidates for ongoing loss, but they are mostly selfish elements. [src: costly_dispensable_genes]
- [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]]: costly+conserved genes are enriched in core functions such as Protein Metabolism, Respiration and Motility. [src: costly_dispensable_genes]
- [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]]: the report suggests HGT-mediated expansion is the primary source of costly non-conserved genes. [src: costly_dispensable_genes]
