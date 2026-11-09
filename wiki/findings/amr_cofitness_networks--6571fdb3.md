---
type: "Finding"
description: "Efflux AMR genes showed histidine-biosynthesis enrichment in 6 organisms and tryptophan in 5, and metal-resistance genes showed stronger chemotaxis enrichment in 4, but no GO term was significantly mechanism-specific after FDR correction."
finding_id: "amr_cofitness_networks--6571fdb3"
result: "null result"
source: "amr_cofitness_networks"
quantities: [{"value": "6", "what": "organisms with histidine biosynthesis enrichment in efflux AMR genes", "unit": "organisms", "denominator": "", "scope": ""}, {"value": "5", "what": "organisms with tryptophan biosynthesis enrichment in efflux AMR genes", "unit": "organisms", "denominator": "", "scope": ""}]
caveat: "The only hint of mechanism specificity, histidine biosynthesis (efflux 68% vs metal 30%), had p = 0.013 uncorrected and q = 0.18 after FDR."
first_added: "2026-11-09"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# No GO term is mechanism-specific after FDR correction

Efflux AMR genes showed histidine-biosynthesis enrichment in 6 organisms and tryptophan in 5, and metal-resistance genes showed stronger chemotaxis enrichment in 4, but no GO term was significantly mechanism-specific after FDR correction. [src: amr_cofitness_networks]

## Key figures

- **6 organisms**: organisms with histidine biosynthesis enrichment in efflux AMR genes [src: amr_cofitness_networks]
- **5 organisms**: organisms with tryptophan biosynthesis enrichment in efflux AMR genes [src: amr_cofitness_networks]

## Evidence

> By mechanism, efflux AMR genes show the strongest enrichment for amino acid biosynthesis (histidine in 6 organisms, tryptophan in 5), while metal resistance genes show stronger chemotaxis enrichment (4 organisms). However, no GO term is significantly mechanism-specific after FDR correction. [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

The only hint of mechanism specificity, histidine biosynthesis (efflux 68% vs metal 30%), had p = 0.013 uncorrected and q = 0.18 after FDR. [src: amr_cofitness_networks]

> The only hint of mechanism specificity is histidine biosynthesis (efflux 68% vs metal 30%, p = 0.013 uncorrected, q = 0.18 after FDR). [src: amr_cofitness_networks]

## Other caveats in this report

- Flagellar and biosynthesis enrichment may reflect shared dispensability in shaken liquid culture and supplemented media rather than co-regulation; the report calls for a fitness-matched permutation. [src: amr_cofitness_networks]
- Old KEGG analysis reported two FDR-significant mechanism-specific terms (lipoprotein and toluene tolerance), whereas InterProScan GO reported zero. [src: amr_cofitness_networks]
- The permutation matched conservation class but not mean fitness, leaving open whether fitness matching would eliminate the flagellar signal. [src: amr_cofitness_networks]
- Pearson correlation removes uniform mean-fitness differences, but condition-specific covariation among dispensable genes can still mimic co-regulation. [src: amr_cofitness_networks]
- The proposed discriminator is a non-AMR permutation matched to mean fitness −0.05 to +0.05: similar flagellar enrichment in controls would support shared dispensability, whereas AMR-specific enrichment would support co-regulation. [src: amr_cofitness_networks]
