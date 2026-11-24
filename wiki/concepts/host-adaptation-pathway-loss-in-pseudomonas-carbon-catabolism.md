---
type: "Concept"
description: "Covers the loss of plant-derived sugar catabolism in host-associated Pseudomonas lineages relative to free-living/plant-associated ones, and the retention of amino acid and organic acid pathways; stops short of within-infection evolution beyond the cited comparisons."
sources: ["summaries/discoveries.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Host-adaptation pathway loss in Pseudomonas carbon catabolism

Host-associated *Pseudomonas* lineages have lost most plant-derived sugar catabolism, while amino acid and organic acid pathways stay nearly universal. The evidence is a genome-scale comparison of GapMind carbon pathway predictions across 433 *Pseudomonas* species (12,732 genomes). It is a computational prediction comparison across species, not a measurement of growth. [src: discoveries] See also [[entities/gapmind]], [[entities/pseudomonas]] and [[entities/pseudomonas-aeruginosa]].

## Literature Context

The candidate papers are only partly relevant to the hub's claim, which is a genus-wide comparison of predicted sugar pathway loss. Two of them address how *Pseudomonas aeruginosa* carbon metabolism changes in host settings. The other two concern *P. putida*, and neither bears on host adaptation.

A study of long-term cystic fibrosis (CF) airway colonization followed three *P. aeruginosa* lineages coevolving in the same environment. The authors report that central metabolic pathways were restructured at the cost of versatility. They describe a converged slow-growth phenotype, auxotrophy, tailored carbon source assimilation from CF sputum, reduced arginine and pyruvate fermentation, and increased oxygen requirements [PMID 29636437](https://pubmed.ncbi.nlm.nih.gov/29636437/). Comparative genomics showed diverse mutational patterns under this phenotypic convergence. The paper is an abstract-level source, so I cannot give its sample details. It supports the idea that host-associated metabolism narrows, but it describes within-host evolution, not ancestral lineage loss.

A transcriptome study grew strain UCBPP-PA14 in whole blood from eight trauma patients and seven healthy volunteers. Expression of 285 genes differed. Carbon metabolism genes rose, especially malonate utilization and mannitol uptake, and genes for amino acid uptake and metabolism fell [PMID 31086830](https://pubmed.ncbi.nlm.nih.gov/31086830/). This is a small in vitro expression study of one strain. It is relevant in two ways. Reduced amino acid gene expression in blood does not conflict with the hub's near-universal amino acid pathway retention, because retention of a pathway is a genomic property and expression is a different measure. Mannitol uptake induction in blood is also notable beside the hub's finding that the mannitol pathway is present in 25.9% of the *P. aeruginosa* group versus 77.5% of the *P. fluorescens* group. The hub's pathway predictions are not contradicted by this, because a minority of the group retains the pathway and the paper tests one strain.

The corpus's findings are therefore consistent with the literature in direction but extend it in scale and level. The hub reports GapMind predictions across 433 species (12,732 genomes), with 43 of 62 pathways significantly different between 7 *Pseudomonas* s.s. species and 189 *Pseudomonas_E* species. It suggests that much of the metabolic loss attributed to infection reflects ancestral streamlining. The CF work documents loss of versatility arising during colonization [PMID 29636437](https://pubmed.ncbi.nlm.nih.gov/29636437/). The two views could both hold, with ancestral sugar loss and further within-host specialization acting at different timescales. This combination is untested, and the hub's open direction of comparing early and late infection isolates with environmental isolates would address it. The *P. putida* papers [PMID 23409067](https://pubmed.ncbi.nlm.nih.gov/23409067/) and [PMID 39261865](https://pubmed.ncbi.nlm.nih.gov/39261865/) concern solvent tolerance and electrogenic glucose conversion. They offer no evidence on host adaptation or pathway loss, so I do not use them to support or challenge the hub.

## Sugar pathway loss in the P. aeruginosa group

The *P. aeruginosa* group shows near-complete loss of plant-derived sugar catabolism compared with the *P. fluorescens/putida* group. [src: discoveries] In subgenus terms, *Pseudomonas* sensu stricto shows this loss relative to *Pseudomonas_E*. [src: pseudomonas_carbon_ecology] Comparing 7 *Pseudomonas* s.s. species with 189 *Pseudomonas_E* species (each with >=5 genomes), [[entities/mann-whitney-u-test|Mann-Whitney U tests]] with Benjamini-Hochberg false discovery rate (FDR) correction found 43 of 62 pathways significantly different (q < 0.05). [src: pseudomonas_carbon_ecology, discoveries] Nineteen pathways showed no significant difference. [src: pseudomonas_carbon_ecology]

All 7 pathways that differ by more than 50 percentage points (pp) involve plant-derived sugars or sugar alcohols. These are absent from *P. aeruginosa* but prevalent in the *P. fluorescens* group. [src: pseudomonas_carbon_ecology] The report counts differences of >50 pp for 7 pathways and >10 pp for 15 pathways. It calls this the most comprehensive evidence to date for metabolic streamlining in host-adapted *Pseudomonas*. [src: pseudomonas_carbon_ecology]

Pathway completeness in the *P. aeruginosa* group versus the *P. fluorescens* group:

| Pathway | P. aeruginosa group | P. fluorescens group | Difference |
|---|---|---|---|
| Xylose | 0.0% | 74.4% | +74.4 pp [src: pseudomonas_carbon_ecology] |
| Ribose | 27.9% | 92.0% | +64.2 pp [src: pseudomonas_carbon_ecology] |
| Arabinose | 0.0% | 62.6% | +62.6 pp [src: pseudomonas_carbon_ecology] |
| Galacturonate | 28.6% | 88.4% | +59.8 pp [src: pseudomonas_carbon_ecology] |
| Myo-inositol | 0.0% | 58.8% | +58.8 pp [src: pseudomonas_carbon_ecology] |
| Mannitol | 25.9% | 77.5% | +51.6 pp [src: pseudomonas_carbon_ecology] |
| Sorbitol | 25.9% | 77.4% | +51.5 pp [src: pseudomonas_carbon_ecology] |

A second summary of the same comparison gives the largest effects as xylose (+74 pp), ribose (+64 pp), arabinose (+63 pp), galacturonate (+60 pp) and myo-inositol (+59 pp). [src: discoveries]

The *P. aeruginosa* group has near-complete loss of xylose, arabinose and myo-inositol catabolism (0% versus 59-74% in the *P. fluorescens* group). It also has dramatic reductions in ribose, galacturonate, mannitol and sorbitol pathways. [src: pseudomonas_carbon_ecology] In a principal component analysis (PCA) of species pathway profiles, the primary axis separates *Pseudomonas* s.s. from *Pseudomonas_E*, driven by this sugar loss. [src: pseudomonas_carbon_ecology] The *P. fluorescens/putida* group also has greater carbon pathway breadth (mean richness 56.1) than *P. aeruginosa* (mean richness ~50), particularly for sugar and sugar alcohol catabolism. [src: pseudomonas_carbon_ecology]

## Retained pathways

Amino acid catabolism, including arginine, histidine, serine and glutamate, stays near-universal (>99%) in both subgenera. [src: pseudomonas_carbon_ecology] Core organic acid pathways for citrate, succinate and pyruvate also stay near-universal (>99%). [src: pseudomonas_carbon_ecology] A separate summary puts amino acid catabolism above 99.5% in both groups. [src: discoveries] In *P. aeruginosa*, the four amino acid pathways stay >99.5% complete despite the sugar losses. [src: pseudomonas_carbon_ecology]

The report lists a shared core of conserved central carbon metabolism: acetate, pyruvate, fructose, L-lactate, D-lactate, glycerol, alanine, sucrose, 2-oxoglutarate, propionate, phenylacetate, deoxyribonate and glucose-6-phosphate. [src: pseudomonas_carbon_ecology]

## Interpretation

These readings go beyond the measurements, which are pathway predictions.

- The report reads the pattern as *P. aeruginosa* keeping amino acid catabolism for host growth, for example on cystic fibrosis (CF) sputum amino acids. It reads the sugar losses as loss of degradation for plant carbon sources the bacterium no longer meets. [src: pseudomonas_carbon_ecology] This is consistent with CF sputum being amino acid-dominated. [src: discoveries] See [[entities/cystic-fibrosis-sputum]].
- The report says the lost sources are those expected to be irrelevant where amino acids and organic acids dominate. [src: pseudomonas_carbon_ecology]
- The lost pathways (xylose, arabinose, myo-inositol, galacturonate) are involved in plant cell wall and rhizosphere carbon cycling. The report calls this consistent with release from selection for plant-associated metabolism during the move to animal hosts. [src: pseudomonas_carbon_ecology]
- The report rates the pathway-loss hypothesis for host-associated clades as strongly supported. [src: pseudomonas_carbon_ecology]

## Lineage-level, not within-infection

The comparison is genome-scale across the genus, not adaptation within one species during infection. [src: pseudomonas_carbon_ecology] The losses are conserved at the species level rather than strain-specific. [src: pseudomonas_carbon_ecology] The report suggests that much of the metabolic loss attributed to infection reflects ancestral streamlining of the *P. aeruginosa* lineage, because the pathways were already absent across thousands of isolates. [src: pseudomonas_carbon_ecology] For lung-adaptation context see [[concepts/pathogen-metabolic-adaptation-in-the-lung-and-stability-of-competition-targets]]. For the lineage-versus-ecology question see [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]].

## Tensions

- Rhamnose pathway completeness was higher in *P. aeruginosa* (66.8%) than in the *P. fluorescens* group (41.3%). [src: pseudomonas_carbon_ecology] Fucose was also higher (66.8% versus 45.1%). [src: pseudomonas_carbon_ecology] Neither difference was significant after FDR correction, so they do not fit the pattern of loss but are not established reversals. The report suggests they may reflect rhamnolipid use as virulence factors. This is a suggestion only. [src: pseudomonas_carbon_ecology]

## Open Directions

- Test whether the sugar losses are tied to one clade or arose repeatedly. Map the pathway calls onto a species phylogeny and use phylogenetic comparative methods. The 7 *Pseudomonas* s.s. species are too few to separate lineage from ecology.
- Check the predictions by growth assays of *P. aeruginosa* and *P. fluorescens* group isolates on xylose, arabinose, myo-inositol and galacturonate.
- Compare isolates from early and late infection with environmental isolates. This would show whether any further loss accrues during infection beyond the ancestral loss.
- Repeat the rhamnose and fucose comparison with more *P. aeruginosa* species or genomes to see whether the non-significant difference becomes resolvable.
