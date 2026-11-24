---
type: "Finding"
description: "The antibiotic-dependent fitness flip is mechanism-dependent: efflux genes (broad-spectrum) show a significantly stronger flip than enzymatic inactivation genes (narrow-spectrum): +0.094 vs \u22120.001, MWU p = 0.007."
finding_id: "amr_fitness_cost--7ffc7d6b"
result: "observation"
source: "amr_fitness_cost"
quantities: [{"value": "+0.094", "what": "efflux gene fitness flip", "unit": "fitness units", "denominator": "", "scope": "efflux genes"}, {"value": "\u22120.001", "what": "enzymatic inactivation gene fitness flip", "unit": "fitness units", "denominator": "", "scope": "enzymatic inactivation genes"}, {"value": "p = 0.007", "what": "MWU test", "unit": "", "denominator": "", "scope": ""}]
caveat: "The nonsignificant class-matched result is likely due to small N per class after matching and heterogeneity across organisms, with some organisms showing strong flips and others near zero."
first_added: "2026-11-24"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# Efflux genes flip more strongly under antibiotics than enzymatic genes

The antibiotic-dependent fitness flip is mechanism-dependent: efflux genes (broad-spectrum) show a significantly stronger flip than enzymatic inactivation genes (narrow-spectrum): +0.094 vs −0.001, MWU p = 0.007. [src: amr_fitness_cost]

## Key figures

- **+0.094 fitness units**: efflux gene fitness flip (scope efflux genes) [src: amr_fitness_cost]
- **−0.001 fitness units**: enzymatic inactivation gene fitness flip (scope enzymatic inactivation genes) [src: amr_fitness_cost]
- **p = 0.007**: MWU test [src: amr_fitness_cost]

## Evidence

> Critically, this flip is **mechanism-dependent**: efflux genes (broad-spectrum) show a significantly stronger flip than enzymatic inactivation genes (narrow-spectrum): +0.094 vs −0.001, MWU p = 0.007. [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

The nonsignificant class-matched result is likely due to small N per class after matching and heterogeneity across organisms, with some organisms showing strong flips and others near zero. [src: amr_fitness_cost]

> This is likely due to the small N per class after matching and heterogeneity across organisms — some organisms show strong flips while others are near zero. [src: amr_fitness_cost]

## Other caveats in this report

- The report suggests that the 43% of AMR genes without an antibiotic fitness flip likely reflect narrow-spectrum resistance tested against non-matching antibiotics rather than non-functional genes. [src: amr_fitness_cost]
- The RB-TnSeq organisms are lab-adapted strains with extensive evolutionary time to compensate for resistance costs. [src: amr_fitness_cost]
- Most Fitness Browser species have few genomes in GTDB (median 9, range 2–399), making the ≥95% prevalence threshold for core AMR gene designation imprecise. [src: amr_fitness_cost]
- With only 2–9 genomes, a gene present in all 9 can be labeled core yet prove accessory with greater sampling depth. [src: amr_fitness_cost]
- Absolute AMR knockout fitness averages −0.024, so AMR knockouts still grow slower than the pool average; their advantage is relative to a non-AMR background averaging around −0.11. [src: amr_fitness_cost]
