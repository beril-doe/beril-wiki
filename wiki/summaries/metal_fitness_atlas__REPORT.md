---
type: "Summary"
description: "Cross-species atlas shows metal fitness genes are predominantly core-genome functions."
doc_type: "short"
full_text: "sources/metal_fitness_atlas__REPORT.md"
---
# Pan-Bacterial Metal Fitness Atlas

## Overview

This report presents a cross-species atlas of bacterial fitness under metal stress, combining 559 experiments across 31 organisms and 16 metals with 383,349 gene × metal fitness records, pangenome conservation analysis, conserved ortholog-family discovery, module analysis, and genome-scale prediction. Its central finding is that metal-important genes are predominantly core-genome genes rather than accessory resistance genes, supporting a core-genome robustness model while distinguishing general metal-sensitive cellular functions from specialized metal resistance. [src: metal_fitness_atlas]

## Key Findings

### 1. Metal-important genes are enriched in the core genome

Across 22 organisms and 14 metals, genes with significant metal-associated fitness defects were 87.4% core versus 76.9% core for baseline genes (OR=2.08, p=4.3e-162). This reverses the initial hypothesis that toxic-metal genes would be accessory-enriched and contrasts with the prior DvH condition-specific result of 71.2% core for heavy-metal genes. The report attributes the discrepancy to the present genome-wide definition, which captures core cellular processes vulnerable to metal disruption, including cell envelope functions, DNA repair, central metabolism, protein quality control, and general stress response. [src: metal_fitness_atlas]

Twenty-one of 22 organisms had metal-important genes that were more core than baseline, with 14 significant at p<0.05; *P. fluorescens* FW300-N2E3 had a negligible negative delta of -0.003 (p=0.70). [src: metal_fitness_atlas]

### 2. Essential metals show stronger core enrichment than toxic metals

Essential-metal tolerance genes for Fe, Mo, W, Se, and Mn had a mean core-fraction delta of +0.148, nearly double the toxic-metal delta of +0.081; the difference was significant by one-sided Mann-Whitney U testing (U=39, p=0.015). The strongest enrichments were manganese (+0.198, all 30 important genes core), zinc (+0.151), molybdenum (+0.148), tungsten (+0.145), and iron (+0.116). Twelve of 14 metals were individually significant at p<0.05; cadmium had delta=-0.010 (p=0.92) and uranium had delta=+0.035 (p=0.34), with limited organism coverage identified as a likely explanation. [src: metal_fitness_atlas]

The per-metal conservation statistics were: manganese, 30 important genes, core fraction 1.000, delta +0.198, OR=inf, p=2.0e-03; zinc, 1,517, 0.890, +0.151, OR=2.94, p=2.0e-49; molybdenum, 302, 0.950, +0.148, OR=5.32, p=1.3e-14; tungsten, 303, 0.947, +0.145, OR=4.98, p=5.3e-14; mercury, 106, 0.934, +0.132, OR=3.62, p=1.6e-04; selenium, 134, 0.933, +0.131, OR=3.59, p=2.9e-05; iron, 651, 0.919, +0.116, OR=3.07, p=8.5e-18; aluminum, 1,381, 0.898, +0.107, OR=2.37, p=1.2e-26; copper, 2,139, 0.867, +0.090, OR=1.91, p=3.8e-27; nickel, 1,760, 0.877, +0.088, OR=1.93, p=3.0e-22; cobalt, 1,859, 0.859, +0.072, OR=1.67, p=8.1e-16; chromium, 262, 0.710, +0.060, OR=1.33, p=4.0e-02; uranium, 178, 0.685, +0.035, OR=1.18, p=3.4e-01; and cadmium, 92, 0.522, -0.010, OR=0.96, p=9.2e-01. [src: metal_fitness_atlas]

Excluding four duplicate *P. fluorescens* FW300 strains and retaining only pseudo3_N2E3 reduced the analysis from 22 to 18 organisms but left the enrichment robust: OR=2.065, p=5.9e-141, compared with OR=2.083, p=4.3e-162 with all organisms. Conservation analysis covered 22 of 31 metal-tested organisms (71%); nine organisms—Putida, Keio, SynE, Miya, Kang, BFirm, Cola, Ponti, and Dino—lacked Fitness Browser pangenome links. [src: metal_fitness_atlas]

### 3. Scale of the metal fitness atlas

The Fitness Browser contained 559 metal-related experiments, representing 8.2% of 6,804 total experiments, across 16 metals. Six metals had cross-species coverage in at least three organisms: cobalt (27 organisms), nickel (26), copper (23), aluminum (22), zinc (17), and iron (3). DvH was the most metal-profiled organism, with 149 experiments across 13 metals; aluminum, cobalt, and nickel were the USGS critical minerals with broad Fitness Browser coverage. [src: metal_fitness_atlas]

Across 24 organisms with fitness matrices, the atlas contained 383,349 gene × metal fitness records and 12,838 broad metal-important genes (3.3%); 5,667 were classified as strict metal-important genes (1.5%). The broad definition was fit < -1 or n_sick ≥ 1. Iron produced 12.3% important genes and molybdenum/tungsten produced 11.2%, compared with 2.7-4.4% for toxic metals. DvH had 1,366 metal-important genes, or 49.8% of its genome, across 13 metals, while *Synechococcus elongatus* had 33.6% of genes important across two metals. [src: metal_fitness_atlas]

### 4. Conserved metal gene families and novel candidates

Among 2,891 ortholog groups with metal phenotypes, 1,182 were conserved across at least two organisms and 601 across at least three organisms. The most broadly conserved family, OG00128, spanned 17 organisms and nine metals. Families with metal phenotypes in more organisms tended to have higher pangenome conservation, consistent with their involvement in fundamental cellular processes. [src: metal_fitness_atlas]

The analysis identified 149 novel metal-biology candidates with conserved metal fitness phenotypes across at least two organisms but without full functional annotation: 89 were truly unknown, 43 had DUF/UPF domains, and 17 had partial functional hints such as transporter or hydrolase annotations without a characterized metal function. These candidates constitute function predictions based solely on cross-species fitness data. [src: metal_fitness_atlas]

### 5. Metal-responsive modules are core-enriched

Using z-scored module activity profiles standardized across all experiments per organism, the analysis identified 600 metal-responsive module records with |z| > 2.0 among 19,453 module × metal-experiment records (3.1%). DvH had 47 responsive modules across 12 metals, and psRCH2 had 11 modules across six metals. The 183 responsive modules with conservation data had a mean core fraction of 0.826 and a median of 0.929, reinforcing the core-enrichment pattern. [src: metal_fitness_atlas]

An initial analysis using raw activity scores from module_conditions.csv found zero responsive modules because raw scores, whose maximum was 0.96, were on a different scale from z-scores; per-experiment profiles with z-normalization resolved this issue. [src: metal_fitness_atlas]

### 6. Pangenome-scale prediction

A metal functional signature containing 1,286 KEGG KO terms was derived from conserved metal gene families and used to score 27,702 pangenome species. After genome-size normalization by metal clusters divided by total KEGG-annotated clusters, *Leptospirillum* ranked at the 91st percentile, *Acidithiobacillus* at the 77th, *Marinobacter* at the 75th, and *Sulfobacillus* at the 71st. Bioleaching genera were not significantly enriched over background after normalization (Mann-Whitney p=0.17), indicating that metal-tolerance genes are broadly distributed rather than concentrated exclusively in specialists. Without normalization, species with large open pangenomes, including *K. pneumoniae* and *P. aeruginosa*, dominated scores because of genome size. [src: metal_fitness_atlas]

The simple gene-presence repertoire score failed to predict metal fitness, echoing the report's interpretation that gene essentiality is context-dependent and that regulatory or expression-based models are needed. [src: metal_fitness_atlas]

### 7. Interpretation: a two-tier metal-response model

The report proposes a two-tier model. Tier 1 consists of core general-stress functions, which make up the majority of metal fitness genes and remain conserved because they serve essential cellular roles beyond metal tolerance. Tier 2 consists of accessory specialized metal-resistance functions, including efflux, sequestration, and enzymatic detoxification, which are visible more clearly when genes important for general stress are excluded. Thus, the atlas refines rather than simply rejects the idea that metal resistance can be an accessory-genome trait. [src: metal_fitness_atlas]

## Caveats and Limitations

Metal coverage was uneven: cobalt and nickel were tested in 27 organisms, whereas uranium, chromium, mercury, cadmium, selenium, and manganese were tested in only one or two organisms. Consequently, cross-species patterns for rare metals largely reflect DvH and psRCH2 biology. [src: metal_fitness_atlas]

Metal concentrations were not normalized by dose or tolerance threshold; for example, nickel concentrations ranged from 0.01-2.0 mM across organisms. Fitness effects therefore cannot be compared directly without accounting for each organism's relative exposure. [src: metal_fitness_atlas]

Phylogenetic non-independence remains a limitation because multiple *Pseudomonas fluorescens* strains can inflate apparent cross-species conservation, although exclusion of four duplicate FW300 strains left the principal core-enrichment result robust. [src: metal_fitness_atlas]

The broad metal-important definition, fit < -1 OR n_sick ≥ 1, captures approximately 3.3% of genes and includes many general stress genes rather than metal-specific resistance genes. The report therefore recommends repeating the analysis with genes important for metals but not for other stresses. [src: metal_fitness_atlas]

Putatively essential genes, estimated at approximately 14.3% of protein-coding genes and approximately 82% core, lack transposon insertions and are absent from the fitness data. Because these genes are overwhelmingly core, their exclusion makes the observed core enrichment a conservative estimate. [src: metal_fitness_atlas]

The conservation analysis covered 22 of 48 organisms because only 22 had pangenome links; the report also states that 22 of 31 metal-tested organisms were covered in the primary conservation analysis. The nine excluded metal-tested organisms lacked Fitness Browser pangenome links, and 26 organisms lacked Fitness Browser pangenome mappings in the broader mapping context. [src: metal_fitness_atlas]

The repertoire prediction did not validate as a predictor of metal fitness. The report identifies regulatory or expression-based modeling, concentration-relative-to-MIC normalization, phylogenetic independent contrasts, enrichment-based pangenome scoring, and functional annotation of the 149 novel candidates using PaperBLAST, InterPro, and structural prediction as required next steps. [src: metal_fitness_atlas]

## Slots Into

- [[concepts/metal-cross-resistance]] — the atlas separates broadly required core metal-stress functions from accessory, specialized metal-resistance mechanisms and supplies cross-metal conservation statistics. [src: metal_fitness_atlas]
- [[concepts/condition-specific-fitness]] — the report directly contrasts broad metal fitness defects with condition-specific heavy-metal genes, explaining why the former are 87.4% core while the prior condition-specific result was 71.2% core. [src: metal_fitness_atlas]
- [[concepts/pangenome-integration]] — 1,182 conserved metal families, core/accessory classification, and genome-size-normalized scores across 27,702 pangenome species connect fitness data to pangenome structure. [src: metal_fitness_atlas]
- [[concepts/gene-essentiality]] — exclusion of putatively essential genes and failure of simple gene-presence repertoire scores highlight context dependence and limits on inferring metal fitness from gene content. [src: metal_fitness_atlas]
- [[concepts/multi-omics-integration]] — ICA module responsiveness links gene-level metal fitness to module-level activity, while the proposed regulatory and expression-based models identify a multi-omic extension. [src: metal_fitness_atlas]
