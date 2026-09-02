---
type: "Concept"
description: "Evidence that AMR genes form tightly co-inherited, multi-mechanism islands"
sources: ["summaries/amr_strain_variation__REPORT.md"]
---
# Resistance-Island Co-inheritance and Mechanistic Linkage

Resistance islands are recurring groups of antimicrobial-resistance (AMR) genes that co-occur within strains, providing a way to study whether resistance mechanisms are inherited as linked modules rather than independently. In the analyzed pangenome resource, co-occurrence indicates genomic linkage or shared lineage history, but it does not by itself establish co-selection, functional synergy, or physical location on a particular mobile element. [src: amr_strain_variation]

## Evidence from Within-Species AMR Variation

The study detected 1,517 resistance islands across 705 species, representing 54% of the species analyzed. [src: amr_strain_variation] Islands had a mean size of 6.2 genes, a median size of 4 genes, a maximum size of 43 genes, and a mean phi coefficient of 0.827. [src: amr_strain_variation] The phi coefficient measures pairwise co-occurrence, so the mean value indicates very tight co-inheritance among genes assigned to these islands. [src: amr_strain_variation]

Of the 1,517 islands, 1,343 (88%) contained genes from multiple resistance mechanisms. [src: amr_strain_variation] Efflux pumps occurred in 954 islands and enzymatic inactivation occurred in 698 islands, making them the most common components reported in the analysis. [src: amr_strain_variation] The complete mechanism counts were 1,026 for Other/Unclassified, 954 for Efflux, 698 for Enzymatic inactivation, 694 for Oxidoreductase, 502 for Regulatory, 341 for Beta-lactamase, 293 for Target modification, and 137 for Cell wall modification. [src: amr_strain_variation]

The prevalence of multi-mechanism islands supports the interpretation that resistance genes can be inherited as coordinated defense modules spanning multiple drug classes. [src: amr_strain_variation] This evidence **supports** [[concepts/cofitness-network-architecture]] by showing that strong AMR gene co-occurrence can form a structured network of tightly linked modules rather than only isolated pairwise associations. [src: amr_strain_variation] The result remains an association: genes may be linked on the same mobile genetic element or maintained by lineage history without providing functional synergy or being jointly selected. [src: amr_strain_variation]

## Relationship to Phylogeny and Acquisition

AMR repertoire similarity was significantly associated with phylogenetic similarity in 701 of 1,261 species (55.6%) tested using Mantel tests at FDR < 0.05, where FDR is the false-discovery rate. [src: amr_strain_variation] The median Mantel r for all AMR genes was 0.247, and 87.8% of species showed positive correlation between ANI distance and AMR Jaccard distance. [src: amr_strain_variation] These results indicate that resistance-island distributions can reflect stable lineage-associated inheritance in addition to recent horizontal acquisition. [src: amr_strain_variation]

Non-core, putatively acquired AMR genes had a median Mantel r of 0.222, compared with 0.117 for core, intrinsic genes; the paired t-test gave t = -8.35, p = 7.0e-16, and n = 489. [src: amr_strain_variation] This finding **supports** the hypothesis that acquired resistance elements can become stably maintained and vertically transmitted within lineages. [src: amr_strain_variation] However, the comparison is partly constrained by the low Jaccard-distance variance of near-universal core genes, so the stronger non-core signal cannot be interpreted as a purely biological measure of island inheritance. [src: amr_strain_variation]

## Mechanistic Interpretation and Limits

The 88% prevalence of multi-mechanism islands suggests the hypothesis that resistance modules may provide broad protection against multiple drug classes or may be co-maintained because their genes share genomic context. [src: amr_strain_variation] The available co-occurrence analysis does not distinguish among physical linkage, ecological co-exposure, clonal expansion, co-selection, and direct functional interaction. [src: amr_strain_variation] Consequently, the evidence supports mechanistic linkage as a testable model, but does not establish that the linked genes act synergistically. [src: amr_strain_variation]

The report specifically identifies genomic-context mapping to plasmids, chromosomes, integron boundaries, and insertion sequences as a next step for resolving the mechanism of island formation and maintenance. [src: amr_strain_variation] Such analyses would connect the statistical islands to physical genomic structures and help distinguish horizontally transferred cassettes from chromosome-linked lineage signatures. [src: amr_strain_variation]

## Relation to Other Concepts

This concept **refines** [[concepts/resistance-island-coinheritance]] by separating the observed statistical co-inheritance of resistance genes from the stronger, unproven claim of functional co-selection. [src: amr_strain_variation] It also **supports** [[concepts/intrinsic-versus-acquired-resistance]] because non-core AMR genes showed a stronger phylogenetic signal than core AMR genes, while retaining the report's statistical caveat. [src: amr_strain_variation] The findings connect to [[concepts/ecological-resistance-association-and-causality]] because environmental or host-associated selection could contribute to island maintenance, but the present co-occurrence results do not establish that causal pathway. [src: amr_strain_variation]

The detailed source report is [[summaries/amr_strain_variation__REPORT]]. [src: amr_strain_variation]

## Open Directions

- Use the 1,517 island records together with genome assemblies and genomic-context mapping to plasmids, chromosomes, integron boundaries, and insertion sequences; determine which islands are physically linked and which are lineage-level co-occurrence patterns. [src: amr_strain_variation]
- Combine island membership with curated exposure metadata and phylogeny-aware models; test whether multi-mechanism islands are co-selected under shared antimicrobial environments rather than merely inherited together. [src: amr_strain_variation]
- Integrate resistance-island genes with virulence-factor profiles and metabolic pathway variation; test whether island composition predicts host-associated phenotypes or fitness beyond lineage background. [src: amr_strain_variation]
- Apply perturbation or competition experiments to representative multi-mechanism islands; test whether linked resistance genes produce additive, synergistic, or independent protection across drug classes. [src: amr_strain_variation]
- Use the reported phi coefficients with fitness and genomic-context data in predictive models; test whether high co-inheritance predicts future AMR gene co-acquisition. [src: amr_strain_variation]
