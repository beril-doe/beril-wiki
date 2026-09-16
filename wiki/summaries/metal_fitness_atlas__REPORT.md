---
type: "Summary"
description: "Cross-species atlas of bacterial gene fitness under metal stress, showing that metal-important genes are enriched in the core genome and proposing a two-tier core-stress versus accessory-resistance model."
doc_type: "short"
full_text: "sources/metal_fitness_atlas__REPORT.md"
---
# Pan-Bacterial Metal Fitness Atlas

## Overview

This report presents a cross-species atlas of bacterial fitness under metal stress, combining 559 experiments across 31 organisms and 16 metals with 383,349 gene × metal fitness records, pangenome conservation analysis, conserved ortholog-family discovery, module analysis, and genome-scale prediction. Its central finding is that metal-important genes are predominantly core-genome genes rather than accessory resistance genes, supporting a core-genome robustness model while distinguishing general metal-sensitive cellular functions from specialized metal resistance. [src: metal_fitness_atlas]

## Key Findings

### 1. Metal-important genes are enriched in the core genome

Across 22 organisms and 14 metals, genes with significant metal-associated fitness defects were 87.4% core versus 76.9% core for baseline genes (OR=2.08, p=4.3e-162). This reverses the initial hypothesis that toxic-metal genes would be accessory-enriched and contrasts with the prior DvH condition-specific result of 71.2% core for heavy-metal genes. The report attributes the discrepancy to the present genome-wide definition, which captures core cellular processes vulnerable to metal disruption, including cell envelope functions, DNA repair, central metabolism, protein quality control, and general stress response. According to the atlas report, the prior DvH result from the field_vs_lab_fitness project ([[summaries/field_vs_lab_fitness__REPORT]]) found heavy-metal resistance genes to be the least conserved condition class (71.2% core) because that analysis isolated *condition-specific* genes, meaning those important only for metals and not for other stresses. The atlas argues that it instead captures all genes with any metal fitness defect, and that these are dominated by core stress-response functions. [src: metal_fitness_atlas] The field_vs_lab_fitness report describes its 71.2% figure differently. There it applies to 198 genes important (fitness < -2) under the heavy-metals condition class, a result that was not significant against a 76.3% baseline, and condition specificity is analyzed in a separate step. The atlas's exclusivity-based explanation is therefore its own interpretation, and the two reports' descriptions of the prior result are not reconciled. [src: metal_fitness_atlas, field_vs_lab_fitness]

Twenty-one of 22 organisms had metal-important genes that were more core than baseline, with 14 significant at p<0.05; *P. fluorescens* FW300-N2E3 had a negligible negative delta of -0.003 (p=0.70). [src: metal_fitness_atlas]

### 2. Essential metals show stronger core enrichment than toxic metals

Essential-metal tolerance genes for Fe, Mo, W, Se, and Mn had a mean core-fraction delta of +0.148, nearly double the toxic-metal delta of +0.081; the difference was significant by one-sided Mann-Whitney U testing (U=39, p=0.015). The strongest enrichments were manganese (+0.198, all 30 important genes core), zinc (+0.151), molybdenum (+0.148), tungsten (+0.145), and iron (+0.116). Twelve of 14 metals were individually significant at p<0.05; cadmium, tested in 1 organism, had delta=-0.010 (p=0.92), and uranium, tested in 2 organisms, had delta=+0.035 (p=0.34), with limited organism coverage identified as a likely explanation. [src: metal_fitness_atlas]

The per-metal conservation statistics were: manganese, 30 important genes, core fraction 1.000, delta +0.198, OR=inf, p=2.0e-03; zinc, 1,517, 0.890, +0.151, OR=2.94, p=2.0e-49; molybdenum, 302, 0.950, +0.148, OR=5.32, p=1.3e-14; tungsten, 303, 0.947, +0.145, OR=4.98, p=5.3e-14; mercury, 106, 0.934, +0.132, OR=3.62, p=1.6e-04; selenium, 134, 0.933, +0.131, OR=3.59, p=2.9e-05; iron, 651, 0.919, +0.116, OR=3.07, p=8.5e-18; aluminum, 1,381, 0.898, +0.107, OR=2.37, p=1.2e-26; copper, 2,139, 0.867, +0.090, OR=1.91, p=3.8e-27; nickel, 1,760, 0.877, +0.088, OR=1.93, p=3.0e-22; cobalt, 1,859, 0.859, +0.072, OR=1.67, p=8.1e-16; chromium, 262, 0.710, +0.060, OR=1.33, p=4.0e-02; uranium, 178, 0.685, +0.035, OR=1.18, p=3.4e-01; and cadmium, 92, 0.522, -0.010, OR=0.96, p=9.2e-01. [src: metal_fitness_atlas]

Excluding four duplicate *P. fluorescens* FW300 strains and retaining only pseudo3_N2E3 reduced the analysis from 22 to 18 organisms but left the enrichment robust: OR=2.065, p=5.9e-141, compared with OR=2.083, p=4.3e-162 with all organisms. Conservation analysis covered 22 of 31 metal-tested organisms (71%); nine organisms—Putida, Keio, SynE, Miya, Kang, BFirm, Cola, Ponti, and Dino—lacked Fitness Browser pangenome links. The report judges these excluded organisms taxonomically diverse, so it considers the exclusion unlikely to introduce systematic bias. [src: metal_fitness_atlas]

### 3. Scale of the metal fitness atlas

The Fitness Browser contained 559 metal-related experiments, representing 8.2% of 6,804 total experiments, across 16 metals. Six metals had cross-species coverage in at least three organisms: cobalt (27 organisms), nickel (26), copper (23), aluminum (22), zinc (17), and iron (3). DvH was the most metal-profiled organism, with 149 experiments across 13 metals; aluminum, cobalt, and nickel were the USGS critical minerals with broad Fitness Browser coverage. [src: metal_fitness_atlas]

Of the 31 organisms with metal data, only 24 had fitness matrices, so the gene-fitness dataset is narrower than the experiment-coverage scope. Across these 24 organisms, the atlas contained 383,349 gene × metal fitness records. The report's contributions list describes these records as spanning 24 organisms and 14 metals, not the 31-organism, 16-metal experiment-coverage scope. Of these records, 12,838 (3.3%) showed significant fitness defects and counted as broad metal-important genes, and 5,667 were classified as strict metal-important genes (1.5%). The report defines these genes inconsistently. Its findings section describes significant defects as fit < -1, |t| > 4, while its limitations section gives the broad definition as fit < -1 OR n_sick ≥ 1. Iron produced 12.3% important genes and molybdenum/tungsten produced 11.2%, compared with 2.7-4.4% for toxic metals. DvH had 1,366 metal-important genes, or 49.8% of its genome, across 13 metals, while *Synechococcus elongatus* had 33.6% of genes important across two metals. [src: metal_fitness_atlas]

### 4. Conserved metal gene families and novel candidates

Among 2,891 ortholog groups with metal phenotypes, 1,182 were conserved across at least two organisms and 601 across at least three organisms. The most broadly conserved family, OG00128, spanned 17 organisms and nine metals. Families with metal phenotypes in more organisms tended to have higher pangenome conservation, consistent with their involvement in fundamental cellular processes. [src: metal_fitness_atlas]

The analysis identified 149 novel metal-biology candidates with conserved metal fitness phenotypes across at least two organisms but without full functional annotation: 89 were truly unknown, 43 had DUF/UPF domains (domain-of-unknown-function or uncharacterized-protein-family domains, meaning a known structural domain whose metal role is unknown), and 17 had partial functional hints such as transporter or hydrolase annotations without a characterized metal function. These candidates constitute function predictions based solely on cross-species fitness data. [src: metal_fitness_atlas]

### 5. Metal-responsive modules are core-enriched

Using z-scored module activity profiles standardized across all experiments per organism, the analysis identified 600 metal-responsive module records with |z| > 2.0 among 19,453 module × metal-experiment records (3.1%). DvH had 47 responsive modules across 12 metals, and psRCH2 had 11 modules across six metals. The 183 responsive modules with conservation data had a mean core fraction of 0.826 and a median of 0.929, reinforcing the core-enrichment pattern. [src: metal_fitness_atlas]

An initial analysis using raw activity scores from module_conditions.csv found zero responsive modules because raw scores, whose maximum was 0.96, were on a different scale from z-scores; per-experiment profiles with z-normalization resolved this issue. In the z-normalized analysis, psRCH2 had 11 responsive modules across 6 metals. [src: metal_fitness_atlas]

### 6. Pangenome-scale prediction

A metal functional signature containing 1,286 KEGG Orthology (KO) terms was derived from conserved metal gene families and used to score 27,702 pangenome species. After genome-size normalization by metal clusters divided by total KEGG-annotated clusters, *Leptospirillum* ranked at the 91st percentile, *Acidithiobacillus* at the 77th, *Marinobacter* at the 75th, and *Sulfobacillus* at the 71st. Bioleaching genera were not significantly enriched over background after normalization (Mann-Whitney p=0.17), indicating that metal-tolerance genes are broadly distributed rather than concentrated exclusively in specialists. Without normalization, species with large open pangenomes, including *K. pneumoniae* and *P. aeruginosa*, dominated scores because of genome size. [src: metal_fitness_atlas]

The simple gene-presence repertoire score failed to predict metal fitness, echoing the report's interpretation that gene essentiality is context-dependent and that regulatory or expression-based models are needed. [src: metal_fitness_atlas]

### 7. Interpretation: a two-tier metal-response model

The report proposes a two-tier model. Tier 1 consists of core general-stress functions, which make up the majority of metal fitness genes and remain conserved because they serve essential cellular roles beyond metal tolerance. Tier 2 consists of accessory specialized metal-resistance functions, including efflux, sequestration, and enzymatic detoxification, which are visible more clearly when genes important for general stress are excluded. Thus, the atlas refines rather than simply rejects the idea that metal resistance can be an accessory-genome trait. [src: metal_fitness_atlas]

## Caveats and Limitations

Metal coverage was uneven: cobalt and nickel were tested in 27 organisms, whereas uranium, chromium, mercury, cadmium, selenium, and manganese were tested in only one or two organisms. Consequently, cross-species patterns for rare metals largely reflect DvH and psRCH2 biology. The limitations section gives a 27-organism count for nickel, which conflicts with the 26-organism nickel count in the atlas-scale findings. The report does not reconcile the two. [src: metal_fitness_atlas]

Metal concentrations were not normalized by dose or tolerance threshold; for example, nickel concentrations ranged from 0.01-2.0 mM across organisms. Fitness effects therefore cannot be compared directly without accounting for each organism's relative exposure. [src: metal_fitness_atlas]

Phylogenetic non-independence remains a limitation because multiple *Pseudomonas fluorescens* strains can inflate apparent cross-species conservation, although exclusion of four duplicate FW300 strains left the principal core-enrichment result robust. [src: metal_fitness_atlas]

The broad metal-important definition, fit < -1 OR n_sick ≥ 1, captures approximately 3.3% of genes and includes many general stress genes rather than metal-specific resistance genes. This wording differs from the findings section, which describes significant fitness defects as fit < -1, |t| > 4. The report therefore recommends repeating the analysis with genes important for metals but not for other stresses. [src: metal_fitness_atlas]

Putatively essential genes, estimated at approximately 14.3% of protein-coding genes and approximately 82% core, lack transposon insertions and are absent from the fitness data. Because these genes are overwhelmingly core, their exclusion makes the observed core enrichment a conservative estimate. [src: metal_fitness_atlas]

The conservation analysis covered 22 of 48 organisms because only 22 had pangenome links; the report also states that 22 of 31 metal-tested organisms were covered in the primary conservation analysis. The nine excluded metal-tested organisms lacked Fitness Browser pangenome links, and 26 organisms lacked Fitness Browser pangenome mappings in the broader mapping context. [src: metal_fitness_atlas]

The repertoire prediction did not validate as a predictor of metal fitness. The report proposes several next steps. These are regulatory or expression-based modeling and normalizing fitness effects by metal concentration relative to MIC (minimum inhibitory concentration) to enable fair cross-species comparison. They also include phylogenetic independent contrasts to control for phylogenetic non-independence when comparing conservation patterns across organisms. The report proposes replacing the simple count-based metal score with a per-species hypergeometric enrichment test that controls for total functional annotation content. Finally, it proposes functional annotation of the 149 novel candidates using PaperBLAST, InterPro, and structural prediction (AlphaFold) to characterize the 89 truly unknown and 43 DUF-domain families with conserved metal phenotypes, whose functions remain uncharacterized. [src: metal_fitness_atlas]

## Proposed Experiments and Coverage Gaps

Six metals on the USGS critical minerals list are tested in only 1-2 organisms each. This limits the cross-species conservation analysis, and the report proposes expanding coverage to 5+ organisms each. [src: metal_fitness_atlas]

Manganese was tested in only 1 organism (DvH). The report describes DvH as showing 100% core enrichment (delta=+0.198) and asks whether this is universal. Testing in MR-1, Keio, Cup4G11, Putida, and Caulo is proposed. *Shewanella* MR-1, which can reduce Mn(IV), would test whether metal reducers show different conservation patterns. This is a single-organism result, and its generality is untested. [src: metal_fitness_atlas]

Chromium fitness coverage is 2 organisms (DvH and psRCH2), and testing in MR-1, Cup4G11, Keio, and pseudo3_N2E3 is proposed. The Oak Ridge FW300 *Pseudomonas* strains were isolated from Cr-contaminated groundwater but have never been tested against chromate. [src: metal_fitness_atlas]

Uranium, the central ENIGMA contaminant, also has fitness coverage in only 2 organisms (DvH and psRCH2). Its core-fraction delta is +0.035 and not significant (p=0.34). The report states that more organisms (proposed: MR-1, ANA3, PV4, Cup4G11) would determine whether uranium fitness genes are truly neutral or the effect was underpowered. The current data cannot distinguish these possibilities. [src: metal_fitness_atlas]

Tungsten was tested in only 1 organism (DvH), which shows strong core enrichment (delta=+0.145). Testing archaea (Methanococcus_S2, Methanococcus_JJ) and Keio is proposed to reveal whether W dependence is unique to sulfate reducers. [src: metal_fitness_atlas]

No rare-earth-element (REE) experiments exist in the Fitness Browser. The report proposes lanthanum chloride (0.1-1 mM) in Putida, Cup4G11, Keio, and Marino. It describes RB-TnSeq (random barcode transposon sequencing, a pooled mutant-fitness assay) under La stress as able to identify the first genome-wide gene set for REE tolerance. It also proposes cerium chloride (0.1-1 mM) in the same panel, to test whether REE tolerance uses a shared or element-specific gene set. These are proposed, not completed, experiments. [src: metal_fitness_atlas]

The report's prose says that two organisms have disproportionately many novel metal candidate genes (54 each) but have been tested against only 1 metal (iron). Its table counts these candidates as novel ortholog groups (OGs), not individual genes. The two organisms are *Methanococcus maripaludis* S2, with 54 novel candidate ortholog groups, and *Methanococcus maripaludis* JJ, also with 54. For S2, the report proposes Ni, Co, Cu, Zn, W, and Mo tests, citing archaeal under-representation and unique metal cofactor requirements (Ni for hydrogenase, W/Mo for formylmethanofuran dehydrogenase). For JJ, it proposes the same panel to enable cross-strain comparison with S2. The broader-metal predictions for both remain unvalidated. [src: metal_fitness_atlas]

*Pseudomonas putida* KT2440 (Putida) has fitness matrices in the Fitness Browser but zero metal experiments. The report calls it the only Fitness Browser organism with no metal data. Putida has the 5th-highest metal gene repertoire score among all Fitness Browser organisms (0.707). A full metal panel (Co, Ni, Cu, Zn, Al, Cr, U) is proposed to validate or refute this prediction. The report's coverage note nonetheless lists Putida among the 9 metal-tested organisms excluded from the conservation analysis. The report does not reconcile the two statements. [src: metal_fitness_atlas]

The atlas scores 27,702 species but cannot validate predictions for organisms without RB-TnSeq libraries. *Acidithiobacillus ferrooxidans*, which the report calls the #1 bioleaching organism, ranks at the 77th percentile after normalization. However, no TnSeq data exist for any *Acidithiobacillus* species, and RB-TnSeq under Fe, Cu, Co, Ni, and Zn is proposed. [src: metal_fitness_atlas]

The report also proposes, but has not performed, RB-TnSeq in two further species. The first is *Geobacter sulfurreducens* (53rd percentile after normalization) under Fe(III), Mn(IV), and U(VI) reduction conditions, to identify genes for extracellular electron transfer and metal transformation. The second is *Leptospirillum ferrooxidans* (91st percentile after normalization, the highest-scoring bioleaching genus), under Fe(II) oxidation and acid conditions. [src: metal_fitness_atlas]

If these experiments were performed, the report projects that the atlas would expand from 14 to 16+ metals (adding REEs) and from 24 to 27+ organisms with fitness data. Coverage for critical metals would expand from 1-2 organisms to 5+. Cross-species statistical power for manganese, chromium, uranium, and tungsten would increase from suggestive to definitive, and the 149 novel candidates could be directly validated. These are conditional projections, not observed results. [src: metal_fitness_atlas]

## Figures

The report's figures are as follows. [src: metal_fitness_atlas]
- `organism_metal_matrix.png`: heatmap of experiment counts per organism × metal.
- `metal_fitness_distributions.png`: mean fitness score distributions under each metal.
- `metal_important_genes_by_organism.png`: % metal-important genes per organism × metal.
- `core_fraction_by_metal.png`: core fraction of metal-important versus baseline genes per metal.
- `metal_conservation_by_organism.png`: core enrichment delta per organism.
- `metal_family_conservation_heatmap.png`: family breadth distribution and conservation trend.
- `metal_module_activity_heatmap.png`: z-scored module activity under metal conditions.
- `species_metal_score_distribution.png`: pangenome-scale metal score distribution and per-genus comparison.
- `bioleaching_species_scores.png`: metal tolerance scores for key bioleaching/metal-reducing species.
- `summary_atlas_overview.png`: three-panel atlas overview (experiments, impact, conservation).
- `summary_metal_families.png`: family breadth and novel versus annotated breakdown.

## Data Sources and Output Files

The [[entities/kescience-fitnessbrowser]] collection supplied the genefitness, expcondition, experiment, and ortholog tables, which provided metal fitness scores, experiment metadata, and cross-organism orthologs. The [[entities/kbase-ke-pangenome]] collection supplied the gene_cluster and eggnog_mapper_annotations tables for core/accessory classification and functional annotations. [src: metal_fitness_atlas]

The experiment analysis subset file, data/metal_experiments_analysis.csv, contains 379 records after excluding Platinum/Cisplatin experiments. The generated signature file, data/metal_functional_signature.csv, lists 1,287 KEGG/PFAM terms, whereas the key finding describes a signature of 1,286 KEGG KO terms. The report does not reconcile the differing counts or term scopes. [src: metal_fitness_atlas]

## Slots Into

- [[concepts/metal-cross-resistance]] — the atlas separates broadly required core metal-stress functions from accessory, specialized metal-resistance mechanisms and supplies cross-metal conservation statistics. [src: metal_fitness_atlas]
- [[concepts/condition-specific-fitness]] — the report directly contrasts broad metal fitness defects with condition-specific heavy-metal genes, explaining why the former are 87.4% core while the prior condition-specific result was 71.2% core. [src: metal_fitness_atlas]
- [[concepts/pangenome-integration]] — 1,182 conserved metal families, core/accessory classification, and genome-size-normalized scores across 27,702 pangenome species connect fitness data to pangenome structure. [src: metal_fitness_atlas]
- [[concepts/gene-essentiality]] — exclusion of putatively essential genes and failure of simple gene-presence repertoire scores highlight context dependence and limits on inferring metal fitness from gene content. [src: metal_fitness_atlas]
- [[concepts/multi-omics-integration]] — ICA (independent component analysis) module responsiveness links gene-level metal fitness to module-level activity, while the proposed regulatory and expression-based models identify a multi-omic extension. [src: metal_fitness_atlas]
- [[concepts/pangenome-conservation-fitness-decoupling]] — metal-important genes are 87.4% core versus a 76.9% baseline and are more core in 21 of 22 organisms. Per-metal deltas range from +0.198 (manganese) to -0.010 (cadmium), linking fitness importance to conservation. [src: metal_fitness_atlas]
- [[concepts/two-speed-bacterial-genome]] — core general-stress functions and accessory specialized resistance (efflux, sequestration, enzymatic detoxification) form a proposed two-tier genome model. [src: metal_fitness_atlas]
- [[concepts/shared-stress-versus-stressor-specific-fitness]] — the broad metal-important definition captures mostly general stress genes; specialized metal resistance becomes visible only after controlling for general stress response. [src: metal_fitness_atlas]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — multiple *P. fluorescens* strains can inflate conservation, yet excluding 4 duplicate FW300 strains still leaves OR=2.065, p=5.9e-141. [src: metal_fitness_atlas]
- [[concepts/sampling-depth-and-downsampling-effects]] — reducing the analysis from 22 to 18 organisms serves as a robustness check on the enrichment result. [src: metal_fitness_atlas]
- [[concepts/experimental-prioritization-of-functional-dark-matter]] — 149 novel metal-biology candidates (89 unknown, 43 DUF/UPF, 17 with partial hints) are prioritized from fitness data alone. [src: metal_fitness_atlas]
- [[concepts/fitness-module-detection-sensitivity]] — raw module activity scores (max 0.96) yielded 0 responsive modules, whereas z-normalization yielded 600 responsive records. [src: metal_fitness_atlas]
- [[concepts/composite-resistance-score-limitations]] — the 1,286-KO signature score is dominated by genome size without normalization and shows no significant bioleaching-genus enrichment (p=0.17); gene presence/absence also failed to predict metal tolerance. [src: metal_fitness_atlas]
- [[concepts/lab-field-fitness-concordance]] — bioleaching genera were not significantly enriched (p=0.17). This null result leaves open, rather than settles, whether laboratory-derived metal signatures can distinguish environmental metal specialists. [src: metal_fitness_atlas]
- [[concepts/pangenome-openness-determinants]] — large open pangenomes (*K. pneumoniae*, *P. aeruginosa*) dominate unnormalized repertoire scores. [src: metal_fitness_atlas]
- [[concepts/genetic-perturbation-coverage-bias]] — only 24 of 31 organisms with metal data have fitness matrices. Predictions for the 27,702 scored species cannot be validated for organisms without RB-TnSeq libraries; for example, no TnSeq data exist for any *Acidithiobacillus* species. [src: metal_fitness_atlas]
- [[concepts/fitness-condition-coverage-prioritization-bias]] — cobalt and nickel were tested in many organisms, while six metals were tested in only 1-2, so rare-metal patterns reflect DvH and psRCH2. No REE experiments exist, and Putida has zero metal experiments. [src: metal_fitness_atlas]
- [[concepts/ontology-and-category-schema-sensitivity]] — the atlas attributes the gap between its 87.4% core result and the prior 71.2% to broad versus condition-specific gene definitions. The field_vs_lab_fitness report describes its own definition differently. [src: metal_fitness_atlas, field_vs_lab_fitness]
- [[concepts/transposon-callability-bias]] — putatively essential genes (~14.3%, ~82% core) lack insertions and are absent from fitness data. [src: metal_fitness_atlas]
