---
type: "Compound"
description: "Amino acid linked to community biosynthesis and accessory pathway variation"
sources: ["summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Leucine

## What this entity is

**Canonical name:** Leucine. [src: nmdc_community_metabolic_ecology]

**Known aliases:** No aliases were reported in the source document. [src: nmdc_community_metabolic_ecology]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: nmdc_community_metabolic_ecology]

Leucine is an amino acid whose community biosynthetic pathway completeness was compared with ambient metabolite intensity using integrated NMDC community data and GTDB pangenome pathway records. [src: nmdc_community_metabolic_ecology]

## Evidence from community metabolomics and pangenomes

Community leucine-biosynthesis completeness was negatively correlated with ambient leucine metabolite intensity, with Spearman r = −0.390, q = 0.022, and n = 62. [src: nmdc_community_metabolic_ecology] The leucine result was one of two amino-acid pathway associations that remained significant after Benjamini-Hochberg false-discovery-rate correction at q < 0.05; the other was arginine biosynthesis. [src: nmdc_community_metabolic_ecology]

The finding supports a weak but consistent community-scale Black Queen Hypothesis signal, in which greater community biosynthetic completeness is associated with lower ambient metabolite intensity, although the study did not establish that leucine biosynthesis was actively expressed. [src: nmdc_community_metabolic_ecology] Leucine was reported to require 37 ATP equivalents for biosynthesis, which the report offered as a possible energetic explanation for the negative association. [src: nmdc_community_metabolic_ecology]

The leucine correlation strengthened from r = −0.326 to r = −0.390, and its q value changed from 0.045 to 0.022, after correction of an isoleucine/leucine compound-mapping collision. [src: nmdc_community_metabolic_ecology] All 62 leucine samples came from one NMDC study, which contributed 125 of 131 samples in the pathway–metabolomics dataset. [src: nmdc_community_metabolic_ecology] The report states that the leucine result was therefore not subject to cross-study LC-MS protocol heterogeneity within those 62 samples, although replication across additional studies remains necessary. [src: nmdc_community_metabolic_ecology]

A separate species-scale analysis found all-gene leucine-biosynthesis completeness of 0.614 versus core-only completeness of 0.468, an exact gap of 0.146. [src: pathway_capability_dependency] This **refines** the community-scale result by showing that leucine pathway potential can depend partly on genes outside the universally conserved core, consistent with accessory-dependent metabolic capacity. [src: pathway_capability_dependency] The distribution is consistent with Black Queen dynamics and a potential basis for community sharing of leucine biosynthetic capacity, but it does not itself demonstrate metabolite exchange. [src: pathway_capability_dependency]

## Interpretation and limitations

The analysis used GapMind pathway completeness as genomic potential rather than as evidence that leucine biosynthesis was active in the sampled communities. [src: nmdc_community_metabolic_ecology] The accessory-dependent completeness result **supports** retaining this distinction: genomic pathway completeness does not by itself establish expression, dependency, or metabolite exchange. [src: pathway_capability_dependency]

Abiotic measurements for pH, temperature, and total organic carbon were unavailable because all were NaN in the 174-sample analysis matrix, so partial correlations controlling for environmental gradients could not be performed. [src: nmdc_community_metabolic_ecology] The leucine association therefore remains compatible with confounding by unmeasured abiotic conditions, community composition, or metabolomics variation. [src: nmdc_community_metabolic_ecology]

Metatranscriptomic data paired with metabolomics would be needed to test whether expressed leucine-biosynthesis completeness correlates more strongly with ambient leucine pools. [src: nmdc_community_metabolic_ecology]

## Related pages

This entity connects to [[concepts/multi-omics-integration]], which covers the integration of community taxonomy, pangenome pathway potential, and metabolomics used in the study. [src: nmdc_community_metabolic_ecology]

It also connects to [[concepts/metabolic-model-gapfilling]], because the study extended GapMind pathway-completeness analysis from species-level annotation to community-weighted metabolic potential. [src: nmdc_community_metabolic_ecology] The species-scale completeness comparison is summarized in [[summaries/pathway_capability_dependency__REPORT]]. [src: pathway_capability_dependency]

The negative association is relevant to [[concepts/condition-specific-fitness]] as an environmental-metabolism comparison involving pathway completeness and metabolite availability. [src: nmdc_community_metabolic_ecology]

See the source summary at [[summaries/nmdc_community_metabolic_ecology__REPORT]]. [src: nmdc_community_metabolic_ecology]
