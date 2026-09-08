---
type: Dataset
description: Arkin-derived NMDC dataset with environmental and multi-omics products
sources:
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: enigma_carbon_census_1
  resource: ../summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
- id: euk_in_prok_correlates
  resource: ../summaries/euk_in_prok_correlates__REPORT.md
  title: euk in prok correlates
- id: functional_dark_matter
  resource: ../summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: nmdc_community_metabolic_ecology
  resource: ../summaries/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
- id: nmdc_context_audit
  resource: ../summaries/nmdc_context_audit__REPORT.md
  title: nmdc context audit
title: NMDC ARKin
---
# NMDC ARKin

## What it is

**Canonical name:** NMDC ARKin. [^berdl_data_atlas]

**Known alias:** `nmdc_arkin`. [^berdl_data_atlas]

**Stable external identifier:** No stable external identifier is specified in the source. [^berdl_data_atlas]

NMDC ARKin is a dataset layer in the BERDL inventory providing environmental abundance, multi-omics, taxonomy, and biosample records for cross-tenant biological analyses. [^berdl_data_atlas] The NMDC Context Audit **refines** this description by identifying `kbase.nmdc_arkin` as an Arkin Lab derivative located in the `kbase` tenant, rather than a native resource in the `nmdc` tenant; the derivative adds embeddings and traits that do not exist upstream. [^nmdc_context_audit]

The audit also **refines** the provenance context: NMDC ARKin is one of 7 maintained resources represented by 20 `nmdc`-named database entries across three tenants and six provenance classes, alongside genuine NMDC resources, external re-hosts, an NMDC-derived MAG resource, and the NEON namesake collision. [^nmdc_context_audit] Consequently, the `nmdc` label alone is not a reliable dataset boundary or authority indicator. [^nmdc_context_audit]

## Key facts

The BERDL inventory contains 16,640 NMDC biosamples and 75,119,498 metatranscriptomic abundance rows. [^berdl_data_atlas] NMDC covers 11 biological topics and has a topic-distribution entropy of 2.61. [^berdl_data_atlas] Its metabolomics, proteomics, and lipidomics layers contain 3.1M, 346K, and 1.4M records, respectively, and are described as largely untapped resources. [^berdl_data_atlas]

The atlas identifies NMDC as a cross-validation resource for UC4, environmental distributions of clinically relevant pathogens and associated biogeochemistry, and UC5, ENVO ontology completeness in NMDC biosamples. [^berdl_data_atlas] The proposed UC4 bridge connects NMDC with PROTECT through 10 shared keys, while the proposed UC5 bridge connects NMDC with refdata through 9 shared keys; neither bridge had realized use at audit time. [^berdl_data_atlas] Join-key presence demonstrates schema-level compatibility but not valid value-space overlap, and UC4 and UC5 require live-cluster execution. [^berdl_data_atlas]

The Context Audit **supports** the need for explicit provenance-aware discovery: `nmdc_arkin`, `nmdc_mags`, and `nmdc_neon` are located in the `kbase` tenant even though users searching only the `nmdc` tenant would not find them. [^nmdc_context_audit] It further **refines** scale interpretation by distinguishing the genuine NMDC biosample universe of 16,640 samples from the co-hosted `nmdc.ncbi_biosamples` mirror containing 51,711,888 biosamples and 756,112,544 attribute rows. [^nmdc_context_audit] These resources should therefore be selected by provenance, authority, scale, and currency rather than by name alone. [^nmdc_context_audit]

The community metabolic-ecology integration **supports** ARKin’s multi-omics role with a 220-sample community pathway matrix linked to 27,690 GTDB species, 80 pathways, 305M GapMind pathway records, and NMDC taxonomy and metabolomics. [^nmdc_community_metabolic_ecology] Taxonomy-bridge coverage averaged 94.6%; 92% of samples mapped at least 85% of community abundance to GTDB pangenome species, and the analysis-ready merged matrix contained 174 samples. [^nmdc_community_metabolic_ecology] This study **refines** the atlas’s general multi-omics opportunity by showing that 33 Freshwater samples lacked paired metabolomics and that the H1 pathway–metabolomics test therefore had 131 samples. [^nmdc_community_metabolic_ecology]

The same analysis **supports** NMDC as a resource for testing community metabolic ecology: 11 of 13 amino-acid pathways had negative pathway-completeness/metabolite correlations, with a significant sign test (p = 0.011), while leucine (r = −0.390, q = 0.022, n = 62) and arginine (r = −0.297, q = 0.049, n = 80) remained significant after Benjamini-Hochberg false-discovery-rate correction. [^nmdc_community_metabolic_ecology] It also **supports** ecosystem-level analysis: Soil and Freshwater communities separated strongly in pathway-completeness PCA, with Soil versus Freshwater U = 3,674 and p < 0.0001, and 17 of 18 amino-acid pathways differing by ecosystem type after correction. [^nmdc_community_metabolic_ecology] These results are genomic-potential measurements rather than evidence of pathway expression, and absent pH, temperature, and total organic carbon measurements prevented abiotic partial-correlation controls. [^nmdc_community_metabolic_ecology]

The ENIGMA Carbon Census **supports** NMDC ARKin’s role as an environmental-abundance resource: its atlas used 3825 taxonomy-bearing NMDC metagenomes, detected 83 of 86 implicated utilizer genera in 1719 metagenomes, and achieved 99% sample labeling through two independent ontology systems. [^enigma_carbon_census_1] That analysis **refines** interpretation of NMDC abundance data: it measures organismal occurrence or abundance rather than compound catabolic activity because the environmental datasets did not measure the census compounds. [^enigma_carbon_census_1]

The eukaryotic-read analysis **supports** ARKin’s value for environmental metadata studies: native results from 2,759 ReadbasedAnalysis runs across 9 studies showed detectable eukaryotic reads in 77% of runs, with a median eukaryotic fraction of 2.7% and a mean of 13.3%; GOTTCHA2 was the usable estimator because the deployed Kraken2 and Centrifuge references were prokaryote-restricted. [^euk_in_prok_correlates] Environment predicted eukaryotic fraction under random validation (R²=0.35) but failed out-of-study GroupKFold validation (R²=−0.30), **refining** cross-study interpretation by indicating that collection-wide environmental associations were largely confounded with study or batch. [^euk_in_prok_correlates] Within the dominant NEON soil study, local vegetation and geography remained associated with eukaryotic fraction; a model using both achieved within-study five-fold R²=+0.17 ± 0.06, supporting batch-controlled rather than naive cross-study regression. [^euk_in_prok_correlates]

The Functional Dark Matter analysis **supports** this batch-controlled environmental interpretation: NMDC independently mapped 5 of 6 carrier genera to 47 taxon columns across 6,365 metagenomic samples and confirmed all 4 testable pre-registered abiotic predictions, including correlations with total nitrogen (ρ = +0.109, n = 1,231, FDR = 2.3e-4), ammonium nitrogen (ρ = +0.231, n = 1,230, FDR = 8.0e-16), pH (ρ = +0.157, n = 4,366, FDR = 7.4e-25), and dissolved oxygen (ρ = -0.298, n = 272, FDR = 1.5e-6). [^functional_dark_matter] It also **supports** NMDC’s value for trait validation: all 7 pre-registered trait-condition predictions reached FDR < 10⁻²¹, including nitrogen-source carriers with nitrogen fixation (ρ = 0.60) and nitrate denitrification (ρ = 0.52), and carbon-source carriers with aerobic chemoheterotrophy (ρ = 0.73) and fermentation (ρ = 0.59). [^functional_dark_matter] However, 441 of 449 exploratory tests reached FDR < 0.05, largely attributed to compositional coupling, so these associations require cautious interpretation and sample-label permutation testing. [^functional_dark_matter]

The eukaryotic-read report **refines** the proposed cross-tenant bridging role by showing that workflow results must be joined to biosamples and studies through `workflow_run_id`, with large taxonomy tables aggregated before joining; 1,067 of 2,759 runs were pooled from multiple biosamples, so biosample-level joins could create pseudo-replication. [^euk_in_prok_correlates]

NMDC ARKin contributes to [multi-omics-integration](../concepts/multi-omics-integration.md) because its metabolomics, proteomics, lipidomics, metatranscriptomic, taxonomy, and biosample layers provide potential cross-tenant multi-omics linkages. [^berdl_data_atlas] The community analysis **supports** this placement by linking community-weighted GapMind pathway completeness to metabolite intensity, while **refining** it through missing freshwater metabolomics, study imbalance, string-based metabolite matching, and the distinction between genomic potential and expression. [^nmdc_community_metabolic_ecology] The eukaryotic-read analysis **refines** this opportunity by demonstrating that classifier reference databases are not interchangeable for contamination estimation and that sequencing and environmental metadata require study- or batch-controlled comparisons. [^euk_in_prok_correlates] The Functional Dark Matter results further **support** integrating NMDC with fitness, pangenome, and environmental evidence while **refining** the interpretation: genus-level carrier correlations can validate pre-registered environmental predictions but cannot by themselves establish specific dark-gene functions. [^functional_dark_matter] The Context Audit **supports** retaining these derivative products while **refining** their interpretation: embeddings, traits, metabolomics, omics files, and MAG catalogs have different provenance and authority contexts and should be exposed with those relationships rather than treated as a single homogeneous NMDC resource. [^nmdc_context_audit]

It also contributes to [environmental-resistome](../concepts/environmental-resistome.md) through the proposed NMDC–PROTECT bridge for examining environmental distributions of clinically relevant pathogens and associated biogeochemistry. [^berdl_data_atlas]

The atlas recommends NMDC ARKin for environmental abundance and multi-omics analyses, alongside [enigma-coral](enigma-coral.md) for field samples and [protect-genomedepot](protect-genomedepot.md) for pathogen genomes. [^berdl_data_atlas]

## Source

See the full inventory and integration analysis in [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md). [^berdl_data_atlas]

See the community pathway-completeness, metabolomics, and ecosystem analysis in [nmdc_community_metabolic_ecology__REPORT](../summaries/nmdc_community_metabolic_ecology__REPORT.md). [^nmdc_community_metabolic_ecology]

See the compound-to-environment census and NMDC environmental atlas in [enigma_carbon_census_1__REPORT](../summaries/enigma_carbon_census_1__REPORT.md). [^enigma_carbon_census_1]

See the eukaryotic-contamination metadata analysis in [euk_in_prok_correlates__REPORT](../summaries/euk_in_prok_correlates__REPORT.md). [^euk_in_prok_correlates]

See the Functional Dark Matter integration of NMDC environmental validation with fitness and gene-prioritization evidence in [functional_dark_matter__REPORT](../summaries/functional_dark_matter__REPORT.md). [^functional_dark_matter]

See the NMDC resource provenance, tenant placement, scale, currency, and discovery audit in [nmdc_context_audit__REPORT](../summaries/nmdc_context_audit__REPORT.md). [^nmdc_context_audit]

[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
[^nmdc_context_audit]: [nmdc context audit](../summaries/nmdc_context_audit__REPORT.md)
[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../summaries/nmdc_community_metabolic_ecology__REPORT.md)
[^enigma_carbon_census_1]: [enigma carbon census 1](../summaries/enigma_carbon_census_1__REPORT.md)
[^euk_in_prok_correlates]: [euk in prok correlates](../summaries/euk_in_prok_correlates__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../summaries/functional_dark_matter__REPORT.md)
