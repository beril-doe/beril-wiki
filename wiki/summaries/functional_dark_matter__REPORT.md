---
type: "Summary"
description: "Summary of the project Functional Dark Matter — Experimentally Prioritized Novel Genetic Systems."
doc_type: "short"
full_text: "sources/functional_dark_matter__REPORT.md"
---
# Functional Dark Matter — Experimentally Prioritized Novel Genetic Systems

This page summarizes the Functional Dark Matter project, which asked which unannotated bacterial genes are most worth testing experimentally. Across 48 Fitness Browser (FB) organisms with 228,709 genes, the report finds 57,011 (24.9%) lacking functional annotation. [src: functional_dark_matter] Hypotheses from genomic proximity are leads for experimental testing, not validated assignments. [src: functional_dark_matter]

## Key Findings

### Census and pangenome links
Most dark genes link to pangenomes, and most of those with conservation tiers are conserved at kingdom or species level. [src: functional_dark_matter]

The report found pangenome links for 39,532 (69.3%) of the 57,011 dark genes through the conservation_vs_fitness project. [src: functional_dark_matter]

Full-pangenome querying and OG_id propagation bring pangenome conservation coverage from 32,791 (57.5%) to 37,997 (66.6%) dark genes. [src: functional_dark_matter]

Among 57,011 dark genes including 19,014 FB-only fallback assignments, the conservation tiers are kingdom 51.4%, species 29.8%, genus 6.2%, class 4.0%, family 3.5%, mobile 1.9%, phylum 1.9% and order 1.3%. [src: functional_dark_matter]

Kingdom-level true knowledge gaps score highest in the conservation × ignorance prioritization, and species-specific strong hypotheses score lowest. [src: functional_dark_matter]

The darkness census classifies 1,853 dark genes as T5 Dawn, with 5–6 evidence lines and nearly characterized status. [src: functional_dark_matter]

See [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]] and [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]].

### Pathway gaps
Across 44 FB-linked species, GapMind identified 1,256 organism-pathway pairs with nearly complete pathways (`steps_missing_low`) where dark genes with strong fitness effects co-occur. [src: functional_dark_matter]

The GapMind analysis reports rhamnose utilization gaps in 31 organisms, with Marinobacter, P. putida and Phaeo as examples. [src: functional_dark_matter]

Marinobacter has 49 gapped pathways in the report's GapMind analysis. [src: functional_dark_matter]

Domain matching of the 1,256 pairs identified 42,239 gene-pathway candidates across 3,186 unique dark genes, with 5,398 high-confidence (EC prefix match), 4,687 medium-confidence (PFam family match) and 32,154 low-confidence (keyword match) hits. [src: functional_dark_matter]

See [[concepts/metabolic-pathway-gap-filling-by-unannotated-genes]].

### Cross-organism and lab–field concordance
Among dark gene ortholog groups present in 3+ FB organisms, 65 show measurable fitness concordance. [src: functional_dark_matter]

Dark ortholog group OG14628 has carbon-source fitness concordance of 1.00 across 5 organisms and occurs in Ralstonia spp. [src: functional_dark_matter]

The strongest concordance is in carbon-source genes (3–8 organisms) and motility genes (3 organisms each), suggesting conserved unannotated carbohydrate-metabolism and chemotaxis components. [src: functional_dark_matter]

Among 151 testable accessory dark gene clusters, 10 showed significant environmental category enrichment (FDR < 0.05). [src: functional_dark_matter]

In NMDC abiotic validation, pH-phenotype carrier abundance correlated positively as expected with pH (rho +0.157, n 4,366, FDR 7.4e-25). [src: functional_dark_matter]

In NMDC trait-condition validation, carbon-source carriers correlated with fermentation (ρ=0.59). [src: functional_dark_matter]

The report considers the 4/4 pre-registered abiotic prediction rate more meaningful than the overall NMDC correlation rate, because it tests specific directional hypotheses. [src: functional_dark_matter]

See [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]] and [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]].

### Prioritized candidates and context evidence

The report places P. putida N2C3 AO356_11255 first among prioritized dark genes, with a fitness effect of 3.4 under nitrogen, a D-Ala-D-Ala carboxypeptidase module prediction, an EamA domain, accessory status and score 0.715. [src: functional_dark_matter]

Shewanella MR-1 genes 199738, 203545 and 202450 have K03306 module predictions with different domain architectures, suggesting paralogous members of a conserved nitrogen-responsive system. [src: functional_dark_matter]

Essential dark genes, defined by absence of viable transposon mutants, represent 55% of experimentally actionable dark matter but score poorly in the fitness-centric NB05 framework. [src: functional_dark_matter]

Shewanella MR-1 locus 201473 ranks 5 among essential dark gene candidates with score 0.835, EarP and TIGR03837 domains, EF-P plus flavodoxin operon context, and high hypothesis confidence. [src: functional_dark_matter]

Cross-species synteny analysis tested 21,011 dark gene–operon partner pairs, those with ortholog groups assigned to both genes, across up to 47 FB organisms. [src: functional_dark_matter]

In operon validation, 1,129 pairs are mutual top-5 cofit pairs, described by the report as the strongest possible co-expression signal from the Fitness Browser. [src: functional_dark_matter]

See [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]] and [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].

### Experimental roadmap and organism choice
The roadmap points first to MR-1 and identifies phyla missing from the FB. [src: functional_dark_matter]

The evidence-weighted roadmap ranks MR-1 as the top organism, with 61 candidates (47 fitness-active plus 14 essential), 83 synteny-validated pairs and 31 cofit-validated pairs. [src: functional_dark_matter]

Greedy weighted set-cover over 16,488 scored dark genes identifies 42 organisms from 28 genera covering 95% of total priority value. [src: functional_dark_matter]

The first 10 organisms in the conservation-weighted covering set cover 31% of priority. [src: functional_dark_matter]

The report classifies Actinobacteria FB coverage as a critical gap, with 0 organisms. [src: functional_dark_matter]

The report classifies Deltaproteobacteria FB coverage as a low gap, with 5 organisms and 17 top-500 genes. [src: functional_dark_matter]

Streptomyces coelicolor A3(2) is priority 2 for new library construction, as a genetically tractable Actinobacteria model that would add an entirely missing phylum. [src: functional_dark_matter]

Campylobacter jejuni NCTC 11168 is priority 5 for library construction, to add missing Epsilonproteobacteria. [src: functional_dark_matter]

The dark gene action plans flag 8,900 essential genes for CRISPRi-based approaches. [src: functional_dark_matter]

See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]] and [[entities/greedy-weighted-set-cover-organism-selection]].

### Re-annotation
Cross-referencing with Bakta leaves some genes hypothetical but still links them to other databases. [src: functional_dark_matter]

The report cross-referenced Bakta v1.12.0 (DB v6.0) annotations for 132.5M pangenome cluster representatives against its 57,011 dark-gene catalog. [src: functional_dark_matter]

Among 6,427 genes remaining hypothetical in both FB and Bakta, 79.4% gain UniRef50 links. [src: functional_dark_matter]

See [[entities/bakta]].

## Key Findings: Finding 3: GapMind identifies 1,256 organism-pathway pairs with metabolic …

This part of the report counts the functionally dark genes in the Fitness Browser (FB) and picks out the experimentally actionable ones: 57,011 dark genes, of which 17,344 are strongly affected or essential. [src: functional_dark_matter] It then links them to pangenomes, fitness modules, GapMind pathway gaps and cross-organism fitness concordance. The counts are direct tallies. The pathway-gap and ortholog links are co-occurrence or concordance results, not demonstrated functions. [src: functional_dark_matter]

### Census of dark genes

About one in four genes in the FB organisms lacks functional annotation. Across 48 FB organisms (228,709 genes), 57,011 (24.9%) lack functional annotation ("hypothetical protein," DUF, or "uncharacterized"). [src: functional_dark_matter] Of these, 7,787 show strong fitness effects (|fitness| ≥ 2 in at least one condition). [src: functional_dark_matter] Another 9,557 are essential, with no viable transposon mutants. [src: functional_dark_matter] Together, 17,344 genes are the experimentally actionable dark matter: genes with clear biological importance but unknown function. [src: functional_dark_matter] See [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]] and [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].

Dark genes are not randomly distributed across organisms. Some species have >35% hypothetical genes and others <15%, which the report attributes to annotation depth rather than true functional content. [src: functional_dark_matter] Among dark genes with strong fitness effects, stress conditions (metals, oxidative, osmotic) dominate, followed by carbon source and nitrogen source utilization. [src: functional_dark_matter]

### Pangenome and module links

Of the 57,011 dark genes, 39,532 (69.3%) have pangenome links via the `conservation_vs_fitness` project. [src: functional_dark_matter] Among these, 12,686 are accessory (environment-specific). [src: functional_dark_matter] Of those, 511 are both accessory and strongly fitness-affecting, which the report calls the prime candidates for biogeographic analysis. [src: functional_dark_matter] Separately, 6,142 dark genes belong to ICA (independent component analysis) fitness modules from the `fitness_modules` project. These modules give guilt-by-association function predictions. [src: functional_dark_matter]

### GapMind pathway gaps

GapMind links dark genes to nearly-complete pathways only at the organism level. Across 44 FB-linked species, it found 1,256 organism-pathway pairs. Each pair has a nearly-complete pathway (score `steps_missing_low`) in an organism that also has dark genes with strong fitness effects. [src: functional_dark_matter] These are organism-level co-occurrences, and no direct gene-to-gap enzymatic matching was performed. [src: functional_dark_matter] The report suggests the dark genes could encode the missing steps. Confirming this requires EC (Enzyme Commission) number matching, structure prediction, or experimental validation. [src: functional_dark_matter] See [[concepts/metabolic-pathway-gap-filling-by-unannotated-genes]].

Carbon source utilization pathways are the most frequently gapped. [src: functional_dark_matter] The report's examples are:

| Pathway | Type | Organisms with gap | Examples |
|---|---|---|---|
| Fucose utilization | carbon | 32 | Marinobacter, P. stutzeri RCH2, D. vulgaris [src: functional_dark_matter] |
| Rhamnose utilization | carbon | 31 | Marinobacter, P. putida, Phaeo [src: functional_dark_matter] |
| Sorbitol utilization | carbon | 30 | D. desulfuricans, D. vulgaris, Miyama [src: functional_dark_matter] |
| Myoinositol utilization | carbon | 28 | P. putida, P. syringae, WCS417 [src: functional_dark_matter] |
| Gluconate utilization | carbon | 26 | Marinobacter, D. desulfuricans [src: functional_dark_matter] |
| Asparagine biosynthesis | amino acid | 24 | across diverse phyla [src: functional_dark_matter] |

The organisms with the most gapped pathways are Marinobacter (49) [src: functional_dark_matter], D. desulfuricans ME-23 (45) [src: functional_dark_matter] and P. stutzeri (45). [src: functional_dark_matter] The report says these also have the largest dark gene complements and the most specific fitness phenotypes. It suggests their missing steps may be encoded by dark genes. [src: functional_dark_matter] This is a suggestion, not a tested result.

### Domain matching

To go beyond organism-level co-occurrence, the report used curated pathway-enzyme mappings (EC prefixes, PFam families, functional keywords). These identify dark genes whose annotations are compatible with gapped pathways. [src: functional_dark_matter] Across the 1,256 organism-pathway pairs, domain matching found 42,239 gene-pathway candidates in 3,186 unique dark genes. [src: functional_dark_matter] The hits split by confidence:

- 5,398 high-confidence hits (EC prefix match). [src: functional_dark_matter]
- 4,687 medium-confidence hits (PFam family match). [src: functional_dark_matter]
- 32,154 low-confidence hits (keyword match). [src: functional_dark_matter]

The report says these candidates narrow the search from all dark genes in a gapped organism to those with enzymatically plausible annotations. [src: functional_dark_matter] Most hits are low-confidence keyword matches. [src: functional_dark_matter]

### Cross-organism fitness concordance

Some dark ortholog groups behave consistently across species. Among dark gene ortholog groups present in 3+ FB organisms, 65 show measurable fitness concordance. This means orthologs of the same unknown gene produce fitness effects under the same condition classes across different bacterial species. [src: functional_dark_matter] See [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]]. The top groups, all with concordance 1.00, are:

| Group | Condition class | Organisms | Domain or note |
|---|---|---|---|
| OG11386 | carbon source | 8 | DUF5064; P. putida, P. syringae, P. stutzeri RCH2 [src: functional_dark_matter] |
| OG15006 | carbon source | 7 | Ralstonia spp. [src: functional_dark_matter] |
| OG05812 | stress | 8 | Peptidase_M50; MR-1, SB2B; module-predicted TIGR01730 [src: functional_dark_matter] |
| OG05815 | stress | 8 | ParE_toxin; S. meliloti [src: functional_dark_matter] |
| OG14628 | carbon source | 5 | Ralstonia spp. [src: functional_dark_matter] |
| OG12530 | carbon source | 4 | DUF2844; B. thailandensis, Burkholderia sp. 376 [src: functional_dark_matter] |
| OG03384 | stress | 6 | Metallophos; module-predicted glutathione S-transferase [src: functional_dark_matter] |
| OG10428 | motility | 3 | ThiS; S. meliloti; max abs fit = 2.2 [src: functional_dark_matter] |
| OG10455 | motility | 3 | MS_channel; S. meliloti; mechanosensitive channel domains [src: functional_dark_matter] |

The strongest concordance is in carbon source genes (spanning 3–8 organisms) and motility genes (3 organisms each). The report suggests these are conserved but unannotated components of carbohydrate metabolism and chemotaxis machinery, respectively. [src: functional_dark_matter] It also notes that OG05812 carries a Peptidase_M50 domain (site-2 protease family), hinting at a conserved regulatory protease under stress. [src: functional_dark_matter]

## Key Findings: Finding 7: Lab-field concordance rate of 61.7%, with NMDC validation …

This part of the report maps dark gene clusters across species, then asks whether the genomes that carry them come from environments that match their lab fitness phenotypes. Breadth is a coarse tool: it does not separate candidates. [src: functional_dark_matter] The lab–field concordance is modest in aggregate: 29/47 clusters were concordant, and one test of that figure is marginal while a second is significant. [src: functional_dark_matter] A separate NMDC metagenomic validation confirmed all 4 testable predictions. [src: functional_dark_matter]

### Phylogenetic breadth

The report maps 30,756 dark gene clusters across 27,690 species. [src: functional_dark_matter] Some clusters are clade-restricted (a single phylum) and others are widespread (3+ phyla). [src: functional_dark_matter] The report treats widespread families as the highest-priority unknowns, because they are conserved across diverse bacteria yet lack annotation. [src: functional_dark_matter] See [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]].

The breadth classification is coarse. 99.9% of dark gene clusters (30,721 of 30,756) map to "universal" breadth, meaning root-level eggNOG ortholog groups (OG) present across domains of life, so the classification does not discriminate among candidates. [src: functional_dark_matter] The species-count metric (pangenome species sharing the same root OG) is finer. It ranges from 1 to 33 species per OG (median=1, mean=2.2). [src: functional_dark_matter]

A supplementary scoring replaces binary breadth with the continuous metric min(n_species / 20, 1.0) × 0.5. [src: functional_dark_matter] Its rankings correlate highly with the original (Spearman ρ = 0.982). [src: functional_dark_matter] The top lists still differ: top-50 overlap is 62% and top-100 overlap is 58%. [src: functional_dark_matter]

### Within-species biogeography of accessory dark genes

Carrier versus non-carrier genome comparisons could test 151 accessory dark gene clusters across 31 species. [src: functional_dark_matter] Of these, 10 showed significant environmental category enrichment (FDR, false discovery rate, < 0.05). [src: functional_dark_matter] One showed significant AlphaEarth embedding divergence. [src: functional_dark_matter]

Two patterns emerge. Pseudomonas putida dark genes with stress or nitrogen phenotypes are enriched in clinical or human-associated isolates. The report reads this as suggesting roles in host-associated niche adaptation, which is an interpretation. [src: functional_dark_matter] Pseudomonas syringae dark genes with in-planta or stress phenotypes are enriched in plant-associated genomes, consistent with their lab phenotypes. [src: functional_dark_matter]

| Organism | Gene | Phenotype | \|fit\| | Carrier environment | OR | FDR | Tag |
|---|---|---|---|---|---|---|---|
| P. putida | PP_0025 | stress | 4.8 | human_clinical | 27.5 | 7e-6 | [src: functional_dark_matter] |
| P. putida | PP_3434 | nitrogen | 3.1 | human_clinical | 28.6 | 7e-6 | [src: functional_dark_matter] |
| P. putida | PP_0642 | nitrogen | 2.8 | human_clinical | 11.6 | 0.001 | [src: functional_dark_matter] |
| P. putida | PP_3105 | stress | 3.7 | human_assoc | inf | 0.004 | [src: functional_dark_matter] |
| B. thetaiotaomicron | 354052 | stress | 2.4 | human_assoc | 0.17 | 0.005 | [src: functional_dark_matter] |
| P. syringae B728a | Psyr_0167 | in planta | 4.6 | plant_assoc | 11.9 | 0.005 | [src: functional_dark_matter] |
| B. thetaiotaomicron | 350920 | stress | 2.2 | human_assoc | 0.37 | 0.031 | [src: functional_dark_matter] |
| P. putida N2C3 | AO356_11255 | nitrogen | 3.4 | freshwater | inf | 0.031 | [src: functional_dark_matter] |
| K. oxytoca | BWI76_RS15640 | carbon | 2.1 | human_assoc | 0.14 | 0.031 | [src: functional_dark_matter] |
| P. syringae B728a | Psyr_2830 | stress | 3.4 | plant_assoc | 10.9 | 0.031 | [src: functional_dark_matter] |

Module predictions were listed for some of these genes: PF13193 for PP_0025, D-Ala-D-Ala carboxypeptidase for AO356_11255, and Phage tail tape-measure for BWI76_RS15640. [src: functional_dark_matter] Universal breadth was reported for PP_0642, 354052, Psyr_0167, 350920, AO356_11255, BWI76_RS15640 and Psyr_2830. [src: functional_dark_matter]

The project's top-ranked candidate, P. putida N2C3 AO356_11255, has carriers exclusively in freshwater/soil environments. This matches its nitrogen utilization lab phenotype. [src: functional_dark_matter]

### Lab–field concordance

In the Fitness Browser (FB) analysis, pre-registered mappings of experiment condition classes to expected environments gave concordance for 29/47 (61.7%) testable dark gene clusters. Carrier genomes were enriched in the environments predicted by lab phenotype. [src: functional_dark_matter] The strongest concordance was for pH-related genes (100%, n=4) and nitrogen source genes (78%, n=9). [src: functional_dark_matter] See [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]].

Six clusters reached FDR < 0.2. [src: functional_dark_matter]

| Gene | Phenotype (\|fit\|) | Expected environments | Carriers | Non-carriers | OR | FDR | Tag |
|---|---|---|---|---|---|---|---|
| K. oxytoca BWI76_RS15525 | carbon (2.3) | soil, freshwater, plant | 14.3% | 2.5% | 6.6 | 0.069 | [src: functional_dark_matter] |
| K. oxytoca BWI76_RS15535 | carbon (2.2) | soil, freshwater, plant | 14.3% | 2.5% | 6.6 | 0.069 | [src: functional_dark_matter] |
| P. putida N2C3 AO356_12450 | carbon (2.1) | soil, freshwater, plant | 62.5% | 0% | inf | 0.093 | [src: functional_dark_matter] |
| P. putida N2C3 AO356_11255 | nitrogen (3.4) | soil, freshwater, wastewater | 80.0% | 8.3% | 44.0 | 0.093 | [src: functional_dark_matter] |
| P. putida N2C3 AO356_25185 | anaerobic (2.7) | soil, freshwater, animal | 55.6% | 0% | inf | 0.178 | [src: functional_dark_matter] |
| P. putida N2C3 AO356_24150 | nitrogen (3.0) | soil, freshwater, wastewater | 55.6% | 0% | inf | 0.178 | [src: functional_dark_matter] |

AO356_11255, the top candidate, shows the clearest signal. It matches its lab phenotype of strong nitrogen utilization fitness. [src: functional_dark_matter]

### Statistical strength of the concordance

The two tests of the same 29/47 dataset give different strength. A one-sided binomial test of 29/47 against p = 0.5 gives p = 0.072, which the report calls marginal. The Wilson score 95% confidence interval (CI) of [0.474, 0.742] includes 0.50. [src: functional_dark_matter] Fisher's combined probability across all 47 individual Fisher's exact tests gives p = 0.031. The report calls this stronger aggregate evidence that the concordance is non-random. [src: functional_dark_matter] Separately, a binomial sign test on 7/7 correct-direction pre-registered NMDC trait predictions gives p = 0.0078. [src: functional_dark_matter]

### NMDC independent validation

A two-tier taxonomy bridge (gtdb_metadata ncbi_taxid plus taxonomy_dim fallback) mapped 5 of 6 carrier genera to 47 NMDC taxon columns across 6,365 metagenomic samples. [src: functional_dark_matter] All 4 testable pre-registered predictions were confirmed. [src: functional_dark_matter] See [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions]].

| Carrier phenotype | Abiotic variable | rho | n | FDR | Direction | Tag |
|---|---|---|---|---|---|---|
| nitrogen source | total nitrogen content | +0.109 | 1,231 | 2.3e-4 | positive (expected) | [src: functional_dark_matter] |
| nitrogen source | ammonium nitrogen | +0.231 | 1,230 | 8.0e-16 | positive (expected) | [src: functional_dark_matter] |
| pH | pH | +0.157 | 4,366 | 7.4e-25 | positive (expected) | [src: functional_dark_matter] |
| anaerobic | dissolved oxygen | -0.298 | 272 | 1.5e-6 | negative (expected) | [src: functional_dark_matter] |

### Documentation

The phylogenetic breadth and supplementary scoring analyses are documented in 02_gapmind_concordance_phylo.ipynb and 10_review_improvements.ipynb. The species-count variant is in data/scoring_species_count_variant.tsv. [src: functional_dark_matter] The biogeographic analysis is in 03_biogeographic_analysis.ipynb. [src: functional_dark_matter]

## Key Findings: Finding 8: Top 100 prioritized candidates span 22 organisms with 82% …

This part of the report covers the field-side validation of lab fitness phenotypes with NMDC metagenomes, the mapping of lab conditions to environments, and the final multi-axis ranking of 17,344 dark genes. The pre-registered NMDC predictions all held. The report itself says the broader correlation rates are probably inflated by confounding and compositional coupling. [src: functional_dark_matter]

### NMDC abiotic validation

The report calls the NMDC abiotic confirmations independent, because the NMDC metagenomic samples are entirely separate from the pangenome-based carrier analysis. [src: functional_dark_matter] Beyond the pre-registered predictions, 76 of 105 total Spearman correlation tests reached false discovery rate (FDR) < 0.05 (72.4%). [src: functional_dark_matter] The report says this high rate likely reflects confounding. The carrier genera (*Pseudomonas*, *Klebsiella*, *Bacteroides*) are abundant and ubiquitous in NMDC samples, so their abundance correlates broadly with abiotic variables regardless of condition class. [src: functional_dark_matter] The report therefore treats the 4/4 pre-registered abiotic prediction rate as the more meaningful metric, because it tests specific directional hypotheses. [src: functional_dark_matter] See [[concepts/compositional-coupling-in-metagenomic-validation-of-carrier-abundance]] and [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]].

### Condition–environment mappings

The research plan specified 7 condition–environment mappings, including osmotic, temperature, and oxidative stress. [src: functional_dark_matter] The implementation used 6 mappings: stress (consolidating metal, osmotic, and oxidative), carbon source, nitrogen source, pH, motility, and anaerobic. [src: functional_dark_matter] Stress types were consolidated because the Fitness Browser (FB) `expGroup` field uses broad "stress" rather than sub-categorizing stress types. [src: functional_dark_matter] Motility and anaerobic were added because they emerged as prominent condition classes among dark genes with strong fitness effects. [src: functional_dark_matter]

### NMDC trait-condition validation

Using the same genus bridge, carrier-genera abundance was correlated with matching community functional trait scores from NMDC `trait_features` (76 functional_group columns across 6,365 samples). [src: functional_dark_matter] All 7 pre-registered predictions were confirmed (FDR < 10⁻²¹). [src: functional_dark_matter]

| Carrier class | Trait | ρ |
|---|---|---|
| nitrogen-source | nitrogen_fixation | 0.60 [src: functional_dark_matter] |
| nitrogen-source | nitrate_denitrification | 0.52 [src: functional_dark_matter] |
| carbon-source | aerobic_chemoheterotrophy | 0.73 [src: functional_dark_matter] |
| carbon-source | fermentation | 0.59 [src: functional_dark_matter] |
| anaerobic | fermentation | 0.59 [src: functional_dark_matter] |
| anaerobic | iron_respiration | 0.45 [src: functional_dark_matter] |

An additional 441/449 exploratory tests reached FDR < 0.05. [src: functional_dark_matter] The report cautions that these correlations likely reflect compositional coupling rather than independent gene-phenotype validation. Genera abundant in a sample contribute to both carrier abundance and community trait scores. [src: functional_dark_matter] The report ties this analysis to notebooks 04_lab_field_concordance.ipynb and 06_robustness_checks.ipynb. [src: functional_dark_matter]

### Multi-axis prioritization of dark genes

Scoring across 6 evidence axes ranked 17,344 dark genes. The axes were fitness importance, cross-organism conservation, functional inference quality, pangenome distribution, biogeographic signal, and experimental tractability. [src: functional_dark_matter] The top 100 candidates (score range 0.624–0.715) come from 22 organisms. *Shewanella* MR-1 (25 candidates), *P. putida* N2C3 (18), and Marinobacter (9) are most represented. [src: functional_dark_matter] Of the top candidates, 82% have high-confidence functional hypotheses supported by 3+ evidence types, and 85/100 have module-based function predictions. [src: functional_dark_matter] The report's dossiers come from notebook 05_prioritization_dossiers.ipynb. [src: functional_dark_matter]

The report's top 20 genes follow, each row tagged to its claim. Columns are organism, gene, |fit|, condition class, module prediction, domains, pangenome status (acc = accessory) and score. A dash means no module prediction. [src: functional_dark_matter]

| Rank | Organism | Gene | \|fit\| | Condition | Module | Domains | Status | Score |
|---|---|---|---|---|---|---|---|---|
| 1 | P. putida N2C3 | AO356_11255 | 3.4 | nitrogen | D-Ala-D-Ala carboxypeptidase | EamA | acc | 0.715 [src: functional_dark_matter] |
| 2 | Shewanella MR-1 | 202463 | 6.4 | stress | PF01145 | YGGT | core | 0.698 [src: functional_dark_matter] |
| 3 | Shewanella MR-1 | 199738 | 5.5 | nitrogen | K03306 | Gcw_chp, TIGR02001 | core | 0.698 [src: functional_dark_matter] |
| 4 | Shewanella MR-1 | 203545 | 4.0 | nitrogen | K03306 | DUF4124 | core | 0.694 [src: functional_dark_matter] |
| 5 | Shewanella MR-1 | 202450 | 3.9 | nitrogen | K03306 | Gly_transporter | core | 0.693 [src: functional_dark_matter] |
| 6 | P. putida N2C3 | AO356_18320 | 3.8 | motility | PF00460 | MotY_N, OmpA | core | 0.689 [src: functional_dark_matter] |
| 7 | P. fluorescens N1B4 | Pf1N1B4_3696 | 3.7 | pH | PF00361 | DUF3108 | core | 0.687 [src: functional_dark_matter] |
| 8 | Shewanella MR-1 | 201124 | 5.0 | nitrogen | PF01144 | HgmA_N, HgmA_C | core | 0.685 [src: functional_dark_matter] |
| 9 | P. putida N2C3 | AO356_15270 | 5.6 | carbon | PF02589 | LrgB | core | 0.685 [src: functional_dark_matter] |
| 10 | Shewanella MR-1 | 203247 | 4.6 | stress | PF01145 | GBBH-like_N | core | 0.685 [src: functional_dark_matter] |
| 11 | Shewanella MR-1 | 203720 | 4.5 | nitrogen | — | Ser_hydrolase | core | 0.680 [src: functional_dark_matter] |
| 12 | Marinobacter | GFF2506 | 3.4 | stress | ArnT/PqaB | AsmA_2, DUF3971 | core | 0.678 [src: functional_dark_matter] |
| 13 | Shewanella MR-1 | 203026 | 3.5 | carbon | — | AFG1_ATPase | core | 0.677 [src: functional_dark_matter] |
| 14 | Marinobacter | GFF1827 | 3.7 | stress | PF01145 | Bax1-I | core | 0.676 [src: functional_dark_matter] |
| 15 | Shewanella MR-1 | 201809 | 4.4 | stress | — | PG_binding_3, Glyco_hydro_108 | core | 0.674 [src: functional_dark_matter] |
| 16 | Shewanella MR-1 | 201731 | 4.0 | motility | TIGR00254 | ZapC | core | 0.674 [src: functional_dark_matter] |
| 17 | Marinobacter | GFF1367 | 5.7 | stress | PF00270 | IMS | core | 0.672 [src: functional_dark_matter] |
| 18 | Shewanella MR-1 | 202474 | 7.1 | carbon | PF00460 | YggL_50S_bp | core | 0.672 [src: functional_dark_matter] |
| 19 | P. putida N2C3 | AO356_17245 | 3.6 | stress | K00763 | Biotin_lipoyl, HlyD | core | 0.671 [src: functional_dark_matter] |
| 20 | P. putida N2C3 | AO356_08210 | 4.0 | stress | K03808 | DUF3426, zinc_ribbon | core | 0.670 [src: functional_dark_matter] |

The report draws three patterns from the top 10:
- *Shewanella* MR-1 genes 199738, 203545, and 202450 carry K03306 module predictions with different domain architectures. This suggests paralogous members of a conserved nitrogen-responsive system. [src: functional_dark_matter]
- MR-1 genes 202463 and 203247 both predict PF01145 under stress. This points to a stress-responsive membrane protein family (YGGT/GBBH-like). [src: functional_dark_matter]
- The top candidate AO356_11255 is the only accessory gene in the top 10. It has the strongest biogeographic signal (lab-field odds ratio (OR) = 44, NMDC nitrogen correlation). [src: functional_dark_matter]

Related pages: [[entities/shewanella-oneidensis-mr-1]] and [[entities/pseudomonas-putida]]. [src: functional_dark_matter]

## Key Findings: Finding 10: Phylogenetic gaps — which new organisms would most expand dark …

This part of the report turns the dark-gene candidate list into an experimental plan. It asks which organism-by-condition experiments would address the most top-500 dark genes. It also asks which new organisms should get libraries. The report states that 10 random barcode transposon sequencing (RB-TnSeq) experiments cover 45% of the top 500 dark genes. [src: functional_dark_matter] The plan is a computational prioritization. The quoted claims give no experimental results for it.

### Ranking experiments

The report assumes RB-TnSeq libraries already exist for the Fitness Browser (FB) organisms. [src: functional_dark_matter] It ranked organism-condition pairs by the number of top-500 dark-gene candidates each would address. It then applied greedy set-cover optimization. [src: functional_dark_matter] The first priority is Shewanella MR-1 under stress. It addresses 57 dark genes, which is 10.7% of the Top 500. [src: functional_dark_matter] See also [[entities/greedy-weighted-set-cover-organism-selection]].

### Shewanella MR-1 as the top organism

The report calls Shewanella MR-1 the single highest-value organism. Three experiments (stress, nitrogen and carbon) would cover 111 top-500 candidates (20.8%). [src: functional_dark_matter] The report ties this to MR-1's deep condition coverage (121 conditions historically). It also cites 587 scored dark genes and 142 genes with |fit| ≥ 4. [src: functional_dark_matter] More on the organism is on [[entities/shewanella-oneidensis-mr-1]]. The three experiments have these named targets:

- **Stress (57 genes):** Genes 202463 (YGGT domain, |fit|=6.4), 203247 (GBBH-like_N, |fit|=4.6) and 203631 (|fit|=4.5) lead. All three carry PF01145 module predictions. The report suggests this points to a stress-responsive membrane protein family. [src: functional_dark_matter]
- **Nitrogen (31 genes):** The K03306 paralog trio leads: 199738 (Gcw_chp/TIGR02001, |fit|=5.5), 203545 (DUF4124, |fit|=4.0) and 202450 (Gly_transporter, |fit|=3.9). The report proposes comparing single and double mutants to test functional redundancy. [src: functional_dark_matter]
- **Carbon (23 genes):** Genes 202474 (YggL_50S_bp, |fit|=7.1) and 202608 (BcrAD_BadFG, |fit|=7.3) lead. They have the highest fitness magnitudes in the entire top-100. [src: functional_dark_matter]

The second-highest-value organism is *Pseudomonas putida* N2C3. It has 48 genes in the top 500, and stress conditions alone would resolve 23 candidates. [src: functional_dark_matter] See [[entities/pseudomonas-putida]].

### Cross-organism ortholog leverage

The report finds that 101 ortholog groups in the top 500 span 2+ organisms. It says this amplifies the return on each experiment. [src: functional_dark_matter] The widely shared groups it lists are:

| Group | Condition | Organisms (n) |
|---|---|---|
| OG03827 | carbon source | 6: MR-1, Marinobacter, ANA3, PV4, *P. fluorescens* N1B4, *P. simiae* N2E2 [src: functional_dark_matter] |
| OG02907 | nitrogen source | 6: MR-1, *E. coli* Keio, *K. oxytoca*, *P. putida*, *P. fluorescens* N1B4, *P. simiae* N2E3 [src: functional_dark_matter] |
| OG01383 | pH | 5: MR-1, *S. meliloti*, *C. metallidurans*, *P. fluorescens* GW456-L13, *P. putida* N2C3 [src: functional_dark_matter] |
| OG03534 | stress | 5: MR-1, ANA3, *Dinoroseobacter*, PV4, *Synechococcus* [src: functional_dark_matter] |
| OG01997 | stress | 4: MR-1, ANA3, *S. meliloti*, *P. putida* N2C3 [src: functional_dark_matter] |

The report proposes that stress experiments in MR-1 and *P. putida* N2C3 alone would give cross-organism concordance data for OG01997. Adding nitrogen experiments would test OG02907 and OG01383 across multiple genetic backgrounds. [src: functional_dark_matter] Related work is in [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]].

### Taxonomic gaps in the Fitness Browser

The FB collection is heavily skewed toward Gammaproteobacteria, with 21 of 48 organisms and 78% of top-500 dark genes. [src: functional_dark_matter] The report's table gives 417 top-500 genes for Gammaproteobacteria. [src: functional_dark_matter] As a share of 500, 417 is 83.4%, so this table count and the 78% figure do not match. The report does not explain the difference, and both figures are given here as stated. The report grades each group's gap severity as follows. See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]].

| Group | FB organisms | Top-500 genes | Gap severity |
|---|---|---|---|
| Gammaproteobacteria | 21 | 417 | Saturated [src: functional_dark_matter] |
| Betaproteobacteria | 8 | 10 | Moderate [src: functional_dark_matter] |
| Alphaproteobacteria | 5 | 71 | Low [src: functional_dark_matter] |
| Deltaproteobacteria | 5 | 17 | Low [src: functional_dark_matter] |
| Bacteroidetes | 5 | 12 | Low [src: functional_dark_matter] |
| Firmicutes | 1 | 5 | Critical [src: functional_dark_matter] |
| Cyanobacteria | 1 | 2 | Moderate [src: functional_dark_matter] |
| Archaea | 2 | 0 | Severe [src: functional_dark_matter] |
| Actinobacteria | 0 | none given | Critical [src: functional_dark_matter] |
| Epsilonproteobacteria | 0 | none given | High [src: functional_dark_matter] |

The most widespread top-500 dark gene clusters are present in 15+ pangenome species. Their common domain families are TauE (sulfonate export, 7 clusters) [src: functional_dark_matter], DUF444 and Cu-oxidase_4 (5 clusters each) [src: functional_dark_matter], and EamA (4 clusters, including the #1 candidate). [src: functional_dark_matter] DUF484, DUF971 and DUF934 each occur in 3+ clusters. [src: functional_dark_matter] The report notes that these families span phyla not in the FB. It proposes adding organisms from the missing phyla to enable cross-phylum concordance testing. [src: functional_dark_matter]

### Recommended new RB-TnSeq libraries

The report prioritizes new organisms by phylogenetic gap filled, laboratory tractability, overlap with widespread dark gene families, and environmental or biomedical relevance. [src: functional_dark_matter]

1. ***Bacillus subtilis* 168 (Firmicutes).** It has established RB-TnSeq protocols. It would fill the largest phylogenetic gap and allow Gram-positive versus Gram-negative comparisons of DUF484, DUF971 and EamA. [src: functional_dark_matter] The existing FB strain BFirm produced only 5 top-500 genes. The report suggests a purpose-built library with broader condition screening could greatly expand this. [src: functional_dark_matter]
2. ***Streptomyces coelicolor* A3(2) (Actinobacteria).** It is a genetically tractable model that would add an entirely missing phylum. [src: functional_dark_matter] Its genome is 8.7 Mb with ~30% hypothetical genes. It has many biosynthetic gene clusters where dark genes may encode novel enzymatic activities. [src: functional_dark_matter]
3. ***Clostridium difficile* 630 (Firmicutes, Clostridia).** This strict anaerobe would test anaerobic-phenotype dark genes that showed strong NMDC dissolved oxygen correlation. [src: functional_dark_matter] Genetic tools and TnSeq have been established for it. [src: functional_dark_matter]
4. ***Mycobacterium smegmatis* mc²155 (Actinobacteria).** It is a fast-growing non-pathogenic model for *M. tuberculosis* with established Tn-seq. [src: functional_dark_matter]
5. ***Campylobacter jejuni* NCTC 11168.** It would add the missing Epsilonproteobacteria. TnSeq has been applied successfully, and this foodborne pathogen has unusual metabolic requirements. [src: functional_dark_matter]
6. ***Lactobacillus plantarum* WCFS1 (Firmicutes, Bacilli).** This plant- and gut-associated fermentative bacterium has well-developed genetic tools. It would allow testing of carbon-source dark genes. [src: functional_dark_matter]
7. ***Rhodobacter sphaeroides* 2.4.1 (Alphaproteobacteria).** It would strengthen concordance testing for the 71 top-500 Alphaproteobacteria genes. Its metabolic strategy differs from that of *Sinorhizobium meliloti*. [src: functional_dark_matter] It is a photosynthetic alphaproteobacterium capable of phototrophy, aerobic/anaerobic respiration and nitrogen fixation. [src: functional_dark_matter]

The report proposes that the first two additions, *B. subtilis* and *S. coelicolor*, would fill the Firmicutes depth and Actinobacteria absence gaps. Together they would enable cross-phylum testing of the ~100 "universal" dark gene families that currently can only be studied in Proteobacteria. [src: functional_dark_matter]

## Key Findings: Finding 12: Conserved gene neighborhoods and cofit-validated operons …

This part of the report ranks essential dark genes, which lack viable transposon mutants, using evidence that does not need fitness magnitudes. It then adds cross-species synteny and co-fitness validation of operon pairs. The evidence is computational. The report offers it as leads for experiments, not as validated assignments. [src: functional_dark_matter]

### Ranking essential dark genes

Essential dark genes represent 55% of the experimentally actionable dark matter, but they score poorly in the fitness-centric NB05 framework. [src: functional_dark_matter] The report therefore ran a separate ranking of all 9,557 essential dark genes. It used five dimensions: gene neighbor context (0.25), cross-organism conservation (0.20), phylogenetic breadth (0.20), domain annotations (0.15) and CRISPRi (CRISPR interference) tractability (0.20). [src: functional_dark_matter] All top-50 candidates have high-confidence functional hypotheses derived from operon context. [src: functional_dark_matter] Each top candidate carries a CRISPRi design with target organism, sgRNA target, growth condition, expected phenotype and validation strategy. [src: functional_dark_matter]

The top ten candidates are:

| Rank | Organism | Locus | Score | Domains | Operon context |
|---|---|---|---|---|---|
| 1 | E. coli Keio | 14796 | 0.875 | YbeY, TIGR00043 | ion transport + NTP hydrolase [src: functional_dark_matter] |
| 2 | Shewanella MR-1 | 200382 | 0.874 | RimP_N, DUF150_C | tRNA-Met + NusA [src: functional_dark_matter] |
| 3 | K. oxytoca | BWI76_RS08540 | 0.865 | OmpA, TIGR02802 | TolB + CpoB (cell division) [src: functional_dark_matter] |
| 4 | P. putida N2C3 | AO356_29395 | 0.838 | Peptidase_M20 | ABC (ATP-binding cassette) transporter + peptidase [src: functional_dark_matter] |
| 5 | Shewanella MR-1 | 201473 | 0.835 | EarP, TIGR03837 | EF-P + flavodoxin [src: functional_dark_matter] |
| 6 | E. coli Keio | 14768 | 0.833 | DUF493 | lipoate biosynthesis + PBP5 [src: functional_dark_matter] |
| 7 | Shewanella MR-1 | 200359 | 0.833 | YbeY, TIGR00043 | CorC + PhoH [src: functional_dark_matter] |
| 8 | P. putida | PP_1910 | 0.828 | YceD | 50S ribosomal L32 + PlsX [src: functional_dark_matter] |
| 9 | P. putida | PP_5002 | 0.828 | GBBH-like_N | HslVU protease + PhaC1 [src: functional_dark_matter] |
| 10 | E. coli Keio | 11474 | 0.825 | DUF4109 | tRNA-Met + translation [src: functional_dark_matter] |

All ten are rated high confidence. [src: functional_dark_matter] For the rank 1 gene, the report predicts an ion transport function from its operon with an annotated ion transport gene. It proposes CRISPRi knockdown in E. coli Keio on varied carbon and nitrogen sources, with OD600 monitoring for growth defects. [src: functional_dark_matter]

### Operon neighbors as evidence

Of 57,011 dark genes, 30,190 (52.9%) share a predicted operon with an annotated gene. The criteria are the same strand and a gap under 300 bp. [src: functional_dark_matter] The mean annotated neighbor fraction of dark genes is 63.6%, below the genome-wide 75% baseline. The report reads this as dark genes co-localizing with other dark genes, consistent with unannotated operonic clusters. [src: functional_dark_matter]

One figure carries little weight. 97.2% of dark genes have an annotated neighbor within a 5-gene window, but this is expected by chance given the 75% annotation rate. [src: functional_dark_matter] Proximity-based hypotheses are leads for testing. Published operon predictors (DOOR, ProOpDB) use signals beyond strand and gap distance. [src: functional_dark_matter]

### Synteny and co-fitness validation

Synteny and co-fitness together give independent support for many operon pairs, and 998 pairs pass both tests. [src: functional_dark_matter]

**Synteny.** The analysis tested 21,011 dark gene–operon partner pairs that have ortholog groups for both genes. It covered up to 47 Fitness Browser organisms. [src: functional_dark_matter] Of these, 17,058 pairs have a conserved neighborhood in at least one other organism. [src: functional_dark_matter] 10,150 pairs are conserved in ≥3 organisms, which the report calls STRING-like evidence of functional linkage. [src: functional_dark_matter] The median conservation score is 0.95. When orthologs co-occur in another genome, they almost always remain neighbors. [src: functional_dark_matter]

**Co-fitness.** This test used 32,075 non-essential operon pairs and the Fitness Browser cofit table (top-20 partners, 13.6M rows). [src: functional_dark_matter] The tiered score is 1.0 for mutual top-5 cofit, 0.75 for one-directional top-5, 0.50 for mutual top-20 with cofit > 0.5, and 0.25 for one-directional top-20. [src: functional_dark_matter] Of the pairs, 2,899 show co-fitness evidence (rank ≤ 20). [src: functional_dark_matter] 1,129 of them are mutual top-5 pairs, which the report calls the strongest possible co-expression signal from the Fitness Browser. [src: functional_dark_matter]

**Combined.** 998 pairs are "double-validated", with conserved synteny (>30%) and co-fitness score ≥ 0.5. The report calls these its highest-confidence functional predictions. [src: functional_dark_matter] Adding this evidence improved scores for 10,757 fitness-active dark genes and 4,028 essential dark genes, and some candidates rose significantly in rank. [src: functional_dark_matter] Co-fitness is unavailable for essential genes, because no viable mutants means no fitness profiles. [src: functional_dark_matter]

### Cross-check and roadmap

The report cross-checked the NB05 top 100 candidates against Paramvir Dehal's prior module-based predictions. 85 of 100 had existing predictions, and all agreed with the report's independent inference. The report calls this strong orthogonal validation. [src: functional_dark_matter]

The evidence-weighted roadmap ranks MR-1 first, with 61 candidates (47 fitness-active + 14 essential), 83 synteny-validated pairs and 31 cofit-validated pairs. [src: functional_dark_matter] P. putida N2C3 follows with 35 candidates [src: functional_dark_matter], then P. putida with 24. [src: functional_dark_matter] Four experiments achieve 45% coverage of the top 300 candidates. [src: functional_dark_matter]

### Limits of the synteny analysis

The synteny analysis uses a 5-gene window and only Fitness Browser organisms (48 genomes). [src: functional_dark_matter] STRING v12 and EFI-GNT analyze thousands of genomes. They also use more sophisticated scoring, including gene fusion and shared phylogenetic profiles. [src: functional_dark_matter] The report says its conservation scores are lower bounds, because broader taxonomic sampling would likely show higher conservation. [src: functional_dark_matter] See also [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]] and [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].

## Key Findings: Finding 14: Pangenome-scale conservation × hypothesis classification …

This part of the report classifies all dark genes by how much evidence they have. It measures how widely their ortholog groups are conserved across the pangenome. It then uses these results to choose a small set of organisms for experiments. [src: functional_dark_matter]

### Darkness spectrum

The census assigns all 57,011 dark genes to five tiers using 6 binary evidence flags: domain annotation, ortholog group, function prediction, co-fitness partner, fitness/essentiality phenotype and pangenome context. [src: functional_dark_matter] See [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]]. The tiers run from no evidence to nearly characterized. [src: functional_dark_matter]

| Tier | Name | Genes | Interpretation |
|---|---|---:|---|
| T1 | Void | 4,273 | No evidence of any kind [src: functional_dark_matter] |
| T2 | Twilight | 12,282 | Single clue (domain or ortholog only) [src: functional_dark_matter] |
| T3 | Dusk | 16,103 | Two converging hints [src: functional_dark_matter] |
| T4 | Penumbra | 22,500 | Substantial evidence, testable hypotheses [src: functional_dark_matter] |
| T5 | Dawn | 1,853 | 5–6 evidence lines, nearly characterized [src: functional_dark_matter] |

### Pangenome conservation

Earlier conservation calls were too coarse to separate dark genes. The report says the coarse eggNOG breadth classification (99.9% "universal") and the sparse 48-organism Fitness Browser sampling (37/48 Proteobacteria) fail to meaningfully distinguish conservation patterns among dark genes. [src: functional_dark_matter]

To fix this, NB11b queried the full 27,690-species GTDB r214 pangenome. It exploded eggNOG_OGs annotations across 93.5M gene clusters and matched 11,774 dark gene root OGs. [src: functional_dark_matter] Propagating root_og assignments within Fitness Browser ortholog groups recovered another 5,206 dark genes (9.1%). [src: functional_dark_matter] Together these steps raised pangenome conservation coverage from 32,791 (57.5%) to 37,997 (66.6%) dark genes. [src: functional_dark_matter] Species counts range from 1 to 27,482 (median 135, mean 2,128), and phylum counts range from 1 to 142. [src: functional_dark_matter]

The 11,774 root OGs fall into 8 taxonomic tiers, based on the narrowest rank containing all member species. [src: functional_dark_matter] Mobile elements are detected through phylogenetic patchiness, meaning presence in distant phyla but few species per phylum. [src: functional_dark_matter]

| Tier | Share of OGs |
|---|---:|
| kingdom | 55.9% [src: functional_dark_matter] |
| class | 11.0% [src: functional_dark_matter] |
| family | 10.5% [src: functional_dark_matter] |
| genus | 6.9% [src: functional_dark_matter] |
| mobile | 6.5% [src: functional_dark_matter] |
| phylum | 4.8% [src: functional_dark_matter] |
| order | 3.9% [src: functional_dark_matter] |
| species | 0.5% [src: functional_dark_matter] |

Over half of dark-gene OGs are pan-bacterial. The report reads this as a fundamental limitation in understanding broadly conserved biology, not a minor annotation gap. [src: functional_dark_matter] See [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]].

At the gene level, 57,011 dark genes include 19,014 Fitness Browser-only fallback assignments. Their tiers are kingdom 51.4%, species 29.8%, genus 6.2%, class 4.0%, family 3.5%, mobile 1.9%, phylum 1.9% and order 1.3%. [src: functional_dark_matter] These gene-level shares and the OG-level shares above describe different populations and are stated separately. [src: functional_dark_matter]

### Hypothesis status and importance ranking

Each dark gene is also placed in a hypothesis status tier. Strong testable hypotheses are 6.0% of dark genes. They rest on module predictions with EC (Enzyme Commission) numbers, high cross-organism concordance, high-confidence GapMind matches, or named domains with strong fitness. [src: functional_dark_matter] Weak leads are 52.5%. They rest on DUF-only domains, bare module predictions, medium/low GapMind, strong fitness without annotation, or named domains without fitness. [src: functional_dark_matter] True knowledge gaps are 41.5% and have zero functional evidence of any kind. [src: functional_dark_matter]

The importance score `conservation × ignorance` ranks all 11,774 dark-gene OGs. The report describes it as tier-adjusted conservation score + log₂-scaled species fraction × ignorance multiplier. [src: functional_dark_matter] Kingdom-level true knowledge gaps rank highest, and species-specific strong hypotheses rank lowest. [src: functional_dark_matter] The top OGs are COG0468 (27,427 species, 142 phyla; true knowledge gap), COG0443 (27,279 species; true knowledge gap) and COG0172 (27,431 species; weak lead). [src: functional_dark_matter]

### Covering sets for organism choice

Greedy weighted set-cover over the 16,488 scored dark genes picks 42 organisms from 28 genera that cover 95% of total priority value. [src: functional_dark_matter] MR-1 ranks first with 587 genes, and 32 organisms suffice for 80% coverage. [src: functional_dark_matter] See [[entities/greedy-weighted-set-cover-organism-selection]] and [[entities/shewanella-oneidensis-mr-1]].

A conservation-weighted covering set of 42 organisms covers 95.6% of total importance-weighted priority across 28,584 high-priority dark genes. [src: functional_dark_matter] It selects organisms by sum(importance) × tractability × phylo_bonus, and phylo_bonus penalizes genus-redundant selections. [src: functional_dark_matter] The first 10 organisms cover 31% of priority. [src: functional_dark_matter]

- Sinorhizobium meliloti ranks first, with 1,630 genes and 195 kingdom-level gaps. [src: functional_dark_matter]
- Pseudomonas putida follows, with 1,043 genes and 172 kingdom gaps. [src: functional_dark_matter]
- S. oneidensis MR-1 contributes 805 genes and 105 kingdom gaps. [src: functional_dark_matter]
- Bacteroides thetaiotaomicron has 1,382 genes and the highest raw count of 267 kingdom gaps. 0.3 tractability deprioritizes it. [src: functional_dark_matter]

### Extended set beyond the Fitness Browser

To reduce the Proteobacteria-heavy sampling, NB11c mapped genus-level OG membership for 25 non-Fitness Browser organisms across the full pangenome. This gave 24 genera and 53,970 genus-OG pairs in 2.9 min. [src: functional_dark_matter] Using all 73 candidates gives a 50-organism set covering 98.7% of OGs across 6 phyla. The Fitness Browser-only set has 41 organisms covering 100% across 4 phyla. [src: functional_dark_matter] At N=5 organisms, coverage reaches 57.7%, against 38.1% for the Fitness Browser-only set (reported as +19.6%). [src: functional_dark_matter] See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]].

The extended set selects 16 non-Fitness Browser organisms. [src: functional_dark_matter] P. aeruginosa PAO1 leads them with 3,713 OGs and tractability 0.8. [src: functional_dark_matter] V. cholerae N16961 (1,049 OGs) and B. cenocepacia K56-2 (956 OGs) are also selected. [src: functional_dark_matter] M. tuberculosis H37Rv ranks #6 and adds 131 new OGs from Actinomycetota. [src: functional_dark_matter] C. jejuni ranks #48 and represents Campylobacterota. [src: functional_dark_matter]

B. subtilis and S. aureus were not selected, because their OGs are subsets of coverage that Pseudomonadota already provide. The report says they remain valuable for studying genes in native Gram-positive genomic context. [src: functional_dark_matter]

### Per-organism action plans

Plans split the genes into 14,450 hypothesis-bearing genes and 2,038 darkest genes. The hypothesis-bearing genes get specific condition recommendations from fitness data, neighbor context or module predictions. The darkest genes need broad phenotypic screens. [src: functional_dark_matter] The plans flag 8,900 essential genes for CRISPRi (CRISPR interference) approaches. [src: functional_dark_matter] See [[entities/crispr-interference-knockdown]].

Recommended experiments are CRISPRi knockdown for essential genes in tractable organisms, condition-specific TnSeq (transposon sequencing) for fitness-active genes, and a broad phenotypic screen for true knowledge gaps. [src: functional_dark_matter] Top conditions come from fitness data or keyword inference. [src: functional_dark_matter] The report ties the spectrum, covering set and action plans to notebook 09_final_synthesis.ipynb. [src: functional_dark_matter]

## Key Findings; Experimental Recommendations

Bakta cross-references reclassify most dark genes, and two prioritization routes give different experimental recommendations. [src: functional_dark_matter] The Bakta results are database cross-references that the report reads as validation. The recommendations are the report's own proposals. [src: functional_dark_matter]

### Bakta reannotation of dark genes

Bakta v1.12.0 (DB v6.0) annotations for 132.5M pangenome cluster representatives were cross-referenced against the 57,011-gene dark catalog. [src: functional_dark_matter] Of 39,532 dark genes with pangenome links, Bakta reclassifies 33,105 (83.7%) as not hypothetical. Its PSC/PSCC pipeline assigns product descriptions where the [[entities/fitness-browser]] had only "hypothetical protein." [src: functional_dark_matter] This is 58.1% of all dark genes. [src: functional_dark_matter]

All 100 top prioritized candidates gain Bakta product descriptions. [src: functional_dark_matter] Examples:
- MR-1 rank 8: Homogentisate 1,2-dioxygenase HmgA. [src: functional_dark_matter]
- MR-1 ranks 13/16: cell division proteins ZapE/ZapC. [src: functional_dark_matter]
- MR-1 rank 26: N-acetylglucosamine kinase. [src: functional_dark_matter]
- Keio rank 31: BolA family iron metabolism protein IbaG. [src: functional_dark_matter]

The report reads these as independent validation of the experimental prioritization. It says the dark genes with the strongest fitness effects tend to be annotated in UniProt but absent from the Fitness Browser's annotation vintage. [src: functional_dark_matter]

Bakta's AMRFinderPlus (antimicrobial resistance, AMR) assigns AMR annotations to 5 dark genes. [src: functional_dark_matter]
- MerF mercury resistance transport in Marinobacter. [src: functional_dark_matter]
- YbtP yersiniabactin transporter in *K. oxytoca*. [src: functional_dark_matter]
- Asr acid resistance protein in *K. oxytoca*. [src: functional_dark_matter]
- HdeD-GI heat resistance membrane protein in *P. stutzeri*. [src: functional_dark_matter]
- An S8 family peptidase in PV4. [src: functional_dark_matter]

6,427 genes remain hypothetical in both the Fitness Browser and Bakta. Many still gain cross-references that could support literature mining: UniRef50 links (79.4%), UniParc/UniRef100 (69.1%) and RefSeq (62.4%). [src: functional_dark_matter] Adding `has_bakta_annotation` as a 7th evidence flag changed the darkness tier of 18,019 genes. The largest shifts were from T4 Penumbra to T5 Dawn, as genes gained their final missing evidence line. [src: functional_dark_matter]

### Two prioritization routes

Of 57,011 dark genes across 48 bacteria, 17,344 have experimentally measurable phenotypes. These are either strong fitness defects (|fit| ≥ 2 in at least one condition) or essentiality, meaning no viable transposon mutants. [src: functional_dark_matter] The report says that convergence of fitness phenotype, conservation, co-regulation, domain structure, gene neighborhood and cross-organism concordance identifies a subset that is both important and interpretable. [src: functional_dark_matter]

Route A is evidence-weighted. It scores each dark gene on 6 dimensions, using data from the 48 Fitness Browser organisms. The weights are fitness importance 0.25, conservation 0.20, inference 0.20, pangenome 0.15, biogeographic 0.10 and tractability 0.10. [src: functional_dark_matter] Route B queries the full 27,690-species GTDB r214 pangenome. It measures the taxonomic breadth of each dark-gene ortholog group (OG) over a species range of 1–27,482. It classifies each OG by taxonomic tier and hypothesis status, then ranks by importance = conservation × ignorance. [src: functional_dark_matter]

| | Route A | Route B |
|---|---|---|
| Top organism | MR-1, with deep condition coverage [src: functional_dark_matter] | *S. meliloti*, with 1,630 OGs and 195 kingdom-level gaps [src: functional_dark_matter] |
| Optimization | Σ(composite_score) × tractability × phylo_diversity [src: functional_dark_matter] | Σ(importance) × tractability × phylo_bonus [src: functional_dark_matter] |
| Organisms selected | 42 (28 genera), 95% of composite priority [src: functional_dark_matter] | 42 (28 genera), 95.6% of importance-weighted priority [src: functional_dark_matter] |
| Key strength | Condition-specific protocols and testable hypotheses [src: functional_dark_matter] | Broadly conserved true knowledge gaps invisible to evidence-based scoring [src: functional_dark_matter] |
| Best for | Targeted RB-TnSeq (random barcode transposon sequencing) under predicted conditions [src: functional_dark_matter] | Broad phenotypic screens for fundamentally unknown genes [src: functional_dark_matter] |

The routes share 39 organisms. Route A uniquely selects Dda3937, Ddia6719 and Miya. Route B uniquely selects Kang, Methanococcus_JJ and Methanococcus_S2. [src: functional_dark_matter]

The report recommends Route A for targeted experiments on genes where convergent evidence gives a testable hypothesis and predicted conditions. [src: functional_dark_matter] It recommends Route B for discovery experiments on broadly conserved genes with the least functional knowledge. [src: functional_dark_matter]

### Top Route A candidates

| Rank | Gene | Organism | Score | Hypothesis and top condition |
|---|---|---|---|---|
| 1 | AO356_11255 | *P. putida* N2C3 | 0.715 | D-alanyl-D-alanine carboxypeptidase (EC 3.4.16.4); nitrogen, fit=3.4. Supported by a module prediction, an EamA domain, the strongest biogeographic signal (lab-field odds ratio OR=44) and an NMDC nitrogen correlation. [src: functional_dark_matter] |
| 2 | 202463 | *S. oneidensis* MR-1 | 0.698 | Stress-responsive membrane protein (PF01145); stress, fit=6.4, the highest fitness magnitude among top candidates. It has a YGGT domain and a co-regulated module. [src: functional_dark_matter] |
| 3 | 199738 | MR-1 | 0.698 | K03306 family (nitrogen metabolism); nitrogen, fit=5.5. It has paralogs 203545 and 202450, so comparing mutants tests functional redundancy. [src: functional_dark_matter] |
| 4 | 203545 | MR-1 | 0.694 | K03306 family with a DUF4124 domain; nitrogen, fit=4.0. It shares a module with 199738 but has a different domain, which suggests subfunctionalization. [src: functional_dark_matter] |
| 5 | 202450 | MR-1 | 0.693 | K03306 family with a Gly_transporter domain; nitrogen, fit=3.9. This suggests a nitrogen/amino acid link. [src: functional_dark_matter] |

### Top Route B candidates

The top three Route B root OGs are all kingdom-tier true knowledge gaps with importance 23.9. All span 142 phyla. [src: functional_dark_matter]
- COG0468 spans 27,427 species. It is pan-bacterial and present in virtually all sequenced genomes. [src: functional_dark_matter]
- COG0443 spans 27,279 species. It is pan-bacterial and functionally uncharacterized. [src: functional_dark_matter]
- COG0491 spans 27,393 species. It is pan-bacterial, with zero evidence across all inference layers. [src: functional_dark_matter]

The report suggests Route A cannot see these genes. They may be essential under all conditions, so they would produce no differential fitness signal. [src: functional_dark_matter] This is a suggestion, not a measured result. [src: functional_dark_matter]

### Essential dark genes and CRISPRi

For essential dark genes with no viable knockout mutants, the report proposes CRISPR interference (CRISPRi) knockdown. It would use gene-neighborhood context, cross-species conservation and domain structure. [src: functional_dark_matter]
- *E. coli* K-12 gene 14796 ranks first (score 0.875). It has a YbeY domain, is conserved in 5+ phyla, sits in a synteny-confirmed operon, and is predicted to mediate ion transport. [src: functional_dark_matter]
- MR-1 gene 200382 ranks second (score 0.874). It has RimP_N/DUF150_C domains and is predicted to be a ribosome assembly factor in a conserved neighborhood. [src: functional_dark_matter]
- *K. oxytoca* BWI76_RS08540 ranks third (score 0.865). It has OmpA/TIGR02802 domains and is predicted to act in cell division. It is conserved across Enterobacteriaceae. [src: functional_dark_matter]

The report attributes these high scores to several converging lines. The genes have detectable domains and belong to widely conserved OGs. They sit in conserved neighborhoods with annotated partners. They are in organisms amenable to CRISPRi. [src: functional_dark_matter]

## Experimental Recommendations: Which organisms and why

This part of the report picks organisms for experiments in two ways. Route A selects by a composite of priority score, tractability and phylogenetic diversity. [src: functional_dark_matter] Route B selects by conservation-weighted importance, which favours conservation breadth over condition-specific evidence depth. [src: functional_dark_matter] Both greedy set-cover selections choose 42 organisms and cover about 95% of their respective priority value. [src: functional_dark_matter] Both draw only on Fitness Browser (FB) organisms, so they are phylogenetically biased, and the report proposes an extended list of 73 organisms to address this. [src: functional_dark_matter] See also [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]] and [[entities/greedy-weighted-set-cover-organism-selection]].

### Route A: hypothesis-driven selection

A greedy weighted set-cover algorithm selected 42 organisms (28 genera) covering 95% of total priority value. It optimizes composite priority score × tractability × phylogenetic diversity. [src: functional_dark_matter] The first five organisms are:

| Rank | Organism | Genes | Tractability | Stated reason |
|---|---|---|---|---|
| 1 | *Shewanella oneidensis* MR-1 | 587 | 0.8 | 121 historical conditions; 172 T5 Dawn and 257 T4 Penumbra genes [src: functional_dark_matter] |
| 2 | *Pseudomonas fluorescens* N1B4 | 624 | 0.7 | Most additional uncovered genes after MR-1, including carbon/nitrogen source panels (215 genes) and membrane stress (77 genes) [src: functional_dark_matter] |
| 3 | *Sinorhizobium meliloti* | 570 | 0.6 | Alphaproteobacteria; 316 T4 Penumbra and 90 T5 Dawn genes [src: functional_dark_matter] |
| 4 | *Escherichia coli* K-12 (Keio) | 368 | 0.9 | Highest tractability; 259 hypothesis-bearing genes immediately testable; 205 essential genes ideal for CRISPRi (CRISPR interference) [src: functional_dark_matter] |
| 5 | *Klebsiella oxytoca* | 396 | 0.65 | Enterobacteriaceae genes not in *E. coli*, including top essential candidate BWI76_RS08540 (score 0.865) [src: functional_dark_matter] |

MR-1 has 544 dark genes with specific stress, nitrogen or carbon condition recommendations. The report calls it the single highest-impact organism, with 25/100 top fitness-active candidates. [src: functional_dark_matter] See [[entities/shewanella-oneidensis-mr-1]].

### Route B: conservation-weighted selection

A conservation-weighted set cover selected 42 organisms covering 95.6% of total importance-weighted priority. It optimizes Σ(importance) × tractability × phylo_bonus, where OG means ortholog group. [src: functional_dark_matter] The first 10 organisms cover 31% of importance-weighted priority, with 9,014 genes across 10 genera. [src: functional_dark_matter]

| Rank | Organism | OGs | Kingdom gaps | Tractability | Stated reason |
|---|---|---|---|---|---|
| 1 | *S. meliloti* | 1,630 | 195 | 0.6 | Its dark genes span the most kingdom-level true knowledge gaps, which are broadly conserved genes with zero functional evidence [src: functional_dark_matter] |
| 2 | *Pseudomonas putida* | 1,043 | 172 | 0.8 | High tractability with deep coverage of conserved unknowns [src: functional_dark_matter] |
| 3 | *S. oneidensis* MR-1 | 805 | 105 | 0.8 | Third rather than first as in Route A, because Route B weights conservation breadth over condition-specific evidence depth [src: functional_dark_matter] |
| 4 | *Bacteroides thetaiotaomicron* | 1,382 | 267 | 0.3 | Low tractability deprioritizes it, but it is critical for Bacteroidota coverage [src: functional_dark_matter] |
| 5 | *Klebsiella michiganensis* | 568 | 65 | 0.65 | Enterobacteriaceae depth beyond *E. coli* [src: functional_dark_matter] |

The report describes the 1,382 OGs of *B. thetaiotaomicron* as the highest raw OG count of any organism. [src: functional_dark_matter] That conflicts with the 1,630 OGs it lists for *S. meliloti*. [src: functional_dark_matter]

### Taxonomic bias and the extended organism list

Both covering sets use only the 48 FB organisms. Of these, 37/48 are Pseudomonadota, and the only other phyla are Bacteroidota (4), Cyanobacteriota (1) and Halobacteriota (2). [src: functional_dark_matter] Bacillota (Firmicutes), Actinomycetota (Actinobacteria) and Campylobacterota have zero FB representation. [src: functional_dark_matter] Kingdom-level OGs make up 55.9% of dark gene OGs. They cannot be addressed experimentally in their non-Proteobacterial hosts using FB organisms alone. [src: functional_dark_matter]

To address this, the report curated an extended list of 73 organisms: the 48 FB organisms plus 25 literature-curated organisms with published TnSeq (transposon sequencing) or CRISPRi resources. [src: functional_dark_matter] The additions are:

- Bacillota (6): *B. subtilis* 168, *S. aureus* USA300, *S. pneumoniae* TIGR4, *C. difficile* R20291, *E. faecium* and *L. monocytogenes* EGD-e, with TnSeq + CRISPRi. [src: functional_dark_matter]
- Actinomycetota (2): *M. tuberculosis* H37Rv and *C. glutamicum* ATCC 13032, with TnSeq + CRISPRi. [src: functional_dark_matter]
- Campylobacterota (2): *C. jejuni* NCTC 11168 and *H. pylori* 26695, with TnSeq. [src: functional_dark_matter]
- Pseudomonadota (15): *P. aeruginosa* PAO1, *Salmonella* 14028s, *V. cholerae* N16961, *A. baumannii* 17978 and 11 others, with TnSeq/CRISPRi. [src: functional_dark_matter]

The report proposes that adding these organisms to Route B would allow kingdom-level dark gene OGs to be characterized in native Gram-positive, Actinobacterial and Campylobacterial contexts. [src: functional_dark_matter] This requires a Spark query mapping each non-FB genome to dark gene root_ogs via the pangenome, which extends the NB11b pipeline. [src: functional_dark_matter]

### Experimental action plan

The plan has three gene classes, each with its own method.

- **Hypothesis-bearing genes.** The plan identifies 14,450 across all 42 organisms. Each has at least one condition recommendation from fitness data, module co-regulation or gene neighborhood context. The recommended experiment is targeted RB-TnSeq (random barcode transposon sequencing) or CRISPRi under the predicted condition. [src: functional_dark_matter] Two examples are MR-1:202463, a stress-responsive YGGT-domain gene to test under oxidative, osmotic and heat stress [src: functional_dark_matter], and the K03306 paralog trio (199738/203545/202450), to test under nitrogen limitation with single and double mutant comparisons. [src: functional_dark_matter]
- **Darkest genes.** The plan identifies 2,038 T1 Void or T2 Twilight genes across all 42 organisms. They have detectable fitness phenotypes but no converging evidence for a specific condition. [src: functional_dark_matter] The recommendation is a broad RB-TnSeq screen following the standard FB protocol of ~50-100 conditions. *E. coli* K-12 alone has 109 such genes. [src: functional_dark_matter]
- **Essential genes.** The covering set contains 8,900 essential genes, which cannot be studied by transposon knockout. [src: functional_dark_matter] The recommended approach is CRISPRi knockdown, using Mobile-CRISPRi for non-model organisms, with growth curves under standard and stress conditions. The top 50 essential candidates have specific designs in NB07. [src: functional_dark_matter]

### Proposed campaigns

Three Route A experiments are proposed:

1. An MR-1 stress screen with RB-TnSeq under 5 stress conditions (oxidative, osmotic, metal, heat, pH). It addresses 161 hypothesis-bearing dark genes, including the #2 overall candidate 202463 (fit=6.4 under stress). [src: functional_dark_matter]
2. An MR-1 nitrogen screen with RB-TnSeq under nitrogen limitation and amino acid supplements. It addresses the K03306 paralog family (3 genes, fits 3.9–5.5) and 74 total dark genes. [src: functional_dark_matter]
3. An *E. coli* K-12 CRISPRi experiment knocking down the top 20 essential dark genes with growth curves. It uses the highest-tractability organism (0.9) and mature tools, with Keio:14796 (YbeY domain, score 0.875) as top target. [src: functional_dark_matter]

For Route B, the report recommends broad phenotypic screens with diverse condition panels, because the target genes are true knowledge gaps without condition predictions. [src: functional_dark_matter] For labs focused on novel function discovery rather than hypothesis testing, the report argues that the Route B ordering maximizes the probability of uncovering completely new biology. That ordering starts with *S. meliloti* (195 kingdom-level gaps), *P. putida* (172) and MR-1 (105). [src: functional_dark_matter] The report calls the two campaigns complementary. Route A gives mechanistic insight where hypotheses exist, and Route B discovers function where none exist. The full plans are in data/experimental_action_plan.tsv (Route A) and data/conservation_experiment_plans.tsv (Route B). [src: functional_dark_matter]

## Results: Step 3: Testing whether lab phenotypes match nature (NB03–NB04)

This part of the report builds a single census of dark genes across the 48 Fitness Browser (FB) organisms. [src: functional_dark_matter] It then adds three inference layers: GapMind gap-filling, cross-organism concordance and phylogenetic breadth. [src: functional_dark_matter] A biogeographic test of ecological relevance follows. [src: functional_dark_matter] The part ends with a composite ranking of candidates. [src: functional_dark_matter]

### Census of dark genes

The census integrates four earlier observatory projects (fitness_modules, essential_genome, conservation_vs_fitness, module_conservation) with direct Fitness Browser queries. [src: functional_dark_matter] The report says this integration was needed because earlier projects answered different questions and stored results in different formats, so no unified catalog existed. [src: functional_dark_matter] See [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]].

The census identifies 57,011 dark genes, which is 24.9% of 228,709 total genes. [src: functional_dark_matter] The census links these genes to other evidence as follows:

- 39,532 (69.3%) link to the pangenome. [src: functional_dark_matter]
- 6,142 (10.8%) belong to independent component analysis (ICA) fitness modules with function predictions. [src: functional_dark_matter]
- 7,787 (13.7%) show strong fitness effects (|fit| ≥ 2). [src: functional_dark_matter]
- 9,557 (16.8%) are essential. [src: functional_dark_matter]

The report counts 17,344 dark genes with measurable phenotypes (fitness or essentiality). It concludes that one quarter of bacterial genes remain dark but that the problem is tractable. [src: functional_dark_matter] The intersection that matters most for biogeographic analysis, accessory dark genes with strong fitness, is 511 genes. [src: functional_dark_matter]

### Additional inference layers

GapMind gap-filling asks whether dark genes encode missing enzymatic steps in nearly-complete metabolic pathways. [src: functional_dark_matter] The report queried 305M GapMind pathway rows, filtered to 44 FB-linked species. It found 1,256 organism-pathway pairs where dark genes co-occur with pathway gaps. [src: functional_dark_matter] See [[concepts/metabolic-pathway-gap-filling-by-unannotated-genes]].

Cross-organism concordance tests whether orthologs of a dark gene show fitness effects under the same conditions in several organisms. [src: functional_dark_matter] The report tested 65 ortholog groups (OG) present in 3+ FB organisms. Motility-related dark genes showed the strongest concordance, which is consistent with conserved but incompletely annotated chemotaxis machinery. [src: functional_dark_matter] The report concludes that dark-gene phenotypes are reproducible across organisms and are not single-species artifacts. [src: functional_dark_matter] See [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]].

Phylogenetic breadth asks how widespread each dark gene family is across the full pangenome of 27,690 species, not only the 48 FB organisms. [src: functional_dark_matter] Mapping 30,756 gene clusters to taxonomy showed that species count (1–33) gives finer resolution than the coarse universal/clade-restricted classification. [src: functional_dark_matter] The report interprets broadly conserved dark genes as likely fundamental and clade-restricted ones as likely niche-specific. [src: functional_dark_matter] This is an interpretation, not a measured result. See [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]].

### Biogeographic test of ecological relevance

The biogeographic analysis tests whether genomes carrying stress-responsive dark genes come from stressful environments. This assesses whether the lab phenotypes are ecologically relevant. [src: functional_dark_matter] Within-species carrier versus non-carrier tests, controlling for phylogeny, found significant environmental enrichment in 10/137 clusters (false discovery rate, FDR, < 0.05). [src: functional_dark_matter] They found AlphaEarth embedding divergence in 1/67 clusters. [src: functional_dark_matter] The directional lab-field concordance rate was 61.7% (29/47 testable clusters), exceeding chance. [src: functional_dark_matter] See [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]].

Independent validation with NMDC confirmed all 4 pre-registered predictions. Nitrogen carriers correlated with nitrogen-rich environments, and pH carriers with pH-extreme environments. [src: functional_dark_matter] In that validation, 76/105 abiotic correlations reached significance. [src: functional_dark_matter] The report states that compositional coupling inflates the NMDC signal. It still argues that directional concordance across independent datasets supports the inference that lab fitness phenotypes reflect real ecological function. [src: functional_dark_matter] The report concludes that genes important under stress in the lab tend to come from organisms found in stressful environments. It says this validates fitness data as a proxy for ecological function. [src: functional_dark_matter] See [[concepts/compositional-coupling-in-metagenomic-validation-of-carrier-abundance]].

### Composite prioritization

A composite score ranks all 17,344 phenotype-bearing dark genes. It has 6 weighted dimensions, each scored 0–1: fitness importance, conservation, module membership, domain annotations, biogeographic signal, and tractability. [src: functional_dark_matter] The top 100 candidates have scores of 0.624–0.715 and span 22 organisms. Of these, 82/100 have high-confidence functional hypotheses, 85/100 have module-based predictions, and 97/100 have domain annotations. [src: functional_dark_matter] The report states that 82% of the top 100 have testable functional hypotheses with specific experimental protocols. [src: functional_dark_matter]

One caveat limits the organism spread. [[entities/shewanella-oneidensis-mr-1|MR-1]] contributes 25/100 top candidates. The report attributes this to its deep condition coverage (121 conditions) rather than to inherent biology. [src: functional_dark_matter]

The report's data outputs for this part are listed below.

- `data/dark_genes_integrated.tsv` has 228,709 rows. [src: functional_dark_matter]
- `data/dark_genes_only.tsv` holds the 57,011 dark gene subset. [src: functional_dark_matter]
- `data/gapmind_gap_candidates.tsv` has 1,256 organism-pathway pairs. [src: functional_dark_matter]
- `data/concordance_scores.tsv` has 65 OG concordance scores. [src: functional_dark_matter]
- `data/phylogenetic_breadth.tsv` has 30,756 clusters. [src: functional_dark_matter]
- `data/biogeographic_profiles.tsv` has 31 species-level profiles. [src: functional_dark_matter]
- `data/carrier_noncarrier_tests.tsv` has 151 within-species tests. [src: functional_dark_matter]
- `data/lab_field_concordance.tsv` has 47 pre-registered concordance tests. [src: functional_dark_matter]
- `data/nmdc_validation.tsv` has 105 NMDC abiotic correlations. [src: functional_dark_matter]
- `data/scoring_all_dark.tsv` has 17,344 fully scored genes. [src: functional_dark_matter]
- `data/prioritized_candidates.tsv` holds the top 100 with hypotheses and suggested experiments. [src: functional_dark_matter]

## Results: Step 8: Final synthesis — darkness spectrum, covering set, action plan (NB09)

This part of the report tests how robust the dark-gene results are, then prioritizes essential dark genes that fitness screens cannot see, adds synteny and co-fitness evidence, and builds a darkness spectrum and organism covering set. Dark genes match annotated genes in cross-organism concordance [src: functional_dark_matter], and the stress-versus-accessory hypothesis failed. [src: functional_dark_matter] Scoring-weight rank correlations stayed high, though specific top-50 lists were moderately sensitive to weights. [src: functional_dark_matter]

### Robustness and controls

The hypothesis that stress-condition dark genes are more accessory than carbon/nitrogen genes was rejected by Fisher's exact test (n=7,491; p=0.013). The effect ran the opposite way: 23.0% of stress genes were accessory versus 25.5% for carbon/nitrogen. [src: functional_dark_matter] The report reads this as showing that condition specificity and pangenome conservation are more complex than a simple stress=accessory, metabolism=core model. [src: functional_dark_matter]

Cross-organism concordance was indistinguishable between 65 dark and 490 annotated ortholog groups (OGs) (Mann-Whitney, p=0.17). [src: functional_dark_matter] The report reads this as support for H1, that dark genes behave like real functional genes, not noise. [src: functional_dark_matter]

Rank correlations stayed high (ρ > 0.93) across 6 alternative scoring-weight configurations. [src: functional_dark_matter] The specific top-50 lists were moderately sensitive, with 64% retention under conservation-dominant weighting. [src: functional_dark_matter] The report advises treating rankings as approximate and focusing on genes that stay in the top tier across weight schemes. [src: functional_dark_matter]

### Essential dark genes

The 9,557 essential dark genes are invisible to standard random barcode transposon sequencing (RB-TnSeq). No viable mutants exist, so they have zero rows in genefitness. [src: functional_dark_matter] The report scores them separately, using neighborhood context, domain structure, ortholog conservation, phylogenetic breadth and CRISPR interference (CRISPRi) tractability. This avoids penalizing them for fitness data they cannot have. [src: functional_dark_matter] It concludes that they make up 55% of phenotype-bearing dark genes but are systematically missed by fitness-based scoring. [src: functional_dark_matter]

Of 57,011 dark genes, 97.2% have at least one annotated gene within a 5-gene window. [src: functional_dark_matter] In addition, 30,190 (52.9%) have annotated operon partners. [src: functional_dark_matter] The top 50 essential candidates score 0.740–0.875 and span 15 organisms. All have high-confidence hypotheses from neighbor context and domain annotations. [src: functional_dark_matter] Those scores exceed the fitness-active top 100 (0.624–0.715), which the report attributes to stronger conservation and neighborhood signals. [src: functional_dark_matter] The report proposes CRISPRi as an experimental route that transposon mutagenesis cannot offer. [src: functional_dark_matter]

### Synteny and co-fitness validation

The earlier operon predictions used a single-genome positional heuristic, so a later notebook added two independent checks. [src: functional_dark_matter] Cross-species synteny asks whether a dark-gene/annotated-gene neighborhood is conserved across organisms. [src: functional_dark_matter] It tested 21,011 pairs across 48 Fitness Browser (FB) genomes. Conservation strengthens the functional inference. [src: functional_dark_matter] Co-fitness validation asks whether predicted operon partners have correlated fitness profiles. [src: functional_dark_matter] It tested 32,075 pairs. The report calls co-fitness-confirmed operons the strongest functional inference for essential genes lacking fitness data. [src: functional_dark_matter]

Genes with both a conserved neighborhood and correlated operon-partner fitness have the strongest guilt-by-association evidence. [src: functional_dark_matter] Re-scoring all 17,344 fitness-active and 9,557 essential dark genes with this evidence produced 300 improved candidates (200 fitness-active + 100 essential) with evidence-weighted experimental recommendations. [src: functional_dark_matter]

### Darkness spectrum and organism covering set

The darkness spectrum classifies all 57,011 dark genes by evidence depth. [src: functional_dark_matter]

| Tier | Genes | Share | Meaning |
|---|---|---|---|
| T1 Void | 4,273 | 7.5% | zero evidence [src: functional_dark_matter] |
| T2 Twilight | 12,282 | 21.5% | one clue [src: functional_dark_matter] |
| T3 Dusk | 16,103 | 28.2% | two converging hints [src: functional_dark_matter] |
| T4 Penumbra | 22,500 | 39.5% | 3–4 evidence lines [src: functional_dark_matter] |
| T5 Dawn | 1,853 | 3.3% | nearly characterized [src: functional_dark_matter] |

The report concludes that only 7.5% are truly unknown and that most need targeted experiments, not broad screens. [src: functional_dark_matter] It also concludes that 92.5% have at least some evidence and 39.5% have 3–4 converging lines. [src: functional_dark_matter]

The minimum covering set is a greedy weighted set-cover algorithm that optimizes priority value × tractability × phylogenetic diversity. [src: functional_dark_matter] It selects 42 organisms from 28 genera covering 95% of total priority. [src: functional_dark_matter] MR-1 ranks first [src: functional_dark_matter], and 32 organisms achieve 80% coverage. [src: functional_dark_matter] Each gene is assigned to exactly one organism for follow-up. [src: functional_dark_matter] A conservation-weighted covering set in NB11 gives an alternative organism ordering, optimized for broadly conserved true knowledge gaps. [src: functional_dark_matter]

The action plan classifies 14,450 genes as hypothesis-bearing, with condition recommendations from fitness data, module prediction or neighbor context. [src: functional_dark_matter] It classifies 2,038 as darkest, requiring broad phenotypic screens. [src: functional_dark_matter] It recommends CRISPRi for 8,900 essential genes in the covering set. [src: functional_dark_matter]

## Results: Step 9: Pangenome-scale conservation × hypothesis classification (NB11, NB11b)

This part of the report moves dark-gene conservation from the 48 Fitness Browser (FB) organisms to the full 27,690-species GTDB r214 pangenome. It then classifies ortholog groups (OG) by taxonomic tier and hypothesis status, and builds conservation-weighted organism covering sets. [src: functional_dark_matter]

### Why the conservation analysis was extended

NB09's evidence-weighted approach depends on Fitness Browser data, so it can assess conservation only in the 48 FB organisms. [src: functional_dark_matter] NB05's eggNOG breadth score does not discriminate: 99.9% of dark gene clusters map to universal root-level OGs and receive identical conservation scores. [src: functional_dark_matter] NB11 addresses the FB-only limit by querying the full 27,690-species GTDB r214 pangenome. [src: functional_dark_matter] See [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]] for the wider question.

### Full-pangenome counts and classification (NB11, NB11b)

A Spark query in NB11b exploded eggNOG_OGs annotations across 93.5M gene clusters. It matched all comma-separated OG entries against 11,774 dark gene root OGs. [src: functional_dark_matter] Species counts per OG now range from 1 to 27,482 (median 135, mean 2,128), replacing the earlier 1-to-33 range from the FB-only analysis. [src: functional_dark_matter] OG_id propagation recovered 5,206 more dark genes. It transferred root_og assignments from genes with known pangenome links to genes in the same 48-organism ortholog group. [src: functional_dark_matter]

Each dark gene OG was placed in one of 8 taxonomic tiers: kingdom 55.9%, class 11.0%, family 10.5%, genus 6.9%, mobile 6.5%, phylum 4.8%, order 3.9% and species 0.5%. [src: functional_dark_matter] Each OG also received one of 3 hypothesis status tiers: strong testable hypothesis 6.0%, weak lead 52.5%, and true knowledge gap 41.5%. [src: functional_dark_matter] The importance score is (tier-adjusted conservation + log₂-scaled species fraction) × an ignorance multiplier. It ranks all OGs and puts kingdom-level true knowledge gaps at the top. [src: functional_dark_matter]

The report reads the 55.9% kingdom-level share as evidence that dark matter is not a minor annotation gap. These OGs span multiple phyla and thousands of species, so the report calls it a fundamental limitation in understanding conserved biology. [src: functional_dark_matter] This is the report's interpretation of the tier counts.

### Conservation-weighted covering set

A greedy set-cover algorithm optimized Σ(importance) × tractability × phylo_bonus. It selected 42 organisms in 28 genera, covering 95.6% of importance-weighted priority. [src: functional_dark_matter] The top three were *Sinorhizobium meliloti* (1,630 OGs, 195 kingdom gaps), *P. putida* (1,043 OGs, 172 kingdom gaps) and *Shewanella oneidensis* MR-1 (805 OGs, 105 kingdom gaps). [src: functional_dark_matter] The report gives per-organism experimental plans that recommend approaches by tier × hypothesis status. [src: functional_dark_matter] This ordering targets completely unknown functions and complements NB09's evidence-weighted ordering. [src: functional_dark_matter] See [[entities/greedy-weighted-set-cover-organism-selection]] and [[entities/pseudomonas-putida]].

### Extended covering set (NB11c)

NB11c assembled 73 candidate organisms to address the Proteobacteria-heavy FB sampling bias: the 48 FB organisms plus 25 literature-curated ones with TnSeq (transposon sequencing) or CRISPRi (CRISPR interference) resources from Bacillota, Actinomycetota and Campylobacterota. [src: functional_dark_matter] A Spark query mapped genus-level OG membership for the 25 non-FB organisms (24 genera), giving 53,970 genus-OG pairs. [src: functional_dark_matter] See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]].

Running the covering set on all 73 candidates gave 50 organisms covering 98.7% of OGs across 6 phyla. The FB-only candidates gave 41 organisms across 4 phyla. [src: functional_dark_matter] The 50-organism set includes 16 non-FB organisms. [src: functional_dark_matter] *P. aeruginosa* PAO1 ranks #1 with 3,713 OGs. [src: functional_dark_matter] *M. tuberculosis* (Actinomycetota) ranks #6. [src: functional_dark_matter] *C. jejuni* (Campylobacterota) ranks #48. [src: functional_dark_matter]

### Caveats

- Conservation assessment in NB09 covers only the 48 FB organisms. NB11 addresses this limit. [src: functional_dark_matter]
- The NB05 eggNOG breadth score is non-discriminative. [src: functional_dark_matter]
- The report states 42 organisms for the conservation-weighted covering set and 41 organisms for FB-only candidates in the extended comparison. The quotes do not say whether these describe the same set. [src: functional_dark_matter]

## Interpretation: Hypothesis Assessment

This part of the report judges its hypotheses against the evidence. It concludes that H1 is partially supported and H0 can be partially rejected, because dark genes with strong fitness effects show non-random patterns across several evidence dimensions. [src: functional_dark_matter] Two sub-hypotheses are supported (H1a, H1c), H1d is supported, H1e is only suggestive, and H1b is rejected. The part ends by placing the work against earlier literature.

### Overall verdict and the noise question

A matched comparison (NB06) finds no significant difference in cross-organism concordance between dark and annotated genes with orthologs in 3+ organisms. The tests gave Mann-Whitney p=0.17 and KS p=1.0. The dark median was 1.0 and the annotated median 1.0; the dark mean was 0.976 and the annotated mean 0.985. [src: functional_dark_matter] The report reads this as support for H1: dark genes behave like real functional genes, not noise. [src: functional_dark_matter] The null result matters here because it shows no detectable gap between the two groups.

### Sub-hypotheses

**H1a, functional coherence: supported.** 6,142 dark genes co-regulate with annotated genes in ICA (independent component analysis) modules. [src: functional_dark_matter] 85/100 top candidates have module-based function predictions. [src: functional_dark_matter] The report calls the guilt-by-association approach from the `fitness_modules` project its single strongest inference layer. [src: functional_dark_matter]

**H1b, stress genes more accessory: rejected.** Fisher's exact testing of n=7,491 dark genes found the opposite of the predicted pattern. Stress-condition dark genes are 23.0% accessory, and carbon/nitrogen dark genes are 25.5% accessory (OR=1.15, p=0.013). [src: functional_dark_matter] The report rejects the hypothesis that stress genes should be more accessory than carbon/nitrogen genes. [src: functional_dark_matter] It suggests that condition specificity and pangenome conservation are related in a more complex way than a stress=accessory, metabolism=core dichotomy. [src: functional_dark_matter]

**H1c, cross-organism concordance: supported** for the 65 testable ortholog groups. [src: functional_dark_matter] Motility-related dark genes show the strongest concordance, consistent with conserved but incompletely annotated chemotaxis machinery. [src: functional_dark_matter]

**H1d, biogeographic pattern: supported.** 10/137 clusters show significant environmental enrichment. [src: functional_dark_matter] Overall lab-field concordance was 61.7% against a 50% chance level. The binomial test gave p = 0.072 and Fisher's combined test gave p = 0.031 (NB10). [src: functional_dark_matter] The binomial test alone does not reach conventional significance, while the combined test does. [src: functional_dark_matter] NMDC independent validation confirmed all 4 testable pre-registered predictions (nitrogen~nitrogen, pH~pH, anaerobic~dissolved oxygen). [src: functional_dark_matter] The strongest within-species signals are in *Pseudomonas* and *P. syringae*. [src: functional_dark_matter] The NMDC correlations give community-level corroboration across 6,365 metagenomic samples. [src: functional_dark_matter]

The NB06 Section 3 NMDC trait-condition analysis confirmed all 7 pre-registered predictions linking dark-gene carrier genera abundance to matching community functional traits. [src: functional_dark_matter] Nitrogen-source carriers correlate with nitrogen_fixation trait scores (ρ=0.60), [src: functional_dark_matter] and carbon-source carriers correlate with aerobic_chemoheterotrophy (ρ=0.73). [src: functional_dark_matter] The report cautions that these high correlations likely reflect compositional coupling, where shared genera drive both scores, rather than independent validation. [src: functional_dark_matter]

**H1e, pathway integration: suggestive** with partial domain-level support. [src: functional_dark_matter] GapMind identifies 1,256 organism-pathway pairs where dark genes co-occur with metabolic gaps. [src: functional_dark_matter] NB10 domain matching found 3,186 of 57,011 dark genes with annotations compatible with at least one gapped pathway. The annotations are EC (Enzyme Commission) numbers, PFam domains, or functional keywords. [src: functional_dark_matter] These give 42,239 gene-pathway candidates, including 5,398 high-confidence EC prefix matches. [src: functional_dark_matter] The report says these candidates narrow the search from organism-level co-occurrence to enzymatically plausible gap-fillers. [src: functional_dark_matter] Full confirmation of specific gene-to-step assignments requires AlphaFold structure prediction or experimental enzymology. [src: functional_dark_matter]

### Relation to prior work

The report's 24.9% dark gene fraction aligns with published estimates of 25–40% hypothetical genes in typical bacterial genomes (Makarova et al. 2019). [src: functional_dark_matter] Deutschbauer et al. (2011) pioneered fitness profiling for function prediction in Shewanella MR-1, using 121 conditions to propose functions for 40 previously hypothetical genes. [src: functional_dark_matter] This project extends the approach to 48 organisms and 7,552 conditions, using the Fitness Browser resource (Price et al. 2018). [src: functional_dark_matter] Shewanella MR-1 accounts for 25/100 of the top candidates. The report calls this consistent with its extensive condition coverage and large hypothetical gene complement. [src: functional_dark_matter]

Vaccaro et al. (2016) showed that fitness profiling in *Pseudomonas stutzeri* RCH2 could identify novel metal resistance genes among hypotheticals. [src: functional_dark_matter] The report's stress-responsive dark genes in *Pseudomonas* species corroborate this pattern. [src: functional_dark_matter] To the report's knowledge, its systematic test of whether lab fitness conditions predict the field environments of gene carriers, across multiple organisms and condition classes, is novel. [src: functional_dark_matter]

Pavlopoulos et al. (2023) identified 106,198 novel protein families from 26,931 metagenomes, doubling the number of known protein families. [src: functional_dark_matter] Zhang et al. (2025) developed FUGAsseM, which predicts high-confidence functions for >443,000 protein families using metatranscriptomic coexpression. [src: functional_dark_matter] The report calls its approach complementary to these computational methods. Every gene in its catalog has measured fitness phenotypes from controlled lab experiments. [src: functional_dark_matter] Its top candidates come with specific experimental protocols. [src: functional_dark_matter] The report also claims that its darkness spectrum (T1 Void through T5 Dawn) is a structured framework absent from prior metagenomic surveys, which typically treat uncharacterized proteins as a single class. [src: functional_dark_matter]

Alam et al. (2011) prioritized orphan proteins in *Streptomyces coelicolor* using phylogenomics and gene expression. This showed that multi-evidence integration can rank unknowns in a single organism. [src: functional_dark_matter] The report extends this to 48 organisms with 6 evidence dimensions. It adds a set-cover organism selection step that turns gene-level priorities into an experimental campaign. [src: functional_dark_matter]

## Interpretation: Limitations

This part of the report lists its contributions and the limits on them. The contributions are a unified catalog, a prioritized candidate list, lab-field concordance testing, cross-organism concordance, a darkness spectrum and organism-selection routes. [src: functional_dark_matter] Several of its validation results are partial or marginal. [src: functional_dark_matter]

### Claimed contributions

The report integrates 57,011 dark genes across 48 bacteria, drawing fitness, conservation, module, ortholog and domain data from 4 prior observatory projects that were previously fragmented across analyses. [src: functional_dark_matter] It combines 6 scored evidence axes into 100 ranked candidates with functional hypotheses and suggested experiments for the Arkin Lab and collaborators. [src: functional_dark_matter] Cross-organism fitness concordance reveals 65 ortholog groups with conserved phenotypes that could not be identified from any single organism. [src: functional_dark_matter]

The lab-field concordance framework connects lab fitness phenotypes to environmental biogeography via pangenome carrier analysis. [src: functional_dark_matter] It finds 61.7% concordance across 47 testable clusters. [src: functional_dark_matter] NMDC metagenomic correlations independently validated it, with 4/4 pre-registered predictions confirmed. [src: functional_dark_matter]

### Darkness spectrum and resource allocation

The darkness spectrum is a five-tier inventory, T1 Void through T5 Dawn, that quantifies each gene's darkness across 6 independent evidence axes. [src: functional_dark_matter] Only 7.5% of dark genes (4,273 T1 Void) are truly unknown with zero evidence. [src: functional_dark_matter] The largest group, 39.5% (T4 Penumbra), has 3–4 converging lines of evidence and is ready for targeted characterization. [src: functional_dark_matter] The report recommends confirmation for T5 Dawn genes [src: functional_dark_matter], targeted experiments for T4 Penumbra genes [src: functional_dark_matter] and broad screens for T1 Void genes. [src: functional_dark_matter]

### Organism selection

The dual-route covering set uses two complementary greedy weighted set-cover algorithms. [src: functional_dark_matter] Route A (evidence-weighted, NB09) selects 42 organisms optimized for genes with testable hypotheses. [src: functional_dark_matter] Route B (conservation-weighted, NB11) selects 42 organisms optimized for discovering functions of broadly conserved true knowledge gaps. [src: functional_dark_matter] The routes share 39 organisms but order them differently, reflecting different experimental strategies. [src: functional_dark_matter] An extended tractable list of 73 organisms (48 FB, the Fitness Browser, plus 25 literature-curated organisms from 3 additional phyla) offers a way to expand coverage beyond the Proteobacteria-dominated Fitness Browser. [src: functional_dark_matter]

### Validation strength and null controls

The NMDC validation is strong in raw significance but limited by compositional coupling. NMDC trait_features analysis (NB06 Section 3) confirmed all 7 pre-registered trait-condition predictions with FDR (false discovery rate) < 10⁻²¹. [src: functional_dark_matter] It also found 441/449 exploratory tests significant at FDR < 0.05. [src: functional_dark_matter] The report says this extreme significance likely reflects compositional coupling, because abundant genera contribute to both carrier abundance and community trait scores. [src: functional_dark_matter] The correlations show ecological co-occurrence, not causal gene-phenotype links. [src: functional_dark_matter]

NB10 adds partial null approximations:
- A sign test on 7/7 trait directions gives p = 0.0078. [src: functional_dark_matter]
- A sign test on 4/4 abiotic directions gives p = 0.0625. [src: functional_dark_matter]
- Fisher's combined probability across all 11 pre-registered tests gives p ≈ 0. [src: functional_dark_matter]
- An inflation factor of ~20× for exploratory tests (441/449 significant vs. 22.5 expected) quantifies the coupling. [src: functional_dark_matter]

A full permutation test shuffling sample labels remains future work and needs Spark access to raw per-sample matrices. [src: functional_dark_matter]

For lab-field concordance, the evidence is only marginal. NB10's binomial test (29/47 vs. p = 0.5) gives one-sided p = 0.072, with a Wilson score 95% CI (confidence interval) of [0.474, 0.742]. This indicates concordance marginally above chance. [src: functional_dark_matter] Fisher's combined probability across all 47 individual tests gives p = 0.031. [src: functional_dark_matter] A full null comparison using annotated accessory genes through the same biogeographic pipeline would further strengthen rejection of H0, but it requires Spark for carrier genome queries. [src: functional_dark_matter]

The NB06 concordance null control shows dark genes reach concordance indistinguishable from annotated genes, which supports H1. [src: functional_dark_matter] Equivalent null controls were not run for the biogeographic and lab-field concordance analyses. [src: functional_dark_matter]

### Limits of the data

- Environmental metadata are sparse. AlphaEarth embeddings cover only 28% of genomes (83K/293K), and NCBI isolation-source metadata are inconsistent, which limits biogeographic tests. [src: functional_dark_matter]
- NMDC validation works at genus level, mapping taxon columns to pangenome genera via ncbi_taxid, and may miss species-specific signals. [src: functional_dark_matter] Only 5 of 6 carrier genera matched. The high significance rate (76/105) likely reflects common genera such as *Pseudomonas* and *Klebsiella* dominating both datasets. [src: functional_dark_matter]
- The 57,011 dark-gene count likely overestimates truly uncharacterized genes, because databases not checked may annotate some hypothetical genes. [src: functional_dark_matter]
- The 6,691 module-based predictions from fitness_modules are guilt-by-association inferences, not direct experimental validation. [src: functional_dark_matter] The "high confidence" prioritization label reflects evidence convergence, not experimental proof. [src: functional_dark_matter]
- Condition coverage differs across organisms. Organisms with more conditions, such as MR-1 with 121, produce more specific phenotypes and so score higher. [src: functional_dark_matter]

### GapMind and gap-filling limits

GapMind covers amino acid biosynthesis and carbon utilization pathways but not all metabolic functions. [src: functional_dark_matter] The analysis misses dark genes with signaling, regulatory or structural roles. [src: functional_dark_matter] It identifies organism-level co-occurrence of pathway gaps and dark genes, not direct gene-to-step assignments. [src: functional_dark_matter] NB10 partly addresses this with curated pathway-enzyme domain matching (EC, Enzyme Commission, prefix, PFam family and keyword compatibility). It identifies 42,239 domain-compatible gene-pathway candidates, including 5,398 high-confidence EC matches. [src: functional_dark_matter] Full gene-to-step validation would need AlphaFold structure prediction or experimental enzymology. [src: functional_dark_matter]

### Essential genes

Of the 17,344 scored dark genes, 9,557 (55%) are essential, with no viable transposon mutants. [src: functional_dark_matter] None appear in the NB05 top 100. Essential genes have zero rows in genefitness, so fitness importance scores them at the essentiality bonus floor, and experimental tractability penalizes them as non-knockable. [src: functional_dark_matter] NB07 prioritizes them separately, using gene neighbors, phylogenetic breadth, cross-organism conservation, domains and CRISPRi (CRISPR interference) tractability. It produces 50 ranked candidates amenable to CRISPRi knockdown. [src: functional_dark_matter]

### Operon and neighborhood methods

NB07's operon predictions use a single-genome positional heuristic: a 5-gene window, same strand and a gap of ≤300 bp. [src: functional_dark_matter] NB08 adds cross-species synteny across 48 Fitness Browser genomes and co-fitness confirmation, but still falls short of industry-standard tools. [src: functional_dark_matter] For comparison, DOOR v2.0 uses intergenic distance, neighborhood conservation, phylogenetic distance and experimentally validated training sets across thousands of genomes. [src: functional_dark_matter] STRING v12 combines genomic neighborhood, gene fusion, phylogenetic co-occurrence, co-expression and text mining across >14,000 organisms. [src: functional_dark_matter]

## Interpretation; Data

This part of the report covers how far the prioritization and neighborhood results can be trusted, how well the organism set covers taxa, and which KBase Data Lakehouse collections and output tables the work rests on. The rankings are robust overall but their top lists depend moderately on expert-chosen weights. [src: functional_dark_matter]

### Weight sensitivity of the prioritization

Both dark-gene prioritization frameworks use arbitrary expert-assigned weights. [src: functional_dark_matter] Sensitivity analyses (NB05/NB07) show overall rank correlations of ρ > 0.93 across alternative weights, but the top-ranked lists are moderately weight-sensitive. [src: functional_dark_matter] The loss is largest when tractability is dropped from the essential-gene ranking.

| Ranking | Weight change | Original top 50 retained |
|---|---|---|
| NB05 (fitness-active) | conservation-dominant | 32/50 (64%) [src: functional_dark_matter] |
| NB05 (fitness-active) | drop tractability | 32/50 (64%) [src: functional_dark_matter] |
| NB07 (essential) | drop tractability | 18/50 (36%) [src: functional_dark_matter] |
| NB07 (essential) | drop neighbor context | 24/50 (48%) [src: functional_dark_matter] |

NB10 identifies candidates that do not depend on the weights. Across all 6 fitness-active weight configurations, 18 genes stay in the top 50 and 35 stay in the top 100. [src: functional_dark_matter] For essential genes, 6 always stay in the top 50 and 19 always stay in the top 100. [src: functional_dark_matter] The report calls these "always-top" candidates the most defensible targets for experimental follow-up. [src: functional_dark_matter] Per-gene rank ranges are in data/robust_ranks_fitness.tsv and data/robust_ranks_essential.tsv. [src: functional_dark_matter]

### Limits of the neighborhood analysis

The neighborhood analysis captures the most accessible signal. It lacks gene-fusion detection, regulatory-element analysis and broad taxonomic sampling, all of which would improve prediction accuracy. [src: functional_dark_matter] The report contrasts this with EFI-GNT, which provides interactive genome neighborhood diagrams across all sequenced genomes with SSN-guided filtering. [src: functional_dark_matter] See [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]].

### Taxonomic coverage

The 48 Fitness Browser organisms are 77% Pseudomonadota (37/48). [src: functional_dark_matter] The extended covering set (NB11c) partly addresses this. It adds 25 non-Fitness-Browser organisms from Bacillota, Actinomycetota and Campylobacterota, which expands phylum coverage from 4 to 6. [src: functional_dark_matter] Three caveats limit this gain:
- Ortholog-group coverage for the non-Fitness-Browser organisms is estimated at genus level, which overestimates individual-organism coverage. [src: functional_dark_matter]
- These organisms lack Fitness Browser condition profiling. Their dark genes can be assigned only broad phenotypic screens, not condition-specific experiments. [src: functional_dark_matter]
- The covering-set algorithm did not select the Bacillota organisms B. subtilis and S. aureus, because their ortholog groups are subsets of Pseudomonadota coverage. They would still be valuable for studying genes in native Gram-positive contexts. [src: functional_dark_matter]

See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]].

### Data sources

The report draws on three KBase Data Lakehouse collections.
- `kescience_fitnessbrowser` supplies fitness phenotypes, gene descriptions, co-fitness, orthologs and domains. [src: functional_dark_matter]
- `kbase_ke_pangenome` supplies pangenome conservation, phylogenetic breadth, environmental metadata and pathway analysis. [src: functional_dark_matter]
- `nmdc_arkin` supplies independent environmental validation through a genus-level taxonomy bridge and a trait-condition concordance analysis. [src: functional_dark_matter]

### Output tables

The report provides these tables, listed with row counts.

| Table | Rows | Content |
|---|---|---|
| dark_genes_integrated.tsv | 228,709 | Full gene table with all cross-references (43 columns) [src: functional_dark_matter] |
| dark_genes_only.tsv | 57,011 | Dark genes subset with pangenome, module, ortholog links [src: functional_dark_matter] |
| gapmind_gap_candidates.tsv | 1,256 | Organism-pathway pairs with dark genes near metabolic gaps [src: functional_dark_matter] |
| gapmind_pathway_summary.tsv | 80 | Per-pathway completeness summary across 44 species [src: functional_dark_matter] |
| gapmind_domain_matched.tsv | 42,239 | Domain-compatible dark gene candidates matched to gapped pathways (EC/PFam/keyword), where EC is Enzyme Commission [src: functional_dark_matter] |
| concordance_scores.tsv | 65 | Cross-organism fitness concordance per ortholog group [src: functional_dark_matter] |
| annotated_control_concordance.tsv | 490 | Annotated ortholog-group concordance scores for null comparison [src: functional_dark_matter] |
| phylogenetic_breadth.tsv | 30,756 | Taxonomic breadth per gene cluster [src: functional_dark_matter] |
| biogeographic_profiles.tsv | 31 | Species-level environmental profiles [src: functional_dark_matter] |
| carrier_genome_map.tsv | 8,139 | Gene cluster to carrier genome mapping [src: functional_dark_matter] |
| carrier_noncarrier_tests.tsv | 151 | Within-species carrier vs non-carrier test results [src: functional_dark_matter] |
| lab_field_concordance.tsv | 47 | Pre-registered lab-field concordance test results [src: functional_dark_matter] |
| nmdc_validation.tsv | 105 | NMDC abiotic correlation tests (7 score types x 15 abiotic variables) [src: functional_dark_matter] |
| nmdc_trait_validation.tsv | 456 | NMDC trait-condition correlation results (7 pre-registered + 449 exploratory) [src: functional_dark_matter] |
| scoring_all_dark.tsv | 17,344 | Full scoring for all strong/essential dark genes [src: functional_dark_matter] |
| prioritized_candidates.tsv | 100 | Top 100 ranked candidates with hypotheses and experiments [src: functional_dark_matter] |
| h1b_test_results.tsv | 1 | H1b formal test results (Fisher's exact, chi-squared) [src: functional_dark_matter] |
| gene_neighbor_context.tsv | 57,011 | Gene neighbor profiles for all dark genes (operon predictions, functional keywords) [src: functional_dark_matter] |
| essential_dark_scored.tsv | 9,557 | Essential dark genes scored across 5 dimensions [src: functional_dark_matter] |
| essential_prioritized_candidates.tsv | 50 | Top 50 essential dark gene candidates with CRISPRi (CRISPR interference) experiments [src: functional_dark_matter] |
| scoring_sensitivity_nb05.tsv | 6 | NB05 scoring sensitivity analysis (6 weight configurations) [src: functional_dark_matter] |
| scoring_sensitivity_nb07.tsv | 6 | NB07 scoring sensitivity analysis (6 weight configurations) [src: functional_dark_matter] |
| conserved_neighborhoods.tsv | 21,011 | Per-pair cross-species synteny conservation scores [src: functional_dark_matter] |
| cofit_validated_operons.tsv | 32,075 | Per-pair co-fitness validation of operon predictions [src: functional_dark_matter] |
| improved_candidates.tsv | 300 | Re-scored top candidates (200 fitness-active + 100 essential) with synteny + cofit evidence [src: functional_dark_matter] |
| experimental_roadmap.tsv | 30 | Evidence-weighted organism experiment priorities [src: functional_dark_matter] |
| dark_gene_census_full.tsv | 57,011 | Full darkness spectrum census with tier, evidence flags, composite score [src: functional_dark_matter] |
| minimum_covering_set.tsv | 16,488 | Gene-to-organism assignments from greedy weighted set cover [src: functional_dark_matter] |
| experimental_action_plan.tsv | 42 | Per-organism experiment recommendations (targeted vs broad screen) [src: functional_dark_matter] |
| robust_ranks_fitness.tsv | 17,344 | Per-gene rank ranges across 6 weight configurations (fitness-active) [src: functional_dark_matter] |

## Data; Supporting Evidence

This part of the report lists the data tables and notebooks behind the analysis. Most entries only name files, but a few state results about pangenome coverage and organism selection. [src: functional_dark_matter]

### Pangenome conservation data

The report built ortholog-group (OG) distribution tables at two scales. The full-pangenome table has 11,774 rows and covers 27,690 species, with per-OG species counts ranging from 1 to 27,482. [src: functional_dark_matter] The earlier Fitness Browser-only version, kept as a backup, has the same 11,774 rows but a species range of only 1–33. [src: functional_dark_matter]

An OG_id to root_og propagation mapping has 7,898 rows. The report says it recovers 5,206 additional dark genes. [src: functional_dark_matter] The full-pangenome query exploded eggNOG_OGs across 93.5M annotations in Spark. [src: functional_dark_matter]

### Extended organism pool

The extended tractable-organism table has 73 rows: 48 Fitness Browser organisms and 25 literature-curated organisms, each with TnSeq (transposon sequencing) and CRISPRi (CRISPR interference) tractability scores. [src: functional_dark_matter] The report ran a genus-level pangenome query for 25 non-Fitness Browser organisms. [src: functional_dark_matter] The extended covering set drew on 73 candidates. It selected 50 organisms across 6 phyla, with 98.7% coverage. [src: functional_dark_matter]

## Future Directions

This part of the report turns the dark-gene prioritization into an experimental plan. It gives two organism-selection routes, specific gene targets, and proposed extensions: structure prediction, NMDC data, and a wider organism list. The targets and extensions are proposals and recommendations; the cited text presents them as plans. [src: functional_dark_matter]

### Two organism-selection routes

The report offers two routes that overlap heavily. Route A (NB09, evidence-weighted) identifies 42 organisms covering 95% of composite priority. [src: functional_dark_matter] It recommends starting with MR-1 stress/nitrogen screens and *E. coli* CRISPRi (CRISPR interference) for targeted hypothesis testing. [src: functional_dark_matter] Route B (NB11, conservation-weighted) also identifies 42 organisms, covering 95.6% of importance-weighted priority. [src: functional_dark_matter] It recommends starting with *S. meliloti*, *P. putida*, and MR-1 broad phenotypic screens for novel function discovery. [src: functional_dark_matter] The routes share 39 organisms and are described as complementary. Route A produces mechanistic insights for genes with hypotheses. Route B discovers functions for broadly conserved true knowledge gaps. [src: functional_dark_matter] See [[entities/greedy-weighted-set-cover-organism-selection]] for the selection method.

### Specific experimental targets

The top 5 fitness-active candidates (4 in MR-1, 1 in *P. putida* N2C3) are described as immediately testable via RB-TnSeq (random barcode transposon sequencing) under their predicted condition classes. [src: functional_dark_matter]

- AO356_11255, a D-alanyl-D-alanine carboxypeptidase prediction with an EamA domain, to be tested under nitrogen limitation. [src: functional_dark_matter]
- MR-1 202463, a YGGT-domain T5 Dawn candidate with composite score 0.698, to be tested under multiple stress conditions. [src: functional_dark_matter]
- MR-1 199738/203545/202450, a K03306 paralog family, to be tested under nitrogen limitation, with single and double mutants compared. [src: functional_dark_matter]

For essential genes, the top 50 candidates (NB07) include specific CRISPRi experiment designs. [src: functional_dark_matter] The highest-priority targets are:

- Keio:14796 (YbeY domain, score 0.875, predicted ion transport). [src: functional_dark_matter]
- MR-1:200382 (RimP_N/DUF150_C, score 0.874, predicted ribosome assembly). [src: functional_dark_matter]
- Koxy:BWI76_RS08540 (OmpA/TIGR02802, score 0.865, predicted cell division). [src: functional_dark_matter]

The covering set assigns 8,900 essential genes to specific organisms for CRISPRi-based approaches. [src: functional_dark_matter]

### Computational extensions

The report proposes AlphaFold2 structure predictions for the top 100 candidates. It singles out the 1,853 T5 Dawn genes (nearly characterized). These predictions could confirm functional hypotheses and distinguish between DUF families. [src: functional_dark_matter] The 4,273 T1 Void genes lack all evidence. They would particularly benefit from structure-based prediction, the only remaining computational inference strategy. [src: functional_dark_matter]

The NMDC dataset includes proteomics (346K observations) and metabolomics (3.1M observations) that the report did not use. [src: functional_dark_matter] Correlating dark gene carrier abundance with metabolite or protein profiles could give more direct functional evidence than abiotic correlations alone. [src: functional_dark_matter]

### Broadening organism coverage

To address this, an extended tractable organism list (`data/extended_tractable_organisms.tsv`) curates 25 additional organisms with published TnSeq (transposon sequencing)/CRISPRi resources. [src: functional_dark_matter] They come from Bacillota (6), Actinomycetota (2), Campylobacterota (2), and additional Pseudomonadota (15). [src: functional_dark_matter]

Adding them to Route B's conservation-weighted covering set would allow experimental characterization of kingdom-level OGs (ortholog groups; 55.9% of dark gene OGs). This would happen in native Gram-positive, Actinobacterial, and Campylobacterial contexts. [src: functional_dark_matter] This needs a pangenome Spark query that maps each organism's genes to dark gene root_ogs, extending the NB11b pipeline. [src: functional_dark_matter]

### Community resource

The report proposes publishing the darkness spectrum census (`dark_gene_census_full.tsv`) and the experimental action plan as a community resource for bacterial functional genomics. Other labs could then target organisms, tiers, or condition classes that match their expertise and infrastructure. [src: functional_dark_matter]

## Caveats and Open Work

- The eggNOG breadth classification does not discriminate among candidates, because 99.9% of dark gene clusters (30,721 of 30,756) map to universal breadth. [src: functional_dark_matter]
- A species-count metric correlates with the original ranking (Spearman ρ = 0.982), but top-50 overlap is 62%. [src: functional_dark_matter]
- K. oxytoca BWI76_RS15525 has FDR 0.069 and P. putida N2C3 AO356_24150 has FDR 0.178, so these enrichments are not significant at 0.05. [src: functional_dark_matter]
- Genomic-proximity hypotheses are leads, and DOOR and ProOpDB use signals beyond strand and gap distance. [src: functional_dark_matter]
- STRING v12 and EFI-GNT analyze thousands of genomes with more sophisticated scoring. [src: functional_dark_matter]

## Slots Into

- [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]]: 57,011 dark genes (24.9%), with 1,853 in T5 Dawn. [src: functional_dark_matter]
- [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]]: the conservation tiers and the coarse breadth classification. [src: functional_dark_matter]
- [[concepts/metabolic-pathway-gap-filling-by-unannotated-genes]]: 1,256 organism-pathway pairs with dark-gene co-occurrence. [src: functional_dark_matter]
- [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]]: 65 concordant dark ortholog groups. [src: functional_dark_matter]
- [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]]: NMDC pH and trait validation. [src: functional_dark_matter]
- [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]]: the Actinobacteria gap and the 42-organism cover. [src: functional_dark_matter]
- [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]]: essential dark genes are 55% of actionable dark matter. [src: functional_dark_matter]
- [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]]: 1,129 mutual top-5 cofit pairs. [src: functional_dark_matter]
- [[concepts/annotation-source-disagreement-and-coverage]]: UniRef links for residual hypotheticals. [src: functional_dark_matter]
