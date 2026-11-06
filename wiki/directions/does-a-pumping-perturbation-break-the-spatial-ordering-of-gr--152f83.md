---
type: "Research direction"
description: "The spatial arrangement of Oak Ridge groundwater communities was stable between two dates 9 days apart (date explains 0.8%, Mantel rho=0.867). Does a hydrologic perturbation such as pumping break that arrangement, and does it do so beyond ordinary elapsed-time and seasonal drift?"
hypothesis: "Spatial ordering of wells persists across short intervals without perturbation but degrades after a pumping-driven shift in flow, so the Mantel correlation between matched pre- and post-perturbation snapshots falls below the unperturbed 9-day value."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Existing snapshots lack matched wells across a measured perturbation, so new paired sampling before and after pumping is required."
collections: ["enigma-coral"]
findings: ["enigma_sso_asv_ecology--6ee64744", "enigma_sso_asv_ecology--ab22d581"]
conflicts: []
papers: ["34130083", "38755262", "38552495", "39998254"]
builds_on: ["findings/enigma_sso_asv_ecology--6ee64744", "findings/enigma_sso_asv_ecology--ab22d581"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does a pumping perturbation break the spatial ordering of groundwater communities?

The spatial arrangement of Oak Ridge groundwater communities was stable between two dates 9 days apart (date explains 0.8%, Mantel rho=0.867). Does a hydrologic perturbation such as pumping break that arrangement, and does it do so beyond ordinary elapsed-time and seasonal drift?

## Hypothesis

Spatial ordering of wells persists across short intervals without perturbation but degrades after a pumping-driven shift in flow, so the Mantel correlation between matched pre- and post-perturbation snapshots falls below the unperturbed 9-day value.

## Why it matters

It would reconcile short-term stability with multi-year, recharge-driven change reported elsewhere, and show what sampling frequency a contaminated site needs.

## How to test it

The existing pump-test ASV snapshot (Brick 460-462, wells L8, M5, U2) overlaps the 5-well set (L7, L9, M4, M6, U2) only at U2, so it cannot support a distance-matrix comparison, and U3 is absent from both. Use it only to check whether Rhodanobacter peaks at M5. The decisive design is new matched sampling of the same wells (including M5 and U3) at two or more pre-perturbation times, to give a baseline Mantel value, then during and after a controlled pumping event. Compare the Mantel correlation across the perturbation with the baseline.

## What would support or refute it

Support: the post-perturbation Mantel correlation falls clearly below the unperturbed baseline (near 0.867 for 9 days). Refutation: it stays near the baseline, implying the structure is robust to pumping.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Existing snapshots lack matched wells across a measured perturbation, so new paired sampling before and after pumping is required.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--6ee64744|Groundwater spatial patterns are stable over nine days]] (Extends retrieved work)
- Finding: [[findings/enigma_sso_asv_ecology--ab22d581|No detectable groundwater community change over nine days]] (Extends retrieved work)

## Closest published work

- [PMID 34130083](https://pubmed.ncbi.nlm.nih.gov/34130083/) Groundwater bacterial communities evolve over time in response to recharge.
- [PMID 38755262](https://pubmed.ncbi.nlm.nih.gov/38755262/) Revealing the hierarchical structure of microbial communities.
- [PMID 38552495](https://pubmed.ncbi.nlm.nih.gov/38552495/) Reproducible responses of geochemical and microbial successional patterns in the subsurface to carbon source amendment.
- [PMID 39998254](https://pubmed.ncbi.nlm.nih.gov/39998254/) Minimal changes in microbial abundances and diversity over 7 years of emplacement for modules of compacted bentonite exposed to natural groundwater.

PMID 34130083 reports groundwater communities diverging across recharge events and PMID 39998254 reports stability in bentonite, but neither follows spatial-structure persistence through a defined perturbation in matched wells at a contaminated site.
