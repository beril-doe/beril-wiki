---
type: "Organism"
description: "Anaerobic sulfate-reducing bacterium studied for metal fitness and gene function."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/lab_field_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Desulfovibrio vulgaris Hildenborough

## What this entity is

**Canonical name:** Desulfovibrio vulgaris Hildenborough. [src: counter_ion_effects]

**Known alias:** DvH. [src: counter_ion_effects]

**Stable external identifier:** No stable external identifier is provided in this report. [src: counter_ion_effects]

## Findings in counter_ion_effects

DvH was analyzed across 13 metals and 6 [[entities/sodium-chloride]] experiments to assess whether shared NaCl and metal-fitness signals reflected counter-ion effects or broader stress biology. [src: counter_ion_effects]

The whole-genome Pearson correlations between DvH metal-fitness profiles and NaCl fitness were: [[entities/zinc]] r=0.715, manganese r=0.545, [[entities/copper]] r=0.532, [[entities/cobalt]] r=0.498, mercury r=0.478, [[entities/nickel]] r=0.446, aluminum r=0.420, molybdenum r=0.396, uranium r=0.350, selenium r=0.342, chromium r=0.318, tungsten r=0.298, and iron r=0.086. [src: counter_ion_effects]

This hierarchy supports the report's conclusion that chloride concentration was not the primary driver of the DvH metal–NaCl relationships, because zinc sulfate supplied 0 mM chloride yet produced the highest correlation, r=0.715. [src: counter_ion_effects]

The report interprets the stronger correlations for zinc, manganese, copper, cobalt, mercury, and nickel as consistent with broad toxicity involving essential-cofactor displacement or disruption of multiple cellular systems; these mechanistic interpretations are extrapolations from fitness-profile correlations rather than direct biochemical tests. [src: counter_ion_effects]

The lower correlations for molybdenum, uranium, selenium, chromium, tungsten, and iron are interpreted as consistent with more pathway-specific effects, with iron at r=0.086 described as affecting specific iron-dependent enzymes rather than causing general cellular damage; these interpretations remain hypotheses requiring direct functional testing. [src: counter_ion_effects]

In the DvH gene-level analysis, 495 unique metal-important genes comprised 73 shared-stress genes (14.7%) and 422 metal-specific genes (85.3%). [src: counter_ion_effects]

Among these DvH genes, 90.5% of metal-specific genes had SEED annotations, compared with 78.1% of shared-stress genes. [src: counter_ion_effects]

## Findings in essential_metabolome and pathway_capability_dependency

[[entities/gapmind]] predicted complete or likely_complete biosynthesis for 17 of 18 amino-acid pathways in DvH, including a gap in serine biosynthesis; this **refines** interpretation of DvH fitness by adding a computationally predicted metabolic limitation, not a demonstrated viability requirement. [src: essential_metabolome]

DvH was the only one of 7 analyzed organisms with fewer than 18 complete or likely_complete amino-acid pathways, at 17/18 and 94.4%; the result suggests the hypothesis of serine auxotrophy but may reflect a non-canonical pathway, divergent enzyme, or annotation limitation. [src: essential_metabolome]

The report describes DvH as an anaerobic sulfate-reducing bacterium associated with organic-rich environments where externally available amino acids could support growth, but this ecological interpretation is not an established mechanism. [src: essential_metabolome]

DvH was one of the 7 Tier 1 organisms with matching GapMind and Fitness Browser data in the pathway-capability analysis, which **supports** using it to compare predicted pathway completeness with experimentally observed fitness rather than treating computational capability as dependency. [src: pathway_capability_dependency]

That analysis classified 161 organism–pathway pairs across 7 model bacteria into Active Dependency, Latent Capability, Incomplete but Important, and Missing categories; no DvH-specific category assignment is reported here. [src: pathway_capability_dependency]

These computational findings **support** retaining [[concepts/condition-specific-fitness]] as the relevant context: rich-media RB-TnSeq, or random-barcode transposon sequencing, can obscure biosynthetic requirements when nutrients are supplied, so serine-free minimal-medium growth testing is needed. [src: essential_metabolome]

The DvH results contribute to [[concepts/condition-specific-fitness]] by separating shared NaCl-associated stress responses from metal-specific fitness responses, and to [[concepts/cofitness-network-architecture]] through whole-genome cross-condition correlation evidence. [src: counter_ion_effects]

## Findings in truly_dark_genes

The truly-dark-gene analysis **refines** the existing annotation-limitation caveat for DvH: DvH/206658 was ranked as a top candidate with score 9, a stress phenotype of |f| = 5.4, and an [[entities/eggnog]] signal suggesting “trehalose synthase” despite its hypothetical annotation. [src: truly_dark_genes] This candidate links DvH’s condition-specific fitness evidence to [[concepts/genomic-under-representation]], while the suggested function remains a hypothesis requiring experimental validation. [src: truly_dark_genes]

DvH contributed 13 of the 100 prioritized truly dark genes across 19 organisms. [src: truly_dark_genes] This **supports** using DvH fitness phenotypes and genomic context to prioritize functional characterization, but does not establish that the candidate phenotype is caused directly by the hypothetical gene because polar effects can occur. [src: truly_dark_genes]

## Findings in field_vs_lab_fitness

A further analysis classified 757 DvH [[entities/kescience-fitnessbrowser]] experiments and integrated their condition-specific fitness with [[concepts/pangenome-integration]] data. [src: field_vs_lab_fitness] Among 2,725 non-essential genes with both fitness and pangenome links, 76.3% were core overall; 678 essential genes were 80.1% core but lacked fitness data because no transposon mutants were recovered. [src: field_vs_lab_fitness]

This **supports** the existing condition-specific interpretation: fitness importance, rather than field-versus-lab classification, best predicted conservation. At fitness < -2, field-stress genes were 83.6% core (298 genes; OR=1.58, FDR q=0.026), whereas heavy-metals genes were 71.2% core (198 genes; OR=0.77, q=0.14) and lab-antibiotic genes were 73.4% core (109 genes; OR=0.86, q=0.49). [src: field_vs_lab_fitness] The result **refines** the metal-fitness findings above by supporting the hypothesis that some specific metal-resistance mechanisms are accessory, while uranium- and mercury-related responses may involve more conserved stress functions; this is an inference, not a direct mobile-element or biochemical measurement. [src: field_vs_lab_fitness]

The field-versus-lab analysis was limited to this single organism, used manually classified conditions, and excluded the 678 essential genes from fitness comparisons; these constraints limit generalization and may compress conservation differences. [src: field_vs_lab_fitness]

## Findings in lab_field_ecology

The Oak Ridge field comparison **refines** the preceding lab-to-field interpretation: the represented Desulfovibrio model organism occurred in 34% of 108 groundwater sites and reached a maximum relative abundance of 0.09%, but its abundance had no detectable uranium association (Spearman rho=0.022, p=0.82). [src: lab_field_ecology] This single genus-level result does not contradict the DvH fitness measurements; it instead supports treating translation from laboratory metal fitness to field abundance as condition- and context-dependent. [src: lab_field_ecology]

The report identifies low Desulfovibrio abundance, genus-level rather than strain-level matching, multidimensional niche requirements, competition and cross-feeding, and temporal mismatch between geochemical snapshots and community history as possible explanations for the laboratory–field disconnect; these are proposed explanations rather than demonstrated mechanisms. [src: lab_field_ecology]

## Limitations

The DvH metal–NaCl correlations are fitness-profile associations and do not by themselves establish the biochemical mechanism of metal toxicity. [src: counter_ion_effects]

The report's within-metal salt comparison was performed in Pseudomonas stutzeri RCH2 rather than DvH, so it does not provide a matched-salt test for this organism. [src: counter_ion_effects]

GapMind predictions are computational; validating the apparent serine gap requires lower-confidence prediction review, literature checking, and growth testing on serine-free minimal medium. [src: essential_metabolome]

The pathway-capability comparison was limited to 7 of 48 Fitness Browser organisms with matching GapMind genome data, and the model-organism set had near-complete core genomes; this **refines** the interpretation of DvH conservation comparisons by limiting their generalizability. [src: pathway_capability_dependency]

The pathway analysis used KEGG-based mapping, which can miss genes lacking KEGG annotations or carrying incorrect annotations, potentially underestimating pathway-assigned genes. [src: pathway_capability_dependency]

The truly-dark-gene candidate interpretation is additionally limited because short genes are harder to annotate and measure, and some strong fitness phenotypes may reflect polar effects on downstream genes. [src: truly_dark_genes]

The field-versus-lab results are from a single-organism analysis, and gene length, subjective condition classification, small field-specific and lab-specific sets, and the absence of mutants for essential genes constrain interpretation. [src: field_vs_lab_fitness]

The Oak Ridge comparison is additionally limited because 16S amplicon sequencing resolves only to genus level and the field analysis does not control pH, dissolved oxygen, carbon sources, or other confounders. [src: lab_field_ecology]

## Related pages

- [[summaries/counter_ion_effects__REPORT]] — source summary for the counter-ion analysis.
- [[summaries/essential_metabolome__REPORT]] — source summary for GapMind pathway analysis.
- [[summaries/pathway_capability_dependency__REPORT]] — source summary for pathway capability versus fitness dependency.
- [[summaries/field_vs_lab_fitness__REPORT]] — source summary for field-versus-lab gene-importance analysis.
- [[summaries/lab_field_ecology__REPORT]] — source summary for the Oak Ridge lab-to-field comparison.
- [[summaries/truly_dark_genes__REPORT]] — source summary for persistent hypothetical genes and DvH candidate prioritization.
- [[concepts/condition-specific-fitness]] — shared and metal-specific condition responses.
- [[concepts/cofitness-network-architecture]] — cross-condition fitness-profile architecture.
- [[concepts/gene-essentiality]] — interpretation of gene-level fitness and core-enrichment analyses.
- [[concepts/metabolic-model-gapfilling]] — computational pathway-completeness evidence and validation gaps.
- [[concepts/genomic-under-representation]] — residual unknown-gene function and candidate prioritization.
