---
type: "Research direction"
description: "Why does community turnover show no uphill-downhill structure (Mantel rho = -0.049, p = 0.580) while hydrogeological zone explains 27.5% of sediment community variance and sediment and groundwater host distinct taxa?"
hypothesis: "Community similarity is controlled by vertical position relative to the water table and by hydrologic connectivity, so an independently measured flow-path distance will correlate with composition better than Euclidean hillslope coordinates."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "ASV sequences are in CORAL, but flow-path distances need hydrological data not shown to exist in the supplied evidence."
collections: ["enigma-coral"]
findings: ["enigma_sso_asv_ecology--519fc7f6", "enigma_sso_asv_ecology--9b46b768", "enigma_sso_asv_ecology--51556105"]
conflicts: []
papers: ["16407148", "30265315", "38755262"]
builds_on: ["findings/enigma_sso_asv_ecology--519fc7f6", "findings/enigma_sso_asv_ecology--9b46b768", "findings/enigma_sso_asv_ecology--51556105"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Is hillslope position uninformative because subsurface communities follow flow paths and depth, not geography?

Why does community turnover show no uphill-downhill structure (Mantel rho = -0.049, p = 0.580) while hydrogeological zone explains 27.5% of sediment community variance and sediment and groundwater host distinct taxa?

## Hypothesis

Community similarity is controlled by vertical position relative to the water table and by hydrologic connectivity, so an independently measured flow-path distance will correlate with composition better than Euclidean hillslope coordinates.

## Why it matters

It would show whether horizontal geography is the wrong organizing axis for subsurface sites and hydrologic connectivity the right one, changing how wells are chosen.

## How to test it

Obtain independent hydrological evidence of connectivity (hydraulic heads, tracer or pump-test responses between wells); metal concentrations in wells 90-120 m northeast of the SSO do not establish flow paths. Compute Mantel and partial Mantel tests of Bray-Curtis dissimilarity against Euclidean hillslope distance, zone difference, and that flow-path distance, conditioned on depth. Refit the zone effect after resolving the sample denominator (37 samples stated versus zone counts of 33, 25, 54 and 45). Apply weighted UniFrac to ASV sequences from Bricks 457/460/477 to test whether phylogenetic structure reveals the east-west signal (rho = 0.227, p = 0.092) that Bray-Curtis does not.

## What would support or refute it

Support: flow-path distance explains composition while hillslope position does not, and weighted UniFrac gives a significant east-west association. Refutation: neither flow-path nor hillslope metrics beat a zone-only model.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. ASV sequences are in CORAL, but flow-path distances need hydrological data not shown to exist in the supplied evidence.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--519fc7f6|Community turnover does not follow the hillslope]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--9b46b768|Hydrogeological zone explains over a quarter of sediment community variance]] (Extends retrieved work)
- Finding: [[findings/enigma_sso_asv_ecology--51556105|Groundwater and sediment host distinct taxa within the same wells]] (Extends retrieved work)

## Closest published work

- [PMID 16407148](https://pubmed.ncbi.nlm.nih.gov/16407148/) The diversity and biogeography of soil bacterial communities.
- [PMID 30265315](https://pubmed.ncbi.nlm.nih.gov/30265315/) Impact of hydrologic boundaries on microbial planktonic and biofilm communities in shallow terrestrial subsurface environments.
- [PMID 38755262](https://pubmed.ncbi.nlm.nih.gov/38755262/) Revealing the hierarchical structure of microbial communities.

PMID 16407148 finds soil composition largely independent of geographic distance at continental scale, and PMID 30265315 reviews hydrologic boundaries; neither tests flow-path versus hillslope distance within one site.
