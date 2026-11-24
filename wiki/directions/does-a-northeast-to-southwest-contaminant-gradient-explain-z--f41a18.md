---
type: "Research direction"
description: "Do measured geochemical gradients explain why SSO sediment communities differ by hydrogeological zone and turn over along the east-west axis rather than the hillslope?"
hypothesis: "Per-segment contaminant and geochemical measurements will explain the east-west turnover and add explanatory power beyond hydrogeological zone, consistent with a plume entering from the northeast and moving southwest."
approach: "experiment"
readiness: "unknown"
readiness_basis: "The geochemistry is registered in CORAL but not loaded into the KBase Data Lakehouse, so this is a data-access step, and the catalog did not show the SSO community tables."
databases: []
tables: []
findings: ["enigma_sso_asv_ecology--a33b6bed", "enigma_sso_asv_ecology--9b46b768", "enigma_sso_asv_ecology--5b3b97d0"]
conflicts: []
papers: ["20305024", "22140175", "16407148"]
builds_on: ["findings/enigma_sso_asv_ecology--a33b6bed", "findings/enigma_sso_asv_ecology--9b46b768", "findings/enigma_sso_asv_ecology--5b3b97d0"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does a northeast-to-southwest contaminant gradient explain zone and east-west structure in SSO sediment communities?

Do measured geochemical gradients explain why SSO sediment communities differ by hydrogeological zone and turn over along the east-west axis rather than the hillslope?

## Hypothesis

Per-segment contaminant and geochemical measurements will explain the east-west turnover and add explanatory power beyond hydrogeological zone, consistent with a plume entering from the northeast and moving southwest.

## Why it matters

If the plume explains community structure, community composition could serve as a map of contaminant transport. If zone alone explains it, the plume model is not needed.

## How to test it

Take the 221 SSO geochemistry samples already registered in CORAL, which are not yet in the KBase Data Lakehouse, and match them to the 37 sediment core segment communities. Fit a zone-only community model, then add measured contaminant concentrations. Test whether east-west turnover remains once geochemistry is included. Also compare VZ and VSZ directly against SZ1 and SZ2, and add pump-test groundwater data from wells L8, M5 and U2.

## What would support or refute it

Support: geochemistry reduces the east-west signal and adds explanatory power beyond zone. Refute: zone explains the same variance with geochemistry added, or the east-west signal is unchanged. The catalog did not show the SSO tables, so their form is unconfirmed.

## Data

Approach: experiment. Readiness: unknown. The geochemistry is registered in CORAL but not loaded into the KBase Data Lakehouse, so this is a data-access step, and the catalog did not show the SSO community tables.

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--a33b6bed|A northeast-to-southwest contamination plume is proposed to structure SSO communities]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--9b46b768|Hydrogeological zone, not well identity, structures SSO sediment communities]] (Candidate novel)
- Finding: [[findings/enigma_sso_asv_ecology--5b3b97d0|SSO community turnover is not aligned with the hillslope]] (Candidate novel)

## Closest published work

- [PMID 20305024](https://pubmed.ncbi.nlm.nih.gov/20305024/) Denitrifying bacteria isolated from terrestrial subsurface sediments exposed to mixed-waste contamination.
- [PMID 22140175](https://pubmed.ncbi.nlm.nih.gov/22140175/) Rhodanobacter denitrificans sp. nov., isolated from nitrate-rich zones of a contaminated aquifer.
- [PMID 16407148](https://pubmed.ncbi.nlm.nih.gov/16407148/) The diversity and biogeography of soil bacterial communities.

The Oak Ridge denitrifier papers (20305024, 22140175) and the soil biogeography paper (16407148) do not test hillslope versus east-west turnover or a plume gradient.
