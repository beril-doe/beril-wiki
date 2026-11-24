---
type: "Concept"
description: "How the small organism count, single-laboratory origin, uneven medium coverage and frozen snapshot limit statistical inference from exometabolomics databases."
sources: ["summaries/discoveries.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pitfalls.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Taxonomic and single-laboratory coverage limits of exometabolomic data

The Web of Microbes (WoM) exometabolomics database is small, comes from one laboratory and is frozen at 2018. [src: pitfalls, webofmicrobes_explorer] These features limit what statistics it can support. [src: webofmicrobes_explorer] The evidence is direct description of the dataset in several reports, plus one failed machine-learning test. [src: genotype_to_phenotype_enigma] [[entities/web-of-microbes]] is the entity page.

## Size and origin

The 2018 WoM snapshot contains 37 organisms across 5 ENIGMA-funded projects. [src: webofmicrobes_explorer] The report calls the data small and from a single laboratory. [src: webofmicrobes_explorer] It judges 37 organisms (20 experimental) too few for statistical analyses across organism groups. [src: webofmicrobes_explorer] The genotype_to_phenotype_enigma analysis uses a still smaller subset, 6 strains and 630 metabolite observations, with 105 compounds per strain. [src: genotype_to_phenotype_enigma]

## Uneven coverage of organisms and media

Observations are concentrated in a few blocks. The largest is 6 biocrust isolates with 5,604 observations in BG11 media. [src: webofmicrobes_explorer] Ten ENIGMA groundwater isolates contribute 1,050 observations in R2A medium. [src: webofmicrobes_explorer] The remainder is thin:
- 4 other isolates (E. coli, Zymomonas, Synechococcus, Microcoleus). [src: webofmicrobes_explorer]
- 10 triculture time-series entries and 2 native microbiome entries. [src: webofmicrobes_explorer]
- 4 theoretical auxotroph predictions and 1 control. [src: webofmicrobes_explorer]

Escherichia coli BW25113 has only 12 observations, in ZMMG medium and focused on sulfur metabolism. [src: webofmicrobes_explorer] The report notes this is minimal even though Keio is among the richest Fitness Browser (FB) organisms. [src: webofmicrobes_explorer]

The fw300_metabolic_consistency report proposes comparing WoM profiles across growth media to find which metabolites are constitutively produced and which depend on the medium. [src: fw300_metabolic_consistency]

## Metabolite identity and direction

Of 589 tracked metabolites, 332 (56.4%) are unidentified and carry the Unk_ prefix. [src: webofmicrobes_explorer] The pitfalls digest gives ~56% and advises filtering these out of named-metabolite analyses. [src: pitfalls] One sentence of the report says that, of 257 identified metabolites, 408 (69.3% of all 589) show at least one change. [src: webofmicrobes_explorer] That sentence mixes two denominators, so read it with care.

The 2018 snapshot has no "Decreased" (consumption) action for any organism. All 742 D observations belong to the control, so the database records production but not consumption. [src: discoveries]

## Frozen snapshot

The dataset is a 2018 frozen snapshot, and newer data live in GNPS2. [src: pitfalls] The Wayback Machine archive may not reflect current WoM. The report expects the GNPS2-hosted version or Northen lab internal datasets to be substantially richer. [src: webofmicrobes_explorer]

## Consequence for modelling

With 6 strains and 105 metabolites, multivariate GBDT (gradient boosted decision tree) prediction fails, with AUC (area under curve) = 0.500 at n=6. [src: genotype_to_phenotype_enigma] Univariate per-metabolite point-biserial correlation between KO (KEGG ortholog) presence and production still identifies 940 strong associations (|r| > 0.7) across all 62 variable metabolites. [src: genotype_to_phenotype_enigma]

## Open Directions

- Re-run the strain-level tests on the GNPS2 version or Northen lab datasets to see whether multivariate models work once n grows beyond 6.
- Hold medium fixed and compare organisms, or hold organism fixed and compare media, to separate medium from taxon effects.
- Repeat the association analysis with Unk_ metabolites excluded.
- Add consumption data to test how much the production-only record limits conclusions.
- Expand E. coli BW25113 coverage beyond the 12 sulfur-focused observations so it can be matched to Fitness Browser data.
