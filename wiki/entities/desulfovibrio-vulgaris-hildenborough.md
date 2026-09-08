---
type: Organism
description: Anaerobic sulfate-reducing bacterium studied for metal fitness and gene
  function.
sources:
- id: counter_ion_effects
  resource: ../summaries/counter_ion_effects__REPORT.md
  title: counter ion effects
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: field_vs_lab_fitness
  resource: ../summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: lab_field_ecology
  resource: ../summaries/lab_field_ecology__REPORT.md
  title: lab field ecology
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: truly_dark_genes
  resource: ../summaries/truly_dark_genes__REPORT.md
  title: truly dark genes
title: Desulfovibrio vulgaris Hildenborough
---
# Desulfovibrio vulgaris Hildenborough

## What this entity is

**Canonical name:** Desulfovibrio vulgaris Hildenborough. [^counter_ion_effects]

**Known alias:** DvH. [^counter_ion_effects]

**Stable external identifier:** No stable external identifier is provided in this report. [^counter_ion_effects]

## Findings in counter_ion_effects

DvH was analyzed across 13 metals and 6 [sodium-chloride](sodium-chloride.md) experiments to assess whether shared NaCl and metal-fitness signals reflected counter-ion effects or broader stress biology. [^counter_ion_effects]

The whole-genome Pearson correlations between DvH metal-fitness profiles and NaCl fitness were: [zinc](zinc.md) r=0.715, manganese r=0.545, [copper](copper.md) r=0.532, [cobalt](cobalt.md) r=0.498, mercury r=0.478, [nickel](nickel.md) r=0.446, aluminum r=0.420, molybdenum r=0.396, uranium r=0.350, selenium r=0.342, chromium r=0.318, tungsten r=0.298, and iron r=0.086. [^counter_ion_effects]

This hierarchy supports the report's conclusion that chloride concentration was not the primary driver of the DvH metal–NaCl relationships, because zinc sulfate supplied 0 mM chloride yet produced the highest correlation, r=0.715. [^counter_ion_effects]

The report interprets the stronger correlations for zinc, manganese, copper, cobalt, mercury, and nickel as consistent with broad toxicity involving essential-cofactor displacement or disruption of multiple cellular systems; these mechanistic interpretations are extrapolations from fitness-profile correlations rather than direct biochemical tests. [^counter_ion_effects]

The lower correlations for molybdenum, uranium, selenium, chromium, tungsten, and iron are interpreted as consistent with more pathway-specific effects, with iron at r=0.086 described as affecting specific iron-dependent enzymes rather than causing general cellular damage; these interpretations remain hypotheses requiring direct functional testing. [^counter_ion_effects]

In the DvH gene-level analysis, 495 unique metal-important genes comprised 73 shared-stress genes (14.7%) and 422 metal-specific genes (85.3%). [^counter_ion_effects]

Among these DvH genes, 90.5% of metal-specific genes had SEED annotations, compared with 78.1% of shared-stress genes. [^counter_ion_effects]

## Findings in essential_metabolome and pathway_capability_dependency

[gapmind](gapmind.md) predicted complete or likely_complete biosynthesis for 17 of 18 amino-acid pathways in DvH, including a gap in serine biosynthesis; this **refines** interpretation of DvH fitness by adding a computationally predicted metabolic limitation, not a demonstrated viability requirement. [^essential_metabolome]

DvH was the only one of 7 analyzed organisms with fewer than 18 complete or likely_complete amino-acid pathways, at 17/18 and 94.4%; the result suggests the hypothesis of serine auxotrophy but may reflect a non-canonical pathway, divergent enzyme, or annotation limitation. [^essential_metabolome]

The report describes DvH as an anaerobic sulfate-reducing bacterium associated with organic-rich environments where externally available amino acids could support growth, but this ecological interpretation is not an established mechanism. [^essential_metabolome]

DvH was one of the 7 Tier 1 organisms with matching GapMind and Fitness Browser data in the pathway-capability analysis, which **supports** using it to compare predicted pathway completeness with experimentally observed fitness rather than treating computational capability as dependency. [^pathway_capability_dependency]

That analysis classified 161 organism–pathway pairs across 7 model bacteria into Active Dependency, Latent Capability, Incomplete but Important, and Missing categories; no DvH-specific category assignment is reported here. [^pathway_capability_dependency]

These computational findings **support** retaining [condition-specific-fitness](../concepts/condition-specific-fitness.md) as the relevant context: rich-media RB-TnSeq, or random-barcode transposon sequencing, can obscure biosynthetic requirements when nutrients are supplied, so serine-free minimal-medium growth testing is needed. [^essential_metabolome]

The DvH results contribute to [condition-specific-fitness](../concepts/condition-specific-fitness.md) by separating shared NaCl-associated stress responses from metal-specific fitness responses, and to [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) through whole-genome cross-condition correlation evidence. [^counter_ion_effects]

## Findings in truly_dark_genes

The truly-dark-gene analysis **refines** the existing annotation-limitation caveat for DvH: DvH/206658 was ranked as a top candidate with score 9, a stress phenotype of |f| = 5.4, and an [eggnog](eggnog.md) signal suggesting “trehalose synthase” despite its hypothetical annotation. [^truly_dark_genes] This candidate links DvH’s condition-specific fitness evidence to [functional-dark-matter](../concepts/functional-dark-matter.md), while the suggested function remains a hypothesis requiring experimental validation. [^truly_dark_genes]

DvH contributed 13 of the 100 prioritized truly dark genes across 19 organisms. [^truly_dark_genes] This **supports** using DvH fitness phenotypes and genomic context to prioritize functional characterization, but does not establish that the candidate phenotype is caused directly by the hypothetical gene because polar effects can occur. [^truly_dark_genes]

## Findings in field_vs_lab_fitness

A further analysis classified 757 DvH [kescience-fitnessbrowser](kescience-fitnessbrowser.md) experiments and integrated their condition-specific fitness with [pangenome-integration](../concepts/pangenome-integration.md) data. [^field_vs_lab_fitness] Among 2,725 non-essential genes with both fitness and pangenome links, 76.3% were core overall; 678 essential genes were 80.1% core but lacked fitness data because no transposon mutants were recovered. [^field_vs_lab_fitness]

This **supports** the existing condition-specific interpretation: fitness importance, rather than field-versus-lab classification, best predicted conservation. At fitness < -2, field-stress genes were 83.6% core (298 genes; OR=1.58, FDR q=0.026), whereas heavy-metals genes were 71.2% core (198 genes; OR=0.77, q=0.14) and lab-antibiotic genes were 73.4% core (109 genes; OR=0.86, q=0.49). [^field_vs_lab_fitness] The result **refines** the metal-fitness findings above by supporting the hypothesis that some specific metal-resistance mechanisms are accessory, while uranium- and mercury-related responses may involve more conserved stress functions; this is an inference, not a direct mobile-element or biochemical measurement. [^field_vs_lab_fitness]

The field-versus-lab analysis was limited to this single organism, used manually classified conditions, and excluded the 678 essential genes from fitness comparisons; these constraints limit generalization and may compress conservation differences. [^field_vs_lab_fitness]

## Findings in lab_field_ecology

The Oak Ridge field comparison **refines** the preceding lab-to-field interpretation: the represented Desulfovibrio model organism occurred in 34% of 108 groundwater sites and reached a maximum relative abundance of 0.09%, but its abundance had no detectable uranium association (Spearman rho=0.022, p=0.82). [^lab_field_ecology] This single genus-level result does not contradict the DvH fitness measurements; it instead supports treating translation from laboratory metal fitness to field abundance as condition- and context-dependent. [^lab_field_ecology]

The report identifies low Desulfovibrio abundance, genus-level rather than strain-level matching, multidimensional niche requirements, competition and cross-feeding, and temporal mismatch between geochemical snapshots and community history as possible explanations for the laboratory–field disconnect; these are proposed explanations rather than demonstrated mechanisms. [^lab_field_ecology]

## Limitations

The DvH metal–NaCl correlations are fitness-profile associations and do not by themselves establish the biochemical mechanism of metal toxicity. [^counter_ion_effects]

The report's within-metal salt comparison was performed in Pseudomonas stutzeri RCH2 rather than DvH, so it does not provide a matched-salt test for this organism. [^counter_ion_effects]

GapMind predictions are computational; validating the apparent serine gap requires lower-confidence prediction review, literature checking, and growth testing on serine-free minimal medium. [^essential_metabolome]

The pathway-capability comparison was limited to 7 of 48 Fitness Browser organisms with matching GapMind genome data, and the model-organism set had near-complete core genomes; this **refines** the interpretation of DvH conservation comparisons by limiting their generalizability. [^pathway_capability_dependency]

The pathway analysis used KEGG-based mapping, which can miss genes lacking KEGG annotations or carrying incorrect annotations, potentially underestimating pathway-assigned genes. [^pathway_capability_dependency]

The truly-dark-gene candidate interpretation is additionally limited because short genes are harder to annotate and measure, and some strong fitness phenotypes may reflect polar effects on downstream genes. [^truly_dark_genes]

The field-versus-lab results are from a single-organism analysis, and gene length, subjective condition classification, small field-specific and lab-specific sets, and the absence of mutants for essential genes constrain interpretation. [^field_vs_lab_fitness]

The Oak Ridge comparison is additionally limited because 16S amplicon sequencing resolves only to genus level and the field analysis does not control pH, dissolved oxygen, carbon sources, or other confounders. [^lab_field_ecology]

## Related pages

- [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md) — source summary for the counter-ion analysis.
- [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md) — source summary for GapMind pathway analysis.
- [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) — source summary for pathway capability versus fitness dependency.
- [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md) — source summary for field-versus-lab gene-importance analysis.
- [lab_field_ecology__REPORT](../summaries/lab_field_ecology__REPORT.md) — source summary for the Oak Ridge lab-to-field comparison.
- [truly_dark_genes__REPORT](../summaries/truly_dark_genes__REPORT.md) — source summary for persistent hypothetical genes and DvH candidate prioritization.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — shared and metal-specific condition responses.
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — cross-condition fitness-profile architecture.
- [gene-essentiality](../concepts/gene-essentiality.md) — interpretation of gene-level fitness and core-enrichment analyses.
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — computational pathway-completeness evidence and validation gaps.
- [functional-dark-matter](../concepts/functional-dark-matter.md) — residual unknown-gene function and candidate prioritization.

[^counter_ion_effects]: [counter ion effects](../summaries/counter_ion_effects__REPORT.md)
[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^truly_dark_genes]: [truly dark genes](../summaries/truly_dark_genes__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
[^lab_field_ecology]: [lab field ecology](../summaries/lab_field_ecology__REPORT.md)
