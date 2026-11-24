---
type: "Summary"
description: "Summary of the project PGP Gene Distribution Across Environments & Pangenomes."
doc_type: "short"
full_text: "sources/pgp_pangenome_ecology__REPORT.md"
---
# PGP Gene Distribution Across Environments & Pangenomes

This page summarises the project PGP Gene Distribution Across Environments & Pangenomes. It asks how plant-growth-promoting (PGP) genes co-occur, where they are enriched, and how they sit in pangenomes. The evidence is a cross-species survey of 11,272 species carrying at least one PGP gene, with statistical tests on each question. [src: pgp_pangenome_ecology] The report claims this is the first such analysis across the full KBase Data Lakehouse pangenome (27K species, 293K genomes), a ~100× scale-up over prior comparative genomic studies of PGPB. [src: pgp_pangenome_ecology] Several interpretations (separate guilds, vertical inheritance, root-exudate tryptophan, an hcn role in the rhizosphere niche) are the report's proposals, not direct measurements. [src: pgp_pangenome_ecology] The report concludes that the canonical PGPB phenotype in agricultural inoculants centers on pqqC + acdS rather than nitrogen fixation. [src: pgp_pangenome_ecology]

## Key Findings

### Co-occurrence of PGP genes
Most focal gene pairs are associated, in both directions. See [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds]].

- Of 10 focal pairs, 8 were significant after Benjamini-Hochberg false discovery rate (BH-FDR) correction. [src: pgp_pangenome_ecology]
- Five pairs showed positive co-occurrence and three showed negative co-occurrence. [src: pgp_pangenome_ecology]
- The strongest positive pair was pqqC × acdS (odds ratio, OR = 7.24, n = 286 co-occurring species, q = 1.2e-83). Here pqqC stands for phosphate solubilization through pyrroloquinoline quinone (PQQ) cofactor biosynthesis, and acdS for ethylene reduction through ACC (1-aminocyclopropane-1-carboxylate) deaminase. [src: pgp_pangenome_ecology]
- The report says this association aligns with trait co-occurrence in curated effective-inoculant collections (Glick 2014; Vejan et al. 2016), but demonstrates it at pangenome scale for the first time. [src: pgp_pangenome_ecology]
- pqqC also co-occurred with hcnC (OR = 1.91) and ipdC (OR = 1.55). The report calls this a "rhizosphere effectiveness" module. [src: pgp_pangenome_ecology]
- The report states that hcnC co-occurs with pqqC (OR = 1.91), and suggests the hcnA–hcnC operon is part of the rhizosphere niche toolkit. [src: pgp_pangenome_ecology]
- nifH (nitrogen fixation) was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19). [src: pgp_pangenome_ecology]
- nifH showed no significant association with ipdC (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology]
- The report interprets this as diazotrophs forming a separate guild from pqqC/acdS-bearing rhizobacteria, with the classical PGPB suite mainly non-diazotrophic. This is an interpretation. [src: pgp_pangenome_ecology] It states that nifH constitutes a separate ecological guild with different co-occurrence partners and environmental distribution. [src: pgp_pangenome_ecology]
- Multi-trait species are rare: only 157 species (1.4%) carry ≥3 focal traits. [src: pgp_pangenome_ecology]
- The report names pqqC + acdS as the most common multi-trait genotype (n = 153), followed by nifH + pqqC (n = 225). The counts do not follow that ranking (225 is larger than 153), and the report does not explain the difference. It notes that nifH + pqqC co-occurs in some generalist lineages despite the overall negative association. [src: pgp_pangenome_ecology]

### Environmental enrichment
Three of five focal genes were enriched in soil/rhizosphere species (1,039 species) against 10,233 species from other environments (BH-FDR q < 0.05). [src: pgp_pangenome_ecology] The table shows which genes. nifH was depleted [src: pgp_pangenome_ecology], and ipdC did not differ significantly. [src: pgp_pangenome_ecology] See [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]].

| Gene | Soil/rhizosphere | Other | OR | q |
|---|---|---|---|---|
| acdS | 15.8% | 2.6% | 7.02 | 5.1e-62 [src: pgp_pangenome_ecology] |
| pqqC | 43.8% | 21.2% | 2.90 | 2.8e-53 [src: pgp_pangenome_ecology] |
| hcnC | 11.3% | 6.4% | 1.85 | 6.1e-08 [src: pgp_pangenome_ecology] |
| nifH | 12.9% | 19.7% | 0.60 | 5.5e-08 (depleted) [src: pgp_pangenome_ecology] |
| ipdC | 1.5% | 1.9% | 0.79 | 0.47 (not significant) [src: pgp_pangenome_ecology] |

- The report states that hcnC is significantly soil-enriched (OR = 1.85). [src: pgp_pangenome_ecology]
- The acdS enrichment (about 7×) survived phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61). [src: pgp_pangenome_ecology]
- It also held in a strict rhizosphere-only sensitivity analysis, using genomes with "rhizosphere" or "root nodule" in the isolation source (OR = 10.6, q = 7.6e-38). [src: pgp_pangenome_ecology]
- The report calls the pqqC–acdS module strongly rhizosphere-enriched (acdS OR = 7.0). [src: pgp_pangenome_ecology] It relates the acdS soil enrichment to Manter et al. (2023), who used direct acdS sequencing to show ACCD+ bacteria are more abundant in soil. [src: pgp_pangenome_ecology] It also cites the ecological model of Glick (1998) and Ravanbakhsh et al. (2017), in which ACC deaminase is advantageous in ethylene-rich root environments. [src: pgp_pangenome_ecology]
- Bacillota_A was an exception to nifH depletion (OR = ∞, q = 2.5e-4). The report attributes this to soil-specific anaerobic diazotrophs such as clostridia. [src: pgp_pangenome_ecology]
- The report attributes the overall nifH depletion to most nitrogen fixers in the database being aquatic/marine (cyanobacteria, Azotobacter) or host-associated (rhizobia). [src: pgp_pangenome_ecology] It says diazotrophs are depleted in soil-classified genomes relative to aquatic and host-associated environments. [src: pgp_pangenome_ecology]
- It reads this as consistent with nitrogen fixation being energetically expensive and most relevant in oligotrophic aquatic environments and specific symbioses rather than bulk soil. [src: pgp_pangenome_ecology] It also relates the depletion to Wardell et al. (2022), who note that nif gene mobility on symbiosis islands is mainly relevant in legume-associated Rhizobiales rather than free-living soil diazotrophs. [src: pgp_pangenome_ecology]
- For ipdC, the raw soil comparison was not significant (raw OR = 0.79). [src: pgp_pangenome_ecology] A phylum-controlled logistic model nonetheless found soil depletion (OR = 0.56, p = 0.027). [src: pgp_pangenome_ecology]

### Core versus accessory status
PGP genes are mostly core, and the report rejects its horizontal gene transfer (HGT) hypothesis (H3) on that basis. [src: pgp_pangenome_ecology] All 13 PGP genes had higher core fractions than the genome-wide baseline of 46.8% (chi-square, BH-FDR q < 0.05 for all). [src: pgp_pangenome_ecology] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

| Gene | Core | Auxiliary | Singleton | q vs baseline |
|---|---|---|---|---|
| pqqC | 81.5% | 7.8% | 10.7% | 0.0 [src: pgp_pangenome_ecology] |
| pqqB | 78.1% | 8.9% | 13.0% | 3.0e-247 [src: pgp_pangenome_ecology] |
| hcnA | 78.5% | 10.8% | 10.8% | 9.2e-37 [src: pgp_pangenome_ecology] |
| ipdC | 76.5% | 9.7% | 13.7% | 3.4e-19 [src: pgp_pangenome_ecology] |
| acdS | 70.4% | 13.4% | 16.2% | 7.9e-25 [src: pgp_pangenome_ecology] |
| nifH | 63.8% | 15.1% | 21.0% | 4.3e-71 [src: pgp_pangenome_ecology] |
| pqqD | 55.5% | 17.0% | 27.5% | 2.2e-86 [src: pgp_pangenome_ecology] |

- The mean accessory fraction across PGP genes was 29.7%, against 53.2% genome-wide. [src: pgp_pangenome_ecology]
- The report concludes that PGP genes are inherited vertically with the core genome, not acquired laterally. [src: pgp_pangenome_ecology] This runs counter to the HGT narrative that has dominated the PGPB literature. [src: pgp_pangenome_ecology]
- It describes the pqqC–acdS module as vertically inherited in the core genome and a stable, specialized rhizosphere niche adaptation rather than a recently acquired multi-trait package. [src: pgp_pangenome_ecology]
- The report relates this to Nascimento et al. (2014), whose phylogenetic analysis found predominantly vertical acdS inheritance despite some HGT events, including in some Proteobacteria. [src: pgp_pangenome_ecology] For pqqC, use as a phylogenetic marker (Meyer et al. 2011) also implies sufficient vertical inheritance for phylogenetic signal. [src: pgp_pangenome_ecology]
- pqqD is an outlier: 55.5% core versus 63–81% for other PGP genes, with the highest singleton fraction (27.5%). The report suggests it occasionally spreads horizontally as a standalone gene. [src: pgp_pangenome_ecology] The functional pqq operon (pqqB–pqqC as a unit) is predominantly core. [src: pgp_pangenome_ecology]
- Pangenome openness (singleton fraction) correlated negatively with PGP gene richness (Spearman ρ = −0.195, p = 2.0e-97, n = 11,272 species with ≥2 genomes). [src: pgp_pangenome_ecology] The report reads this as consistent with stable, specialized niches rather than generalist HGT-driven acquisition. [src: pgp_pangenome_ecology] It relates this to Sentausa & Fournier (2024, PNAS), who found plant- and host-associated lifestyles tend toward more closed pangenomes. [src: pgp_pangenome_ecology] See [[concepts/pangenome-openness-and-its-correlates]].
- pqqD is the most widespread PGP gene (11,040 species, 55.5% core). It is the most promiscuous pqq gene and often a single-gene orphan in species lacking other pqq genes. [src: pgp_pangenome_ecology]
- Excluding pqqD, pqqC is the most prevalent focal trait (3,028 species, 26.8% of species with any PGP gene). ipdC is the rarest (214 species, 1.9%). The 226 figure counts ipdC gene clusters, not species. [src: pgp_pangenome_ecology]

### Tryptophan biosynthesis and ipdC
Tryptophan pathway completeness predicts ipdC presence overall, but the tyrosine negative control and the soil stratification complicate a simple reading. [src: pgp_pangenome_ecology] See [[concepts/aromatic-amino-acid-biosynthesis-and-auxin-pathway-gene-coupling]].

- Species with complete tryptophan biosynthesis (GapMind score ≥ 0.9) carried ipdC at 2.5% versus 0.9% in incomplete species (Fisher OR = 2.81, p = 6.3e-10). [src: pgp_pangenome_ecology]
- Model 1 (tryptophan only) gave OR = 2.81, 95% CI 1.97–4.01, p = 1.4e-08, n = 11,272. [src: pgp_pangenome_ecology]
- Model 2, adding a soil covariate, gave OR_trp = 2.87, p = 7.0e-09. [src: pgp_pangenome_ecology]
- The tyrosine pathway, used as a negative control, predicted ipdC at similar effect size (OR = 3.62, p = 2.3e-11). [src: pgp_pangenome_ecology] The negative control therefore failed (OR = 3.62, comparable to trp OR = 2.81), which the report calls mechanistically interpretable. [src: pgp_pangenome_ecology]
- The report explains this mechanistically. ipdC in Enterobacter cloacae and related species is regulated by TyrR, activated by tryptophan, phenylalanine and tyrosine (Ryu & Patten 2008, PMID 18757531). [src: pgp_pangenome_ecology] It proposes that species with complete aromatic amino acid pathways more often keep the full TyrR circuit, and so ipdC. Species without it are unlikely to produce IAA even if ipdC is present. [src: pgp_pangenome_ecology]
- Within soil/rhizosphere species (n = 1,039) the association reversed (OR = 0.30, p = 0.02). [src: pgp_pangenome_ecology] In non-soil species (n = 10,233) it stayed positive (OR = 3.56, p = 7.7e-13). [src: pgp_pangenome_ecology]
- The report concludes that autonomous trp biosynthesis does not predict ipdC prevalence within soil species, and that ipdC is less prevalent in soil-dwelling species. [src: pgp_pangenome_ecology]
- The report hypothesizes that soil PGPB obtain tryptophan from root exudates. This would relax selection for autonomous biosynthesis while ipdC is kept for IAA production. [src: pgp_pangenome_ecology] It also states this is consistent with soil PGPB obtaining aromatic amino acids from plant exudates rather than synthesizing them de novo. [src: pgp_pangenome_ecology]

## Data and Methods

- 11,272 of 27,702 species in the KBase Data Lakehouse pangenome carry at least one of 13 PGP gene markers. [src: pgp_pangenome_ecology]
- The report extracted 32,736 PGP gene clusters. [src: pgp_pangenome_ecology]
- Genes were detected from bakta `gene` annotations matching exact names (nifH, acdS, pqqC, etc.). [src: pgp_pangenome_ecology]
- 27,690 species have GapMind tryptophan completeness scores. [src: pgp_pangenome_ecology]
- 291,279 genomes have ncbi_isolation_source metadata, of which 93.5% were classifiable. [src: pgp_pangenome_ecology]
- The soil/rhizosphere class is conservative: only 1,637 species (5.9% of species with an environment label) are soil/rhizosphere dominant, reflecting NCBI's clinical and host-associated sampling bias. [src: pgp_pangenome_ecology]
- Tables used in the kbase_ke_pangenome database: bakta_annotations and gene_cluster for PGP clusters with core/auxiliary/singleton flags [src: pgp_pangenome_ecology]; pangenome for species genome counts and core/accessory baselines [src: pgp_pangenome_ecology]; gtdb_metadata for isolation source [src: pgp_pangenome_ecology]; genome for genome-to-species mapping [src: pgp_pangenome_ecology]; gtdb_taxonomy_r214v1 for phylogenetic controls [src: pgp_pangenome_ecology]; gapmind_pathways for tryptophan and tyrosine completeness. [src: pgp_pangenome_ecology]

## Caveats and Open Work

- The report considers the acdS and pqqC enrichment ORs (7.0 and 2.9) likely underestimates, because many soil isolates carry broader "environmental" labels. [src: pgp_pangenome_ecology]
- ncbi_isolation_source is noisy and NCBI is heavily biased toward clinical and host-associated isolates. [src: pgp_pangenome_ecology]
- Name-only gene detection misses genes annotated only by product description or with variant names, particularly less-characterized PGP genes. [src: pgp_pangenome_ecology]
- There was no functional validation: an annotated pqqC cluster is not necessarily functional, and truncations, frameshifts and pseudogenization are not filtered. [src: pgp_pangenome_ecology]
- A phylum-plus-soil logistic model (Model 3) for ipdC failed through quasi-complete separation, caused by ipdC's rarity (214 species, 1.9%). Conclusions therefore rest on Models 1 and 2. [src: pgp_pangenome_ecology] Only 214/11,272 species carry ipdC, which limits power for the stratified H4 analysis. [src: pgp_pangenome_ecology]
- The soil reversal (OR = 0.30, p = 0.02) should be treated as hypothesis-generating rather than conclusive. [src: pgp_pangenome_ecology]
- GapMind trp and tyr completeness scores both proxy overall pathway completeness. Controlling for genome size or total pathway count would be needed to isolate specific coupling. [src: pgp_pangenome_ecology] A better H4 test would control for genome completeness (size, COG coverage, clusters of orthologous groups) to separate aromatic-pathway effects from general metabolic capacity. [src: pgp_pangenome_ecology]
- The RESEARCH_PLAN estimated ~1,913 nifH clusters, but the actual count was 2,756 (43% higher). The report attributes this to growth of the GTDB r214 pangenome and says it affects no analysis. [src: pgp_pangenome_ecology]
- Proposed next step: determine whether pqqC and acdS are physically co-located (same island or operon) or occur at separate loci, to separate operon linkage from independent co-selection. [src: pgp_pangenome_ecology]
- Proposed next step: compare marine/aquatic diazotrophs, including cyanobacteria and Azotobacter, with legume-symbiotic rhizobia and free-living soil diazotrophs in genome structure and PGP trait co-occurrence. [src: pgp_pangenome_ecology]
- Proposed next step (controlled H4 test): regress ipdC presence on trp completeness while controlling for genome-wide pathway completeness (number of complete pathways or genome size), to isolate the aromatic-amino-acid-specific signal from global metabolic capacity. [src: pgp_pangenome_ecology]
- Proposed next step: a focused study of hcnA-C phylogeny and co-occurrence with biocontrol phenotypes. [src: pgp_pangenome_ecology]
- Proposed next step: cross-reference species carrying pqqC + acdS + hcnC with commercial inoculant strains, to assess whether the genomic signature predicts inoculant efficacy. [src: pgp_pangenome_ecology]

## Slots Into

- [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds]]: pqqC–acdS positive association and nifH negative associations suggest separate guilds; hcnC co-occurs with pqqC. [src: pgp_pangenome_ecology]
- [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]]: acdS, pqqC and hcnC are enriched in soil/rhizosphere, and nifH is depleted. [src: pgp_pangenome_ecology]
- [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]]: all 13 PGP genes are more core than baseline. [src: pgp_pangenome_ecology]
- [[concepts/pangenome-openness-and-its-correlates]]: openness correlates negatively with PGP richness. [src: pgp_pangenome_ecology]
- [[concepts/aromatic-amino-acid-biosynthesis-and-auxin-pathway-gene-coupling]]: tryptophan and tyrosine completeness both predict ipdC. [src: pgp_pangenome_ecology]
