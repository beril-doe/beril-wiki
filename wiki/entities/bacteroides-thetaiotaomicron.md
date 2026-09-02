---
type: "Organism"
description: "Bacteroidetes organism with low gapfilling resolution and distinctive co-inheritance patterns"
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md"]
---
# Bacteroides thetaiotaomicron

## Identity

**Canonical name:** Bacteroides thetaiotaomicron. [src: annotation_gap_discovery]

**Known alias:** Btheta. [src: annotation_gap_discovery]

**Stable external identifier:** No stable external identifier was provided in the source report. [src: annotation_gap_discovery]

Bacteroides thetaiotaomicron was the sole Bacteroidetes organism among the 14 organisms analyzed in the annotation-gap discovery study. [src: annotation_gap_discovery]

## Key study findings

The organism had the lowest annotation-gap resolution rate in the study: 3 of 15 gapfilled reaction-organism pairs were resolved, corresponding to exactly 20.0%. [src: annotation_gap_discovery] Its 20.0% resolution rate was the low end of a 3.5-fold range across organisms, compared with the highest reported rate of 71.4% for [[entities/klebsiella-michiganensis]]. [src: annotation_gap_discovery]

The study associated the lower resolution rate with greater phylogenetic and metabolic divergence from the proteobacterial majority, but presented this as an interpretation rather than a directly tested causal explanation. [src: annotation_gap_discovery] The study's dataset was phylogenetically biased: 12 of 14 organisms were Proteobacteria, leaving Bacteroides thetaiotaomicron as the sole Bacteroidetes organism. [src: annotation_gap_discovery]

A later co-fitness/pangenome analysis **refines** this interpretation by showing that Btheta had 287 genomes, 4,649 pangenome clusters, and 328,455 co-fitness pairs available for analysis. [src: cofitness_coinheritance] Its pairwise co-fitness signal was weak but positive: delta phi was +0.001 across 242,676 evaluated pairs, with mean phi 0.067 for cofit pairs and 0.067 for matched random pairs (p<1e-6). [src: cofitness_coinheritance] This **supports** the broader conclusion that laboratory co-fitness only weakly predicts pangenome co-occurrence, while showing that Btheta had sufficient genomic variation for the comparison. [src: cofitness_coinheritance]

The same analysis found a stronger coordinated-module signal in Btheta: 22 of 36 independent component analysis (ICA) modules were significant, with mean within-module phi=0.192 versus a null mean of 0.086. [src: cofitness_coinheritance] This **supports** the hypothesis that multi-gene coordinated regulation can constrain co-inheritance more strongly than pairwise functional relationships alone, but does not directly explain the organism's gapfilling resolution rate. [src: cofitness_coinheritance]

The costly-plus-dispensable gene analysis adds that Bacteroides thetaiotaomicron contributed 14.0% of its genes to this quadrant, the second-highest organism-level proportion after *Pseudomonas stutzeri* RCH2 at 21.5%. [src: costly_dispensable_genes] This **refines** the existing pangenome context by placing Btheta toward the high end of costly, non-conserved gene burden, while the report does not establish whether this reflects mobile-element expansion, strain-specific biology, or another cause. [src: costly_dispensable_genes]

The organism was included in a workflow combining metabolic-model gapfilling, Fitness Browser phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology to assign candidate genes to gapfilled reactions. [src: annotation_gap_discovery] Fitness Browser measurements used random-barcode transposon sequencing (RB-TnSeq), a method that measures genome-wide mutant fitness with barcoded transposon libraries. [src: annotation_gap_discovery]

## Interpretation and limitations

Bacteroides thetaiotaomicron's result suggests that annotation-gap resolution may be less effective for phylogenetically distant clades with divergent metabolism, but the source study did not establish this as a general rule from this single Bacteroidetes organism. [src: annotation_gap_discovery] The co-fitness analysis **refines** the available context: Btheta showed a strong module-level co-inheritance pattern despite its weak pairwise signal, indicating that aggregate pangenome organization and gapfilling evidence measure related but distinct properties. [src: cofitness_coinheritance]

The 14.0% costly-plus-dispensable proportion **supports** treating Btheta's accessory genome as biologically informative rather than simply inert genomic background, but this is a cross-organism classification result and does not explain its 20.0% gapfilling resolution rate. [src: costly_dispensable_genes] The costly-plus-dispensable analysis also interprets this gene class overall as enriched for mobile genetic elements and recent acquisitions, but provides no Btheta-specific enrichment measurement; that organism-level mechanism therefore remains a hypothesis rather than an established finding for Btheta. [src: costly_dispensable_genes]

The study noted that better-annotated reference genomes and stronger Fitness Browser coverage were associated with higher organism-level resolution, so differences in annotation quality and experimental coverage may also contribute to the organism's lower rate. [src: annotation_gap_discovery] The co-fitness study also cautioned that prevalence ceilings make co-occurrence comparisons most informative for organisms with substantial auxiliary gene content; it did not establish that Btheta's module signal caused or improved annotation-gap resolution. [src: cofitness_coinheritance]

The report did not provide organism-specific evidence sufficient to distinguish the effects of phylogenetic distance, metabolic divergence, annotation quality, Fitness Browser coverage, and accessory-genome composition. [src: annotation_gap_discovery] The costly-plus-dispensable classification additionally cautions that burden was defined as max_fit > 1 in any experiment and that binary core/accessory status and sequence-linking thresholds limit interpretation. [src: costly_dispensable_genes]

## Related pages

- [[summaries/annotation_gap_discovery__REPORT]] — source summary containing the organism-level resolution results and study limitations.
- [[summaries/cofitness_coinheritance__REPORT]] — source summary of Btheta's pairwise co-fitness and ICA-module co-inheritance results.
- [[summaries/costly_dispensable_genes__REPORT]] — cross-organism analysis placing Btheta's costly-plus-dispensable gene proportion in context.
- [[concepts/metabolic-model-gapfilling]] — the organism's 3-of-15 gapfilled-pair resolution result contributes to cross-organism assessment of gapfilling-based annotation inference.
- [[concepts/cofitness-network-architecture]] — covers the weak pairwise and stronger module-level co-inheritance signals.
- [[concepts/condition-specific-fitness]] — links carbon-source fitness measurements to annotation-gap resolution.
- [[concepts/pangenome-integration]] — covers pangenome conservation evidence used in candidate-gene assignment and co-inheritance analysis.
- [[concepts/multi-omics-integration]] — covers integration of fitness, annotation, sequence-homology, pathway, and metabolic-model evidence.
