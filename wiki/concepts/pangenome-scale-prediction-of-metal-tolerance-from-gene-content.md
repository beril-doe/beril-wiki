---
type: "Concept"
description: "Whether gene-repertoire signatures from metal fitness data predict metal tolerance across species, including bioleaching taxa and normalization issues."
sources: ["summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md"]
---
# Pangenome-scale prediction of metal tolerance from gene content

This page covers whether gene-repertoire signatures from metal fitness data predict metal tolerance across species, including bioleaching taxa and normalization issues. The evidence is mixed. A 1,286-term KEGG signature was scored across 27,702 species, and normalization recovers known bioleaching genera. [src: metal_fitness_atlas] Simple presence/absence did not validate. [src: metal_fitness_atlas] See [[entities/metal-fitness-atlas]] and [[summaries/metal_fitness_atlas__REPORT]].

## Scoring the pangenome

A metal functional signature of 1,286 KEGG KO (KEGG ortholog) terms was derived from conserved metal gene families and used to score all 27,702 pangenome species. [src: metal_fitness_atlas] The atlas cannot validate predictions for organisms that lack random barcode transposon sequencing (RB-TnSeq) libraries. [src: metal_fitness_atlas]

## Normalization changes the picture

Without normalization, species with large open pangenomes, such as K. pneumoniae and P. aeruginosa, dominate the scores. This reflects genome size rather than metal biology. [src: metal_fitness_atlas] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]]. The atlas report proposes replacing count-based scores with per-species hypergeometric enrichment tests that control for total functional annotation content. [src: metal_fitness_atlas]

With normalization (metal clusters / total KEGG-annotated clusters), the specialist bioleaching organisms emerge. Leptospirillum ranks at the 91st percentile, Acidithiobacillus at the 77th, Marinobacter at the 75th and Sulfobacillus at the 71st. [src: metal_fitness_atlas] The report names Leptospirillum as the highest-scoring bioleaching genus after normalization. [src: metal_fitness_atlas] Acidithiobacillus ferrooxidans is at the 77th percentile and Geobacter sulfurreducens at the 53rd (both normalized). [src: metal_fitness_atlas]

Bioleaching genera as a group are not significantly enriched over background after normalization (Mann-Whitney p=0.17). The report reads this as metal tolerance genes being broadly distributed rather than concentrated in specialists. [src: metal_fitness_atlas]

## Repertoire prediction failed validation

Simple gene presence/absence did not predict metal tolerance, and the report says a regulatory or expression-based model is needed. [src: metal_fitness_atlas] The report says this echoes Rosconi et al. (2022): gene essentiality is context-dependent and cannot be predicted from gene presence alone. [src: metal_fitness_atlas] One untested prediction is that Pseudomonas putida has the 5th-highest metal gene repertoire score among Fitness Browser (FB) organisms (0.707). [src: metal_fitness_atlas] See pseudomonas putida and [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]].

## Cross-resistance report

The cross-resistance report calls its null result expected. It cites the earlier bacdive_metal_validation project, which showed that metal-tolerance prediction needs pangenome-scale analysis (42K strains, Cohen's d = +1.0) for statistical power. [src: metal_cross_resistance] It states that a proper H3 test would apply the KEGG/PFAM mapping approach to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance] It proposes this validation, predicting multi-metal tolerance across 27K species and checking it against BacDive polymetallic isolation environments. [src: metal_cross_resistance]

## Tensions

- Normalized scores place several bioleaching genera at high percentiles [src: metal_fitness_atlas], yet the group is not significantly enriched (p=0.17). [src: metal_fitness_atlas]

## Open Directions

- Run the H3 validation against BacDive polymetallic isolation environments, to close the gap left by the null result. See [[concepts/validating-metal-tolerance-predictions-against-culture-collection-metadata]].
- Replace count-based scores with per-species hypergeometric enrichment tests, to remove the genome-size confound.
- Test the Pseudomonas putida prediction with a full metal panel (Co, Ni, Cu, Zn, Al, Cr, U). See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]].
- Build a regulatory or expression-based model, since presence/absence failed.
