---
type: "Dataset"
description: "A genome-based metal tolerance score derived from cross-species RB-TnSeq fitness data and projected onto 27,702 pangenome species through KEGG annotations."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
aliases: ["Metal Atlas", "metal fitness atlas", "metal tolerance score", "n_metal_clusters"]
---
# Metal Fitness Atlas

The Metal Fitness Atlas (also called the Metal Atlas, or the metal tolerance score, with the gene-count feature n_metal_clusters) is a genome-based metal tolerance score. It is derived from cross-species random barcode transposon sequencing (RB-TnSeq) fitness data and projected onto 27,702 pangenome species through KEGG functional annotations. [src: bacdive_metal_validation, metal_fitness_atlas] The score is a genome-based prediction, not a direct tolerance measurement. [src: bacdive_phenotype_metal_tolerance] A later report found that its core-genome enrichment holds after removing pleiotropic genes. [src: metal_specificity]

## Key facts

- The atlas is described as the first cross-species genome-wide fitness atlas for metal tolerance. It holds 383,349 gene × metal fitness records across 24 organisms and 14 metals. [src: metal_fitness_atlas]
- It has metal data for 31 organisms, of which 24 have fitness matrices. [src: metal_fitness_atlas]
- Of all gene × metal records, 3.3% (12,838 / 383,349) show significant fitness defects, defined as fit < -1 and |t| > 4. [src: metal_fitness_atlas]
- A signature of 1,286 KEGG ortholog (KO) terms, derived from conserved metal gene families, was used to score all 27,702 pangenome species. [src: metal_fitness_atlas]
- The atlas scores 27,702 species but cannot validate predictions for organisms without RB-TnSeq libraries. [src: metal_fitness_atlas]
- Pangenome-scale prediction across 27,702 species uses genome-size-normalized scoring. It suggests that metal tolerance genes are broadly distributed, not concentrated in specialists. [src: metal_fitness_atlas]
- The normalized score (metal_score_norm) controls for genome size, which matters because Pseudomonadota tend to have larger genomes. [src: bacdive_metal_validation] Without normalization, the environmental signal could partly reflect genome size rather than metal gene content. [src: bacdive_metal_validation] Without normalization, species with large open pangenomes such as K. pneumoniae and P. aeruginosa dominate the scores, reflecting genome size rather than metal biology. [src: metal_fitness_atlas]
- The atlas found metal genes to be 87.4% core (odds ratio, OR=2.08). [src: counter_ion_effects, metal_cross_resistance]

### Atlas data tables

| Table | Rows | Content |
|---|---|---|
| metal_experiments.csv | 559 | All metal experiments classified by metal, organism, concentration [src: metal_fitness_atlas] |
| metal_fitness_scores.csv | 383,349 | Per-gene per-metal fitness summaries [src: metal_fitness_atlas] |
| metal_important_genes.csv | 12,838 | Genes with significant metal fitness defects [src: metal_fitness_atlas] |
| metal_conservation_stats.csv | 14 | Core fraction statistics per metal [src: metal_fitness_atlas] |
| conserved_metal_families.csv | 1,182 | Ortholog families with conserved metal phenotypes [src: metal_fitness_atlas] |
| novel_metal_candidates.csv | 149 | Novel families with conserved metal phenotypes, classified by novelty type [src: metal_fitness_atlas] |
| metal_modules.csv | 19,453 | Module × metal-experiment z-scored activity records [src: metal_fitness_atlas] |
| metal_functional_signature.csv | 1,287 | KEGG/PFAM terms in the metal gene signature [src: metal_fitness_atlas] |
| species_metal_scores.csv | 27,702 | Metal tolerance scores for all pangenome species [src: metal_fitness_atlas] |

## Validation against isolation ecology and phenotypes

Two reports interpret isolation-environment results as validating the prediction method. One says heavy metal contamination isolates score d=+1.0 above the environmental baseline. [src: bacdive_metal_validation] Another says the genome-based method is validated against real-world isolation ecology. [src: discoveries] See [[concepts/isolation-environment-validation-of-genome-predicted-metal-tolerance]].

In a BacDive phenotype analysis, n_metal_clusters is the number of metal resistance gene clusters. Adding it lifts the full model to R² = 0.63, and the report concludes that the genome-encoded repertoire is the true predictor. [src: bacdive_phenotype_metal_tolerance] Gene count explains more variance than all phenotype features combined and substantially more than taxonomy alone. [src: bacdive_phenotype_metal_tolerance] It contributes most of the improvement over taxonomy (delta R² = +0.28). [src: bacdive_phenotype_metal_tolerance] The analysis covered 5,647 species and 10 phenotype features. [src: bacdive_phenotype_metal_tolerance] It drew on [[entities/kbase-ke-pangenome]] scores for 27,702 species. [src: bacdive_phenotype_metal_tolerance]

The caveat is that the scores are predictions. The phenotype associations are therefore phenotype-to-genome, not phenotype-to-phenotype, although partial correlations control for n_metal_clusters. [src: bacdive_phenotype_metal_tolerance] A separate project's BacDive validation at Fitness Browser organism scale (n = 26) lacks the power of the atlas at pangenome scale (42K strains). [src: metal_cross_resistance]

## Robustness to shared-stress confounding

Shared osmotic-stress machinery could in principle inflate the atlas's core enrichment, because those genes are core. [src: counter_ion_effects] A correction removing about 40% shared-stress genes did not remove the enrichment. [src: counter_ion_effects] The report concludes that the result is not an artifact of shared stress overlap. [src: counter_ion_effects, discoveries] See [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]].

A second report reaches the same conclusion by removing all pleiotropic genes. It argues the 87.4% core finding was not inflated by general stress genes, because the remaining metal-specific set is 88% core. [src: metal_specificity]

- Core enrichment increased for 7 of 14 metals: Mo, W, Hg, Se, Ni, Cr and U. [src: counter_ion_effects] Shared-stress genes are about 90% core, and removing them leaves metal-specific genes that are still highly core. [src: counter_ion_effects]
- Delta values rose for molybdenum (+0.132 to +0.145) [src: counter_ion_effects], tungsten (+0.129 to +0.134) [src: counter_ion_effects], mercury (+0.116 to +0.133) [src: counter_ion_effects] and selenium (+0.115 to +0.131). [src: counter_ion_effects]
- Aluminum fell modestly from +0.099 to +0.068. [src: counter_ion_effects] Zinc fell from +0.145 to +0.115. [src: counter_ion_effects]
- Cadmium reversed, from -0.008 to -0.108. [src: counter_ion_effects] Its core fraction went from 0.522 to 0.422 against a baseline of 0.530. [src: counter_ion_effects] This had very low power, with 92 original genes from 1 organism. [src: counter_ion_effects]
- Iron moved from -0.040 to +0.182, but with n=9 from 1 organism. [src: counter_ion_effects]
- The report concludes that users need not filter sodium chloride (NaCl)-responsive genes. [src: counter_ion_effects] It also says this strengthens the core genome robustness model, in which metal fitness genes are core because they represent fundamental cellular processes. [src: counter_ion_effects]
- The report suggests its gene classification could refine the atlas finding that condition-specific metal genes are less core. [src: counter_ion_effects]

## Metal specificity of atlas genes

Across 24 organisms, 4,177 (55%) of 7,609 metal-important gene records were sick under metal stress. Their sick rate was under 5% across 5,945 non-metal experiments. [src: discoveries] A further 38% were general sick [src: discoveries] and 7% were metal+stress. [src: discoveries] The report concludes that most atlas genes are genuine metal tolerance determinants. [src: discoveries] See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]].

Metal-specific genes were 84.8% core (pooled), against 90.2% for general sick genes (Cochran-Mantel-Haenszel p=0.011). [src: discoveries] Both categories exceed the 79.8% baseline. [src: discoveries] This partially supports the atlas's two-tier model, in which general stress response is more core than specialized metal resistance, though both are mostly core. [src: discoveries] The metal specificity report states the same: general stress is more core than specific resistance as hypothesized, but the effect is modest, both tiers are strongly core-enriched, and the accessory genome contributes only a small fraction. [src: metal_specificity] The report concludes that the accessory genome contributes only modestly to metal resistance machinery. [src: discoveries]

Among novel candidates, three stand out as metal-specific [src: discoveries]:
- UCP030820/OG01015: oxidoreductase, 67% metal-specific, 7 metals. [src: discoveries]
- YebC/OG01383: transcriptional regulator/translation factor, 58%, 6 metals, 11 organisms. [src: discoveries] See [[entities/yebc]].
- DUF1043-YhcB/OG03264: cell division protein, 50%, 5 metals. [src: discoveries]

YfdZ (15%) and the Mla/Yrb system (0-25%) are pleiotropic. [src: discoveries] DUF39 has 0% metal-specificity and sick rate 0.64 despite spanning 8 metals. [src: discoveries]

## Proposed extension

A cross-resistance report proposes applying the atlas's KEGG/PFAM mapping to cross-resistance gene signatures across 27K species. It would then validate the predictions against BacDive polymetallic isolation environments. [src: metal_cross_resistance] It says a proper H3 test needs this. [src: metal_cross_resistance]
