---
type: "Finding"
description: "The GT2 gene tree yielded 77 detected HGT events, of which 32 were high-confidence cross-phylum events (normalised); the strongest, Node_4915, spans 8 phyla at max divergence 4.843."
finding_id: "t4ss_cazy_environmental_hgt--a2b33180"
result: "observation"
source: "t4ss_cazy_environmental_hgt"
quantities: [{"value": "77", "what": "HGT events detected in the GT2 gene tree", "unit": "events", "denominator": "", "scope": "GT2 gene tree"}, {"value": "32", "what": "high-confidence cross-phylum events (normalised)", "unit": "events", "denominator": "", "scope": "GT2 gene tree"}, {"value": "8", "what": "phyla spanned by Node_4915", "unit": "phyla", "denominator": "", "scope": "Node_4915"}, {"value": "4.843", "what": "max divergence at Node_4915", "unit": "", "denominator": "", "scope": ""}]
caveat: "Pending checks include Node_4915 BLAST validation against NCBI nr and a housekeeping-gene null baseline."
first_added: "2026-10-27"
source_hash: "51a111efe7b5ea5f55b6310291e8badbd42dcc5ebe29717b03e23d2c103de389"
---
# GT2 gene tree shows many cross-phylum horizontal transfer events

The GT2 gene tree yielded 77 detected HGT events, of which 32 were high-confidence cross-phylum events (normalised); the strongest, Node_4915, spans 8 phyla at max divergence 4.843. [src: t4ss_cazy_environmental_hgt]

## Key figures

- **77 events**: HGT events detected in the GT2 gene tree (scope GT2 gene tree) [src: t4ss_cazy_environmental_hgt]
- **32 events**: high-confidence cross-phylum events (normalised) (scope GT2 gene tree) [src: t4ss_cazy_environmental_hgt]
- **8 phyla**: phyla spanned by Node_4915 (scope Node_4915) [src: t4ss_cazy_environmental_hgt]
- **4.843**: max divergence at Node_4915 [src: t4ss_cazy_environmental_hgt]

## Evidence

> **77 HGT events** detected in GT2 gene tree; **32 high-confidence cross-phylum events** (normalised). Strongest: Node_4915 spans 8 phyla at max divergence 4.843. [src: t4ss_cazy_environmental_hgt]

From the report [[summaries/t4ss_cazy_environmental_hgt__REPORT]].

## Caveat

Pending checks include Node_4915 BLAST validation against NCBI nr and a housekeeping-gene null baseline. [src: t4ss_cazy_environmental_hgt]

> 1. Synteny threshold permutation test (requires Spark unfiltered data) 2. Node_4915 BLAST validation (requires BLAST against NCBI nr) 3. Housekeeping gene null baseline 4. Biome enrichment factorisation: θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)] [src: t4ss_cazy_environmental_hgt]

## Other caveats in this report

- The report labels the work preliminary and says NB05 threshold validation and NB06 manuscript figures are pending, although it later presents NB05 analysis results. [src: t4ss_cazy_environmental_hgt]
- T4SS-mediated dissemination of carbohydrate-active enzymes is presented as a hypothesis, not a demonstrated mechanism; the associations are observational and require experimental validation. [src: t4ss_cazy_environmental_hgt]
- The report links CAZy–T4SS synteny to a metal-resistance niche-breadth hypothesis; describing these genomes as transfer hubs is interpretive. [src: t4ss_cazy_environmental_hgt]
