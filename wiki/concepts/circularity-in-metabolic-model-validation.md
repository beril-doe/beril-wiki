---
type: "Concept"
description: "Gapfilled reactions can become assumptions rather than independent tests of model validity."
sources: ["summaries/annotation_gap_discovery__REPORT.md"]
---
# Gapfilled Models Can Make Their Own Validation Circular

[[summaries/annotation_gap_discovery__REPORT]] shows that validating a metabolic model with gene knockouts can become circular when the model requires the tested gapfilled reactions in order to grow on the selected conditions. [src: annotation_gap_discovery]

## The circularity problem

The study inserted 23 gene-protein-reaction (GPR) rules—formal links between genes and metabolic reactions—into SBML models for high- and medium-confidence candidate assignments. [src: annotation_gap_discovery] The models were then tested with gene-knockout simulations on minimal media containing the relevant carbon sources. [src: annotation_gap_discovery] These simulations produced zero wildtype growth. [src: annotation_gap_discovery]

The zero-growth result could not independently validate the candidate genes because the models required the corresponding gapfilled reactions themselves to grow on those carbon sources. [src: annotation_gap_discovery] Removing a gene associated with one of those reactions therefore removed a reaction that had already been introduced specifically to restore the model's growth prediction. [src: annotation_gap_discovery] The knockout result consequently reflected a dependency built into the model construction rather than an independent demonstration that the gene is biologically required. [src: annotation_gap_discovery]

## Why this matters for metabolic-model validation

The circularity concerns the distinction between model repair and model validation: gapfilling repairs a failed growth prediction by adding reactions, whereas validation must test predictions against evidence not used to create that repair. [src: annotation_gap_discovery] In this study, baseline flux-balance analysis (FBA), a constraint-based method for predicting metabolic flux and growth, achieved 42.5% overall accuracy across 574 organism-carbon source combinations, with recall of 86.5% (244 of 282 growth-positive conditions correctly predicted) and precision of 42.5% (244 of 574 growth predictions correct). [src: annotation_gap_discovery] The models produced 330 false positives, indicating that model permissiveness was already a substantial limitation before the knockout test. [src: annotation_gap_discovery]

Conditional gapfilling for 38 false-negative cases added 219 reactions, including 201 enzymatic, 14 transport, and 12 exchange reactions. [src: annotation_gap_discovery] Because the repaired reactions were selected to recover growth in those cases, using growth dependence on the same reactions as the principal knockout test could not distinguish a correct biological assignment from a computationally necessary repair. [src: annotation_gap_discovery] This limitation links the study to [[concepts/metabolic-model-gapfilling]] and to [[concepts/metabolic-model-validation]], where the validity of added reactions must be assessed independently of the objective that selected them. [src: annotation_gap_discovery]

## Scope of the evidence

The circularity finding applies specifically to the reported in-model knockout validation; it does not show that all 23 candidate GPR rules were incorrect. [src: annotation_gap_discovery] The broader annotation pipeline resolved 96 of 201 gapfilled enzymatic reaction-organism pairs (47.8%), including 44 high-confidence pairs (21.9%), 19 medium-confidence pairs (9.5%), and 33 low-confidence pairs (16.4%). [src: annotation_gap_discovery] Those confidence assignments combined evidence from homology, fitness, pangenome conservation, and annotation resources, but the knockout simulations did not provide an independent validation of the assignments in this model configuration. [src: annotation_gap_discovery]

The report therefore prioritizes targeted gene-knockout or CRISPRi validation of the 44 high-confidence gene-reaction assignments rather than treating the reported simulations as conclusive biological confirmation. [src: annotation_gap_discovery] CRISPRi is a gene-suppression method that can provide an experimental perturbation distinct from the model's internally imposed growth requirement. [src: annotation_gap_discovery] This distinction also connects the issue to [[concepts/gene-essentiality]] and [[concepts/essentiality-assay-discordance]], because computational essentiality and experimentally observed fitness effects should not be treated as interchangeable evidence. [src: annotation_gap_discovery]

## Tensions

The gapfilling pipeline produced candidate assignments that were supported by multiple evidence streams, while the in-model knockout validation was inconclusive because the tested reactions were required for model growth. [src: annotation_gap_discovery] Thus, the same model can be useful for prioritizing candidate genes while remaining unsuitable for independently validating those candidates through growth knockouts that depend on the repaired reactions. [src: annotation_gap_discovery]

## Open Directions

- Reconstruct the 38 false-negative cases with gapseq and compare growth predictions and knockout outcomes to test whether reducing the 330 false positives changes the circularity of validation. [src: annotation_gap_discovery]
- Experimentally test the 44 high-confidence assignments, prioritizing rxn02185 and rxn03436 across 9 organisms, using targeted gene knockouts or CRISPRi and matched carbon-source growth assays. [src: annotation_gap_discovery]
- Hold out carbon sources or fitness experiments during model repair, then evaluate the 23 GPR-linked candidates against the withheld data to ask whether candidate-dependent growth generalizes beyond the evidence used for gapfilling. [src: annotation_gap_discovery]
- Compare model predictions before and after removal of each candidate reaction and pair the simulations with direct mutant fitness measurements to determine whether loss of predicted growth reflects biological gene requirement or a gapfilling dependency. [src: annotation_gap_discovery]
