---
type: "Concept"
description: "How CAZyme class counts and the glycosyl transferase to glycoside hydrolase balance in bacterial genomes differ across biomes, and which lineages drive it; stops short of family-level substrate specificity."
sources: ["summaries/cazyme_pangenome_ecology__REPORT.md"]
---
# Biome-level carbohydrate-active enzyme repertoire differentiation

Bacterial genomes differ strongly in carbohydrate-active enzyme (CAZyme) content across biomes, and the glycosyl transferase (GT) to glycoside hydrolase (GH) balance separates degradation-oriented from biosynthesis-oriented environments. [src: cazyme_pangenome_ecology] The evidence is one cross-sectional, genome-resolved dataset at CAZy class resolution, and it supports association, not cause. [src: cazyme_pangenome_ecology] See [[summaries/cazyme_pangenome_ecology__REPORT]].

## Literature Context

The candidate papers show that CAZyme repertoires are structured by habitat and lineage, mostly at family resolution and in narrower settings than a pan-biome survey. A curated resource of 43,972 human gut bacterial genomes yielded 475 CAZyme families, with a conserved core of 73 families (15.4%). Taxa fell into four functional clusters, and growth assays on representative strains were consistent with the cluster assignments [PMID 41794458](https://pubmed.ncbi.nlm.nih.gov/41794458/). In piglet gut collections, glycoside hydrolases were the dominant CAZyme category among 266 cultured genomes and 482 MAGs (metagenome-assembled genomes) [PMID 35171009](https://pubmed.ncbi.nlm.nih.gov/35171009/). A separate post-weaning study tracked 294 carbohydrate-active enzymes across porcine gut MAGs and assigned them to taxa [PMID 34370660](https://pubmed.ncbi.nlm.nih.gov/34370660/). Antarctic krill gut isolates and metagenomes were rich in hydrolases, and Flavobacteriaceae and Pseudoalteromonadaceae dominated the carbohydrate-active enzyme capacity [PMID 38466097](https://pubmed.ncbi.nlm.nih.gov/38466097/). In a small comparison of mangrove and terrestrial forest soils, only 15 MAGs were recovered. Carbohydrate-processing differences were organized at the lineage level, and several MAG-reference pairs stayed comparatively conserved [PMID 42785187](https://pubmed.ncbi.nlm.nih.gov/42785187/). Bacteroidetes glycosidases from the human gut have also been reported as a source of cell-penetrating fragments, which shows that GH-rich Bacteroidetes matter beyond digestion. That was a functional screen, not a repertoire comparison [PMID 42425523](https://pubmed.ncbi.nlm.nih.gov/42425523/).

The corpus's central measured claim is that all 6 non-zero CAZy classes differ across 18 biomes. The effect survived genome-size correction and held within all 5 top phyla. Its GT/GH ratio, which it proposes as an ecological metric separating consumers from producers, is an interpretation and was not tested as a separation. The biome-level result is consistent with the literature in direction. The papers above agree that CAZyme content varies with environment and lineage, and that GHs are prominent in the guts of animals. Partial support comes from piglet gut genomes with GH dominance [PMID 35171009](https://pubmed.ncbi.nlm.nih.gov/35171009/). The corpus table shows GH above GT in pig-gut (16.8 versus 10.8) and rumen genomes, but not in every gut biome. Honeybee-gut has GT 18.4 against GH 14.8. The comparison is therefore partial, not a general gut-wide agreement. The Bacteroidota emphasis, with soil Bacteroidota at a mean of 65.3 GH genes, fits the importance of Bacteroidetes glycosidases in gut and marine-animal microbiota [PMID 42425523](https://pubmed.ncbi.nlm.nih.gov/42425523/), [PMID 38466097](https://pubmed.ncbi.nlm.nih.gov/38466097/). The lineage-level organization in forest MAGs also resembles the corpus's lineage-driven pattern, though that study is small [PMID 42785187](https://pubmed.ncbi.nlm.nih.gov/42785187/).

The corpus extends this work by comparing biomes at one class-level resolution across a very large genome set, where the candidates are single-habitat or family-resolved. It does not resolve substrate specificity. Family-level work such as the human gut atlas, with its enrichment of GH30/GH30_9/GH79 in Bifidobacterium [PMID 41794458](https://pubmed.ncbi.nlm.nih.gov/41794458/), shows what the corpus's proposed family-level follow-up could reveal. None of the candidates tests the GT/GH ratio as a predictor of biome or of EPS production, so those claims stay novel and untested. No candidate contradicts the corpus. Its cross-sectional, associational design remains a limit that these studies do not address.

## Biome effect on CAZy classes

All 6 non-zero CAZy classes differed across 18 biomes (Kruskal-Wallis test, all p < 10^-150 after Benjamini-Hochberg false discovery rate, BH-FDR, correction). [src: cazyme_pangenome_ecology] The effect survived genome-size correction (Kruskal-Wallis on per-Mbp residuals). It was also significant within all 5 top phyla: Pseudomonadota, Firmicutes_A, Bacteroidota, Bacillota_A and Actinomycetota. [src: cazyme_pangenome_ecology] Test statistics were GT H = 12,524 [src: cazyme_pangenome_ecology], GH H = 7,793 [src: cazyme_pangenome_ecology], CB H = 7,527 [src: cazyme_pangenome_ecology], CE H = 2,584 [src: cazyme_pangenome_ecology], PL H = 893 (BH-adjusted p 1.1 × 10^-180) [src: cazyme_pangenome_ecology] and AA H = 767 (BH-adjusted p 8.3 × 10^-154). [src: cazyme_pangenome_ecology] The class CL was all zeros and was excluded. [src: cazyme_pangenome_ecology]

## Class counts by biome

Total CAZyme load spans 3.5× across biomes, from barley-rhizosphere (68.5) to marine (21.9). [src: cazyme_pangenome_ecology] Fiber-rich environments carry 3–4× more GH genes than marine: sheep-rumen 28.9 mean genes, tomato-rhizosphere 31.9, barley-rhizosphere 37.7 and soil 23.5, against marine 9.0. [src: cazyme_pangenome_ecology] GT genes are enriched in soil (22.8) and rhizosphere (20–25) relative to gut biomes (~11–13). [src: cazyme_pangenome_ecology]

Mean values per genome, by biome (genomes; total CAZy; GH; GT):

| Biome | Genomes | Total | GH | GT |
|---|---|---|---|---|
| barley-rhizo. | 74 | 68.5 | 37.7 | 24.6 [src: cazyme_pangenome_ecology] |
| tomato-rhizo. | 471 | 60.2 | 31.9 | 22.0 [src: cazyme_pangenome_ecology] |
| soil | 16,628 | 50.7 | 23.5 | 22.8 [src: cazyme_pangenome_ecology] |
| sheep-rumen | 1,871 | 49.4 | 28.9 | 15.8 [src: cazyme_pangenome_ecology] |
| maize-rhizo. | 265 | 50.4 | 25.4 | 19.9 [src: cazyme_pangenome_ecology] |
| zebrafish-fecal | 67 | 41.5 | 19.3 | 18.2 [src: cazyme_pangenome_ecology] |
| cow-rumen | 2,729 | 39.1 | 23.7 | 11.7 [src: cazyme_pangenome_ecology] |
| mouse-gut | 2,847 | 36.2 | 20.0 | 12.9 [src: cazyme_pangenome_ecology] |
| honeybee-gut | 128 | 35.1 | 14.8 | 18.4 [src: cazyme_pangenome_ecology] |
| human-skin | 476 | 32.8 | 14.0 | 15.0 [src: cazyme_pangenome_ecology] |
| marine-sed. | 5,169 | 32.5 | 14.6 | 15.6 [src: cazyme_pangenome_ecology] |
| human-gut | 4,158 | 31.4 | 16.6 | 12.2 [src: cazyme_pangenome_ecology] |
| chicken-gut | 1,286 | 30.5 | 16.4 | 11.4 [src: cazyme_pangenome_ecology] |
| pig-gut | 1,263 | 30.1 | 16.8 | 10.8 [src: cazyme_pangenome_ecology] |
| non-model-fish | 152 | 30.0 | 15.0 | 12.4 [src: cazyme_pangenome_ecology] |
| human-oral | 408 | 25.2 | 11.3 | 11.5 [src: cazyme_pangenome_ecology] |
| marine | 11,132 | 21.9 | 9.0 | 11.0 [src: cazyme_pangenome_ecology] |
| human-vaginal | 249 | 20.5 | 8.9 | 9.0 [src: cazyme_pangenome_ecology] |

## GT/GH balance

The report proposes the GT/GH ratio as an ecological metric that separates carbohydrate consumers (GH-dominant) from producers (GT-dominant). [src: cazyme_pangenome_ecology] In rumen genomes, 74% have GH > GT, which the report reads as degradation dominance on fiber-rich substrate. [src: cazyme_pangenome_ecology] Soil genomes are balanced (GT ≈ GH), which the report attributes to dual demands for plant-polysaccharide degradation and EPS biosynthesis for biofilms and soil particle adhesion. [src: cazyme_pangenome_ecology] In marine genomes, 71% have GT > GH, which the report interprets as investment in capsules, biofilms and cell-surface structures in oligotrophic waters. [src: cazyme_pangenome_ecology] The report says that neither the marine nor the rumen proportion has been reported before. [src: cazyme_pangenome_ecology]

The report's wider interpretation is that carbohydrate substrate availability constrains bacterial genomes. [src: cazyme_pangenome_ecology] Fiber-rich rumen, soil and rhizosphere environments are said to select for large GH repertoires. [src: cazyme_pangenome_ecology] Oligotrophic marine environments are said to yield relatively more GT for protective surface structures. [src: cazyme_pangenome_ecology] These are interpretations, not tested mechanisms.

## Lineages driving the pattern

Bacteroidota have the most GH-skewed profiles, and Pseudomonadota are relatively GT-enriched. [src: cazyme_pangenome_ecology] Soil Bacteroidota carry a mean of 65.3 GH genes. That is the highest of any phylum–biome combination and 2.8× the Bacteroidota cross-biome average. [src: cazyme_pangenome_ecology] The report states that this magnitude had not been quantified at genome-resolved scale, and that this is the first pan-bacterial quantification. [src: cazyme_pangenome_ecology] See [[entities/bacteroidota]], [[entities/pseudomonadota]], [[entities/glycoside-hydrolases]] and [[entities/glycosyl-transferases]].

## Relation to earlier work

The soil-versus-marine contrast agrees with López-Sánchez et al. (2024). That study found more abundant and diverse CAZymes in soil MAGs (metagenome assembled genomes) than in marine sediment MAGs within Bacteroidia, Gammaproteobacteria and Alphaproteobacteria. [src: cazyme_pangenome_ecology] The report says it extends that comparison from 37 sediment sites to 18 biomes at 49K-genome scale. [src: cazyme_pangenome_ecology] It also claims the first genome-resolved CAZyme class-composition analysis at this scale. [src: cazyme_pangenome_ecology] Sun et al. (2023) found different CAZyme compositions in free-living and particle-associated marine bacteria, and the report presents its work as extending this to a pan-environmental framework. [src: cazyme_pangenome_ecology] Andrade et al. (2017) compared freshwater and soil CAZyme metagenomes in the Caatinga biome and found environment-specific differences. [src: cazyme_pangenome_ecology]

## Limits

- The data cannot show whether environment shapes CAZyme repertoires or repertoires determine environment. [src: cazyme_pangenome_ecology]
- The design is cross-sectional: biomes are compared, and lineages colonizing new environments are not tracked. [src: cazyme_pangenome_ecology]
- The [[entities/kescience-mgnify]] genome_cazy table gives only 7 top-level classes (GH, GT, PL, CE, AA, CB, CL), not families such as GH1 or GH2. [src: cazyme_pangenome_ecology]
- Finer substrate-specificity analysis needs arkinlab_dbcan, which has only 1,161 MGnify genomes, 2.3% of the catalog. [src: cazyme_pangenome_ecology]

## Proposed follow-up in the report

The report proposes repeating the analysis at family level as arkinlab_dbcan covers more MGnify genomes. [src: cazyme_pangenome_ecology] It also proposes testing whether the GT/GH ratio predicts biome of origin in a held-out set [src: cazyme_pangenome_ecology] and whether it correlates with measured EPS production or polysaccharide degradation phenotypes. [src: cazyme_pangenome_ecology]

## Open Directions

- Repeat the analysis at CAZy family level (GH1, GH2, etc.) as arkinlab_dbcan grows. This would show which substrate-degradation pathways are enriched in each biome.
- Test whether the GT/GH ratio predicts biome of origin in a held-out genome set. This would check whether the ratio is a usable ecological metric.
- Test whether the GT/GH ratio correlates with measured EPS production or polysaccharide degradation phenotypes. This would check the functional interpretation.
- Compare lineages that have colonized new environments with their relatives. This would address the cross-sectional limit and the causal question.
