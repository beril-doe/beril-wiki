---
type: "Concept"
description: "Which clades and orders carry the PHB pathway, how prevalent it is across GTDB species, and which families are enriched or depleted; stops at distribution, not mechanism."
sources: ["summaries/phb_granule_ecology__REPORT.md"]
---
# Phylogenetic distribution of PHB synthesis across bacteria and archaea

This page covers where the polyhydroxybutyrate (PHB) pathway occurs across bacteria and archaea in the [[entities/gtdb]] species tree. In one genome-based census of 27,690 species, 21.9% carry phaC, the PHA (polyhydroxyalkanoate) synthase step. Carriage is concentrated in a few lineages, mainly [[entities/pseudomonadota]]. The evidence comes from a single report, so every figure is that report's estimate ([[summaries/phb_granule_ecology__REPORT]]). [src: phb_granule_ecology]

## Overall prevalence

Across 27,690 GTDB species, 21.9% carry phaC, the committed step for PHB biosynthesis, and 21.7% have a complete pathway (phaC + phaA/phaB). [src: phb_granule_ecology] The report reads the near-identical values as showing that virtually all phaC-carrying species also have the upstream biosynthetic enzymes. [src: phb_granule_ecology] It calls this the first precise estimate across the full tree and the first comprehensive pangenome-scale survey of PHB distribution. [src: phb_granule_ecology] It says earlier work was qualitative, limited to single clades, focused on degradation, or confined to single-species horizontal gene transfer (HGT) case studies. [src: phb_granule_ecology]

## Phylum-level distribution

The 6,067 phaC-carrying species span 95 of 142 GTDB phyla, but they cluster in a few lineages. [src: phb_granule_ecology] Five phyla hold 85.5% of phaC-positive species while making up 30.4% of total species diversity: Pseudomonadota, Myxococcota, Halobacteriota, Thermoproteota and Desulfobacterota. [src: phb_granule_ecology]

| Phylum | Prevalence | Species |
|---|---|---|
| Pseudomonadota | 60.9% | 4,544/7,456 [src: phb_granule_ecology] |
| Myxococcota | 52.9% | 83/157 [src: phb_granule_ecology] |
| Halobacteriota | 34.4% | 89/259 [src: phb_granule_ecology] |
| Thermoproteota | 27.9% | 65/233 [src: phb_granule_ecology] |
| Desulfobacterota | 21.9% | 70/319 [src: phb_granule_ecology] |
| [[entities/actinomycetota]] | 18.5% | 587/3,172 [src: phb_granule_ecology] |

Pseudomonadota alone accounts for 74.9% of phaC-carrying species (4,544/6,067). This reflects high prevalence across Alpha- and Gammaproteobacteria orders. [src: phb_granule_ecology] The report presents the Halobacteriota figure as quantifying the scale of archaeal PHA capacity. [src: phb_granule_ecology]

Several phyla have no PHB at all: Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135) and Marinisomatota (0/90). [src: phb_granule_ecology] [[entities/patescibacteria]] is near zero at 0.4% (4/981). The report calls this consistent with reduced genomes and limited metabolic capacity. [src: phb_granule_ecology]

The report also cites Pieja et al. (2011) for lineage-specific capacity within methanotrophs: all Type II positive, all Type I negative. [src: phb_granule_ecology]

## Order-level distribution

Prevalence varies widely between orders. 23 orders with more than 20 species exceed 50% phaC prevalence, and 117 orders fall below 10%. [src: phb_granule_ecology]

The top orders are Azospirillales and Rhodospirillales (both 100%), Caulobacterales (99.3%) and Sphingomonadales (95.9%). [src: phb_granule_ecology] Within Pseudomonadota, order prevalence runs from 100% in Azospirillales and Rhodospirillales down to several orders below 10%. [src: phb_granule_ecology]

## Family-level enrichment and depletion

Within-phylum Fisher's exact tests covered 248 families with at least 10 species. They used Bonferroni correction at alpha = 0.05. [src: phb_granule_ecology] The result was 41 enriched, 62 depleted and 145 not significant families. [src: phb_granule_ecology]

Enriched families are concentrated in Pseudomonadota. They include Burkholderiaceae, Burkholderiaceae_B, Rhodocyclaceae, Caulobacteraceae, Sphingomonadaceae, Xanthobacteraceae, Rhodanobacteraceae and Legionellaceae. [src: phb_granule_ecology] Other phyla also contain enriched families:

- Actinomycetota: Mycobacteriaceae and Nocardioidaceae. [src: phb_granule_ecology]
- Halobacteriota: Haloarculaceae and Natrialbaceae. [src: phb_granule_ecology]
- Thermoproteota: Nitrosopumilaceae. [src: phb_granule_ecology]
- Cyanobacteriota: Microcystaceae. [src: phb_granule_ecology]
- Bacillota: Bacillaceae_G. [src: phb_granule_ecology]

Enriched families skew toward freshwater (5/41) and wastewater (3/41) environments. Depleted families skew toward marine (18/62) and host-associated (12/62) environments. [src: phb_granule_ecology] This reading is limited by the dominant "other_unknown" category (30/41 enriched, 26/62 depleted), which reflects sparse environmental metadata. [src: phb_granule_ecology] See also [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Open Directions

- Repeat the family tests with a phylogenetically aware model, to check that enrichment is not just shared ancestry within Pseudomonadota.
- Compare the 0% phyla (Campylobacterota, Gemmatimonadota, Nanoarchaeota, Marinisomatota) against genome completeness, to separate true absence from missing annotation.
- Improve environmental metadata for the "other_unknown" species, then re-test the freshwater/wastewater versus marine/host skew. See [[concepts/environmental-variability-and-storage-polymer-pathway-enrichment-feast-famine-hypothesis]].
- Test the Pieja et al. methanotroph split (Type I versus Type II) across GTDB methanotroph genomes.
