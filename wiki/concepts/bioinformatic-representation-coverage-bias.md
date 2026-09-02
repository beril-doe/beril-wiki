---
type: "Concept"
description: "How reference-database coverage biases genomic function inference"
sources: ["summaries/alphafold_msa_annotation__REPORT.md"]
---
# Reference-database coverage shapes genomic annotation inference

Genomic annotation inference is constrained not only by the genes present in a pangenome but also by whether those genes bridge to reference databases and structurally characterized sequence space. The [[summaries/alphafold_msa_annotation__REPORT]] evaluates AlphaFold multiple-sequence-alignment (MSA) depth, meaning the number of homologous sequences represented in an alignment, as a proxy for reference coverage and annotation richness across bacterial gene clusters. [src: alphafold_msa_annotation]

## Evidence for coverage bias

The analysis began with 132,531,501 gene clusters, of which 38,804,903 (29.3%) had a real UniProt accession and 38,051,842 (28.7%) bridged successfully to AlphaFold MSA depths. The remaining 70.7% lacked UniRef100 identifiers or had UniParc-only identifiers without an AlphaFold entry, so the analysed subset was biased toward better-studied organisms. [src: alphafold_msa_annotation] This incomplete bridge suggests the hypothesis that the unrepresented 70.7% contains an even larger annotation gap, although that gap was not directly measured. [src: alphafold_msa_annotation]

Among bridged clusters, core genes had a median MSA depth of 15,308, compared with 5,299 for auxiliary+singleton clusters and 5,527 for auxiliary non-singleton clusters. Core genes therefore had 2.89× the median depth of auxiliary+singleton clusters and 2.77× that of auxiliary non-singleton clusters, showing that pangenome class is associated with unequal reference representation. [src: alphafold_msa_annotation] The 10th-percentile MSA depth was 334 for core genes versus 25–32 for accessory genes, further indicating that the lower tail of reference coverage is concentrated among accessory genes. [src: alphafold_msa_annotation]

Hypothetical-protein rates showed the same class-dependent pattern: 13.8% in auxiliary+singleton clusters, 11.6% in auxiliary non-singleton clusters, and 3.8% in core clusters. Chi-square tests were overwhelmingly significant (χ² > 500,000; p ≈ 0), with odds ratios of 0.25 for core versus auxiliary+singleton and 0.31 for core versus auxiliary non-singleton. [src: alphafold_msa_annotation] These results support [[concepts/pangenome-integration]] by showing that apparent functional annotation differences between core and accessory genes partly track unequal representation in reference databases. [src: alphafold_msa_annotation]

## MSA depth and inferred function

Across 38,051,842 gene cluster–UniProt pairs, MSA depth and domain-hit count had Spearman ρ = 0.7563. [src: alphafold_msa_annotation] Mean domain hits increased from 0.59 for MSA depth < 10 to 10.83 for MSA depth ≥ 10,000, while mean distinct InterPro (IPR) families increased from 0.059 to 4.601, an 18× span in mean domain hits. [src: alphafold_msa_annotation] This relationship supports [[concepts/structural-annotation-gap]] because sparse reference representation is associated with fewer detectable domain-level annotations, rather than merely with a smaller number of named gene functions. [src: alphafold_msa_annotation]

The monotone relationship between MSA depth and domain hits held within core, auxiliary non-singleton, and auxiliary+singleton classes, with core genes showing slightly higher domain richness per MSA bin than accessory genes at equivalent depth. [src: alphafold_msa_annotation] This refines the simple interpretation that core genes are better annotated solely because they belong to the core: even after comparing similar MSA-depth bins, annotation richness differs modestly by pangenome class. [src: alphafold_msa_annotation]

Reference coverage is not equivalent to domain-annotation coverage. Of all 132,531,501 gene clusters, 111,035,431 (83.8%) had at least one InterProScan domain annotation, with mean hits of 7.5 and mean distinct IPR families of 3.3, whereas only 29.3% bridged to AlphaFold MSA depth. [src: alphafold_msa_annotation] The contrast indicates that different annotation resources expose different layers of the genomic annotation landscape: a gene can have an InterProScan domain assignment without having a successful AlphaFold bridge, while MSA depth provides an additional measure of how broadly its sequence space is represented. [src: alphafold_msa_annotation]

## The core-gene annotation paradox

The cross-class pattern does not mean that all core genes are well represented. The report identified 415,603 distinct core clusters with MSA depth < 10, represented across 14,768 species clades. Their mean and median MSA depths were 4.57 and 4.0, respectively; 286,439 (68.9%) were hypothetical, 137 (0.033%) were EC-annotated, and 346 (0.083%) were KEGG-mapped. [src: alphafold_msa_annotation]

This low-coverage core subset had a 68.9% hypothetical rate versus 3.8% for all core genes, while EC and KEGG annotations were below 0.1%. [src: alphafold_msa_annotation] The result supports [[concepts/core-gene-annotation-paradox]]: conservation-based classification can identify a gene as core while reference-database coverage remains too sparse to support a confident functional inference. [src: alphafold_msa_annotation]

The report interprets these clusters as candidates for experimental structural characterization because they are conserved by pangenome classification yet isolated from characterized sequence space; this is a prioritization hypothesis rather than direct experimental validation. [src: alphafold_msa_annotation] Top-ranked proteins with MSA depth = 1 came primarily from poorly characterized marine and soil bacteria, including Oceanicoccus, Dwaynesavagella, and CAILRJ01. [src: alphafold_msa_annotation]

## What the bias changes

The evidence supports a two-layer model of annotation bias. An MSA-depth-driven gap affects core, auxiliary, and singleton classes, while a pangenome-class gap produces higher hypothetical-protein rates among accessory and singleton genes, likely associated with horizontal transfer, rapid evolution, and taxonomically narrow distribution. [src: alphafold_msa_annotation] The cross-class comparison is dominated by the higher average MSA depth of core genes, whereas the low-MSA-depth core subset reveals severe underannotation within a class that is usually treated as well characterized. [src: alphafold_msa_annotation]

This distinction matters for downstream analyses that use annotations as biological evidence. Functional counts, pathway prevalence, and candidate-gene prioritization can be biased toward taxa and gene classes with stronger reference representation, while genes from poorly represented organisms may appear hypothetical or lack pathway assignments even when they are conserved or biologically important. [src: alphafold_msa_annotation] The report provides direct evidence for the coverage gradient and annotation associations, but the effects on downstream ecological or phenotypic conclusions remain a testable inference rather than a measured outcome. [src: alphafold_msa_annotation]

The representative-sequence design limits interpretation: MSA depth was looked up for each gene cluster's representative sequence, so within-cluster sequence diversity was ignored and the representative could have higher or lower MSA depth than typical cluster members. [src: alphafold_msa_annotation] The 293K genomes were not phylogenetically balanced, and common taxa such as Pseudomonas and E. coli were over-represented, influencing core-gene counts and MSA-depth distributions. [src: alphafold_msa_annotation] Spearman ρ = 0.7563 was computed on the full 38,051,842-pair dataset without subgroup stratification, so its value may differ among pangenome classes and organisms with different annotation gaps. [src: alphafold_msa_annotation] The analysis also used a static version-6 BERDL AlphaFold snapshot, and later UniProt deposits may change MSA depths. [src: alphafold_msa_annotation]

## Related integration

The coverage gradient strengthens [[concepts/pangenome-integration]] by connecting core/accessory structure to reference representation and hypothetical-protein rates. [src: alphafold_msa_annotation] It extends [[concepts/structural-annotation-gap]] by identifying low-MSA-depth core genes as a distinct underannotated subset. [src: alphafold_msa_annotation] It also creates a testable bridge to [[concepts/multi-omics-integration]] and [[concepts/gene-essentiality]], because the report proposes joining the 415,603 paradox clusters to Fitness Browser measurements to identify conserved, structurally novel proteins with condition-specific or growth-essential phenotypes. [src: alphafold_msa_annotation]

## Open Directions

- Recompute the bridge using all 132,531,501 gene clusters, including the 70.7% without a successful AlphaFold entry, with identifier recovery and stratified missingness analysis to test whether the unrepresented population has a larger annotation gap. [src: alphafold_msa_annotation]
- Recalculate MSA depth and InterProScan richness by phylogenetically balanced taxon strata, using mixed-effects or stratified Spearman analyses, to determine how much of ρ = 0.7563 is driven by organism composition. [src: alphafold_msa_annotation]
- Compare representative-sequence MSA depths with member-level depths within gene clusters, using within-cluster distributions, to quantify whether representatives systematically overestimate or underestimate typical reference coverage. [src: alphafold_msa_annotation]
- Join the 415,603 core clusters with Fitness Browser measurements and test condition-specific associations between low MSA depth, hypothetical status, and fitness effects. [src: alphafold_msa_annotation]
- Reprocess the static version-6 AlphaFold snapshot against later UniProt deposits and compare MSA-depth changes, to measure how temporal database growth alters inferred annotation coverage. [src: alphafold_msa_annotation]
