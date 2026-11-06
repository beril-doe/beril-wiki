---
type: "Finding"
description: "Under a permutation null (200 label permutations, mean 0.785 \u00b1 0.054), the observed E1\u2013E3 top-30 target Jaccard of 0.104 had empirical p = 0.000, so divergence is real, but the earlier NB04 argument from Jaccard 0.14 lacked a reference distribution and was retracted."
finding_id: "ibd_phage_targeting--56e3bb7d"
result: "correction"
source: "ibd_phage_targeting"
quantities: [{"value": "0.104", "what": "observed Jaccard between top-30 E1 and E3 target sets", "unit": "Jaccard", "denominator": "", "scope": "E1 vs E3"}, {"value": "0.785 \u00b1 0.054", "what": "permutation-null Jaccard mean", "unit": "Jaccard", "denominator": "200 random-label permutations", "scope": "E1 vs E3"}, {"value": "0.14", "what": "original NB04 Jaccard, near the random-overlap baseline (~0.10)", "unit": "Jaccard", "denominator": "", "scope": "E1 vs E3 original claim"}]
caveat: "Stopping-rule criteria failed for held-out-species Jaccard (E1 0.230, E3 0.064 versus > 0.5) and bootstrap ARI (0.16 versus > 0.30), so the original within-ecotype Tier-A could not be trusted directly."
first_added: "2026-10-27"
source_hash: "7bb70c12c17426e8c3553768511907d214bbcaa696a58e3a283e6ad8dd52ff53"
---
# Ecotype-specific targeting survives, but the earlier Jaccard statistic was replaced

Under a permutation null (200 label permutations, mean 0.785 ± 0.054), the observed E1–E3 top-30 target Jaccard of 0.104 had empirical p = 0.000, so divergence is real, but the earlier NB04 argument from Jaccard 0.14 lacked a reference distribution and was retracted. [src: ibd_phage_targeting]

## Key figures

- **0.104 Jaccard**: observed Jaccard between top-30 E1 and E3 target sets (scope E1 vs E3) [src: ibd_phage_targeting]
- **0.785 ± 0.054 Jaccard**: permutation-null Jaccard mean (denominator 200 random-label permutations; scope E1 vs E3) [src: ibd_phage_targeting]
- **0.14 Jaccard**: original NB04 Jaccard, near the random-overlap baseline (~0.10) (scope E1 vs E3 original claim) [src: ibd_phage_targeting]

## Evidence

> 2. **H2b — target sets differ between ecotypes (Jaccard = 0.14).** ~~*Interpretation retained; statistic replaced.*~~ Jaccard 0.14 was near the random-overlap baseline (~0.10 for top-30 of ~300 filtered species). Under a permutation null (200 random-label permutations, null mean 0.785 ± 0.054), the observed Jaccard of 0.104 has empirical p = 0.000 — H2b survives strongly and the divergence is real, but the claim in NB04 rested on an effect size without a reference distribution, which is the wrong argument structure. [src: ibd_phage_targeting]

From the report [[summaries/ibd_phage_targeting__REPORT]].

## Caveat

Stopping-rule criteria failed for held-out-species Jaccard (E1 0.230, E3 0.064 versus > 0.5) and bootstrap ARI (0.16 versus > 0.30), so the original within-ecotype Tier-A could not be trusted directly. [src: ibd_phage_targeting]

> | 1. Feature-leakage bound (held-out-species Jaccard) | > 0.5 | 0.230 ✗ | 0.064 ✗ | | 2. Ecotype-specific Tier-A (NB04e) | ≥ 3 | 51 ✓ | 40 ✓ (single-study) | | 3. Engraftment pathobionts under confound-free contrast | ≥ 3 of 6 | 5/5 tested ✓ (cohort-level) | | 4. Ecotype framework internal stability (bootstrap ARI) | > 0.30 | 0.16 ✗ | [src: ibd_phage_targeting]

## Other caveats in this report

- The two phage-gap species score 4.0 and 3.3; INPHARED and IMG/VR searches remain a priority rather than completed evidence. [src: ibd_phage_targeting]
- No E1 patient has a feasible pure-phage cocktail in the proposed design, which instead combines direct phages, alternative therapies, and limited or engineered interventions. [src: ibd_phage_targeting]
- F. plautii occurs in 78 % of patients, including all nine E1 patients; its bile-acid-coupling cost and phage gap motivate deprioritization. [src: ibd_phage_targeting]
- E. coli is present in only 35 % of UC Davis patients, limiting direct applicability of the five-phage cocktail to ~8/23 patients. [src: ibd_phage_targeting]
- The proposed dosing rules call for ecotype reassessment every 3-6 months, ecotype-conditional target inclusion, and full retesting after a 5-fold M. gnavus qPCR change; these are proposed clinical rules, not validated outcomes. [src: ibd_phage_targeting]
