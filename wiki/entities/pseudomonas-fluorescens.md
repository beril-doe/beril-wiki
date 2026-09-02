---
type: "Organism"
description: "Pseudomonas fluorescens utilization phenotypes and carbon-ecology context"
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Pseudomonas fluorescens

## What this entity is

**Canonical name:** *Pseudomonas fluorescens*. [src: fw300_metabolic_consistency]

**Known aliases:** *P. fluorescens*; *Pseudomonas_E fluorescens/protegens* is the broad GTDB-reclassified clade label used for aggregated records and is not a direct synonym for every strain. [src: fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in the document. [src: fw300_metabolic_consistency]

The document uses *P. fluorescens* as the species-level reference for comparing FW300-N2E3 exometabolite production with [[entities/bacdive]] utilization phenotypes. [src: fw300_metabolic_consistency]

The ENIGMA analysis **refines** this species-level framing: all ENIGMA *Pseudomonas* belonged to the environmental *Pseudomonas_E fluorescens/protegens* clade, whereas globally sampled *Pseudomonas* was 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic. [src: genotype_to_phenotype_enigma] The ENIGMA-linked environmental profile therefore should not be treated as representative of the full global genus distribution; the 14 ENIGMA genera occurred in 4,086–288,686 of 464,000 global 16S samples, with *Pseudomonas* occurring in 206K samples. [src: genotype_to_phenotype_enigma]

The carbon-ecology analysis further **refines** the clade-level context: its *Pseudomonas_E* comparison included 189 species, including the *P. fluorescens/putida* group, rather than measuring *P. fluorescens* alone. [src: pseudomonas_carbon_ecology] Across the comparison, 43 of 62 GapMind carbon pathways differed significantly between 7 *Pseudomonas* s.s. species and those 189 *Pseudomonas_E* species after Benjamini-Hochberg false-discovery-rate correction, with the largest *Pseudomonas_E* advantages involving xylose (74.4% versus 0.0%), ribose (92.0% versus 27.9%), arabinose (62.6% versus 0.0%), and myo-inositol (58.8% versus 0.0%). [src: pseudomonas_carbon_ecology] This **supports** pathway-rich environmental specialization in the broader *Pseudomonas_E* clade but does not establish these values for every *P. fluorescens* strain. [src: pseudomonas_carbon_ecology]

## Key facts from fw300_metabolic_consistency

[[entities/pseudomonas-fw300-n2e3]] was analyzed against species-level *P. fluorescens* utilization data from [[entities/bacdive]], but the report cautions that the BacDive aggregation spans a broad clade under GTDB reclassification and may not represent the FW300-N2E3 strain specifically. [src: fw300_metabolic_consistency]

Among WoM-produced metabolites, *P. fluorescens* BacDive utilization was positive for 3 of 7 matched metabolites (43%), compared with an overall *P. fluorescens* baseline of 22 of 80 (27.5%); the binomial comparison gave p = 0.40. [src: fw300_metabolic_consistency]

For tryptophan, 0 of 50 *P. fluorescens* strains utilized the compound as a carbon source, with n = 50 and pct_positive = 0.0 under the report's per-strain consensus procedure. [src: fw300_metabolic_consistency]

For trehalose, 1 of 6 *P. fluorescens* strains was positive; for lysine, 0 of 3 were positive; and for glycine, 0 of 1 was positive. [src: fw300_metabolic_consistency]

The report treats tryptophan as the strongest production-versus-utilization discordance because FW300-N2E3 increased tryptophan in WoM, showed 231 significant Fitness Browser gene effects when grown on tryptophan, and had a complete GapMind tryptophan-biosynthesis prediction, whereas 0 of 50 *P. fluorescens* strains utilized tryptophan. [src: fw300_metabolic_consistency]

The trehalose result is interpreted as potentially strain-variable and more consistent with an osmoprotectant role than a carbon-source role, while the lysine result has a small sample and the glycine result is insufficient for a firm conclusion. [src: fw300_metabolic_consistency]

Three metabolites showed strong BacDive utilization among the matched data: malate was utilized by 49 of 49 *P. fluorescens* strains (100%), arginine by 40 of 48 strains (83%), and valine by 1 of 1 strain. [src: fw300_metabolic_consistency]

BacDive utilization values were calculated after applying majority voting among duplicate records for each strain, and the report emphasizes that compound coverage ranged from 1 to 51 strains. [src: fw300_metabolic_consistency]

The carbon analysis **supports** the distinction between broad clade-level capability and strain physiology: within *Pseudomonas_E*, plant-associated species averaged 56.7 complete pathways, free-living species 56.1, and host-associated species 55.2, while lifestyle categories substantially overlapped. [src: pseudomonas_carbon_ecology] Among 54 free-living and plant-associated species, carbon profiles nevertheless showed a significant but modest environment association (999-permutation p = 0.006); a four-class Random Forest achieved balanced accuracy of 0.408 +/- 0.169 against a 0.250 chance baseline. [src: pseudomonas_carbon_ecology] Thus, these results **refine** the environmental interpretation: carbon profiles contain ecological signal, but are insufficient alone for fine-grained environment prediction. [src: pseudomonas_carbon_ecology]

The ENIGMA analysis **supports** retaining this caution: strain-name collisions caused 12 of 32 genus-level pangenome mismatches, and GTDB-Tk genus checks reduced verified linkages from 32 to 20 while eliminating all false matches. [src: genotype_to_phenotype_enigma] Thus, the report uses *P. fluorescens* utilization data as a species- and clade-level comparison for [[entities/pseudomonas-fw300-n2e3]], not as a direct measurement of FW300-N2E3 physiology. [src: fw300_metabolic_consistency]

The carbon study also notes that its 62 GapMind pathways omit genus-specific aromatic capabilities, including toluene, naphthalene, and benzoate degradation, which may be important to *P. putida* and related environmental ecotypes. [src: pseudomonas_carbon_ecology] It proposes within-species analysis of *P. fluorescens* and *P. putida* ecotypes and experimental comparison with RB-TnSeq fitness data from [[entities/kescience-fitnessbrowser]]. [src: pseudomonas_carbon_ecology]

## Related pages

- [[summaries/fw300_metabolic_consistency__REPORT]] — source summary containing the cross-database analysis. [src: fw300_metabolic_consistency]
- [[summaries/genotype_to_phenotype_enigma__REPORT]] — integrated genotype–condition–phenotype analysis and environmental context. [src: genotype_to_phenotype_enigma]
- [[summaries/pseudomonas_carbon_ecology__REPORT]] — GapMind carbon-pathway analysis across *Pseudomonas* species and environments. [src: pseudomonas_carbon_ecology]
- [[entities/bacdive]] — database supplying the species-level utilization phenotypes. [src: fw300_metabolic_consistency]
- [[entities/pseudomonas-fw300-n2e3]] — FW300-N2E3 isolate analyzed in the report. [src: fw300_metabolic_consistency]
- [[concepts/multi-omics-integration]] — cross-database integration of metabolomics, fitness, phenotype, and pathway evidence. [src: fw300_metabolic_consistency]
- [[concepts/metabolic-model-gapfilling]] — interpretation of GapMind pathway predictions alongside utilization data. [src: fw300_metabolic_consistency]
