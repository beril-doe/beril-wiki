---
type: "Dataset"
description: "Metabolic reconstruction, reaction, and compound resource used in BERDL workflows."
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# ModelSEED

## What this entity is

ModelSEED is a metabolic-reconstruction and biochemical-reaction resource used with [[entities/rast]] annotations to build draft metabolic models and perform gapfilling. [src: annotation_gap_discovery]

- **Canonical name:** ModelSEED. [src: annotation_gap_discovery]
- **Known aliases:** ModelSEED metabolic reconstruction resource; ModelSEED biochemical-reaction resource. [src: annotation_gap_discovery]
- **Stable external identifier:** No stable external identifier was reported in the source document. [src: annotation_gap_discovery]

The BERDL Data Atlas inventories 56,012 ModelSEED reactions and 45,708 ModelSEED compounds, refining the resource’s documented role with a measure of its catalog scale. [src: berdl_data_atlas] The atlas also identifies ModelSEED as a reference layer for cross-tenant genome, annotation, pathway, and biochemistry analyses, supporting its use as an integration point rather than only a standalone reconstruction resource. [src: berdl_data_atlas]

The ENIGMA Carbon Census further **supports** this integration role by using ModelSEED alongside PubChem, KEGG, and genome-depot annotations in a compound-to-genome knowledge census. [src: enigma_carbon_census_1] Its annotation-ceiling analysis **refines** the interpretation of ModelSEED coverage: simple, common, pollutant-adjacent compounds were more likely to be represented in ModelSEED and related resources, so apparent biological darkness can partly reflect resource coverage rather than absence of catabolism. [src: enigma_carbon_census_1]

## Role in annotation-gap discovery

The study used ModelSEED/RAST annotations and [[entities/cobrapy]] to construct draft metabolic models for 14 organisms across 574 organism–carbon-source combinations. [src: annotation_gap_discovery]

Baseline flux-balance analysis (FBA), a constraint-based method for predicting metabolic flux and growth, achieved 42.5% overall accuracy, with recall of 86.5% corresponding to 244 of 282 growth-positive conditions correctly predicted and precision of 42.5% corresponding to 244 of 574 growth predictions correct. [src: annotation_gap_discovery]

The baseline models produced 330 false positives, meaning predicted growth on carbon sources that the organisms could not use experimentally. [src: annotation_gap_discovery]

Conditional ModelSEED gapfilling was applied to 38 false-negative cases and added 219 reactions: 201 enzymatic reactions, 14 transport reactions, and 12 exchange reactions, averaging 5.8 added reactions per case. [src: annotation_gap_discovery]

Among the 201 gapfilled enzymatic reaction–organism pairs, 96 pairs, or 47.8%, received candidate genes through integration with [[entities/kescience-fitnessbrowser]] phenotypes, pangenome annotations, [[entities/gapmind]] pathway evidence, and BLAST homology. [src: annotation_gap_discovery]

The resulting assignments included 44 high-confidence pairs, or 21.9%; 19 medium-confidence pairs, or 9.5%; and 33 low-confidence pairs, or 16.4%, while 105 pairs, or 52.2%, remained unresolved. [src: annotation_gap_discovery]

The study generated 574 gapfilling results, 219 gapfilled reaction details, 109 carbon-source-to-ModelSEED-compound mappings, and 201 master reaction–gene candidate records. [src: annotation_gap_discovery]

## Compound-linking and integration limits

The Web of Microbes (WoM) explorer **supports** ModelSEED’s role as a cross-collection compound layer but **refines** expectations about identifier quality. Of 257 identified, non-unknown WoM compounds, 69 (26.8%) had definitive ModelSEED links through exact name matching; 107 (41.6%) had formula-only matches, yielding 176 compounds with any link (68.5%) and leaving 81 unmatched (31.5%). [src: webofmicrobes_explorer] The 107 formula-only compounds expanded to 900 ModelSEED molecules, an average of 8.4 ModelSEED molecules per WoM compound, so exact name matches are high-confidence 1:1 mappings whereas formula-only matches are candidate sets requiring manual curation. [src: webofmicrobes_explorer]

This compound-link ambiguity **refines** the interpretation of the 109 carbon-source-to-ModelSEED-compound mappings produced in the annotation-gap study: a mapping can provide a useful modeling candidate without establishing a unique biochemical identity. [src: annotation_gap_discovery, webofmicrobes_explorer] The WoM assessment also found that GapMind pathway matching was blocked by internal pathway identifiers rather than simple metabolite names, indicating that pathway-to-substrate/product lookup is needed before ModelSEED-linked analyses can be interpreted consistently. [src: webofmicrobes_explorer]

## Limitations and interpretation

ModelSEED gapfilling is non-unique because multiple valid reaction sets may explain a false-negative case, and the study used the default procedure, which minimizes the number of added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]

The draft models contained systematic errors from automated annotations, and their 42.5% baseline FBA accuracy was dominated by false positives, indicating overly permissive model behavior. [src: annotation_gap_discovery]

The study’s knockout validation was inconclusive because the models could not grow on carbon-source minimal media without the gapfilled reactions, making tests of genes assigned to those reactions circular in this setting. [src: annotation_gap_discovery]

The Carbon Census **extends** this limitation from individual draft models to a broader resource-defined gap: 74/83 enrichment compounds were organism-dark, including 33 KEGG-linked compounds with no reaction in queried genomes and 29 fully orphan compounds. [src: enigma_carbon_census_1] These categories identify ModelSEED- and related-resource pathway coverage, rather than confirmed biological non-use, as a target for metabolic-model gapfilling and enrichment experiments. [src: enigma_carbon_census_1]

The atlas’s cross-tenant inventory supports the resource’s broader integration value, but its warning that schema-level join-key presence does not establish valid value-space overlap refines how ModelSEED-linked bridges should be interpreted: proposed joins require live validation rather than relying on table compatibility alone. [src: berdl_data_atlas]

The evidence-triangulation results support [[concepts/metabolic-model-gapfilling]] by showing how ModelSEED gapfilling can supply candidate reactions for integration with phenotype, annotation, pangenome, pathway, and sequence evidence, while also exposing model-quality and solution-nonuniqueness limitations. [src: annotation_gap_discovery]

## Related pages

- [[summaries/annotation_gap_discovery__REPORT]] — source report describing the integrated annotation-gap discovery study. [src: annotation_gap_discovery]
- [[summaries/berdl_data_atlas__REPORT]] — atlas inventory quantifying ModelSEED’s reaction and compound reference layers. [src: berdl_data_atlas]
- [[summaries/enigma_carbon_census_1__REPORT]] — compound-to-genome census that evaluates annotation coverage and organism-dark compounds. [src: enigma_carbon_census_1]
- [[summaries/webofmicrobes_explorer__REPORT]] — WoM compound-link assessment and cross-collection integration analysis. [src: webofmicrobes_explorer]
- [[concepts/metabolic-model-gapfilling]] — cross-document synthesis of metabolic-model gapfilling. [src: annotation_gap_discovery]
- [[concepts/multi-omics-integration]] — synthesis of evidence integration for annotation and functional inference. [src: annotation_gap_discovery]
- [[entities/cobrapy]] — modeling framework used with ModelSEED/RAST annotations. [src: annotation_gap_discovery]
- [[entities/rast]] — annotation source used in draft-model construction. [src: annotation_gap_discovery]
- [[entities/gapmind]] — pathway-completeness resource integrated with gapfilling evidence. [src: annotation_gap_discovery]
