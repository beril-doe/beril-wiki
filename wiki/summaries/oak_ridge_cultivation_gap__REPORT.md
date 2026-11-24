---
type: "Summary"
description: "Summary of the project What Metabolic Functions Does the Cultured Collection Miss?."
doc_type: "short"
full_text: "sources/oak_ridge_cultivation_gap__REPORT.md"
---
# What Metabolic Functions Does the Cultured Collection Miss?

This report asks which metabolic functions a cultured isolate collection misses, compared with subsurface metagenome-assembled genomes (MAGs). It compares 3,110 ENIGMA Genome Depot cultured isolates, mostly from the Oak Ridge Field Research Center, with 2,279 QC-passing subsurface MAGs from kbase_ke_pangenome. [src: oak_ridge_cultivation_gap] The headline result is a large KO asymmetry. The report cautions that genome size and taxonomy drive much of it, and it treats the MAG-enriched KOs as the informative cultivation gaps. [src: oak_ridge_cultivation_gap] The report also proposes follow-up analyses, listed under Caveats and Open Work. [src: oak_ridge_cultivation_gap]

## Key Findings

### Overall scale of the difference

Most KOs differ between cohorts, and the cultured cohort carries more of them. Of 10,845 KOs tested (the union of both cohorts), 8,482 (78.2%) differed significantly (Fisher's exact test, Benjamini-Hochberg false discovery rate (BH-FDR) < 0.05). [src: oak_ridge_cultivation_gap] Of these, 7,669 were enriched in cultured genomes and 813 were depleted. [src: oak_ridge_cultivation_gap] In addition, 6,387 KOs appeared only in the cultured collection and 554 only in MAGs. [src: oak_ridge_cultivation_gap] The median log2 ratio for shared KOs was +2.22. [src: oak_ridge_cultivation_gap]

| Feature | Cultured | MAGs |
|---|---|---|
| Genomes | 3,110 (3,102 with KO annotations) [src: oak_ridge_cultivation_gap] | 2,279 [src: oak_ridge_cultivation_gap] |
| Unique KOs | 10,291 [src: oak_ridge_cultivation_gap] | 4,458 [src: oak_ridge_cultivation_gap] |
| Genome-KO pairs | 6,347,317 [src: oak_ridge_cultivation_gap] | 727,204 [src: oak_ridge_cultivation_gap] |
| Mean KOs per genome | 2,046 [src: oak_ridge_cultivation_gap] | 319 [src: oak_ridge_cultivation_gap] |
| Genome size | 5.8 Mbp mean [src: oak_ridge_cultivation_gap] | ~1.5 Mbp median [src: oak_ridge_cultivation_gap] |

### Genome size and taxonomy confound the comparison

The report attributes much of the asymmetry to genome-size disparity rather than specific functional selection, driven substantially by MAG taxonomic composition. [src: oak_ridge_cultivation_gap] It states that the headline 78% conflates genome-size asymmetry with true functional divergence. [src: oak_ridge_cultivation_gap] The 4-fold genome size difference (5.8 vs 1.5 Mbp) is called the dominant driver of the bias distribution. [src: oak_ridge_cultivation_gap] Cultured isolates are predominantly Proteobacteria with large genomes (5-7 Mbp), while the MAG cohort includes 40% Patescibacteria with streamlined genomes (0.5-1.5 Mbp). [src: oak_ridge_cultivation_gap] Patescibacteria (Candidate Phyla Radiation, CPR) make up about 40% of the 2,279 MAGs. [src: oak_ridge_cultivation_gap] Other major MAG phyla are Pseudomonadota (17%), Bacteroidota (8%) and Desulfobacterota. [src: oak_ridge_cultivation_gap] The report describes Patescibacteria as having ultra-small genomes (typically 0.5-1.5 Mbp), reduced metabolic capacity and probable obligate symbiotic lifestyles. [src: oak_ridge_cultivation_gap] It attributes the median MAG genome size of 1.5 Mbp to this dominance. [src: oak_ridge_cultivation_gap] It regards their near-absence from the cultured collection as expected, because host dependence and metabolic complementation resist standard cultivation. [src: oak_ridge_cultivation_gap] It calls the roughly 40% Patescibacteria in MAGs versus near-zero in cultured collections the single largest taxonomic bias in cultivation-based subsurface genomics. [src: oak_ridge_cultivation_gap] The cultured collection is dominated by Pseudomonadaceae (180 genomes), Variovorax (123), Cupriavidus (111) and other Burkholderiales. [src: oak_ridge_cultivation_gap]

The report reads most of the 7,669 cultured-enriched KOs as genes in larger cultivable genomes, not functions selected for by cultivation. It adds that the cultured collection genuinely does not sample CPR organisms. [src: oak_ridge_cultivation_gap] The 813 MAG-enriched KOs are the biologically informative cultivation gaps, because subsurface organisms carry them despite smaller genomes. [src: oak_ridge_cultivation_gap] The report predicts, without testing it here, that excluding Patescibacteria would give the remaining MAGs substantially more KOs per genome and narrow the apparent gap. [src: oak_ridge_cultivation_gap] A genome-size-normalized analysis, such as size-matched phyla, was not performed. [src: oak_ridge_cultivation_gap] The report also notes a long tail of MAG-enriched KOs of unknown or poorly characterized function that may represent novel subsurface metabolisms. [src: oak_ridge_cultivation_gap] It hypothesizes that the 554 MAG-only KOs likely include Patescibacteria-specific functions worth investigating for novel metabolisms. [src: oak_ridge_cultivation_gap]

### Hypothesis tests on marker pathways

Across 10 marker categories (36 KOs), H1 (depletion of specific deep-subsurface functions in cultured genomes) was partially supported. H2 (enrichment of cultivation-favorable functions) was strongly supported. [src: oak_ridge_cultivation_gap]

| Category | KOs | Mean log2 ratio | Direction | Significant KOs | Versus prediction |
|---|---|---|---|---|---|
| Wood-Ljungdahl | 5 | -1.58 | MAG-enriched | 4/5 | Yes (depleted) [src: oak_ridge_cultivation_gap] |
| NiFe-hydrogenase | 2 | +6.26 | Cultured-enriched | 2/2 | No (predicted depleted) [src: oak_ridge_cultivation_gap] |
| Sulfate reduction | 5 | +0.79 | Mixed | 4/5 | Partial [src: oak_ridge_cultivation_gap] |
| Denitrification | 6 | +2.05 | Cultured-enriched | 6/6 | Variable as predicted [src: oak_ridge_cultivation_gap] |
| Methanogenesis | 3 | +0.98 | Neither (too rare) | 0/3 | N/A [src: oak_ridge_cultivation_gap] |
| N-fixation | 3 | +1.56 | Mixed | 2/3 | Variable as predicted [src: oak_ridge_cultivation_gap] |
| Metal resistance | 4 | +3.33 | Cultured-enriched | 4/4 | Partial [src: oak_ridge_cultivation_gap] |
| Motility/chemotaxis | 3 | +7.23 | Cultured-enriched | 3/3 | Yes (enriched) [src: oak_ridge_cultivation_gap] |
| Aerobic respiration | 3 | +7.29 | Cultured-enriched | 3/3 | Yes (enriched) [src: oak_ridge_cultivation_gap] |
| Conjugation/MGE | 2 | +3.08 | Cultured-enriched | 2/2 | No (predicted depleted) [src: oak_ridge_cultivation_gap] |

### Functions depleted in cultured genomes

For the Wood-Ljungdahl pathway, 4 of 5 marker KOs were significantly depleted in cultured genomes (mean log2 ratio = -1.58). [src: oak_ridge_cultivation_gap] The CO dehydrogenase/acetyl-CoA synthase complex (K00194, K00197, K00198) showed 3.5-3.8 log2 depletion. The report calls this consistent with a hallmark of uncultivated deep-subsurface lineages. [src: oak_ridge_cultivation_gap] These components support autotrophic carbon fixation under anaerobic, energy-limited conditions. [src: oak_ridge_cultivation_gap] The report calls Wood-Ljungdahl components hallmarks of autotrophic lifestyles under energy limitation. [src: oak_ridge_cultivation_gap] It warns that Wood-Ljungdahl carbon fixation and dissimilatory sulfite reduction are systematically underrepresented in ENIGMA's cultured collection. [src: oak_ridge_cultivation_gap] K15023 was in 0.6% of cultured genomes and no MAGs, and the report suggests it is likely a mis-annotated or divergent variant. [src: oak_ridge_cultivation_gap]

Sulfate reduction was heterogeneous. The dsrAB genes (K11180, K11181) were 3.0-3.1 log2 depleted in cultured genomes. [src: oak_ridge_cultivation_gap] They serve terminal electron acceptor metabolism. [src: oak_ridge_cultivation_gap] aprAB (K00394) showed no significant difference. [src: oak_ridge_cultivation_gap] sat/PAPSS (K00395, K00958) were cultured-enriched. [src: oak_ridge_cultivation_gap] The report suggests this indicates different taxonomic distributions of the two subsystems. [src: oak_ridge_cultivation_gap]

Methanogenesis mcrABG (K00399-K00402) occurred in only 3 cultured genomes (0.1%) and zero MAGs. This is too rare to give a meaningful signal. [src: oak_ridge_cultivation_gap]

### Functions enriched in cultured genomes

Aerobic-respiration coxABC markers had mean log2 enrichment of +7.29 and 91% prevalence in cultured genomes. [src: oak_ridge_cultivation_gap] coxA and coxC were completely absent from MAGs. [src: oak_ridge_cultivation_gap] Motility/chemotaxis markers (fliC, cheA, cheW) had mean log2 = +7.23 and 80% cultured prevalence [src: oak_ridge_cultivation_gap], and cheA and cheW were absent from all MAGs. [src: oak_ridge_cultivation_gap] All 6 denitrification marker KOs tested were enriched (log2 +1.5 to +3.0), with narGH strongest. [src: oak_ridge_cultivation_gap] All 4 metal-resistance marker KOs tested were enriched (log2 +1.5 to +5.9) [src: oak_ridge_cultivation_gap], and arsC was in 89% of cultured genomes versus 14% of MAGs. [src: oak_ridge_cultivation_gap]

The report says enrichment of aerobic respiration (log2 = +7.3), motility/chemotaxis (log2 = +7.2) and denitrification (log2 = +2.1) recapitulates the porewater-bias signature first documented in clay_confined_subsurface. [src: oak_ridge_cultivation_gap] It interprets this as systematic cultivation selection for organisms from mobile, oxygenated porewater, adapted to flow, oxygen gradients and high-energy electron acceptors. [src: oak_ridge_cultivation_gap] The enrichment is consistent across clay and mixed groundwater/aquifer lithologies. [src: oak_ridge_cultivation_gap] The report suggests porewater bias appears to be a general property of cultivation-based genome collections, not specific to one lithology. [src: oak_ridge_cultivation_gap]

### Unexpected results

NiFe-hydrogenase (K06281, K06282) was predicted to be depleted in cultured genomes. It instead occurred in ~7.5% of cultured genomes and 0% of MAGs (log2 = +6.2). [src: oak_ridge_cultivation_gap] The report says this contradicts the Beaver & Neufeld (2024) prediction that group 1 [NiFe]-hydrogenases concentrate in uncultivated lineages. Either the cultured collection captures hydrogenotrophs better than expected, or the KO assignment conflates hydrogenase groups. [src: oak_ridge_cultivation_gap]

Conjugation markers virB4 and virD4 were predicted to be depleted through plasmid loss during cultivation. They were instead enriched (log2 +2.8 to +3.3). [src: oak_ridge_cultivation_gap] The report interprets the genomically encoded conjugation apparatus as well retained. It suggests the Goff et al. (2024) prediction of MGE (mobile genetic element) depletion may apply specifically to episomal elements not captured by whole-genome sequencing of either cohort. [src: oak_ridge_cultivation_gap] The report says the enrichment contradicts the Goff et al. (2024) prediction, based on MGEs from contaminated Oak Ridge subsurface enriched in heavy metal resistance gene clusters. [src: oak_ridge_cultivation_gap] It hypothesizes that the result reflects genomically integrated conjugation machinery retained by isolates versus episomal MGEs lost during cultivation. [src: oak_ridge_cultivation_gap] It cites Kothari et al. (2019) for large circular plasmids in ORFRC plasmidomes. [src: oak_ridge_cultivation_gap]

## Annotation cross-validation

The report compared Genome Depot native KO calls with eggNOG-mapper annotations from the KBase Data Lakehouse pangenome for 147 ENIGMA cultured genomes matched by accession (153 ENIGMA records, 147 unique pangenome genomes). [src: oak_ridge_cultivation_gap] Pooled across the genomes, the pipelines agree on 5,751 KOs, with 1,505 Depot-only and 148 eggNOG-only assignments, a pooled Jaccard similarity of 0.777. [src: oak_ridge_cultivation_gap] Per-genome Jaccard is much lower (median 0.140, IQR 0.057-0.400). [src: oak_ridge_cultivation_gap] The report attributes this to eggNOG calling a narrower KO set per genome (typically ~1,000-1,800 KOs vs ~1,500-2,200 for the Depot), which inflates the union denominator. [src: oak_ridge_cultivation_gap] It concludes that pooled agreement supports Genome Depot KOs as a reliable reference. It reads the per-genome gap as pipeline sensitivity differences, not systematic disagreement about present functions. [src: oak_ridge_cultivation_gap]

## Supporting literature and significance

The report cites literature on the Wood-Ljungdahl pathway in uncultivated subsurface lineages. Takami et al. (2012) showed a deeply branching thermophilic bacterium with the acetyl-CoA pathway dominating a subsurface ecosystem, and called the pathway among the most ancient bacterial strategies. [src: oak_ridge_cultivation_gap] Jungbluth et al. (2017) found deep subsurface Firmicutes with Wood-Ljungdahl, hydrogenotrophy and dissimilatory sulfate reduction in marine and terrestrial systems. [src: oak_ridge_cultivation_gap] Merino et al. (2020) found novel Actinobacteria with the pathway in a serpentinizing system, the first report for Actinobacteriota. [src: oak_ridge_cultivation_gap]

For Patescibacteria, Westmeijer et al. (2026) showed that cell-size fractionation of deep groundwater enriches Patescibacteria, Nanobdellota and Omnitrophota, which resist standard cultivation. [src: oak_ridge_cultivation_gap] Ruiz-Gonzalez et al. (2025) documented diverse Patescibacteria along a subterranean estuary. [src: oak_ridge_cultivation_gap] Gios et al. (2025) showed HGT (horizontal gene transfer) shapes their metabolic capacities, with up to 13% of genome content attributed to HGT. [src: oak_ridge_cultivation_gap] Chaudhari et al. (2024) showed genome streamlining in Parcubacteria moving from soil to groundwater. [src: oak_ridge_cultivation_gap]

The report presents this as the first quantitative per-function cultivation-coverage analysis comparing matched cultured and MAG cohorts for a well-characterized subsurface system. [src: oak_ridge_cultivation_gap] Its cultivation_bias_diagnostic() function can be applied to any two genome-KO matrices in other KBase Data Lakehouse projects. [src: oak_ridge_cultivation_gap] The function is provided by notebook 07_bias_diagnostic_module.ipynb [src: oak_ridge_cultivation_gap], and notebook 08_synthesis.ipynb provides summary statistics and a combined figure. [src: oak_ridge_cultivation_gap]

## Data and Methods

The cultured cohort is 3,110 ENIGMA Genome Depot isolate genomes, and the MAG cohort is 2,279 QC-passing subsurface MAGs from groundwater, aquifer and subsurface samples globally. [src: oak_ridge_cultivation_gap] KO prevalence was compared with Fisher's exact test and BH-FDR < 0.05. [src: oak_ridge_cultivation_gap] Of the cultured genomes, 3,102 had KO annotations. [src: oak_ridge_cultivation_gap] Cultured genomes were annotated by the ENIGMA Genome Depot pipeline (unknown tool version), and MAG KOs came from bakta via kbase_ke_pangenome.bakta_db_xrefs. [src: oak_ridge_cultivation_gap] Cultured genome inventory and KOs came from enigma_genome_depot_enigma tables, and the revised MAG cohort from kbase_ke_pangenome tables. [src: oak_ridge_cultivation_gap] The original MAG inventory used enigma_coral tables, but assembly FASTAs were inaccessible. [src: oak_ridge_cultivation_gap]

## Caveats and Open Work

- The MAG side was originally scoped to 623 ORFRC-specific MAGs from enigma_coral. Their assembly FASTAs were inaccessible from JupyterHub, so the report's findings concern subsurface systems generally rather than Oak Ridge specifically. [src: oak_ridge_cultivation_gap] The report says the results do not directly measure the cultivation gap at Oak Ridge, though the broader comparison is arguably more generalizable. [src: oak_ridge_cultivation_gap]
- The cultured collection spans 20+ years of isolation, primarily at ORFRC, while MAGs span global sites, so composition differences may reflect geography as much as cultivation bias. [src: oak_ridge_cultivation_gap]
- Genome-size disparity and Patescibacteria dominance confound the cultured-enriched KO counts. [src: oak_ridge_cultivation_gap] No genome-size-normalized analysis was performed. [src: oak_ridge_cultivation_gap]
- The report's prediction that excluding Patescibacteria would narrow the gap is stated as an expectation. [src: oak_ridge_cultivation_gap]
- MAGs are incomplete (mean completeness 78.7% in the QC-filtered cohort), so some KOs scored absent may lie in the missing 20% of the genome. [src: oak_ridge_cultivation_gap] This makes the 813 MAG-enriched KOs a conservative estimate, and some cultured-enriched KOs may be false positives. [src: oak_ridge_cultivation_gap]
- Annotation-pipeline sensitivity differences could bias the comparison, though KO-level comparison is more robust than pathway-level. [src: oak_ridge_cultivation_gap]
- The NiFe-hydrogenase result may reflect KO assignments that conflate hydrogenase groups. [src: oak_ridge_cultivation_gap]

### Next analyses proposed by the report

- Genome-size-normalized analysis: repeat the comparison in phyla represented in both cohorts, with size-matched genomes, to separate cultivation selection from genome streamlining. [src: oak_ridge_cultivation_gap]
- ORFRC-specific MAG comparison: when CORAL assembly FASTAs become accessible through JupyterHub or MinIO/CTS, annotate the 623 ORFRC-specific MAGs to produce a site-matched cultivation-coverage table. [src: oak_ridge_cultivation_gap]
- Investigate the 554 MAG-only KOs, which likely include Patescibacteria-specific functions. [src: oak_ridge_cultivation_gap] Cross-referencing them with the HGT analysis of Gios et al. (2025) could show which were horizontally acquired. [src: oak_ridge_cultivation_gap]
- Accessory genome analysis: compare plasmid- and prophage-borne content between cohorts using the pangenome's bakta annotations, to test the Goff et al. (2024) prediction that MGE-borne metal resistance is specifically depleted in cultured isolates. [src: oak_ridge_cultivation_gap]
- Cross-site generalization: apply cultivation_bias_diagnostic() to other KBase Data Lakehouse sites with both cultured and MAG collections, to test whether the porewater-bias signature is universal across subsurface environments. [src: oak_ridge_cultivation_gap]

## Slots Into

- [[concepts/genome-size-and-taxonomic-composition-confounding-of-cultured-versus-mag-functional-comparisons]]: genome size (5.8 Mbp vs ~1.5 Mbp median) and CPR dominance drive much of the KO asymmetry. [src: oak_ridge_cultivation_gap] The proposed size-matched analysis would separate selection from streamlining. [src: oak_ridge_cultivation_gap]
- [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages]]: Wood-Ljungdahl and dsrAB depletion and the 554 MAG-only KOs mark what cultivation misses. [src: oak_ridge_cultivation_gap]
- [[concepts/porewater-bias-as-a-general-signature-of-cultivation-based-subsurface-collections]]: enrichment of aerobic respiration, motility and denitrification recapitulates the clay-subsurface signature. [src: oak_ridge_cultivation_gap] Other sites could test its universality. [src: oak_ridge_cultivation_gap]
- [[concepts/mobile-genetic-element-retention-in-cultured-isolates-versus-episomal-loss]]: virB4 and virD4 were enriched in cultured genomes, contrary to the plasmid-loss prediction. [src: oak_ridge_cultivation_gap] An accessory-genome comparison is proposed. [src: oak_ridge_cultivation_gap]
- [[concepts/annotation-pipeline-concordance-for-kegg-ortholog-calls]]: pooled Jaccard 0.777 against per-genome median 0.140 between Depot and eggNOG-mapper. [src: oak_ridge_cultivation_gap]
- [[entities/patescibacteria]]: about 40% of the MAGs, nearly absent from the cultured collection. [src: oak_ridge_cultivation_gap]
- [[entities/wood-ljungdahl-pathway]]: 4 of 5 marker KOs were depleted in cultured genomes. [src: oak_ridge_cultivation_gap]
- [[entities/group-1-nife-hydrogenase]]: the result contradicts the Beaver & Neufeld prediction. [src: oak_ridge_cultivation_gap]
- [[entities/cultivation-bias-diagnostic]]: the function can be applied to any two genome-KO matrices. [src: oak_ridge_cultivation_gap]
