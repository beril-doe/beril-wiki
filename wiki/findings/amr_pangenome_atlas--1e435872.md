---
type: "Finding"
description: "AMR genes are significantly less conserved than the pangenome average, with only 30.3% core vs 46.8% baseline (OR=0.49, chi-squared=23,117, p\u22480), and in a paired test of 4,252 species (each with \u22655 AMR clusters) 63.7% show AMR less core than their species baseline."
finding_id: "amr_pangenome_atlas--1e435872"
result: "observation"
source: "amr_pangenome_atlas"
quantities: [{"value": "30.3%", "what": "fraction of AMR clusters that are core", "unit": "%", "denominator": "AMR clusters", "scope": "vs 46.8% pangenome baseline"}, {"value": "2.2x", "what": "enrichment of AMR in the auxiliary genome", "unit": "fold", "denominator": "", "scope": "33.6% vs 15.3%"}, {"value": "63.7%", "what": "species showing AMR less core than their species baseline", "unit": "%", "denominator": "4,252 species each with \u22655 AMR clusters", "scope": "paired Wilcoxon p=1.1e-130"}, {"value": "-0.102", "what": "mean difference in core fraction (AMR minus species baseline)", "unit": "", "denominator": "", "scope": "paired test of 4,252 species"}]
caveat: "Some singleton AMR clusters may reflect annotation artifacts rather than true species-specific resistance genes."
first_added: "2026-10-27"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# AMR clusters are depleted from core and enriched in auxiliary genomes

AMR genes are significantly less conserved than the pangenome average, with only 30.3% core vs 46.8% baseline (OR=0.49, chi-squared=23,117, p≈0), and in a paired test of 4,252 species (each with ≥5 AMR clusters) 63.7% show AMR less core than their species baseline. [src: amr_pangenome_atlas]

## Key figures

- **30.3%**: fraction of AMR clusters that are core (denominator AMR clusters; scope vs 46.8% pangenome baseline) [src: amr_pangenome_atlas]
- **2.2x fold**: enrichment of AMR in the auxiliary genome (scope 33.6% vs 15.3%) [src: amr_pangenome_atlas]
- **63.7%**: species showing AMR less core than their species baseline (denominator 4,252 species each with ≥5 AMR clusters; scope paired Wilcoxon p=1.1e-130) [src: amr_pangenome_atlas]
- **-0.102**: mean difference in core fraction (AMR minus species baseline) (scope paired test of 4,252 species) [src: amr_pangenome_atlas]

## Evidence

> AMR genes are significantly less conserved than the pangenome average: only **30.3% are core** vs 46.8% baseline (OR=0.49, chi-squared=23,117, p≈0). The **auxiliary genome is 2.2x enriched** for AMR (33.6% vs 15.3%). This depletion is consistent across species: in a paired test of 4,252 species (each with ≥5 AMR clusters), 63.7% show AMR less core than their species baseline (Wilcoxon p=1.1e-130, mean difference -0.102). [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

Some singleton AMR clusters may reflect annotation artifacts rather than true species-specific resistance genes. [src: amr_pangenome_atlas]

> - **Singleton inflation**: Some singleton AMR clusters may reflect annotation artifacts rather than true species-specific resistance genes [src: amr_pangenome_atlas]

## Other caveats in this report

- Environment classification is limited by sparse and inconsistent BioSample isolation-source metadata; 46.8% of species fall in Other/Unknown. [src: amr_pangenome_atlas]
- The 100% identity link threshold may miss close variants, and fitness findings from predominantly environmental Fitness Browser organisms may not generalize to recently acquired mobile resistance in clinical pathogens. [src: amr_pangenome_atlas]
- Mechanism labels were assigned by product-description keywords, not by CARD Antibiotic Resistance Ontology terms. [src: amr_pangenome_atlas]
- The 22.2% unclassified fraction partly reflects keyword-match failures; CARD ARO cross-reference mapping is proposed as a more systematic alternative. [src: amr_pangenome_atlas]
- The authors propose, rather than directly establish, that greater niche breadth enables AMR accumulation through more opportunities for horizontal transfer. [src: amr_pangenome_atlas]
