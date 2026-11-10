---
type: "Finding"
description: "CRISPR-Cas \u00d7 CBASS was the only tested pair not reaching significance (z = 0.21, p_emp = 0.98), with CBASS essentially independent of CRISPR-Cas presence despite the largest prevalence gap (96 % vs 7 %)."
finding_id: "phage_defense_arsenal--8c6a7f5f"
result: "null result"
source: "phage_defense_arsenal"
quantities: [{"value": "0.21", "what": "z-score for CRISPR-Cas \u00d7 CBASS co-occurrence", "unit": "", "denominator": "", "scope": ""}, {"value": "0.98", "what": "Empirical p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 96 % CRISPR-Cas prevalence is an upper bound from permissive eggNOG matching (Cas1 PF01867 is present in only 55 % of species); the syndrome analysis uses eggNOG OR Pfam, which favours recall, so CRISPR-Cas syndromes may be slightly underestimated in specificity but not in significance."
first_added: "2026-11-09"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# CRISPR-Cas and CBASS are the one pair without significant co-occurrence

CRISPR-Cas × CBASS was the only tested pair not reaching significance (z = 0.21, p_emp = 0.98), with CBASS essentially independent of CRISPR-Cas presence despite the largest prevalence gap (96 % vs 7 %). [src: phage_defense_arsenal]

## Key figures

- **0.21**: z-score for CRISPR-Cas × CBASS co-occurrence [src: phage_defense_arsenal]
- **0.98**: Empirical p-value [src: phage_defense_arsenal]

## Evidence

> The only pair that does not reach significance is **CRISPR-Cas × CBASS** (z = 0.21, p_emp = 0.98) — the two systems with the largest prevalence gap (96 % vs 7 %), where CBASS is essentially independent of CRISPR-Cas presence. [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

The 96 % CRISPR-Cas prevalence is an upper bound from permissive eggNOG matching (Cas1 PF01867 is present in only 55 % of species); the syndrome analysis uses eggNOG OR Pfam, which favours recall, so CRISPR-Cas syndromes may be slightly underestimated in specificity but not in significance. [src: phage_defense_arsenal]

> - **CRISPR-Cas prevalence (96 %) is inflated** by permissive eggNOG description-based matching. The Pfam Cas1 (PF01867) hit is only present in 55 % of species. Prevalence numbers in Finding 1 should be interpreted as an upper bound; the syndrome analysis uses the combined presence set (eggNOG OR Pfam) which favours recall, meaning CRISPR-Cas syndromes may be slightly underestimated in specificity but not in significance. [src: phage_defense_arsenal]

## Other caveats in this report

- Arms-race and syndrome tests use species with at least five sequenced genomes. [src: phage_defense_arsenal]
- The DISARM accessory-enrichment estimate is likely affected by nonspecific PF00176 DrmB/SNF2 helicase detection. [src: phage_defense_arsenal]
- The report argues that the DISARM per-cluster caveat does not undermine its species-level arms-race and syndrome results. [src: phage_defense_arsenal]
- The arms-race association varies by phylum; the Actinomycetota effect is described as roughly threefold weaker than the Campylobacterota effect. [src: phage_defense_arsenal]
- CRISPR-Cas prevalence is method-dependent: eggNOG description matching gives 96 %, versus ~55 % with Cas1 PF01867. [src: phage_defense_arsenal]
