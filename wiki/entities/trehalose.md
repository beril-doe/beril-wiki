---
type: "Compound"
description: "Disaccharide produced by FW300-N2E3 with strain-variable catabolism and a proposed osmoprotectant role."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Trehalose

Trehalose is a disaccharide that Pseudomonas strain FW300-N2E3 produces. In the fw300_metabolic_consistency report, catabolism looks strain-variable across *P. fluorescens* isolates, and the report proposes an osmoprotectant role. The evidence is one strain's Web of Microbes (WoM) data plus BacDive species consensus (n=6), and the report rates it Moderate confidence. [src: fw300_metabolic_consistency]

## Key facts

- In FW300-N2E3 WoM data, trehalose was Increased. BacDive counts were 1+/5-, rated Moderate confidence (n=6). The report read this as strain-variable and likely osmoprotectant, not catabolic. [src: fw300_metabolic_consistency]
- BacDive trehalose utilization was strain-variable (1/6 positive). The report takes this to suggest that trehalose metabolism varies across *P. fluorescens* isolates. [src: fw300_metabolic_consistency] See [[entities/pseudomonas-fluorescens]].
- In the webofmicrobes_explorer report, WoM trehalose with action I is linked to the Fitness Browser condition D-Trehalose dihydrate as carbon source. [src: webofmicrobes_explorer] This is an example of [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]].

## Proposed osmoprotectant role

The report interprets FW300-N2E3 trehalose production (WoM: Increased) together with low species-level catabolism (1/6 BacDive strains positive, per-strain consensus). It says this likely reflects trehalose's well-documented role as an osmoprotectant in Pseudomonads. [src: fw300_metabolic_consistency] This is an interpretation, not a direct test. The report cites two supporting studies:

- Wang et al. (2020) showed that *Pseudomonas protegens*, closely related to *P. fluorescens*, upregulates trehalose synthesis under osmotic stress. [src: fw300_metabolic_consistency]
- Harty et al. (2019) demonstrated ethanol-stimulated trehalose production in *Pseudomonas aeruginosa*. [src: fw300_metabolic_consistency]

The report also hypothesizes that trehalose secretion during growth on R2A medium in WoM may reflect a constitutive stress-protection strategy rather than metabolic overflow. [src: fw300_metabolic_consistency] See [[entities/r2a-medium]].

## Caveats

Species consensus may not reflect FW300-N2E3's own capabilities. Trehalose utilization at 1/6 positive illustrates this strain-level variation, even after per-strain consensus deduplication (majority vote among duplicate records per strain). [src: fw300_metabolic_consistency] See [[concepts/reliability-of-species-level-bacdive-consensus-phenotypes]] and [[concepts/metabolite-production-versus-utilization-discordance]].

Sources: [[summaries/fw300_metabolic_consistency__REPORT]], [[summaries/webofmicrobes_explorer__REPORT]].
