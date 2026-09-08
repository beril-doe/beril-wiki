---
type: Summary
description: BERDL-wide analysis of SNIPE prevalence, ecology, and phage-defense trade-offs
doc_type: short
full_text: ../sources/snipe_defense_system__REPORT.md
title: SNIPE Defense System in the BERDL Pangenome
sources:
- id: snipe_defense_system
  resource: ../sources/snipe_defense_system__REPORT.md
  title: snipe defense system
---
# SNIPE Defense System in the BERDL Pangenome

## Overview

This report evaluates [snipe-defense-system](../entities/snipe-defense-system.md) across the BERDL pangenome, connecting its phage-defense mechanism to the metabolic cost of losing the ManYZ transporter, correcting the Pfam assignment of its nuclease domain, and surveying its prevalence, pangenome status, environmental association, and occurrence in phage-therapy targets. The analysis supports the hypothesis that SNIPE homologues are widespread, predominantly mobile, and associated with particular ecological contexts. [^snipe_defense_system]

## Key Findings

### Phage resistance without transporter loss

SNIPE constitutively localizes to the inner membrane and cleaves phage DNA as it passes through the ManYZ mannose-transporter pore, potentially providing phage resistance while retaining transporter function. By contrast, *manY* and *manZ* loss blocks or sharply reduces phage lambda growth but causes loss of mannose transport and partial glucose-transport defects; *manX* loss produces fitness defects specifically on D-mannose and D-glucosamine. Under phage pressure, *man* mutants sweep to >95% frequency, then decline when phages evolve alternative injection mechanisms. [^snipe_defense_system]

Direct RB-TnSeq (random barcode transposon sequencing) measurements from the Deutschbauer/Price Fitness Browser covered 168 *E. coli* K-12 experiments for each ManXYZ gene. The worst, average, and strongly deleterious fitness values were: *manX*, -3.93 worst, -0.249 average, 6 conditions below -1, and 4 below -2; *manY*, -3.82 worst, -0.171 average, 10 conditions below -1, and 4 below -2; and *manZ*, -4.14 worst, -0.082 average, 7 conditions below -1, and 4 below -2. [^snipe_defense_system]

The strongest defects occurred on D-glucosamine, where *manX*, *manY*, and *manZ* fitness values were -3.79, -2.79, and -3.63, respectively, and on D-mannose, where they were -2.75, -3.00, and -2.74. On D-trehalose, the values were -1.27, -1.49, and —, and on sodium chlorite they were -1.47, -1.32, and -1.08. Cofitness correlations were 0.851 for *manX*↔*manZ*, 0.705 for *manX*↔*manY*, and 0.725 for *manY*↔*manZ*, supporting their operation as a single operon. [^snipe_defense_system]

The Fitness Browser contradicts the UniProt “fructose-specific” annotation for ManX: on D-mannose, *manX*, *manY*, and *manZ* fitness values were -2.75, -3.00, and -2.74, while *fruA* was -0.06; on D-glucosamine they were -3.79, -2.79, and -3.63, while *fruA* was -1.02; and on D-fructose they were -0.22, +0.15, and -0.07, while *fruA* was -1.44. These measurements support mannose/glucosamine specificity rather than fructose transport. [^snipe_defense_system]

### Corrected SNIPE domain architecture

The report identifies PF13250 as the correct Pfam assignment for DUF4041, also called the SNIPE-associated domain and associated with InterPro IPR025280. It identifies PF13455, or Mug113, as the SNIPE nuclease family; PF13455 belongs to the GIY-YIG clan CL0418 but is distinct from canonical GIY-YIG PF01541. The *E. coli* SNIPE protein A0A0A1A5Z2 is 558 aa long, with PF13250 at positions 232–333 and PF13455 at positions 443–520. [^snipe_defense_system]

Among the surveyed BERDL annotations, zero gene clusters contained both DUF4041/PF13250 and canonical GIY-YIG PF01541. The analysis found 4,572 DUF4041-containing gene clusters, of which 54 carried the description “Meiotically up-regulated gene 113,” consistent with full-length SNIPE proteins containing the Mug113 nuclease annotation. The report therefore recommends searching PF13250, DUF4041, or T5orf172 together with PF13455 rather than using PF01541 as the SNIPE nuclease marker. [^snipe_defense_system]

### Pangenome prevalence and mobility

DUF4041/PF13250 occurred in 4,572 gene clusters across 1,696 species and 33 bacterial and archaeal phyla, substantially exceeding the >500 homologues reported in the original paper. The largest species counts were Pseudomonadota, 556 species; Actinomycetota, 334; Bacillota_A, 275; Bacillota, 206; Bacteroidota, 114; Nitrospirota, 45; Cyanobacteriota, 28; and Planctomycetota, 22. [^snipe_defense_system]

Of the 4,572 DUF4041-containing clusters, 13.3% were core, 30.7% were accessory, and 56.1% were singleton; the combined accessory-plus-singleton fraction was 86.7%. This distribution strongly supports the report’s interpretation that SNIPE is commonly gained or lost and is consistent with mobile defense-island carriage rather than stable core inheritance. [^snipe_defense_system]

The report estimates that 80.4% of DUF4041-containing clusters—3,675/4,572—were represented by the descriptions T5orf172 or DUF4041 and therefore formed a high-confidence SNIPE-family set. The remaining approximately 20%—897 clusters—included primary annotations such as histidine kinase, 319 clusters, and seryl-tRNA aminoacylation, 238 clusters, which may reflect secondary-domain detection or annotation noise. [^snipe_defense_system]

### Environmental association

Among species with AlphaEarth embeddings, SNIPE-bearing species numbered n=1,069 and non-SNIPE species n=13,977. Welch’s t-tests with Bonferroni correction found significant differences in 22 of 64 dimensions at p < 0.05; the largest effect was dimension A19, with Cohen’s d = 0.26 and p = 5.0e-14. Effect sizes ranged from |d| = 0.11–0.26, indicating a modest but consistent environmental shift rather than strict habitat segregation. [^snipe_defense_system]

AlphaEarth dimensions were derived from satellite remote-sensing imagery at sample collection latitude/longitude coordinates and can capture signals such as vegetation indices, temperature, precipitation, and land cover. The report does not assign a named biological interpretation to A19 or the other dimensions. AlphaEarth coverage was 28.4% of genomes and was biased toward environmental isolates with latitude/longitude metadata. [^snipe_defense_system]

### Fitness Browser and phage-host evidence

The Fitness Browser contained 48 organisms, 228K genes, 27M fitness scores, and 7,552 experiments. ManXYZ was present only in *E. coli* K-12 among those organisms, whereas one full two-domain SNIPE protein occurred in *Methanococcus maripaludis* JJ at locus MMJJ_RS01635. This protein carried PF13250, PF13455, and PF10544 and had 129 experiments of fitness data; its minimum fitness was -1.16 on formate/acetate and it was dispensable under most conditions. [^snipe_defense_system]

PF13455 occurred in 7 genes across 6 Fitness Browser organisms: *Azospirillum brasilense*, *Bacteroides thetaiotaomicron*, *Cupriavidus*, *Desulfovibrio vulgaris*, *Paraburkholderia kururiensis*, and *M. maripaludis*. Only *M. maripaludis* had the complete PF13250-plus-PF13455 architecture. [^snipe_defense_system]

The PhageFoundry strain-modelling database contained 188 *E. coli* strains, 96 phages, and 17,672 possible binary infection outcomes, of which 3,929 were positive and 13,743 negative. Its machine-learning model used 1,582 gene-cluster presence/absence features and achieved AUC = 0.883 and accuracy = 84.3%. The Lambdavirus phage 411_P1 infected 1 of 188 strains, or 0.5%; comparison infection rates were 43.4% for Myoviridae, 13.0% for Podoviridae, and 9.7% for Siphoviridae. [^snipe_defense_system]

The low Lambdavirus infection rate is consistent with widespread ManYZ variation or loss in the sampled *E. coli* strains. The report relates this observation to the PhageFoundry study’s conclusion that adsorption factors are primary predictors of phage-host interactions and to SNIPE’s proposed action at the adsorption/injection interface. [^snipe_defense_system]

### Klebsiella detection

PhageFoundry detected DUF4041 in *Klebsiella* but not in *Acinetobacter*, *P. aeruginosa*, or *P. viridiflava* in the four-species browser comparison. The corresponding counts were: *Klebsiella*, DUF4041 1, GIY-YIG 1, nuclease 98, restriction 42, and abortive infection 2; *Acinetobacter*, 0, 3, 91, 33, and 2; *P. aeruginosa*, 0, 2, 125, 54, and 2; and *P. viridiflava*, 0, 0, 90, 41, and 1. [^snipe_defense_system]

The three *Klebsiella* DUF4041 proteins—JJW41_17025, KFB13_RS08150, and KFB31_RS01490—were each 558 aa. The same genome browser contained 28 mannose PTS IID/ManZ proteins, 1 mannose PTS IIA/ManX protein, 4,619 PF02378 PTS_EIIC annotations, and 571 PF00358 PTS_EIIA_1 annotations. The co-occurrence is consistent with SNIPE defending a mannose-transporter phage-entry route, but no *Klebsiella* SNIPE or ManYZ fitness data were available. [^snipe_defense_system]

## Caveats and Unresolved Gaps

The report states that eggNOG Pfam annotations may miss divergent SNIPE homologues, and that only 54/4,572 DUF4041 clusters showed Mug113 co-annotation, suggesting that many SNIPE nuclease domains may go undetected. DUF4041 is strongly associated with SNIPE but may also occur in non-SNIPE proteins. [^snipe_defense_system]

The AlphaEarth analysis covered 28.4% of genomes and was skewed toward environmental isolates with geographic metadata, limiting generalization to the full pangenome. The planned comparison of COG V defense-gene density could not be completed through the REST API because it required Spark Connect for a 93M × 132M row join. [^snipe_defense_system]

NMDC metagenome ecosystem analysis was limited because only 2 samples matched the API query format; the report identifies interactive MCP-tool queries as a way to improve coverage. PhageFoundry provides genome annotations but no fitness/TnSeq tables for *Klebsiella*, so strain-specific mutant libraries or curated external *K. pneumoniae* Tn-Seq datasets would be needed to test SNIPE and ManYZ fitness directly. [^snipe_defense_system]

The report’s H1 assessment is supported across prevalence, accessory status, environmental association, and the proposed ManYZ trade-off, while H0 is rejected for taxonomic distribution and environmental niche association. However, the environmental result establishes statistical association rather than a specific causal habitat mechanism, and the archaeal Fitness Browser example does not establish the Enterobacterales phage-lambda mechanism in archaea. [^snipe_defense_system]

## Slots Into

- [phage-defense-syndromes-and-arms-race](../concepts/phage-defense-syndromes-and-arms-race.md) — SNIPE’s proposed DNA-cleavage mechanism, the ManYZ resistance-versus-metabolic-cost trade-off, phage-host interaction evidence, and the corrected PF13250/PF13455 architecture. [^snipe_defense_system]
- [pangenome-integration](../concepts/pangenome-integration.md) — the detection of 4,572 DUF4041 clusters across 1,696 species and 33 phyla, with 86.7% accessory or singleton status. [^snipe_defense_system]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — the AlphaEarth comparison showing significant differences in 22 of 64 dimensions, with explicit coverage and sampling-bias caveats. [^snipe_defense_system]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the 168-condition ManXYZ fitness measurements and the substrate-specific separation of mannose/glucosamine from fructose phenotypes. [^snipe_defense_system]

[^snipe_defense_system]: [snipe defense system](../sources/snipe_defense_system__REPORT.md)
