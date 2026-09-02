<!-- tension-hash: 1934e98a144b783f -->
# Broad cross-collection bridges vs evidential and biological validation

[[concepts/cross-tenant-data-bridging]] records a disagreement over whether technically successful joins and large-scale associations constitute validated biological evidence. One side emphasizes the breadth and actionability of cross-collection bridges; the other emphasizes untested use cases, ambiguous authority, uncertain chemical direction, annotation error, sampling structure, and weak external validation. The distinction matters because a valid computational join may still fail to establish shared provenance, biological utilization, mechanism, or clinical usefulness.

## Evidence Sides

### **Broad integration and association claims**

The atlas exposes **536 schema-level bridges**, and the 19-metabolite Fitness Browser bridge is directly actionable. [src: berdl_data_atlas] [src: webofmicrobes_explorer] The prophage study found module-level pangenome and NMDC associations were concordant, and its environmental effect exceeded family-level phylogeny in the reported PERMANOVA. [src: prophage_ecology] Human-associated environments enriched tail (**log2(OR)=2.21**), head morphogenesis (**1.98**), and anti-defense (**1.70**); **TerL** lineages did not show independent enrichment in **0/500** FDR-corrected tests. [src: prophage_ecology] Binary growth was predicted for tryptophan (**AUC 0.933**), phenylalanine (**0.932**), and valine (**0.927**). [src: genotype_to_phenotype_enigma] The IBD CCA result was **r=0.964**, and PaperBLAST reported organism-level Gini **0.967** and gene-level Gini **0.669**. [src: ibd_phage_targeting] [src: paperblast_explorer]

### **Validation, provenance, and biological meaning remain limited**

Only UC1 was sample-executed, while UC2–UC5 remained untested. [src: berdl_data_atlas] The NMDC audit found **20 entries resolve to 7 resources**, with `kbase.nmdc_neon` a NEON namesake collision. [src: nmdc_context_audit] Missing consumption actions mean production cannot be treated as utilization, while **107** formula-only ModelSEED matches expand to **900** candidate molecules. [src: webofmicrobes_explorer] Tryptophan had **231** significant Fitness Browser genes and a complete GapMind pathway, yet **0/50** *P. fluorescens* strains used it as carbon. [src: fw300_metabolic_consistency]

Prophage annotations came from eggNOG rather than geNomad or VIBRANT; the false-positive rate is uncharacterized. Genome size was dominant (**rho=0.717**), only **28%** of genomes had embeddings, and genus-level NMDC inference assumed conserved prophage content. [src: prophage_ecology] The arms-race pattern therefore does not demonstrate coevolution. [src: prophage_ecology] Field-versus-lab prediction was weak (**AUC 0.548; field-only 0.517; lab-only 0.531**) with no significant module-conservation correlation (**rho=0.071, p=0.62**). [src: field_vs_lab_fitness] HMP2/FRANZOSA clustering had cross-cohort LOSO **ARI=0.000**, and the cocktail covered only tested strains. [src: ibd_phage_targeting]

## Possible Reconciliations

- **Hypothesis—scope:** schema-level bridges may be valid for UC1 or auxiliary comparisons without validating UC2–UC5 or clinical use.
- **Hypothesis—definition:** production, presence, association, and predicted growth may be distinct endpoints; a join can establish correspondence without establishing utilization or mechanism.
- **Hypothesis—measurement:** formula-only matches, namesake collisions, eggNOG annotations, and incomplete embeddings may inflate apparent integration while preserving useful candidate-generation value.
- **Hypothesis—sampling:** the ecotype median partial correlation was **0.081** across **183 species** versus **0.003** originally, a reported **27x** difference caused by different sampling. [src: ecotype_env_reanalysis]

## Resolving Work

- Re-run UC1–UC5 with provenance-aware identifiers; measure which bridges preserve authority, resource identity, and reproducibility.
- Validate the **107** formula-only matches experimentally using standards and consumption assays; test whether **900** candidate molecules resolve to biologically distinct compounds.
- Reannotate prophages with geNomad, VIBRANT, and eggNOG, then estimate false-positive rates and repeat the PERMANOVA with genome-size and embedding-coverage controls.
- Perform blinded cross-cohort and cross-strain validation of phage targeting and genotype-to-phenotype models; ask whether performance exceeds tested-strain and cohort-specific baselines.
- Reanalyze co-fitness, field activity, and PaperBLAST evidence after prevalence, sampling, and publication-coverage matching.
