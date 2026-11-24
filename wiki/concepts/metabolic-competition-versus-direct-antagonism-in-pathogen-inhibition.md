---
type: "Concept"
description: "How much of commensal inhibition of Pseudomonas aeruginosa is explained by overlap in substrate use versus taxon-specific direct antagonism, including model overfitting caveats; stops at formulation selection."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/discoveries.md"]
---
# Metabolic competition versus direct antagonism in pathogen inhibition

The strongest inhibitors combine both mechanisms. [src: cf_formulation_design] Cross-validation shows the model overfits, so effect sizes need conservative reading. [src: cf_formulation_design] The page stops at formulation selection (see [[concepts/multi-criterion-design-of-protective-microbiome-formulations]]).

## Metabolic competition: real but partial

Metabolic overlap with PA14, weighted by PA14's substrate preferences, significantly predicts planktonic inhibition across the 142 isolates (r = 0.384, p = 2.3×10⁻⁶). [src: cf_formulation_design] The discoveries digest lists the preferred amino acids as proline, histidine, ornithine, glutamate and aspartate, and gives R²=27.4%. [src: discoveries] A multivariate model with metabolic overlap, total growth on PA-preferred substrates, metabolic breadth and maximum growth explains R² = 0.274. [src: cf_formulation_design] The report calls this the first quantification of metabolic competition's predictive power for PA14 inhibition. It describes resource competition as real but partial. [src: cf_formulation_design] It attributes approximately 27% of variance to this "eat their lunch" mechanism. [src: cf_formulation_design] It judges hypothesis H1 (metabolic competition) supported but incomplete, with approximately 73% of variance unexplained by metabolism alone. [src: cf_formulation_design] Overall, the report's data support a model in which effective formulations suppress P. aeruginosa through at least three mechanisms at once. [src: cf_formulation_design]

## Direct antagonism beyond metabolism

Adding genus-level taxonomy raises R² to 0.360, an additional 8.6% of variance. The report reads this as intrinsic species-level mechanisms, likely direct antagonism, acting independently of metabolism. [src: cf_formulation_design] Elsewhere it gives the figure as an additional 9% from taxonomy. It names likely bacteriocins, secreted enzymes or contact-dependent killing. [src: cf_formulation_design] The report treats isolates whose inhibition substantially exceeds metabolic predictions as candidate direct antagonists. [src: cf_formulation_design]

The largest positive residuals are:

| Isolate | Residual |
|---|---|
| Streptococcus salivarius ASMA-737 | +74.1% [src: cf_formulation_design] |
| Gemella sanguinis ASMA-3044 | +62.2% [src: cf_formulation_design] |
| Neisseria mucosa ASMA-3643 | +57.2% [src: cf_formulation_design] |

S. salivarius, N. mucosa and G. sanguinis all show strong positive residuals in the metabolic model. [src: cf_formulation_design] These species dominate the report's FDA-safe formulations. The report suggests they combine metabolic competition with direct antagonism. [src: cf_formulation_design] The dual-mechanism species show 57–74% more inhibition than their metabolic overlap predicts. [src: cf_formulation_design, discoveries] Species-level residuals are reported as S. salivarius +74%, G. sanguinis +62% and Rothia dentocariosa +57%. [src: cf_formulation_design] R. dentocariosa and N. mucosa are both dual-mechanism inhibitors. [src: cf_formulation_design] See also [[entities/streptococcus-salivarius]], [[entities/rothia-dentocariosa]] and [[entities/neisseria-mucosa]].

For R. dentocariosa, the report cites published work. Stubbendieck et al. (2023) identified a peptidoglycan endopeptidase that inhibits Moraxella catarrhalis. [src: cf_formulation_design] They also demonstrated colonization resistance in the nasal tract. [src: cf_formulation_design] The report proposes, as a hypothesis, that its isolates use similar mechanisms and that this explains their high residuals. [src: cf_formulation_design] The report presents dual-mechanism species as a formulation design principle not previously articulated for respiratory pathogens. [src: cf_formulation_design]

The report proposes comparative genomics of the top direct antagonists (ASMA-737 S. salivarius, ASMA-3044 G. sanguinis, ASMA-3643 N. mucosa) against low-inhibition isolates of the same species. It would search for bacteriocin gene clusters, type VI secretion system (T6SS) loci and secreted enzymes. [src: cf_formulation_design]

## Overfitting and unexplained variance

Five-fold cross-validation (CV) gives CV R² = 0.145 ± 0.142, below the training R² of 0.274. This indicates overfitting to the cohort. [src: cf_formulation_design] The report estimates out-of-sample power is closer to 15% than 27%. It says the qualitative conclusion stands, because metabolic overlap is still a significant predictor (p = 2.3×10⁻⁶), but the effect size should be read conservatively. [src: cf_formulation_design] The report suggests the remaining 64% of variance reflects unmeasured biofilm dynamics, pH effects, iron competition, quorum sensing interference and stochastic variation in the planktonic assay. [src: cf_formulation_design] These are proposed explanations, not measured ones.

## Use in formulation selection

The report adds R. dentocariosa for lung tropism and direct antagonism depth. [src: cf_formulation_design] It uses S. salivarius as the direct antagonism backbone. [src: cf_formulation_design] G. sanguinis adds depth at k=5. [src: cf_formulation_design] The k=2 formulation has 84% mean per-organism inhibition. This suggests the hypothesis that direct antagonism may matter more than niche coverage for clinical efficacy, which a proposed mouse model could test. [src: cf_formulation_design] See [[summaries/cf_formulation_design__REPORT]] and [[summaries/discoveries]].

## Open Directions

- Run the comparative genomics of top antagonists versus low-inhibition conspecifics described above, to test whether the residuals have a genetic basis.
- Test the direct-antagonism-versus-niche-coverage hypothesis in the proposed mouse model.
- Add biofilm, pH, iron and quorum-sensing measurements to the model, to test whether they account for the unexplained variance.
- Validate the model on isolates held out from the 142-isolate cohort, to replace the cross-validated estimate (0.145 ± 0.142) with an independent one.
