---
type: "Organism"
description: "ENIGMA groundwater Pseudomonas isolate linked across the KBase Data Lakehouse fitness and metabolite resources"
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Pseudomonas FW300-N2E3

## What this entity is

**Canonical name:** *Pseudomonas* FW300-N2E3. [src: fw300_metabolic_consistency]

**Known aliases:** FW300-N2E3. [src: fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: fw300_metabolic_consistency]

*Pseudomonas* FW300-N2E3 is an isolate analyzed by integrating [[entities/web-of-microbes]] exometabolomics, [[entities/kescience-fitnessbrowser]] mutant-fitness data, [[entities/bacdive]] utilization phenotypes, and [[entities/gapmind]] pathway predictions. [src: fw300_metabolic_consistency]

## Key facts

FW300-N2E3 was isolated from groundwater at the [[entities/oak-ridge-field-research-center]] in an ENIGMA SFA context. [src: fw300_metabolic_consistency]

The organism produced or increased 58 metabolites in Web of Microbes exometabolomics, comprising 27 emerged metabolites and 31 increased metabolites. [src: fw300_metabolic_consistency]

A separate curated Web of Microbes–Fitness Browser matching analysis identified 19 produced metabolites also tested as carbon or nitrogen sources, including lactate as an emerged product and alanine, arginine, glycine, proline, phenylalanine, tryptophan, threonine, trehalose, malate, and other compounds as increased or emerged metabolites; 5 of the 19 were emerged (`E`) and 14 were increased (`I`). This **refines** the broader 58-metabolite production count by defining a high-confidence cross-collection subset rather than replacing it. [src: webofmicrobes_explorer]

FW300-N2E3 matches the Fitness Browser strain `pseudo3_N2E3`, which has 5,854 genes and 211 experiments. This **supports** the existing conclusion that the isolate has substantial fitness-resource coverage for metabolite-to-gene analyses. [src: webofmicrobes_explorer]

Of those 58 metabolites, 21 could be cross-referenced against at least one other database; 17/21 (81%) were fully concordant across all matched databases, 4/21 (19%) were partially concordant, and none were fully discordant. [src: fw300_metabolic_consistency]

Across 41 individual metabolite-database comparisons, 37 were concordant (90.2%), and the mean concordance score was 0.94. [src: fw300_metabolic_consistency]

Fitness Browser comparisons were concordant for 21/21 (100%) metabolites, while [[entities/gapmind]] comparisons were concordant for 13/13 (100%) metabolites. [src: fw300_metabolic_consistency]

The organism showed increased tryptophan in its Web of Microbes exometabolome, 231 significant genes in Fitness Browser growth experiments on tryptophan, and a complete tryptophan biosynthesis pathway prediction from GapMind. [src: fw300_metabolic_consistency]

In contrast, 0 out of 50 *Pseudomonas fluorescens* strains in [[entities/bacdive]] could utilize tryptophan as a carbon source, with n=50 and pct_positive=0.0 using per-strain consensus. [src: fw300_metabolic_consistency]

This production-plus-growth-but-no-species-level-catabolism pattern supports the hypothesis that tryptophan overflow metabolism may serve cross-feeding or signaling rather than catabolism; it does not show that FW300-N2E3 itself cannot grow on tryptophan. [src: fw300_metabolic_consistency]

All 13 metabolites mapped to GapMind—lactate, valine, alanine, arginine, aspartate, glutamic acid, glycine, phenylalanine, proline, trehalose, tryptophan, malate, and lysine—had complete pathway predictions for FW300-N2E3, and all 13 also showed growth in Fitness Browser experiments. [src: fw300_metabolic_consistency]

The new Web of Microbes analysis gives de novo lactate production by FW300-N2E3 alongside Fitness Browser lactate-utilization phenotypes as a direct metabolite-to-fitness example. This **supports** the proposed cross-feeding or production–utilization analysis while not establishing that lactate production and utilization occur under the same conditions. [src: webofmicrobes_explorer]

Across 21 Web of Microbes metabolites with matching Fitness Browser experiments, FW300-N2E3 had significant effects for 601 unique genes and 4,764 total significant gene-condition hits, using |fit| > 1 and |t| > 4. [src: fw300_metabolic_consistency]

The most genetically complex metabolisms were carnitine, with 283 significant genes; alanine, with 295 genes across D/L forms; arginine, with 270 genes; and tryptophan, with 231 genes. [src: fw300_metabolic_consistency]

A total of 231 genes were significant in 3 or more metabolite conditions, and the top 18 genes were significant in all 21 conditions. [src: fw300_metabolic_consistency]

The top 18 broadly pleiotropic genes included homoserine O-acetyltransferase, ATP phosphoribosyltransferase, dihydroxy-acid dehydratase, isopropylmalate dehydrogenase, shikimate dehydrogenase, and imidazoleglycerol-phosphate dehydratase. [src: fw300_metabolic_consistency]

Emerged metabolites had a mean of 184.4 +/- 115.5 significant genes, including means of 221.0 detrimental and 21.0 beneficial effects. [src: fw300_metabolic_consistency]

Increased metabolites had a mean of 163.5 +/- 74.1 significant genes, including means of 206.5 detrimental and 12.8 beneficial effects. [src: fw300_metabolic_consistency]

Malate, arginine, and valine were four-way consistency cases: malate was increased, involved 92 Fitness Browser genes, was utilized by 49/49 BacDive strains (100%), and had a complete GapMind pathway; arginine was increased, involved 270 Fitness Browser genes, was utilized by 40/48 BacDive strains (83%), and had a complete GapMind pathway; and valine emerged, involved 160 Fitness Browser genes, was utilized by 1/1 BacDive strain, and had a complete GapMind pathway. [src: fw300_metabolic_consistency]

Trehalose showed 1+/5- utilization in BacDive, lysine showed 0+/3-, and glycine showed 0+/1-; the source characterized these results as moderate confidence for trehalose and lysine and low confidence for glycine. [src: fw300_metabolic_consistency]

## Interpretation and limitations

Web of Microbes measured exometabolomic production on R2A rich medium, whereas Fitness Browser fitness was measured on minimal medium with single carbon or nitrogen sources, so direct comparisons are condition-dependent. [src: fw300_metabolic_consistency]

BacDive aggregates *P. fluorescens* strains and, under GTDB reclassification, spans a broad clade identified as *Pseudomonas_E fluorescens_E*; therefore, species-level utilization rates may not represent FW300-N2E3 specifically. [src: fw300_metabolic_consistency]

Only 21/58 (36%) of the Web of Microbes metabolites could be tested against any other database, and only 3 metabolites had four-way coverage. [src: fw300_metabolic_consistency]

The planned NB04 analysis mapping fitness-important genes to specific GapMind pathway steps was deferred, limiting mechanistic interpretation of the tryptophan overflow hypothesis. [src: fw300_metabolic_consistency]

The 2018 Web of Microbes snapshot contains 37 organisms and 589 metabolites, and its organism records include production or amplification actions but no organism consumption action in this export. This **refines** interpretation of the production–fitness bridge: the dataset can identify produced metabolites tested in Fitness Browser, but cannot test the stronger prediction that consumed metabolites determine gene essentiality. [src: webofmicrobes_explorer]

## Related topics

These results contribute to [[concepts/multi-omics-integration]], [[concepts/condition-specific-fitness]], [[concepts/metabolic-model-gapfilling]], [[concepts/cross-tenant-data-bridging]], [[concepts/gene-essentiality]], and [[concepts/provenance-aware-resource-discovery]]. [src: fw300_metabolic_consistency] [src: webofmicrobes_explorer]

For the complete project reports, see [[summaries/fw300_metabolic_consistency__REPORT]] and [[summaries/webofmicrobes_explorer__REPORT]].
