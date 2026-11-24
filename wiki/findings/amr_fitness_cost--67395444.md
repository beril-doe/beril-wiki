---
type: "Finding"
description: "While mechanism doesn't predict fitness cost, it strongly predicts conservation status (\u03c7\u00b2 = 69.3, p = 1.4\u00d710\u207b\u00b9\u00b3)."
finding_id: "amr_fitness_cost--67395444"
result: "observation"
source: "amr_fitness_cost"
quantities: [{"value": "\u03c7\u00b2 = 69.3", "what": "chi-square for mechanism versus conservation", "unit": "", "denominator": "", "scope": ""}, {"value": "p = 1.4\u00d710\u207b\u00b9\u00b3", "what": "significance", "unit": "", "denominator": "", "scope": ""}]
caveat: "Most FB species have few genomes (median 9), making the \u226595% prevalence threshold for core imprecise, so the core versus accessory null should be interpreted cautiously for species with <20 genomes."
first_added: "2026-11-24"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# Mechanism predicts pangenome conservation of AMR genes

While mechanism doesn't predict fitness cost, it strongly predicts conservation status (χ² = 69.3, p = 1.4×10⁻¹³). [src: amr_fitness_cost]

## Key figures

- **χ² = 69.3**: chi-square for mechanism versus conservation [src: amr_fitness_cost]
- **p = 1.4×10⁻¹³**: significance [src: amr_fitness_cost]

## Evidence

> While mechanism doesn't predict fitness cost, it strongly predicts conservation status (χ² = 69.3, p = 1.4×10⁻¹³). [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

Most FB species have few genomes (median 9), making the ≥95% prevalence threshold for core imprecise, so the core versus accessory null should be interpreted cautiously for species with <20 genomes. [src: amr_fitness_cost]

> Most FB species have few genomes (median 9), making the ≥95% prevalence threshold for "core" imprecise. The core vs accessory null result should be interpreted cautiously for species with <20 genomes. [src: amr_fitness_cost]

## Other caveats in this report

- The report suggests that the 43% of AMR genes without an antibiotic fitness flip likely reflect narrow-spectrum resistance tested against non-matching antibiotics rather than non-functional genes. [src: amr_fitness_cost]
- The report attributes the nonsignificant class-matched antibiotic result likely to small per-class sample sizes and organism heterogeneity, with strong flips in some organisms and near-zero flips in others. [src: amr_fitness_cost]
- The RB-TnSeq organisms are lab-adapted strains with extensive evolutionary time to compensate for resistance costs. [src: amr_fitness_cost]
- Most Fitness Browser species have few genomes in GTDB (median 9, range 2–399), making the ≥95% prevalence threshold for core AMR gene designation imprecise. [src: amr_fitness_cost]
- With only 2–9 genomes, a gene present in all 9 can be labeled core yet prove accessory with greater sampling depth. [src: amr_fitness_cost]
