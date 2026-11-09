---
type: "Research direction"
description: "Clinical-dominated species carry several-fold more resistance-gene clusters, yet the link between clinical fraction and overall accessory share is borderline. Is the clinical excess confined to the resistance catalog, and within it to classical antibiotic resistance rather than metal and stress systems, or do clinical species also carry excess of unrelated accessory gene classes?"
hypothesis: "Classical antibiotic-resistance clusters rise with clinical fraction much more steeply than size-matched clusters of unrelated accessory functions and than metal and stress-response clusters from the same catalog."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The species-level resistance table and environment labels exist; separating antibiotic from metal and stress clusters and building size-matched control counts across 823 species needs new queries on the pangenome collection."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["amr_environmental_resistome--96de8ae3", "amr_environmental_resistome--4d34e715", "amr_environmental_resistome--e39caf4e"]
conflicts: ["conflict--environmental-resistome--86566e6b", "conflict--environmental-resistome--ecbc42fd"]
papers: ["38993487", "38923192", "25003965", "41594066"]
builds_on: ["findings/amr_environmental_resistome--96de8ae3", "findings/amr_environmental_resistome--4d34e715", "findings/amr_environmental_resistome--e39caf4e", "conflicts/conflict--environmental-resistome--86566e6b", "conflicts/conflict--environmental-resistome--ecbc42fd"]
projects: ["amr_environmental_resistome", "amr_pangenome_atlas", "amr_strain_variation", "ecotype_analysis"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Is the resistance-gene excess in clinical species specific, or part of broad accessory-genome inflation?

Clinical-dominated species carry several-fold more resistance-gene clusters, yet the link between clinical fraction and overall accessory share is borderline. Is the clinical excess confined to the resistance catalog, and within it to classical antibiotic resistance rather than metal and stress systems, or do clinical species also carry excess of unrelated accessory gene classes?

## Hypothesis

Classical antibiotic-resistance clusters rise with clinical fraction much more steeply than size-matched clusters of unrelated accessory functions and than metal and stress-response clusters from the same catalog.

## Why it matters

Clinical species are also the most sequenced, so the excess could be a side effect of open, well-sampled genomes. The resistance catalog also contains metal and stress systems, so a catalog-wide excess alone would not show antibiotic selection. A steeper rise for classical antibiotic-resistance genes would be the first piece of evidence that clinical gene content is shaped by drug exposure.

## How to test it

Use the 823 species with at least 5 genomes in at least 2 environments. Split resistance clusters into classical antibiotic-resistance genes and metal or stress systems, mapping mechanisms to an antibiotic-resistance ontology rather than keyword labels. For each species, count clusters of several non-resistance accessory classes, such as metabolic and transport clusters, matched in size. Regress each count on clinical-genome fraction while holding total genome count constant. Compare the slope for antibiotic resistance with slopes for metal and stress systems and for the control classes, and repeat within phylum.

## What would support or refute it

Support: the antibiotic-resistance slope is clearly steeper than every control class and than metal and stress systems. Refutation: control classes or metal and stress systems rise with clinical fraction about as steeply, so the excess is general accessory inflation or catalog breadth.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The species-level resistance table and environment labels exist; separating antibiotic from metal and stress clusters and building size-matched control counts across 823 species needs new queries on the pangenome collection.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/amr_environmental_resistome--96de8ae3|Clinical-dominated species carry several-fold more AMR clusters than environmental-dominated ones]] (Extends retrieved work)
- Finding: [[findings/amr_environmental_resistome--4d34e715|Clinical species carry more AMR gene clusters than soil or aquatic species]] (Extends retrieved work)
- Finding: [[findings/amr_environmental_resistome--e39caf4e|Clinical species' resistomes are mostly accessory, soil's less so]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--environmental-resistome--86566e6b|Species-level environment–AMR association versus sparse within-species environmental structure]]
- Conflict: [[conflicts/conflict--environmental-resistome--ecbc42fd|AMRFinderPlus catalog scope: broad stress-resistance landscape versus narrow antibiotic-resistance reading, with unclassified fractions that do not match]]

## Closest published work

- [PMID 38993487](https://pubmed.ncbi.nlm.nih.gov/38993487/) Comparative genome analyses of clinical and non-clinical Clostridioides difficile strains.
- [PMID 38923192](https://pubmed.ncbi.nlm.nih.gov/38923192/) Comparative resistomics analysis of multidrug-resistant Chryseobacteria.
- [PMID 25003965](https://pubmed.ncbi.nlm.nih.gov/25003965/) Improved annotation of antibiotic resistance determinants reveals microbial resistomes cluster by ecology.
- [PMID 41594066](https://pubmed.ncbi.nlm.nih.gov/41594066/) Clinical and Environmental Plasmids: Antibiotic Resistance, Virulence, Mobility, and ESKAPEE Pathogens.

PMIDs 38993487 and 38923192 show more resistance genes in clinical strains of single genera, and PMID 25003965 shows resistomes cluster by ecology; none compares the resistance excess against non-resistance accessory classes or against metal and stress systems across species.
