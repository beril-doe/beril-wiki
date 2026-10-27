---
type: "Research direction"
description: "Is the near-total dissimilarity between depths within one well, compared with the similarity of same-zone samples across wells, caused by plume travel through the saturated zone, or by hydrogeological zone properties independent of contamination?"
hypothesis: "If plume exposure drives depth turnover, measured contaminant chemistry (nitrate, pH, metals) will still explain a significant share of community composition after hydrogeological zone is accounted for. If zone alone drives it, contaminant terms will add little."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Community data are in the lakehouse, but the geochemistry is reported as not loaded and depth-matched porewater chemistry would have to be measured."
collections: ["enigma-coral"]
findings: ["enigma_sso_asv_ecology--7ffad219", "enigma_sso_asv_ecology--9b46b768", "enigma_sso_asv_ecology--519fc7f6"]
conflicts: []
papers: ["30265315", "20305024", "22140175", "16407148"]
builds_on: ["findings/enigma_sso_asv_ecology--7ffad219", "findings/enigma_sso_asv_ecology--9b46b768", "findings/enigma_sso_asv_ecology--519fc7f6"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does depth-stratified plume exposure, not lateral flow, structure the Oak Ridge subsurface community?

Is the near-total dissimilarity between depths within one well, compared with the similarity of same-zone samples across wells, caused by plume travel through the saturated zone, or by hydrogeological zone properties independent of contamination?

## Hypothesis

If plume exposure drives depth turnover, measured contaminant chemistry (nitrate, pH, metals) will still explain a significant share of community composition after hydrogeological zone is accounted for. If zone alone drives it, contaminant terms will add little.

## Why it matters

It would separate contaminant selection from natural vertical stratification, which decides whether depth-resolved sampling is needed to monitor plume spread.

## How to test it

The report describes the 221 SSO geochemistry samples (metals, IC/TOC, isotopes, NH3/NO2) as registered but not loaded into CORAL. First load them and link them to the SSO ASV samples. Then fit a db-RDA (distance-based redundancy analysis) or PERMANOVA with zone (VZ/VSZ/SZ1/SZ2) and contaminant terms, with well as a blocking factor. Test whether the within-well depth contrast (median BC 0.977) shrinks relative to the same-zone cross-well contrast (0.835) after conditioning on chemistry. The zone-variance estimate (27.5%) carries an unresolved denominator inconsistency (37 samples stated, zone counts 33, 25, 54 and 45), so refit it on a clarified sample set. Follow with depth-resolved porewater sampling at the wells to measure chemistry directly.

## What would support or refute it

Support: contaminant terms retain significant variance within zones and track the depth contrast. Refutation: zone explains composition and chemistry adds nothing, or chemistry does not vary with depth.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Community data are in the lakehouse, but the geochemistry is reported as not loaded and depth-matched porewater chemistry would have to be measured.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--7ffad219|Depth, not horizontal position, appears to determine plume exposure]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--9b46b768|Hydrogeological zone explains over a quarter of sediment community variance]] (Extends retrieved work)
- Finding: [[findings/enigma_sso_asv_ecology--519fc7f6|Community turnover does not follow the hillslope]] (Candidate novel)

## Closest published work

- [PMID 30265315](https://pubmed.ncbi.nlm.nih.gov/30265315/) Impact of hydrologic boundaries on microbial planktonic and biofilm communities in shallow terrestrial subsurface environments.
- [PMID 20305024](https://pubmed.ncbi.nlm.nih.gov/20305024/) Denitrifying bacteria isolated from terrestrial subsurface sediments exposed to mixed-waste contamination.
- [PMID 22140175](https://pubmed.ncbi.nlm.nih.gov/22140175/) Rhodanobacter denitrificans sp. nov., isolated from nitrate-rich zones of a contaminated aquifer.
- [PMID 16407148](https://pubmed.ncbi.nlm.nih.gov/16407148/) The diversity and biogeography of soil bacterial communities.

PMID 30265315 reviews hydrologic boundaries shaping subsurface communities, and PMIDs 20305024 and 22140175 describe Oak Ridge taxa, but none separates plume exposure from zone structure using depth-versus-lateral contrasts.
