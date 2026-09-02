---
type: "Concept"
description: "Groundwater and sediment host distinct, habitat-associated microbial communities"
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Groundwater–Sediment Community Partitioning

Groundwater and sediment at the same subsurface wells contained distinct microbial communities, indicating that the groundwater assemblage cannot be treated as a simple sample of attached sediment microbiota. [src: enigma_sso_asv_ecology] This finding connects to [[concepts/collection-site-versus-microenvironment-mismatch]] and [[concepts/subsurface-compartment-specific-metabolism]], because physical sampling habitat may structure both observed community composition and inferred metabolism. [src: enigma_sso_asv_ecology]

## Core Evidence

Groundwater and sediment communities collected at the same wells had a median Bray–Curtis dissimilarity of 0.424, where Bray–Curtis dissimilarity measures compositional difference between communities. [src: enigma_sso_asv_ecology] Within-well dissimilarities ranged from 0.364–0.450 across 5 wells. [src: enigma_sso_asv_ecology] This direct paired comparison supports habitat partitioning rather than an interpretation based only on differences among geographically separated wells. [src: enigma_sso_asv_ecology]

Groundwater was enriched in several taxa associated in the report with plume or oxidative processes, including *Rhodanobacter* at 3.62% versus 1.23% in sediment, a reported 2.9× enrichment; *Gallionella* at 0.14% versus 0.01%, a reported 8.9× enrichment; and *Sideroxydans* at 0.06% versus 0.01%, a reported 7.0× enrichment. [src: enigma_sso_asv_ecology] Sediment was enriched in *Anaeromyxobacter* at 1.24% versus 0.03% in groundwater, with groundwater reported as 0.02× the sediment value; *Arcobacter* at 0.54% versus 0.00%; and *Ca. Methanoperedens* at 0.42% versus 0.00%. [src: enigma_sso_asv_ecology] *Geobacter* was 0.00% in sediment and 0.01% in groundwater, reported as 5.5× enriched in groundwater. [src: enigma_sso_asv_ecology]

The taxonomic contrast is consistent with groundwater enrichment in denitrifiers and iron oxidizers and sediment enrichment in anaerobic taxa. [src: enigma_sso_asv_ecology] The report therefore interprets groundwater and sediment as distinct attached and planktonic habitats rather than as interchangeable compartments. [src: enigma_sso_asv_ecology] Because these functional assignments were inferred from taxonomy, the habitat-associated metabolic interpretation is a hypothesis requiring direct genomic and geochemical validation. [src: enigma_sso_asv_ecology]

## Limits on Interpretation

The comparison is confounded by an 18-month sampling offset: sediment cores were collected once per well during February–March 2023, whereas groundwater was sampled in September 2024. [src: enigma_sso_asv_ecology] Seasonal change or plume dynamics could therefore contribute to the observed groundwater–sediment difference, and the available data do not isolate habitat effects from this temporal mismatch. [src: enigma_sso_asv_ecology] Sediment also lacked within-well temporal replication, so sediment community stability could not be assessed. [src: enigma_sso_asv_ecology]

Groundwater ASV coverage was available for only 5 of 9 wells—L7, L9, M4, M6, and U2—and excluded the inferred hotspot wells M5 and U3. [src: enigma_sso_asv_ecology] Consequently, the observed taxonomic contrast does not establish whether the same partitioning pattern applies across the complete SSO well grid or at the proposed plume hotspots. [src: enigma_sso_asv_ecology]

## Relation to Spatial and Functional Inference

The groundwater–sediment contrast refines the broader SSO spatial model by showing that community composition varies not only across wells and hydrogeological zones but also between sample habitats within wells. [src: enigma_sso_asv_ecology] In the sediment dataset, hydrogeological zone explained 27.5% of community variance (F = 4.05, p = 0.0001), while well identity explained 19.2% and was not significant (F = 0.80, p = 0.979). [src: enigma_sso_asv_ecology] These results support interpreting subsurface microbial geography through both hydrogeological compartment and habitat type, rather than assigning a single community profile to each well. [src: enigma_sso_asv_ecology]

The inferred groundwater enrichment of denitrifiers and iron oxidizers, together with sediment enrichment of anaerobic taxa, suggests that habitat-specific sampling may alter reconstructed redox or metabolic patterns. [src: enigma_sso_asv_ecology] This is an extrapolated interpretation because genus-level functional inference covered 65 of 1,038 genera and 21% of total reads, while 56% of reads remained outside the genus-level inference. [src: enigma_sso_asv_ecology] Class-level functional inference covered 78% of reads, but its trait scores were consensus estimates rather than empirical measurements of the specific SSO populations. [src: enigma_sso_asv_ecology] Direct metagenomics and matched geochemistry are therefore needed to test whether the taxonomic partition corresponds to distinct realized metabolic activity. [src: enigma_sso_asv_ecology]

## Tensions

The paired community comparison supports groundwater–sediment partitioning, but the 18-month sampling offset prevents a clean attribution of the difference to habitat alone. [src: enigma_sso_asv_ecology] The proposed plume-associated explanation further remains unconfirmed because direct SSO geochemistry was unavailable: 221 geochemistry sample tubes were registered in CORAL, but metals, ion chromatography/total organic carbon, isotopes, ammonia, and nitrite measurements had not been loaded. [src: enigma_sso_asv_ecology] Thus, habitat separation is directly supported by the paired ASV dissimilarities, whereas the specific geochemical mechanism remains a testable hypothesis. [src: enigma_sso_asv_ecology]

## Open Directions

- Collect groundwater and sediment contemporaneously at the same wells and repeat paired Bray–Curtis comparisons to separate habitat partitioning from the 18-month sampling offset. [src: enigma_sso_asv_ecology]
- Load the 221 registered SSO geochemistry samples into CORAL and test whether nitrate, pH, and metal concentrations explain the groundwater–sediment taxonomic contrast. [src: enigma_sso_asv_ecology]
- Extract pump-test ASVs from Brick 460-462 for L8, M5, and U2 and test whether the predicted *Rhodanobacter* maximum occurs at M5. [src: enigma_sso_asv_ecology]
- Perform same-resolution metagenomic profiling of groundwater and sediment to test whether habitat-enriched taxa carry the inferred denitrification, iron-oxidation, iron-reduction, sulfur-oxidation, and methanotrophy functions. [src: enigma_sso_asv_ecology]
- Repeat groundwater and sediment sampling across seasons to determine whether the observed partitioning persists during plume and environmental change. [src: enigma_sso_asv_ecology]

Related source: [[summaries/enigma_sso_asv_ecology__REPORT]]
