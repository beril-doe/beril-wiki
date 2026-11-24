---
type: "Summary"
description: "Summary of the project Metabolic Capability vs Dependency."
doc_type: "short"
full_text: "sources/pathway_capability_dependency__REPORT.md"
---
# Metabolic Capability vs Dependency

This report asks whether a bacterium that encodes a complete metabolic pathway depends on it. [src: pathway_capability_dependency] It crosses GapMind pathway-completeness predictions with random barcode transposon sequencing (RB-TnSeq) fitness data from the Fitness Browser. [src: pathway_capability_dependency] It also extends the question to a pan-bacterial scale. [src: pathway_capability_dependency] The main answer is that capability and dependency often differ: only 35.4% (57/161) of classified organism-pathway pairs are Active Dependencies. [src: pathway_capability_dependency] The report states this as its central finding: genomic capability and metabolic dependency are distinct. [src: pathway_capability_dependency] The fitness part rests on only 7 Fitness Browser organisms. [src: pathway_capability_dependency] The importance threshold is median-based, so the category split is partly built in (see caveats). [src: pathway_capability_dependency]

## Key Findings

### Organism-level classification: capability is not dependency

The Tier 1 analysis covers the 7 Fitness Browser organisms with GapMind data. Of the 48 organisms in the Fitness Browser, only these 7 have matching GapMind data. [src: pathway_capability_dependency] An earlier essential_metabolome pilot also identified 7 Fitness Browser organisms with GapMind data and flagged that Escherichia coli is absent from GapMind coverage. [src: pathway_capability_dependency] Across them, 23 GapMind pathways had sufficient gene-level annotation, yielding 161 organism-pathway pairs. [src: pathway_capability_dependency] A pathway counts as complete when GapMind predicts it complete in >50% of conspecific genomes. [src: pathway_capability_dependency] It counts as fitness-important when its composite importance score exceeds the data-driven median threshold. [src: pathway_capability_dependency]

The categories were:

| Category | Share |
|---|---|
| Active Dependency | 35.4% (57/161) [src: pathway_capability_dependency] |
| Latent Capability | 41.0% (66/161) [src: pathway_capability_dependency] |
| Incomplete but Important | 14.9% (24/161) [src: pathway_capability_dependency] |
| Missing | 8.7% (14/161) [src: pathway_capability_dependency] |

- Active Dependencies are complete pathways that contain fitness-important genes. The organism needs and uses them. [src: pathway_capability_dependency]
- Latent Capabilities are genomically complete, but their genes show no significant fitness defects under standard conditions. They are encoded but dispensable under tested conditions. [src: pathway_capability_dependency]
- Incomplete but Important pathways are scored incomplete by GapMind but have fitness-important mapped genes. The report suggests annotation gaps or salvage routes as explanations. [src: pathway_capability_dependency]
- Missing pathways are neither complete nor important, so they are absent and unneeded. [src: pathway_capability_dependency]

The report reads the 41% Latent Capability rate as suggesting that nearly half of complete pathways are conditionally, but not permanently, dispensable. [src: pathway_capability_dependency]

The composite importance score weights essentiality at 40% (fraction of pathway genes that are putative essentials). [src: pathway_capability_dependency] It weights fitness breadth at 30% (fraction of conditions with a significant phenotype). [src: pathway_capability_dependency] It weights fitness magnitude at 30% (severity of the worst defect). [src: pathway_capability_dependency] The breadth weight follows the fitness_effects_conservation finding that breadth predicts conservation better than magnitude. [src: pathway_capability_dependency] Fitness Browser genes were mapped to GapMind pathways through the Fitness Browser's own KEGG annotations (besthitkegg to Enzyme Commission (EC) number to KEGG map), not the pangenome link table. [src: pathway_capability_dependency]

The organisms are Desulfovibrio vulgaris Hildenborough, Shewanella oneidensis MR-1, Pseudomonas putida KT2440, Pseudomonas stutzeri RCH2, Caulobacter crescentus, Sinorhizobium meliloti and Azospirillum brasilense. [src: pathway_capability_dependency]

### Latent Capabilities are conditionally active

Stratifying fitness effects by condition type (nitrogen source, carbon source, stress, other) showed that all 66 Latent Capability pairs become fitness-important under at least one condition type. [src: pathway_capability_dependency] The stratification was adopted from field_vs_lab_fitness, which found field-important genes to be 83.6% core versus a 76.3% baseline. [src: pathway_capability_dependency] Nitrogen limitation, stress and carbon limitation most often trigger reclassification. [src: pathway_capability_dependency] The report names nitrogen limitation and stress as the most frequent triggers, as expected if amino acid biosynthesis matters when nutrients are scarce. [src: pathway_capability_dependency] The report therefore reads "Latent Capability" as "conditionally active" rather than "genomic baggage". The pathways are kept because they are needed outside the standard laboratory conditions. [src: pathway_capability_dependency] This agrees with the core_gene_tradeoffs finding of 28,017 Fitness Browser genes that are costly in the lab but conserved in nature, which motivated the stratification. [src: pathway_capability_dependency] The report says this shows at pathway level that laboratory fitness is an incomplete proxy for natural selection, because every latent pathway matters under some conditions. [src: pathway_capability_dependency]

A caveat limits the "all become important" result. The median threshold, applied to each condition-type subset, may let some pathways inevitably cross it. [src: pathway_capability_dependency]

The report proposes that Black Queen Hypothesis gene loss may be constrained by the breadth of environments a species meets, not only by mean fitness under one condition. [src: pathway_capability_dependency] That proposal is an interpretation, not a direct test. The report reframes the hypothesis as a continuum of dependency that varies with environmental context. [src: pathway_capability_dependency] It proposes that pathways dispensable under carbon-rich conditions may be essential under nitrogen limitation. [src: pathway_capability_dependency] It asserts that how often a species meets each condition type sets the selective pressure to keep a pathway. [src: pathway_capability_dependency]

### Conservation validation

Active Dependencies have mean core gene completeness of 0.986, against 0.975 for Latent Capabilities. [src: pathway_capability_dependency] The report attributes the small gap to the well-studied model organisms, whose core genomes are near-complete and well annotated. [src: pathway_capability_dependency] It calls the small enrichment consistent in direction with metal_fitness_atlas, which found fitness-important genes enriched in the core genome (OR=2.08 for metal-fitness genes). [src: pathway_capability_dependency] The report adopted that project's odds-ratio (OR) based conservation validation and cross-species aggregation, citing 87.4% of metal-fitness genes as core. [src: pathway_capability_dependency] It places Active Dependencies at the high end of the 16pp fitness-conservation gradient from conservation_fitness_synthesis, which it reads as showing conserved genes are functionally active, not inert. [src: pathway_capability_dependency] It calls them the metabolic instance of the general tendency of conserved genes to be fitness-important. [src: pathway_capability_dependency] The cofitness_coinheritance result that 73% of accessory modules show co-inheritance with co-fitness is taken as validating pathway-level fitness aggregation. [src: pathway_capability_dependency]

## Pan-bacterial Pathway Variation and Pangenome Openness

Species with more variable pathways have more open pangenomes. The Tier 2 analysis covers 2,810 GTDB species with at least 10 genomes in the pangenome database. It spans 80 GapMind pathways: 18 amino acid biosynthesis and 62 carbon source utilization. [src: pathway_capability_dependency] The data were extracted from the KBase Data Lakehouse and cover 293,000 genomes. [src: pathway_capability_dependency] Variable pathways are those present in 10-90% of genomes, and openness is the fraction of accessory gene clusters. [src: pathway_capability_dependency] The raw Spearman correlation is rho=0.327 (p=7.2e-71, n=2,810 species). [src: pathway_capability_dependency] Genome count is a critical confounder, because more sequenced genomes may show more variable pathways through sampling depth alone. [src: pathway_capability_dependency] After controlling for it, the partial Spearman correlation strengthens to rho=0.530 (p=2.83e-203). [src: pathway_capability_dependency] The report reads the strengthening as showing that confounding partly suppressed the raw correlation. [src: pathway_capability_dependency] The report calls the result consistent with the Black Queen Hypothesis prediction that pathway gene loss is ongoing, and says it confirms hypothesis H1b. [src: pathway_capability_dependency] It suggests that pathway gain and loss is a major driver of pangenome dynamics. [src: pathway_capability_dependency]

The signal is weaker within genera. It is significant at p<0.05 in 5 of 18 genera tested (Clostridium, Eubacterium, Mesorhizobium, Pseudomonas, Streptomyces). The direction is positive in 13 of 18. [src: pathway_capability_dependency] It is strongest in Clostridium (rho=0.534) and Eubacterium (rho=0.506). [src: pathway_capability_dependency] Small within-genus samples limit statistical power for many groups. [src: pathway_capability_dependency]

The genus checks follow the ecotype_analysis finding that phylogeny dominates gene content in 60.5% of species; the report added phylogenetic controls to all correlations and ecotype analyses in response. [src: pathway_capability_dependency] The report says the relationship holds in the majority of genera with at least 20 species. It suggests this reflects a general evolutionary dynamic, not a clade-specific artifact. [src: pathway_capability_dependency] Full phylum-level stratification would need the GTDB taxonomy table from the KBase Data Lakehouse, so the report used genus-level grouping as a conservative phylogenetic control. [src: pathway_capability_dependency]

The report notes that the pangenome_openness project found no correlation between openness and environment or phylogeny effect sizes. [src: pathway_capability_dependency] It concludes that pathway variation is a mechanistically interpretable correlate of openness that those broader variables did not capture. [src: pathway_capability_dependency] The report also cites module_conservation, which found that module family breadth does not predict conservation. It presents pathway variability, not breadth, as the informative metric at pathway level. [src: pathway_capability_dependency]

## Accessory Dependence of Amino Acid Biosynthesis

Comparing GapMind with sequence_scope = 'core' (core pangenome genes only) against 'all' (all genes) shows which pathways depend on accessory genes. [src: pathway_capability_dependency] Amino acid biosynthesis pathways consistently show the largest gaps. [src: pathway_capability_dependency] Carbon source utilization pathways tend to show smaller gaps. The report suggests carbon catabolism genes may be either universally present or universally absent. [src: pathway_capability_dependency] The most accessory-dependent pathways are all amino acid biosynthesis routes. [src: pathway_capability_dependency]

| Pathway | All genes | Core only | Gap |
|---|---|---|---|
| Leucine (leu) | 0.614 | 0.468 | 0.146 [src: pathway_capability_dependency] |
| Valine (val) | 0.614 | 0.468 | 0.146 [src: pathway_capability_dependency] |
| Arginine (arg) | 0.613 | 0.472 | 0.141 [src: pathway_capability_dependency] |
| Lysine (lys) | 0.804 | 0.664 | 0.140 [src: pathway_capability_dependency] |
| Threonine (thr) | 0.803 | 0.663 | 0.140 [src: pathway_capability_dependency] |

For these top 5 pathways, approximately 14% of species-level pathway completeness comes from accessory genes. [src: pathway_capability_dependency] The report takes this as direct evidence that accessory genes contribute to pathway completeness. [src: pathway_capability_dependency] It describes the Tier 2 analysis as extending core enrichment of fitness-important genes from single genes to whole pathways, since pathway completeness can depend on accessory genes. [src: pathway_capability_dependency] For a substantial fraction of bacteria, amino acid biosynthesis completeness therefore depends on accessory pangenome genes. [src: pathway_capability_dependency] The report reads this as direct evidence for Black Queen dynamics, with synthesis capacity spread across strains rather than universally kept. [src: pathway_capability_dependency] Strain differences in biosynthetic capability are a precondition for Black Queen dynamics, in which metabolic functions become community-level public goods. [src: pathway_capability_dependency] The report names leucine, valine, arginine and lysine as the most common candidates for community-level metabolic sharing. [src: pathway_capability_dependency]

Together with the metal_fitness_atlas result, the report proposes that core genes encode universally needed functions such as central metabolism, metal tolerance and translation. [src: pathway_capability_dependency] Accessory genes encode conditionally needed functions, including specific biosynthetic pathways. [src: pathway_capability_dependency] Pangenome openness then reflects the rate at which conditionally needed pathways are gained and lost. [src: pathway_capability_dependency]

## Metabolic Ecotypes

Within-species pathway variation defines 2-8 metabolic ecotypes per species. [src: pathway_capability_dependency] This comes from hierarchical clustering of binary pathway profiles (complete or incomplete across 80 pathways) with Jaccard distance, among 225 species with 50+ genomes and at least 3 variable pathways. [src: pathway_capability_dependency] Ecotype counts were set by cutting each dendrogram at 50% of maximum distance. [src: pathway_capability_dependency] The median is 4 ecotypes per species and the maximum is 8. [src: pathway_capability_dependency] Alistipes onderdonkii and Barnesiella intestinihominis have the most, with 8 ecotypes each. Both are gut commensals with substantial intraspecific metabolic diversity. [src: pathway_capability_dependency]

Ecotype count correlates with pangenome openness at raw Spearman rho=0.262 (p=6.8e-05). [src: pathway_capability_dependency] The partial correlation after controlling for genome count remains significant at rho=0.322 (p=8.0e-07). [src: pathway_capability_dependency] The report says this supports hypothesis H2, that within-species metabolic variation is real biology linked to genome fluidity and not only a sampling artifact. [src: pathway_capability_dependency]

## Data and Methods

The report obtains data from the KBase Data Lakehouse through Spark on JupyterHub. [src: pathway_capability_dependency] Key tables are kbase_ke_pangenome.gapmind_pathways (305M rows), kescience_fitnessbrowser.genefitness (27M rows) and kescience_fitnessbrowser.experiment (7.5K experiments). [src: pathway_capability_dependency] About 3.9 GB is cached locally across all extracts. [src: pathway_capability_dependency] The authors are Dileep Kishore and Paramvir Dehal. [src: pathway_capability_dependency]

## Caveats and Open Work

- The fitness-based classification covers only 7 of 48 Fitness Browser organisms with GapMind data. These are well-studied model organisms with near-complete core genomes, which the report says compresses the conservation contrast. [src: pathway_capability_dependency]
- The median-based importance threshold splits pathways approximately 50/50 into important and not-important by construction. [src: pathway_capability_dependency] The report cautions that all Latent Capabilities becoming important under some condition may partly reflect inevitable threshold crossing. [src: pathway_capability_dependency] Calibrating against an independent validation set, such as known essentials from essential_metabolome, would give a more defensible threshold. [src: pathway_capability_dependency]
- Latent Capability reflects standard laboratory conditions only. [src: pathway_capability_dependency] Condition-type stratification only partially addresses the fact that laboratory RB-TnSeq cannot capture the full range of natural selective pressures. [src: pathway_capability_dependency]
- Genes without KEGG annotations, or with incorrect ones, are missed, which may underestimate the true number of genes per pathway. [src: pathway_capability_dependency]
- GapMind covers amino acid biosynthesis and carbon utilization only. Cofactor biosynthesis, lipid metabolism and secondary metabolism are not assessed. [src: pathway_capability_dependency]
- Genome count confounds the pan-bacterial associations, and small genus samples limit power. [src: pathway_capability_dependency] Species with more sequenced genomes are more likely to show pathway variation and more ecotypes. Partial correlations mitigate but do not fully eliminate this bias. [src: pathway_capability_dependency]
- Full phylogenetic independent contrasts were not computed. The report controlled for genome count and checked within taxonomic groups. [src: pathway_capability_dependency]
- Phylogeny dominates gene content in 60.5% of species in ecotype_analysis, so metabolic ecotypes may partly reflect intra-species phylogenetic structure. [src: pathway_capability_dependency]
- The fixed 50% distance threshold for ecotypes is a simplification, and other thresholds would give different counts. [src: pathway_capability_dependency] The median of 4 ecotypes per species should be read as an order-of-magnitude estimate. [src: pathway_capability_dependency]
- The planned H2 analysis correlating metabolic ecotypes with AlphaEarth environmental niche breadth was not executed. [src: pathway_capability_dependency] AlphaEarth embeddings cover only 28% of genomes (83K/293K), which would significantly limit the sample size. [src: pathway_capability_dependency]

## Slots Into

- [[concepts/metabolic-capability-versus-fitness-dependency]]: only 35.4% (57/161) of classified pairs are Active Dependencies, and 41.0% (66/161) are Latent Capabilities. [src: pathway_capability_dependency]
- [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]]: accessory-dependent amino acid pathways are read as direct evidence for Black Queen dynamics. [src: pathway_capability_dependency]
- [[concepts/within-species-metabolic-ecotypes-from-pathway-variation]]: 2-8 ecotypes per species, with partial rho=0.322 against openness. [src: pathway_capability_dependency]
- [[concepts/pangenome-openness-and-its-correlates]]: variable pathway count has partial rho=0.530 with openness. [src: pathway_capability_dependency]
