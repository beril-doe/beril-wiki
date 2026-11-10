---
type: "Research direction"
description: "After correcting the iron-reduction markers, deep and shallow clay genomes no longer differ, yet rock-associated clay communities are reported to be dominated by iron reducers. Do clay Bacillota_B use an electron-transfer route the cytochrome markers miss?"
hypothesis: "Deep-clay Bacillota_B carry flavin-based extracellular electron transfer genes more often than soil Bacillota_B. These genes would account for iron reduction where the cytochrome markers show no deep-versus-shallow difference."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Genomes are available, but profile searches for a new gene set must be built and run, and the isolate test needs wet-lab work."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["bacillota_b_subsurface_accessory--bbe885ea", "clay_confined_subsurface--208cd800", "bacillota_b_subsurface_accessory--f9a4cc6b"]
conflicts: []
papers: ["37642485", "35100867", "30266730", "34669448", "27739431"]
builds_on: ["findings/bacillota_b_subsurface_accessory--bbe885ea", "findings/clay_confined_subsurface--208cd800", "findings/bacillota_b_subsurface_accessory--f9a4cc6b"]
projects: ["bacillota_b_subsurface_accessory", "clay_confined_subsurface"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Do deep-clay Bacillota_B reduce iron through flavin-based electron transfer rather than multi-heme cytochromes?

After correcting the iron-reduction markers, deep and shallow clay genomes no longer differ, yet rock-associated clay communities are reported to be dominated by iron reducers. Do clay Bacillota_B use an electron-transfer route the cytochrome markers miss?

## Hypothesis

Deep-clay Bacillota_B carry flavin-based extracellular electron transfer genes more often than soil Bacillota_B. These genes would account for iron reduction where the cytochrome markers show no deep-versus-shallow difference.

## Why it matters

It would show that the cytochrome-based marker survey was blind to the real iron-reduction route in a major clay lineage. Iron reduction would then need to be reassessed for repository-relevant clays.

## How to test it

Search the anchor and baseline Bacillota_B genomes in the Pangenome Collection and KBase Genomes for flavin-binding extracellular electron transfer gene sets, using sequence profiles rather than the multi-heme markers. Compare deep, shallow and soil groups. Then test a cultured Desulfosporosinus or related clay isolate for Fe(III) reduction with and without a flavin-pathway inhibitor or knockout.

## What would support or refute it

Support: flavin-pathway genes are more common in deep-clay genomes and the isolate reduces Fe(III) in a way that tracks them. Refutation: the genes are equally common in soil genomes, or the isolate does not reduce Fe(III).

## Data

Approach: analysis then experiment. Readiness: needs compute. Genomes are available, but profile searches for a new gene set must be built and run, and the isolate test needs wet-lab work.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/bacillota_b_subsurface_accessory--bbe885ea|Corrected iron-reduction comparison shows no significant deep versus shallow difference]] (Insufficient literature evidence)
- Finding: [[findings/clay_confined_subsurface--208cd800|Corrected iron-reduction markers show no significant cohort difference]] (Insufficient literature evidence)
- Finding: [[findings/bacillota_b_subsurface_accessory--f9a4cc6b|Sulfate-reduction signal in deep clay survives while iron-reduction side fails]] (Insufficient literature evidence)

## Closest published work

- [PMID 37642485](https://pubmed.ncbi.nlm.nih.gov/37642485/) Clay-associated microbial communities and their relevance for a nuclear waste repository in the Opalinus Clay rock formation.
- [PMID 35100867](https://pubmed.ncbi.nlm.nih.gov/35100867/) Evidence for Horizontal and Vertical Transmission of Mtr-Mediated Extracellular Electron Transfer among the Bacteria.
- [PMID 30266730](https://pubmed.ncbi.nlm.nih.gov/30266730/) Divergent Nrf Family Proteins and MtrCAB Homologs Facilitate Extracellular Electron Transfer in Aeromonas hydrophila.
- [PMID 34669448](https://pubmed.ncbi.nlm.nih.gov/34669448/) Cytochrome OmcS Is Not Essential for Extracellular Electron Transport via Conductive Pili in Geobacter sulfurreducens Strain KN400.
- [PMID 27739431](https://pubmed.ncbi.nlm.nih.gov/27739431/) Reconstructing a hydrogen-driven microbial metabolic network in Opalinus Clay rock.

PMID 37642485 reports iron reducers in rock-associated clay communities, and PMIDs 35100867, 30266730 and 34669448 study multi-heme transfer; none asks which route clay Bacillota_B use.
