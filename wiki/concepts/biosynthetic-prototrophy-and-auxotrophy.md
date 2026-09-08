---
type: Concept
description: How pathway completeness, fitness, and nutrient dependence relate
sources:
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: conservation_fitness_synthesis
  resource: ../summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
title: Biosynthetic Prototrophy, Auxotrophy, and Nutrient Dependence
---
# Biosynthetic Prototrophy, Auxotrophy, and Nutrient Dependence

[essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md) examines biosynthetic prototrophy and possible auxotrophy using [gapmind](../entities/gapmind.md), a computational method for evaluating pathway completeness, across seven organisms selected from essential-gene data. [^essential_metabolome] The related [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) refines this framework by explicitly separating predicted pathway capability from experimentally observed fitness dependency. [^pathway_capability_dependency] A broader analysis extended this comparison to 1,695 complete pathway–organism pairs from 48 organisms, using GapMind completeness, Fitness Browser gene-fitness data, and SEED subsystem annotations as a pathway-membership proxy. [^metabolic_capability_dependency] The [conservation_fitness_synthesis__REPORT](../summaries/conservation_fitness_synthesis__REPORT.md) further refines the interpretation by showing that gene conservation and laboratory fitness are related but non-equivalent signals, rather than treating conservation as a direct measure of biosynthetic dependence. [^conservation_fitness_synthesis]

## Definitions and Scope

Biosynthetic prototrophy here refers to the predicted capacity to synthesize a required metabolite, whereas auxotrophy refers to a predicted pathway gap that could create dependence on an externally supplied nutrient. [^essential_metabolome]

The analysis is a seven-organism pilot rather than a pan-bacterial assessment because only 7 organisms were mapped successfully, although the underlying essential-gene collection contains 45 organisms. [^essential_metabolome] The broader capability-dependency study included 48 fitness-tested organisms but still had only 48 organisms among approximately 293,000 genomes with pathway predictions, limiting generalization across taxa. [^metabolic_capability_dependency]

The pathway calls used GapMind categories of complete or likely_complete, so they represent computational evidence rather than direct growth or biochemical measurements. [^essential_metabolome] This distinction is supported by the capability-dependency analyses: across 161 organism-pathway combinations from 7 model bacteria and 23 GapMind pathways, complete pathways could be either Active Dependency or Latent Capability, while incomplete pathways could still contain fitness-important genes. [^pathway_capability_dependency] Active Dependency comprised 57 pairs (35.4%), Latent Capability 66 (41.0%), Incomplete but Important 24 (14.9%), and Missing 14 (8.7%). [^pathway_capability_dependency] Thus, pathway completeness is evidence of biosynthetic potential, not by itself evidence of nutrient independence or pathway dispensability.

The larger analysis **refines** this result: among 1,695 complete pathway–organism pairs, 267 (15.8%) were latent, 547 (32.3%) intermediate, and 881 (51.9%) active, with pathway category strongly predicting dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴). [^metabolic_capability_dependency] Its latent fraction remained threshold-sensitive, ranging from 4.7% to 21.1% across 16 tested threshold combinations, but the conclusion that a non-trivial fraction of complete pathways are fitness-neutral held across that range. [^metabolic_capability_dependency]

## Evidence for Broad Amino-Acid Prototrophy

17 of 18 amino-acid biosynthesis pathways were present in all 7 analyzed organisms, representing 100% within this sample. [^essential_metabolome]

The pathways complete in all 7 organisms were arg, asn, chorismate, cys, gln, gly, his, ile, leu, lys, met, phe, pro, thr, trp, tyr, and val. [^essential_metabolome]

Six of the 7 organisms had all 18 amino-acid pathways complete, while [desulfovibrio-vulgaris-hildenborough](../entities/desulfovibrio-vulgaris-hildenborough.md) had 17/18 complete pathways, or 94.4%. [^essential_metabolome]

The other six organisms—*Caulobacter vibrioides*, *Shewanella oneidensis*, *Pseudomonas aeruginosa*, *Pseudomonas putida*, *Sinorhizobium meliloti*, and *Azospirillum brasilense*—each had 18/18 pathways and 100%. [^essential_metabolome]

This pattern supports the hypothesis that amino-acid prototrophy is common among the sampled free-living bacteria, but it does not establish universal completeness across bacteria because the sample contained only 7 organisms and one pathway was incomplete in one organism. [^essential_metabolome] The broader analysis **qualifies** this pattern: amino-acid biosynthesis was predominantly active, with 48 of 735 pairs (6.5%) latent, whereas carbon-source utilization was 217 of 892 (24.3%) latent. [^metabolic_capability_dependency] Thus, complete amino-acid pathways were less often fitness-neutral than complete carbon-utilization pathways in that dataset, although these are aggregate fitness classes rather than direct tests of prototrophy.

These findings refine [biosynthetic-self-sufficiency-and-cultivation](biosynthetic-self-sufficiency-and-cultivation.md) by showing that predicted pathway completeness can indicate biosynthetic potential without demonstrating that the pathway is required or sufficient for growth under a defined cultivation condition. [^essential_metabolome] The capability-dependency classification supports this distinction because 66 complete pathways were Latent Capability rather than fitness-important under the aggregate tested conditions. [^pathway_capability_dependency]

## Apparent Serine Auxotrophy in *Desulfovibrio vulgaris*

Serine biosynthesis was the sole amino-acid pathway not present in all 7 organisms, with a complete prediction in 6 of 7 organisms, or 85.7%. [^essential_metabolome]

The missing serine pathway was assigned to *D. vulgaris* by the GapMind analysis. [^essential_metabolome]

This result suggests the hypothesis that *D. vulgaris* may depend on externally supplied serine, but the evidence is not sufficient to establish serine auxotrophy because the result is computational and may reflect pathway-detection limitations. [^essential_metabolome]

A divergent enzyme, a non-canonical pathway, or a gene missing from the genome annotation could produce an apparent GapMind gap even when serine biosynthesis is biologically possible. [^essential_metabolome]

The report interprets the possible auxotrophy in the context of *D. vulgaris* as an anaerobic sulfate-reducing bacterium associated with organic-rich environments, including sediments, intestinal tracts, and biofilms, where amino acids may be available from protein degradation. [^essential_metabolome]

The hypothesis that losing an energetically costly biosynthetic capacity could be advantageous when serine is freely available is an ecological interpretation rather than a demonstrated mechanism. [^essential_metabolome]

The 24 Incomplete but Important pairs in the capability-dependency analysis **support** treating pathway gaps as testable hypotheses rather than definitive auxotrophy calls: fitness-important genes can occur even when GapMind reports incompleteness. [^pathway_capability_dependency] This case connects to [metabolic-model-gapfilling](metabolic-model-gapfilling.md) because the serine result illustrates how a pathway-completeness call can identify a testable metabolic gap while remaining vulnerable to incomplete annotation and non-canonical chemistry. [^essential_metabolome]

## Carbon-Source Capacity and Accessory Biosynthesis

Fumarate and succinate were reported as conserved TCA-cycle intermediates, acetate, propionate, and L-lactate were reported as conserved fermentation products, all amino acids were reported as carbon sources, deoxyribose and deoxyribonate were reported as conserved nucleotide derivatives, and putrescine was reported as a conserved polyamine carbon source. [^essential_metabolome]

Each of these reported carbon-source capacities was present in all 7 organisms, or 87.5%. [^essential_metabolome] Ethanol and deoxyinosine were nearly universal, occurring in 6 of 7 organisms, or 75%. [^essential_metabolome] The shared carbon-catabolic capacity is consistent with the ecological breadth of the sampled organisms, but that interpretation is limited by the small and phylogenetically restricted sample. [^essential_metabolome]

The broader capability analysis **refines** this interpretation by showing that carbon-source pathways were the most likely to be latent: 217 of 892 (24.3%) were latent, compared with 48 of 735 (6.5%) amino-acid biosynthesis pathways. [^metabolic_capability_dependency] Across 2,810 GTDB species with at least 10 genomes, GapMind assessed 80 pathways—18 amino-acid biosynthesis and 62 carbon-source utilization pathways—and found that variable pathway count was associated with pangenome openness (partial Spearman rho=0.530, p=2.83e-203 after controlling for genome count). [^pathway_capability_dependency] This supports the hypothesis that biosynthetic and catabolic capacity can vary within species and track genome fluidity, rather than being uniformly conserved across all members of a species.

Core-only versus all-gene comparisons further showed accessory-dependent completeness for several amino-acid pathways: the gaps were 0.146 for leucine and valine, 0.141 for arginine, 0.140 for lysine, and 0.140 for threonine biosynthesis. [^pathway_capability_dependency] These differences support the interpretation that some biosynthetic capacity may be distributed through accessory genes and could contribute to community nutrient sharing, but they do not demonstrate metabolite exchange. [^pathway_capability_dependency] At the clade level, the larger study further found a positive association between latent capability rate and pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades), **supporting** a link between fitness-neutral complete pathways and genome dynamics while not establishing nutrient sharing. [^metabolic_capability_dependency]

## Pathway Potential Is Not Essentiality

The report does not establish that a complete biosynthetic pathway is essential for viability. [^essential_metabolome]

The essential-gene measurements used RB-TnSeq, or random-barcode transposon sequencing, in rich media, where nutrient supplementation can make biosynthetic genes appear non-essential. [^essential_metabolome] Consequently, the dataset cannot distinguish genes essential for biosynthesis from genes essential for viability under the tested rich-media conditions. [^essential_metabolome]

This caveat supports [condition-specific-fitness](condition-specific-fitness.md) because the apparent importance of a biosynthetic pathway depends on which nutrients are supplied and which environmental condition is assayed. [^essential_metabolome] The capability-dependency analysis **supports** this condition-dependent interpretation: all 66 aggregate Latent Capability pairs became fitness-important under at least one condition type, with nitrogen limitation, stress, and carbon limitation the most frequent triggers. [^pathway_capability_dependency] However, its median-based condition-specific threshold can cause reclassification by construction, so these results require independent calibration rather than establishing universal biological dependency. [^pathway_capability_dependency]

The conservation–fitness synthesis **further supports** separating pathway potential from essentiality. Across 194,216 protein-coding genes in 43 bacteria, essential genes were 82% core while always-neutral genes were 66% core, showing a modest conservation gradient rather than a one-to-one mapping between retention and measured fitness. [^conservation_fitness_synthesis] Core genes were also 1.78x more likely to have strong condition-specific phenotypes, so conservation did not identify an inert housekeeping genome. [^conservation_fitness_synthesis] The costly-and-conserved category is evidence for, rather than a direct measurement of, purifying selection in nature; laboratory cost and natural retention therefore cannot establish nutrient dependence without condition-matched physiological tests. [^conservation_fitness_synthesis]

It also qualifies the interpretation of [gene-essentiality](gene-essentiality.md): pathway completeness and essential-gene measurements address related but non-identical questions about metabolic capacity and condition-specific viability. [^essential_metabolome] Pathway-level conservation did not distinguish latent capabilities from active dependencies: mean conservation was 0.829 for 755 active dependencies, 0.907 for 508 intermediate pathways, and 0.869 for 248 latent capabilities, with Mann–Whitney U p = 0.94 for active > latent and rank-biserial r = 0.052. [^metabolic_capability_dependency] This **supports** caution that conservation alone is not a proxy for pathway dependence. The synthesis likewise identifies 28,017 genes that were costly in the laboratory and conserved in the pangenome, but treats them as evidence for natural purifying selection rather than direct natural-fitness measurements. [^conservation_fitness_synthesis]

## Coverage and Inference Limits

The [escherichia-coli](../entities/escherichia-coli.md) K-12 genome was absent from the GapMind results in the KBase pangenome collection, with 0 GapMind predictions for the Keio genome GCF_000005845.2. [^essential_metabolome]

The mapped genomes had 694 predictions for *D. vulgaris* GCF_000195755.1, 694 for *S. oneidensis* GCF_000146165.2, 1,041 for *P. putida* GCF_000007565.2, 745 for *P. aeruginosa* GCF_000006765.1, 694 for *C. vibrioides* GCF_000022005.1, 1,735 for *S. meliloti* GCF_000006965.1, and 1,786 for *A. brasilense* GCF_000011365.1. [^essential_metabolome]

The report attributes the missing *E. coli* coverage to its exclusion from [gtdb](../entities/gtdb.md) pangenome construction because it had too many genomes for species-level analysis. [^essential_metabolome] This coverage issue reduced the intended analysis from 45 Fitness Browser organisms to a 7-organism pilot and leaves coverage for the remaining 38 organisms unknown. [^essential_metabolome]

The source data included 305M GapMind predictions across 293K genomes in [kbase-ke-pangenome](../entities/kbase-ke-pangenome.md), 859 universally essential gene families across 45 organisms, 80 pathway-completeness records, 18 amino-acid pathway records, 62 carbon-pathway records, 7,389 raw GapMind predictions for the selected organisms, and 8 manual organism-to-genome mappings. [^essential_metabolome]

The capability-dependency study likewise found matching GapMind data for only 7 of 48 Fitness Browser organisms, and its model-organism core genomes had mean completeness of 0.986 for Active Dependencies versus 0.975 for Latent Capabilities. [^pathway_capability_dependency] This **supports** caution that the small difference may be compressed by well-studied, near-complete genomes rather than reflecting a general rule about prototrophy. The newer analysis also notes that SEED-proxy mapping can generate false positives and that direct GapMind per-step gene assignments would improve pathway-membership precision. [^metabolic_capability_dependency]

These missing-data and sampling constraints connect to [callability-limited-comparative-inference](callability-limited-comparative-inference.md) because an absent prediction can reflect collection or mapping coverage rather than biological absence. [^essential_metabolome]

## Open Directions

- Inspect lower-confidence GapMind predictions and records with a steps_missing status for *D. vulgaris* to determine whether the serine gap reflects a near-complete pathway rather than a true absence. [^essential_metabolome]
- Test *D. vulgaris* growth on serine-free minimal medium and matched serine-supplemented medium to distinguish physiological auxotrophy from a computational detection gap. [^essential_metabolome]
- Expand organism-to-genome mapping across the remaining 38 organisms and rerun GapMind to test whether the 17-of-18 amino-acid completeness pattern persists across broader phylogenetic coverage. [^essential_metabolome]
- Combine GapMind with [eggnog](../entities/eggnog.md) EC-to-[kegg](../entities/kegg.md) pathway analysis to test whether independent annotation pipelines recover the same serine and carbon-source capacities. [^essential_metabolome]
- Link essential-gene calls directly to pathway membership and assay organisms in defined media to test whether predicted pathway completeness corresponds to condition-specific biosynthetic essentiality. [^essential_metabolome]
- Independently calibrate the condition-specific importance threshold against known essentials from essential_metabolome before interpreting Latent Capability reclassification as biological confirmation. [^pathway_capability_dependency]
- Stratify pathway gaps by phylogeny and ecology after expanding the sample to test whether nutrient dependence is associated with lineage or environment. [^essential_metabolome]
- Test whether accessory-dependent amino-acid pathways predict measured metabolite exchange in defined microbial communities rather than inferring sharing from gene-content differences alone. [^pathway_capability_dependency]
- Reanalyze the 48-organism capability dataset with direct GapMind gene assignments and matched condition-specific fitness assays to determine whether the carbon-versus-amino-acid latent-fraction contrast reflects biology or SEED-proxy and laboratory-condition biases. [^metabolic_capability_dependency]
- Use condition-matched fitness assays and pangenome conservation to test whether costly-and-conserved biosynthetic genes retain fitness in defined nutrient-limited media, rather than inferring natural purifying selection from rich-medium measurements. [^conservation_fitness_synthesis]

[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../summaries/conservation_fitness_synthesis__REPORT.md)
