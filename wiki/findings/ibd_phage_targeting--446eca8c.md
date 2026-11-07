---
type: "Finding"
description: "Among Tier-A core biosynthetic gene clusters versus the catalog background (Fisher's exact), iron_siderophore had OR 44.4 (FDR 6.5e-56) and genotoxin_microcin had OR 234.0 (FDR 3.3e-35)."
finding_id: "ibd_phage_targeting--446eca8c"
result: "observation"
source: "ibd_phage_targeting"
quantities: [{"value": "44.4", "what": "Fisher OR for iron_siderophore BGC enrichment (FDR 6.5e-56)", "unit": "odds ratio", "denominator": "54/286 Tier-A core BGCs vs 51/9,774 background BGCs", "scope": "Tier-A core vs BGC catalog"}, {"value": "234.0", "what": "Fisher OR for genotoxin_microcin BGC enrichment (FDR 3.3e-35)", "unit": "odds ratio", "denominator": "25/286 Tier-A core BGCs vs 4/9,774 background BGCs", "scope": "Tier-A core vs BGC catalog"}]
caveat: "The comparator is the full 10,060-cluster catalog rather than a matched set, so the 44\u00d7 iron OR is partly inflated by background rarity (51 / 9,774 = 0.5 %) and should not be read as a precise effect size."
first_added: "2026-10-27"
source_hash: "7bb70c12c17426e8c3553768511907d214bbcaa696a58e3a283e6ad8dd52ff53"
---
# Tier-A core gene clusters are enriched for iron-siderophore and genotoxin themes

Among Tier-A core biosynthetic gene clusters versus the catalog background (Fisher's exact), iron_siderophore had OR 44.4 (FDR 6.5e-56) and genotoxin_microcin had OR 234.0 (FDR 3.3e-35). [src: ibd_phage_targeting]

## Key figures

- **44.4 odds ratio**: Fisher OR for iron_siderophore BGC enrichment (FDR 6.5e-56) (denominator 54/286 Tier-A core BGCs vs 51/9,774 background BGCs; scope Tier-A core vs BGC catalog) [src: ibd_phage_targeting]
- **234.0 odds ratio**: Fisher OR for genotoxin_microcin BGC enrichment (FDR 3.3e-35) (denominator 25/286 Tier-A core BGCs vs 4/9,774 background BGCs; scope Tier-A core vs BGC catalog) [src: ibd_phage_targeting]

## Evidence

> **Test 1 — BGC-theme enrichment** (Fisher's exact, Tier-A core BGCs in theme vs background BGCs in theme; BH-FDR across themes; 4 IBD-relevant themes covering iron-siderophore MIBiG matches, genotoxin/microcin MIBiG matches, RiPP-bacteriocin classes, and NRPS-PKS-hybrid classes): | Theme | Tier-A core | Background | Fisher OR | FDR | Supported | |---|---:|---:|---:|---:|---| | **iron_siderophore** | 54 / 286 | 51 / 9,774 | **44.4** | **6.5e-56** | ✓ | | **genotoxin_microcin** | 25 / 286 | 4 / 9,774 | **234.0** | **3.3e-35** | ✓ | | **NRPS_PKS_hybrid** | 32 / 286 | 739 / 9,774 | **1.54** | **0.042** | ✓ | | bacteriocin_RiPP | 154 / 286 | 5,217 / 9,774 | 1.02 | 0.90 | — (background-rate) | [src: ibd_phage_targeting]

From the report [[summaries/ibd_phage_targeting__REPORT]].

## Caveat

The comparator is the full 10,060-cluster catalog rather than a matched set, so the 44× iron OR is partly inflated by background rarity (51 / 9,774 = 0.5 %) and should not be read as a precise effect size. [src: ibd_phage_targeting]

> - **NB08a Tier-A "background" comparator is the full BGC catalog (10,060 BGCs across all species), not a matched comparator.** The Fisher OR of 44× for iron_siderophore is partly inflated by the catalog-wide rarity of iron MIBiG matches (51 / 9,774 = 0.5 %). A more conservative comparator would be a "matched-niche" pathobiont set (gut Proteobacteria + CD-associated Firmicutes) at similar genome-assembly depth. The 44× number should not be treated as a precise effect size, but the qualitative finding — *E. coli* alone among actionable Tier-A carries the iron-siderophore signature — is robust across choice of comparator. [src: ibd_phage_targeting]

## Other caveats in this report

- The two phage-gap species score 4.0 and 3.3; INPHARED and IMG/VR searches remain a priority rather than completed evidence. [src: ibd_phage_targeting]
- No E1 patient has a feasible pure-phage cocktail in the proposed design, which instead combines direct phages, alternative therapies, and limited or engineered interventions. [src: ibd_phage_targeting]
- F. plautii occurs in 78 % of patients, including all nine E1 patients; its bile-acid-coupling cost and phage gap motivate deprioritization. [src: ibd_phage_targeting]
- E. coli is present in only 35 % of UC Davis patients, limiting direct applicability of the five-phage cocktail to ~8/23 patients. [src: ibd_phage_targeting]
- The proposed dosing rules call for ecotype reassessment every 3-6 months, ecotype-conditional target inclusion, and full retesting after a 5-fold M. gnavus qPCR change; these are proposed clinical rules, not validated outcomes. [src: ibd_phage_targeting]
