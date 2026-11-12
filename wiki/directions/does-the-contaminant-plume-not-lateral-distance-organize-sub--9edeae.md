---
type: "Research direction"
description: "Do microbial communities at the Oak Ridge site differ with depth because contamination moves through particular saturated layers, rather than because of horizontal position or hydrogeological zone alone?"
hypothesis: "Within a hydrogeological zone, differences between communities track measured contaminant chemistry (nitrate, metals, pH), not horizontal distance between wells. Layer identity adds little once chemistry is known."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "Community counts and sample tables are shown, but the catalog did not show whether chemistry exists for the same samples; the depth finding's caveat says the plume explanation awaits geochemical confirmation."
databases: ["enigma.coral", "enigma.sso_staging"]
tables: ["enigma.coral.ddt_brick0000459", "enigma.coral.ddt_brick0000476", "enigma.coral.sdt_sample", "enigma.coral.sdt_community", "enigma.sso_staging.toc_tn_anions", "enigma.sso_staging.picarro_gas", "enigma.sso_staging.sample_registry"]
findings: ["enigma_sso_asv_ecology--7ffad219", "enigma_sso_asv_ecology--519fc7f6", "enigma_sso_asv_ecology--9b46b768"]
conflicts: []
papers: ["20305024", "22140175", "30265315", "16407148"]
builds_on: ["findings/enigma_sso_asv_ecology--7ffad219", "findings/enigma_sso_asv_ecology--519fc7f6", "findings/enigma_sso_asv_ecology--9b46b768"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does the contaminant plume, not lateral distance, organize subsurface communities by depth layer?

Do microbial communities at the Oak Ridge site differ with depth because contamination moves through particular saturated layers, rather than because of horizontal position or hydrogeological zone alone?

## Hypothesis

Within a hydrogeological zone, differences between communities track measured contaminant chemistry (nitrate, metals, pH), not horizontal distance between wells. Layer identity adds little once chemistry is known.

## Why it matters

Same-well, different-depth pairs were nearly completely different, while same-zone pairs from different wells were more alike. Hillslope position showed no structure. The plume explanation currently rests on community composition alone and awaits chemical confirmation. If chemistry explains the depth pattern, sampling and remediation should follow flow layers rather than map position.

## How to test it

First establish which sediment and groundwater samples have matching chemistry, since the registered site geochemistry samples may not yet be loaded and the staging tables for carbon, nitrogen, anions and gas have unshown coverage. Also settle the sediment sample count, because the sediment analysis counts 37 core segments but its zone counts add up to more. For samples with chemistry, partition community dissimilarity among zone, depth, horizontal distance and chemistry. Then compare same-zone, cross-well pairs matched for chemistry with pairs that differ in chemistry. If chemistry is missing for most samples, measure it on archived cores and well water.

## What would support or refute it

Support: chemistry removes most of the depth and zone effect, and cross-well similarity of same-zone samples follows chemical similarity. Refute: depth or zone still explains much of the variation after chemistry is accounted for, or horizontal distance explains it, pointing to isolation or unmeasured factors.

## Data

Approach: analysis then experiment. Readiness: unknown. Community counts and sample tables are shown, but the catalog did not show whether chemistry exists for the same samples; the depth finding's caveat says the plume explanation awaits geochemical confirmation.

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--7ffad219|Depth, not horizontal position, appears to determine plume exposure]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--519fc7f6|Community turnover does not follow the hillslope]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--9b46b768|Hydrogeological zone explains over a quarter of sediment community variance]] (Extends retrieved work)

## Closest published work

- [PMID 20305024](https://pubmed.ncbi.nlm.nih.gov/20305024/) Denitrifying bacteria isolated from terrestrial subsurface sediments exposed to mixed-waste contamination.
- [PMID 22140175](https://pubmed.ncbi.nlm.nih.gov/22140175/) Rhodanobacter denitrificans sp. nov., isolated from nitrate-rich zones of a contaminated aquifer.
- [PMID 30265315](https://pubmed.ncbi.nlm.nih.gov/30265315/) Impact of hydrologic boundaries on microbial planktonic and biofilm communities in shallow terrestrial subsurface environments.
- [PMID 16407148](https://pubmed.ncbi.nlm.nih.gov/16407148/) The diversity and biogeography of soil bacterial communities.

PMIDs 20305024 and 22140175 describe subsurface community members at this site and 30265315 reviews hydrologic boundaries, but none tests whether chemistry accounts for depth turnover compared with horizontal structure.
