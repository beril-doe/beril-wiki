---
type: "Research direction"
description: "Why does defense-system count rise with prophage burden in every major phylum, and are the defense systems encoded within the prophages themselves?"
hypothesis: "Part of the universal positive association comes from defense systems carried inside or beside prophages; it weakens when prophage-embedded systems are removed."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Annotations are in the catalog, but defense-prophage positional analysis needs new computation."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["phage_defense_arsenal--023c48cb", "phage_defense_arsenal--606107b1", "phage_defense_arsenal--8c6a7f5f", "prophage_ecology--3d5d045b"]
conflicts: []
papers: ["29371424", "29085076", "31533127", "25092302", "40639337"]
builds_on: ["findings/phage_defense_arsenal--023c48cb", "findings/phage_defense_arsenal--606107b1", "findings/phage_defense_arsenal--8c6a7f5f", "findings/prophage_ecology--3d5d045b"]
projects: ["phage_defense_arsenal", "prophage_ecology"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Does defense-system richness track prophage burden because defenses guard against, or are carried by, prophages?

Why does defense-system count rise with prophage burden in every major phylum, and are the defense systems encoded within the prophages themselves?

## Hypothesis

Part of the universal positive association comes from defense systems carried inside or beside prophages; it weakens when prophage-embedded systems are removed.

## Why it matters

It would distinguish an arms-race explanation from mobile-element hitchhiking of defense genes, reshaping how defense repertoires are interpreted.

## How to test it

In species from the pangenome, locate defense genes, including R-M Type II, Gabija and CBASS, relative to prophage regions. Recompute the within-phylum partial association between defense count and prophage burden, controlling for genome size, after excluding defense genes within prophage boundaries. Test whether Gabija and R-M co-occurring pairs sit together on the genome.

## What would support or refute it

Support: the association drops sharply after exclusion and pairs sit in islands. Refute: it stays similar in all phyla and defense genes are mostly outside prophages.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Annotations are in the catalog, but defense-prophage positional analysis needs new computation.

## Builds on

- Finding: [[findings/phage_defense_arsenal--023c48cb|Defense–prophage association is positive in all nine major phyla]] (Candidate novel)
- Finding: [[findings/phage_defense_arsenal--606107b1|R-M Type II and Gabija form the strongest defense syndrome]] (Candidate novel)
- Finding: [[findings/phage_defense_arsenal--8c6a7f5f|CBASS occurrence is independent of CRISPR-Cas]] (Candidate novel)
- Finding: [[findings/prophage_ecology--3d5d045b|Human-associated environments enriched for complete prophages and anti-defense genes beyond phylogeny]] (Candidate novel)

## Closest published work

- [PMID 29371424](https://pubmed.ncbi.nlm.nih.gov/29371424/) Systematic discovery of antiphage defense systems in the microbial pangenome.
- [PMID 29085076](https://pubmed.ncbi.nlm.nih.gov/29085076/) DISARM is a widespread bacterial defence system with broad anti-phage activities.
- [PMID 31533127](https://pubmed.ncbi.nlm.nih.gov/31533127/) Cyclic GMP-AMP signalling protects bacteria against viral infection.
- [PMID 25092302](https://pubmed.ncbi.nlm.nih.gov/25092302/) Pervasive domestication of defective prophages by bacteria.
- [PMID 40639337](https://pubmed.ncbi.nlm.nih.gov/40639337/) Bacteriophage genomes encode both broad and specific counter-defense repertoires to overcome bacterial defense systems.

29371424 and 29085076 describe defense islands; this tests whether the pan-phylum link with prophage burden reflects defense carried by prophages.
