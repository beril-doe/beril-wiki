---
type: "Finding"
description: "Accessory ICA modules (<50% core; n=11) had mean delta phi +0.108, with 8/11 (73%) significant at p<0.05 and 4/11 (36%) at FDR q<0.05."
finding_id: "cofitness_coinheritance--9ed1fa6e"
result: "observation"
source: "cofitness_coinheritance"
quantities: [{"value": "+0.108", "what": "mean delta phi", "unit": "", "denominator": "", "scope": ""}, {"value": "8/11 (73%)", "what": "modules significant at p<0.05", "unit": "", "denominator": "", "scope": ""}, {"value": "4/11 (36%)", "what": "modules significant at FDR q<0.05", "unit": "", "denominator": "", "scope": ""}]
caveat: "Korea, the best pairwise organism, shows 0% significant modules, all >90% core with prevalence near 1.0."
first_added: "2026-11-24"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Accessory ICA modules show the strongest co-inheritance

Accessory ICA modules (<50% core; n=11) had mean delta phi +0.108, with 8/11 (73%) significant at p<0.05 and 4/11 (36%) at FDR q<0.05. [src: cofitness_coinheritance]

## Key figures

- **+0.108**: mean delta phi [src: cofitness_coinheritance]
- **8/11 (73%)**: modules significant at p<0.05 [src: cofitness_coinheritance]
- **4/11 (36%)**: modules significant at FDR q<0.05 [src: cofitness_coinheritance]

## Evidence

> | Module type | n | Mean delta phi | Significant (p<0.05) | Significant (FDR q<0.05) | |-------------|---|---------------|---------------------|--------------------------| | Accessory (<50% core) | 11 | **+0.108** | **8/11 (73%)** | **4/11 (36%)** | | Core (>90% core) | 120 | +0.059 | 29/120 (24%) | 13/120 (11%) | | Mixed (50-90%) | 64 | +0.031 | 14/64 (22%) | 4/64 (6%) | [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

Korea, the best pairwise organism, shows 0% significant modules, all >90% core with prevalence near 1.0. [src: cofitness_coinheritance]

> Btheta shows the strongest module-level signal (61% significant), while Korea (despite being the best pairwise organism) shows 0% significant modules -- all Korea modules are >90% core with prevalence near 1.0. [src: cofitness_coinheritance]

## Other caveats in this report

- In Korea, 95.2% of cofit pairs had NaN phi because both genes had 100% prevalence across 72 genomes, producing zero-variance vectors. [src: cofitness_coinheritance]
- Only ~8,000 of 166,601 Korea pairs were computable, and the report attributes the negative delta to statistical noise rather than a biological signal. [src: cofitness_coinheritance]
- The report suggests that the negative co-fitness-strength association likely reflects a prevalence ceiling effect, because the strongest co-fitness pairs are core genes with near-universal prevalence and little co-occurrence variance. [src: cofitness_coinheritance]
- Most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance]
- Ralstonia UW163 and GMI1000 were excluded from primary analysis because they had zero Fitness Browser co-fitness data despite appearing in its organism table. [src: cofitness_coinheritance]
