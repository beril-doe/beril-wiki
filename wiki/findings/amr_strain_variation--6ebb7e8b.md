---
type: "Finding"
description: "Mantel tests comparing ANI distance matrices with AMR Jaccard distance matrices across 1,261 species show that 55.6% (701 species) have significant phylogenetic signal (FDR < 0.05), with a median Mantel r of 0.247 and 87.8% of species showing positive correlation."
finding_id: "amr_strain_variation--6ebb7e8b"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "55.6%", "what": "Species with significant phylogenetic signal", "unit": "%", "denominator": "1,261 species", "scope": "FDR < 0.05"}, {"value": "701", "what": "Species with significant Mantel signal", "unit": "species", "denominator": "1,261 species", "scope": "FDR < 0.05"}, {"value": "0.247", "what": "Median Mantel r", "unit": "", "denominator": "", "scope": "1,261 species"}, {"value": "87.8%", "what": "Species showing positive correlation", "unit": "%", "denominator": "1,261 species", "scope": ""}]
caveat: "ANI extraction was limited to species with <=500 genomes, excluding mega-species such as E. coli (15,388 genomes) and K. pneumoniae (14,240 genomes) from the phylogenetic signal analysis."
first_added: "2026-10-27"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# Over half of species show significant ANI–AMR phylogenetic signal

Mantel tests comparing ANI distance matrices with AMR Jaccard distance matrices across 1,261 species show that 55.6% (701 species) have significant phylogenetic signal (FDR < 0.05), with a median Mantel r of 0.247 and 87.8% of species showing positive correlation. [src: amr_strain_variation]

## Key figures

- **55.6%**: Species with significant phylogenetic signal (denominator 1,261 species; scope FDR < 0.05) [src: amr_strain_variation]
- **701 species**: Species with significant Mantel signal (denominator 1,261 species; scope FDR < 0.05) [src: amr_strain_variation]
- **0.247**: Median Mantel r (scope 1,261 species) [src: amr_strain_variation]
- **87.8%**: Species showing positive correlation (denominator 1,261 species) [src: amr_strain_variation]

## Evidence

> Mantel tests comparing ANI distance matrices with AMR Jaccard distance matrices across 1,261 species reveal that 55.6% (701 species) show significant phylogenetic signal (FDR < 0.05), with a median Mantel r of 0.247 and 87.8% of species showing positive correlation. [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

ANI extraction was limited to species with <=500 genomes, excluding mega-species such as E. coli (15,388 genomes) and K. pneumoniae (14,240 genomes) from the phylogenetic signal analysis. [src: amr_strain_variation]

> - **Species size cap for Mantel tests**: ANI extraction was limited to species with <=500 genomes for computational feasibility, excluding mega-species like *E. coli* (15,388 genomes) and *K. pneumoniae* (14,240 genomes) from the phylogenetic signal analysis. [src: amr_strain_variation]

## Other caveats in this report

- Coordinated defense against multiple drug classes is an interpretation of island composition, not a directly demonstrated functional effect. [src: amr_strain_variation]
- The authors interpret stronger non-core phylogenetic signal as suggesting clonal inheritance after acquisition rather than random horizontal acquisition. [src: amr_strain_variation]
- Environmental testing of AMR ecotypes was limited: 52.7% of genomes lacked a classifiable isolation_source, leaving only 2 species eligible for chi-squared tests under the stated criteria. [src: amr_strain_variation]
- Visual environmental structuring in three case-study species did not establish a statistically supported environment–ecotype association; the report describes the test as underpowered. [src: amr_strain_variation]
- The report cautions that sparse, noisy NCBI BioSample dates may explain the corrected temporal null result; it is not evidence that temporal trends are absent. [src: amr_strain_variation]
