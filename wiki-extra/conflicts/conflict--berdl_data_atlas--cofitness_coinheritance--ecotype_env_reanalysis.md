<!-- tension-hash: 459994d3d70b48a3 -->
# Broad Data Bridges vs Demonstrated Biological Use

[[concepts/cross-tenant-data-bridging]] exposes a disagreement between the apparent reach of cross-tenant and cross-collection integration and the evidence that those joins represent real, biologically meaningful use. One side treats schema-level compatibility, actionable bridges, and concordant patterns as evidence that integration is productive; the other emphasizes that technical joins can lack validation, directionality, provenance, or independent clinical and experimental support. The distinction matters because a large bridge inventory may otherwise be mistaken for demonstrated interoperability or biological utilization.

## Evidence Sides

### **Integration is technically broad and sometimes actionable**

The atlas contains **536 schema-level bridges**, and the original audit identified five high-leverage bridges; **UC1 was subsequently sample-executed**. [src: berdl_data_atlas] The WoM snapshot found a directly actionable **19-metabolite Fitness Browser bridge**, while **107 formula-only ModelSEED matches** expanded to **900 candidate molecules**. [src: webofmicrobes_explorer] These results support a framework in which a join can be technically valid even when downstream interpretation remains incomplete. The prophage study further found module-level pangenome and NMDC associations were concordant. [src: prophage_ecology] Its reported environmental effect exceeded family-level phylogeny in PERMANOVA, and human-associated environments were enriched for tail (**log2(OR)=2.21**), head morphogenesis (**1.98**), and anti-defense (**1.70**), consistent with the arms-race framework in [[concepts/phage-defense-syndromes-and-arms-race]]. [src: prophage_ecology]

### **Technical connection does not establish use, authority, or mechanism**

The original audit recorded five high-leverage bridges with **zero realized use**, while **UC2–UC5 remained untested**. [src: berdl_data_atlas] The realized-use count is a lower bound because README mining may miss plans and notebooks. [src: berdl_data_atlas] In the NMDC audit, **20 entries resolve to 7 resources**, and `kbase.nmdc_neon` is a NEON namesake collision. [src: nmdc_context_audit] In WoM, missing consumption actions meant production could not be treated as utilization. [src: webofmicrobes_explorer] Tryptophan increased in WoM and had **231 significant Fitness Browser genes** and a complete GapMind pathway, yet **0/50** *P. fluorescens* strains used it as carbon. [src: fw300_metabolic_consistency] Binary growth prediction reached **AUC 0.933**, **0.932**, and **0.927** for tryptophan, phenylalanine, and valine, while continuous phenotypes had negative R². [src: genotype_to_phenotype_enigma]

Mechanistic and evidential support is also uneven: prophage false-positive rate was uncharacterized, only **28%** of genomes had embeddings, and genome size was dominant (**rho=0.717**). [src: prophage_ecology] TerL lineages showed independent enrichment in **0/500** FDR-corrected tests. [src: prophage_ecology] PaperBLAST had organism-level Gini **0.967** and gene-level Gini **0.669**; **9.2%** of 50%-identity families had zero papers, **46.1%** exactly one, and **4.3%** at least 20. [src: paperblast_explorer] The IBD CCA result was **r=0.964**, but cross-cohort LOSO ARI was **0.000** and the cocktail covered only tested strains. [src: ibd_phage_targeting]

## Possible Reconciliations

- **Measurement hypothesis:** “Zero documented use” may differ from zero use because README mining can miss plans and notebooks.
- **Scope hypothesis:** A schema bridge can be valid at the data-model level while its biological direction, chemical identity, or consumption action remains untested.
- **Provenance hypothesis:** Resource resolution and namesake collisions may make apparent tenant or catalog agreement weaker than the join suggests.
- **Evidence hypothesis:** Concordant modules or predictive binary phenotypes may support association without establishing mechanism, utilization, or clinical validity.

## Resolving Work

- Audit all **536** bridges with repositories, notebooks, execution logs, and plans to determine whether “zero documented use” reflects missing documentation or absent execution.
- Trace the **19-metabolite** and **107-to-900** matches to reaction direction, measured consumption, and molecular identity; test whether each bridge supports utilization rather than production-only association.
- Re-resolve the **20 entries** against authoritative resource identifiers and provenance metadata; test whether the **7 resources** and `kbase.nmdc_neon` collision represent distinct authorities.
- Reanalyze prophage calls with geNomad and VIBRANT, estimate false-positive rates, and test whether environmental effects persist after genome size, embedding coverage, and genus-level inference are controlled.
- Validate IBD and fitness findings in held-out cohorts and untested strains, asking whether the observed associations generalize beyond the discovery and tested sets.
