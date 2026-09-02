---
type: "Organism"
description: "Shewanella oneidensis MR1, a model organism for fitness and pathway analysis."
sources: ["summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Shewanella oneidensis

## What this entity is

**Shewanella oneidensis** is the canonical organism name used for the MR1 strain in the essential-metabolome analysis. [src: essential_metabolome]

- **Known alias:** MR1. [src: essential_metabolome]
- **Genome identifier:** GCF_000146165.2. [src: essential_metabolome]

## Key facts from the essential-metabolome analysis

*Shewanella oneidensis* (MR1) was one of 7 organisms successfully mapped for the pilot comparison of essential-gene organisms using [[entities/gapmind]] pathway-completeness predictions. [src: essential_metabolome]

MR1 had complete predictions for 18 of 18 amino-acid biosynthesis pathways, corresponding to 100% pathway completeness in the analysis. [src: essential_metabolome] The 18 pathways assessed were arg, asn, chorismate, cys, gln, gly, his, ile, leu, lys, met, phe, pro, thr, trp, tyr, and val; MR1 was complete for all 18. [src: essential_metabolome]

The analysis reported 694 raw [[entities/gapmind]] predictions for the MR1 genome, GCF_000146165.2. [src: essential_metabolome] MR1 was included in a pilot rather than a pan-bacterial assessment because only 7 organisms were mapped successfully from an underlying collection containing 45 organisms. [src: essential_metabolome]

The pathway-capability analysis **supports and extends** this pilot placement: *S. oneidensis* was one of the 7 Tier 1 organisms with matching GapMind and Fitness Browser data, among 48 Fitness Browser organisms considered. [src: pathway_capability_dependency] The broader analysis classified organism–pathway pairs by both GapMind capability and experimentally observed fitness dependency, thereby **refining** the interpretation of MR1’s complete pathway calls rather than treating completeness as proof of requirement. [src: pathway_capability_dependency]

## Fitness and functional-dark-matter integration

The functional-dark-matter analysis **refines** the pilot’s pathway-completeness view by placing MR1 in a broader Fitness Browser prioritization: MR-1 contributed 25 of the top 100 phenotype-bearing dark-gene candidates across 22 organisms. [src: functional_dark_matter]

MR-1 202463 was among the highest-ranked fitness-active candidates, with |fit| = 6.4 under stress and a YGGT domain prediction. [src: functional_dark_matter] The analysis also identified the MR-1 K03306 paralog trio 199738, 203545, and 202450, with nitrogen-associated fitness effects of 5.5, 4.0, and 3.9 respectively. [src: functional_dark_matter]

This **supports** using MR1 as an experimental priority beyond the rich-media essential-metabolome pilot: the first three experiments in a greedy set-cover sequence—MR-1 stress, nitrogen source, and carbon source—would address 111 of the top 500 dark genes (20.8%). [src: functional_dark_matter] These fitness results do not establish that the complete amino-acid pathways identified by [[entities/gapmind]] are individually required for viability; they instead add condition-specific evidence for other, poorly characterized genes. [src: functional_dark_matter]

The truly-dark-gene analysis **refines** this prioritization by using a stricter set: genes hypothetical in both the original pipeline and Bakta. MR-1 contributed 8 of the top 100 candidates in that separate ranking across 19 organisms; this is not a contradiction of the earlier count of 25 because the analyses rank different dark-gene populations. [src: truly_dark_genes] The MR-1-specific candidates and their underlying evidence are detailed in [[summaries/truly_dark_genes__REPORT]]. [src: truly_dark_genes]

## Interpretation and limitations

The MR1 result contributes to the observation that 17 of 18 amino-acid biosynthesis pathways were present in all 7 analyzed organisms, although the small and phylogenetically restricted sample limits generalization to bacteria as a whole. [src: essential_metabolome]

The pathway calls were computational [[entities/gapmind]] predictions rather than experimental measurements, and complete or likely_complete calls can miss non-canonical pathways, divergent enzymes, or genes absent from genome annotations. [src: essential_metabolome] The essential-gene context came from rich-media [[entities/tnseq]] experiments, meaning nutrient supplementation could make biosynthetic genes appear non-essential; the analysis therefore does not establish that MR1’s complete pathways are individually required for viability. [src: essential_metabolome]

The functional-dark-matter rankings also require caution because Fitness Browser condition coverage is uneven, and MR-1 has 121 historical conditions; deeper condition coverage can produce more specific phenotypes and higher prioritization scores. [src: functional_dark_matter] The new capability–dependency framework **reinforces** this caution: across its 161 organism–pathway pairs, complete pathways could lack fitness defects under standard conditions yet become important under other tested conditions, while the condition-specific median threshold may itself drive some reclassifications. [src: pathway_capability_dependency]

The truly-dark ranking should likewise be interpreted as a prioritization rather than a demonstrated function: the report notes that short genes can be harder to measure for fitness and that strong phenotypes may reflect polar effects on downstream genes. [src: truly_dark_genes]

## Related pages

- [[summaries/essential_metabolome__REPORT]] — source report for the essential-metabolome pilot. [src: essential_metabolome]
- [[summaries/functional_dark_matter__REPORT]] — source report for experimentally prioritized dark-gene systems. [src: functional_dark_matter]
- [[summaries/pathway_capability_dependency__REPORT]] — source report linking pathway capability with fitness dependency. [src: pathway_capability_dependency]
- [[summaries/truly_dark_genes__REPORT]] — source report distinguishing persistent hypothetical genes from annotation-lag genes. [src: truly_dark_genes]
- [[concepts/metabolic-model-gapfilling]] — cross-project context for GapMind pathway-completeness analysis. [src: essential_metabolome]
- [[concepts/gene-essentiality]] — context for essential-gene measurements and pathway completeness. [src: essential_metabolome]
- [[concepts/condition-specific-fitness]] — context for rich-media conditions and nutrient-dependent fitness interpretation. [src: essential_metabolome]
