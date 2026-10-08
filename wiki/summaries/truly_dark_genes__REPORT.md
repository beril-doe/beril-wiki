---
type: "Summary"
description: "Summary of the truly_dark_genes project, which separates Fitness Browser dark genes into annotation-lag, truly dark and unlinked sets after Bakta reannotation, characterizes the truly dark genes' structural, evolutionary and phenotypic properties, and ranks candidates for experimental characterization."
doc_type: "short"
full_text: "sources/truly_dark_genes__REPORT.md"
---
# Truly Dark Genes — What Remains Unknown After Modern Annotation?

## Overview

This project distinguishes genuinely unknown genes from annotation-lag genes by reannotating Fitness Browser dark genes with Bakta v1.12.0, integrating pangenome and functional-database evidence, testing genomic and phenotypic properties, and ranking candidates for experimental characterization. Of 57,011 dark genes, 39,532 had pangenome links that permitted assessment: 33,105 (83.7%) were reclassified by Bakta and 6,427 remained hypothetical in both pipelines. A further 17,479 dark genes lacked pangenome links and could not be assessed. [src: truly_dark_genes]

## Key Findings

### 1. Most dark genes are annotation-lag genes, but 6,427 remain truly dark

The census decomposed 57,011 Fitness Browser dark genes into 33,105 annotation-lag genes, 6,427 truly dark genes, and 17,479 unlinked genes. The truly dark set consists of genes called hypothetical by both the original Fitness Browser pipeline and Bakta; among the 39,532 linked genes, they represent 16.3%, while the unlinked genes have unknown Bakta status. Methanococcus strains S2 and JJ account for 55% of truly dark genes, and across organisms the fraction of dark genes resisting Bakta ranges from 4–96%, with archaeal organisms at the high end. The report's future-directions section phrases this share as archaea contributing 55% of truly dark genes, and its organism-distribution figure identifies Methanococcus as dominating truly dark gene counts. [src: truly_dark_genes]

### 2. Truly dark genes are structurally distinct from annotation-lag genes

Compared with annotation-lag genes, truly dark genes have a median length of 121 amino acids versus 194, a core-genome fraction of 43.1% versus 72.7%, an essential fraction of 18.0% versus 13.4%, mean GC content of 0.542 versus 0.584, ortholog presence of 29.3% versus 63.7%, and median ortholog breadth of 1 versus 4 organisms. The reported effect sizes are d = −0.432 for length, OR = 0.284 for core-genome fraction, OR = 1.420 for essential fraction, d = −0.395 for GC content, OR = 0.236 for ortholog presence, and d = −1.072 for ortholog breadth; the corresponding p-values are < 1e-100, < 1e-100, < 1e-10, 2e-115, < 1e-100, and < 1e-100, respectively. The report characterizes truly dark genes as shorter, less conserved, more taxonomically restricted, and lower in GC content, consistent with biological novelty rather than database lag. The report also asserts that all effects exceed pre-registered thresholds of Cohen's d ≥ 0.2 or OR ≥ 1.5, but its essential-fraction row reports OR = 1.420, so this assertion is internally inconsistent for that comparison. [src: truly_dark_genes]

### 3. Sequence databases recognize many genes but rarely assign function

Among truly dark genes, 79.4% have UniRef50 links and 84.7% have database cross-references, including RefSeq and UniParc, but only 4.0% have Pfam domain hits and 4.6% have KEGG KOs (KEGG Orthology identifiers, which assign genes to curated ortholog groups with known functions). eggNOG-mapper provides partial signal for 43.5% of truly dark clusters; only 17.0% have COG (Clusters of Orthologous Groups, a protein-family functional classification) categories, and 55.4% of COG assignments are in category S, meaning function unknown. The remaining COG assignments span L, M, K, T, C, and J without a dominant functional theme. The Key Findings present the 79.4%, 84.7%, 4.0% and 4.6% values as percentages of truly dark genes. The Results section instead places the 84.7% cross-reference, 4.0% Pfam and 4.6% KEGG-KO values under 5,870 unique truly dark gene clusters rather than all 6,427 genes. Those three values therefore use clusters as the denominator and should not be read as fractions of genes. [src: truly_dark_genes]

### 4. Most truly dark genes have partial clues

A 12-dimensional clue matrix found that 246 genes (3.8%) have zero annotation clues, while the remaining 96.2% have combinations of sequence identifiers, eggNOG hits, orthologs, module membership, and/or fitness phenotypes. The four reported tiers are Tier 1, no clues: 246 genes (3.8%); Tier 2, minimal sequence identifiers only: 3,867 (60.2%); Tier 3, partial function through Pfam, COG, or eggNOG: 711 (11.1%); and Tier 4, phenotype only, with fitness, essentiality, or module signal but no functional annotation: 1,603 (24.9%). Tier 3 and Tier 4 together contain 2,314 genes identified as the most promising for narrowing experimental hypotheses. [src: truly_dark_genes]

### 5. Accessory-genome and horizontal-transfer signatures support novelty

The report describes truly dark genes as "4.2× less likely" to have cross-organism orthologs (OR = 0.236; proportions 29.3% versus 63.7%). That phrase describes the odds ratio imprecisely and is not a 4.2-fold probability comparison. When orthologs exist, they span a median of 1 organism versus 4 for annotation-lag genes. Only 3 of 65 dark-gene ortholog groups with cross-organism concordance data contain truly dark genes. Mean absolute GC deviation from the host-genome mean is 0.047 for truly dark genes versus 0.038 for annotation-lag genes, with d = 0.247 and p = 1.3e-43; strong GC deviation, defined as |z| > 2, affects 9.2% versus 4.0%. In addition, 12.0% of truly dark genes are within 2 genes of a mobile genetic element, such as a transposase, integrase, or phage protein. These patterns are consistent with horizontal gene transfer (HGT), the movement of genetic material between organisms, contributing to annotation resistance, although GC deviation is an imperfect HGT proxy. The Results section limits the 12.0% mobile-element statistic to the 4,394 truly dark genes in organisms with independent component analysis (ICA) fitness-module data, not necessarily all 6,427. Mobile-element proximity supports horizontal transfer but does not establish it. [src: truly_dark_genes]

### 6. Stress enrichment was rejected

The report rejected the hypothesis that truly dark genes are enriched in stress conditions. For truly dark genes with strong fitness phenotypes, defined as |f| ≥ 2, one comparison reports stress conditions at 28.7% versus 43.2% for annotation-lag genes, with OR = 0.53 and p < 0.001. The results section separately reports stress at 43.3% versus 54.7%, carbon-source conditions at 13.7% versus 21.7%, and motility conditions at 1.2% versus 3.2%; it reports enrichment in mixed-community conditions (7.5% versus 0%), iron conditions (0.7% versus 0%), nutrient time-series conditions, and rich media. The interpretation suggests, rather than establishes, that truly dark genes may encode novel metabolic or community-interaction functions rather than stress responses. The report's discussion also proposes inter-species interaction functions, novel metabolic capabilities or community-specific behaviors that single-organism annotation databases represent poorly; these are hypotheses, not established gene functions. The two stress comparisons differ and the report does not reconcile them: 28.7% versus 43.2% in the Key Findings and 43.3% versus 54.7% in the Results. [src: truly_dark_genes]

### 7. Dark genes cluster in genomic neighborhoods and fitness modules

Among 4,394 truly dark genes in organisms with ICA data, 41% of neighboring genes are also hypothetical, 12.0% are within 2 genes of a mobile element, and 25.9% show operon-like cofitness with adjacent genes, using |r| ≥ 0.3. A total of 594 genes belong to ICA fitness modules; guilt-by-association analysis links these modules to candidate functions including phage integrases, metal transporters, chemotaxis systems, and iron regulation. The report interprets the 41% hypothetical-neighbor pattern as genomic "dark islands", which are contiguous regions of unknown function. It proposes three likely origins: recently acquired genomic islands, phage-derived regions and species-specific gene neighborhoods. None of these origins has been demonstrated. [src: truly_dark_genes]

### 8. One hundred candidates were prioritized

A multi-criteria score incorporating fitness importance, annotation clues, ortholog breadth, genomic context, and experimental tractability ranks all 6,427 truly dark genes on a maximum scale of 12 and identifies 100 top candidates with scores of 8–10 across 19 organisms. PV4/5210953 scores 10 and has a motility phenotype of |f| = 5.5, an operon association with TatC, and ICA module M016. ANA3/7026383 scores 9 and has a nitrogen-source phenotype of |f| = 8.6, an operon association with an ABC transporter, and ICA module M018. DvH/206658 scores 9 and has a stress phenotype of |f| = 5.4; eggNOG suggests “trehalose synthase” despite its hypothetical annotation. Methanococcus_S2/MMP_RS06570 scores 9 and has 8 annotation clues, including DUF190 and COG-T signal-transduction evidence, plus an operon association with fluoride-efflux transporter CrcB. [src: truly_dark_genes]

The top 100 candidates span 19 organisms; Methanococcus_S2 contributes 29, DvH 13, Methanococcus_JJ 13, and MR-1 8. Of the 100 candidates, 34 are essential, 53 are in operons, and 30 are in ICA fitness modules. The report estimates that approximately 2,841 additional truly dark genes may exist among the 17,479 unlinked dark genes at the 16.3% truly-dark rate, including 2,208 with strong fitness phenotypes, and states that the ranked list covers approximately 69% of the estimated total truly dark gene population. [src: truly_dark_genes]

### 9. Detailed annotation and orthology coverage remains sparse

Among 5,870 unique truly dark gene clusters, Pfam provides 362 hits for 235 clusters (4.0%), with TPR repeats dominating non-DUF hits and 56 clusters having DUF-only domains. Cross-reference data contain 26,917 entries for 4,971 clusters (84.7%), dominated by SO, UniRef, and UniParc identifiers, with only 6 KEGG entries and 1 EC number. eggNOG provides 2,551 annotations for 2,551 clusters (43.5%), and in this cluster-level landscape only 17.0% have COG categories and 4.6% have KEGG KOs; orthology data contain 3,449 pairs for 1,885 genes (29.3% of truly dark genes) across 48 Fitness Browser organisms. [src: truly_dark_genes]

## Caveats and Limitations

The pangenome linkage gap prevents assessment of 17,479 dark genes (31%); the report estimates that approximately 2,841 of them may be truly dark, describing this as a 31% coverage gap in the prioritized list. [src: truly_dark_genes]

Bakta may produce false-negative functional calls: some genes labeled hypothetical may have known functions that did not match the Bakta PSC database at the tested version, v6.0. [src: truly_dark_genes]

Bidirectional best hit (BBH) ortholog coverage, which treats reciprocal top-scoring matches between genomes as orthologs, includes only 32 of 48 Fitness Browser organisms, so truly dark genes from the remaining 16 organisms lack concordance and ortholog-breadth data. [src: truly_dark_genes]

GC deviation is an imperfect HGT indicator because gene-specific composition biases, including those associated with membrane proteins, and amelioration over time can also produce deviation. [src: truly_dark_genes]

Short genes are inherently harder to annotate because they contain fewer domains and have fewer homologs, and they are harder to measure for fitness because they provide fewer transposon-insertion sites. Consequently, the length difference of d = −0.432 may partially explain other observed differences. [src: truly_dark_genes]

Some strong fitness phenotypes may result from polar effects on downstream genes rather than from the truly dark gene itself. [src: truly_dark_genes]

The proposed biological interpretation is therefore strongest for the directly measured differences and weaker for causal explanations: accessory-genome enrichment, GC deviation, mobile-element proximity, and narrow taxonomic breadth support recent acquisition and rapid evolution, but do not by themselves establish HGT or gene function. [src: truly_dark_genes]

## Data Sources

Gene properties (length, GC, position) and cross-organism orthologs came from the Fitness Browser `kescience_fitnessbrowser` gene and ortholog tables ([[data/kescience-fitnessbrowser]]). Pfam domain hits, database cross-references and eggNOG functional annotations came from the `bakta_pfam_domains`, `bakta_db_xrefs` and `eggnog_mapper_annotations` tables of the KBase pangenome collection `kbase_ke_pangenome` ([[data/kbase-ke-pangenome]]). The report includes a figure of the organism distribution of truly dark genes (fig01_organism_distribution.png). [src: truly_dark_genes]

Figures referenced by the report [src: truly_dark_genes]:
- fig01_organism_distribution.png: truly dark gene counts by organism, with Methanococcus dominating.
- fig02_gene_length.png: gene-length comparison of truly dark and annotation-lag genes.
- fig03_summary_comparison.png: multi-panel comparison of truly dark (TD) and annotation-lag (AL) properties.
- fig04_clue_coverage.png: clue-coverage bar chart and clues-per-gene histogram.
- fig05_annotation_tiers.png: annotation-tier distribution and gene length by tier.
- fig06_ortholog_breadth.png: ortholog-breadth distributions and per-organism coverage.
- fig07_gc_deviation.png: GC-deviation distributions, presented as a horizontal-gene-transfer indicator.
- fig08_genomic_context.png: cofitness, mobile elements and condition enrichment.
- fig09_prioritization.png: priority-score distribution and top-100 candidate analysis.

## Future Directions

The report proposes several lines of future work; none of them is a completed result [src: truly_dark_genes]:
- Structure prediction with AlphaFold2 or ESMFold for the top-100 candidates, followed by Foldseek searches for remote structural homologs. The report calls this the most promising path to functional annotation for sequences with no detectable sequence homology.
- Growth assays for top candidates in predicted conditions, such as motility assays for PV4/5210953 and nitrogen limitation for ANA3/7026383. Mobile-CRISPRi (Peters et al. 2019) is suggested for rapid functional testing across organisms.
- Extension of pangenome linkage to the 17,479 unlinked dark genes, followed by Bakta runs to identify additional truly dark candidates and expand the priority list. This work has not yet established any additional candidates.
- Characterization of genomic “dark islands”, which are contiguous hypothetical regions, as potential functional units. Some may be prophage remnants and others recently acquired metabolic cassettes, but both possibilities remain speculative.
- A Methanococcus deep-dive, motivated by the report's statement that archaea contribute 55% of truly dark genes. It would use high cofitness signals (r > 0.97) to map operonic structure and generate functional predictions for archaeal-specific hypothetical proteins.

## Slots Into

- [[concepts/genomic-under-representation]] — Quantifies the residual functional dark matter after modern Bakta, Pfam, KEGG, and eggNOG annotation, and provides a clue-based framework for prioritizing unknown genes.
- [[concepts/gene-essentiality]] — Shows that 18.0% of truly dark genes are essential versus 13.4% of annotation-lag genes and that 34 of the top 100 candidates are essential.
- [[concepts/condition-specific-fitness]] — Tests and rejects stress enrichment while identifying reported enrichment in mixed-community, iron, nutrient time-series, and rich-media conditions.
- [[concepts/cofitness-network-architecture]] — Uses operon-like cofitness and ICA-module membership to infer candidate functions for genes lacking direct annotation.
- [[concepts/pangenome-integration]] — Separates annotation lag from persistent hypothetical genes using pangenome-linked Bakta reannotation and identifies the 17,479-gene linkage gap.
- [[concepts/gene-function-acquisition-depth]] — Provides evidence that narrow ortholog breadth, accessory-genome localization, GC deviation, and mobile-element proximity distinguish truly dark genes from annotation-lag genes.
- [[concepts/evidence-triangulation-for-functional-annotation]] — Shows that sequence identifiers and cross-references are abundant but rarely functional. eggNOG, operon context and ortholog data supply partial and sometimes conflicting clues, such as the trehalose-synthase hint for a hypothetical gene.
- [[concepts/research-attention-inequality]] — Splits the dark-gene census into annotation-lag, truly dark and unlinked genes.
- [[concepts/structural-annotation-gap]] — Documents that truly dark genes are shorter, less conserved and concentrated in archaea, with sparse Pfam coverage and a gene-length confound.
- [[concepts/comparative-conservation-metric-calibration]] — Reports effect sizes for core-genome fraction, ortholog presence and ortholog breadth between truly dark and annotation-lag genes.
- [[concepts/adversarial-research-quality-assurance]] — Flags an internal inconsistency between the claimed pre-registered thresholds and the reported essentiality effect.
- [[concepts/horizontal-gene-transfer-driven-innovation]] — Adds evidence from GC deviation, mobile-element proximity and dark islands that is consistent with horizontal acquisition but does not prove it.
- [[concepts/experimental-prioritization-of-functional-dark-matter]] — Provides a multi-criteria ranking of all truly dark genes, with named top candidates and an extrapolated coverage gap.
- [[concepts/homology-search-negative-evidence]] — Treats persistent hypothetical calls as negative evidence, with the caveat that some may be Bakta PSC false negatives.
- [[concepts/fitness-condition-coverage-prioritization-bias]] — Reports condition enrichment and depletion profiles and an unreconciled discrepancy between two stress comparisons.
- [[concepts/transposon-callability-bias]] — Notes that short genes offer fewer insertion sites and that polar effects may produce spurious phenotypes. [src: truly_dark_genes]
