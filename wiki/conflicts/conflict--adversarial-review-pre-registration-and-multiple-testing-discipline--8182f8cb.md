<!-- tension-hash: 8182f8cb5a8ecc47 -->
# Tension: Review Closure and Pre-registration Claims Versus Residual Gaps in Reported Rigor

Several projects describe their adversarial review (a review deliberately designed to find flaws) and pre-registration (stating hypotheses and analysis plans before seeing data) in ways that sit uneasily with other statements in the same reports. In gene_function_ecological_agora the count of review rounds is given as 8 and as 9, and post-hoc revision is both defended and conceded. In microbeatlas_metal_ecology a result is called independent of robustness checks although the plan was not preregistered. In plant_microbiome_ecotypes all five review issues are closed, yet gaps remain. This matters because readers use review closure and pre-registration as signals of trust. The tension comes from [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## Evidence Sides

**Side A: rigor is documented and issues are closed**
- One statement says 8 adversarial review rounds were integrated in gene_function_ecological_agora. [src: gene_function_ecological_agora]
- The same report says most revisions came from biology engagement and not data accommodation. [src: gene_function_ecological_agora]
- microbeatlas_metal_ecology calls its confirmatory result independent of the robustness analyses. [src: microbeatlas_metal_ecology]
- plant_microbiome_ecotypes reports that all five adversarial-review issues were closed. [src: plant_microbiome_ecotypes]

**Side B: the record shows residual or inconsistent discipline**
- Another statement refers to 9 adversarial review rounds, including REVIEW_9. [src: discoveries, gene_function_ecological_agora]
- The gene_function_ecological_agora report also says the cumulative count shows pre-registration was insufficiently calibrated. [src: gene_function_ecological_agora]
- The analysis plan of microbeatlas_metal_ecology was not preregistered. [src: microbeatlas_metal_ecology]
- plant_microbiome_ecotypes reports that H1 lacks the planned phylogenetic control (a correction for shared ancestry) and that the 15-marker shuffle had no multiple-testing correction (adjustment for running many tests). [src: plant_microbiome_ecotypes]

## Possible Reconciliations

- **Hypothesis: counting convention.** The 8 and 9 may differ because REVIEW_9 was added after the integrated set, or because one count excludes it. The tension text does not say.
- **Hypothesis: different senses of independence.** Independence from robustness analyses may be a statement about analysis dependence, not about pre-registration, so both microbeatlas_metal_ecology statements could hold.
- **Hypothesis: closure means addressed, not fully fixed.** A closed issue may be documented as a limitation. That would let plant_microbiome_ecotypes be consistent, though it would not remove the missing control or correction.
- **Hypothesis: revisions were biology-driven yet still signal weak pre-registration.** Both gene_function_ecological_agora statements could be true if the plan was too uncalibrated to anticipate legitimate changes.

## Resolving Work

- Audit the review files of gene_function_ecological_agora, including REVIEW_9, against the changelog, asking which count is correct and what each round changed.
- Classify each revision in gene_function_ecological_agora by trigger (biology engagement or data accommodation) using the revision log, and ask whether data-driven changes cluster after results were seen.
- Define independence for microbeatlas_metal_ecology and rerun its confirmatory test with a documented, time-stamped plan, asking whether the conclusion holds.
- Add the planned phylogenetic control to H1 in plant_microbiome_ecotypes, using a phylogenetic regression, and ask whether the effect survives.
- Apply a multiple-testing correction to the 15-marker shuffle in plant_microbiome_ecotypes, asking which markers remain significant.
