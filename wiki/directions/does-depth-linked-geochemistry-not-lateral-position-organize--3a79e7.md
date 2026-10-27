---
type: "Research direction"
description: "Does geochemistry measured in the same wells account for the depth-driven community turnover and the sediment-versus-groundwater genus partition, while lateral position adds little?"
hypothesis: "Within-well depth turnover (median Bray-Curtis 0.977 versus 0.835 for same-zone samples across wells) reflects plume geochemistry. Geochemical variables alone should then predict community composition about as well as depth or zone, and lateral coordinates should add little. Concurrent sediment and groundwater sampling should preserve the Rhodanobacter and Anaeromyxobacter partition."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Geochemistry is registered but sample-name resolution is incomplete, and concurrent sediment-groundwater sampling does not exist."
collections: ["enigma-coral"]
findings: ["enigma_sso_asv_ecology--7ffad219", "enigma_sso_asv_ecology--519fc7f6", "enigma_sso_asv_ecology--9b46b768", "enigma_sso_asv_ecology--51556105", "enigma_sso_asv_ecology--ab22d581"]
conflicts: []
papers: ["22179233", "20305024", "30265315", "16407148", "34130083"]
builds_on: ["findings/enigma_sso_asv_ecology--7ffad219", "findings/enigma_sso_asv_ecology--519fc7f6", "findings/enigma_sso_asv_ecology--9b46b768", "findings/enigma_sso_asv_ecology--51556105", "findings/enigma_sso_asv_ecology--ab22d581"]
projects: ["enigma_sso_asv_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Does depth-linked geochemistry, not lateral position, organize Oak Ridge subsurface communities?

Does geochemistry measured in the same wells account for the depth-driven community turnover and the sediment-versus-groundwater genus partition, while lateral position adds little?

## Hypothesis

Within-well depth turnover (median Bray-Curtis 0.977 versus 0.835 for same-zone samples across wells) reflects plume geochemistry. Geochemical variables alone should then predict community composition about as well as depth or zone, and lateral coordinates should add little. Concurrent sediment and groundwater sampling should preserve the Rhodanobacter and Anaeromyxobacter partition.

## Why it matters

It would confirm a plume model currently inferred from community composition alone, and indicate that sampling designs should stratify by depth.

## How to test it

Load the registered SSO geochemistry (221 samples) from enigma-coral, resolving sample names to wells. Run variance partitioning (db-RDA) of communities on three predictor sets, geochemistry (pH, nitrate, uranium, metals), depth or zone, and lateral coordinates, without conditioning on depth, reporting unique and shared fractions plus cross-validated prediction from each set. Use the hillslope Mantel test (rho = -0.049, p = 0.580) only as a spatial-structure test, not as variance explained. Zone explained 27.5% of sediment variance (F = 4.05, p = 0.0001), but the report lists 37 segments against zone counts of 33, 25, 54 and 45; groundwater ASV data cover 5 of 9 wells. Resample groundwater concurrently with sediment to remove the 18-month offset.

## What would support or refute it

Support: geochemistry alone explains much of the community variation and predicts held-out samples comparably to depth or zone, with large shared depth-geochemistry variance, while lateral position adds little. Refute: geochemistry alone explains little total variation or predicts poorly where depth does well, or lateral structure emerges with concurrent sampling. Little unique geochemical variance beyond zone would not refute the mechanism, because depth-linked geochemistry predicts mostly shared variance.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Geochemistry is registered but sample-name resolution is incomplete, and concurrent sediment-groundwater sampling does not exist.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--7ffad219|Depth, not horizontal position, appears to determine plume exposure]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--519fc7f6|Community turnover does not follow the hillslope]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--9b46b768|Hydrogeological zone explains over a quarter of sediment community variance]] (Extends retrieved work)
- Finding: [[findings/enigma_sso_asv_ecology--51556105|Groundwater and sediment host distinct taxa within the same wells]] (Extends retrieved work)
- Finding: [[findings/enigma_sso_asv_ecology--ab22d581|No detectable groundwater community change over nine days]] (Extends retrieved work)

## Closest published work

- [PMID 22179233](https://pubmed.ncbi.nlm.nih.gov/22179233/) Denitrifying bacteria from the genus Rhodanobacter dominate bacterial communities in the highly contaminated subsurface of a nuclear legacy waste site.
- [PMID 20305024](https://pubmed.ncbi.nlm.nih.gov/20305024/) Denitrifying bacteria isolated from terrestrial subsurface sediments exposed to mixed-waste contamination.
- [PMID 30265315](https://pubmed.ncbi.nlm.nih.gov/30265315/) Impact of hydrologic boundaries on microbial planktonic and biofilm communities in shallow terrestrial subsurface environments.
- [PMID 16407148](https://pubmed.ncbi.nlm.nih.gov/16407148/) The diversity and biogeography of soil bacterial communities.
- [PMID 34130083](https://pubmed.ncbi.nlm.nih.gov/34130083/) Groundwater bacterial communities evolve over time in response to recharge.

PMID 22179233 ties Rhodanobacter dominance to low pH and 30265315 reviews hydrologic boundaries; neither tests depth versus horizontal structure with a paired sediment-groundwater design.
