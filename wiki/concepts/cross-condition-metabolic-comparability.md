---
type: "Concept"
description: "Metabolic evidence can diverge when assays measure different conditions or capabilities."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md"]
---
# Metabolic evidence is condition-dependent across assays and databases

Metabolic evidence is not directly interchangeable when assays measure different biological capabilities or environmental conditions. The [[summaries/fw300_metabolic_consistency__REPORT]] compared Web of Microbes exometabolomics, Fitness Browser mutant-fitness experiments, BacDive species-level utilization phenotypes, and GapMind pathway predictions for *Pseudomonas* FW300-N2E3, showing that apparent agreement depends on both assay scope and growth medium. [src: fw300_metabolic_consistency]

## Evidence for high concordance within the matched subset

FW300-N2E3 produced or increased 58 metabolites in Web of Microbes exometabolomics: 27 emerged and 31 increased. [src: fw300_metabolic_consistency] Only 21 of the 58 metabolites could be cross-referenced against at least one other database; 17/21 (81%) were fully concordant, 4/21 (19%) were partially concordant, and none were fully discordant, giving a mean concordance score of 0.94. [src: fw300_metabolic_consistency] Across 41 individual metabolite-database comparisons, 37 were concordant (90.2%); Fitness Browser comparisons were concordant for 21/21 (100%) metabolites and GapMind comparisons for 13/13 (100%), whereas BacDive utilization was concordant for 3/7 (43%) matched metabolites. [src: fw300_metabolic_consistency]

This high matched-set agreement supports cross-database integration when the metabolite identity, organismal context, and measured capability are aligned. [src: fw300_metabolic_consistency] It does not establish that the 37 untested metabolites are concordant, because those metabolites were observed only in Web of Microbes and were not tested in BacDive, not predicted by GapMind, and not used as Fitness Browser conditions for this organism. [src: fw300_metabolic_consistency]

## Why assay outputs can disagree

Web of Microbes exometabolomics measured compounds that FW300-N2E3 produced or increased, whereas BacDive growth assays measured whether *Pseudomonas fluorescens* strains could utilize compounds as carbon sources. [src: fw300_metabolic_consistency] Production can therefore represent overflow metabolism, biosynthetic byproduct release, or active ecological secretion without implying that the producing organism can catabolize the compound. [src: fw300_metabolic_consistency] The report's 21/58 (36%) cross-database testable fraction and 37/58 (64%) Web-of-Microbes-only fraction show that database coverage is itself a constraint on comparability. [src: fw300_metabolic_consistency]

The media also differed: Web of Microbes exometabolomics was measured on R2A rich medium, whereas Fitness Browser experiments used minimal medium with single carbon or nitrogen sources. [src: fw300_metabolic_consistency] Consequently, a metabolite detected in the rich-medium exometabolome and a fitness effect measured during single-substrate growth are condition-specific observations rather than identical tests of metabolism. [src: fw300_metabolic_consistency] This limitation refines interpretation of [[concepts/multi-omics-integration]] and [[concepts/cross-tenant-data-bridging]] by showing that successful data joining requires semantic alignment in addition to matching names. [src: fw300_metabolic_consistency]

## Tryptophan illustrates capability-specific discordance

Tryptophan was increased in the FW300-N2E3 exometabolome, had 231 genes with significant Fitness Browser effects during growth on tryptophan, and had a complete tryptophan biosynthesis pathway prediction from GapMind. [src: fw300_metabolic_consistency] In contrast, 0 out of 50 *Pseudomonas fluorescens* strains in BacDive utilized tryptophan as a carbon source, with n=50 and pct_positive=0.0 under per-strain consensus. [src: fw300_metabolic_consistency]

This pattern supports the hypothesis that tryptophan production can coexist with growth-associated genetic requirements without species-level tryptophan catabolism, potentially because of overflow, signaling, or cross-feeding. [src: fw300_metabolic_consistency] It does not show that FW300-N2E3 itself cannot grow on tryptophan, because the BacDive result aggregates *P. fluorescens* strains rather than testing this isolate specifically. [src: fw300_metabolic_consistency] The report also retains a separate literature-context value of n=52 for tryptophan alongside the primary 0+/50- result with n=50, because the document does not reconcile those values. [src: fw300_metabolic_consistency]

## Sample size and taxonomic aggregation shape comparability

BacDive utilization counts were computed after applying per-strain consensus, with duplicate records resolved by majority vote within strain. [src: fw300_metabolic_consistency] The four production-versus-non-utilization cases had different evidentiary strength: tryptophan was 0+/50- with high confidence, trehalose was 1+/5- with moderate confidence, lysine was 0+/3- with moderate confidence, and glycine was 0+/1- with low confidence. [src: fw300_metabolic_consistency]

These results support reporting sample size with every species-level utilization rate rather than treating positive or negative proportions as equally informative. [src: fw300_metabolic_consistency] BacDive aggregates *P. fluorescens* strains across a broad clade identified under GTDB reclassification as *Pseudomonas_E fluorescens_E*, so its consensus may not represent FW300-N2E3 specifically. [src: fw300_metabolic_consistency] This taxonomic and sampling limitation is relevant to [[concepts/taxonomic-resolution-dependent-functional-inference]] and [[concepts/metadata-resolution-and-within-species-heterogeneity]]. [src: fw300_metabolic_consistency]

## Fitness evidence requires condition-aware interpretation

Across 21 WoM metabolites with matching Fitness Browser experiments, FW300-N2E3 had significant effects for 601 unique genes and 4,764 total significant gene-condition hits, using |fit| > 1 and |t| > 4. [src: fw300_metabolic_consistency] A total of 231 genes were significant in 3 or more metabolite conditions, while the top 18 genes were significant in all 21 conditions. [src: fw300_metabolic_consistency] The broadly pleiotropic genes included functions in methionine, histidine, branched-chain amino acid, leucine, and aromatic amino acid biosynthesis, and were interpreted as housekeeping fitness requirements rather than substrate-specific catabolism. [src: fw300_metabolic_consistency]

The approximately 370 genes significant in only 1–2 conditions were treated as the more substrate-specific component. [src: fw300_metabolic_consistency] Emerged metabolites had a mean of 184.4 +/- 115.5 significant genes, including means of 221.0 detrimental and 21.0 beneficial effects, while increased metabolites had a mean of 163.5 +/- 74.1 significant genes, including means of 206.5 detrimental and 12.8 beneficial effects. [src: fw300_metabolic_consistency] Both groups therefore had detrimental-to-beneficial ratios of approximately 10:1, indicating that most significant genes were required for growth on the tested substrates rather than inhibitory. [src: fw300_metabolic_consistency]

These findings support [[concepts/condition-specific-fitness]] while cautioning that a large fitness landscape does not by itself identify the mechanism responsible for metabolite production or utilization. [src: fw300_metabolic_consistency] The deferred NB04 analysis, which would have mapped fitness-important genes to specific GapMind pathway steps, leaves the distinction between biosynthetic, catabolic, and regulatory fitness genes unresolved. [src: fw300_metabolic_consistency]

## Four-way agreement is possible but limited

Malate, arginine, and valine were the three metabolites with four-way coverage across production, Fitness Browser growth, BacDive utilization, and GapMind pathway prediction. [src: fw300_metabolic_consistency] Malate was increased, supported growth involving 92 Fitness Browser genes, was utilized by 49/49 BacDive strains (100%), and had a complete GapMind pathway. [src: fw300_metabolic_consistency] Arginine was increased, supported growth involving 270 Fitness Browser genes, was utilized by 40/48 BacDive strains (83%), and had a complete GapMind pathway. [src: fw300_metabolic_consistency] Valine emerged, supported growth involving 160 Fitness Browser genes, was utilized by 1/1 BacDive strain, and had a complete GapMind pathway. [src: fw300_metabolic_consistency]

These three cases are the report's gold-standard examples of four-way consistency, but they represent only 3 of 58 Web-of-Microbes metabolites. [src: fw300_metabolic_consistency] Their limited number means that strong agreement should be treated as demonstrated for particular metabolite-condition combinations, not as evidence that all exometabolomic signals will transfer across databases. [src: fw300_metabolic_consistency]

## Open Directions

- Map the 601 unique Fitness Browser genes and 4,764 significant gene-condition hits to GapMind pathway steps using the deferred NB04 analysis, and test whether genes associated with FW300-N2E3 tryptophan production are biosynthetic, catabolic, or regulatory. [src: fw300_metabolic_consistency]
- Repeat the four-database comparison for additional ENIGMA isolates, including *Pseudomonas stutzeri* RCH2, and test whether the observed concordance and discordance patterns are isolate-specific or reproducible across organisms. [src: fw300_metabolic_consistency]
- Expand Web-of-Microbes–BacDive matching with InChIKey or CHEBI identifiers, and test whether identifier-based joining increases the 8/58 BacDive match count without conflating biologically distinct compounds. [src: fw300_metabolic_consistency]
- Use community metabolic modeling for the Oak Ridge groundwater community to test whether FW300-N2E3 tryptophan secretion can support auxotrophic community members under the relevant environmental conditions. [src: fw300_metabolic_consistency]
- Compare FW300-N2E3 Web-of-Microbes profiles across growth media to test which metabolites are constitutive and which are medium-dependent. [src: fw300_metabolic_consistency]
