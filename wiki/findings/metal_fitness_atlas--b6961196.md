---
type: "Finding"
description: "Bioleaching genera as a group are not significantly enriched over background after normalization (Mann-Whitney p=0.17), indicating that metal tolerance genes are broadly distributed across bacteria rather than concentrated in specialists."
finding_id: "metal_fitness_atlas--b6961196"
result: "null result"
source: "metal_fitness_atlas"
quantities: [{"value": "p=0.17", "what": "Mann-Whitney p-value for bioleaching genera vs background", "unit": "", "denominator": "", "scope": ""}]
caveat: "Without normalization, species with large open pangenomes (K. pneumoniae, P. aeruginosa) dominate, reflecting genome size rather than metal biology."
first_added: "2026-11-24"
source_hash: "9ea58c19144575c5e8a783b777863269a18b37241d89bb6c0a9c2a044de1353d"
---
# Bioleaching genera are not enriched for metal-tolerance signature

Bioleaching genera as a group are not significantly enriched over background after normalization (Mann-Whitney p=0.17), indicating that metal tolerance genes are broadly distributed across bacteria rather than concentrated in specialists. [src: metal_fitness_atlas]

## Key figures

- **p=0.17**: Mann-Whitney p-value for bioleaching genera vs background [src: metal_fitness_atlas]

## Evidence

> However, bioleaching genera as a group are not significantly enriched over background after normalization (Mann-Whitney p=0.17), indicating that metal tolerance genes are broadly distributed across bacteria rather than concentrated in specialists — consistent with the core genome robustness model. [src: metal_fitness_atlas]

From the report [[summaries/metal_fitness_atlas__REPORT]].

## Caveat

Without normalization, species with large open pangenomes (K. pneumoniae, P. aeruginosa) dominate, reflecting genome size rather than metal biology. [src: metal_fitness_atlas]

> Without normalization, species with large open pangenomes (*K. pneumoniae*, *P. aeruginosa*) dominate, reflecting genome size rather than metal biology. [src: metal_fitness_atlas]

## Other caveats in this report

- The atlas conservation analysis covers 22 of 31 metal-tested organisms (71%). [src: metal_fitness_atlas]
- The 9 organisms excluded from atlas conservation analysis—Putida, Keio, SynE, Miya, Kang, BFirm, Cola, Ponti, and Dino—lack Fitness Browser–pangenome links. [src: metal_fitness_atlas]
- The report considers systematic bias from excluded organisms unlikely because they are taxonomically diverse. [src: metal_fitness_atlas]
- The atlas's functional predictions for unknown genes are based solely on cross-species fitness data. [src: metal_fitness_atlas]
- An initial Pan-Bacterial Metal Fitness Atlas ICA analysis using raw module_conditions.csv activity scores produced 0 responsive modules because raw scores (max 0.96) differed in scale from z-scores; per-experiment profiles with z-normalization resolved this. [src: metal_fitness_atlas]
