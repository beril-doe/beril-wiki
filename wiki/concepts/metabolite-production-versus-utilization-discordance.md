---
type: "Concept"
description: "Whether metabolites an organism releases (exometabolomics) are also ones it or its species can catabolize, including overflow and cross-feeding interpretations; stops at community-level modelling."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Metabolite production versus utilization discordance

This page covers whether metabolites an organism releases, as seen by exometabolomics, are also ones it or its species can catabolize. The evidence is one organism, Pseudomonas FW300-N2E3, where tryptophan is the single high-confidence discordance. [src: fw300_metabolic_consistency] The cross-feeding reading is an interpretation, not a tested result. [src: fw300_metabolic_consistency] See [[entities/pseudomonas-fluorescens-fw300-n2e3]] and [[entities/web-of-microbes]].

## Literature Context

The candidate literature for this page is thin. It contains one paper, and it is not about exometabolomics or Pseudomonas. [PMID 42801896](https://pubmed.ncbi.nlm.nih.gov/42801896/) studies a two-species Escherichia coli and Staphylococcus aureus model exposed to sublethal silver nanoparticles (AgNPs). Repeated exposure to 0.5 mg/L AgNPs for 9 days increased the S. aureus/E. coli ratio threefold. Untreated co-cultures were dominated by E. coli. During competition with S. aureus, E. coli activated ethanolamine utilization in Eut bacterial microcompartments. This led to extracellular accumulation of acetate and ammonium. Physiological assays identified nitrogen, rather than carbon, as the principal growth-promoting currency of this cross-feeding interaction. Deleting eutBC in AgNP-exposed co-cultures abolished the coexistence phenotype. Mass-matched Ag⁺ exposure did not induce ethanolamine utilization or more balanced coexistence. The authors frame these results as specific to this two-species model, and the abstract does not report a larger community.

This paper bears on the hub's central interpretive step, which is that a released metabolite can act as a cross-feeding currency. It does not test the hub's question of whether an organism's released metabolites are ones its own species can catabolize. It does give a worked example in which a metabolic byproduct of one organism supports a neighbour. It also shows that the useful currency can differ from the obvious one. Here nitrogen mattered more than carbon.

The hub's claims sit as follows. The tryptophan overflow reading for Pseudomonas FW300-N2E3 is consistent in kind with this paper, because both treat released metabolites as ecologically meaningful rather than as waste. The hub's data are different in nature. They are one organism, a single high-confidence discordance (tryptophan, 0 of 50 P. fluorescens strains positive in BacDive), and no tested transfer to a partner. The AgNP study did test transfer, using a deletion and growth assays. The hub's cross-feeding reading therefore remains an untested hypothesis. The AgNP paper does not strengthen the tryptophan inference, because it concerns different metabolites, different organisms and an induced stress condition.

The paper makes two modest points for the hub's proposed community model. First, a test of tryptophan cross-feeding could compare which element, carbon or nitrogen, is the transferred currency, since tryptophan carries both. Second, the paper's eutBC deletion in the releasing E. coli suggests a genetic control that removes the release pathway and checks whether the interaction outcome disappears. The hub's trehalose reading, an osmoprotectant released constitutively, has no counterpart in this paper. The paper also does not address production versus utilization at the species level, so that question is novel to the corpus relative to these candidates.

Overall, the corpus extends no established result here. The AgNP study offers only an analogy and a design suggestion.

## Production and utilization test different capabilities

The report treats production (exometabolomics) and utilization (BacDive growth assays) as fundamentally different capabilities. [src: fw300_metabolic_consistency] A bacterium can release a metabolite by overflow metabolism, biosynthetic byproduct release, or active secretion for ecological purposes without being able to catabolize it for energy. [src: fw300_metabolic_consistency]

## The tryptophan case

Tryptophan is the most robust discordance in the FW300-N2E3 dataset. The organism produces it and grows on it as a sole carbon source, but the species as a whole cannot catabolize it. [src: fw300_metabolic_consistency]

- FW300-N2E3 increases tryptophan in its Web of Microbes (WoM) exometabolome (action = I). [src: fw300_metabolic_consistency]
- It has 231 genes with significant fitness when grown on tryptophan in the Fitness Browser (FB). [src: fw300_metabolic_consistency]
- GapMind predicts a complete tryptophan biosynthesis pathway. [src: fw300_metabolic_consistency]
- In BacDive, 0 of 50 Pseudomonas fluorescens strains use tryptophan as a carbon source (high confidence, n=50, pct_positive=0.0, per-strain consensus). [src: fw300_metabolic_consistency]

The report calls this a tryptophan overflow hypothesis, supported by four independent databases. [src: fw300_metabolic_consistency] The pattern is consistent with overflow serving a cross-feeding or signaling function rather than a catabolic one. [src: fw300_metabolic_consistency] The report reads tryptophan secretion by a prototroph that cannot re-assimilate it as a hallmark of cross-feeding potential for auxotrophic community members. [src: fw300_metabolic_consistency] It also suggests that the 231 fitness genes reflect complex regulatory and transport machinery rather than simple catabolism. [src: fw300_metabolic_consistency] The report cites literature as consistent with this reading:

- Ramoneda et al. (2023) found tryptophan auxotrophy particularly common across thousands of genomes. [src: fw300_metabolic_consistency]
- Yousif et al. (2025) found common obligate cross-feeding in soil communities, with amino acids as key currency. [src: fw300_metabolic_consistency]
- Fritts et al. (2021) reviewed extracellular metabolism as a driver of cross-feeding. [src: fw300_metabolic_consistency]
- Sibanyoni et al. (2025) documented amino acid cross-feeding between Priestia megaterium and P. fluorescens in the rhizosphere. [src: fw300_metabolic_consistency]

## Reliability varies across metabolites

Four metabolites showed WoM production but BacDive non-utilization, and their reliability differed dramatically. [src: fw300_metabolic_consistency] Only tryptophan reaches high confidence for a genuine discordance. [src: fw300_metabolic_consistency] Tryptophan had BacDive counts 0+/50- (high confidence, n=50) and was read as a robust overflow or cross-feeding signal. [src: fw300_metabolic_consistency] Trehalose was Increased with BacDive counts 1+/5- (moderate confidence, n=6) and was read as strain-variable and likely an osmoprotectant. [src: fw300_metabolic_consistency] The report reads trehalose production with 1/6 BacDive strains positive as likely reflecting its osmoprotectant role in Pseudomonads. [src: fw300_metabolic_consistency] It cites Wang et al. (2020) on upregulated trehalose synthesis under osmotic stress in Pseudomonas protegens [src: fw300_metabolic_consistency] and Harty et al. (2019) on ethanol-stimulated trehalose production in Pseudomonas aeruginosa. [src: fw300_metabolic_consistency] The report hypothesizes that trehalose secretion on R2A medium may be constitutive stress protection rather than overflow. [src: fw300_metabolic_consistency]

## Limits of the data and proposed tests

The 2018 WoM snapshot has no consumption ("Decreased") action for any organism. All 742 D observations belong to the control. [src: webofmicrobes_explorer] It records production but not consumption, so it cannot test whether consumed metabolites predict gene essentiality. [src: webofmicrobes_explorer]

The report proposes four follow-ups. It would map FW300-N2E3 tryptophan fitness genes to GapMind pathway steps to tell biosynthetic, catabolic and regulatory roles apart, which would separate overflow from active catabolism. [src: fw300_metabolic_consistency] It would repeat the analysis in other ENIGMA isolates, such as Pseudomonas stutzeri RCH2, to test whether the pattern is species-specific. [src: fw300_metabolic_consistency] It would compare WoM profiles across growth media to find constitutive versus medium-dependent metabolites. [src: fw300_metabolic_consistency] It would use the tryptophan finding to parameterize a community model of cross-feeding with tryptophan auxotrophs in Oak Ridge groundwater. [src: fw300_metabolic_consistency]

## Open Directions

- Classify the 231 tryptophan fitness genes by GapMind pathway step, to separate overflow from active catabolism.
- Repeat the WoM and FB comparison in Pseudomonas stutzeri RCH2 and other ENIGMA isolates, to test whether the pattern is general.
- Compare WoM profiles of FW300-N2E3 across media, to test whether trehalose release is constitutive.
- Parameterize a community model of tryptophan cross-feeding with known auxotrophs, to test the cross-feeding interpretation.
