---
type: Compound
description: Aromatic amino acid linked to microbial metabolism and ipdC distribution
sources:
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: pgp_pangenome_ecology
  resource: ../summaries/pgp_pangenome_ecology__REPORT.md
  title: pgp pangenome ecology
title: Tryptophan
---
# Tryptophan

## What it is

**Canonical name:** Tryptophan. [^fw300_metabolic_consistency]

**Known aliases:** No aliases were reported in the source document. [^fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in the source document. [^fw300_metabolic_consistency]

## Evidence from fw300_metabolic_consistency

[fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) reports that [pseudomonas-fw300-n2e3](pseudomonas-fw300-n2e3.md) increased tryptophan in its [web-of-microbes](web-of-microbes.md) exometabolome. [^fw300_metabolic_consistency]

The organism had 231 genes with significant fitness effects when grown on tryptophan in [kescience-fitnessbrowser](kescience-fitnessbrowser.md), using the report's significance criteria of |fit| > 1 and |t| > 4. [^fw300_metabolic_consistency]

[gapmind](gapmind.md) predicted a complete tryptophan biosynthesis pathway in FW300-N2E3, and the organism showed growth on tryptophan in Fitness Browser experiments. [^fw300_metabolic_consistency]

In contrast, 0 of 50 *Pseudomonas fluorescens* strains in [bacdive](bacdive.md) could utilize tryptophan as a carbon source; the per-strain consensus result was reported as 0+/50-, with n=50 and pct_positive=0.0. [^fw300_metabolic_consistency]

The report identifies tryptophan as the strongest and most robust production-versus-utilization discordance among the matched metabolites, while emphasizing that the BacDive result does not show that FW300-N2E3 itself cannot grow on tryptophan. [^fw300_metabolic_consistency]

The combination of production, organism-level growth, and complete biosynthesis prediction but no species-level carbon utilization supports the hypothesis that tryptophan overflow metabolism may serve cross-feeding or signaling rather than catabolism. [^fw300_metabolic_consistency]

The Fitness Browser result belongs to a broader fitness landscape: across 21 WoM metabolites with matching Fitness Browser experiments, FW300-N2E3 had significant effects for 601 unique genes and 4,764 total significant gene-condition hits. [^fw300_metabolic_consistency]

The report cautions that the 231 genes significant in three or more metabolite conditions, including genes involved in aromatic amino acid biosynthesis, may represent broadly required housekeeping functions rather than tryptophan-specific catabolism. [^fw300_metabolic_consistency]

## Evidence from pgp_pangenome_ecology

The pangenome analysis **refines** the pathway interpretation above: among 11,272 species, [ipdc](ipdc.md) occurred in 2.5% of species with a complete tryptophan pathway by [gapmind](gapmind.md) score (≥ 0.9), versus 0.9% with an incomplete pathway (Fisher OR = 2.81, p = 6.3e-10). A logistic model gave OR = 2.81, 95% CI 1.97–4.01, p = 1.4e-08, and adding soil status gave OR = 2.87, p = 7.0e-09. [^pgp_pangenome_ecology]

This association does not establish a tryptophan-specific mechanism: tyrosine-pathway completeness predicted ipdC at a similar effect size (OR = 3.62, p = 2.3e-11), consistent with regulation by TyrR, which responds to tryptophan, tyrosine, and phenylalanine. [^pgp_pangenome_ecology]

Within soil/rhizosphere species, the association reversed (OR = 0.30, p = 0.02), whereas it remained positive in non-soil species (OR = 3.56, p = 7.7e-13). This soil result is hypothesis-generating rather than conclusive because ipdC occurred in only 214 of 11,272 species (1.9%); one proposed hypothesis is that soil PGPB obtain aromatic amino acids from plant exudates while retaining ipdC for indole-3-acetic-acid production. [^pgp_pangenome_ecology]

## Interpretation and limitations

Production was measured by exometabolomics on R2A rich medium, whereas Fitness Browser fitness was measured on minimal medium with tryptophan as a single carbon or nitrogen source, so the comparisons are condition-dependent. [^fw300_metabolic_consistency]

BacDive aggregates *P. fluorescens* strains across a broad clade identified under GTDB reclassification as *Pseudomonas_E fluorescens_E*, and its species-level consensus may not represent FW300-N2E3 specifically. [^fw300_metabolic_consistency]

The document reports a separate literature-context sample-size statement of n=52 for tryptophan, while its primary result reports 0+/50- with n=50; this discrepancy is retained rather than reconciled. [^fw300_metabolic_consistency]

The planned pathway-level analysis mapping fitness-important genes to specific GapMind steps was deferred, leaving the distinction between biosynthetic, catabolic, and regulatory fitness genes unresolved. [^fw300_metabolic_consistency]

The pangenome result also may reflect general metabolic capacity: genome size, COG coverage, and total pathway count were not controlled, and the phylum-plus-soil model failed because rare ipdC caused quasi-complete separation. [^pgp_pangenome_ecology]

## Related pages

- [multi-omics-integration](../concepts/multi-omics-integration.md) — Tryptophan links exometabolomics, gene-fitness measurements, utilization phenotypes, and pathway predictions. [^fw300_metabolic_consistency]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — Its 231 significant fitness-effect genes illustrate condition-dependent genetic requirements. [^fw300_metabolic_consistency]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — Its complete GapMind pathway prediction agrees with the Fitness Browser growth result. [^fw300_metabolic_consistency]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — Soil context reverses the otherwise positive association between tryptophan-pathway completeness and ipdC. [^pgp_pangenome_ecology]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — The ipdC association and its rarity inform interpretation of pathway-linked gene distribution. [^pgp_pangenome_ecology]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — Its interpretation depends on joining metabolite, fitness, phenotype, and pathway data across BERDL collections. [^fw300_metabolic_consistency]
- [pseudomonas-fw300-n2e3](pseudomonas-fw300-n2e3.md) — Organism producing tryptophan and showing growth-associated fitness effects on it. [^fw300_metabolic_consistency]
- [web-of-microbes](web-of-microbes.md) — Source of the tryptophan exometabolomics observation. [^fw300_metabolic_consistency]
- [kescience-fitnessbrowser](kescience-fitnessbrowser.md) — Source of the tryptophan fitness measurements. [^fw300_metabolic_consistency]
- [bacdive](bacdive.md) — Source of the species-level tryptophan utilization data. [^fw300_metabolic_consistency]
- [gapmind](gapmind.md) — Source of the complete tryptophan biosynthesis prediction and the pangenome pathway scores. [^fw300_metabolic_consistency][^pgp_pangenome_ecology]
- [pgp_pangenome_ecology__REPORT](../summaries/pgp_pangenome_ecology__REPORT.md) — Detailed pangenome evidence connecting aromatic-pathway completeness with ipdC distribution. [^pgp_pangenome_ecology]

[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^pgp_pangenome_ecology]: [pgp pangenome ecology](../summaries/pgp_pangenome_ecology__REPORT.md)
