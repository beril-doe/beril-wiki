---
type: "Concept"
description: "What laboratory knockout fitness data can and cannot say about rare or novel genes and about conservation, including coverage and condition biases."
sources: ["summaries/fitness_effects_conservation__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Fitness measurement of novel singleton genes and assay limits

Novel singleton genes show near-zero mean fitness in the [[entities/fitness-browser]] analysis, but coverage, condition and design caveats limit what that means. [src: fitness_effects_conservation] The evidence comes from [[summaries/fitness_effects_conservation__REPORT]] and [[summaries/truly_dark_genes__REPORT]].

## What the fitness data show for novel genes

Novel singleton genes have near-zero mean fitness. The report reads this as little detectable benefit or detriment under the tested laboratory conditions. [src: fitness_effects_conservation] They are not systematically detrimental, and their mean fitness is similar to that of auxiliary genes. [src: fitness_effects_conservation] The report describes them as largely invisible to lab-based fitness assays. [src: fitness_effects_conservation]

## Limits of the assay

- **Condition bias.** The laboratory conditions favour rich media and standard stresses, so many ecological niches are unrepresented. [src: fitness_effects_conservation]
- **Coverage.** The Fitness Browser covers 43 bacteria, mostly Proteobacteria, which limits generalizability. [src: fitness_effects_conservation]
- **Missing data.** Singleton or novel genes may lack fitness data because of poor transposon coverage, not because they are truly neutral. [src: fitness_effects_conservation]
- **Single knockouts.** Measurements are for single-gene knockouts, so epistatic interactions are not captured. [src: fitness_effects_conservation]
- **Weak prediction of conservation.** The report calls its 16pp gradient statistically robust, but says it means fitness importance only weakly predicts conservation. [src: fitness_effects_conservation] See [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]].

## Confounds for dark genes

The truly dark gene analysis adds two measurement confounds. Short genes are harder to annotate because they have fewer domains and fewer homologs. They are also harder to measure fitness for because they have fewer TA sites. The gene-length difference (d = −0.432) may therefore partly explain other differences between truly dark and annotation-lag genes. [src: truly_dark_genes] Some strong fitness phenotypes may also reflect polar effects on downstream genes, not the function of the dark gene itself. [src: truly_dark_genes] Related pages: [[concepts/condition-specific-fitness-of-dark-genes]], [[concepts/sequence-composition-and-conservation-of-unannotatable-genes]] and [[entities/random-barcode-transposon-sequencing]].

## Open Directions

- Test whether singleton genes with poor transposon coverage differ in mean fitness from well-covered ones. This would separate missing data from true neutrality.
- Repeat the singleton analysis with gene length as a covariate or in length-matched sets. This would show how much of the near-zero signal comes from short genes.
- Check strong phenotypes of dark genes for polar effects by looking at neighbouring genes in the same operon.
- Extend the analysis to organisms outside Proteobacteria and to niche-relevant conditions. This would address the coverage and condition biases.
