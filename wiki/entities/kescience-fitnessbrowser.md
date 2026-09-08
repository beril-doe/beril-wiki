---
type: Dataset
description: BERDL dataset of comparative microbial mutant-growth fitness measurements
sources:
- id: acinetobacter_adp1_explorer
  resource: ../summaries/acinetobacter_adp1_explorer__REPORT.md
  title: acinetobacter adp1 explorer
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: adp1_triple_essentiality
  resource: ../summaries/adp1_triple_essentiality__REPORT.md
  title: adp1 triple essentiality
- id: alphafold_msa_annotation
  resource: ../summaries/alphafold_msa_annotation__REPORT.md
  title: alphafold msa annotation
- id: amr_cofitness_networks
  resource: ../summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
- id: amr_fitness_cost
  resource: ../summaries/amr_fitness_cost__REPORT.md
  title: amr fitness cost
- id: amr_pangenome_atlas
  resource: ../summaries/amr_pangenome_atlas__REPORT.md
  title: amr pangenome atlas
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: aromatic_catabolism_network
  resource: ../summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: caulobacter_fur_lipida_loss
  resource: ../summaries/caulobacter_fur_lipida_loss__REPORT.md
  title: caulobacter fur lipida loss
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: conservation_fitness_synthesis
  resource: ../summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
- id: conservation_vs_fitness
  resource: ../summaries/conservation_vs_fitness__REPORT.md
  title: conservation vs fitness
- id: core_gene_tradeoffs
  resource: ../summaries/core_gene_tradeoffs__REPORT.md
  title: core gene tradeoffs
- id: costly_dispensable_genes
  resource: ../summaries/costly_dispensable_genes__REPORT.md
  title: costly dispensable genes
- id: counter_ion_effects
  resource: ../summaries/counter_ion_effects__REPORT.md
  title: counter ion effects
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: enigma_carbon_census_1
  resource: ../summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
- id: essential_genome
  resource: ../summaries/essential_genome__REPORT.md
  title: essential genome
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: field_vs_lab_fitness
  resource: ../summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: fitness_effects_conservation
  resource: ../summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: fitness_modules
  resource: ../summaries/fitness_modules__REPORT.md
  title: fitness modules
- id: functional_dark_matter
  resource: ../summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
- id: lab_field_ecology
  resource: ../summaries/lab_field_ecology__REPORT.md
  title: lab field ecology
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: metal_cross_resistance
  resource: ../summaries/metal_cross_resistance__REPORT.md
  title: metal cross resistance
- id: metal_fitness_atlas
  resource: ../summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
- id: module_conservation
  resource: ../summaries/module_conservation__REPORT.md
  title: module conservation
- id: paperblast_explorer
  resource: ../summaries/paperblast_explorer__REPORT.md
  title: paperblast explorer
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
- id: prophage_amr_comobilization
  resource: ../summaries/prophage_amr_comobilization__REPORT.md
  title: prophage amr comobilization
- id: snipe_defense_system
  resource: ../summaries/snipe_defense_system__REPORT.md
  title: snipe defense system
- id: truly_dark_genes
  resource: ../summaries/truly_dark_genes__REPORT.md
  title: truly dark genes
- id: webofmicrobes_explorer
  resource: ../summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
title: KBase Fitness Browser
---
# KBase Fitness Browser

## Identity

**Canonical name:** KBase Fitness Browser. [^acinetobacter_adp1_explorer]

**Known aliases:** Fitness Browser; `kescience_fitnessbrowser`; KEScience FitnessBrowser. [^acinetobacter_adp1_explorer][^berdl_data_atlas]

**Stable external identifier:** No stable external identifier was reported in the source documents. [^acinetobacter_adp1_explorer]

KBase Fitness Browser is a BERDL data collection for microbial mutant-growth fitness measurements. [^acinetobacter_adp1_explorer] The BERDL Data Atlas inventories 27,410,721 measurements, and the collection is represented in 35 of 66 audited BERIL projects (53%). [^berdl_data_atlas] Across 48 bacteria, Fitness Browser data contributed to analysis of 194,216 genes; 15 gene families were essential in every organism, 859/17,222 ortholog families (5.0%) were universally essential, 4,799 (27.9%) were variably essential, and 11,564 (67.1%) were never essential. [^discoveries] The same synthesis found 7,084 orphan essential genes, 58.7% hypothetical, and used module transfer to generate 1,382 function predictions for hypothetical essential genes across 48 organisms. [^discoveries]

The functional-dark-matter analysis **supports and extends** this scale: across 48 organisms it assessed 228,709 genes, including 57,011 dark genes (24.9%) lacking functional annotation; 7,787 had strong fitness effects (|fitness| ≥ 2 in at least one condition), and 9,557 were essential because no viable transposon mutants were recovered. [^functional_dark_matter] Thus 17,344 dark genes had experimentally measurable phenotypes, although the dark-gene fraction ranged from more than 35% to less than 15% and may primarily reflect annotation depth rather than biological differences. [^functional_dark_matter] Among dark genes, 39,532 (69.3%) had pangenome links, 12,686 were accessory, 511 were both accessory and strongly fitness-active, and 6,142 belonged to independent-component-analysis (ICA) fitness modules. [^functional_dark_matter]

The truly-dark-gene analysis **refines** this census: of 57,011 dark genes, 39,532 had pangenome links; Bakta v1.12.0 reclassified 33,105 (83.7%) as annotation-lag genes, while 6,427 remained hypothetical in both pipelines and were classified as truly dark. A further 17,479 dark genes lacked pangenome links and could not be assessed. [^truly_dark_genes] Truly dark genes were shorter, less conserved, more taxonomically restricted, and lower in GC content than annotation-lag genes: median length was 121 versus 194 amino acids, core-genome fraction 43.1% versus 72.7%, essential fraction 18.0% versus 13.4%, mean GC content 0.542 versus 0.584, ortholog presence 29.3% versus 63.7%, and median ortholog breadth 1 versus 4 organisms. [^truly_dark_genes] Reported effect sizes were d = −0.432, OR = 0.284, OR = 1.420, d = −0.395, OR = 0.236, and d = −1.072, respectively, with corresponding p-values < 1e-100, < 1e-100, < 1e-10, 2e-115, < 1e-100, and < 1e-100. [^truly_dark_genes]

This **supports** Fitness Browser as a source of experimentally informative unknown genes while **qualifying** direct interpretation of its dark-gene fraction: among truly dark genes, 79.4% had UniRef50 links and 84.7% had database cross-references, but only 4.0% had Pfam hits and 4.6% had KEGG KOs; eggNOG-mapper provided partial signal for 43.5% of truly dark clusters, and 55.4% of COG assignments were category S, function unknown. [^truly_dark_genes] Only 246 genes (3.8%) had no annotation clues; 3,867 (60.2%) had minimal sequence identifiers, 711 (11.1%) had partial functional evidence, and 1,603 (24.9%) had phenotype-only evidence. [^truly_dark_genes] The resulting 100-candidate ranking covered 19 organisms; 34 candidates were essential, 53 were in operons, and 30 were in ICA modules. [^truly_dark_genes]

The pan-bacterial essential-genome analysis **supports** this scale: 41,059 essential genes among 221,005 genes (18.6%) were analyzed across 48 bacteria, with essentiality rates ranging from 12.2% in Pedo557 to 29.7% in Magneto. [^essential_genome] Its 2,838,750 bidirectional-best-hit pairs yielded 17,222 ortholog groups, including 859 universally essential, 4,799 variably essential, and 11,564 never-essential families. [^essential_genome] Fifteen families were essential in all 48 organisms, including conserved ribosomal proteins, groEL, pyrG, fusA, valS, and SelGGPS; this stricter experimental intersection is narrower than the 859-family computationally defined universal set. [^essential_genome] Variable essentiality and 7,084 orphan essentials indicate strong genomic-context dependence, while module transfer supplied 1,382 indirect, family-backed predictions for hypothetical essential genes. [^essential_genome]

## Web of Microbes integration

The Web of Microbes (WoM) bridge **extends** Fitness Browser from mutant-growth phenotypes to exometabolite observations. In a 2018 WoM snapshot, two direct strain matches and two same-strain or genus-level matches were identified: *Pseudomonas* sp. FW300-N2E3 matched `pseudo3_N2E3` with 5,854 genes and 211 experiments; *Pseudomonas* sp. GW456-L13 matched `pseudo13_GW456_L13` with 5,243 genes and 106 experiments; *E. coli* BW25113 matched `Keio` as the same strain with 4,610 genes and 168 experiments; and *Synechococcus* PCC7002 matched `SynE` (PCC 7942) at genus level with 2,722 genes and 129 experiments. [^webofmicrobes_explorer] The two direct *Pseudomonas* matches are ENIGMA groundwater isolates with substantial Fitness Browser data, whereas the WoM *E. coli* record contains only 12 observations focused on sulfur metabolism in ZMMG medium despite the richer Keio collection. [^webofmicrobes_explorer]

For `pseudo3_N2E3`, curated matching found 19 WoM-produced metabolites also tested by Fitness Browser as carbon or nitrogen sources: alanine, arginine, glycine, lactate, proline, phenylalanine, tryptophan, valine, lysine, threonine, trehalose, adenine, adenosine, inosine, thymine, malate, nicotinamide, and carnitine. Five were de novo products (`E`) and 14 were amplified metabolites (`I`). [^webofmicrobes_explorer] This **supports and concretizes** the existing metabolic use of Fitness Browser: the bridge can ask which genes are fitness-important when an organism uses a metabolite that it produces, with de novo lactate production by FW300-N2E3 and Fitness Browser lactate-utilization phenotypes as a direct example. [^webofmicrobes_explorer]

WoM action semantics distinguish amplification from emergence: for the control, `D` means detected in the starting medium (742 observations) and `N` means not detected (1,023); for organisms, `I` means increased (1,338), `E` means emerged de novo (1,155), and `N` means no significant change (7,509). `E` and `I` were mutually exclusive across all 10,744 observations; all 742 `D` observations belonged exclusively to the control, and no organism had a decreased or consumption action in this snapshot. [^webofmicrobes_explorer] The absence of consumption measurements **qualifies** stronger Fitness Browser interpretations: produced-metabolite links do not show whether the same organism consumes the compound, and therefore cannot yet test whether consumed metabolites predict gene essentiality. [^webofmicrobes_explorer]

Among ENIGMA isolates grown in R2A, the fraction of changes representing de novo production, `E/(E+I)`, ranged from 15.2% to 32.4%; GW456-L13 had 49 increased and 34 emerged metabolites, with 32.4% novel, while FW507-14TSA had 44 increased and 33 emerged, with 31.4% novel. [^webofmicrobes_explorer] The proposed association between this metabolic-novelty phenotype and pangenome gene content remains a future hypothesis, not an established Fitness Browser relationship. [^webofmicrobes_explorer]

## SNIPE and ManXYZ integration

The SNIPE-defense analysis **refines** the collection’s comparative scope with a focused phage-resistance example. Fitness Browser contained 48 organisms, 228K genes, 27M fitness scores, and 7,552 experiments; [snipe-defense-system](snipe-defense-system.md) was represented by one complete two-domain protein in [methanococcus-maripaludis](methanococcus-maripaludis.md) JJ (locus MMJJ_RS01635), with 129 experiments, a minimum fitness of -1.16 on formate/acetate, and dispensibility under most conditions. [^snipe_defense_system] ManXYZ was present only in [escherichia-coli](escherichia-coli.md) K-12 among these organisms, so the archaeal SNIPE result does not establish the Enterobacterales phage-lambda mechanism. [^snipe_defense_system]

The E. coli RB-TnSeq measurements **support** condition-specific interpretation of transporter loss: across 168 experiments, *manX*, *manY*, and *manZ* had worst fitness values of -3.93, -3.82, and -4.14 and average values of -0.249, -0.171, and -0.082, respectively; the strongest defects were on D-glucosamine and D-mannose. [^snipe_defense_system] Cofitness correlations of 0.851 for *manX*↔*manZ*, 0.705 for *manX*↔*manY*, and 0.725 for *manY*↔*manZ* support their operation as one operon. [^snipe_defense_system] The measurements contradict the UniProt “fructose-specific” annotation for ManX and support mannose/glucosamine rather than fructose specificity. [^snipe_defense_system]

SNIPE is proposed to cleave phage DNA at the ManYZ transporter pore while retaining mannose transport, whereas *manY* or *manZ* loss blocks or sharply reduces lambda growth at a metabolic cost; this is a mechanistic hypothesis rather than a Fitness Browser measurement in *Klebsiella*. [^snipe_defense_system] The corrected architecture uses PF13250/DUF4041 with PF13455/Mug113, not canonical GIY-YIG PF01541; the surveyed collection found zero clusters containing both DUF4041/PF13250 and PF01541. [^snipe_defense_system] The source reports 4,572 DUF4041 clusters across 1,696 species and 33 phyla, with 13.3% core, 30.7% accessory, and 56.1% singleton clusters; 86.7% were accessory or singleton. [^snipe_defense_system] These data **support** using Fitness Browser alongside pangenome and phage-host resources to test mobile defense systems, while the lack of *Klebsiella* fitness data remains an explicit gap. [^snipe_defense_system]

## Literature and resource coverage

The [paperblast_explorer__REPORT](../summaries/paperblast_explorer__REPORT.md) analysis **extends** Fitness Browser’s comparative role by linking it to [kescience-paperblast](kescience-paperblast.md) through 129,823 VIMSS cross-references. [^paperblast_explorer] PaperBLAST contains 12.4 million rows across 14 tables, including 3,195,890 gene-to-paper links, 2,089,192 structural-site records, 1,951,949 text snippets, 1,358,798 GeneRIF summaries, 1,135,366 gene/protein records, 815,571 unique protein sequences, 599,587 curated gene-paper links, and 255,096 curated annotations. [^paperblast_explorer] Of 841K genes with text-mined paper links, 551K (65.6%) have exactly one paper; the median is 1 and the mean is 3.8 papers per gene. [^paperblast_explorer] Only 6% of genes (50K) account for 57.7% of gene-paper links, and organism- and gene-level Gini coefficients are 0.967 and 0.669. [^paperblast_explorer]

This **refines** interpretation of Fitness Browser-derived function predictions: a literature link is evidence of discoverability, not necessarily functional characterization. [^paperblast_explorer] *Homo sapiens* accounts for 46.7% of PaperBLAST gene-paper records; the top five organisms account for 72.8%, and the top 1,000 of 20,723 organisms capture 94.2%. [^paperblast_explorer] Among 15,312 bacterial organisms, the top 100 capture 44.3% of bacterial literature; the leaders are *Mycobacterium tuberculosis* H37Rv with 9,079 papers, *Escherichia coli* K-12 with 8,860, and *Pseudomonas aeruginosa* PAO1 with 5,928. [^paperblast_explorer] Environmental and non-pathogenic organisms are therefore underrepresented in literature-linked evidence surrounding comparative fitness resources. [^paperblast_explorer]

MMseqs2, a sequence-search and clustering method, reduced 815,571 PaperBLAST proteins to 628K clusters at 90% identity, 345K at 50%, and 215K at 30%. [^paperblast_explorer] At 50% identity, 31,653 families (9.2%) have zero papers, 159,046 (46.1%) exactly one paper, and 14,904 (4.3%) 20 or more papers; 5,218 multi-member families representing 14,534 sequences have no literature. [^paperblast_explorer] Family size is positively associated with coverage: 95.4% of multi-member clusters have at least one member with a paper, while 5,218 (4.6%) have none. [^paperblast_explorer] These dark families are dominated by REBASE methyltransferases and biolip structural entries, although missed text mining cannot be distinguished from genuinely unstudied proteins. [^paperblast_explorer]

The PaperBLAST bridge **supports and qualifies** provenance-aware interpretation: it mines PubMed Central full text, misses paywalled literature, has 35% of organisms classified as Unknown by heuristic domain mapping, includes approximately 19% of SwissProt, uses a conventional rather than biologically universal 50% sequence-identity boundary, and had no negative controls. [^paperblast_explorer]

## Comparative scope and evidence integration

The conservation–fitness synthesis covered approximately 194K genes across 43 bacteria and supplied laboratory-fitness data for 194,216 protein-coding genes. [^conservation_fitness_synthesis] Essential genes were 82% core, whereas always-neutral genes were 66% core. [^conservation_fitness_synthesis] A direct analysis linked 177,863 Fitness Browser genes to pangenome clusters, with 100.0% median protein identity and 94.2% median gene coverage; 44 of 48 organisms mapped and 33 were retained for essentiality analysis. [^conservation_vs_fitness] Among 27,693 putative essential genes, 86.1% were core versus 81.2% of non-essential genes; median odds ratio was 1.56, and 18 of 33 organisms showed significant enrichment at BH-FDR q < 0.05. [^conservation_vs_fitness] This supports a modest association between essentiality and conservation, not the claim that every conserved gene is essential.

The fitness-effects analysis **supports and refines** these results: across approximately 194,000 genes from 43 bacteria, essential genes with no viable mutants were 82% core (n=27,693), genes often sick in more than 10% of experiments were 78% core (n=15,989), mixed genes were 70% core (n=20,739), sometimes-sick genes were 72% core (n=25,201), always-neutral genes were 66% core (n=94,889), and sometimes-beneficial genes were 70% core (n=9,705). [^fitness_effects_conservation] Essential genes were 82.2% core, genes with min_fit < -3 were 77.7% core, and genes with min_fit from -1 to 0 were 66.4% core; fitness breadth had a weak association with core status (Spearman rho=0.086, p=8.1e-230). [^fitness_effects_conservation]

The discoveries log found universally essential genes were 91.7% core versus 80.7% for non-essential genes, while orphan essentials were 49.5% core. [^discoveries] The essential-genome analysis **supports** this context-dependent interpretation: universally essential genes were 91.7% core, variably essential genes 88.9% core, never-essential genes 81.7% core, and orphan essentials 49.5% core; essentiality penetrance and core fraction had only a weak positive correlation (rho=0.123, p=1.6e-17). [^essential_genome]

The module-conservation analysis **extends** comparison from genes to co-regulated ICA fitness modules. Across 1,116 modules in 32 organisms, module genes were 86.0% core versus 81.5% for all genes (OR=1.46, p=1.6e-87). [^module_conservation] Among 974 modules with at least 3 mapped genes, 577 (59%) were >90% core, 349 (36%) were 50–90% core, and 48 (5%) were <50% core; median module core fraction was 93.4%. [^module_conservation] This **refines** the gene-level result: conservation also characterizes most co-regulated units, but family breadth did not predict conservation (Spearman rho=-0.01, p=0.914). [^module_conservation]

The metal-fitness atlas **extends** conservation–fitness analysis to metal-important genes. Across 559 metal experiments across 31 organisms and 16 metals, it assembled 383,349 gene × metal fitness records; across 22 organisms and 14 metals, metal-important genes were 87.4% core versus 76.9% for baseline genes (OR=2.08, p=4.3e-162). [^metal_fitness_atlas] This **refines** the earlier condition-specific heavy-metal result of 71.2% core. [^metal_fitness_atlas] Essential-metal tolerance genes had a mean core-fraction delta of +0.148 versus +0.081 for toxic metals (Mann-Whitney U=39, p=0.015); manganese was +0.198, zinc +0.151, molybdenum +0.148, tungsten +0.145, and iron +0.116. [^metal_fitness_atlas]

The metal cross-resistance analysis **supports and qualifies** this result: across 452 metal experiments involving 37 organisms and 14 metals, 119,561 genes had metal-fitness data. [^metal_cross_resistance] Among 8,162 metal-important genes in 28 organisms, general-stress, metal-shared, and metal-specific tiers had mean pangenome core fractions of 92.0%, 91.0%, and 89.8%, respectively, with 57.2%, 50.4%, and 45.7% fully core at at least 95%. [^metal_cross_resistance] The three tiers included 318 metal-shared ortholog groups present in at least 2 organisms. [^metal_cross_resistance]

The prophage-AMR analysis **refines** expectations for mobile-resistance questions: it proposed comparing fitness costs for prophage-proximal and distal AMR genes, but Fitness Browser contains RB-TnSeq data for only 48 model organisms and has poor overlap with the GTDB pangenome species analyzed there, so the comparison could not be tested. [^prophage_amr_comobilization] Whether prophage-proximal AMR genes have distinct fitness costs remains open. [^prophage_amr_comobilization]

## Metabolic capability and dependency

Fitness Browser supports comparative metabolic analysis. Carbon-source RB-TnSeq measurements from 14 organisms covered 574 organism–carbon-source combinations; an integrated pipeline resolved 96 of 201 gapfilled enzymatic reaction–organism pairs (47.8%), compared with 51 pairs (25.4%) from Fitness Browser annotation matching alone. [^annotation_gap_discovery] Ortholog-transferred fitness data supplied 12,241 entries covering 2,005 genes and 13 conditions in an aromatic-catabolism analysis. [^aromatic_catabolism_network] [complex-i](complex-i.md) orthologs had mean fitness values of -1.35 on aromatic conditions versus -0.77 on comparison conditions, with Mann-Whitney p < 0.0001; because transfer mixes organisms with different respiratory-chain architectures, this is not definitive for [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md). [^aromatic_catabolism_network]

The functional-dark-matter analysis **extends** this metabolic use but cautions against direct gene-to-pathway interpretation. GapMind identified 1,256 organism–pathway pairs across 44 Fitness Browser-linked species in which nearly complete pathways co-occurred with strongly fitness-active dark genes; the most frequent gaps were fucose utilization in 32 organisms, rhamnose utilization in 31, sorbitol utilization in 30, myoinositol utilization in 28, gluconate utilization in 26, and asparagine biosynthesis in 24. [^functional_dark_matter] Domain matching produced 42,239 gene–pathway candidates across 3,186 dark genes, including 5,398 high-confidence EC-prefix matches, 4,687 medium-confidence Pfam-family matches, and 32,154 low-confidence keyword matches. [^functional_dark_matter] These are organism-level co-occurrences or computational hypotheses, not direct enzyme assignments.

The truly-dark-gene analysis **supports and sharpens** this caution: 6,427 genes remained hypothetical after Bakta reannotation, and 2,314 Tier 3 or Tier 4 genes had partial functional or phenotype evidence suitable for narrowing experimental hypotheses, but only 4.6% had KEGG KOs and only 4.0% had Pfam hits. [^truly_dark_genes] Truly dark genes showed accessory-genome and possible horizontal-transfer signatures: mean absolute GC deviation was 0.047 versus 0.038 for annotation-lag genes, strong GC deviation affected 9.2% versus 4.0%, and 12.0% were within 2 genes of a mobile genetic element. [^truly_dark_genes] These measurements support novelty or recent acquisition as hypotheses, but do not establish horizontal gene transfer or direct gene function. [^truly_dark_genes]

The metabolic capability/dependency analysis **supports and refines** this distinction. Across 1,695 complete pathway–organism pairs from 48 organisms, GapMind completeness was combined with Fitness Browser gene-fitness data and SEED subsystem annotations as a pathway-membership proxy. [^metabolic_capability_dependency] There were 267 latent capabilities (15.8%), 547 intermediate pairs (32.3%), and 881 active dependencies (51.9%); carbon-source utilization was latent in 217 of 892 pairs (24.3%), compared with 48 of 735 amino-acid-biosynthesis pairs (6.5%). [^metabolic_capability_dependency] Pathway-level conservation did not distinguish latent from active pathways (Mann–Whitney U p=0.94; rank-biserial r=0.052), while latent-capability rate correlated with pangenome openness (Spearman ρ=0.69, p=0.0004, n=22 clades). [^metabolic_capability_dependency]

The pathway-capability analysis **refines** this classification using 161 organism–pathway combinations across 7 model bacteria and 23 GapMind pathways: 57 (35.4%) were Active Dependency, 66 (41.0%) Latent Capability, 24 (14.9%) Incomplete but Important, and 14 (8.7%) Missing. [^pathway_capability_dependency] All 66 aggregate Latent Capability pairs became fitness-important under at least one condition type, especially nitrogen limitation, stress, or carbon limitation; however, the condition-specific median importance threshold can cause reclassification by construction. [^pathway_capability_dependency] Active Dependencies had mean core gene completeness of 0.986 versus 0.975 for Latent Capabilities. [^pathway_capability_dependency]

The same analysis **supports and extends** the pangenome link: across 2,810 GTDB species with at least 10 genomes, variable pathway count correlated with pangenome openness at raw Spearman rho=0.327, p=7.2e-71, and partial rho=0.530, p=2.83e-203 after controlling for genome count. [^pathway_capability_dependency] The signal was positive in 13 of 18 genera and significant in 5 of 18; metabolic ecotype count among 225 species correlated with openness at raw rho=0.262, p=6.8e-05 and partial rho=0.322, p=8.0e-07. [^pathway_capability_dependency] Accessory-dependent completeness was largest for leucine and valine biosynthesis, each with all-gene completeness 0.614, core-only completeness 0.468, and gap 0.146; gaps were 0.141 for arginine, 0.140 for lysine, and 0.140 for threonine. [^pathway_capability_dependency] These results suggest a basis for community-level sharing, but do not demonstrate metabolite exchange. [^pathway_capability_dependency]

The FW300-N2E3 integration **supports and extends** this role by joining Fitness Browser with Web of Microbes exometabolomics, BacDive utilization phenotypes, and GapMind predictions. Among 21 matched metabolites, comparisons were concordant for 21/21 (100%); across 41 individual metabolite-database comparisons, 37 were concordant (90.2%), with 17/21 (81%) fully concordant and mean concordance 0.94. [^fw300_metabolic_consistency] For FW300-N2E3, 601 genes produced 4,764 significant gene-condition hits across 21 metabolites using |fit| > 1 and |t| > 4. [^fw300_metabolic_consistency] The 13 metabolites mapped to GapMind all had complete predictions and all showed growth in Fitness Browser, a 13/13 agreement. [^fw300_metabolic_consistency]

The WoM report **refines** this bridge’s annotation and coverage limits. Of 257 identified, non-unknown WoM compounds, 69 (26.8%) had definitive ModelSEED links through exact name matching; 107 (41.6%) had formula-only matches, yielding 176 compounds with any link (68.5%) and 81 unmatched (31.5%). [^webofmicrobes_explorer] The 107 formula-only compounds expanded to 900 ModelSEED molecules, an average of 8.4 molecules per WoM compound; formula-only matches are therefore candidate sets for manual curation rather than definitive compound identities. [^webofmicrobes_explorer] WoM-to-GapMind integration was blocked by internal pathway identifiers rather than simple metabolite names, so a pathway-to-substrate/product lookup table is required. [^webofmicrobes_explorer]

## Condition dependence and ENIGMA growth integration

The genotype-to-phenotype study **supports and extends** Fitness Browser’s condition-specific role by aligning 486 strain × condition anchor pairs covering 7 strains and 72 conditions; 275 pairs (56.6%) showed measurable growth. [^genotype_to_phenotype_enigma] Five conditions—cytidine, glycine, inosine, thymidine, and uridine—occurred in all four aligned datasets. [^genotype_to_phenotype_enigma] The combined corpus contained 46,389 genome × condition pairs across 727 genomes and 363 conditions with 4,293 shared [kegg](kegg.md) orthologs. [^genotype_to_phenotype_enigma]

This study **refines** Fitness Browser as a predictor: leave-one-strain-out binary-growth AUC was 0.633, while genus-blocked full-corpus LightGBM modeling, a gradient-boosting method, achieved AUC 0.620. [^genotype_to_phenotype_enigma] KO × condition interactions increased mean AUC from 0.620 to 0.653, with improvement in 80 of 106 held-out genera; 95 of 343 individually testable conditions achieved AUC > 0.75. [^genotype_to_phenotype_enigma] Performance was stronger for amino acids (AUC 0.775 across 7,765 pairs) and nucleosides (0.780 across 829 pairs) than metals (0.605 across 232 pairs), antibiotics (0.619 across 238 pairs), or nitrogen (0.435 across 152 pairs). [^genotype_to_phenotype_enigma]

The truly-dark-gene analysis **contradicts** a simple stress-enrichment interpretation of unknown-gene phenotypes. For genes with strong fitness phenotypes, stress conditions were reported at 28.7% versus 43.2% for annotation-lag genes (OR = 0.53, p < 0.001); the results section separately reported stress at 43.3% versus 54.7%, carbon-source conditions at 13.7% versus 21.7%, and motility at 1.2% versus 3.2%. [^truly_dark_genes] It reported enrichment in mixed-community conditions (7.5% versus 0%), iron conditions (0.7% versus 0%), nutrient time-series conditions, and rich media. [^truly_dark_genes] These results suggest, but do not establish, novel metabolic or community-interaction functions. [^truly_dark_genes]

The Oak Ridge comparison **supports** condition-specific interpretation but **contradicts** simple aggregate-tolerance extrapolation: among 12 Fitness Browser genera, laboratory metal-tolerance score versus high-uranium/low-uranium field abundance ratio was positive but not significant (Spearman rho=0.503, p=0.095, n=12). [^lab_field_ecology] GapMind achieved AUC 0.646, 78.8% accuracy, and 24.3% coverage on 118 testable pairs, while matched-condition Carbon Source Phenotypes transfer achieved AUC 0.800 and 76.8% accuracy at 23% coverage; internal five-fold validation achieved AUC 0.858. [^genotype_to_phenotype_enigma] Approximately 76% of ENIGMA conditions lacked GapMind or Carbon Source Phenotypes coverage, and genus-blocked prediction of µmax, lag, and max_A had negative R². [^genotype_to_phenotype_enigma]

## Modules, cofitness, and metal conditions

Robust ICA and DBSCAN, density-based spatial clustering of applications with noise, produced 17–52 fitness modules per organism across 32 bacteria; 94.2% had significantly elevated within-module cofitness, with mean |r|=0.34 versus background 0.12 and mean genomic-adjacency enrichment of 22.7×. [^discoveries] The stricter module analysis **supports and refines** this architecture: 1,116 stable modules across 32 organisms, each with at least 100 experiments, showed 94.2% elevated within-module cofitness, 2.8× correlation enrichment, and 22.7× genomic-adjacency enrichment. [^fitness_modules] Cross-organism alignment found 156 module families spanning at least 2 organisms, including 28 spanning 5+ organisms and one spanning 21 of 32 organisms; 145 had consensus functional labels. [^discoveries][^fitness_modules]

The truly-dark-gene analysis **supports** module and neighborhood inference for unannotated genes: among 4,394 truly dark genes in organisms with ICA data, 41% of neighboring genes were also hypothetical, 25.9% showed operon-like cofitness with adjacent genes using |r| ≥ 0.3, and 594 belonged to ICA modules. [^truly_dark_genes] Guilt-by-association linked these modules to candidate functions including phage integrases, metal transporters, chemotaxis systems, and iron regulation. [^truly_dark_genes] A ranked set of 100 candidates used fitness importance, annotation clues, ortholog breadth, genomic context, and experimental tractability; PV4/5210953 scored 10 with |f| = 5.5 and an operon association with TatC, while ANA3/7026383 scored 9 with a nitrogen-source phenotype of |f| = 8.6 and an ABC-transporter association. [^truly_dark_genes]

The module-conservation analysis **supports** this architecture while qualifying its genomic interpretation: among 974 modules with at least 3 mapped genes, 577 (59%) were core, 349 (36%) mixed, and 48 (5%) accessory, with median core fraction 93.4%. [^module_conservation] Module genes were 86.0% core versus 81.5% for all genes (OR=1.46, p=1.6e-87), but family breadth was unrelated to conservation (rho=-0.01, p=0.914). [^module_conservation] Zero essential genes appeared in ICA modules because essential genes lack usable transposon-insertion fitness variation. [^module_conservation]

The metal analysis **supports** condition-linked network architecture: across 317 organism–metal observations involving 28 organisms and 85 unique metal pairs, 98.1% of gene-level fitness correlations were positive (311/317), 99.1% were significant (p < 0.05), and all 15 pairs tested in at least 5 organisms showed greater than 90% sign consistency. [^metal_cross_resistance] No pair showed systematically negative cross-resistance. [^metal_cross_resistance] Strongest listed associations included Fe-Zn (mean r = 0.61, n = 6), Co-Ni (r = 0.56, n = 28), Co-Zn (r = 0.52, n = 18), Ni-Zn (r = 0.51, n = 18), Cu-Zn (r = 0.48, n = 16), Cu-Fe and Co-Fe (r = 0.45, n = 7 each), Al-Zn (r = 0.44, n = 13), Co-Cu and Cu-Ni (r = 0.43, n = 24 each); Al was most independent at mean r = 0.34, while Al-Ni and Al-Co were weakest at r = 0.34 and r = 0.30. [^metal_cross_resistance]

This **refines** cofitness as a universal but condition-modulated signal: cross-resistance had a universal positive directional layer and chemistry-specific magnitude layer, with leave-one-out consensus prediction r = 0.41 and Mantel mean r = 0.23. [^metal_cross_resistance] Non-metal stress controls are needed to distinguish general stress from universal metal cross-resistance. [^metal_cross_resistance]

The metal-fitness atlas **extends** pairwise correlations to module activity: per-organism z-scoring identified 600 metal-responsive module records among 19,453 module × metal records (3.1%); 183 responsive modules with conservation data had mean core fraction 0.826 and median 0.929. [^metal_fitness_atlas] An initial raw-score analysis found zero responsive modules because raw scores had a maximum of 0.96 and were not comparable with z-scores; per-experiment z-normalization resolved the discrepancy. [^metal_fitness_atlas]

The functional-dark-matter analysis **supports** module-based prioritization: 6,142 dark genes belonged to ICA modules, and 85/100 top-ranked phenotype-bearing dark genes had module-based predictions. [^functional_dark_matter] Cross-species synteny conserved 17,058 of 21,011 dark-gene–operon-partner pairs in at least one other organism and 10,150 in at least 3 organisms; cofitness found 2,899 of 32,075 non-essential operon pairs with evidence, including 998 double-validated by conserved synteny and strong cofitness. [^functional_dark_matter]

Ortholog transfer achieved 95.8% precision and 91.2% coverage for gene-level KO prediction, whereas Module-ICA had <1% KO-level precision but captured process-level co-regulation. [^discoveries] The held-out benchmark **refines** this distinction: ortholog transfer achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1; domain-based prediction achieved 29.1% precision, 66.6% coverage, and 0.401 F1; Module-ICA achieved <1% strict precision and 23.3% coverage; and cofitness voting achieved <1% strict precision and 73.0% coverage. [^fitness_modules]

## Essentiality and experimental prioritization

RB-TnSeq yields no viable knockout fitness profiles for essential genes. [^functional_dark_matter] Of 9,557 essential dark genes, the recommended strategy is CRISPRi, CRISPR interference for transcriptional knockdown, including Mobile-CRISPRi for less-established organisms, followed by growth measurements under standard and stress conditions. [^functional_dark_matter] Among all dark genes, 30,190 (52.9%) shared a predicted operon with an annotated gene and 97.2% had an annotated neighbor within a five-gene window, although the latter rate is expected given the 75% genome-wide annotation rate. [^functional_dark_matter]

The truly-dark-gene analysis **supports and extends** this prioritization: 18.0% of truly dark genes were essential versus 13.4% of annotation-lag genes, and 34 of the top 100 candidates were essential. [^truly_dark_genes] The report ranked all 6,427 truly dark genes on a maximum scale of 12; top candidates scored 8–10 across 19 organisms. [^truly_dark_genes] Methanococcus_S2 contributed 29 candidates, DvH 13, Methanococcus_JJ 13, and MR-1 8. [^truly_dark_genes] Proposed work includes AlphaFold2 or ESMFold structure prediction followed by Foldseek, growth assays under predicted conditions, Mobile-CRISPRi, characterization of contiguous dark islands, and extension of pangenome linkage to the 17,479 unlinked genes. [^truly_dark_genes]

The highest-ranked essential candidates were *Escherichia coli* Keio 14796 with score 0.875 and a YbeY domain, MR-1 200382 with score 0.874 and RimP_N/DUF150_C domains, and *Klebsiella oxytoca* BWI76_RS08540 with score 0.865 and OmpA/TIGR02802 domains. [^functional_dark_matter] The essential-genome analysis found 8,297 hypothetical essential genes, of which 3,912 had orthologs and received module-based predictions while 4,385 orphan targets did not; universally essential families were mostly strict single-copy families, with 839 of 859 having copy ratio <=1.5 and no non-essential paralogs. [^essential_genome]

A six-axis score combining fitness importance, cross-organism conservation, inference quality, pangenome distribution, biogeographic signal, and experimental tractability ranked 17,344 phenotype-bearing dark genes. [^functional_dark_matter] The top 100 spanned 22 organisms; Shewanella MR-1 contributed 25, *P. putida* N2C3 18, and Marinobacter 9. [^functional_dark_matter] A greedy set-cover analysis found that 10 organism–condition experiments would address 242 of the top 500 dark genes (45.3%); the first three MR-1 experiments—stress, nitrogen source, and carbon source—would address 111 candidates (20.8%). [^functional_dark_matter]

The metal-fitness atlas **refines** the essentiality warning: its broad definition identified 12,838 genes (3.3%) across 24 organisms, including 5,667 strict metal-important genes (1.5%), while putatively essential genes—approximately 14.3% of protein-coding genes and approximately 82% core—lack transposon insertions. [^metal_fitness_atlas] Their exclusion makes the observed 87.4% core enrichment conservative; the simple gene-presence repertoire score failed to predict metal fitness, supporting regulatory or expression-based modeling. [^metal_fitness_atlas] The 149 conserved novel candidates—89 truly unknown, 43 DUF/UPF, and 17 with partial functional hints—require annotation using PaperBLAST, InterPro, or structural prediction. [^metal_fitness_atlas]

## Environmental and cross-tenant validation

The ENIGMA Carbon Census **supports and extends** this cross-tenant role by using Fitness Browser with PubChem, KEGG, ModelSEED, ENIGMA genome-depot, GTDB, SSO, NMDC, and Planet Microbe. [^enigma_carbon_census_1] Across 83 enrichment compounds, all 83 were structure-resolved, 54 were KEGG-linked, and 9 were callable under the project definition; lauric acid was callable only from a Tier-1 measured RB-TnSeq carbon-source experiment and had no ENIGMA-isolate utilizer rows. [^enigma_carbon_census_1] The effective carbon-callable set was 8 rather than 9 after xanthine reaction R02107 was recognized as purine nitrogen acquisition rather than carbon catabolism; 74/83 compounds (89%) were organism-dark. [^enigma_carbon_census_1]

The Oak Ridge comparison **extends** validation from database joins to field ecology: Fitness Browser measurements were compared with [enigma-coral](enigma-coral.md) groundwater community composition and geochemistry across 108 [oak-ridge-field-research-center](oak-ridge-field-research-center.md) sites using [16s-amplicon-sequencing](16s-amplicon-sequencing.md). [^lab_field_ecology] Of 26 Fitness Browser genera, 14 were detected in the field; *Sphingomonas* occurred at 93% of sites, *Pseudomonas* at 91%, and *Caulobacter* at 82%. [^lab_field_ecology] Five genera showed FDR-significant uranium associations in both directions, indicating that field ecology integrates processes beyond laboratory metal tolerance. [^lab_field_ecology]

The metal studies **refine and qualify** validation: multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8), whereas the Metal Fitness Atlas found broad but genome-size-sensitive pangenome signatures. [^metal_cross_resistance][^metal_fitness_atlas] After genome-size normalization, *Leptospirillum* ranked at the 91st percentile, *Acidithiobacillus* at the 77th, *Marinobacter* at the 75th, and *Sulfobacillus* at the 71st; bioleaching genera were not significantly enriched (Mann-Whitney p=0.17). [^metal_fitness_atlas] Without normalization, large open pangenomes, including *K. pneumoniae* and *P. aeruginosa*, dominated scores. [^metal_fitness_atlas]

After excluding 2 organisms without tier data and collapsing multiple strains from the same species, the BacDive comparison had 20 independent species; the report also reports n = 26 at Fitness Browser organism scale. [^metal_cross_resistance] Genus-plus-species substring matching was imprecise for genus-only organisms such as Acidovorax sp. [^metal_cross_resistance] The Metal Fitness Atlas covered only 22 of 31 metal-tested organisms in its primary conservation analysis, and nine lacked Fitness Browser pangenome links. [^metal_fitness_atlas]

## ADP1, deletion, and TnSeq comparisons

The ADP1 Data Explorer tested connectivity between its user-provided database and [kescience-fitnessbrowser](kescience-fitnessbrowser.md). [^acinetobacter_adp1_explorer] An organism query returned 1 result for the ADP1 database against Fitness Browser, with 0 matches; [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) was absent from the collection. [^acinetobacter_adp1_explorer] Its mutant-growth measurements across 8 carbon sources therefore provide a complementary resource.

The ADP1 database recorded a mean pairwise correlation of 0.44 among mutant-growth profiles across 8 carbon sources; urea fitness was nearly uncorrelated with quinate fitness (r = 0.11), while butanediol-acetate and butanediol-lactate showed the strongest correlations (r = 0.58 and r = 0.53). [^acinetobacter_adp1_explorer] Its complete deletion matrix measured 2,034 genes across the same 8 carbon sources and identified 625 genes with condition-specificity score ≥ 1.0. [^adp1_deletion_phenotypes] The highest pairwise correlation was r = 0.58 and the median across 28 condition pairs was r = 0.25; a 24-gene quinate-specific module was the main discrete exception. [^adp1_deletion_phenotypes]

The triple-essentiality analysis supports treating ADP1 measurements as complementary rather than interchangeable with complete-gene knockout data: continuous fitness predicted knockout essentiality with AUC = 0.700 in rich media and AUC = 0.725 in minimal media, while RB-TnSeq and knockout essentiality disagreed at the 0.05 threshold (Cohen’s kappa -0.081 across 1,933 genes). [^adp1_triple_essentiality] The ADP1 matrix excludes 499 essential genes plus 316 genes with incomplete data, and Fitness Browser fitness should not be equated directly with lethality. [^adp1_deletion_phenotypes][^adp1_triple_essentiality]

## Limitations and operational safeguards

Fitness Browser essentiality is an upper bound because missing transposon insertions can reflect small size, AT-rich sequence, or scaffold-edge effects; RB-TnSeq measures essentiality under particular library-construction conditions, typically rich media, and can miss stress-specific requirements. [^essential_genome] Conservative BBH orthology can miss paralogs, gene fusions, and distant homologs. [^essential_genome] ICA membership depends on a |Pearson r| >= 0.3 threshold and a maximum of 50 genes per module; the >90% core and <50% core boundaries are convenient rather than biologically motivated; and the pangenome-linked module analysis covered 29/32 organisms because Cola, Kang, and SB2B lacked GTDB links. [^module_conservation]

The truly-dark-gene analysis **refines** these limitations: the pangenome linkage gap prevents assessment of 17,479 dark genes, or 31%; Bakta may produce false-negative functional calls; BBH ortholog coverage includes only 32 of 48 organisms; short genes are harder both to annotate and to measure by transposon insertion; and strong fitness phenotypes can reflect polar effects on downstream genes. [^truly_dark_genes] GC deviation is an imperfect HGT proxy because gene-specific composition bias and amelioration can also produce deviation. [^truly_dark_genes] The estimate that approximately 2,841 unlinked dark genes may be truly dark at the 16.3% linked-gene rate, including 2,208 with strong fitness phenotypes, is an extrapolation rather than a directly measured count. [^truly_dark_genes]

The metabolic capability/dependency study **refines** these limitations: Fitness Browser data represented only 48 organisms among 293,000 genomes with pathway predictions; laboratory media may make environmentally important pathways appear latent; the intermediate class comprised 32.3% of complete pairs; pathway-level conservation can miss partial gene loss; and an organism-to-clade linkage returned zero matches because a taxonomy column contained boolean strings rather than numeric taxids. [^metabolic_capability_dependency] The pathway-capability analysis limited its direct capability–fitness comparison to 7 of 48 organisms with matching GapMind genome data, and its 80-pathway survey excluded cofactor biosynthesis, lipid metabolism, and secondary metabolism. [^pathway_capability_dependency] Its condition-specific median threshold is circular for reclassification, and full phylogenetic independent contrasts were not computed; the related ecotype_analysis project found that phylogeny dominates gene content in 60.5% of species. [^pathway_capability_dependency] The proposed AlphaEarth niche-breadth analysis was not executed because embeddings covered 83K/293K genomes, or 28%. [^pathway_capability_dependency]

Environment-linked metabolic clusters were observational and lacked explicit phylogenetic correction; significant cluster–isolation-environment associations occurred in *Salmonella enterica* (χ²=1570.2, df=25, p<0.0001) and *Phenylobacterium* sp. (χ²=12.2, df=1, p=0.0005), but not in four marine organisms. [^metabolic_capability_dependency]

The FW300-N2E3 analysis **refines** metabolic comparisons: only 21/58 Web of Microbes metabolites were testable against another database, BacDive coverage ranged from 1 to 51 strains, species-level *Pseudomonas fluorescens* consensus may not represent FW300-N2E3, and the four-way comparison included only 3 metabolites. [^fw300_metabolic_consistency] Seven of 31 mapped Fitness Browser conditions had no FW300-N2E3 data, and two matches were approximate base-to-nucleoside mappings. [^fw300_metabolic_consistency] Tryptophan was 0+/50- with high confidence, trehalose 1+/5- with moderate confidence, lysine 0+/3- with moderate confidence, and glycine 0+/1- with low confidence; the source also reports n=52 for tryptophan in its literature-context discussion, versus n=50 in the primary result. [^fw300_metabolic_consistency] The planned NB04 pathway-level analysis was deferred, so the tryptophan pattern remains a hypothesis about overflow, cross-feeding, or signaling rather than proof that the isolate cannot grow on tryptophan. [^fw300_metabolic_consistency]

The metal atlas adds comparability limits: metal concentrations were not normalized by dose or tolerance threshold, organisms contributed 3 to 112 metal experiments, rare-metal patterns largely reflected DvH and psRCH2 biology, and multiple *Pseudomonas fluorescens* strains can inflate apparent conservation. [^metal_fitness_atlas] Excluding four duplicate FW300 strains left core enrichment robust (OR=2.065, p=5.9e-141, versus OR=2.083, p=4.3e-162 with all organisms), but PGLS, phylogenetic generalized least squares, remains needed. [^metal_fitness_atlas]

The ENIGMA integration adds limitations: normalized-name alignment produced 42 molecular matches, although ChEBI-ID canonicalization could expand this to 60–80; only 35.7% of 27,632 growth curves were fit-ok, with approximately 9% failing for technical reasons; and approximately 76% of ENIGMA conditions lacked GapMind or Carbon Source Phenotypes coverage. [^genotype_to_phenotype_enigma] Continuous-rate prediction lacked GC%, codon-usage bias, and Morgan fingerprints because GC% was available for only 32 of 727 genomes, nucleotide sequences were inaccessible from JupyterHub, and RDKit was required for Morgan fingerprints. [^genotype_to_phenotype_enigma] The active-learning proposal requires retrospective comparison with random selection and wet-lab execution of the 50-condition proposal. [^genotype_to_phenotype_enigma]

The collection is taxonomically uneven: 37/48 organisms are Pseudomonadota, and the top 500 dark-gene candidates included 417 Gammaproteobacteria, 71 Alphaproteobacteria, 17 Deltaproteobacteria, 12 Bacteroidetes, 10 Betaproteobacteria, 5 Firmicutes, 2 Cyanobacteria, and 0 Archaea, Actinobacteria, or Epsilonproteobacteria. [^functional_dark_matter] Environmental metadata are sparse: AlphaEarth embeddings cover only 28% of genomes (83K/293K), NCBI isolation-source metadata are inconsistent, NMDC validation is genus-level, and only 5 of 6 carrier genera were matched. [^functional_dark_matter] NMDC trait correlations are vulnerable to compositional coupling, a full sample-label permutation test remains future work, and the 29/47 lab–field concordance rate has a one-sided binomial p = 0.072. [^functional_dark_matter]

The WoM integration **supports and qualifies** these coverage warnings: its 2018 snapshot contained 37 organisms across 5 ENIGMA-funded projects and 589 metabolites, of which 332 (56.4%) were unidentified with an `Unk_` prefix; it was a single-laboratory, small-organism resource, and its current state may differ from the archived export. [^webofmicrobes_explorer] No organism consumption action appeared in the snapshot, and the report suggests that newer GNPS2 or Northen laboratory datasets may contain richer consumption data. [^webofmicrobes_explorer] Genus-level pangenome representation was available for all WoM organism genera, but species-level matching required strain-to-genome mapping that was not attempted. [^webofmicrobes_explorer]

The SNIPE analysis **reinforces and qualifies** coverage warnings: the complete architecture occurred in only one Fitness Browser organism, PF13455 occurred in 7 genes across 6 organisms, and no *Klebsiella* SNIPE or ManYZ fitness data were available. [^snipe_defense_system] The PaperBLAST analysis further qualifies them: text mining is not equivalent to functional characterization; 65.6% of genes have exactly one text-mined paper; PMC-only mining misses paywalled articles; heuristic domain assignment leaves 35% of organisms Unknown; SwissProt coverage is partial; 50% sequence identity is an arbitrary family threshold; and the analysis had no negative controls. [^paperblast_explorer]

The pitfalls report **refines** operational interpretation. Fitness Browser has approximately 27M rows, and its fields are strings, so `fit` and `t` must be explicitly cast before comparison, ordering, arithmetic, or aggregation. [^pitfalls] Exact case is required for `orgId`, analyses should filter by organism because `genefitness` has approximately 27M rows, and KO mapping is a two-hop join through `besthitkegg` and then `keggmember`; `kgroupdesc` uses `desc` and experiment grouping uses `expGroup`. [^pitfalls] Essential genes are absent from transposon fitness records: genefitness-only analyses miss approximately 14.3% of protein-coding genes, and genes absent from genefitness provide only an upper bound on essentiality. [^pitfalls]

BERDL is migrating from Delta to Iceberg, so live catalog discovery should prefer `catalog.namespace.table` dotted addresses when available and fall back to underscore-form addresses only when necessary. [^pitfalls] The `data_lakehouse_ingest` name is a MinIO governance-group name rather than a database prefix; the `kbase_ke_pangenome` database is under tenant `kbase` with dataset `ke_pangenome`, not tenant `kbase_ke`. [^pitfalls] Direct Spark SQL is preferred for complex or large queries because REST requests can return 504, 524, 503, or empty responses, while REST `/count` loops and `/schema` requests frequently time out on large tables. [^pitfalls]

Large Fitness Browser and linked pangenome analyses should remain in Spark until the final small output: billion-row pangenome tables require key filters before joins, a 1 GB serialized driver cap makes large `.toPandas()` collections unsafe, and disabling automatic broadcast joins can harm performance. [^pitfalls] Spark `DECIMAL` values arrive in pandas as `decimal.Decimal`; SQL `CAST(... AS DOUBLE)` or post-collection `.astype(float)` prevents mixed-type arithmetic failures. [^pitfalls] Temporary Spark Connect views can disappear after reconnects, so they should be re-registered immediately before use. [^pitfalls]

Fitness Browser comparisons require explicit design validation. [^pitfalls] In the cited IBD analysis, clustering taxa and testing those same taxa caused selection-on-outcome leakage: a 33-species Tier-A list had held-out-species Jaccard values of 0.230 for E1 and 0.064 for E3, while independent within-substudy evidence reduced the list to 3 candidates. [^pitfalls] Held-out-feature clustering, leave-one-feature-out refitting, or clustering on an independent pathway or EC matrix is preferable; the 0.5 and 0.3 Jaccard boundaries are project-specific safeguards, not universal guarantees. [^pitfalls]

Additional safeguards apply when linking Fitness Browser to external resources. [^pitfalls] Short ENIGMA strain names are not globally unique: ENIGMA MT20 was *Rhodanobacter glycinis*, whereas GTDB MT20 was *Streptococcus pneumoniae*; the erroneous match involved 8,434 genomes, including 1,751 clinical genomes, and 12 of 32 pangenome linkages through `ncbi_strain_identifiers` were incorrect genus matches. [^pitfalls] Assembly accessions such as `GCF_*` should be preferred when possible. [^pitfalls] MetaPhlAn3 cross-cohort analysis requires an NCBI-taxid-backed, GTDB-version-aware synonymy layer rather than simple string normalization; failure to reconcile names produced log₂FC approximately 28, equivalent to approximately 2.68 × 10⁸ fold, in the cited CrohnsPhage mart. [^pitfalls]

The Fitness Browser collection should not be treated as a complete environmental or taxonomic census. AlphaEarth embeddings cover 83,227 of 293,059 genomes, or 28.4%; a separate quality check found 3,838 of 83,287 genomes, or 4.6%, with at least one NaN among 64 dimensions, leaving 79,449 after filtering. [^pitfalls] Per-genome NCBI environment classification yielded 52.7% unknown labels, or 94,957 of 180,025 genomes, whereas species-level majority voting reached 91% coverage. [^pitfalls] The pooled geographic distance–embedding distance curve had a 2.0x near-versus-far ratio, compared with 3.4x for environmental samples and 2.0x for human-associated samples; human-associated samples can therefore dilute environmental geographic signals. [^pitfalls]

Live BERDL catalogs should be discovered with `get_databases()`, `get_tables()`, and `get_table_schema()`, rather than historical inventories. [^discoveries] Large joins touching the 2.5B-row UniProt identifier table should disable broadcast joins with `SET spark.sql.autoBroadcastJoinThreshold = -1`; nbconvert workflows should cache large Spark outputs as CSV because direct `toPandas()` calls can cause DeadKernelError. [^discoveries] The pitfalls report **qualifies** this historical guidance: automatic broadcast disabling can itself harm performance, so optimizer behavior should generally be trusted and explicit hints used only when needed. [^pitfalls]

## Related Pages

- [webofmicrobes_explorer__REPORT](../summaries/webofmicrobes_explorer__REPORT.md) — Web of Microbes action semantics, Fitness Browser strain overlap, metabolite-to-fitness links, ModelSEED matching, and pangenome integration.
- [truly_dark_genes__REPORT](../summaries/truly_dark_genes__REPORT.md) — persistent hypothetical genes after Bakta reannotation, annotation clues, fitness modules, and experimental prioritization.
- [snipe_defense_system__REPORT](../summaries/snipe_defense_system__REPORT.md) — SNIPE defense-system architecture, ManXYZ fitness, pangenome prevalence, environmental association, and phage-host evidence.
- [pitfalls](../summaries/pitfalls.md) — BERDL namespace, provenance, join, statistical-design, coverage, Spark, and reproducibility pitfalls.
- [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) — pathway completeness, capability versus dependency, pangenome openness, and metabolic ecotypes.
- [paperblast_explorer__REPORT](../summaries/paperblast_explorer__REPORT.md) — PaperBLAST literature coverage, protein-family clustering, dark families, and the bridge to Fitness Browser.
- [prophage_amr_comobilization__REPORT](../summaries/prophage_amr_comobilization__REPORT.md) — GTDB pangenome prophage–AMR co-localization, repertoire breadth, and the untested fitness-cost comparison.
- [discoveries](../summaries/discoveries.md) — cross-project discoveries integrating Fitness Browser findings with essentiality, condition-specific fitness, cofitness, AMR, metabolic modeling, and data-quality results.
- [functional_dark_matter__REPORT](../summaries/functional_dark_matter__REPORT.md) — experimentally prioritized dark genes, pathway hypotheses, conservation, environmental validation, and proposed campaigns.
- [fitness_modules__REPORT](../summaries/fitness_modules__REPORT.md) — ICA-derived pan-bacterial fitness modules and function-prediction benchmarks.
- [module_conservation__REPORT](../summaries/module_conservation__REPORT.md) — ICA fitness-module conservation in bacterial pangenomes and its essentiality limitation.
- [essential_genome__REPORT](../summaries/essential_genome__REPORT.md) — pan-bacterial essentiality, orthology, conservation, and module-based prediction.
- [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md) — GapMind pilot linking essential-gene organisms to pathway completeness and carbon-source capacity.
- [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md) — pathway completeness, latent capability, measured dependency, pangenome openness, and metabolic ecotypes.
- [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md) — DvH field-versus-laboratory fitness and pangenome conservation.
- [lab_field_ecology__REPORT](../summaries/lab_field_ecology__REPORT.md) — Oak Ridge field ecology comparison of laboratory metal tolerance and groundwater abundance.
- [fitness_effects_conservation__REPORT](../summaries/fitness_effects_conservation__REPORT.md) — Fitness Browser fitness, fitness breadth, and pangenome conservation across 43 bacteria.
- [conservation_fitness_synthesis__REPORT](../summaries/conservation_fitness_synthesis__REPORT.md) — Fitness Browser and pangenome conservation across 43 bacteria.
- [conservation_vs_fitness__REPORT](../summaries/conservation_vs_fitness__REPORT.md) — Fitness Browser gene fitness, pangenome clusters, and essentiality conservation.
- [enigma_carbon_census_1__REPORT](../summaries/enigma_carbon_census_1__REPORT.md) — ENIGMA Carbon Census linking compounds, fitness, utilization predictions, field occurrence, and abundance.
- [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) — four-database metabolic consistency analysis for *Pseudomonas* FW300-N2E3.
- [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md) — ENIGMA genotype × condition modeling and active-learning design.
- [metal_cross_resistance__REPORT](../summaries/metal_cross_resistance__REPORT.md) — gene-resolution metal cross-resistance, metal-important genes, and BacDive validation.
- [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) — pan-bacterial metal-fitness atlas, conserved modules, and pangenome-scale prediction.
- [acinetobacter_adp1_explorer__REPORT](../summaries/acinetobacter_adp1_explorer__REPORT.md) — ADP1 database and BERDL connectivity analysis.
- [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md) — ADP1 deletion growth phenotypes across 8 carbon sources.
- [adp1_triple_essentiality__REPORT](../summaries/adp1_triple_essentiality__REPORT.md) — ADP1 fitness, knockout, TnSeq, FBA, and proteomics comparison.
- [alphafold_msa_annotation__REPORT](../summaries/alphafold_msa_annotation__REPORT.md) — AlphaFold MSA depth, annotation gaps, and proposed fitness analyses.
- [amr_cofitness_networks__REPORT](../summaries/amr_cofitness_networks__REPORT.md) — AMR cofitness networks from Fitness Browser matrices.
- [amr_fitness_cost__REPORT](../summaries/amr_fitness_cost__REPORT.md) — AMR fitness costs and antibiotic-dependent importance.
- [amr_pangenome_atlas__REPORT](../summaries/amr_pangenome_atlas__REPORT.md) — AMR pangenome annotations linked to Fitness Browser measurements.
- [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md) — Fitness Browser phenotypes with metabolic gapfilling and annotation evidence.
- [aromatic_catabolism_network__REPORT](../summaries/aromatic_catabolism_network__REPORT.md) — transferred fitness data evaluating Complex I dependence across substrates.
- [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md) — BERDL data depth, cross-tenant bridges, realized use, and structural fitness atlas.
- [caulobacter_fur_lipida_loss__REPORT](../summaries/caulobacter_fur_lipida_loss__REPORT.md) — Caulobacter Fitness Browser envelope-stress signatures.
- [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md) — laboratory cofitness, pangenome co-occurrence, and co-inheritance.
- [core_gene_tradeoffs__REPORT](../summaries/core_gene_tradeoffs__REPORT.md) — function-specific burden, conservation, and condition-dependent fitness trade-offs.
- [costly_dispensable_genes__REPORT](../summaries/costly_dispensable_genes__REPORT.md) — costly, pangenome-dispensable genes across 43 bacteria.
- [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md) — counter-ion confounding and shared NaCl stress in metal-fitness measurements.
- [enigma_carbon_census_1__REPORT](../summaries/enigma_carbon_census_1__REPORT.md) — ENIGMA carbon compounds, fitness, utilization predictions, field occurrence, and abundance.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — cross-condition interpretation of mutant-growth fitness.
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — cofitness networks and multigene modules.
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — pathway completeness, metabolic gapfilling, and Fitness Browser evidence.
- [gene-essentiality](../concepts/gene-essentiality.md) — cross-organism essentiality and laboratory fitness.
- [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) — organism represented in the source database but absent from this collection.
- [complex-i](complex-i.md) — respiratory complex evaluated through transferred fitness measurements.
- [snipe-defense-system](snipe-defense-system.md) — SNIPE phage-defense system evaluated through pangenome and Fitness Browser evidence.

[^acinetobacter_adp1_explorer]: [acinetobacter adp1 explorer](../summaries/acinetobacter_adp1_explorer__REPORT.md)
[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
[^discoveries]: [discoveries](../summaries/discoveries.md)
[^functional_dark_matter]: [functional dark matter](../summaries/functional_dark_matter__REPORT.md)
[^truly_dark_genes]: [truly dark genes](../summaries/truly_dark_genes__REPORT.md)
[^essential_genome]: [essential genome](../summaries/essential_genome__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../summaries/webofmicrobes_explorer__REPORT.md)
[^snipe_defense_system]: [snipe defense system](../summaries/snipe_defense_system__REPORT.md)
[^paperblast_explorer]: [paperblast explorer](../summaries/paperblast_explorer__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../summaries/conservation_fitness_synthesis__REPORT.md)
[^conservation_vs_fitness]: [conservation vs fitness](../summaries/conservation_vs_fitness__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../summaries/fitness_effects_conservation__REPORT.md)
[^module_conservation]: [module conservation](../summaries/module_conservation__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../summaries/metal_cross_resistance__REPORT.md)
[^prophage_amr_comobilization]: [prophage amr comobilization](../summaries/prophage_amr_comobilization__REPORT.md)
[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
[^aromatic_catabolism_network]: [aromatic catabolism network](../summaries/aromatic_catabolism_network__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
[^lab_field_ecology]: [lab field ecology](../summaries/lab_field_ecology__REPORT.md)
[^fitness_modules]: [fitness modules](../summaries/fitness_modules__REPORT.md)
[^enigma_carbon_census_1]: [enigma carbon census 1](../summaries/enigma_carbon_census_1__REPORT.md)
[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^adp1_triple_essentiality]: [adp1 triple essentiality](../summaries/adp1_triple_essentiality__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
