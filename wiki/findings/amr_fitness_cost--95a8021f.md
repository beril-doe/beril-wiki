---
type: "Finding"
description: "Core (intrinsic, N=638) and accessory (acquired, N=163) AMR genes show virtually identical fitness distributions: mean \u22120.024 vs \u22120.024, Cohen's d = 0.002, MWU p = 0.33."
finding_id: "amr_fitness_cost--95a8021f"
result: "null result"
source: "amr_fitness_cost"
quantities: [{"value": "N=638", "what": "core AMR genes", "unit": "genes", "denominator": "", "scope": ""}, {"value": "N=163", "what": "accessory AMR genes", "unit": "genes", "denominator": "", "scope": ""}, {"value": "p = 0.33", "what": "MWU test", "unit": "", "denominator": "", "scope": ""}]
caveat: "Most FB species have few genomes in GTDB (median 9, range 2\u2013399), which makes the \u226595% prevalence threshold for core designation imprecise."
first_added: "2026-11-24"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# Core and accessory AMR genes have identical fitness distributions

Core (intrinsic, N=638) and accessory (acquired, N=163) AMR genes show virtually identical fitness distributions: mean −0.024 vs −0.024, Cohen's d = 0.002, MWU p = 0.33. [src: amr_fitness_cost]

## Key figures

- **N=638 genes**: core AMR genes [src: amr_fitness_cost]
- **N=163 genes**: accessory AMR genes [src: amr_fitness_cost]
- **p = 0.33**: MWU test [src: amr_fitness_cost]

## Evidence

> Core (intrinsic, N=638) and accessory (acquired, N=163) AMR genes show virtually identical fitness distributions: mean −0.024 vs −0.024, Cohen's d = 0.002, MWU p = 0.33. [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

Most FB species have few genomes in GTDB (median 9, range 2–399), which makes the ≥95% prevalence threshold for core designation imprecise. [src: amr_fitness_cost]

> An important caveat: most FB species have few genomes in GTDB (median 9, range 2–399), which makes the ≥95% prevalence threshold for "core" designation imprecise. [src: amr_fitness_cost]

## Other caveats in this report

- The report suggests that the 43% of AMR genes without an antibiotic fitness flip likely reflect narrow-spectrum resistance tested against non-matching antibiotics rather than non-functional genes. [src: amr_fitness_cost]
- The report attributes the nonsignificant class-matched antibiotic result likely to small per-class sample sizes and organism heterogeneity, with strong flips in some organisms and near-zero flips in others. [src: amr_fitness_cost]
- The RB-TnSeq organisms are lab-adapted strains with extensive evolutionary time to compensate for resistance costs. [src: amr_fitness_cost]
- With only 2–9 genomes, a gene present in all 9 can be labeled core yet prove accessory with greater sampling depth. [src: amr_fitness_cost]
- Absolute AMR knockout fitness averages −0.024, so AMR knockouts still grow slower than the pool average; their advantage is relative to a non-AMR background averaging around −0.11. [src: amr_fitness_cost]
