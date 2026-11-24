---
type: "Concept"
description: "How reference strain PA14 differs from clinical CF isolates in T3SS, biofilm and regulatory genotype, and strain variation in genome content."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/pitfalls.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Pseudomonas aeruginosa strain diversity and representativeness of reference strains

The reference strain PA14 differs from PAO1 in type III secretion system (T3SS) effector, biofilm polysaccharides and regulatory state. [src: cf_formulation_design] In genome typing, PA14 is rare among cystic fibrosis (CF) Pseudomonas aeruginosa isolates by virulence genotype. [src: pitfalls] The cross-project pitfalls digest agrees: CF P. aeruginosa is 94% ExoS+ and 92% Pel+Psl+ (PAO1-like). [src: pitfalls] The evidence comes from one report's typing of 6,760 genomes plus a PROTECT collection analysis. [src: cf_formulation_design] It is direct genome-based typing. The report's inhibition measurements have not been validated against ExoS+/PAO1-type strains. [src: cf_formulation_design] See [[entities/pseudomonas-aeruginosa-pa14]], [[entities/pseudomonas-aeruginosa]], [[summaries/cf_formulation_design__REPORT]] and [[summaries/pitfalls]].

## Literature Context

The candidate papers show that P. aeruginosa is a genetically diverse species and that findings from single reference strains may not transfer. The international reference panel paper collated 43 strains to reflect the organism's diversity, and noted that most virulence and pathogenesis studies focus on a small number of strains [PMID 24214409](https://pubmed.ncbi.nlm.nih.gov/24214409/). A comparative genomics study of two CF isolates described a mosaic genome: a conserved core interrupted by strain-specific blocks of genes in regions of genomic plasticity, with niche adaptation as a major force shaping genome composition [PMID 18287045](https://pubmed.ncbi.nlm.nih.gov/18287045/). Strain variation also shows up in regulation. An RIP-seq study of three strains from the major phylogenetic lineages found that most Hfq interactions were not conserved among strains. The accessory Hfq interactome included most mRNAs encoding T3SS components and secreted toxins in two strains [PMID 35273147](https://pubmed.ncbi.nlm.nih.gov/35273147/). That work addresses post-transcriptional interactions, not effector genotype. Among seven Liverpool epidemic strain isolates, regulatory polymorphisms were mostly isolate-specific and phenotypes varied widely, including biofilm formation [PMID 24505294](https://pubmed.ncbi.nlm.nih.gov/24505294/). A study of seven clinical isolates reported universal and isolate-specific mucin-driven metabolic shifts [PMID 42390224](https://pubmed.ncbi.nlm.nih.gov/42390224/). Within the T3SS, ExoY activity was found in about 60% of 40 reference panel strains, with no significant difference between CF and non-CF isolates [PMID 34675890](https://pubmed.ncbi.nlm.nih.gov/34675890/).

The corpus's central claim is that PA14 (ExoU+, Pel-only, ladS mutant) represents <5% of CF isolates, with CF isolates 94% ExoS+ and 92% Pel+Psl+ across 6,760 genomes. This is consistent with the literature's general warning that reference strains under-represent species diversity [PMID 24214409](https://pubmed.ncbi.nlm.nih.gov/24214409/). The candidate papers do not give ExoS/ExoU or Pel/Psl frequencies, so they neither confirm nor contradict those percentages. The corpus's genotype-based quantification of PA14's rarity in CF is therefore an extension, not a replication. The Hfq result supports, as a hypothesis, that T3SS-related regulation may differ between strains, which would add to the hub's genotype-level contrast. It does not show that T3SS expression differs.

The corpus's 24% gene-content range across 15 PROTECT strain groups, with 1,358 extra genes in the largest group, fits the mosaic accessory-genome picture [PMID 18287045](https://pubmed.ncbi.nlm.nih.gov/18287045/). Its hypothesis that these genes are conditionally expressed accessory functions is untested. The corpus's separate finding that sugar pathway losses are conserved at the species level limits the strain-specific view for those pathways. The corpus predicts one formulation will work across strains because amino acid catabolism is invariant. The isolate-specific mucin responses [PMID 42390224](https://pubmed.ncbi.nlm.nih.gov/42390224/) and regulatory diversity [PMID 24505294](https://pubmed.ncbi.nlm.nih.gov/24505294/) suggest this prediction needs testing. The corpus itself says its PA14 inhibition assays have not been validated against ExoS+/PAO1-type strains, so the invariance claim stays a prediction.

## How PA14 differs from PAO1

PA14 and PAO1 differ qualitatively in T3SS effectors (ExoU vs ExoS), biofilm polysaccharides (Pel-only vs Pel+Psl) and regulatory state (ladS mutation). [src: cf_formulation_design] The report cites Grace et al. (2022) as a review of these differences, including the psl deletion and ladS frameshift. [src: cf_formulation_design] PA14 is ExoU+, Pel-only and a ladS mutant, and represents <5% of CF isolates by virulence genotype. [src: pitfalls]

## T3SS effector type across 6,760 genomes

The analysis covers 6,760 genomes, with environmental metadata for 4,769. [src: cf_formulation_design] ExoS dominates in CF and ExoU becomes more common in other settings. [src: cf_formulation_design]

| Source | ExoS+ | ExoU+ | Both | Genomes |
|---|---|---|---|---|
| CF patient | 94% | 5% | 0% | 291 [src: cf_formulation_design] |
| Lung/respiratory | 82% | 16% | 1% | 1,505 [src: cf_formulation_design] |
| Other clinical | 63% | 33% | 3% | 1,731 [src: cf_formulation_design] |
| Environmental | 62% | 35% | 1% | 370 [src: cf_formulation_design] |

The report reads the higher ExoU prevalence outside CF as consistent with ExoU being an acute cytotoxic effector rather than a chronic colonization factor. [src: cf_formulation_design] Co-expressing exoS+/exoU+ strains were detected in 1.5% of genomes, concentrated in non-CF clinical settings. [src: cf_formulation_design] Song et al. (2023) described hypervirulent co-expressing strains. [src: cf_formulation_design]

The 94% ExoS+ figure agrees with earlier clinical work. Hu et al. (2013) found a predominantly exoS+/exoU– genotype in longitudinal CF isolates from young children. [src: cf_formulation_design] Sarges et al. (2020) reported similar ExoS dominance, with exoS+/exoU+ as a rare variant. [src: cf_formulation_design] The report says its result extends these observations to 291 genomes. [src: cf_formulation_design]

## Biofilm and regulatory genotype

In the genome set, 96.4% carry both Pel and Psl operons, a PAO1-like architecture. [src: cf_formulation_design] Only 3.5% are Pel-only (PA14-like), with slight enrichment in CF (8%) versus environmental (3%). [src: cf_formulation_design] The report calls PA14's psl deletion a rare variant, not representative of the species. [src: cf_formulation_design] CF isolates are 92% Pel+Psl+. [src: cf_formulation_design, pitfalls] Bakta annotation detects ladS in only 0.5% of genomes. [src: cf_formulation_design] The report calls PA14's ladS frameshift an extreme outlier that locks it in an acute-virulence regulatory state unrepresentative of natural infection. [src: cf_formulation_design] It concludes that PA14 is a poor model for chronic CF infection. [src: cf_formulation_design]

## The PROTECT collection

In the PROTECT collection of 651 genomes, 47% carry exoS and 7% carry exoU. [src: cf_formulation_design] Of 643 profiled genomes, 304 (47%) are PAO1-like (ExoS+) [src: cf_formulation_design] and 48 (7%) are PA14-like (ExoU+). [src: cf_formulation_design] 291 (45%) are intermediate, lacking clear T3SS annotation in GenomeDepot. [src: cf_formulation_design] This is a gene-name annotation coverage gap, so the classification is incomplete. [src: cf_formulation_design] Among classifiable isolates, 86% are PAO1-like, which the report takes as confirming that PA14 is not representative of the PROTECT CF collection. [src: cf_formulation_design] Strain groups are uniformly PAO1-like or uniformly PA14-like. The report interprets this as T3SS effector type being a clonal trait inherited within lineages rather than horizontally transferred. [src: cf_formulation_design] See also [[entities/protect-genome-depot]].

### Pfam-based tree

The PROTECT and pangenome databases share 2,850 standardized Pfam domains, with ~3,200 unique domains per genome. [src: cf_formulation_design] The tree spans 165 genomes: 13 PROTECT strain group representatives, 150 sampled lung/airway genomes and the PAO1/PA14 references. [src: cf_formulation_design] It uses Jaccard distances on 1,557 variable Pfam domains present in 5–95% of genomes. [src: cf_formulation_design] PROTECT isolates are distributed across lung diversity rather than clustered in one lineage, which the report reads as sampling the breadth of CF variation. [src: cf_formulation_design] ExoU+ isolates cluster separately from the ExoS+ majority. The report calls this consistent with PAPI-1/PAPI-2 pathogenicity island acquisition as a deep phylogenetic event. [src: cf_formulation_design]

## Genome content variation

Among 15 PROTECT strain groups, genome size ranges from 6.12 Mb (5,668 CDS) to 7.35 Mb (7,026 CDS), a 24% gene-content difference. [src: cf_formulation_design] The largest group (725, 98 isolates) carries 1,358 extra genes relative to the smallest. [src: cf_formulation_design] All groups keep the same amino acid catabolic pathways (97%+ conservation). [src: cf_formulation_design] The report therefore hypothesizes that the extra genes are conditionally expressed accessory functions (prophages, mobile elements, niche adaptations) affecting virulence and persistence rather than amino acid growth rate. [src: cf_formulation_design] It notes that within-species genome size is a much weaker growth-rate predictor than cross-species variation. [src: cf_formulation_design]

Mathee et al. (2008) described a mosaic P. aeruginosa genome with strain-specific regions of genomic plasticity. The pseudomonas_carbon_ecology report states that its own results show sugar pathway losses are conserved at the species level, not strain-specific. [src: pseudomonas_carbon_ecology] This limits the mosaic, strain-specific view: it does not extend to those sugar pathway losses. [src: pseudomonas_carbon_ecology]

## Implications claimed for the formulation

The report predicts that strains respond similarly, because the amino acid catabolism targets are invariant across the species. [src: cf_formulation_design] It expects strains to differ in virulence, antibiotic resistance and biofilm properties, which affect disease severity but not the metabolic competition mechanism. [src: cf_formulation_design] It also predicts one formulation should work against all variants regardless of T3SS type. [src: cf_formulation_design] It suggests ExoS dominance may give a wider window for competitive exclusion, since ExoS kills more slowly and apoptotically than ExoU. [src: cf_formulation_design]

These predictions are limits, not tested results. All inhibition assays used PA14, which represents <5% of CF isolates. [src: cf_formulation_design] In the cf_formulation_design project, PA14 inhibition assays therefore test the formulation against a minority variant. [src: pitfalls] The pitfalls digest recommends validating PA14-based assay results against ExoS+ strains before generalizing to CF. [src: pitfalls] The inhibition measurements have not been validated against ExoS+/PAO1-type strains. [src: cf_formulation_design] Mucoid clinical isolates adapted to chronic infection may respond differently. [src: cf_formulation_design] The report therefore elevates PAO1 and clinical strain testing (Proposed Experiment 4.6) in importance. [src: cf_formulation_design] See [[concepts/generalizability-limits-of-planktonic-single-strain-inhibition-assays]].

### Experiments the report proposes

The report proposes repeating inhibition and carbon utilization assays against PAO1 and 3–5 mucoid clinical isolates from the PROTECT collection. [src: cf_formulation_design] It also proposes characterizing the 15 strain groups for virulence factors, biofilm capacity and resistance, and correlating these with the 1,358-gene accessory genome. [src: cf_formulation_design] Such accessory-gene differences would inform whether some patients need formulation plus antibiotics, whether biofilm-adapted strains resist through spatial refuge rather than metabolic advantage, and which strain groups to prioritize for mouse testing. [src: cf_formulation_design] The expected outcome is an annotation linking group differences to virulence, biofilm and resistance rather than metabolic competition, which would confirm one formulation design serves all variants. [src: cf_formulation_design]

## Open Directions

- Run the PAO1 and mucoid PROTECT isolate assays to test whether the invariance prediction holds in ExoS+ strains.
- Annotate the 1,358-gene accessory genome against virulence, biofilm and resistance traits measured across the 15 strain groups.
- Improve T3SS annotation for the 45% of PROTECT genomes lacking clear effector calls, to firm up the 86% PAO1-like estimate.
- Test whether the species-level conservation of sugar pathway losses holds across the 15 PROTECT strain groups, given the mosaic-genome view.
