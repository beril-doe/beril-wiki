---
type: "Concept"
description: "Covers differences between sediment-attached and groundwater or filter-fraction communities and caveats about sampling offsets; stops at genome-level mechanisms."
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Attached versus planktonic communities in groundwater and sediment

Sediment-attached and groundwater communities at SSO wells differ substantially in 16S amplicon data, with a median BC (Bray-Curtis dissimilarity) of 0.424 within wells. [src: enigma_sso_asv_ecology] The evidence comes from one report, [[summaries/enigma_sso_asv_ecology__REPORT]], and an 18-month sampling offset confounds the comparison. [src: enigma_sso_asv_ecology] The functional interpretations (plume transport, biofilm lifestyle) are the report's explanations, not direct tests.

## Literature Context

The candidate papers agree that free-living and attached subsurface communities usually differ, though each comes with limits. A review of shallow terrestrial subsurface habitats says that significant differences in composition, structure and activity between planktonic and biofilm communities are commonly accepted. It also says sampling constraints and the difficulty of working with solid substrata leave the contribution of each phase largely unresolved [PMID 30265315](https://pubmed.ncbi.nlm.nih.gov/30265315/). In sand-packed columns perfused with groundwater, free-living populations showed a greater diversity of phylotypes than solid-phase populations. The attached community had higher enzyme activities per volume of porous medium. Per cell, attached bacteria had higher aminopeptidase activity and free-living bacteria had higher beta-glucosidase activity. This was a laboratory column study, not a field aquifer [PMID 11916670](https://pubmed.ncbi.nlm.nih.gov/11916670/).

Field and genomic work points the same way. In a pristine porous aquifer, in situ microcosms of sterile sediment were exposed to groundwater for almost 1 year. Null-model analysis of 16S amplicon data indicated selection of specific OTUs rather than random colonization. A small fraction of early-colonizing persistent OTUs dominated the final communities (68%-85%). The authors conclude that planktonic versus sediment-attached differences are not purely stochastic [PMID 30378251](https://pubmed.ncbi.nlm.nih.gov/30378251/). In a multi-omics study of groundwater, sediment-associated ultra-small Patescibacteria and DPANN archaea differed from their planktonic counterparts in species composition and transcriptional activity. They also showed metabolic adaptations that reflect a surface-associated lifestyle [PMID 36808147](https://pubmed.ncbi.nlm.nih.gov/36808147/). That study also found that water oxygen content largely shaped community composition and activity.

The corpus finding of distinct sediment and groundwater assemblages at SSO wells is consistent with this literature. The median within-well Bray-Curtis dissimilarity was 0.424, and the range across 5 paired wells was 0.364–0.450. The filter-size effect within groundwater (R² = 10.1%, p = 0.001) also fits the general expectation of separate free-living and particle-associated communities [PMID 30265315](https://pubmed.ncbi.nlm.nih.gov/30265315/). The corpus's reading of Anaeromyxobacter as a biofilm-forming, surface-attached organism, with 41× sediment enrichment of Anaeromyxobacter dehalogenans, is compatible with the idea that sediment surfaces select for particular taxa [PMID 30378251](https://pubmed.ncbi.nlm.nih.gov/30378251/). The same selection idea supports the report's rejection of simple detachment as the explanation for the depletion of Anaeromyxobacter, Arcobacter and Ca. Methanoperedens in groundwater. The corpus does not test this directly.

The corpus extends this literature in a few ways. It gives taxon-level percentages for a contaminated Oak Ridge system: for example, Rhodanobacter at 1.23% in sediment and 3.62% in groundwater. None of the candidate papers addresses plume-adapted denitrifiers or iron oxidizers, so the plume-transport interpretation is novel and untested in this evidence. The candidates also cannot resolve the 18-month sampling offset, with sediment taken in Feb-Mar 2023 and groundwater in Sep 2024. That offset confounds material type with time. The review's emphasis on temporal and spatial sampling challenges reinforces the caveat [PMID 30265315](https://pubmed.ncbi.nlm.nih.gov/30265315/). Nothing in the candidates contradicts the corpus.

## Community differences between materials

Across 5 wells with both materials, within-well BC was 0.364–0.450. [src: enigma_sso_asv_ecology] The report presents this as complementary amplicon-level evidence for distinct sediment and groundwater assemblages, alongside 2025 work that generated 77 sediment and 33 groundwater metagenomes from the ORR to examine attached versus planktonic communities. [src: enigma_sso_asv_ecology]

Within groundwater, filter size explained R² = 10.1% (p = 0.001) of variation, which the report reads as distinct free-living and particle-associated communities. [src: enigma_sso_asv_ecology] See [[entities/permanova]] and [[concepts/temporal-stability-of-groundwater-communities]] for related analyses.

## Taxa enriched in groundwater or sediment

Groundwater was enriched in denitrifier and iron-oxidizer genera, while sediment held more of the iron/U-reducing, sulfur-oxidizing and methane-oxidizing taxa. [src: enigma_sso_asv_ecology] Values are percent of community.

| Taxon | Association | Sediment % | Groundwater % | Groundwater enrichment |
|---|---|---|---|---|
| Rhodanobacter | Denitrification | 1.23 | 3.62 | 2.9× [src: enigma_sso_asv_ecology] |
| Gallionella | Iron oxidation | 0.01 | 0.14 | 8.9× [src: enigma_sso_asv_ecology] |
| Sideroxydans | Iron oxidation | 0.01 | 0.06 | 7.0× [src: enigma_sso_asv_ecology] |
| Geobacter | Iron reduction | 0.00 | 0.01 | 5.5× [src: enigma_sso_asv_ecology] |
| Anaeromyxobacter | Iron/U reduction | 1.24 | 0.03 | 0.02× [src: enigma_sso_asv_ecology] |
| Arcobacter | Sulfur oxidation | 0.54 | 0.00 | 0× [src: enigma_sso_asv_ecology] |
| Ca. Methanoperedens | Methane oxidation | 0.42 | 0.00 | 0× [src: enigma_sso_asv_ecology] |

Gallionella, Sideroxydans and Geobacter are near zero in sediment, so their large ratios rest on very small percentages. [src: enigma_sso_asv_ecology] See [[entities/rhodanobacter]] and [[entities/sideroxydans]].

## Report's interpretation

The report interprets groundwater enrichment of Rhodanobacter, Gallionella and Sideroxydans as organisms that thrive in flowing, metal-rich contaminated plume water. [src: enigma_sso_asv_ecology] Its plume model says flowing water carries plume-adapted denitrifiers and iron oxidizers, while sediment-attached anaerobes remain in biofilms. [src: enigma_sso_asv_ecology] It reads the depletion of Anaeromyxobacter, Arcobacter and Ca. Methanoperedens in groundwater as distinct attached and planktonic communities rather than simple detachment. [src: enigma_sso_asv_ecology] It calls the 41× sediment enrichment of Anaeromyxobacter dehalogenans consistent with a biofilm-forming, surface-attached lifestyle. [src: enigma_sso_asv_ecology] Plume control of structure is discussed in [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].

## Caveats on sampling offset

Sediment cores (Feb-Mar 2023) and groundwater (Sep 2024) were collected 18 months apart, so seasonal or plume dynamics could confound the comparison. [src: enigma_sso_asv_ecology] The offset confounds material type with time, and cross-material temporal comparisons should be read with that caveat. [src: enigma_sso_asv_ecology]

## Open Directions

- Pair sediment and groundwater samples collected at the same time from the same wells. This would remove the 18-month confound in the BC comparison.
- Test the plume-transport explanation by relating per-well enrichment ratios of Rhodanobacter, Gallionella and Sideroxydans to plume geochemistry.
- Compare the 16S patterns with the 77 sediment and 33 groundwater ORR metagenomes to check that the attached-versus-planktonic pattern holds.
- Expand beyond 5 paired wells to test whether the 0.364–0.450 BC range holds.
