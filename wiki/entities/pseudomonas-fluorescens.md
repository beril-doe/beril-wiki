---
type: Organism
description: Pseudomonas fluorescens utilization phenotypes and carbon-ecology context
sources:
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
title: Pseudomonas fluorescens
---
# Pseudomonas fluorescens

## What this entity is

**Canonical name:** *Pseudomonas fluorescens*. [^fw300_metabolic_consistency]

**Known aliases:** *P. fluorescens*; *Pseudomonas_E fluorescens/protegens* is the broad GTDB-reclassified clade label used for aggregated records and is not a direct synonym for every strain. [^fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in the document. [^fw300_metabolic_consistency]

The document uses *P. fluorescens* as the species-level reference for comparing FW300-N2E3 exometabolite production with [bacdive](bacdive.md) utilization phenotypes. [^fw300_metabolic_consistency]

The ENIGMA analysis **refines** this species-level framing: all ENIGMA *Pseudomonas* belonged to the environmental *Pseudomonas_E fluorescens/protegens* clade, whereas globally sampled *Pseudomonas* was 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic. [^genotype_to_phenotype_enigma] The ENIGMA-linked environmental profile therefore should not be treated as representative of the full global genus distribution; the 14 ENIGMA genera occurred in 4,086–288,686 of 464,000 global 16S samples, with *Pseudomonas* occurring in 206K samples. [^genotype_to_phenotype_enigma]

The carbon-ecology analysis further **refines** the clade-level context: its *Pseudomonas_E* comparison included 189 species, including the *P. fluorescens/putida* group, rather than measuring *P. fluorescens* alone. [^pseudomonas_carbon_ecology] Across the comparison, 43 of 62 GapMind carbon pathways differed significantly between 7 *Pseudomonas* s.s. species and those 189 *Pseudomonas_E* species after Benjamini-Hochberg false-discovery-rate correction, with the largest *Pseudomonas_E* advantages involving xylose (74.4% versus 0.0%), ribose (92.0% versus 27.9%), arabinose (62.6% versus 0.0%), and myo-inositol (58.8% versus 0.0%). [^pseudomonas_carbon_ecology] This **supports** pathway-rich environmental specialization in the broader *Pseudomonas_E* clade but does not establish these values for every *P. fluorescens* strain. [^pseudomonas_carbon_ecology]

## Key facts from fw300_metabolic_consistency

[pseudomonas-fw300-n2e3](pseudomonas-fw300-n2e3.md) was analyzed against species-level *P. fluorescens* utilization data from [bacdive](bacdive.md), but the report cautions that the BacDive aggregation spans a broad clade under GTDB reclassification and may not represent the FW300-N2E3 strain specifically. [^fw300_metabolic_consistency]

Among WoM-produced metabolites, *P. fluorescens* BacDive utilization was positive for 3 of 7 matched metabolites (43%), compared with an overall *P. fluorescens* baseline of 22 of 80 (27.5%); the binomial comparison gave p = 0.40. [^fw300_metabolic_consistency]

For tryptophan, 0 of 50 *P. fluorescens* strains utilized the compound as a carbon source, with n = 50 and pct_positive = 0.0 under the report's per-strain consensus procedure. [^fw300_metabolic_consistency]

For trehalose, 1 of 6 *P. fluorescens* strains was positive; for lysine, 0 of 3 were positive; and for glycine, 0 of 1 was positive. [^fw300_metabolic_consistency]

The report treats tryptophan as the strongest production-versus-utilization discordance because FW300-N2E3 increased tryptophan in WoM, showed 231 significant Fitness Browser gene effects when grown on tryptophan, and had a complete GapMind tryptophan-biosynthesis prediction, whereas 0 of 50 *P. fluorescens* strains utilized tryptophan. [^fw300_metabolic_consistency]

The trehalose result is interpreted as potentially strain-variable and more consistent with an osmoprotectant role than a carbon-source role, while the lysine result has a small sample and the glycine result is insufficient for a firm conclusion. [^fw300_metabolic_consistency]

Three metabolites showed strong BacDive utilization among the matched data: malate was utilized by 49 of 49 *P. fluorescens* strains (100%), arginine by 40 of 48 strains (83%), and valine by 1 of 1 strain. [^fw300_metabolic_consistency]

BacDive utilization values were calculated after applying majority voting among duplicate records for each strain, and the report emphasizes that compound coverage ranged from 1 to 51 strains. [^fw300_metabolic_consistency]

The carbon analysis **supports** the distinction between broad clade-level capability and strain physiology: within *Pseudomonas_E*, plant-associated species averaged 56.7 complete pathways, free-living species 56.1, and host-associated species 55.2, while lifestyle categories substantially overlapped. [^pseudomonas_carbon_ecology] Among 54 free-living and plant-associated species, carbon profiles nevertheless showed a significant but modest environment association (999-permutation p = 0.006); a four-class Random Forest achieved balanced accuracy of 0.408 +/- 0.169 against a 0.250 chance baseline. [^pseudomonas_carbon_ecology] Thus, these results **refine** the environmental interpretation: carbon profiles contain ecological signal, but are insufficient alone for fine-grained environment prediction. [^pseudomonas_carbon_ecology]

The ENIGMA analysis **supports** retaining this caution: strain-name collisions caused 12 of 32 genus-level pangenome mismatches, and GTDB-Tk genus checks reduced verified linkages from 32 to 20 while eliminating all false matches. [^genotype_to_phenotype_enigma] Thus, the report uses *P. fluorescens* utilization data as a species- and clade-level comparison for [pseudomonas-fw300-n2e3](pseudomonas-fw300-n2e3.md), not as a direct measurement of FW300-N2E3 physiology. [^fw300_metabolic_consistency]

The carbon study also notes that its 62 GapMind pathways omit genus-specific aromatic capabilities, including toluene, naphthalene, and benzoate degradation, which may be important to *P. putida* and related environmental ecotypes. [^pseudomonas_carbon_ecology] It proposes within-species analysis of *P. fluorescens* and *P. putida* ecotypes and experimental comparison with RB-TnSeq fitness data from [kescience-fitnessbrowser](kescience-fitnessbrowser.md). [^pseudomonas_carbon_ecology]

## Related pages

- [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) — source summary containing the cross-database analysis. [^fw300_metabolic_consistency]
- [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md) — integrated genotype–condition–phenotype analysis and environmental context. [^genotype_to_phenotype_enigma]
- [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md) — GapMind carbon-pathway analysis across *Pseudomonas* species and environments. [^pseudomonas_carbon_ecology]
- [bacdive](bacdive.md) — database supplying the species-level utilization phenotypes. [^fw300_metabolic_consistency]
- [pseudomonas-fw300-n2e3](pseudomonas-fw300-n2e3.md) — FW300-N2E3 isolate analyzed in the report. [^fw300_metabolic_consistency]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — cross-database integration of metabolomics, fitness, phenotype, and pathway evidence. [^fw300_metabolic_consistency]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — interpretation of GapMind pathway predictions alongside utilization data. [^fw300_metabolic_consistency]

[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
