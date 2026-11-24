---
type: "Concept"
description: "Whether any substrate favours commensals over a pathogen, from assay selectivity and genomic pathway comparison; stops at validation experiments yet to be run."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/discoveries.md"]
---
# Selective prebiotics for commensal consortia

Direct growth assays found no clearly selective substrate for commensals over *Pseudomonas aeruginosa* PA14 among those tested. [src: cf_formulation_design] A genomic pathway comparison then pointed to sugar alcohols and pentoses as alternatives. [src: cf_formulation_design] These candidates come from pathway predictions, and the report says the prediction must be validated experimentally. [src: cf_formulation_design] The evidence comes from one report, [[summaries/cf_formulation_design__REPORT]], and from its restatement in [[summaries/discoveries]]. [src: discoveries]

## Assay selectivity: no selective prebiotic among tested substrates

The assays found no substrate that gave commensals a clear advantage. The report computed selectivity as commensal mean optical density (OD) divided by PA14 OD for all 20 tested substrates. [src: cf_formulation_design] PA14 outgrew the average commensal on every tested substrate. [src: cf_formulation_design] The most selective substrates (cysteine, threonine and methionine) had ratios of only 0.77–0.96. [src: cf_formulation_design] No amino acid or simple sugar gave commensals a clear advantage. [src: cf_formulation_design] The report concluded that among the 22 tested substrates no selective prebiotic exists. [src: cf_formulation_design] It attributed the lack of selective amino acid prebiotics to PA14 being too metabolically versatile on amino acids. [src: cf_formulation_design] This null result motivated a genomic search for untested substrates. [src: cf_formulation_design]

## Genomic pathway comparison

The genomic comparison suggests a different strategy. [[entities/gapmind]] predicts completeness for ~80 carbon and amino acid pathways, many outside the 22 tested substrates. [src: cf_formulation_design] The report compared completeness between its 5 core commensals and *P. aeruginosa* across the pangenome. [src: cf_formulation_design] It identified xylitol, myoinositol, arabinose and xylose as candidate prebiotics that commensals can metabolize but PA14 cannot. [src: cf_formulation_design] It found six pathways complete in at least one commensal but absent in PA14. [src: cf_formulation_design, discoveries] These were xylitol, myoinositol, xylose, arabinose, fucose and rhamnose. [src: discoveries] Each pathway is carried by only 1–2 of the 5 core species, so these are species-specific capabilities and not consortium-wide ones. [src: cf_formulation_design]

| Substrate | PA completeness | Commensal carriage | Selectivity |
|---|---|---|---|
| Myoinositol | 0% | *R. dentocariosa* (100%) | 1.00 [src: cf_formulation_design] |
| Xylitol | 0% | *S. salivarius* (98%), *G. sanguinis* (100%) | 1.00 [src: cf_formulation_design] |
| Xylose | 0% | *N. mucosa* (100%), *G. sanguinis* (100%) | 1.00 [src: cf_formulation_design] |
| Arabinose | 0% | *N. mucosa* (100%), *G. sanguinis* (100%) | 1.00 [src: cf_formulation_design] |
| Fucose | 1% | *N. mucosa* (100%), *G. sanguinis* (100%) | 0.99 [src: cf_formulation_design] |
| Rhamnose | 1% | *N. mucosa* (100%), *G. sanguinis* (100%) | 0.99 [src: cf_formulation_design] |

The report calls this a qualitatively different strategy from amino acid supplementation. Sugar alcohols feed commensals on substrates PA14 cannot access, instead of competing on PA14's substrates. [src: cf_formulation_design]

## Supporting expression and practical context

Patient metatranscriptomics is said to corroborate the genomic predictions. It showed 47 KEGG pathways with a >2× commensal-to-PA expression ratio in vivo. These were dominated by PTS sugar transport systems for maltose, trehalose and N-acetylmuramic acid, which only commensals expressed. [src: cf_formulation_design, discoveries] These pathways are not the six candidate substrates. The report names the six as strong prebiotic candidates. [src: cf_formulation_design] It states that they are genomically complete in formulation species, absent from PA14's repertoire and actively transported by commensals in patient airways. [src: cf_formulation_design] It also describes them as commercially available and FDA-GRAS. [src: cf_formulation_design, discoveries]

[[entities/xylitol]] is already used in CF airway products for other indications. [src: cf_formulation_design, discoveries] The report describes it as FDA-approved for CF airway use, with mucolytic/antimicrobial properties, which makes it a dual-purpose opportunity. [src: cf_formulation_design] It cites Durairaj et al. (2007) for the safety of inhaled xylitol in CF patients. [src: cf_formulation_design] It cites Singh et al. (2020) for a randomized controlled trial of aerosolized hypertonic xylitol versus saline during CF exacerbations. [src: cf_formulation_design] The report says these studies establish the delivery route and safety profile its strategy would use. [src: cf_formulation_design]

The report also proposes pairings. It hypothesizes that prebiotics could give the consortium a biomass advantage before competition begins. [src: cf_formulation_design] Xylitol would benefit [[entities/streptococcus-salivarius]], the top inhibitor. Xylose, arabinose and fucose would benefit *N. mucosa*, the engraftment anchor, and *G. sanguinis*. [src: cf_formulation_design] The report hypothesizes that a multi-prebiotic cocktail aimed at different members may work better than a single prebiotic. [src: cf_formulation_design]

## Proposed validation

The report proposes growing the 5 core formulation species and PA14 on the six substrates as sole carbon sources, using endpoint OD and growth curves. [src: cf_formulation_design] It expects commensals to grow and PA14 not to, with selectivity ratios >10 against <1 for all tested amino acids. [src: cf_formulation_design] It also proposes chronic PA14 lung infection mouse tests of k=2 (*R. dentocariosa* + *N. mucosa*), k=3 (*M. luteus* + *N. mucosa* + *S. salivarius*) and k=5 formulations, with and without xylitol + xylose. [src: cf_formulation_design] The prebiotic arm would test xylitol for *S. salivarius* and xylose for *N. mucosa*. [src: cf_formulation_design]

## Caveats

The genomic prediction of 100% commensal pathway completeness versus 0% PA is strong, but the report says it must be validated experimentally. [src: cf_formulation_design] Carriage is species-specific, not consortium-wide. [src: cf_formulation_design]

## Open Directions

- Run the sole-carbon-source growth assays on the six substrates, and compare the resulting selectivity ratios with the expected >10. This closes the gap between prediction and measurement.
- Run the mouse infection arms with and without xylitol + xylose. This tests whether prebiotics help in vivo.
- Test single prebiotics against cocktails matched to the species that carry each pathway. This addresses the species-specific carriage.
- Relate the results to [[concepts/multi-criterion-design-of-protective-microbiome-formulations]] and [[concepts/engraftability-and-lung-adaptation-of-candidate-commensals]].
