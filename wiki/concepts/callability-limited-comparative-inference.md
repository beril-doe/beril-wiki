---
type: "Concept"
description: "Ecological contrasts fail when evidence is available for only one side."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Unequal evidence callability can make ecological contrasts untestable

## Core idea

Ecological comparison requires comparable evidence on both sides of the contrast; when pathway, organism, or phenotype calls exist for only one source or group, the comparison can become untestable rather than merely statistically underpowered. [src: enigma_carbon_census_1] “Callability” here means that a compound could be linked to an organism-level utilization prediction or a measured fitness result through the queried resources, not that the compound is biologically absent from the uncalled group. [src: enigma_carbon_census_1]

This distinction connects [[summaries/enigma_carbon_census_1__REPORT]] to [[concepts/occurrence-versus-catabolic-activity]], [[concepts/nonrandom-missingness-in-comparative-genomics]], and [[concepts/ecotype-environment-gene-content]]. [src: enigma_carbon_census_1]

## Evidence asymmetry in the ENIGMA carbon census

The census began with 83 enrichment compounds, of which 83 were structure-resolved, 54 were KEGG-linked, and 9 were callable under the project definition. [src: enigma_carbon_census_1] The remaining 74/83 compounds, or 89%, were organism-dark because their genetic determinants of utilization were not linkable through the queried BERDL and curated resources. [src: enigma_carbon_census_1]

The dark fraction was similar for the two source groups: 53/59 groundwater compounds, or 90%, and 21/24 necromass compounds, or 88%, were organism-dark. [src: enigma_carbon_census_1] This means that the source labels did not supply balanced compound-level evidence for testing whether groundwater and necromass compounds differed in organismal utilization architecture. [src: enigma_carbon_census_1]

The imbalance was sharper for the source-tracking hypothesis H3: only 2 of the 8 ENIGMA-isolate-callable compounds were necromass-sourced, and both were phthalate-class aromatics with Actinomycetota-heavy utilizers. [src: enigma_carbon_census_1] Lauric acid was also necromass-sourced, but its call came only from measured fitness in a reference bacterium, with no ENIGMA-isolate rows and no field data. [src: enigma_carbon_census_1] Consequently, the project reported an SSO field-occurrence atlas rather than a statistical groundwater-versus-necromass source contrast. [src: enigma_carbon_census_1]

This is an evidence-coverage limitation, not evidence that the two sources have equivalent biology. [src: enigma_carbon_census_1] The available callable set was too small and compositionally confounded to separate source effects from compound-class and annotation-coverage effects. [src: enigma_carbon_census_1]

## Callability is not evenly distributed across evidence tiers

The 8 ENIGMA-isolate-callable compounds were concentrated in Shikimates/Phenylpropanoids, with salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid, and terephthalic acid in that class; Phenylethylamine and xanthine were in Alkaloids; and Abscisic acid was in Terpenoids. [src: enigma_carbon_census_1] H1, the hypothesis of a coverage gradient by chemical class, was not formally supported: the chi-square test gave χ²=5.07, p=0.53, df=6, using class counts of Shikimates 5/25, Alkaloids 2/26, Terpenoids 1/17, Fatty acids 0/10, Polyketides 0/2, AA/Peptides 0/2, and mixed 0/1. [src: enigma_carbon_census_1]

The null result does not establish equal callability across classes because the callable sample was small and confounded with annotation coverage. [src: enigma_carbon_census_1] Adding measured-fitness lauric acid did not change the verdict. [src: enigma_carbon_census_1]

The project also found a category error in the callable set: xanthine was initially scored as carbon-catabolic because allowlisted reaction R02107, xanthine→urate, represents purine nitrogen acquisition rather than carbon catabolism. [src: enigma_carbon_census_1] After removing R02107 from the carbon allowlist, the effective carbon-callable set was 8 rather than 9, although committed tables still contained xanthine because they were not regenerated. [src: enigma_carbon_census_1] Thus, even apparently balanced comparisons can be altered by the operational definition of a positive call. [src: enigma_carbon_census_1]

## Why environmental occurrence cannot repair missing catabolic evidence

The environmental atlas covered 86 implicated genera using 3825 taxonomy-bearing NMDC metagenomes and 302 Planet Microbe marine runs. [src: enigma_carbon_census_1] In NMDC, 83/86 genera were detected in 1719 metagenomes, and 99% of samples were labeled through two independent ontology systems. [src: enigma_carbon_census_1]

These observations provide organismal abundance or occurrence, not evidence that the organisms catabolize the census compounds, because no environmental dataset measured those compounds. [src: enigma_carbon_census_1] The atlas therefore cannot substitute for missing utilization calls when the question concerns source-specific degradation capacity. [src: enigma_carbon_census_1]

The same limitation applies to the SSO field atlas: 62 of the implicated utilizer genera were detected at genus resolution, with top field prevalences approximately 0.7–0.9, and 3-hydroxybenzoic-acid utilizers reached 0.90 field prevalence. [src: enigma_carbon_census_1] These values show that candidate genera occur in the field, but they do not demonstrate compound use in those environments. [src: enigma_carbon_census_1] This refines [[concepts/ecotype-environment-gene-content]] by separating environmental presence from evidence for the focal metabolic phenotype. [src: enigma_carbon_census_1]

## Consequences for comparative inference

A source contrast is testable only when both source groups have sufficient, comparable calls for the same type of biological evidence. [src: enigma_carbon_census_1] When one group contributes mostly dark compounds and the other contributes the small callable subset, any observed difference can reflect resource visibility, chemical-class composition, or assay availability rather than ecology. [src: enigma_carbon_census_1]

The ENIGMA census therefore supports the conclusion that H3 was untestable and confounded, rather than supporting or rejecting a groundwater-versus-necromass utilization difference. [src: enigma_carbon_census_1] H4 illustrates the same principle in a different form: it was strongly supported for the 8 ENIGMA-isolate-callable compounds but null for the other 75 compounds lacking isolate-level placement. [src: enigma_carbon_census_1] The null result for the 75 compounds is a missing-evidence result, not a biological finding that those compounds lack phylogenetically structured utilizers. [src: enigma_carbon_census_1]

This concept complements [[concepts/callability-limited-comparative-inference]]’s broader methodological concern with [[concepts/potential-versus-realized-data-integration]] and [[concepts/cross-tenant-data-bridging]]: integrating more resources can expand callability, but it does not make unmeasured activity equivalent to measured utilization. [src: enigma_carbon_census_1]

## Tensions

The census showed a directional concentration of callable compounds in simpler, commonly represented chemical classes, but H1 was not formally supported by the chi-square test. [src: enigma_carbon_census_1] This tension should be retained as an annotation-coverage hypothesis rather than resolved as either a true chemical-class gradient or its absence. [src: enigma_carbon_census_1]

The environmental atlas showed broad occurrence of implicated genera, including strong periphyton representation of Burkholderiales/Comamonadaceae, while the same atlas could not establish compound degradation or activity. [src: enigma_carbon_census_1] This is a measurement-scope tension between ecological occupancy evidence and catabolic-function evidence, not a contradiction in the observations. [src: enigma_carbon_census_1]

## Open Directions

- Re-run the groundwater-versus-necromass comparison after targeted PaperBLAST and PubMed/abstract-level searches promote dark compounds to callable status, then ask whether the source contrast remains after matching compounds by chemical class and evidence tier. [src: enigma_carbon_census_1]
- Apply a study-aware mixed model or sample-level permutation to NMDC and SSO metadata, using the available sample-level environment labels, and ask whether source-associated occurrence differences persist without treating every metagenome as an independent identically sampled observation. [src: enigma_carbon_census_1]
- Regenerate the committed callable tables after excluding R02107 and ask whether xanthine changes any class, source, or co-occurrence conclusion. [src: enigma_carbon_census_1]
- Test the 29 fully orphan compounds and the 6 biosynthesis-known/catabolism-unknown compounds with wet-lab enrichment and genome-resolved sequencing, asking whether the current source imbalance reflects true specialization or resource-level missingness. [src: enigma_carbon_census_1]
- Pair periphyton and soil metagenomes with compound-resolved measurements and metatranscriptomic or metaproteomic assays, asking whether the observed Burkholderiales/Comamonadaceae reservoir is active on the enrichment compounds. [src: enigma_carbon_census_1]
