<!-- tension-hash: c50aa829e1d71f9c -->
# Does flux balance analysis track experimental growth and essentiality, or not?

Flux balance analysis (FBA) is a constraint-based method that predicts feasible metabolic flux distributions from a genome-scale model. Two strands of evidence on [[concepts/metabolic-model-gapfilling]] point in different directions on how reliable FBA is. A multi-organism annotation-gap study reports 42.5% baseline FBA accuracy and 330 false positives [src: annotation_gap_discovery]. Evidence centred on *Acinetobacter baylyi* ADP1 reports that FBA often agrees with transposon sequencing (TnSeq), which measures gene essentiality by mapping where insertion mutants survive. That evidence includes a 73.8% concordance [src: acinetobacter_adp1_explorer]. The disagreement matters because the gapfilling concept treats FBA output as something to validate against phenotypes. Whether that validation is encouraging or sobering depends on which strand is taken as representative.

## Evidence Sides

**Side A: baseline FBA accuracy is low and false positives dominate**

The annotation-gap study reports a 42.5% baseline FBA accuracy and 330 false positives [src: annotation_gap_discovery]. Accuracy here is scored on growth or no-growth predictions for organism–carbon-source combinations, not on genes [src: annotation_gap_discovery]. The false positives are cases where the model predicts growth that is not observed, so the result describes overly permissive draft models rather than missed growth [src: annotation_gap_discovery].

**Side B: FBA often agrees with TnSeq in ADP1**

The ADP1-centred evidence indicates that FBA often agrees with TnSeq [src: acinetobacter_adp1_explorer]. The reported figure is a 73.8% concordance, scored over genes that have both FBA flux predictions and TnSeq essentiality calls [src: acinetobacter_adp1_explorer]. Because the organisms, media mappings, and endpoints differ, harmonized simulations are required, and the 73.8% concordance therefore does not erase the broader accuracy result [src: acinetobacter_adp1_explorer].

## Possible Reconciliations

- **Hypothesis: different endpoints.** Side A scores growth or no-growth predictions on carbon sources, while Side B scores gene-level essentiality against TnSeq. Agreement on one endpoint may not transfer to the other.
- **Hypothesis: model construction.** Side A uses draft models built from automated RAST annotations [src: annotation_gap_discovery], while Side B centres on a single organism. If the ADP1 model differs in construction or curation, Side B would be a single-organism result that may not generalize.
- **Hypothesis: media mapping.** The documented mapping concern in the annotation-gap study is that errors in matching conditions to exchange reactions would produce spurious false negatives [src: annotation_gap_discovery]. A separate, untested possibility is that mapping differences also shift false-positive rates between the two settings.
- **Hypothesis: both hold.** FBA could be broadly unreliable for draft growth predictions and still reasonably concordant for essentiality in one organism's model. The tension would then reflect scope, not error.

None of these is established. Each requires the harmonized simulations described below.

## Resolving Work

- **Score ADP1 on the growth endpoint.** Run the ADP1 model on the same growth or no-growth carbon-source endpoint used for the annotation-gap organisms, with matched media mappings. This tests whether ADP1 shows the same false-positive pattern as the draft models.
- **Score draft models on the essentiality endpoint.** Compute FBA-versus-TnSeq essentiality concordance for the annotation-gap organisms. Their knockout validation was inconclusive because growth requires the gapfilled reactions, making single-gene knockouts circular [src: annotation_gap_discovery]; so restrict scoring to genes outside gapfilled reactions, or to conditions where models grow without gapfilling. This tests whether the ADP1 concordance is matched.
- **Standardize media mapping.** Apply one condition-to-exchange-reaction mapping across both projects and re-run both analyses. This tests how much of the discrepancy, in false positives and false negatives, comes from mapping rather than model structure.
- **Stratify by provenance and gapfilling.** Split predictions by annotation provenance and by gapfilled-reaction involvement in both datasets. This asks whether disagreements concentrate in inferred rather than directly supported reactions.
