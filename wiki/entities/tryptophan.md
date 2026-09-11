---
type: "Compound"
description: "Aromatic amino acid linked to microbial metabolism and ipdC distribution"
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md"]
---
# Tryptophan

## What it is

**Canonical name:** Tryptophan. [src: fw300_metabolic_consistency]

**Known aliases:** No aliases were reported in the source document. [src: fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: fw300_metabolic_consistency]

## Evidence from fw300_metabolic_consistency

[[summaries/fw300_metabolic_consistency__REPORT]] reports that [[entities/pseudomonas-fw300-n2e3]] increased tryptophan in its [[entities/web-of-microbes]] exometabolome. [src: fw300_metabolic_consistency]

The organism had 231 genes with significant fitness effects when grown on tryptophan in [[entities/kescience-fitnessbrowser]], using the report's significance criteria of |fit| > 1 and |t| > 4. [src: fw300_metabolic_consistency]

[[entities/gapmind]] predicted a complete tryptophan biosynthesis pathway in FW300-N2E3, and the organism showed growth on tryptophan in Fitness Browser experiments. [src: fw300_metabolic_consistency]

In contrast, 0 of 50 *Pseudomonas fluorescens* strains in [[entities/bacdive]] could utilize tryptophan as a carbon source; the per-strain consensus result was reported as 0+/50-, with n=50 and pct_positive=0.0. [src: fw300_metabolic_consistency]

The report identifies tryptophan as the strongest and most robust production-versus-utilization discordance among the matched metabolites, while emphasizing that the BacDive result does not show that FW300-N2E3 itself cannot grow on tryptophan. [src: fw300_metabolic_consistency]

The combination of production, organism-level growth, and complete biosynthesis prediction but no species-level carbon utilization supports the hypothesis that tryptophan overflow metabolism may serve cross-feeding or signaling rather than catabolism. [src: fw300_metabolic_consistency]

The Fitness Browser result belongs to a broader fitness landscape: across 21 WoM metabolites with matching Fitness Browser experiments, FW300-N2E3 had significant effects for 601 unique genes and 4,764 total significant gene-condition hits. [src: fw300_metabolic_consistency]

The report cautions that the 231 genes significant in three or more metabolite conditions, including genes involved in aromatic amino acid biosynthesis, may represent broadly required housekeeping functions rather than tryptophan-specific catabolism. [src: fw300_metabolic_consistency]

## Evidence from pgp_pangenome_ecology

The pangenome analysis **refines** the pathway interpretation above: among 11,272 species, [[entities/ipdc]] occurred in 2.5% of species with a complete tryptophan pathway by [[entities/gapmind]] score (≥ 0.9), versus 0.9% with an incomplete pathway (Fisher OR = 2.81, p = 6.3e-10). A logistic model gave OR = 2.81, 95% CI 1.97–4.01, p = 1.4e-08, and adding soil status gave OR = 2.87, p = 7.0e-09. [src: pgp_pangenome_ecology]

This association does not establish a tryptophan-specific mechanism: tyrosine-pathway completeness predicted ipdC at a similar effect size (OR = 3.62, p = 2.3e-11), consistent with regulation by TyrR, which responds to tryptophan, tyrosine, and phenylalanine. [src: pgp_pangenome_ecology]

Within soil/rhizosphere species, the association reversed (OR = 0.30, p = 0.02), whereas it remained positive in non-soil species (OR = 3.56, p = 7.7e-13). This soil result is hypothesis-generating rather than conclusive because ipdC occurred in only 214 of 11,272 species (1.9%); one proposed hypothesis is that soil PGPB obtain aromatic amino acids from plant exudates while retaining ipdC for indole-3-acetic-acid production. [src: pgp_pangenome_ecology]

## Interpretation and limitations

Production was measured by exometabolomics on R2A rich medium, whereas Fitness Browser fitness was measured on minimal medium with tryptophan as a single carbon or nitrogen source, so the comparisons are condition-dependent. [src: fw300_metabolic_consistency]

BacDive aggregates *P. fluorescens* strains across a broad clade identified under GTDB reclassification as *Pseudomonas_E fluorescens_E*, and its species-level consensus may not represent FW300-N2E3 specifically. [src: fw300_metabolic_consistency]

The document reports a separate literature-context sample-size statement of n=52 for tryptophan, while its primary result reports 0+/50- with n=50; this discrepancy is retained rather than reconciled. [src: fw300_metabolic_consistency]

The planned pathway-level analysis mapping fitness-important genes to specific GapMind steps was deferred, leaving the distinction between biosynthetic, catabolic, and regulatory fitness genes unresolved. [src: fw300_metabolic_consistency]

The pangenome result also may reflect general metabolic capacity: genome size, COG coverage, and total pathway count were not controlled, and the phylum-plus-soil model failed because rare ipdC caused quasi-complete separation. [src: pgp_pangenome_ecology]

## Related pages

- [[concepts/multi-omics-integration]] — Tryptophan links exometabolomics, gene-fitness measurements, utilization phenotypes, and pathway predictions. [src: fw300_metabolic_consistency]
- [[concepts/condition-specific-fitness]] — Its 231 significant fitness-effect genes illustrate condition-dependent genetic requirements. [src: fw300_metabolic_consistency]
- [[concepts/metabolic-model-gapfilling]] — Its complete GapMind pathway prediction agrees with the Fitness Browser growth result. [src: fw300_metabolic_consistency]
- [[concepts/ecotype-environment-gene-content]] — Soil context reverses the otherwise positive association between tryptophan-pathway completeness and ipdC. [src: pgp_pangenome_ecology]
- [[concepts/gene-function-acquisition-depth]] — The ipdC association and its rarity inform interpretation of pathway-linked gene distribution. [src: pgp_pangenome_ecology]
- [[concepts/cross-tenant-data-bridging]] — Its interpretation depends on joining metabolite, fitness, phenotype, and pathway data across the KBase Data Lakehouse collections. [src: fw300_metabolic_consistency]
- [[entities/pseudomonas-fw300-n2e3]] — Organism producing tryptophan and showing growth-associated fitness effects on it. [src: fw300_metabolic_consistency]
- [[entities/web-of-microbes]] — Source of the tryptophan exometabolomics observation. [src: fw300_metabolic_consistency]
- [[entities/kescience-fitnessbrowser]] — Source of the tryptophan fitness measurements. [src: fw300_metabolic_consistency]
- [[entities/bacdive]] — Source of the species-level tryptophan utilization data. [src: fw300_metabolic_consistency]
- [[entities/gapmind]] — Source of the complete tryptophan biosynthesis prediction and the pangenome pathway scores. [src: fw300_metabolic_consistency, pgp_pangenome_ecology]
- [[summaries/pgp_pangenome_ecology__REPORT]] — Detailed pangenome evidence connecting aromatic-pathway completeness with ipdC distribution. [src: pgp_pangenome_ecology]
