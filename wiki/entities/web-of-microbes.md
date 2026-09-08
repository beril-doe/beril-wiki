---
type: Dataset
description: Exometabolomics database linking microbial compounds to organism observations
sources:
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
- id: webofmicrobes_explorer
  resource: ../summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
title: Web of Microbes
---
# Web of Microbes

## Identity

**Canonical name:** Web of Microbes. [^fw300_metabolic_consistency]

**Known alias:** WoM. [^fw300_metabolic_consistency]

**Stable external identifier:** None was reported in the source documents. [^fw300_metabolic_consistency]

Web of Microbes is an exometabolomics database used in the FW300-N2E3 metabolic-consistency analysis, alongside [kescience-fitnessbrowser](kescience-fitnessbrowser.md), [bacdive](bacdive.md), and [gapmind](gapmind.md). [^fw300_metabolic_consistency] It was also used in the ENIGMA genotype-to-phenotype study to associate metabolites with growth-predictive genes and Fitness Browser-cognate KOs. [^genotype_to_phenotype_enigma] A separate exploration characterized a 2018 snapshot and its links to Fitness Browser, ModelSEED, GapMind, and pangenome resources. [^webofmicrobes_explorer]

## Evidence from fw300_metabolic_consistency

Web of Microbes identified 58 metabolites that were produced or increased by *Pseudomonas* FW300-N2E3, comprising 27 emerged metabolites and 31 increased metabolites. [^fw300_metabolic_consistency]

Of the 58 metabolites, 21 could be cross-referenced against at least one other database; 17/21 (81%) were fully concordant across all matched databases, 4/21 (19%) were partially concordant, and none were fully discordant. [^fw300_metabolic_consistency] The mean concordance score for the 21 testable metabolites was 0.94. [^fw300_metabolic_consistency] Across 41 individual metabolite-database comparisons, 37 were concordant (90.2%). [^fw300_metabolic_consistency]

The remaining 37 metabolites, representing 64% of the Web of Microbes observations, were observed only in Web of Microbes and were not tested in BacDive, predicted by GapMind, or used as Fitness Browser conditions for FW300-N2E3. [^fw300_metabolic_consistency] Web of Microbes was manually matched to 28/58 metabolites (48%) in Fitness Browser carbon or nitrogen-source conditions, 8/58 (14%) in BacDive *P. fluorescens* utilization data, and 13/58 (22%) in GapMind pathway predictions. [^fw300_metabolic_consistency]

The Web of Microbes measurements were exometabolomic observations from FW300-N2E3 grown on R2A rich medium. [^fw300_metabolic_consistency] The report emphasizes that Web of Microbes metabolite production is not equivalent to growth-based utilization, because exometabolomics can measure overflow metabolism, biosynthetic byproduct release, or active ecological secretion. [^fw300_metabolic_consistency]

The pitfalls audit **refines** interpretation of Web of Microbes organism observations: codes `I` and `E` mean increased and emerged, respectively, while `N` means no change and `D` occasionally means decreased; the binary “produced” definition is `action IN ('I', 'E')`. [^pitfalls] In the “The Environment” control, however, `D` means detected and `N` means not detected, so actor context is required. [^pitfalls] The 2018 snapshot **refines** this account by showing 1,338 `I`, 1,155 `E`, and 7,509 `N` organism observations, with `E` and `I` mutually exclusive, while no organism-level decreased or consumption action was present; its control contained 742 `D` and 1,023 `N` observations. [^webofmicrobes_explorer] The same snapshot contained 589 metabolites, including 332 (56.4%) unidentified compounds with an `Unk_` prefix. [^webofmicrobes_explorer]

The ENIGMA analysis **supports and refines** this production-versus-utilization distinction: with n = 6 strains, multivariate gradient-boosted decision-tree modeling failed to predict growth from Web of Microbes data (AUC = 0.500), whereas univariate per-metabolite point-biserial correlations identified 940 strong associations with |r| > 0.7 across all 62 variable metabolites—454 production relationships and 486 consumption relationships. [^genotype_to_phenotype_enigma]

Those associations used a focused set of 156 Fitness Browser-cognate KOs and included K01048 with taurine production, K05710 with thymine production, K02613 with lactate consumption, and K07334 with hypoxanthine consumption. [^genotype_to_phenotype_enigma] Growth-predictive KOs and metabolite-production-associated KOs had Spearman rho = 0.043, which **supports** the interpretation that these datasets address different biological questions rather than providing interchangeable evidence. [^genotype_to_phenotype_enigma]

## Key cross-database observations

Tryptophan was increased in the Web of Microbes exometabolome, while Fitness Browser recorded 231 genes with significant fitness effects on tryptophan and GapMind predicted a complete tryptophan-biosynthesis pathway. [^fw300_metabolic_consistency] The same analysis found that 0 of 50 *P. fluorescens* strains in BacDive utilized tryptophan as a carbon source, making tryptophan the strongest production-versus-utilization discordance associated with the Web of Microbes data. [^fw300_metabolic_consistency]

Malate was increased in Web of Microbes, involved 92 Fitness Browser genes, was utilized by 49/49 BacDive strains (100%), and had a complete GapMind pathway prediction. [^fw300_metabolic_consistency]

Arginine was increased in Web of Microbes, involved 270 Fitness Browser genes, was utilized by 40/48 BacDive strains (83%), and had a complete GapMind pathway prediction. [^fw300_metabolic_consistency]

Valine emerged in Web of Microbes, involved 160 Fitness Browser genes, was utilized by 1/1 BacDive strain, and had a complete GapMind pathway prediction. [^fw300_metabolic_consistency]

The newer exploration **supports** the feasibility of metabolite-to-fitness analyses: for `pseudo3_N2E3`, 19 WoM-produced metabolites matched Fitness Browser carbon or nitrogen-source experiments, including lactate, malate, arginine, tryptophan, valine, lysine, threonine, trehalose, and other amino acids and nucleotides; 5 were `E` products and 14 were `I` metabolites. [^webofmicrobes_explorer] It also identified direct Fitness Browser matches for *Pseudomonas* FW300-N2E3 and GW456-L13, with 5,854 genes and 211 experiments and 5,243 genes and 106 experiments, respectively. [^webofmicrobes_explorer]

## Cross-database integration and limitations

Only 21/58 Web of Microbes metabolites (36%) could be tested against another database, and only 3 metabolites had four-way coverage across Web of Microbes, Fitness Browser, BacDive, and GapMind. [^fw300_metabolic_consistency] The Web of Microbes R2A rich-medium measurements and Fitness Browser minimal-medium single-substrate experiments differ in growth conditions, limiting direct comparison of production and fitness results. [^fw300_metabolic_consistency]

Manual name matching may have missed additional Web of Microbes correspondences because of nomenclature differences, although excluding two approximate Fitness Browser matches changed the mean concordance score only from 0.937 to 0.930. [^fw300_metabolic_consistency] The 2018 exploration **refines** the integration assessment: of 257 identified, non-unknown compounds, 69 (26.8%) had definitive ModelSEED links by exact name matching, while 107 (41.6%) had formula-only links; the latter expanded to 900 ModelSEED molecules, leaving 81 unmatched (31.5%), so formula matches are candidate sets rather than definitive identifications. [^webofmicrobes_explorer]

The ENIGMA Web of Microbes analysis was limited to n = 6 strains for the multivariate model and 62 variable metabolites; its reported correlations therefore do not establish causal metabolite effects. [^genotype_to_phenotype_enigma] The 2018 snapshot was additionally small—37 organisms (20 experimental organisms)—and came from a single laboratory. [^webofmicrobes_explorer]

The pitfalls findings **support** cautious use of Web of Microbes action codes and **refine** cross-database interpretation: the four-valued BacDive utilization vocabulary (`+`, `-`, `produced`, and `+/-`) is not binary, and for *Pseudomonas fluorescens*, indole had 60 “produced” entries but only 1 actual utilization test. [^pitfalls] Consequently, only explicit `+` and `-` observations should enter utilization percentages. [^pitfalls]

The 2018 export **contrasts with** the expected richer current resource because it contains no organism consumption action; this prevents the stronger test of whether consumed metabolites predict gene essentiality. [^webofmicrobes_explorer] GapMind matching was blocked by internal pathway identifiers rather than simple metabolite names, and species-level pangenome matching requires strain-to-genome mapping, although genus-level pangenome representation was available for all WoM organism genera. [^webofmicrobes_explorer]

The Web of Microbes results feed the cross-database synthesis in [multi-omics-integration](../concepts/multi-omics-integration.md) and the evidence-joining analysis in [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md). [^fw300_metabolic_consistency]

## Source

- [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) — metabolic consistency analysis integrating Web of Microbes, Fitness Browser, BacDive, and GapMind. [^fw300_metabolic_consistency]
- [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md) — genotype-to-phenotype modeling linking exometabolomics associations with growth and gene features. [^genotype_to_phenotype_enigma]
- [pitfalls](../summaries/pitfalls.md) — database interpretation, action-code semantics, and utilization-coding safeguards. [^pitfalls]
- [webofmicrobes_explorer__REPORT](../summaries/webofmicrobes_explorer__REPORT.md) — 2018 Web of Microbes snapshot, action semantics, compound-link quality, and cross-collection integration. [^webofmicrobes_explorer]

[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../summaries/webofmicrobes_explorer__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
