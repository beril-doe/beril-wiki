---
type: "Summary"
description: "Cross-database consistency of Pseudomonas FW300-N2E3 metabolism across Web of Microbes exometabolomics, Fitness Browser gene fitness, BacDive species-level utilization and GapMind pathway predictions, with sample-size-aware grading of discordances."
doc_type: "short"
full_text: "sources/fw300_metabolic_consistency__REPORT.md"
---
# Metabolic Consistency of Pseudomonas FW300-N2E3 Across Four KBase Data Lakehouse Databases

## Overview

This report integrates Web of Microbes (WoM) exometabolomics, Fitness Browser mutant-fitness data, BacDive species-level utilization phenotypes, and GapMind pathway predictions for *Pseudomonas* FW300-N2E3. It evaluates whether metabolite production, growth capability, species-level utilization, and pathway completeness agree across databases, while emphasizing sample-size-aware interpretation of discordances. [src: fw300_metabolic_consistency]

## Key Findings

### 1. High overall concordance

FW300-N2E3 produced or increased 58 WoM metabolites: 27 emerged and 31 increased. Of these, 21 could be cross-referenced against at least one other database. Among the 21 testable metabolites, 17/21 (81%) were fully concordant across all matched databases, 4/21 (19%) were partially concordant, and none were fully discordant. The mean concordance score was 0.94. The remaining 37 metabolites (64%) were observed only in WoM and were not tested in BacDive, not predicted by GapMind, and not used as Fitness Browser conditions for this organism. [src: fw300_metabolic_consistency]

Across 41 individual metabolite-database comparisons, 37 were concordant (90.2%). Fitness Browser comparisons were concordant for 21/21 (100%) metabolites and GapMind comparisons for 13/13 (100%); BacDive utilization was the variable component, with 3/7 (43%) matched metabolites utilized. A binomial test comparing the BacDive utilization rate for WoM-produced metabolites, 3/7 (43%), with the overall *P. fluorescens* baseline, 22/80 (27.5%), gave p = 0.40. This showed no significant difference, so the metabolites FW300-N2E3 produces are utilized at a rate consistent with the species norm. The report therefore describes the 94% concordance as largely structural, because Fitness Browser and GapMind are invariably concordant with WoM production. [src: fw300_metabolic_consistency]

Excluding two approximate Fitness Browser matches—Cytosine→Cytidine and Uracil→Uridine—reduced the testable set from 21 to 19 and changed mean concordance from 0.937 to 0.930. Both approximate matches were already fully concordant, so the sensitivity analysis produced a negligible change. [src: fw300_metabolic_consistency]

![Concordance categories and cross-database coverage for 58 WoM-produced metabolites](figures/concordance_summary.png)
*Figure: two-panel figure with a concordance-category pie chart and a cross-database coverage histogram for the 58 WoM-produced metabolites.* [src: fw300_metabolic_consistency]

![Consistency heatmap across WoM, Fitness Browser, BacDive, and GapMind](figures/consistency_heatmap.png)
*Figure: 58-row heatmap showing WoM, Fitness Browser, BacDive and GapMind signals per metabolite.* [src: fw300_metabolic_consistency]

### 2. Tryptophan overflow is the strongest discordance

FW300-N2E3 increased tryptophan in its WoM exometabolome, had 231 genes with significant fitness effects when grown on tryptophan in Fitness Browser, and had a complete tryptophan biosynthesis pathway prediction from GapMind. In contrast, 0 out of 50 *P. fluorescens* strains in BacDive could utilize tryptophan as a carbon source, with high confidence based on n=50 and pct_positive=0.0 using per-strain consensus. The report calls this the most robust discordance in the dataset: the organism produces tryptophan and grows on it as a sole carbon source, but the species as a whole cannot catabolize it. It describes the pattern as consistent with tryptophan overflow metabolism serving a cross-feeding or signaling function rather than a catabolic one. Overflow, cross-feeding and signaling are interpretations, not directly measured functions. [src: fw300_metabolic_consistency]

This production-plus-growth-but-no-species-level-catabolism pattern is consistent with the hypothesis that tryptophan overflow metabolism serves cross-feeding or signaling rather than catabolism. The report treats this as the most robust production-versus-utilization discordance, not as evidence that FW300-N2E3 itself cannot grow on tryptophan. [src: fw300_metabolic_consistency]

### 3. GapMind predictions agree with experimental measurements

All 13 metabolites mapped to GapMind—lactate, valine, alanine, arginine, aspartate, glutamic acid, glycine, phenylalanine, proline, trehalose, tryptophan, malate, and lysine—had complete pathway predictions for FW300-N2E3. All 13 also showed growth in Fitness Browser experiments. The report interprets this 13/13 agreement between computational pathway prediction and experimental measurement as validation of GapMind for this organism. This is a single-organism result. [src: fw300_metabolic_consistency]

In its literature context, the report says this agreement aligns with Price et al. (2022), who reported high accuracy for GapMind pathway predictions when validated against fitness data. It also says GapMind 2024 (Price et al. 2024) further improved amino acid biosynthesis annotations. Both are external results, separate from the 13/13 agreement observed for FW300-N2E3. The report also claims that pangenome-level predictions in the KBase Data Lakehouse inherit this accuracy. That claim is an extrapolation, not a separate validation result. [src: fw300_metabolic_consistency]

### 4. Produced metabolites have rich fitness landscapes

Across 21 WoM metabolites with matching Fitness Browser experiments, FW300-N2E3 had significant effects for 601 unique genes and 4,764 total significant gene-condition hits, using |fit| > 1 and |t| > 4. The most genetically complex metabolisms were carnitine with 283 genes, alanine with 295 genes across D/L forms, arginine with 270 genes, and tryptophan with 231 genes. [src: fw300_metabolic_consistency]

![Number of significant fitness genes per WoM-produced metabolite](figures/fitness_hits_per_metabolite.png)
*Figure: horizontal bar chart of significant fitness genes per WoM-produced metabolite, separating detrimental from beneficial effects.* [src: fw300_metabolic_consistency]

A total of 231 genes were significant in 3 or more metabolite conditions, and the top 18 genes were significant in all 21 conditions. These broadly pleiotropic genes included homoserine O-acetyltransferase, ATP phosphoribosyltransferase, dihydroxy-acid dehydratase, isopropylmalate dehydrogenase, shikimate dehydrogenase, and imidazoleglycerol-phosphate dehydratase, representing methionine, histidine, branched-chain amino acid, leucine, aromatic amino acid, and histidine biosynthesis functions. The report interprets these as housekeeping fitness requirements rather than substrate-specific catabolism; the approximately 370 genes significant in only 1–2 conditions are treated as the more substrate-specific component. [src: fw300_metabolic_consistency]

The 7 Emerged metabolites had a mean of 184.4 +/- 115.5 significant genes, with means of 221.0 detrimental and 21.0 beneficial effects. The 14 Increased metabolites had a mean of 163.5 +/- 74.1 significant genes, with means of 206.5 detrimental and 12.8 beneficial effects. Emerged metabolites, which were produced de novo, showed slightly more fitness-important genes than Increased metabolites, which were already present but amplified. The variance was high. Both groups had strong detrimental-to-beneficial ratios of approximately 10:1, indicating that most significant genes were required for growth on the substrates rather than inhibitory. [src: fw300_metabolic_consistency]

### 5. BacDive discordances vary in evidentiary quality

Four metabolites showed WoM production but BacDive non-utilization. Tryptophan was Increased with 0+/50- BacDive utilization and high confidence at n=50; trehalose was Increased with 1+/5- and moderate confidence at n=6; lysine was Emerged with 0+/3- and moderate confidence at n=3; and glycine was Increased with 0+/1- and low confidence at n=1. [src: fw300_metabolic_consistency]

The report considers tryptophan the only high-confidence production-versus-utilization discordance. Trehalose (Increased; 1+/5-, moderate confidence at n=6) appears strain-variable, with 1/6 positive strains, suggesting that trehalose metabolism varies across *P. fluorescens* isolates, and is interpreted as more consistent with an osmoprotectant role than a carbon-source role. Lysine (Emerged; 0+/3-, n=3) has a consistent negative result but a small sample. Glycine (Increased; 0+/1-, n=1) has only one BacDive measurement, which the report grades as unreliable and insufficient for a conclusion. BacDive counts use per-strain consensus, applying majority vote among duplicate records per strain. [src: fw300_metabolic_consistency]

### 6. Three metabolites have four-way concordance

Malate was Increased by WoM, supported growth involving 92 Fitness Browser genes, was utilized by 49/49 BacDive strains (100%), and had a complete GapMind pathway. Arginine was Increased, supported growth involving 270 Fitness Browser genes, was utilized by 40/48 BacDive strains (83%), and had a complete GapMind pathway. Valine Emerged, supported growth involving 160 Fitness Browser genes, was utilized by 1/1 BacDive strain, and had a complete GapMind pathway; its utilization result rests on a single strain. These three metabolites are the report's gold-standard cases of four-way consistency. [src: fw300_metabolic_consistency]

## Cross-Database Coverage and Interpretation

Manual matching associated 28/58 WoM metabolites (48%) with Fitness Browser carbon or nitrogen source conditions, 8/58 (14%) with BacDive *P. fluorescens* utilization data, and 13/58 (22%) with GapMind pathway predictions. The low overlap reflects nomenclature differences and scope differences, including WoM compounds such as N-acetylated amino acids and nucleotide derivatives that were not tested in the other resources. [src: fw300_metabolic_consistency]

Of 31 Fitness Browser conditions mapped in the crosswalk, 7—4-aminobutanoate, 5-oxo-proline, Betaine, Guanine, Nicotinamide, Sarcosine, and trans-Aconitate—returned no FW300-N2E3 fitness data because no experiments existed for those conditions. The downstream fitness analysis therefore used only the 24 conditions with actual data. [src: fw300_metabolic_consistency]

The report distinguishes metabolite production from utilization: exometabolomics can measure overflow metabolism, biosynthetic byproduct release, or active secretion for ecological purposes, whereas BacDive growth assays measure utilization as a growth capability. Therefore, production and non-utilization are not intrinsically contradictory. [src: fw300_metabolic_consistency]

FW300-N2E3 was isolated from groundwater at the Oak Ridge Field Research Center in an ENIGMA SFA context. Citing Fritts et al. 2021 and Giri et al. 2021, the report proposes that tryptophan secretion by a prototroph unable to re-assimilate it is a hallmark of cross-feeding potential. On this view, the secreted tryptophan could supply essential amino acids to auxotrophic community members. The report also suggests that the 231 fitness-important genes for tryptophan growth point to complex regulatory and transport machinery rather than simple catabolism, which would fit a secretion or signaling role. Both proposals are inferences, not measurements of cross-feeding. The report identifies the pathway-level distinction between biosynthetic, catabolic, and regulatory fitness genes as unresolved because the planned NB04 analysis was deferred. [src: fw300_metabolic_consistency]

The report interprets trehalose production with low species-level catabolism—1/6 BacDive strains positive—as potentially reflecting osmoprotection rather than metabolic overflow. It connects this interpretation to prior observations of trehalose synthesis under osmotic stress in *Pseudomonas protegens*, which is closely related to *P. fluorescens*, and of ethanol-stimulated trehalose production in *Pseudomonas aeruginosa*. The report further suggests the hypothesis that trehalose secretion during growth on R2A medium, the condition WoM measured, reflects a constitutive stress-protection strategy rather than metabolic overflow. These studies of other organisms provide context only. They do not directly test the mechanism in FW300-N2E3, so the osmoprotection explanation remains a hypothesis. [src: fw300_metabolic_consistency]

## Literature Context

The report cites Ramoneda et al. (2023), who mapped amino acid auxotrophies across thousands of bacterial genomes and found tryptophan auxotrophy to be particularly common. The report suggests this creates ecological niches for tryptophan-producing prototrophs like FW300-N2E3, but that niche is an extrapolation, not a measurement in this study. The report also cites Yousif et al. (2025), who found that obligate metabolite cross-feeding is common in soil microbial communities, with amino acids as key exchanged currency. Cross-feeding was not measured for FW300-N2E3. [src: fw300_metabolic_consistency]

The report also aligns the tryptophan finding with two further studies. Fritts et al. (2021) reviewed extracellular metabolism as a driver of microbial cross-feeding. Sibanyoni et al. (2025) documented amino acid cross-feeding between *Priestia megaterium* and *P. fluorescens* in the rhizosphere. Neither study is a direct FW300-N2E3 measurement, so the cross-feeding interpretation remains a hypothesis. [src: fw300_metabolic_consistency]

## Data Sources and Outputs

- `kescience_webofmicrobes` (tables `observation`, `organism`, `compound`, `environment`, `project`) supplied the exometabolomic profile of FW300-N2E3. [src: fw300_metabolic_consistency]
- `kescience_fitnessbrowser` (tables `genefitness`, `experiment`, `gene`, `seedannotation`) supplied gene fitness on carbon and nitrogen sources. [src: fw300_metabolic_consistency]
- `kescience_bacdive` (tables `metabolite_utilization`, `strain`, `taxonomy`) supplied species-level metabolite utilization. [src: fw300_metabolic_consistency]
- `kbase_ke_pangenome` (table `gapmind_pathways`) supplied pathway-completeness predictions. [src: fw300_metabolic_consistency]

Web of Microbes (WoM) is described in the report's cited reference as a curated microbial exometabolomics database for linking chemistry and microbes. The project outputs include a per-metabolite fitness summary (`data/wom_fb_summary.tsv`, 31 rows) and a full consistency matrix with concordance categories (`data/consistency_matrix.tsv`, 58 rows); the notebook `02_wom_fb_integration.ipynb` integrates WoM production with Fitness Browser gene fitness and identifies significant genes per metabolite. [src: fw300_metabolic_consistency]

## Caveats and Limitations

- Only 21/58 WoM metabolites (36%) could be tested against any other database, and only 3 metabolites had four-way coverage. The untested 64% may contain additional discordances. [src: fw300_metabolic_consistency]
- WoM exometabolomics was measured on R2A rich medium, whereas Fitness Browser fitness was measured on minimal medium with single carbon or nitrogen sources; condition-dependent metabolism limits direct comparison. [src: fw300_metabolic_consistency]
- BacDive aggregates *P. fluorescens* strains and, under GTDB reclassification, spans a broad clade identified as *Pseudomonas_E fluorescens_E*. Per-strain consensus deduplication, a majority vote among duplicate records per strain, was applied before species-level utilization rates were computed. However, strain-level variation (e.g., trehalose: 1/6 positive) means the species consensus may not reflect FW300-N2E3's specific capabilities. [src: fw300_metabolic_consistency]
- The report states in its literature-context discussion that only tryptophan, with n=52, has sufficient data for a confident conclusion, while its primary tryptophan result reports 0+/50- with n=50. This difference is retained rather than reconciled because the document gives both values. [src: fw300_metabolic_consistency]
- Manual name matching identified 28 WoM–Fitness Browser and 8 WoM–BacDive matches; two Fitness Browser matches were approximate base-to-nucleoside mappings. Additional matches may have been missed because of nomenclature differences, although excluding the two approximate matches changed mean concordance only from 0.937 to 0.930. [src: fw300_metabolic_consistency]
- Fitness Browser coverage includes pleiotropic housekeeping genes: the top 18 genes were significant across all 21 conditions because of amino acid biosynthesis requirements rather than substrate-specific catabolism. Separating housekeeping and substrate-specific signals is needed to sharpen WoM–Fitness Browser integration. [src: fw300_metabolic_consistency]
- The planned NB04 pathway-level analysis, which would map fitness-important genes to specific GapMind pathway steps, was deferred. This limits mechanistic interpretation of the tryptophan overflow hypothesis. [src: fw300_metabolic_consistency]
- BacDive compound coverage varies from 1 to 51 strains, and raw records can be higher because of duplicate entries per strain; sample size must therefore accompany consensus utilization values. [src: fw300_metabolic_consistency]

## Future Directions

- **Pathway-level analysis (NB04)**: map fitness-important genes to specific GapMind pathway steps to determine whether tryptophan fitness genes are biosynthetic, catabolic or regulatory. The report leaves these roles unresolved; this mapping would distinguish overflow metabolism from active catabolism. [src: fw300_metabolic_consistency]
- **Cross-species comparison**: repeat the analysis for other ENIGMA isolates with both WoM and Fitness Browser data, for example *Pseudomonas stutzeri* RCH2, to test whether the production-versus-utilization pattern is species-specific or general. RCH2 is a proposed candidate, not an organism tested here, so whether the pattern generalizes remains untested. [src: fw300_metabolic_consistency]
- **Expanded BacDive matching**: use chemical identifiers (InChIKey, CHEBI) rather than name matching to increase the WoM–BacDive overlap beyond 8 metabolites. [src: fw300_metabolic_consistency]
- **Community metabolic modeling**: use the tryptophan overflow finding to parameterize a community metabolic model predicting cross-feeding between FW300-N2E3 and known tryptophan auxotrophs in the Oak Ridge groundwater community. The report proposes these predictions; it does not report them. [src: fw300_metabolic_consistency]
- **Condition-dependent exometabolomics**: compare WoM profiles across growth media to determine which metabolites are constitutively produced and which are medium-dependent. The report does not establish this. [src: fw300_metabolic_consistency]

## Slots Into

- [[concepts/multi-omics-integration]] — Cross-database integration of WoM exometabolomics, Fitness Browser gene fitness, BacDive phenotypes, and GapMind pathway predictions establishes a 94% mean concordance while exposing coverage and interpretation limits. [src: fw300_metabolic_consistency]
- [[concepts/condition-specific-fitness]] — The 4,764 significant gene-condition hits, 601 unique genes, and separation of pleiotropic housekeeping from substrate-specific fitness effects extend interpretation of condition-dependent gene fitness. [src: fw300_metabolic_consistency]
- [[concepts/metabolic-model-gapfilling]] — The 13/13 complete GapMind predictions concordant with Fitness Browser growth and WoM production provide organism-level evidence for pathway-gap assessment. [src: fw300_metabolic_consistency]
- [[concepts/cross-tenant-data-bridging]] — The report demonstrates a cross-database metabolite crosswalk spanning four KBase Data Lakehouse collections and quantifies how nomenclature and scope constrain evidence joining. [src: fw300_metabolic_consistency]
- [[concepts/cross-condition-metabolic-comparability]] — The 21/58 testable metabolites, the 0.94 mean concordance (largely structural) and the R2A versus minimal-medium contrast show how far cross-database metabolic comparison can reach. [src: fw300_metabolic_consistency]
- [[concepts/sample-size-aware-phenotype-consensus]] — The high, moderate and low confidence grades for BacDive discordances (n=50, n=6, n=3, n=1) and the unreconciled n=50 versus n=52 tryptophan counts illustrate per-strain consensus with sample-size grading. [src: fw300_metabolic_consistency]
- [[concepts/occurrence-versus-catabolic-activity]] — Exometabolomic production and growth-assay utilization measure different capabilities, as the tryptophan and trehalose cases show. [src: fw300_metabolic_consistency]
- [[concepts/computational-pathway-prediction-validation]] — The 13/13 GapMind–Fitness Browser agreement and the four-way concordant cases are single-organism validation evidence. [src: fw300_metabolic_consistency]
- [[concepts/community-metabolic-interdependence]] — The hypothesized tryptophan cross-feeding by an Oak Ridge groundwater prototroph is supported only by literature context. [src: fw300_metabolic_consistency]
- [[concepts/biosynthetic-prototrophy-and-auxotrophy]] — The cited prevalence of tryptophan auxotrophy frames FW300-N2E3 as a candidate tryptophan-producing prototroph. [src: fw300_metabolic_consistency]
- [[concepts/callability-limited-comparative-inference]] — With only 36% of metabolites testable and 3 with four-way coverage, discordances may be hidden in the untested 64%. [src: fw300_metabolic_consistency]
