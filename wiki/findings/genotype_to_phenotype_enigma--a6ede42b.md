---
type: "Finding"
description: "Across 464K samples, the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9\u00b0C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster worldwide."
finding_id: "genotype_to_phenotype_enigma--a6ede42b"
result: "observation"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "1.35", "what": "pH units more acidic for the Rhodanobacter-Ralstonia-Dyella cluster", "unit": "pH units", "denominator": "", "scope": "464K global samples"}, {"value": "6.9", "what": "warmer environments for the same cluster", "unit": "\u00b0C", "denominator": "", "scope": "464K global samples"}]
caveat: "Spearman co-occurrence suggests shared or exclusive niches but does not prove direct interaction, and compositionally aware SparCC analysis on the full 100WS ASV matrix is suggested."
first_added: "2026-10-27"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Global pH niche partition separates two Oak Ridge genus clusters

Across 464K samples, the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9°C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster worldwide. [src: genotype_to_phenotype_enigma]

## Key figures

- **1.35 pH units**: pH units more acidic for the Rhodanobacter-Ralstonia-Dyella cluster (scope 464K global samples) [src: genotype_to_phenotype_enigma]
- **6.9 °C**: warmer environments for the same cluster (scope 464K global samples) [src: genotype_to_phenotype_enigma]

## Evidence

> - **A global pH-driven niche partition (464K samples)** explains local Oak Ridge co-occurrence: the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9°C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster worldwide. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

Spearman co-occurrence suggests shared or exclusive niches but does not prove direct interaction, and compositionally aware SparCC analysis on the full 100WS ASV matrix is suggested. [src: genotype_to_phenotype_enigma]

> - **Co-occurrence is correlation, not causation**: Spearman co-occurrence suggests shared/exclusive niches but does not prove direct interaction. SparCC analysis (compositionally aware) on the full 100WS ASV matrix would strengthen these findings. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- Ribose transporter and protocatechuate cycloisomerase are interpretable feature examples, but concordance with Fitness Browser is weak at 1.19× enrichment; cross-genus gene presence and within-strain essentiality address different questions. [src: genotype_to_phenotype_enigma]
- GTDB-based profiles classify global Pseudomonas genomes as 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic, whereas ENIGMA Pseudomonas are in environmental Pseudomonas_E. Rhodanobacter is reported as 55% aquatic, 10% contaminated, and 0% clinical. Transfer from clinical phenotype databases may be biased. [src: genotype_to_phenotype_enigma]
- Different pH-dependent growth profiles and predictive genomic features for the two clusters are proposed expectations, not reported validation results. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains by `ncbi_strain_identifiers` caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The MT20 collision linked Rhodanobacter glycinis to unrelated Streptococcus pneumoniae and introduced 1,751 spurious clinical genomes. GTDB-Tk taxonomy and genus checks reduced verified linkages from 32 to 20 while eliminating false matches. [src: genotype_to_phenotype_enigma]
