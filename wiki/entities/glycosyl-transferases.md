---
type: "Gene_Or_Pathway"
description: "CAZy class of enzymes that build glycans such as exopolysaccharides and capsules, including the GT2 family near T4SS loci."
sources: ["summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/t4ss_cazy_environmental_hgt__REPORT.md"]
aliases: ["GT", "GT2", "GT2 glycosyltransferases", "glycosyltransferase family 2"]
---
# Glycosyl transferases

Glycosyl transferases (GT) are a CAZy class of enzymes that build glycans such as exopolysaccharides and capsules, including the GT2 family near T4SS loci. [src: cazyme_pangenome_ecology, t4ss_cazy_environmental_hgt] Two reports bear on them: one compares their abundance across biomes, and one links GT2 to type IV secretion system (T4SS) loci in environmental metagenome assembled genomes (MAGs). [src: cazyme_pangenome_ecology, t4ss_cazy_environmental_hgt]

## Key facts

- The report states that oligotrophic marine environments produce bacterial genomes with relatively more glycosyl transferases for biosynthesis of protective capsules and exopolysaccharides. [src: cazyme_pangenome_ecology]
- Pseudomonadota were relatively GT-enriched, while Bacteroidota had the most GH-skewed (glycoside hydrolase) profiles. [src: cazyme_pangenome_ecology] See [[entities/glycoside-hydrolases]].

## Distribution across biomes

Bacterial GT genes differ strongly by biome. They were enriched in soil (22.8) and rhizosphere (20–25) relative to gut biomes (~11–13), which the report describes as consistent with exopolysaccharide and biofilm biosynthesis demands. [src: cazyme_pangenome_ecology] The bacterial biome-effect Kruskal-Wallis test for class GT gave H = 12,524 and BH-adjusted p ≈ 0. [src: cazyme_pangenome_ecology] See [[concepts/biome-level-carbohydrate-active-enzyme-repertoire-differentiation]], [[entities/kruskal-wallis-test-with-eta-squared-effect-size]] and [[summaries/cazyme_pangenome_ecology__REPORT]].

## GT2 near T4SS loci

T4SS machinery in environmental MAGs is significantly co-localised with GT2 glycosyltransferase cassettes. [src: t4ss_cazy_environmental_hgt] GT2 is the top CAZy co-occurrence hit near T4SS loci (767 genomes, avg 5,041 bp). [src: t4ss_cazy_environmental_hgt] The report notes that threshold validation of this ≤10 kb co-occurrence screen is pending. [src: t4ss_cazy_environmental_hgt]

The GT2 neighbourhood analysis covers 376 genomes. [src: t4ss_cazy_environmental_hgt] List-format parsing finds T4SS in 503 neighbourhood entries and GT2 in 495, which the report interprets as confirming syntenic co-localisation at the contig level. [src: t4ss_cazy_environmental_hgt] GH23 (murein lytic transglycosylase) is the second most common CAZy family in these neighbourhoods, with 106 occurrences. [src: t4ss_cazy_environmental_hgt] The report suggests from this that cell wall remodelling genes cluster with GT2–T4SS syntenic loci. [src: t4ss_cazy_environmental_hgt]

The GT2 gene tree contains 77 detected horizontal gene transfer events. [src: t4ss_cazy_environmental_hgt] The report also gives 32 cross-phylum events as positive evidence from phylogenetic incongruence. [src: t4ss_cazy_environmental_hgt] See [[concepts/horizontal-transfer-of-carbohydrate-active-enzymes-via-conjugative-machinery]], [[entities/type-iv-secretion-system]] and [[summaries/t4ss_cazy_environmental_hgt__REPORT]].
