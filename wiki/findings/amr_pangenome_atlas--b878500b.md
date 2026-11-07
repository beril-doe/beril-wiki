---
type: "Finding"
description: "Among 2,684 species with \u22653 genomes and AlphaEarth embeddings, environmental diversity correlates positively with AMR count (Spearman rho=0.466, p=1.6e-144) and negatively with AMR core fraction (rho=-0.173, p=1.8e-19)."
finding_id: "amr_pangenome_atlas--b878500b"
result: "observation"
source: "amr_pangenome_atlas"
quantities: [{"value": "0.466", "what": "Spearman rho between environmental diversity and AMR count", "unit": "", "denominator": "2,684 species with \u22653 genomes and embeddings", "scope": "p=1.6e-144"}, {"value": "-0.173", "what": "Spearman rho between environmental diversity and AMR core fraction", "unit": "", "denominator": "2,684 species", "scope": "p=1.8e-19"}]
caveat: "Only 28% of genomes have AlphaEarth embeddings, biased toward genomes with geographic metadata."
first_added: "2026-10-27"
source_hash: "d3ff61262afb26bda0b9720898fba96907b71a2b2f1209b3f8d18d168f387de6"
---
# Species from more diverse environments carry more, less-core AMR genes

Among 2,684 species with ≥3 genomes and AlphaEarth embeddings, environmental diversity correlates positively with AMR count (Spearman rho=0.466, p=1.6e-144) and negatively with AMR core fraction (rho=-0.173, p=1.8e-19). [src: amr_pangenome_atlas]

## Key figures

- **0.466**: Spearman rho between environmental diversity and AMR count (denominator 2,684 species with ≥3 genomes and embeddings; scope p=1.6e-144) [src: amr_pangenome_atlas]
- **-0.173**: Spearman rho between environmental diversity and AMR core fraction (denominator 2,684 species; scope p=1.8e-19) [src: amr_pangenome_atlas]

## Evidence

> **AlphaEarth embedding analysis** (2,684 species with ≥3 genomes and embeddings) reveals that **environmental diversity strongly predicts AMR count** (Spearman rho=0.466, p=1.6e-144). Species sampled from more diverse environments carry more AMR genes, and those AMR genes are less core (rho=-0.173, p=1.8e-19). [src: amr_pangenome_atlas]

From the report [[summaries/amr_pangenome_atlas__REPORT]].

## Caveat

Only 28% of genomes have AlphaEarth embeddings, biased toward genomes with geographic metadata. [src: amr_pangenome_atlas]

> - **AlphaEarth coverage**: Only 28% of genomes have embeddings, biased toward genomes with geographic metadata [src: amr_pangenome_atlas]

## Other caveats in this report

- Environment classification is limited by sparse and inconsistent BioSample isolation-source metadata; 46.8% of species fall in Other/Unknown. [src: amr_pangenome_atlas]
- The 100% identity link threshold may miss close variants, and fitness findings from predominantly environmental Fitness Browser organisms may not generalize to recently acquired mobile resistance in clinical pathogens. [src: amr_pangenome_atlas]
- Mechanism labels were assigned by product-description keywords, not by CARD Antibiotic Resistance Ontology terms. [src: amr_pangenome_atlas]
- The 22.2% unclassified fraction partly reflects keyword-match failures; CARD ARO cross-reference mapping is proposed as a more systematic alternative. [src: amr_pangenome_atlas]
- The authors propose, rather than directly establish, that greater niche breadth enables AMR accumulation through more opportunities for horizontal transfer. [src: amr_pangenome_atlas]
