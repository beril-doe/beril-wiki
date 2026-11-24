---
type: "Organism"
description: "Heavily sampled species excluded from ANI and ecotype analyses due to genome-count caps."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/discoveries.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/paperblast_explorer__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/snipe_defense_system__REPORT.md", "summaries/thermodynamic_impact__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["AIEC", "BW25113", "E. coli", "E. coli BW25113", "E. coli K-12", "E. coli Keio", "Escherichia coli K-12", "Keio", "adherent-invasive Escherichia coli"]
---
# Escherichia coli

Escherichia coli (also E. coli, E. coli K-12, BW25113, Keio, and adherent-invasive Escherichia coli, AIEC) is a heavily sampled species. A 500-genome cap excluded it from the AMR (antimicrobial resistance) ecotype case studies. [src: amr_strain_variation] Extraction of ANI (average nucleotide identity) for the phylogenetic signal analysis was limited to species with <=500 genomes, which also excluded it. [src: amr_strain_variation] It also appears in the Keio fitness data, a thermodynamic metabolic-model analysis and an IBD phage-targeting report. [src: discoveries, thermodynamic_impact, ibd_phage_targeting]

## Key facts

- Escherichia coli K-12 has 8,860 papers in PaperBLAST. [src: paperblast_explorer]
- Escherichia coli BW25113 in Web of Microbes (WoM) is the same strain as Keio in the [[entities/fitness-browser]], which allows direct metabolite-to-gene-fitness linking. [src: discoveries]
- The WoM match to Fitness Browser Keio lists 4,610 genes and 168 experiments. [src: webofmicrobes_explorer]

## Exclusion from genome-scale analyses

Several reports exclude E. coli because of its genome count. [src: amr_strain_variation, conservation_vs_fitness]

- The AMR ecotype case studies excluded it because it exceeds the 500-genome computational cap. [src: amr_strain_variation]
- ANI extraction for the phylogenetic signal analysis was limited to species with <=500 genomes. This excluded Escherichia coli (15,388 genomes) and [[entities/klebsiella-pneumoniae]] (14,240 genomes). [src: amr_strain_variation]
- The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly [[entities/klebsiella-pneumoniae]], [[entities/staphylococcus-aureus]] and Escherichia coli. Environmental species are underrepresented. [src: amr_strain_variation]
- In the conservation-versus-fitness analysis, the main E. coli clade was absent from the pangenome because it has too many genomes. Keio (BW25113) mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness]
- In the essential-metabolome report, E. coli genomes are completely absent from GapMind in the KBase pangenome collection. [src: essential_metabolome] The Keio genome GCF_000005845.2 has 0 GapMind predictions. [src: essential_metabolome] The report attributes this to the exclusion of E. coli from GTDB pangenome construction because it has too many genomes for species-level analysis. [src: essential_metabolome]

## Fitness data and dark genes

Keio is a top target for functional follow-up in the dark matter report, while WoM holds little data for this strain. [src: functional_dark_matter, webofmicrobes_explorer]

- WoM data for BW25113 are limited to 12 observations in ZMMG medium, focused only on sulfur metabolism. [src: webofmicrobes_explorer] The report notes this is minimal even though Keio is one of the richest Fitness Browser organisms. [src: webofmicrobes_explorer]
- In the functional dark matter report, Keio locus 14796 ranks 1 among essential dark gene candidates. Its score is 0.875, it has YbeY and TIGR00043 domains, and its operon context is ion transport plus NTP hydrolase, with high hypothesis confidence. [src: functional_dark_matter]
- The same ranking puts Keio locus 14768 at rank 6 (score 0.833, DUF493, lipoate biosynthesis plus PBP5 operon context). [src: functional_dark_matter] It puts locus 11474 at rank 10 (score 0.825, DUF4109, tRNA-Met plus translation operon context). [src: functional_dark_matter]
- Another table describes gene 14796 as conserved in 5+ phyla, in a synteny-confirmed operon, and predicted to mediate ion transport. [src: functional_dark_matter]
- E. coli K-12 (Keio) is fourth in Route A with 368 genes and the highest tractability (0.9). It has 259 immediately testable hypothesis-bearing genes and 205 essential genes ideal for CRISPRi (CRISPR interference). [src: functional_dark_matter]
- The proposed experiment knocks down the top 20 essential dark genes with growth curves, and its top target is Keio:14796. [src: functional_dark_matter] The report also proposes CRISPRi knockdown of Keio:14796 on varied carbon/nitrogen sources, monitored by OD600. [src: functional_dark_matter] It lists Keio:14796 among the highest-priority targets. [src: functional_dark_matter]
- For the darkest genes, the report recommends broad RB-TnSeq (random barcode transposon sequencing) screens over the standard ~50-100 conditions. E. coli K-12 has 109 genes in this category. [src: functional_dark_matter]

## ManXYZ and phage lambda

The SNIPE report uses Keio fitness data, as covered in [[entities/manxyz-mannose-phosphotransferase-system]]. Phage lambda phenotypes come from Burmeister et al. 2021 (PMID 34032565, PubMed identifier) and use the Keio collection (BW25113). [src: snipe_defense_system] Direct RB-TnSeq ManXYZ fitness measurements in E. coli K-12 cover 168 experiments (Price et al. 2018). [src: snipe_defense_system] Among the 48 Fitness Browser organisms, ManXYZ is present only in E. coli K-12 (Keio). [src: snipe_defense_system] The E. coli SNIPE protein A0A0A1A5Z2 is 558 aa. InterPro annotates it with PF13250 (positions 232–333) and PF13455 (positions 443–520). [src: snipe_defense_system]

Fitness Browser values for E. coli K-12 (168 experiments each):

- manX: worst fitness -3.93, average -0.249, 6 conditions with fit < -1, 4 with fit < -2. [src: snipe_defense_system]
- manY: worst fitness -3.82, average -0.171, 10 conditions with fit < -1, 4 with fit < -2. [src: snipe_defense_system]
- manZ: worst fitness -4.14, average -0.082, 7 conditions with fit < -1, 4 with fit < -2. [src: snipe_defense_system]

## Inflammatory bowel disease and AIEC

In the IBD phage-targeting report, E. coli stands out for iron and genotoxin biosynthetic gene clusters (BGCs). The report associates it with MIBiG Colibactin, Yersiniabactin and Enterobactin in target scoring. [src: ibd_phage_targeting] E. coli alone among Tier-A core species carries the iron-plus-genotoxin BGC signature. [src: ibd_phage_targeting] The tally is 54 iron MIBiG (19 Yersiniabactin, 16 Enterobactin, 19 siderophore-class). [src: ibd_phage_targeting] It is also 25 genotoxin (8 Colibactin, 15 Microcin B17). [src: ibd_phage_targeting] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

- E. coli has a Tier-A score of 3.6 and is not in the bile-acid network. Its action is strain-content-mediated and specific to the AIEC subset. [src: ibd_phage_targeting]
- The report assigns Tier-1 phage priority with low bile-acid cost. It requires strain-resolved targeting of the pks/Yersiniabactin/Enterobactin-positive AIEC subset. [src: ibd_phage_targeting]
- Only 8 of 23 UC Davis patients carry detectable E. coli (35 %). The report contrasts this with literature that frames AIEC as the prototypical Crohn's disease (CD) pathobiont. [src: ibd_phage_targeting]
- E. coli had 20 passing pathways in NB07b. It showed within-carrier CD-DOWN per-pathway abundance, opposite to its cohort-level CD-up direction. [src: ibd_phage_targeting]
- In NB09c, the HMP2 cadaverine correlation with E. coli was +0.45, the strongest in the curated cross-feeding panel. [src: ibd_phage_targeting]

## Plant-marker negative controls

The plant-microbiome report used E. coli as a negative control, and the marker panels misclassified it. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

- The refined marker cohorts misclassified neutral E. coli K-12 as dual-nature. [src: plant_microbiome_ecotypes]
- NB08 negative controls classified non-plant Escherichia, Salmonella and Clostridioides as 100% dual-nature. [src: plant_microbiome_ecotypes]
- The Phase 1 91-marker panel included ubiquitous bacterial functions (flagella, chemotaxis, T6SS, biofilm, quorum sensing, T2SS) that classified Escherichia and Salmonella as 100% dual-nature. [src: plant_microbiome_ecotypes]
- Escherichia negative controls improved to 25% PGP-only in the refined analysis, down from ubiquitous dual-nature classification in Phase 1. [src: plant_microbiome_ecotypes]

## Thermodynamic flux models

In the thermodynamic-impact report, the E. coli K-12 MG1655 model is listed as Proteobacteria with a GramNeg template. It has 1,765 reactions, 1,317 genes and growth 0.5625. [src: thermodynamic_impact] See thermodynamic constraint formulation in flux balance models.

- Hard-cutoff FVA (flux variability analysis) gave 1,732 Marvin-blocked reactions and 1,731 OPAM2-blocked reactions. It gave 2 newly blocked and 3 newly unblocked reactions. [src: thermodynamic_impact]
- rxn01545 changed from forward to blocked, as Marvin dG = 3.8 became OPAM2 dG = -159.8 kJ/mol. [src: thermodynamic_impact] rxn01649 changed from reverse to blocked, as Marvin dG = 11.6 became OPAM2 dG = -152.4 kJ/mol. [src: thermodynamic_impact]
- rxn10052 [src: thermodynamic_impact], rxn00097 [src: thermodynamic_impact] and rxn00104 [src: thermodynamic_impact] changed from blocked to variable when constraints were relaxed.
- Carbon-source phenotype predictions, unconstrained: CP 8, CN 2, FP 1, FN 1, accuracy 83.3%. [src: thermodynamic_impact]
- Carbon-source phenotype predictions, Marvin: CP 0, CN 3, FP 0, FN 9, accuracy 25.0%. [src: thermodynamic_impact]
- Carbon-source phenotype predictions, OPAM2: CP 0, CN 3, FP 0, FN 9, accuracy 25.0%. [src: thermodynamic_impact]
- Under TMFA (thermodynamics-based metabolic flux analysis), growth is 0.5625 unconstrained, 0.5625 with Marvin and 0.5625 with OPAM2, with 1,210 constrained reactions. [src: thermodynamic_impact]
- TMFA constrains more reactions than hard cutoffs (1,210 vs 928) while preserving full growth. [src: thermodynamic_impact]
- Under TMFA, 25 reactions show flux differences between Marvin and OPAM2 dG values. [src: thermodynamic_impact]
- The TMFA impact table gives 18 flux-changed reactions (percentage column 1.02), 4 newly blocked, 12 newly active and 2 reversed. [src: thermodynamic_impact]
