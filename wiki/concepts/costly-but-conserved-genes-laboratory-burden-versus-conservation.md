---
type: "Concept"
description: "Whether genes that are burdensome in laboratory conditions are nonetheless conserved in the core genome, how this varies by SEED functional category, and how burden-by-conservation quadrants and natural selection might explain it; stops at the lab-to-nature inference."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md", "summaries/discoveries.md", "summaries/fitness_effects_conservation__REPORT.md"]
---
# Costly but conserved genes: laboratory burden versus conservation

Some genes that are burdensome in the laboratory are still conserved in the core genome. The reports count 28,017 such costly-and-conserved genes in Fitness Browser (FB) data. [src: conservation_fitness_synthesis, core_gene_tradeoffs] They explain these genes as natural selection for functions that laboratory conditions do not test. [src: costly_dispensable_genes, discoveries] The lab-to-nature step is an interpretation, and the reports state that laboratory conditions are a limited proxy for nature. [src: conservation_fitness_synthesis, core_gene_tradeoffs]

## Core genes are more often burdens than accessory genes

Core genes are more likely than accessory genes to show positive fitness when deleted: 24.4% versus 19.9%. [src: conservation_fitness_synthesis] One report gives the same figures as "ever beneficial" and adds OR=0.77 for auxiliary versus core (OR = odds ratio). [src: fitness_effects_conservation] This contradicts the streamlining hypothesis. Accessory genes are less costly than core genes and are not systematically burdensome. [src: conservation_fitness_synthesis] The authors suggest that core genes more often take part in trade-offs, helping in some conditions and costing in others. [src: fitness_effects_conservation]

Antimicrobial resistance (AMR) genes fit this picture only partly. Singleton AMR genes are the costliest, with median fitness -0.019. [src: amr_pangenome_atlas] The AMR report treats core AMR genes as an exception to the core-burden finding, because they appear less costly than non-AMR core genes. [src: amr_pangenome_atlas] See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]].

## Variation by SEED functional category

The core-burden excess is function-specific. Core genes are disproportionately burdensome in Protein Metabolism (+6.2pp), Motility (+7.8pp) and RNA Metabolism (+12.9pp). [src: core_gene_tradeoffs] The synthesis report gives the same three values. [src: conservation_fitness_synthesis] Cell Wall reverses the pattern: non-core cell wall genes are more burdensome (-14.1pp). [src: conservation_fitness_synthesis, core_gene_tradeoffs] More detail is in [[concepts/function-specific-burden-of-core-genes]].

The reports explain these categories biologically. Flagella are expensive but essential for chemotaxis. Ribosomal components are costly but required for rapid growth responses. [src: core_gene_tradeoffs] Motility is presented as the example of the burden paradox. [src: core_gene_tradeoffs] The report says core genes are more burdensome in the lab because they encode energetically expensive functions that are essential in natural environments. [src: core_gene_tradeoffs]

## Burden-by-conservation quadrants

The selection signature matrix crosses lab burden with pangenome conservation. Its cells are:

- Costly and conserved: 28,017 genes, which the report says natural selection maintains despite lab-measured cost. [src: core_gene_tradeoffs, costly_dispensable_genes]
- Costly and dispensable: 5,526 non-core genes, which are candidates for ongoing gene loss. [src: core_gene_tradeoffs, discoveries]
- Neutral and dispensable: 21,886 genes, described as niche-specific. [src: core_gene_tradeoffs, discoveries]
- Neutral and conserved: 86,761 genes, described as classic housekeeping genes. [src: core_gene_tradeoffs]

Costly and dispensable genes are significantly depleted (FDR < 0.05, false discovery rate) in 14 SEED top-level categories. These include Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response and RNA Metabolism. [src: costly_dispensable_genes] Costly and conserved genes are enriched in Protein Metabolism, Respiration and Motility. [src: costly_dispensable_genes] The report reads this as lab-measured burden offset by natural selection in the environment. [src: costly_dispensable_genes] Adding pangenome conservation to FB phenotype data separates evolutionarily stable phenotypic genes from transient ones. [src: costly_dispensable_genes] See [[entities/gene-quadrant-dataset]] and mobile element origin of costly non conserved genes.

## Natural selection as the proposed explanation

The reports call the 28,017 costly and conserved genes their strongest evidence for purifying selection in natural environments. [src: conservation_fitness_synthesis, core_gene_tradeoffs, discoveries] This is an inference from laboratory data. Genes with strong condition-specific effects are more likely to be core, which the report reads as the conserved genome being functionally active. [src: core_gene_tradeoffs] The report cites Rosconi et al. (2022) on strain-dependent essentiality in *S. pneumoniae*. It says this supports conservation reflecting selection across diverse environments rather than universal essentiality. [src: core_gene_tradeoffs] It cites Koskiniemi et al. (2012) on fitness costs of dispensable genes in *Salmonella*. It calls this consistent with higher lab burden in core genes. [src: core_gene_tradeoffs] The synthesis report summarises the split this way: the lab captures the cost of maintaining genes, and the pangenome captures the evolutionary pressure to keep them. [src: conservation_fitness_synthesis] Related pages: [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]] and [[concepts/condition-dependent-fitness-trade-offs-of-core-versus-accessory-genes]].

## Caveats

The lab-to-nature inference is limited in several ways.

- Lab conditions are an impoverished proxy for nature [src: conservation_fitness_synthesis] and capture only a fraction of natural conditions. [src: core_gene_tradeoffs]
- A gene with positive fitness on deletion in rich media may be essential in soil, biofilm or host tissue. [src: conservation_fitness_synthesis]
- FB condition types are biased toward experimental convenience, not ecological relevance. [src: core_gene_tradeoffs, costly_dispensable_genes]
- "Burden" (fit > 1) may reflect trade-offs rather than true dispensability. [src: core_gene_tradeoffs]
- Burden is defined as max_fit > 1 in any experiment, so one experiment can classify a gene as burdensome. This makes the call sensitive to noise. [src: costly_dispensable_genes]
- The 90% identity threshold for DIAMOND matching may miss rapidly evolving genes. [src: core_gene_tradeoffs]
- The pangenome core/auxiliary split is binary. [src: costly_dispensable_genes] The report proposes replacing it with the fraction of species genomes carrying each gene cluster, to distinguish "almost core" from "rare accessory" genes. [src: costly_dispensable_genes]

The costly_dispensable_genes report claims novelty: the first systematic characterization of genes that are burdensome and not conserved. [src: costly_dispensable_genes] It also claims novelty in its cross-organism scale of 142,190 genes across 43 bacteria. [src: costly_dispensable_genes]

## Open Directions

- Use the fraction of species genomes carrying each gene cluster instead of the binary core/accessory call. This tests whether the costly-and-conserved quadrant holds at graded conservation.
- Redo the burden classification with a replicate-robust criterion instead of a single experiment with max_fit > 1. This tests whether the 28,017 count is sensitive to noise.
- Compare costly-and-conserved genes with fitness data from ecologically relevant conditions such as soil or host-like media. This would test the natural-selection explanation directly.
- Test whether the core-burden excess reflects trade-offs. Check whether costly core genes are also strongly beneficial in other conditions.
