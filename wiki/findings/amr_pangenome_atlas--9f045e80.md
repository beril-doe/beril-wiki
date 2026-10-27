---
type: "Finding"
description: "Zero AMR clusters have Pfam domain hits in the bakta_pfam_domains table, which the report suggests means AMRFinderPlus and Pfam HMM scans target non-overlapping sequence space for these gene families."
finding_id: "amr_pangenome_atlas--9f045e80"
result: "null result"
source: "amr_pangenome_atlas"
quantities: [{"value": "zero", "what": "AMR clusters with Pfam domain hits", "unit": "clusters", "denominator": "", "scope": "bakta_pfam_domains table"}]
caveat: "Some singleton AMR clusters may reflect annotation artifacts rather than true species-specific resistance genes."
first_added: "2026-10-27"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# No AMR clusters have Pfam domain hits

Zero AMR clusters have Pfam domain hits in the bakta_pfam_domains table, which the report suggests means AMRFinderPlus and Pfam HMM scans target non-overlapping sequence space for these gene families. [src: amr_pangenome_atlas]

## Key figures

- **zero clusters**: AMR clusters with Pfam domain hits (scope bakta_pfam_domains table) [src: amr_pangenome_atlas]

## Evidence

> 93.0% of AMR clusters have both Bakta product annotations and eggNOG hits (2 annotation sources). The remaining 7.0% have Bakta annotations only. Notably, **zero AMR clusters have Pfam domain hits** in the `bakta_pfam_domains` table — AMRFinderPlus and Pfam HMM scans appear to target non-overlapping sequence space for these gene families. The sparsely-annotated (1-source) AMR clusters are enriched for singletons (55.4% vs 34.6%). [src: amr_pangenome_atlas]

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
