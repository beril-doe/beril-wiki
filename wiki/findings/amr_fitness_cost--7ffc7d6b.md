---
type: "Finding"
description: "The antibiotic-dependent fitness flip is mechanism-dependent: efflux genes (broad-spectrum) show a significantly stronger flip than enzymatic inactivation genes (narrow-spectrum), +0.094 vs \u22120.001, MWU p = 0.007."
finding_id: "amr_fitness_cost--7ffc7d6b"
result: "observation"
source: "amr_fitness_cost"
quantities: [{"value": "+0.094", "what": "flip for efflux genes", "unit": "", "denominator": "", "scope": ""}, {"value": "\u22120.001", "what": "flip for enzymatic inactivation genes", "unit": "", "denominator": "", "scope": ""}, {"value": "0.007", "what": "Mann-Whitney U p-value for the difference", "unit": "", "denominator": "", "scope": "efflux vs enzymatic inactivation"}]
caveat: "The report proposes that the 43% of AMR genes that don't flip reflect narrow-spectrum resistance tested against non-matching antibiotics, not non-functional genes."
first_added: "2026-10-27"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# Efflux genes flip toward importance under antibiotics more than enzymatic inactivation genes

The antibiotic-dependent fitness flip is mechanism-dependent: efflux genes (broad-spectrum) show a significantly stronger flip than enzymatic inactivation genes (narrow-spectrum), +0.094 vs −0.001, MWU p = 0.007. [src: amr_fitness_cost]

## Key figures

- **+0.094**: flip for efflux genes [src: amr_fitness_cost]
- **−0.001**: flip for enzymatic inactivation genes [src: amr_fitness_cost]
- **0.007**: Mann-Whitney U p-value for the difference (scope efflux vs enzymatic inactivation) [src: amr_fitness_cost]

## Evidence

> Critically, this flip is **mechanism-dependent**: efflux genes (broad-spectrum) show a significantly stronger flip than enzymatic inactivation genes (narrow-spectrum): +0.094 vs −0.001, MWU p = 0.007. [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

The report proposes that the 43% of AMR genes that don't flip reflect narrow-spectrum resistance tested against non-matching antibiotics, not non-functional genes. [src: amr_fitness_cost]

> The 43% of AMR genes that don't flip likely reflect narrow-spectrum resistance being tested against non-matching antibiotics, not non-functional genes. [src: amr_fitness_cost]

## Other caveats in this report

- The report argues that low AMR putative essentiality reduces concern about strong right-censoring. [src: amr_fitness_cost]
- Small per-class samples and organism heterogeneity are proposed, not established, explanations for the class-matched null result. [src: amr_fitness_cost]
- Compensatory evolution as the explanation for uniform mechanism costs is a hypothesis, not a direct measurement. [src: amr_fitness_cost]
- An irreducible gene-maintenance cost floor is speculative. [src: amr_fitness_cost]
- GTDB sampling per Fitness Browser species is sparse (median 9 genomes, range 2–399), making the ≥95% core designation imprecise, particularly with 2–9 genomes. [src: amr_fitness_cost]
