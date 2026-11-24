---
type: "Concept"
description: "Which functional categories and trait genes (COG, AMR, defense, plant-interaction, PGP) sit in the core versus accessory pangenome, and what that implies for horizontal acquisition versus vertical inheritance; stops at HGT-inference methods."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/cog_analysis__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_amr_comobilization__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
---
# Core versus accessory partitioning of gene functions and trait genes

This page covers which functional categories and trait genes sit in the core versus the accessory pangenome, and what that implies for horizontal acquisition versus vertical inheritance. In a 32-species COG analysis, translation, nucleotide, coenzyme, amino acid and energy categories are enriched in core genes, while mobile-element and defense categories are enriched among novel/singleton genes. [src: cog_analysis, discoveries] Anti-phage defense systems agree: 6 of 7 are strongly accessory-biased. [src: phage_defense_arsenal] Prophage markers and AMR genes are also mostly accessory, and prophage modules split into core-leaning lysis and packaging versus singleton-dominated integration and head morphogenesis. [src: prophage_amr_comobilization, prophage_ecology] AMR genes are less core than the pangenome baseline overall, but the split varies by environment, and soil AMR is majority core. [src: amr_pangenome_atlas, amr_environmental_resistome] Plant growth-promoting (PGP) genes are the opposite case: they are predominantly core, and the report rejects horizontal transfer for them. [src: discoveries, pgp_pangenome_ecology] The horizontal-acquisition reading is mostly an interpretation of core/accessory status, not a direct transfer test. [src: amr_environmental_resistome]

## Literature Context

Several candidate papers describe the same broad pattern the hub reports: accessory gene content is rich in adaptive and poorly characterised functions, and horizontal gene transfer (HGT) is the usual explanation. In Aggregatibacter, 1,550 core genes and 1,670 variable genes were found across 31 A. actinomycetemcomitans and 2 A. aphrophilus strains. Accessory genes made up 14.1% to 23.2% of A. actinomycetemcomitans genomes, and most fell in poorly characterised COG categories. They were often organised into genomic islands (n = 387) with base-composition biases, which the authors say suggests acquisition by HGT [PMID 26420795](https://pubmed.ncbi.nlm.nih.gov/26420795/). In E. coli, core genes were the most highly expressed and slowest evolving. Putatively transferred genes were expressed at the lowest level and evolved fastest [PMID 18218112](https://pubmed.ncbi.nlm.nih.gov/18218112/). In Burkholderiaceae, secondary replicons were enriched in the accessory pangenome fraction. The authors link this to faster gene acquisition by HGT and to adaptation to novel environments [PMID 30608550](https://pubmed.ncbi.nlm.nih.gov/30608550/). In Gammaproteobacteria, secondary replicons had a very small core gene set and were enriched in antibiotic, biocide and metal resistance genes [PMID 37185344](https://pubmed.ncbi.nlm.nih.gov/37185344/). A Nocardia cyriacigeorgica study found 2,935 single-copy core genes under purifying selection. It also found that HGT and mobile elements contributed to genomic plasticity, and that clades differed in functional categories [PMID 35430877](https://pubmed.ncbi.nlm.nih.gov/35430877/).

The corpus's COG result, with core enrichment in translation and energy and novel-gene enrichment in mobile elements and defense, is consistent with this picture. So are its accessory-biased defense systems and its accessory-leaning AMR genes. The corpus's reading of accessory AMR as acquired is also consistent with the replicon studies that tie resistance genes to HGT-prone replicons [PMID 37185344](https://pubmed.ncbi.nlm.nih.gov/37185344/). Its scale is larger than these single-genus or single-species studies, because it spans many species and phyla. That makes the cross-phylum consistency a mild extension of them, not a replication.

A caution comes from the one candidate that measures HGT directly. A tree-topology method applied to 297 core orthologous clusters from 40 microbial genomes detected significant HGT in 33 clusters. It estimated a low mean genome-specific HGT rate of 2.0% [PMID 16122348](https://pubmed.ncbi.nlm.nih.gov/16122348/). That is a different approach from composition or core/accessory status, and the papers do not compare the two. They do not show that status-based inference is unreliable. The hub itself notes that its transfer readings rest on core/accessory status and that nucleotide identity between soil and clinical AMR genes was not tested. Direct tests of that kind remain open.

The corpus's plant growth-promoting (PGP) result is not addressed by any candidate. The hub finds PGP genes predominantly core and rejects HGT for them. The candidates offer no PGP-specific evidence that confirms or contradicts this, so that claim stands as novel relative to this evidence set. The candidates on infant gut resistomes [PMID 39134593](https://pubmed.ncbi.nlm.nih.gov/39134593/) and a single adult fecal sample [PMID 29185915](https://pubmed.ncbi.nlm.nih.gov/29185915/) use "core resistome" for metagenomic carriage. This is not pangenome core status, so they do not bear directly on the hub's claims.

## Functional categories: a two-speed genome

A clusters of orthologous groups (COG) analysis of 32 bacterial species across 9 phyla (357,623 genes) finds a consistent "two-speed genome". [src: cog_analysis, discoveries] The report says all 8 predictions from its initial Neisseria gonorrhoeae analysis were confirmed across 32 species. [src: cog_analysis, discoveries] Novel/singleton genes are enriched in COG L (mobile elements) by +10.88%, with 100% consistency across species, which is the strongest signal. [src: cog_analysis, discoveries] They are enriched in COG V (defense mechanisms) by +2.83%, with 100% consistency. [src: cog_analysis, discoveries] They are enriched in COG S (unknown function) by +1.64%, with only 69% consistency. [src: cog_analysis, discoveries]

Core genes are enriched in the categories below. Translation (J) is the strongest depletion in novel genes. [src: cog_analysis, discoveries]

| COG category | Enrichment | Consistency |
|---|---|---|
| J (Translation) | -4.65% | 97% [src: cog_analysis, discoveries] |
| F (Nucleotide metabolism) | -2.09% | 100% [src: cog_analysis, discoveries] |
| H (Coenzyme metabolism) | -2.06% | 97% [src: cog_analysis, discoveries] |
| E (Amino acid metabolism) | -1.81% | 81% [src: cog_analysis, discoveries] |
| C (Energy production) | -1.75% | 88% [src: cog_analysis, discoveries] |

Composite assignments such as LV (mobile+defense) and EGP (amino acid+carbohydrate+inorganic ion) are described as genuine multifunctional genes, not annotation artifacts. [src: discoveries] LV shows +0.34% enrichment with 76% consistency. [src: discoveries] The report suggests this reflects functional modules such as mobile defense islands. [src: discoveries]

The report reads core genes as an ancient, conserved "metabolic engine" of translation, energy and biosynthesis. [src: cog_analysis, discoveries] It reads novel genes as recent acquisitions for ecological adaptation, including mobile elements, defense and niche-specific functions. [src: cog_analysis, discoveries] It asserts that horizontal gene transfer (HGT), not vertical inheritance, is the primary innovation mechanism, and that the L enrichment suggests most genomic novelty comes from mobile elements. [src: discoveries] It says the patterns hold across bacterial phyla, which it takes to suggest deep evolutionary constraint. [src: cog_analysis, discoveries] It calls this a fundamental organizing principle of pangenome structure. [src: cog_analysis] The core enrichment in translation (COG J) and energy production (COG C) matches Charlesworth & Jensen (2022) and the minimal-genome literature. [src: cog_analysis]

## Prophage modules and prophage-linked AMR

Prophage marker clusters in the pangenome inventory are 83.8% accessory and 53.8% singleton. [src: prophage_amr_comobilization] AMR gene clusters in the same inventory are 69.7% accessory and 36.1% singleton, so they are accessory but less often singleton than prophage markers. [src: prophage_amr_comobilization]

Within prophages, the pangenome conservation analysis shows modules differ. Lysis module D was 62.6% core and packaging module A was 57.0% core. [src: prophage_ecology] Integration module E was 59.3% singleton and head morphogenesis module B was 56.0% singleton. [src: prophage_ecology] The report calls this consistent with the expectation that phage structural genes diversify rapidly while regulatory and lysis genes are more conserved (Hendrix et al. 2000). [src: prophage_ecology] See [[concepts/annotation-based-prophage-detection-prevalence-and-domesticated-remnants]].

## Anti-phage defense systems

Six of seven bacterial defense systems are accessory-biased. They show highly significant auxiliary and singleton enrichment relative to a baseline of 46.8 % core and 37.9 % singleton across 132,531,501 gene clusters. [src: phage_defense_arsenal] The report calls this consistent with the defense-island hypothesis. [src: phage_defense_arsenal] Per-system core fractions differed from the 46.8 % baseline with χ² p ≈ 0 for all systems. [src: phage_defense_arsenal]

| System | Core % | Singleton % | Direction |
|---|---|---|---|
| Retron | 8.2 | 65.8 | Strong accessory [src: phage_defense_arsenal] |
| Gabija | 9.1 | 68.8 | Strong accessory [src: phage_defense_arsenal] |
| R-M Type II | 9.4 | 68.2 | Strong accessory [src: phage_defense_arsenal] |
| R-M Type I | 9.8 | 65.3 | Strong accessory [src: phage_defense_arsenal] |
| CBASS | 11.8 | 61.1 | Strong accessory [src: phage_defense_arsenal] |
| BREX | 20.7 | 55.8 | Moderate accessory [src: phage_defense_arsenal] |
| CRISPR-Cas | 27.4 | 47.2 | Mild accessory [src: phage_defense_arsenal] |
| DISARM | 40.6 | 42.3 | Near baseline [src: phage_defense_arsenal] |

For the accessory-enriched systems, singleton fractions are 1.5–1.8× above the 37.9 % background. The report reads this as consistent with active horizontal transfer of defense loci through mobile genetic elements, a core prediction of the defense-islands hypothesis of Rocha & Bikard 2022. [src: phage_defense_arsenal] R-M enzymes have been known to be mobile since the 1990s, and the report says its R-M Type II result (9 % core, 68 % singleton) quantifies this at pangenome scale. [src: phage_defense_arsenal] It reads the Retron 8 % core / 66 % singleton pattern as consistent with retrons being small-genetic-element hitchhikers. [src: phage_defense_arsenal]

DISARM is the exception, and the report says this is almost certainly a detection artefact. The DrmB SNF2 helicase Pfam (PF00176) anchor is a widespread housekeeping-helicase domain that inflates the cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal] The DISARM accessory-enrichment result is therefore unreliable, because the extra hits bias the distribution toward core. [src: phage_defense_arsenal] DISARM arms-race and syndrome results are unaffected, since they rely on species-level presence/absence rather than per-cluster calls. [src: phage_defense_arsenal] See [[concepts/pan-bacterial-prevalence-phylum-distribution-and-mobility-of-anti-phage-defense-systems]].

## Acquisition depth as an independent line of evidence

In the gene_function_ecological_agora project, Sankoff parsimony attributed 17M gain events on the GTDB-r214 species tree to five acquisition-depth bins: recent, older_recent, mid, older and ancient. [src: discoveries] The recent-to-ancient gain ratio per function class is a substantive measure of vertical-versus-horizontal dominance, separate from any pre-registered test. [src: discoveries] CRISPR-Cas had a ratio of 24.5×, read as an HGT-active signature. [src: discoveries] Mixed regulatory and metabolic pathway KOs had 2× the Innovator-Exchange rate of pure regulatory or pure metabolic KOs. [src: discoveries] See [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]].

Independent leaf_consistency analysis found the species-with-KO fraction falling monotonically across depth bins, from 0.34 (recent) to 0.20 (ancient). [src: discoveries] A clade-level finding with low within-clade leaf consistency can hide a mixture of positive sub-clades and negative members. [src: discoveries] Mycobacteriaceae mycolic acid shows this. The family-rank producer-side Cohen's d was 0.31, supporting H2 Innovator-Isolated. [src: discoveries] Median leaf consistency for the mycolic-acid KOs was 0.15, below the atlas reference 0.20. [src: discoveries] The report reads this as gain events landing in clades where only ~15% of family members carry the KO panel. [src: discoveries] Restricting to the mycolic-positive sub-clade (10 of 13 genera with mean leaf consistency ≥ 0.5) gave producer d=+0.394 versus family-rank d=+0.309. [src: discoveries] The pre-registered mycolic, photosystem II and Bacteroidota polysaccharide utilization locus findings each had convergent atlas Cohen's d, clade-by-biome Fisher's enrichment (p<10⁻¹¹) and BacDive phenotype evidence where coverage existed. [src: discoveries] The report argues this convergence makes a clade-level verdict robust against single-substrate failure. [src: discoveries]

## Plant growth-promoting and plant-interaction genes

Beneficial PGP genes are 64.6% core versus 45.2% for pathogenic genes (Mann-Whitney p=3.4e-125) in plant_microbiome_ecotypes. [src: discoveries] The report suggests beneficial functions are under stronger purifying selection and more deeply embedded in bacterial evolutionary history than pathogenic capabilities. [src: discoveries]

### Plant microbiome cohorts and baseline

The cohort table gives core and singleton percentages of gene clusters. The genome-wide baseline is the fraction of all gene clusters classified as core by their respective species pangenomes. [src: plant_microbiome_ecotypes] All chi-square tests against this baseline were significant (p≈0). [src: plant_microbiome_ecotypes]

| Cohort | Core % | Singleton % | Clusters |
|---|---|---|---|
| Beneficial | 64.6 [src: plant_microbiome_ecotypes] | 20.7 [src: plant_microbiome_ecotypes] | 60,590 [src: plant_microbiome_ecotypes] |
| Colonization | 66.6 [src: plant_microbiome_ecotypes] | 20.8 [src: plant_microbiome_ecotypes] | 153,092 [src: plant_microbiome_ecotypes] |
| Pathogenic | 45.2 [src: plant_microbiome_ecotypes] | 31.0 [src: plant_microbiome_ecotypes] | 374,416 [src: plant_microbiome_ecotypes] |
| Genome-wide baseline | 46.8 [src: plant_microbiome_ecotypes] | 35.3 [src: plant_microbiome_ecotypes] | — |

Beneficial gene clusters are predominantly core (64.6%), significantly above both the 46.8% baseline and pathogenic clusters (45.2%). [src: plant_microbiome_ecotypes] The per-species comparison gave Mann-Whitney U=83,567,419 (p=3.38e-125), with a bootstrap 95% CI for the beneficial-pathogenic difference of [0.089, 0.106]. [src: plant_microbiome_ecotypes] That test used species with ≥3 markers of each type, as a complementary species-level view. [src: plant_microbiome_ecotypes] The report presents this as a quantitative demonstration across the full bacterial tree of life. [src: plant_microbiome_ecotypes] Among specific functions, the highest core fractions were biofilm (83.3%), IAA biosynthesis (78.1%), nitrogen fixation (72.3%) and phosphate solubilization (70.9%). [src: plant_microbiome_ecotypes]

A further architecture-function analysis (Phase 2) extended this to 50 novel ortholog groups (OGs) with 60.1–83.1% core fractions. [src: plant_microbiome_ecotypes] All 50 had core fractions of 60.1–83.1% against a baseline of 46.8%, which the report interprets as reinforcing stable core-genome inheritance of plant-enriched functions. [src: plant_microbiome_ecotypes] The report also suggests plant adaptation involves HGT-mediated accessory gene acquisition followed by core genome stabilization, reconciling genus-level mobilome enrichment (MGnify, p=1.49×10⁻⁵) with genome-level mobile element depletion from the literature. [src: plant_microbiome_ecotypes]

In contrast, T4SS (48.5% singleton), coronatine toxin (45.2% singleton) and effectors (39.8% singleton) were strongly accessory/singleton-enriched. [src: plant_microbiome_ecotypes] Overall, plant-interaction markers had a singleton enrichment ratio of 0.78, meaning they are less mobile than the genomic average (Wilcoxon p<1e-300). [src: plant_microbiome_ecotypes] Cross-species context variation (the same ortholog group core in one species and singleton in another) was higher for pathogenic markers (0.534) than beneficial ones (0.450), but not significantly (Kruskal-Wallis p=0.122). [src: plant_microbiome_ecotypes]

The PGP result supports H2 and aligns with Levy et al. (2018), who found plant-associated bacteria enriched in core metabolic functions but depleted in mobile elements. [src: plant_microbiome_ecotypes] The report suggests beneficial functions are under strong positive selection once acquired and become fixed in the core genome. [src: plant_microbiome_ecotypes] It reads pathogenic functions (T3SS, effectors, toxins) as more dynamic, consistent with host-pathogen arms-race coevolution. [src: plant_microbiome_ecotypes]

The result contrasts with Loper et al. (2012), who found biocontrol traits in Pseudomonas largely accessory. [src: plant_microbiome_ecotypes] The report suggests taxonomic scope may explain this: its analysis spans 25,660 species, while Loper et al. studied 10 strains within a single species group. [src: plant_microbiome_ecotypes]

### Domain-based markers

A Phase 2b Pfam recovery found 19,364 domain hits across 7,962 species for five of 10 marker Pfams. [src: plant_microbiome_ecotypes] Core fractions were low to moderate: nitrogenase NifH PF00142 (6,632 hits, 4,040 species, 32.4% core) [src: plant_microbiome_ecotypes], cellulase GH5 PF00150 (6,898 hits, 3,234 species, 25.9%) [src: plant_microbiome_ecotypes], pectate lyase 3 PF12708 (4,149 hits, 2,283 species, 24.6%) [src: plant_microbiome_ecotypes], pectate lyase PF00544 (1,115 hits, 546 species, 20.8%) [src: plant_microbiome_ecotypes] and T6SS VgrG PF05943 (570 hits, 343 species, 10.9%). [src: plant_microbiome_ecotypes] The report considers the higher core fraction of NifH (32.4%) than of CWDEs (21–26%) consistent with H2. [src: plant_microbiome_ecotypes]

### PGP genes in the pangenome ecology report

The pgp_pangenome_ecology report agrees. All 13 PGP genes had higher core fractions than the genome-wide 46.8% core baseline (chi-square, BH-FDR [Benjamini-Hochberg false discovery rate] q < 0.05 for all genes). [src: pgp_pangenome_ecology] The mean accessory fraction was 29.7% versus 53.2% genome-wide. [src: pgp_pangenome_ecology] Selected genes:

| Gene | Core | Auxiliary | Singleton | q vs baseline |
|---|---|---|---|---|
| pqqC | 81.5% | 7.8% | 10.7% | 0.0 [src: pgp_pangenome_ecology] |
| hcnA | 78.5% | 10.8% | 10.8% | 9.2e-37 [src: pgp_pangenome_ecology] |
| pqqB | 78.1% | 8.9% | 13.0% | 3.0e-247 [src: pgp_pangenome_ecology] |
| ipdC | 76.5% | 9.7% | 13.7% | 3.4e-19 [src: pgp_pangenome_ecology] |
| acdS | 70.4% | 13.4% | 16.2% | 7.9e-25 [src: pgp_pangenome_ecology] |
| nifH | 63.8% | 15.1% | 21.0% | 4.3e-71 [src: pgp_pangenome_ecology] |
| pqqD | 55.5% | 17.0% | 27.5% | 2.2e-86 [src: pgp_pangenome_ecology] |

pqqD is the most widespread PGP gene, present in 11,040 species. [src: pgp_pangenome_ecology] It is the most promiscuous pqq gene and often occurs as a single-gene orphan in species lacking other pqq genes. [src: pgp_pangenome_ecology] The report calls pqqD an outlier (55.5% core versus 63–81% for other PGP genes, singleton fraction 27.5%), suggesting it occasionally spreads horizontally as a standalone gene. [src: pgp_pangenome_ecology] The functional pqq operon (pqqB–pqqC as a unit) is predominantly core. [src: pgp_pangenome_ecology] The report rejects its HGT hypothesis (H3) and concludes PGP genes are inherited vertically with the core genome. [src: pgp_pangenome_ecology, discoveries] It notes this runs counter to the HGT narrative that has dominated the PGPB literature. [src: pgp_pangenome_ecology] It reads the core pqqC–acdS module as a stable, specialized rhizosphere adaptation, not a recently acquired package. [src: pgp_pangenome_ecology]

The literature fits. Nascimento et al. (2014) found predominantly vertical acdS inheritance despite some HGT events, including in some Proteobacteria. [src: pgp_pangenome_ecology] pqqC's use as a phylogenetic marker (Meyer et al. 2011) implies sufficient vertical inheritance for phylogenetic signal. [src: pgp_pangenome_ecology]

Pangenome openness (singleton fraction) correlates negatively with PGP gene richness (Spearman ρ = −0.195, p = 2.0e-97, n = 11,272 species with ≥2 genomes). [src: pgp_pangenome_ecology] The report reads this as consistent with stable, specialized niches rather than generalist HGT-driven acquisition. [src: pgp_pangenome_ecology] It relates this to Sentausa & Fournier (2024, PNAS), who found plant- and host-associated lifestyles tend toward more closed pangenomes. [src: pgp_pangenome_ecology] See [[concepts/pangenome-openness-and-its-correlates]].

The plant-interaction picture is not uniform. Species carrying singleton marker gene clusters are 16x more likely to carry transposase/integrase singletons (OR=15.95, p=8.8e-20). [src: discoveries] The report suggests recently acquired plant-interaction genes arrive by HGT on mobile genetic elements. [src: discoveries] See [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

## Storage-pathway genes

Among 311 discordant phaC-positive species, 60.1% carry phaC as accessory genome, versus 32.3% across all phaC-carrying species. The report reads this as strong support for horizontal acquisition. [src: phb_granule_ecology] Overall, 5,371 species carry core phaC and 1,959 carry accessory phaC, and some species carry both. [src: phb_granule_ecology] See [[concepts/horizontal-transfer-of-storage-pathway-genes-inferred-from-pangenome-core-accessory-status]].

## Metal functional categories

Across 293,059 prokaryotic genomes, the core fraction at the 95% prevalence threshold is 0 for all five metal functional categories, because no metal KO meets the near-universal threshold. [src: comprehensive_metal_ecology] Category conditional phylogenetic generalized least squares (PGLS) therefore finds that coreness cannot explain functional specificity. [src: comprehensive_metal_ecology]

## Annotation and sequence-database depth

Core genes are better represented in sequence databases than accessory genes. This fits the classic view that core genes do housekeeping and accessory genes encode adaptive traits. [src: alphafold_msa_annotation] Median multiple sequence alignment (MSA) depth is 15,308 for core gene clusters. That is 2.89× the auxiliary+singleton median of 5,299 and 2.77× the auxiliary non-singleton median of 5,527. [src: alphafold_msa_annotation] The gap is largest at the low end: the 10th-percentile MSA depth is 334 for core genes and 25–32 for accessory genes. [src: alphafold_msa_annotation] The report concludes that even poorly represented core genes are better characterised than the typical accessory gene. [src: alphafold_msa_annotation]

| Class | n clusters | Median MSA depth | p10 | p90 | Very low (<10) | Hypothetical |
|---|---|---|---|---|---|---|
| Core | 25,571,299 | 15,308 | 334 | 19,500 | 415,733 (1.6%) | 979,912 (3.8%) [src: alphafold_msa_annotation] |
| Aux non-singleton | 5,384,900 | 5,527 | 32 | 19,192 | 245,002 (4.6%) | 622,748 (11.6%) [src: alphafold_msa_annotation] |
| Aux + singleton | 7,095,643 | 5,299 | 25 | 19,203 | 392,959 (5.5%) | 979,300 (13.8%) [src: alphafold_msa_annotation] |

Core genes are far less likely to be hypothetical. The chi-square statistic is above 500,000, with odds ratios of 0.25 (core vs aux+singleton) and 0.31 (core vs aux non-singleton). [src: alphafold_msa_annotation] The report reads the MSA gradient as the expected effect of long-term purifying selection in core genomes. [src: alphafold_msa_annotation] It describes two separate drivers of the annotation gap. The first is MSA depth, which applies to all classes. The second is a pangenome-class gap, in which accessory and singleton genes carry more hypothetical proteins independent of MSA depth. [src: alphafold_msa_annotation] The report tentatively attributes the second gap to horizontal transfer, rapid evolution and a taxonomically narrow distribution. [src: alphafold_msa_annotation] The gap is concentrated in accessory genes and in a subset of highly conserved core genes. [src: alphafold_msa_annotation] The structural novelty signal is present within every class. [src: alphafold_msa_annotation] The report notes that the lower hypothetical rate in core genes seems to contradict its hypothesis H2 as literally stated. It says the paradox-protein census resolves this. [src: alphafold_msa_annotation] It says no earlier analysis quantified this gradient against 241M AlphaFold entries. [src: alphafold_msa_annotation] See [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes]].

## Antimicrobial resistance genes

AMR genes are under-represented in the core overall, though not uniformly accessory. In the atlas, 30.3% of AMR genes are core versus a 46.8% baseline (OR=0.49). [src: amr_pangenome_atlas] The auxiliary genome is 2.2x enriched for AMR (33.6% vs 15.3%). [src: amr_pangenome_atlas] In a paired test of 4,252 species with ≥5 AMR clusters each, 63.7% had AMR less core than their species baseline (Wilcoxon p=1.1e-130, mean difference -0.102). [src: amr_pangenome_atlas] Resistance mechanism strongly predicts conservation status (χ² = 69.3, p = 1.4×10⁻¹³). [src: amr_fitness_cost] The report cites a split of metal resistance 44% accessory versus efflux 13% core. [src: amr_environmental_resistome]

Within species, core AMR genes are mostly fixed, auxiliary ones are variable or rare, and singletons are mostly rare. [src: amr_strain_variation]

| Atlas class | Fixed | Variable | Rare |
|---|---|---|---|
| Core | 77.3% | 22.7% | 0.0% [src: amr_strain_variation] |
| Auxiliary | 0.0% | 57.3% | 42.7% [src: amr_strain_variation] |
| Singleton | 0.0% | 21.3% | 78.7% [src: amr_strain_variation] |

### Environment dependence

The core/accessory split of AMR varies with environment across 14,723 species. [src: amr_environmental_resistome] The core share differs significantly by environment (KW H=506.0, p=4×10⁻¹⁰⁷, η²=0.036). [src: amr_environmental_resistome] Clinical species are 68% accessory versus 43% for soil. [src: amr_environmental_resistome]

| Environment | Mean core AMR | Mean accessory AMR |
|---|---|---|
| Soil | 57.1% | 42.9% [src: amr_environmental_resistome] |
| Aquatic | 54.4% | 45.6% [src: amr_environmental_resistome] |
| Host-associated | 49.7% | 50.3% [src: amr_environmental_resistome] |
| Other environmental | 40.4% | 59.6% [src: amr_environmental_resistome] |
| Clinical | 32.4% | 67.6% [src: amr_environmental_resistome] |
| Human gut | 19.7% | 80.3% [src: amr_environmental_resistome] |

Clinical and human gut species carry 2.5× more AMR clusters than soil or aquatic species, and the excess is almost entirely accessory. [src: amr_environmental_resistome] Soil species average 2 AMR clusters, mostly core. [src: amr_environmental_resistome]

The report interprets this as chromosomal natural resistance in soil versus mobile clinical resistance. [src: amr_environmental_resistome] It also interprets it as an ancient baseline resistome with clinical enrichment above it from anthropogenic antibiotic selection. [src: amr_environmental_resistome] It confirms at pangenome scale the pattern Jiang et al. (2024) saw in river metagenomes. [src: amr_environmental_resistome] It asserts that clinical and gut species acquired AMR largely by HGT. [src: amr_environmental_resistome] It reads accessory efflux and target-modification genes in clinical and gut bacteria as recent HGT-driven accumulation. [src: amr_environmental_resistome] It reads the more often core metal-resistance genes of soil and aquatic bacteria as ancient adaptation. [src: amr_environmental_resistome] It explains efflux as core because it serves host-associated organisms across conditions. It explains metal resistance as accessory because it is needed only in metal-rich environments. [src: amr_environmental_resistome]

These transfer readings rest on core/accessory status. The report did not test nucleotide identity between soil and clinical genes. [src: amr_environmental_resistome] The 95% core threshold depends on genome count, so labels are imprecise for species with few genomes. [src: amr_environmental_resistome] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]] and [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]].

### Proposed follow-ups in the source report

The report proposes identifying AMR clusters present in both soil and clinical species as candidates for recent cross-niche HGT. [src: amr_environmental_resistome] It proposes testing whether the accessory AMR fraction rose over time in species sampled across decades, such as S. aureus and K. pneumoniae. [src: amr_environmental_resistome] It proposes combining the environment-AMR profiles with amr_fitness_cost to ask whether clinically enriched AMR genes are costlier from recent acquisition or cheaper from strong selection. [src: amr_environmental_resistome] It proposes testing whether accessory AMR clusters in clinical species associate with plasmids, transposons or integrative elements once genomad_mobile_elements is available in the KBase Data Lakehouse. [src: amr_environmental_resistome]

## Tensions

- The cog_analysis report asserts HGT, not vertical inheritance, is the primary innovation mechanism in bacterial pangenomes. [src: discoveries] The PGP analysis rejects HGT for 13 PGP genes and finds them vertically inherited with the core. [src: pgp_pangenome_ecology]
- The PGP genes are mostly core, yet plant-interaction marker singletons co-occur with transposase/integrase singletons, which the report reads as recent HGT on mobile elements. [src: discoveries]
- The plant microbiome report reads its core-enriched OGs as stable core inheritance [src: plant_microbiome_ecotypes], while also suggesting acquisition by HGT followed by core stabilization. [src: plant_microbiome_ecotypes] Both readings rest on core/accessory status.
- The plant microbiome report finds beneficial genes largely core, contrasting with Loper et al.'s largely accessory Pseudomonas biocontrol traits. The report attributes this to taxonomic scope, which it does not test. [src: plant_microbiome_ecotypes]
- pqqD is largely accessory-leaning (55.5% core, 27.5% singleton), while the pqqB–pqqC operon is predominantly core. [src: pgp_pangenome_ecology]

## Open Directions

- Compare nucleotide identity of AMR clusters shared between soil and clinical species, to close the gap left by status-only inference.
- Test the accessory AMR fraction over time in densely sampled species such as S. aureus and K. pneumoniae.
- Combine environment-AMR profiles with amr_fitness_cost to separate recent-acquisition cost from selection.
- Test plasmid, transposon and integrative-element association of accessory AMR clusters once mobile-element calls exist.
- Recompute core/accessory labels with a genome-count-aware threshold, to check how much small-genome-count imprecision shifts the environment contrasts.
- Run the acquisition-depth gain-ratio analysis on PGP genes, to test directly whether their core status reflects vertical inheritance rather than inferring it from core/accessory labels.
- Repeat the metal analysis with a lower prevalence threshold, since no metal KO reaches 95% and coreness could not be tested.
- Recompute DISARM core/accessory classes with a more specific anchor than PF00176, to see whether DISARM becomes accessory like the other defense systems.
- Repeat the beneficial-versus-pathogenic core comparison within Pseudomonas only, to test whether taxonomic scope explains the contrast with Loper et al.
- Test whether prophage modules with high core fractions (lysis, packaging) are domesticated remnants rather than active prophages, using the module-level conservation classes.
