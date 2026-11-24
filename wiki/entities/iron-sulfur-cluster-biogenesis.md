---
type: "Gene_Or_Pathway"
description: "Metal cofactor assembly pathway (iscS, iscU, sufB, nifU) with molybdopterin and cobalamin genes making up the cofactor-biosynthesis group with the strongest niche-breadth signal."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
aliases: ["Fe-S cluster assembly", "metal cofactor biosynthesis"]
---
# Iron-sulfur cluster biogenesis

Iron-sulfur (Fe–S) cluster biogenesis, also called Fe–S cluster assembly or metal cofactor biosynthesis, is the metal-cofactor assembly pathway behind genes such as iscS, iscU, sufB and nifU. In the comprehensive metal ecology report, the cofactor-biosynthesis group (Fe–S cluster, molybdopterin and cobalamin genes) has the strongest niche-breadth signal of any metal gene category. That result comes from one MAG-based analysis with only 7 KOs, so it needs caution. [src: comprehensive_metal_ecology]

## Key facts

- Sulfur-associated KOs predominantly encode the Fe–S cluster biogenesis proteins iscS, iscU, sufB and nifU. [src: comprehensive_metal_ecology]
- The cofactor category is anchored by 7 KOs encoding Fe–S cluster assembly, molybdopterin synthesis and cobalamin pathway genes. [src: comprehensive_metal_ecology]
- These genes are constitutively required in organisms that depend on metal-cofactor chemistry for core metabolism, including nitrogen fixation, anaerobic respiration and methanogenesis. [src: comprehensive_metal_ecology]
- The Fe–S cluster biosynthesis ortholog group (OG) COG0316/iscA occurs in 94.3% of plant species. [src: plant_microbiome_ecotypes]
- The plant microbiome report treats Fe–S clusters as essential cofactors for nitrogenase, respiratory chain complexes and oxidative stress defense. [src: plant_microbiome_ecotypes]
- That report cites Fuangthong et al. (2015) for a link between IscR-mediated Fe–S cluster regulation and both pathogenicity and oxidative stress resistance in plant-associated bacteria. [src: plant_microbiome_ecotypes] See [[concepts/functional-characterization-of-plant-enriched-gene-families]] and [[summaries/plant_microbiome_ecotypes__REPORT]].

## Niche-breadth association

Cofactor biosynthesis shows the largest metal functional-category effect on niche breadth, and it equals the housekeeping baseline. [src: comprehensive_metal_ecology] In the bacterial global MGnify MAG (metagenome-assembled genome) analysis, the category (7 KOs) has β = −0.033, standard error 0.005 and false-discovery-rate-adjusted p = 5.2×10⁻⁹. [src: comprehensive_metal_ecology] The report contrasts this with resistance/detoxification genes (106 KOs), which show no association (β ≈ 0, p = 0.66). [src: comprehensive_metal_ecology] It reads the exact match to the housekeeping baseline as constitutive, irreversible genomic investment. [src: comprehensive_metal_ecology] This links to [[concepts/constitutive-versus-inducible-gene-classes-in-niche-breadth-associations]]. The report also relates the signal to Fe–S cluster assembly being one of the most conserved, vertically inherited gene sets in prokaryotes (Lill 2009). [src: comprehensive_metal_ecology]

## Robustness

A leave-one-KO-out jackknife over the 4 assignable cofactor KOs (K01772, K02225, K03635, K22225) leaves every 3-KO remainder highly significant. The β range is −0.016 to −0.029, all p < 0.001, and no sign changes occur. [src: comprehensive_metal_ecology] The report concludes the signal is spread across the Fe–S cluster, molybdopterin and cobalamin pathway rather than concentrated in one gene. [src: comprehensive_metal_ecology]

## Caveats

The strongest categorical signal rests on only 7 KOs. The statistical result is robust (ΔAIC = −35.4), but the narrow biological definition warrants caution. [src: comprehensive_metal_ecology] The report states that no published study systematically quantifies Fe–S or molybdopterin gene variation by ecological niche type, and it calls this signal the project's novel observation. [src: comprehensive_metal_ecology] See also [[concepts/validity-of-curated-metal-gene-annotation]] and [[summaries/comprehensive_metal_ecology__REPORT]].
