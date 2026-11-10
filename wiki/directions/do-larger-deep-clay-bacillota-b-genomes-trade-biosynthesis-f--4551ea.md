---
type: "Research direction"
description: "Deep-clay Bacillota_B genomes are larger than soil relatives, yet the quality-filtered deep-clay genomes were less complete for amino-acid synthesis pathways than soil baseline genomes. Where does the extra DNA go, and does it replace synthesis with uptake?"
hypothesis: "The extra gene content in deep-clay Bacillota_B is mostly transport, regulatory and mobile-element genes. Genomes with the most amino-acid pathway gaps carry the most matching uptake transporters, which points to dependence on neighbours rather than self-sufficiency."
approach: "analysis then experiment"
readiness: "data in the lakehouse"
readiness_basis: "Anchor and baseline genomes, orthogroup presence and pathway completeness are already in the pangenome collection; only the growth test needs new work, and the small anchor sets limit the analysis."
collections: ["kbase-ke-pangenome"]
findings: ["bacillota_b_subsurface_accessory--0b68d03d", "bacillota_b_subsurface_accessory--b2fd7eb1", "clay_confined_subsurface--10b5365e"]
conflicts: []
papers: ["38902796", "32252814", "40054447", "30728279", "35387071"]
builds_on: ["findings/bacillota_b_subsurface_accessory--0b68d03d", "findings/bacillota_b_subsurface_accessory--b2fd7eb1", "findings/clay_confined_subsurface--10b5365e"]
projects: ["bacillota_b_subsurface_accessory", "clay_confined_subsurface"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Do larger deep-clay Bacillota_B genomes trade biosynthesis for transporters and partner dependence?

Deep-clay Bacillota_B genomes are larger than soil relatives, yet the quality-filtered deep-clay genomes were less complete for amino-acid synthesis pathways than soil baseline genomes. Where does the extra DNA go, and does it replace synthesis with uptake?

## Hypothesis

The extra gene content in deep-clay Bacillota_B is mostly transport, regulatory and mobile-element genes. Genomes with the most amino-acid pathway gaps carry the most matching uptake transporters, which points to dependence on neighbours rather than self-sufficiency.

## Why it matters

It would show that deep-subsurface genome growth can go with metabolic dependence, not only streamlining. That challenges the usual picture of compact, self-sufficient subsurface cells.

## How to test it

Within Bacillota_B in the Pangenome Collection, sort the many orthogroups enriched in the deep-clay anchor genomes into functional classes. Compare deep-clay and soil genomes on amino-acid pathway gaps and on matching amino-acid transporter counts. Run it per genus (BRH-c8a, BRH-c4a, Desulfosporosinus), because the 10-genome anchor set is dominated by a few genera. The pathway comparison rests on only 6 quality-filtered deep genomes against 137 baseline genomes, and the 18-pathway measure has a ceiling (most cultured organisms score 17-18 of 18), so also score pathway gaps at finer resolution than the 18-pathway count. Then grow a cultured Desulfosporosinus isolate in defined medium with and without single amino acids.

## What would support or refute it

Support: transporter and regulatory classes dominate the enriched gene content, pathway gaps track transporter counts, and the isolate needs the supplied amino acids. Refutation: the extra content is mostly biosynthetic or mobile, the pathway gaps do not track transporters, or the pattern comes from one genus alone.

## Data

Approach: analysis then experiment. Readiness: data in the lakehouse. Anchor and baseline genomes, orthogroup presence and pathway completeness are already in the pangenome collection; only the growth test needs new work, and the small anchor sets limit the analysis.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/bacillota_b_subsurface_accessory--0b68d03d|Deep-clay Bacillota_B genomes are larger than soil baselines, not compact]] (Extends retrieved work)
- Finding: [[findings/bacillota_b_subsurface_accessory--b2fd7eb1|Many orthogroups are enriched in deep-clay anchors versus soil baselines]] (Insufficient literature evidence)
- Finding: [[findings/clay_confined_subsurface--10b5365e|Quality-filtered deep-clay genomes show lower amino-acid pathway completeness than soil baseline]] (Insufficient literature evidence)

## Closest published work

- [PMID 38902796](https://pubmed.ncbi.nlm.nih.gov/38902796/) Genome streamlining in Parcubacteria transitioning from soil to groundwater.
- [PMID 32252814](https://pubmed.ncbi.nlm.nih.gov/32252814/) Small and mighty: adaptation of superphylum Patescibacteria to groundwater environment drives their genome simplicity.
- [PMID 40054447](https://pubmed.ncbi.nlm.nih.gov/40054447/) Microbial ecosystems and ecological driving forces in the deepest ocean sediments.
- [PMID 30728279](https://pubmed.ncbi.nlm.nih.gov/30728279/) Gene Expansion and Positive Selection as Bacterial Adaptations to Oligotrophic Conditions.
- [PMID 35387071](https://pubmed.ncbi.nlm.nih.gov/35387071/) A Large-Scale Genome-Based Survey of Acidophilic Bacteria Suggests That Genome Streamlining Is an Adaption for Life at Low pH.

PMIDs 38902796, 32252814 and 40054447 tie groundwater and deep habitats to smaller genomes; this asks what a larger deep-clay genome contains and whether it signals metabolic dependence.
