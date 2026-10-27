---
type: "Finding"
description: "After genome-size normalization, bioleaching genera as a group are not significantly enriched over background in the 1,286-term KEGG KO metal signature scored across 27,702 pangenome species (Mann-Whitney p=0.17), although Leptospirillum ranks at the 91st percentile individually."
finding_id: "metal_fitness_atlas--33814a75"
result: "null result"
source: "metal_fitness_atlas"
quantities: [{"value": "0.17", "what": "Mann-Whitney p-value for bioleaching genera versus background", "unit": "", "denominator": "", "scope": "after genome-size normalization"}, {"value": "27,702", "what": "pangenome species scored", "unit": "species", "denominator": "", "scope": ""}, {"value": "91st", "what": "Leptospirillum percentile after genome-size normalization", "unit": "percentile", "denominator": "", "scope": "normalized score"}]
caveat: "Without genome-size normalization, species with large open pangenomes (K. pneumoniae, P. aeruginosa) dominate the scores, reflecting genome size rather than metal biology."
first_added: "2026-10-27"
source_hash: "9ea58c19144575c5e8a783b777863269a18b37241d89bb6c0a9c2a044de1353d"
---
# Bioleaching genera not enriched for metal signature after normalization

After genome-size normalization, bioleaching genera as a group are not significantly enriched over background in the 1,286-term KEGG KO metal signature scored across 27,702 pangenome species (Mann-Whitney p=0.17), although Leptospirillum ranks at the 91st percentile individually. [src: metal_fitness_atlas]

## Key figures

- **0.17**: Mann-Whitney p-value for bioleaching genera versus background (scope after genome-size normalization) [src: metal_fitness_atlas]
- **27,702 species**: pangenome species scored [src: metal_fitness_atlas]
- **91st percentile**: Leptospirillum percentile after genome-size normalization (scope normalized score) [src: metal_fitness_atlas]

## Evidence

> A metal functional signature of 1,286 KEGG KO terms was derived from the conserved metal gene families and used to score all **27,702 pangenome species**. With genome-size normalization (metal clusters / total KEGG-annotated clusters), the true specialist bioleaching organisms emerge: *Leptospirillum* ranks at the 91st percentile, *Acidithiobacillus* at the 77th, *Marinobacter* at the 75th, and *Sulfobacillus* at the 71st. However, bioleaching genera as a group are not significantly enriched over background after normalization (Mann-Whitney p=0.17), indicating that metal tolerance genes are broadly distributed across bacteria rather than concentrated in specialists — consistent with the core genome robustness model. Without normalization, species with large open pangenomes (*K. pneumoniae*, *P. aeruginosa*) dominate, reflecting genome size rather than metal biology. [src: metal_fitness_atlas]

From the report [[summaries/metal_fitness_atlas__REPORT]].

## Caveat

Without genome-size normalization, species with large open pangenomes (K. pneumoniae, P. aeruginosa) dominate the scores, reflecting genome size rather than metal biology. [src: metal_fitness_atlas]

> A metal functional signature of 1,286 KEGG KO terms was derived from the conserved metal gene families and used to score all **27,702 pangenome species**. With genome-size normalization (metal clusters / total KEGG-annotated clusters), the true specialist bioleaching organisms emerge: *Leptospirillum* ranks at the 91st percentile, *Acidithiobacillus* at the 77th, *Marinobacter* at the 75th, and *Sulfobacillus* at the 71st. However, bioleaching genera as a group are not significantly enriched over background after normalization (Mann-Whitney p=0.17), indicating that metal tolerance genes are broadly distributed across bacteria rather than concentrated in specialists — consistent with the core genome robustness model. Without normalization, species with large open pangenomes (*K. pneumoniae*, *P. aeruginosa*) dominate, reflecting genome size rather than metal biology. [src: metal_fitness_atlas]

## Other caveats in this report

- Excluding 4 duplicate P. fluorescens FW300 strains reduces the analysis from 22 to 18 organisms while retaining core enrichment (OR=2.065, p=5.9e-141 versus OR=2.083, p=4.3e-162). [src: metal_fitness_atlas]
- Conservation analysis covers 22 of 31 metal-tested organisms (71%); 9 lack Fitness Browser–pangenome links. [src: metal_fitness_atlas]
- The 31 organisms with metal data include only 24 with fitness matrices; the experiment-coverage scope is broader than the gene-fitness dataset. [src: metal_fitness_atlas]
- The prior DvH condition-specific heavy-metal analysis found 71.2% core; this atlas includes all genes with metal fitness defects, a broader definition that explains the differing conservation result. [src: metal_fitness_atlas]
- Metal concentrations vary across organisms—for nickel, 0.01-2.0 mM—without dose-response normalization. [src: metal_fitness_atlas]
