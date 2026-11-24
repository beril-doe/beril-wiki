---
type: "Finding"
description: "ICA-derived co-regulated multi-gene modules show a substantially stronger co-inheritance signal (delta=+0.053, 26% significant at p<0.05, 11% after FDR correction)."
finding_id: "cofitness_coinheritance--92f9f732"
result: "inference"
source: "cofitness_coinheritance"
quantities: [{"value": "delta=+0.053", "what": "module-level delta phi", "unit": "", "denominator": "", "scope": ""}, {"value": "26%", "what": "modules significant at p<0.05", "unit": "", "denominator": "", "scope": ""}, {"value": "11%", "what": "modules significant after FDR correction", "unit": "", "denominator": "", "scope": ""}]
caveat: "Co-fitness captures pairwise gene relationships, whereas ICA modules capture multi-gene coordinated regulation, which may better reflect the selective units that constrain co-inheritance."
first_added: "2026-11-24"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Multi-gene ICA modules show stronger co-inheritance than pairwise co-fitness

ICA-derived co-regulated multi-gene modules show a substantially stronger co-inheritance signal (delta=+0.053, 26% significant at p<0.05, 11% after FDR correction). [src: cofitness_coinheritance]

## Key figures

- **delta=+0.053**: module-level delta phi [src: cofitness_coinheritance]
- **26%**: modules significant at p<0.05 [src: cofitness_coinheritance]
- **11%**: modules significant after FDR correction [src: cofitness_coinheritance]

## Evidence

> **Multi-gene modules** (ICA-derived co-regulated groups) show a substantially stronger co-inheritance signal (delta=+0.053, 26% significant at p<0.05, 11% after FDR correction), particularly accessory modules (73% significant, 36% after FDR). [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

Co-fitness captures pairwise gene relationships, whereas ICA modules capture multi-gene coordinated regulation, which may better reflect the selective units that constrain co-inheritance. [src: cofitness_coinheritance]

> **Pairwise vs multi-gene**: Co-fitness captures pairwise gene relationships. ICA modules capture multi-gene coordinated regulation, which may better reflect the selective units that constrain co-inheritance. [src: cofitness_coinheritance]

## Other caveats in this report

- In Korea, 95.2% of cofit pairs had NaN phi because both genes had 100% prevalence across 72 genomes, producing zero-variance vectors. [src: cofitness_coinheritance]
- Only ~8,000 of 166,601 Korea pairs were computable, and the report attributes the negative delta to statistical noise rather than a biological signal. [src: cofitness_coinheritance]
- The report suggests that the negative co-fitness-strength association likely reflects a prevalence ceiling effect, because the strongest co-fitness pairs are core genes with near-universal prevalence and little co-occurrence variance. [src: cofitness_coinheritance]
- Most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance]
- Ralstonia UW163 and GMI1000 were excluded from primary analysis because they had zero Fitness Browser co-fitness data despite appearing in its organism table. [src: cofitness_coinheritance]
