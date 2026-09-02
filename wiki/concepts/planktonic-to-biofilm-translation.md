---
type: "Concept"
description: "Planktonic inhibition does not establish protection in airway biofilms"
sources: ["summaries/cf_formulation_design__REPORT.md"]
---
# Planktonic Competition Assays Do Not Directly Establish Biofilm Protection in Cystic-Fibrosis Airways

Planktonic competition assays can identify candidate mechanisms and commensal combinations that inhibit *Pseudomonas aeruginosa* (PA), but they do not directly establish protection in cystic-fibrosis airways because PA primarily occupies structured biofilms in those lungs. [src: cf_formulation_design]

## Evidence Boundary

The [[summaries/cf_formulation_design__REPORT]] integrates planktonic inhibition, carbon-utilization profiling, growth kinetics, patient metagenomics and metatranscriptomics, pairwise interaction data, and pangenome analysis to design protective microbiome formulations. [src: cf_formulation_design]

In the 142-isolate cohort with both inhibition and carbon-utilization data, metabolic overlap with PA14 significantly predicted planktonic inhibition (r = 0.384, p = 2.3×10⁻⁶), while a multivariate metabolic model explained R² = 0.274 of inhibition variance and increased to R² = 0.360 after adding genus-level taxonomy. [src: cf_formulation_design]

Five-fold cross-validation yielded CV R² = 0.145 ± 0.142, indicating that the out-of-sample predictive power of the planktonic metabolic model was lower than its training fit. [src: cf_formulation_design]

The report therefore supports metabolic competition as a real but incomplete planktonic mechanism: approximately 73% of inhibition variance remained unexplained by metabolism alone, and genus contributed an additional 8.6% of explained variance, plausibly capturing species-specific direct-antagonism mechanisms. [src: cf_formulation_design]

## Why Planktonic Results Do Not Transfer Directly

The inhibition assays used planktonic cultures and PA14, whereas PA in cystic-fibrosis lungs primarily occupies structured biofilms, so measured inhibition is not a direct measurement of biofilm protection. [src: cf_formulation_design]

The carbon panel contained 22 tested substrates and omitted mucins, lipids, iron, polyamines, and the sugar alcohols identified genomically, leaving important airway resources and interactions untested in the planktonic assay system. [src: cf_formulation_design]

Growth kinetics also captured only selected planktonic properties: commensals exceeded PA14's maximum growth rate in 13.8% of substrate comparisons but began growing earlier in 43.1% of comparisons, and adding kinetics to the metabolic model increased the fit to R² = 0.311 for the 29 isolates with all three assay types. [src: cf_formulation_design]

These results support [[concepts/condition-specific-fitness]] by showing that substrate-specific growth and inhibition can vary with the measured condition, but they do not demonstrate that the same advantages persist in a spatially structured airway biofilm. [src: cf_formulation_design]

## Formulation Implications

The strict-safe optimization identified *Neisseria mucosa*, *Streptococcus salivarius*, *Micrococcus luteus*, *Rothia dentocariosa*, and *Gemella sanguinis* as a five-species core, while the recommended k=2 candidate of *R. dentocariosa* + *N. mucosa* provided 84% mean inhibition and combined engraftability 0.820. [src: cf_formulation_design]

The k=3 formulation of *M. luteus* + *N. mucosa* + *S. salivarius* achieved 100% PA14 niche coverage and 75% inhibition, but *M. luteus* had zero lung genomes and zero detected patient engraftability, making its contribution dependent on untested in vivo establishment. [src: cf_formulation_design]

The report recommends testing PAO1 and 3–5 mucoid clinical PA isolates because PA14-based inhibition measurements have not been validated against PAO1 or ExoS+ clinical strains, even though the pangenome analysis found no amino-acid pathway differences between ExoU+ and ExoS+ PA. [src: cf_formulation_design]

Pairwise interaction evidence is also insufficient for biofilm formulation claims: the analysis covered only 3 A × 3 B isolate combinations, the complete 10-pair interaction matrix for the five-species core has not been measured, and the overall mean synergy was −5.8% across only 8 comparisons and 5 unique pairs. [src: cf_formulation_design]

The formulation findings therefore **support** [[concepts/competitive-exclusion-consortium-design]] as a candidate-design framework, but they do not establish that planktonic inhibition will produce protection against established airway biofilms. [src: cf_formulation_design]

## Tensions

The report identifies strong planktonic candidate performance, including 88% best inhibition for *N. mucosa* and 79% for *R. dentocariosa*, while simultaneously acknowledging that the assay architecture does not reproduce the structured biofilm state that dominates cystic-fibrosis airways. [src: cf_formulation_design]

This tension is not a numerical contradiction: it marks a translation gap between direct planktonic measurements and the unmeasured biofilm-protection phenotype. [src: cf_formulation_design]

The multi-omics and pangenome evidence can refine candidate selection, but genomic pathway conservation and patient transcriptional activity do not by themselves demonstrate spatial colonization, biofilm competition, or protection from PA in vivo. [src: cf_formulation_design]

## Open Directions

- Test the proposed k=2 and k=3 formulations in mixed-species biofilm models using PA14, PAO1, and 3–5 mucoid clinical PA isolates to determine whether planktonic inhibition predicts biofilm biomass reduction or PA exclusion. [src: cf_formulation_design]
- Expand carbon and airway-medium assays to include mucins, lipids, iron, polyamines, xylitol, myoinositol, xylose, and arabinose, then measure whether the predicted commensal-to-PA growth advantages persist under biofilm conditions. [src: cf_formulation_design]
- Measure the complete 10-pair interaction matrix for the five-species core in spatially structured co-cultures to test whether the provisional pairwise synergy estimates generalize to the full formulation. [src: cf_formulation_design]
- Track formulation species by strain-resolved metagenomics and metatranscriptomics during biofilm growth or an airway-relevant model to test whether inferred engraftability predicts actual establishment and activity. [src: cf_formulation_design]
- Compare planktonic and biofilm phenotypes across the 22-substrate panel and the genomically nominated sugar alcohols and pentoses to quantify which condition-specific fitness measurements transfer between assay formats. [src: cf_formulation_design]
