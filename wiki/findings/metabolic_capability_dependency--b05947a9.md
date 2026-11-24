---
type: "Finding"
description: "Carbon source utilization pathways are 3.7\u00d7 more likely to be latent than amino acid biosynthesis pathways (24.3% vs 6.5%)."
finding_id: "metabolic_capability_dependency--b05947a9"
result: "observation"
source: "metabolic_capability_dependency"
quantities: [{"value": "24.3%", "what": "latent fraction of carbon source utilization pathways", "unit": "%", "denominator": "", "scope": ""}, {"value": "6.5%", "what": "latent fraction of amino acid biosynthesis pathways", "unit": "%", "denominator": "", "scope": ""}, {"value": "3.7\u00d7", "what": "relative likelihood of being latent, carbon vs amino acid", "unit": "", "denominator": "", "scope": ""}]
caveat: "Condition-dependent carbon utilization pathways, such as for deoxyribose or ethanol, may be encoded but never activated in a lab setting, making them appear latent even if ecologically important."
first_added: "2026-11-24"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# Carbon utilization pathways are far more often latent than amino acid biosynthesis

Carbon source utilization pathways are 3.7× more likely to be latent than amino acid biosynthesis pathways (24.3% vs 6.5%). [src: metabolic_capability_dependency]

## Key figures

- **24.3%**: latent fraction of carbon source utilization pathways [src: metabolic_capability_dependency]
- **6.5%**: latent fraction of amino acid biosynthesis pathways [src: metabolic_capability_dependency]
- **3.7×**: relative likelihood of being latent, carbon vs amino acid [src: metabolic_capability_dependency]

## Evidence

> The finding that carbon source utilization pathways are 3.7× more likely to be latent than amino acid biosynthesis pathways (24.3% vs 6.5%) is a specific, testable prediction: organisms in nutrient-rich environments should disproportionately lose carbon-pathway genes over evolutionary time, while amino acid biosynthesis genes are retained under stronger purifying selection. [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

Condition-dependent carbon utilization pathways, such as for deoxyribose or ethanol, may be encoded but never activated in a lab setting, making them appear latent even if ecologically important. [src: metabolic_capability_dependency]

> Carbon source utilization pathways, by contrast, are highly condition-dependent — a pathway for utilizing deoxyribose or ethanol may be encoded but never activated in a lab setting, making it appear latent even if ecologically important. [src: metabolic_capability_dependency]

## Other caveats in this report

- Varying the active threshold ±25% (1.5–2.5) and latent threshold ±25% (0.75–1.25) gave latent fractions of 4.7% to 21.1% (SD = 5.9 percentage points across 16 threshold combinations). [src: metabolic_capability_dependency]
- The report states that the large intermediate zone (32.3%) makes the latent fraction moderately sensitive to threshold tightening. [src: metabolic_capability_dependency]
- GapMind deoxyribonate and myoinositol pathways lacked matching SEED subsystem role descriptions and were absent from all analyses. [src: metabolic_capability_dependency]
- Full-name GapMind phenylalanine and tyrosine entries lacked SEED coverage, but their phe and tyr equivalents were included through abbreviation-based matching. [src: metabolic_capability_dependency]
- Alanine appeared in fitness metrics but was excluded from classification for all organisms because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]
