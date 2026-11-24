# Priya Ranjan

ORCID: [0000-0002-0357-1939](https://orcid.org/0000-0002-0357-1939)

## Contributions

The project [[summaries/pgp_pangenome_ecology__REPORT]] surveyed 11,272 species carrying at least one plant-growth-promoting (PGP) gene. It reports this as the first such analysis across the full KBase Data Lakehouse pangenome (27K species, 293K genomes). [src: pgp_pangenome_ecology] The report states that the canonical PGPB phenotype in agricultural inoculants centers on pqqC + acdS rather than nitrogen fixation. [src: pgp_pangenome_ecology] Its interpretations about separate guilds, vertical inheritance, root-exudate tryptophan and an hcn role in the rhizosphere niche are proposals, not direct measurements. [src: pgp_pangenome_ecology]

On co-occurrence, 8 of 10 focal gene pairs were significant after Benjamini-Hochberg false discovery rate correction. Five pairs were positive and three were negative. [src: pgp_pangenome_ecology] The strongest positive pair was pqqC × acdS (OR = 7.24, n = 286 co-occurring species, q = 1.2e-83). [src: pgp_pangenome_ecology] nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19). It showed no significant association with ipdC (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology] Only 157 species (1.4%) carry at least 3 focal traits. [src: pgp_pangenome_ecology] See [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds]].

On environmental enrichment, acdS (OR = 7.02, q = 5.1e-62), pqqC (OR = 2.90, q = 2.8e-53) and hcnC (OR = 1.85, q = 6.1e-08) were enriched in soil/rhizosphere species (1,039 species) relative to 10,233 other species. nifH was depleted (OR = 0.60, q = 5.5e-08), and ipdC did not differ significantly (raw OR = 0.79, q = 0.47). [src: pgp_pangenome_ecology] The acdS enrichment survived phylum-level fixed effects (OR = 6.98, p = 4.8e-61). It also held in a strict rhizosphere-only sensitivity analysis (OR = 10.6, q = 7.6e-38). [src: pgp_pangenome_ecology] A phylum-controlled model nonetheless found ipdC soil depletion (OR = 0.56, p = 0.027). [src: pgp_pangenome_ecology] See [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]].

On pangenome structure, all 13 PGP genes had higher core fractions than the genome-wide baseline of 46.8% (q < 0.05 for all). The mean accessory fraction was 29.7% against 53.2% genome-wide. The report rejects its horizontal gene transfer hypothesis on this basis. [src: pgp_pangenome_ecology] pqqD was an outlier at 55.5% core, with the highest singleton fraction (27.5%). [src: pgp_pangenome_ecology] Pangenome openness correlated negatively with PGP gene richness (Spearman ρ = −0.195, p = 2.0e-97, n = 11,272 species with ≥2 genomes). [src: pgp_pangenome_ecology] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]] and [[concepts/pangenome-openness-and-its-correlates]].

On tryptophan biosynthesis, species with complete tryptophan biosynthesis carried ipdC at 2.5% versus 0.9% in incomplete species (Fisher OR = 2.81, p = 6.3e-10). [src: pgp_pangenome_ecology] The tyrosine negative control predicted ipdC at a similar effect size (OR = 3.62, p = 2.3e-11), so the control failed. [src: pgp_pangenome_ecology] Within soil/rhizosphere species the association reversed (OR = 0.30, p = 0.02). In non-soil species it stayed positive (OR = 3.56, p = 7.7e-13). [src: pgp_pangenome_ecology] See [[concepts/aromatic-amino-acid-biosynthesis-and-auxin-pathway-gene-coupling]].

## Projects (1)

- [[summaries/pgp_pangenome_ecology__REPORT|pgp_pangenome_ecology]]
