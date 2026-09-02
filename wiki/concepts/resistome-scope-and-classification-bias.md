---
type: "Concept"
description: "How AMR catalog scope and mechanism labels bias resistome conclusions"
sources: ["summaries/amr_pangenome_atlas__REPORT.md"]
---
# Resistome conclusions depend on gene-catalog scope and mechanism classification

Resistome conclusions are conditional on which genes a catalog includes and how those genes are assigned to resistance mechanisms. The [[summaries/amr_pangenome_atlas__REPORT]] analyzed 83,008 [[entities/amrfinderplus]] hits on gene-cluster representatives from 27,690 pangenome species, covering 1,939 AMR gene families and 2,079 AMR products. [src: amr_pangenome_atlas]

## Catalog scope changes what counts as resistance

The AMRFinderPlus Reference Gene Catalog used in the analysis includes stress-response genes alongside classical antibiotic-resistance genes, so the 83,008 hits are not all antibiotic resistance in the narrow sense. [src: amr_pangenome_atlas] The five most abundant families included bla beta-lactamases with 6,115 hits, merA mercury reductase with 4,506, arsD arsenic metallochaperone with 2,611, merP mercury-binding protein with 2,222, and vanR vancomycin response regulator with 1,929. [src: amr_pangenome_atlas] Mercury-resistance families collectively contributed approximately 15,000 hits and 18% of all AMR annotations, while arsenic-resistance families contributed another approximately 6,000 hits. [src: amr_pangenome_atlas]

This scope makes the observed resistome partly a broader stress-resistance landscape, linking [[concepts/environmental-resistome]] to the catalog's inclusion criteria rather than measuring only clinically defined antibiotic resistance. [src: amr_pangenome_atlas] The report therefore supports interpreting AMR abundance and environmental distributions as catalog-dependent measurements, not as direct counts of antibiotic resistance alone. [src: amr_pangenome_atlas]

## Mechanism labels add a second source of bias

Mechanism classification was performed by keyword matching against AMRFinderPlus product descriptions rather than by mapping to the CARD Antibiotic Resistance Ontology. [src: amr_pangenome_atlas] The resulting table contained 18,448 Other/Unclassified hits, or 22.2% of all hits, compared with 15,755 enzymatic-inactivation hits, or 19.0%; 14,338 efflux hits, or 17.3%; 12,824 beta-lactamase hits, or 15.4%; 6,955 target-modification hits, or 8.4%; 6,852 oxidoreductase hits, or 8.3%; 4,964 cell-wall-modification hits, or 6.0%; and 2,848 regulatory hits, or 3.4%. [src: amr_pangenome_atlas]

The 22.2% Other/Unclassified category means that mechanism-specific comparisons are incomplete and that apparent enrichment or depletion can partly reflect label assignment. [src: amr_pangenome_atlas] This **refines** [[concepts/annotation-dependent-resistome-inference]]: annotation quality affects not only whether a resistance gene is detected, but also which biological mechanism is inferred from it. [src: amr_pangenome_atlas]

## Scope and classification affect conservation claims

The analysis found that 30.3% of AMR genes were core compared with 46.8% for the pangenome baseline, with odds ratio 0.49, chi-squared statistic 23,117, and p approximately 0, while the auxiliary genome was 2.2x enriched for AMR at 33.6% versus 15.3%. [src: amr_pangenome_atlas] In a paired test of 4,252 species with at least 5 AMR clusters, 63.7% had AMR less core than their species baseline, with Wilcoxon p=1.1e-130 and mean difference -0.102. [src: amr_pangenome_atlas]

These conservation results are sensitive to the catalog's mixture of classical antibiotic-resistance genes and heavy-metal or stress-response genes. [src: amr_pangenome_atlas] Within the catalog, beta-lactamases were 54.9% core with p=7.7e-74 for enrichment versus baseline, whereas regulatory genes were 6.5% core; blaTEM, tet(C), and ant(2'')-Ia were 0% core. [src: amr_pangenome_atlas] Intrinsic efflux pumps such as emhABC were greater than 95% core, while acquired efflux genes were accessory. [src: amr_pangenome_atlas]

The report interprets these contrasting patterns as an intrinsic-acquired dichotomy, but the strength of that interpretation depends on whether the catalog and labels reliably distinguish vertically inherited intrinsic resistance from acquired resistance. [src: amr_pangenome_atlas] This **supports** [[concepts/intrinsic-versus-acquired-resistance]] while also identifying catalog scope and mechanism classification as prerequisites for comparing the two categories. [src: amr_pangenome_atlas]

## Functional enrichment is also scope-dependent

Among 77K AMR clusters with eggNOG annotations compared with an 86M-cluster baseline, COG V, the Cluster of Orthologous Groups category for defense mechanisms, was 7.05x enriched at 14.9% versus 2.1%; COG P for inorganic ion transport was 1.93x enriched at 10.7% versus 5.6%; and COG J for translation was 1.50x enriched. [src: amr_pangenome_atlas] COG L for replication was depleted at 0.12x, COG I for lipid metabolism at 0.10x, and COG N for cell motility at 0.08x. [src: amr_pangenome_atlas]

The strong enrichment of defense and inorganic-ion transport functions is compatible with a broad resistance catalog that includes mercury- and arsenic-resistance genes, rather than demonstrating that antibiotic-resistance genes alone dominate these functional categories. [src: amr_pangenome_atlas] This **refines** [[concepts/pangenome-integration]] by showing that cross-dataset functional synthesis requires explicit control for catalog composition and label scope. [src: amr_pangenome_atlas]

## Detection and annotation coverage constrain interpretation

AMRFinderPlus detection methods were HMM at 51.5%, BLASTP at 22.7%, EXACTP at 13.0%, PARTIALP at 9.7%, and ALLELEP at 3.0% of hits. [src: amr_pangenome_atlas] Bakta product annotations and eggNOG hits were present for 93.0% of AMR clusters, while 7.0% had Bakta annotations only. [src: amr_pangenome_atlas] Among sparsely annotated one-source clusters, 55.4% were singletons compared with 34.6% of two-source clusters. [src: amr_pangenome_atlas] Zero AMR clusters had Pfam domain hits in the bakta_pfam_domains table, indicating non-overlapping target sequence space for the AMRFinderPlus and Pfam scans. [src: amr_pangenome_atlas]

These results **support** [[concepts/bioinformatic-representation-coverage-bias]] and [[concepts/structural-annotation-gap]]: observed resistome composition reflects detection modality, annotation support, and the possibility that singleton calls are artifacts as well as true species-specific genes. [src: amr_pangenome_atlas] The report specifically cautions that singleton inflation may cause some singleton AMR clusters to reflect annotation artifacts rather than true species-specific resistance genes. [src: amr_pangenome_atlas]

## Implications for environmental and clinical comparisons

Human/Clinical species carried 10.6 AMR clusters per species across 2,248 species, compared with 4.6 for Soil/Terrestrial across 2,469 species, 3.9 for Aquatic across 1,827 species, and 3.0 for Animal across 959 species; the difference was significant with Kruskal-Wallis H=440 and p=7.0e-93. [src: amr_pangenome_atlas] Clinical AMR was less core at 30.8% than soil AMR at 58.1% or plant AMR at 63.1%, supporting the interpretation that clinical environments select for acquired or mobile resistance while environmental AMR is more predominantly intrinsic. [src: amr_pangenome_atlas]

That environmental interpretation remains conditional because the catalog includes heavy-metal resistance and because genome databases over-represent clinical pathogens, potentially inflating AMR counts for human-associated species. [src: amr_pangenome_atlas] Of the 14,723 AMR-carrying species, 7,838, or 53.2%, received a non-Other/Unknown environment classification, while the Other/Unknown bin contained 46.8% of species because of sparse and inconsistent free-text isolation_source metadata in NCBI BioSample records. [src: amr_pangenome_atlas] These limitations **support** treating [[concepts/environmental-resistome]] comparisons as hypotheses about catalog-defined resistance distributions rather than complete measurements of environmental antibiotic resistance. [src: amr_pangenome_atlas]

## Tensions

The report simultaneously uses AMRFinderPlus as a broad resistance-gene catalog and interprets subsets as intrinsic, acquired, antibiotic, environmental, or clinical resistance. [src: amr_pangenome_atlas] The broad catalog supports detection of metal and other stress-resistance systems, whereas the narrow antibiotic-resistance interpretation is weakened by the inclusion of mercury- and arsenic-resistance families and by the 22.2% Other/Unclassified mechanism category. [src: amr_pangenome_atlas] This is a classification tension rather than a numerical contradiction, and it should be preserved when comparing this analysis with narrower resistome studies. [src: amr_pangenome_atlas]

## Open Directions

- Map the 83,008 AMRFinderPlus hits to CARD ARO terms and compare mechanism counts, core fractions, and environmental contrasts with the keyword-based classification to determine how much of the 18,448-hit Other/Unclassified category is reclassified. [src: amr_pangenome_atlas]
- Separate classical antibiotic-resistance genes from mercury-, arsenic-, and other stress-response genes, then repeat the 30.3% versus 46.8% core comparison and the 2.2x auxiliary-genome enrichment test to quantify the effect of catalog scope. [src: amr_pangenome_atlas]
- Reanalyze AMR functional enrichment using the 77K AMR clusters and 86M-cluster baseline after stratifying by mechanism and catalog class, asking whether the 7.05x COG V and 1.93x COG P enrichments persist for antibiotic-only genes. [src: amr_pangenome_atlas]
- Validate singleton AMR clusters with broader homology, domain, and synteny analyses, asking whether the 55.4% singleton rate among sparsely annotated one-source clusters represents annotation artifacts or genuine species-specific resistance. [src: amr_pangenome_atlas]
- Compare the catalog-defined environmental gradients against AMR calls in NMDC and MGnify metagenomes, using CARD ARO harmonization and metadata-stratified models to test whether clinical, soil, aquatic, and plant differences persist under comparable sampling and classification. [src: amr_pangenome_atlas]
