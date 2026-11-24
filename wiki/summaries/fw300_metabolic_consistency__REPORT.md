---
type: "Summary"
description: "Summary of the project Metabolic Consistency of Pseudomonas FW300-N2E3 Across Four KBase Data Lakehouse Databases."
doc_type: "short"
full_text: "sources/fw300_metabolic_consistency__REPORT.md"
---
# Metabolic Consistency of Pseudomonas FW300-N2E3 Across Four KBase Data Lakehouse Databases

The evidence comes from one organism and a small set of matched metabolites. [src: fw300_metabolic_consistency] The report claims the first systematic single-organism cross-database metabolic consistency analysis spanning exometabolomics, mutant fitness, species phenotypes and pathway predictions. [src: fw300_metabolic_consistency] It states that integrating Web of Microbes (WoM) exometabolomics with Fitness Browser (FB) gene fitness is feasible and yields biologically meaningful insights. [src: fw300_metabolic_consistency]

## Key Findings

### Overall concordance

The 21 testable metabolites were mostly concordant. 17/21 (81%) were fully concordant, 4/21 (19%) were partially concordant, and none were fully discordant. The mean concordance score was 0.94. [src: fw300_metabolic_consistency] Across all 41 metabolite-database comparisons, 37 were concordant (90.2%). [src: fw300_metabolic_consistency]

The report calls the 94% concordance largely structural. FB (21/21 = 100%) and GapMind (13/13 = 100%) are invariably concordant with WoM production. [src: fw300_metabolic_consistency] BacDive is the only variable component, with 3/7 = 43% of matched metabolites utilized. [src: fw300_metabolic_consistency] A binomial test found no significant difference between this 43% and the overall *P. fluorescens* baseline of 22/80 = 27.5% (p = 0.40). The report reads this as the produced metabolites being utilized at a rate consistent with the species norm. [src: fw300_metabolic_consistency]

Two FB matches were approximate base-to-nucleoside mappings: Cytosine→Cytidine and Uracil→Uridine, flagged fb_match_quality=approximate in the crosswalk. [src: fw300_metabolic_consistency] Excluding them reduced testable metabolites from 21 to 19 and shifted mean concordance from 0.937 to 0.930. The report calls this negligible because both were already fully concordant. [src: fw300_metabolic_consistency] A sensitivity analysis found that excluding them did not affect concordance results. [src: fw300_metabolic_consistency]

### Matching coverage

The comparison started from 58 WoM metabolites, 27 Emerged and 31 Increased. [src: fw300_metabolic_consistency] Matches were 28/58 (48%) to FB carbon/nitrogen source conditions, 8/58 (14%) to BacDive *P. fluorescens* utilization data, and 13/58 (22%) to GapMind pathway predictions. [src: fw300_metabolic_consistency] Manual curation identified 28 WoM–FB and 8 WoM–BacDive matches. [src: fw300_metabolic_consistency] The remaining 37 metabolites (64%) were observed only in WoM. [src: fw300_metabolic_consistency] The report attributes the low matching to nomenclature and scope differences. For example, N-acetylated amino acids and nucleotide derivatives have not been tested in FB, BacDive or GapMind. [src: fw300_metabolic_consistency] Additional matches may exist but were missed because of nomenclature differences. [src: fw300_metabolic_consistency]

Of 31 FB conditions mapped in the crosswalk, 7 had no FW300-N2E3 experiments: 4-aminobutanoate, 5-oxo-proline, Betaine, Guanine, Nicotinamide, Sarcosine and trans-Aconitate. [src: fw300_metabolic_consistency] The downstream analysis uses only the 24 conditions with actual fitness data. [src: fw300_metabolic_consistency]

### Tryptophan: production without utilization

FW300-N2E3 increases tryptophan in its exometabolome (WoM action = I). [src: fw300_metabolic_consistency] It has 231 genes with significant fitness on tryptophan in FB. [src: fw300_metabolic_consistency] GapMind predicts a complete tryptophan biosynthesis pathway. [src: fw300_metabolic_consistency] Yet 0 of 50 *P. fluorescens* strains in BacDive utilize tryptophan as a carbon source (high confidence, per-strain consensus). [src: fw300_metabolic_consistency] The report calls this the most robust discordance in the dataset. The organism produces tryptophan and grows on it as a sole carbon source, but the species as a whole cannot catabolize it. [src: fw300_metabolic_consistency]

The report proposes a tryptophan overflow hypothesis, supported by converging evidence from four databases: produced (WoM), genetically important for growth (FB), complete biosynthetic pathway (GapMind), and universally non-utilizable at the species level (BacDive). [src: fw300_metabolic_consistency] It proposes, as interpretation, that this fits overflow metabolism serving a cross-feeding or signaling function. [src: fw300_metabolic_consistency] It suggests the 231 fitness genes reflect complex regulatory and transport machinery rather than simple catabolism. [src: fw300_metabolic_consistency] It reads tryptophan secretion by a prototroph that cannot re-assimilate it as a sign of cross-feeding potential for auxotrophic community members. [src: fw300_metabolic_consistency] It cites Ramoneda et al. (2023), who found tryptophan auxotrophy particularly common across thousands of bacterial genomes. [src: fw300_metabolic_consistency] The report says the tryptophan finding aligns with Fritts et al. (2021), who reviewed extracellular metabolism as a driver of microbial cross-feeding. [src: fw300_metabolic_consistency] It also cites Sibanyoni et al. (2025), who documented amino acid cross-feeding between *Priestia megaterium* and *P. fluorescens* in the rhizosphere. [src: fw300_metabolic_consistency] It cites Yousif et al. (2025) as finding common obligate metabolite cross-feeding in soil communities, with amino acids as key exchanged currency. [src: fw300_metabolic_consistency] These are hypotheses, not measurements.

Four metabolites showed WoM production with BacDive non-utilization, but their reliability varied widely. [src: fw300_metabolic_consistency] BacDive counts use per-strain consensus, a majority vote among duplicate records per strain, applied before computing species-level utilization rates. [src: fw300_metabolic_consistency]

| Metabolite | WoM action | BacDive | Confidence and reading |
|---|---|---|---|
| Tryptophan | Increased | 0+/50- | High (n=50); robust overflow/cross-feeding signal [src: fw300_metabolic_consistency] |
| Trehalose | Increased | 1+/5- | Moderate (n=6); strain-variable, likely osmoprotectant, not catabolic [src: fw300_metabolic_consistency] |
| Lysine | Emerged | 0+/3- | Moderate (n=3); consistent negatives, small sample [src: fw300_metabolic_consistency] |
| Glycine | Increased | 0+/1- | Low (n=1); single measurement, unreliable [src: fw300_metabolic_consistency] |

Only tryptophan reaches high confidence for a genuine production-versus-utilization discordance. [src: fw300_metabolic_consistency] The trehalose result (1/6 positive) suggests that trehalose metabolism varies across *P. fluorescens* isolates. [src: fw300_metabolic_consistency] The report interprets trehalose production, with only 1/6 BacDive strains positive, as likely reflecting an osmoprotectant role. [src: fw300_metabolic_consistency] It cites Wang et al. (2020), who showed that *Pseudomonas protegens* upregulates trehalose synthesis under osmotic stress [src: fw300_metabolic_consistency], and Harty et al. (2019), who demonstrated ethanol-stimulated trehalose production in *Pseudomonas aeruginosa*. [src: fw300_metabolic_consistency] It hypothesizes that trehalose secretion on R2A medium may reflect constitutive stress protection rather than metabolic overflow. [src: fw300_metabolic_consistency] The single glycine measurement is insufficient to draw conclusions. [src: fw300_metabolic_consistency]

The report's central point is that exometabolomic production and BacDive growth-assay utilization test fundamentally different capabilities. [src: fw300_metabolic_consistency] A bacterium can produce a metabolite by overflow metabolism, biosynthetic byproduct release or ecological secretion without being able to catabolize it for energy. [src: fw300_metabolic_consistency]

### GapMind agreement

Every metabolite mapped to a GapMind pathway had a "complete" prediction for FW300-N2E3. These were lactate, valine, alanine, arginine, aspartate, glutamic acid, glycine, phenylalanine, proline, trehalose, tryptophan, malate and lysine. [src: fw300_metabolic_consistency] All 13 also showed growth in FB experiments. [src: fw300_metabolic_consistency] The report reads this perfect agreement as validating GapMind's accuracy for this organism [src: fw300_metabolic_consistency] and its utility for this organism. [src: fw300_metabolic_consistency] This aligns with Price et al. (2022), who reported high accuracy for GapMind predictions validated against fitness data. [src: fw300_metabolic_consistency] The report adds that GapMind 2024 improved amino acid biosynthesis annotations and that pangenome-level predictions in the KBase Data Lakehouse inherit this accuracy. [src: fw300_metabolic_consistency]

### Fitness genes

Across the 21 WoM metabolites with matching FB experiments, FW300-N2E3 had significant fitness effects (|fit| > 1, |t| > 4) for 601 unique genes. [src: fw300_metabolic_consistency] There were 4,764 significant gene-condition hits. [src: fw300_metabolic_consistency] The most genetically complex metabolisms were carnitine (283 genes), alanine (295 genes across D/L forms), arginine (270 genes) and tryptophan (231 genes). [src: fw300_metabolic_consistency]

231 genes were significant in 3+ metabolite conditions. [src: fw300_metabolic_consistency] The top 18, significant in all 21 conditions, are amino acid biosynthesis enzymes. Examples are homoserine O-acetyltransferase (methionine), ATP (adenosine triphosphate) phosphoribosyltransferase (histidine), dihydroxy-acid dehydratase (branched-chain amino acids), isopropylmalate dehydrogenase (leucine), shikimate dehydrogenase (aromatic amino acids) and imidazoleglycerol-phosphate dehydratase (histidine). [src: fw300_metabolic_consistency] They are essential biosynthesis genes, not substrate-specific catabolism genes. [src: fw300_metabolic_consistency] The report interprets these as housekeeping fitness, essential for growth on any minimal medium, rather than substrate-specific metabolism. [src: fw300_metabolic_consistency] About 370 genes significant in only 1-2 conditions are the truly substrate-specific ones. They include carnitine-specific transporters, lactate dehydrogenases and trehalose-specific phosphotransferases. [src: fw300_metabolic_consistency] The report recommends separating the housekeeping and substrate-specific components in future WoM–FB integration. [src: fw300_metabolic_consistency]

Emerged metabolites (produced de novo) showed slightly more fitness-important genes than Increased metabolites (already present but amplified), though with high variance. [src: fw300_metabolic_consistency]

| WoM action | N metabolites | Mean sig genes | Mean detrimental | Mean beneficial |
|---|---|---|---|---|
| Emerged | 7 | 184.4 +/- 115.5 | 221.0 | 21.0 [src: fw300_metabolic_consistency] |
| Increased | 14 | 163.5 +/- 74.1 | 206.5 | 12.8 [src: fw300_metabolic_consistency] |

Both categories had detrimental:beneficial ratios of about 10:1. The report reads this as most fitness-significant genes being required for growth rather than inhibitory. [src: fw300_metabolic_consistency]

### Metabolites concordant across all four databases

Three metabolites achieved concordance across all four databases. [src: fw300_metabolic_consistency]

- Malate: Increased, FB growth (92 genes), BacDive utilized (49/49, 100%), GapMind complete. [src: fw300_metabolic_consistency]
- Arginine: Increased, FB growth (270 genes), BacDive utilized (40/48, 83%), GapMind complete. [src: fw300_metabolic_consistency]
- Valine: Emerged, FB growth (160 genes), BacDive utilized (1/1), GapMind complete. [src: fw300_metabolic_consistency]

The report treats these as the gold standard of cross-database consistency. FW300-N2E3 produces and grows on them, the species utilizes them, and their pathways are computationally complete. [src: fw300_metabolic_consistency]

## Data and Methods

FW300-N2E3 was isolated from groundwater at the Oak Ridge Field Research Center (ENIGMA SFA), where it exists in complex microbial communities. [src: fw300_metabolic_consistency] Production calls come from WoM, with FB fitness experiments, BacDive *P. fluorescens* utilization data and GapMind pathway predictions as comparators. [src: fw300_metabolic_consistency] BacDive counts use per-strain consensus. [src: fw300_metabolic_consistency]

The KBase Data Lakehouse sources were kescience_webofmicrobes (observation, organism, compound, environment, project) [src: fw300_metabolic_consistency], kescience_fitnessbrowser (genefitness, experiment, gene, seedannotation) [src: fw300_metabolic_consistency], kescience_bacdive (metabolite_utilization, strain, taxonomy) [src: fw300_metabolic_consistency] and kbase_ke_pangenome (gapmind_pathways). [src: fw300_metabolic_consistency] The metabolite crosswalk unifies 58 metabolites across the four databases. [src: fw300_metabolic_consistency] BacDive aggregates *P. fluorescens* strains across a broad clade, designated *Pseudomonas_E fluorescens_E* under GTDB reclassification. [src: fw300_metabolic_consistency]

## Caveats and Open Work

- Only 21 of 58 metabolites were testable, and 37 (64%) were seen only in WoM. [src: fw300_metabolic_consistency] Only 3 had four-way coverage, and the untested 64% may hold additional discordances. [src: fw300_metabolic_consistency]
- The report describes the high concordance as largely structural, because FB (21/21 = 100%) and GapMind (13/13 = 100%) are invariably concordant with WoM production. [src: fw300_metabolic_consistency]
- The BacDive comparison rests on 7 matched metabolites, and the 43% rate did not differ significantly from the species baseline. [src: fw300_metabolic_consistency]
- Trehalose, lysine and glycine have small BacDive samples, so only tryptophan is a high-confidence discordance. [src: fw300_metabolic_consistency] The report states that only tryptophan has sufficient BacDive data for a confident conclusion, and it gives n=52 for this statement. [src: fw300_metabolic_consistency] The report does not explain how this n=52 relates to the 50 strains in the tryptophan comparison above. [src: fw300_metabolic_consistency] Sample-size-based scoring shows many BacDive discordances are data-limited. [src: fw300_metabolic_consistency]
- BacDive compound coverage varies from 1 to 51 strains under per-strain consensus, and raw records can be higher because of duplicates. [src: fw300_metabolic_consistency]
- Using BacDive consensus without sample size can produce false discordance calls. [src: fw300_metabolic_consistency] Strain variation, such as trehalose at 1/6 positive, means species consensus may not reflect FW300-N2E3's capabilities. [src: fw300_metabolic_consistency]
- Two FB matches were approximate; excluding them changed little. [src: fw300_metabolic_consistency]
- Low matching rates reflect nomenclature and scope differences. [src: fw300_metabolic_consistency]
- WoM used R2A rich medium, whereas FB used minimal medium with single C/N sources, so some WoM metabolites may only be produced on rich media. [src: fw300_metabolic_consistency]
- The planned NB04 mapping of fitness genes to GapMind pathway steps was deferred. It would strengthen the mechanistic interpretation of the tryptophan overflow hypothesis. [src: fw300_metabolic_consistency]
- The report notes that no published study has systematically compared WoM exometabolomic profiles with FB gene fitness data, despite their shared ENIGMA/Arkin Lab origin. [src: fw300_metabolic_consistency]

Next analyses the report proposes:
- Pathway-level analysis (NB04) to learn whether tryptophan fitness genes are biosynthetic, catabolic or regulatory, which would distinguish overflow metabolism from active catabolism. [src: fw300_metabolic_consistency]
- Repeating the analysis in other ENIGMA isolates, such as *Pseudomonas stutzeri* RCH2, to test whether the pattern is species-specific or general. [src: fw300_metabolic_consistency]
- Using InChIKey and CHEBI identifiers instead of name matching to expand WoM–BacDive overlap beyond 8 metabolites. [src: fw300_metabolic_consistency]
- Using the tryptophan finding to parameterize a community metabolic model of cross-feeding with tryptophan auxotrophs in the Oak Ridge groundwater community. [src: fw300_metabolic_consistency]
- Comparing WoM profiles across growth media to separate constitutive from medium-dependent production. [src: fw300_metabolic_consistency]

## Slots Into

- [[concepts/cross-database-concordance-of-metabolite-evidence]]: 17/21 fully concordant and mean concordance 0.94, largely structural. [src: fw300_metabolic_consistency]
- [[concepts/metabolite-production-versus-utilization-discordance]]: tryptophan is produced but not utilized by the species. [src: fw300_metabolic_consistency]
- [[concepts/housekeeping-versus-substrate-specific-fitness-genes]]: the top 18 pleiotropic biosynthesis genes versus about 370 substrate-specific genes. [src: fw300_metabolic_consistency]
- [[concepts/reliability-of-species-level-bacdive-consensus-phenotypes]]: confidence varies with BacDive sample size, from n=50 to n=1. [src: fw300_metabolic_consistency]
