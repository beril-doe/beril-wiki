---
type: "Finding"
description: "Beta-lactamases are 54.9% core (p=7.7e-74 for enrichment vs baseline) and intrinsic efflux pumps like emhABC are >95% core, whereas regulatory genes are only 6.5% core and blaTEM, tet(C) and ant(2'')-Ia are 0% core."
finding_id: "amr_pangenome_atlas--9947286c"
result: "observation"
source: "amr_pangenome_atlas"
quantities: [{"value": "54.9%", "what": "core fraction of beta-lactamase AMR clusters", "unit": "%", "denominator": "", "scope": "p=7.7e-74 vs baseline"}, {"value": "6.5%", "what": "core fraction of regulatory AMR genes", "unit": "%", "denominator": "", "scope": ""}, {"value": "0%", "what": "core fraction of blaTEM, tet(C) and ant(2'')-Ia", "unit": "%", "denominator": "", "scope": "fully accessory/singleton"}, {"value": ">95%", "what": "core fraction of intrinsic efflux pumps such as emhABC", "unit": "%", "denominator": "", "scope": ""}]
caveat: "Mechanism labels were assigned by keyword matching against AMRFinderPlus product descriptions, not by the CARD Antibiotic Resistance Ontology."
first_added: "2026-10-27"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# Core versus accessory status of AMR genes depends on resistance mechanism

Beta-lactamases are 54.9% core (p=7.7e-74 for enrichment vs baseline) and intrinsic efflux pumps like emhABC are >95% core, whereas regulatory genes are only 6.5% core and blaTEM, tet(C) and ant(2'')-Ia are 0% core. [src: amr_pangenome_atlas]

## Key figures

- **54.9%**: core fraction of beta-lactamase AMR clusters (scope p=7.7e-74 vs baseline) [src: amr_pangenome_atlas]
- **6.5%**: core fraction of regulatory AMR genes [src: amr_pangenome_atlas]
- **0%**: core fraction of blaTEM, tet(C) and ant(2'')-Ia (scope fully accessory/singleton) [src: amr_pangenome_atlas]
- **>95%**: core fraction of intrinsic efflux pumps such as emhABC [src: amr_pangenome_atlas]

## Evidence

> Not all AMR mechanisms behave the same. **Beta-lactamases are 54.9% core** (p=7.7e-74 for enrichment vs baseline) — these are intrinsic resistance genes present in the species' chromosomal backbone. In contrast, **regulatory genes are only 6.5% core**, and known mobile elements like blaTEM, tet(C), and ant(2'')-Ia are **0% core** (fully accessory/singleton). Efflux pumps split: intrinsic pumps like emhABC are >95% core, while acquired efflux genes are accessory. [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

Mechanism labels were assigned by keyword matching against AMRFinderPlus product descriptions, not by the CARD Antibiotic Resistance Ontology. [src: amr_pangenome_atlas]

> Mechanism classification uses keyword matching against AMRFinderPlus product descriptions (e.g., "beta-lactamase", "efflux", "acetyltransferase"), not the CARD Antibiotic Resistance Ontology (ARO). [src: amr_pangenome_atlas]

## Other caveats in this report

- Environment classification is limited by sparse and inconsistent BioSample isolation-source metadata; 46.8% of species fall in Other/Unknown. [src: amr_pangenome_atlas]
- The 100% identity link threshold may miss close variants, and fitness findings from predominantly environmental Fitness Browser organisms may not generalize to recently acquired mobile resistance in clinical pathogens. [src: amr_pangenome_atlas]
- The 22.2% unclassified fraction partly reflects keyword-match failures; CARD ARO cross-reference mapping is proposed as a more systematic alternative. [src: amr_pangenome_atlas]
- The authors propose, rather than directly establish, that greater niche breadth enables AMR accumulation through more opportunities for horizontal transfer. [src: amr_pangenome_atlas]
- Clinical-pathogen over-representation in genome databases may inflate AMR counts for human-associated species. [src: amr_pangenome_atlas]
