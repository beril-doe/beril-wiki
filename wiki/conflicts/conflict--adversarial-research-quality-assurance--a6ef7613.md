<!-- tension-hash: a6ef7613e8385ddb -->
# Report Prose Versus Report Tables: Which Stated Figure Stands?

Several project reports in this corpus state figures in their prose that disagree with the figures in their own tables. [src: bacdive_phenotype_metal_tolerance, bacillota_b_subsurface_accessory, caulobacter_fur_lipida_loss, cf_formulation_design, enigma_carbon_census_1, ibd_phage_targeting, lab_field_ecology, pitfalls, plant_microbiome_ecotypes, snipe_defense_system, truly_dark_genes] This matters because the wiki copies numbers exactly and never reconciles conflicting numbers silently. When a report contradicts itself, any single number carried into a concept page quietly takes one side. The disagreement falls under [[concepts/adversarial-research-quality-assurance]], which treats challenging sample-size statements, statistical interpretations and data provenance as necessary validation, not as an optional check.

## Evidence Sides

**Side A: the figure as stated in report prose**

The reports' narrative text gives a figure for a result. [src: bacdive_phenotype_metal_tolerance, bacillota_b_subsurface_accessory, caulobacter_fur_lipida_loss, cf_formulation_design, enigma_carbon_census_1, ibd_phage_targeting, lab_field_ecology, pitfalls, plant_microbiome_ecotypes, snipe_defense_system, truly_dark_genes] This figure is recorded as stated. No replacement number is computed. [src: bacdive_phenotype_metal_tolerance, bacillota_b_subsurface_accessory, caulobacter_fur_lipida_loss, cf_formulation_design, enigma_carbon_census_1, ibd_phage_targeting, lab_field_ecology, pitfalls, plant_microbiome_ecotypes, snipe_defense_system, truly_dark_genes]

**Side B: the figure in the same report's own table**

The same reports' tables give a figure that disagrees with the prose. [src: bacdive_phenotype_metal_tolerance, bacillota_b_subsurface_accessory, caulobacter_fur_lipida_loss, cf_formulation_design, enigma_carbon_census_1, ibd_phage_targeting, lab_field_ecology, pitfalls, plant_microbiome_ecotypes, snipe_defense_system, truly_dark_genes] This figure is also recorded rather than reconciled. [src: bacdive_phenotype_metal_tolerance, bacillota_b_subsurface_accessory, caulobacter_fur_lipida_loss, cf_formulation_design, enigma_carbon_census_1, ibd_phage_targeting, lab_field_ecology, pitfalls, plant_microbiome_ecotypes, snipe_defense_system, truly_dark_genes]

The tension text names the affected sources as a group. It does not say which specific figure in which report conflicts, so this page does not assign any particular discrepancy to any single project.

## Possible Reconciliations

- *Hypothesis:* the prose may have been written against an earlier analysis run and not updated after the tables were regenerated. If so, the table would reflect the final run, but this has not been checked.
- *Hypothesis:* prose and table may use different denominators, filters or thresholds. For example, one might count before a quality filter and the other after it. Under this hypothesis both figures could be correct for differently defined quantities, and the mismatch would be a labelling problem rather than an error.
- *Hypothesis:* some mismatches may be transcription errors in either location. Under this hypothesis neither the prose nor the table can be preferred by default.

None of these hypotheses is established by the evidence, and none justifies preferring one side.

## Resolving Work

- **Notebook outputs, re-executed:** for each listed report, re-run the cited analysis notebook and compare its output cells with both the prose figure and the table figure. Question: which location matches the current computation?
- **Denominator and threshold audit:** for each discrepant pair, extract the filter criteria, sample counts and significance thresholds stated next to the prose figure and next to the table. Question: are the two figures measuring the same quantity?
- **Version history of report files:** use the repository history to date when each prose figure and each table figure was last edited. Question: did the prose lag behind a regenerated table, or the reverse?
- **Automated prose–table consistency check:** parse each report's numbers in narrative sentences and match them to table cells by label. Question: how widespread is the mismatch beyond the reports already listed?
- **Propagation trace in the wiki:** find every concept and entity page that cites one of these reports, and record which of the two figures each page copied. Question: which wiki claims currently rest on a contested number and need both sides shown?
