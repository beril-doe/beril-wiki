---
type: "Dataset"
description: "Bakta AMR annotation table in the pangenome data used for Tier 1 resistance gene identification."
sources: ["summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/prophage_amr_comobilization__REPORT.md"]
aliases: ["bakta_annotations"]
---
# bakta_amr

The bakta_amr table is used for Tier 1 AMR gene identification in the KBase Data Lakehouse pangenome data. [src: amr_fitness_cost] It is broad, covering 53.2% of pangenome species, but it is biased toward Pseudomonadota. [src: amr_pangenome_atlas, gene_function_ecological_agora]

## Key facts

- The table holds 83,008 AMRFinderPlus hits on gene cluster representatives. They cover 82,908 distinct clusters across 14,723 species, which is 53.2% of the 27,690 pangenome species. [src: amr_pangenome_atlas]
- The hits span 1,939 distinct AMR gene families and 2,079 AMR products. [src: amr_pangenome_atlas]
- Detection methods are HMM (51.5%), BLASTP (22.7%), EXACTP (13.0%), PARTIALP (9.7%) and ALLELEP (3.0%). [src: amr_pangenome_atlas]
- It sits in the [[entities/kbase-ke-pangenome]] database. [src: amr_fitness_cost] See also [[entities/amrfinderplus]].

## Use in projects

The amr_fitness_cost project used bakta_amr and bakta_annotations for Tier 1 and Tier 2 antimicrobial resistance (AMR) gene identification. [src: amr_fitness_cost] Tier 1 came from bakta_amr, and Tier 2 expanded the set by keyword annotation. [src: amr_fitness_cost] The prophage_amr_comobilization project used bakta_amr, bakta_annotations and bakta_pfam_domains to identify AMR and prophage markers. [src: prophage_amr_comobilization] See [[entities/bakta-pfam-domains]].

### Tier 1 versus Tier 2

Tier 1 genes (N=110) and Tier 2 keyword-annotated genes (N=691) had indistinguishable fitness distributions (KS p = 0.17). The report took this to mean the keyword expansion does not dilute or bias the signal. [src: amr_fitness_cost] Even so, 86% of AMR genes are Tier 2 keyword matches, which may include non-AMR genes such as general efflux transporters. The consistent Tier 1 sensitivity results mitigate this concern. [src: amr_fitness_cost] Related context is in [[concepts/essentiality-and-annotation-caveats-in-transposon-based-resistance-gene-fitness-analysis]].

## Biases and limits

The gene_function_ecological_agora report describes the bakta_amr set as dominated by clade-specific resistance variants. It reads its negative AMR result as consistent with that narrowness, not as a methodology failure. [src: gene_function_ecological_agora] It attributes an AMR detection bias to the Pseudomonadota-heavy AMRFinderPlus reference set. [src: gene_function_ecological_agora] Because of this bias, M17 excludes AMR from the positive-control panel. In NB08c Diagnostic D, 49% of AMR UniRefs were more than 50% Pseudomonadota. [src: gene_function_ecological_agora] The atlas reports AMR only informationally, as info_amr (54.8% recent, 4.1% ancient acquisitions), and does not use it as load-bearing evidence. [src: gene_function_ecological_agora] See [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]].
