---
type: "Concept"
description: "How keyword, Pfam or eggNOG annotation-proxy detection of prophage genes, rather than dedicated callers, shapes prevalence, false positives and domesticated remnants; stops at executed tool comparisons."
sources: ["summaries/phage_defense_arsenal__REPORT.md", "summaries/prophage_amr_comobilization__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
---
# Annotation-based prophage detection, prevalence and domesticated remnants

The prophage_ecology report says this likely inflates prevalence by including domesticated remnants and bacterial homologs, and that the false positive rate is uncharacterized. [src: prophage_ecology] The prophage_amr_comobilization report says its keyword/Pfam approach may include false positives such as phage-defense systems and miss divergent prophages. [src: prophage_amr_comobilization]

## Literature Context

The single candidate paper is a review of gene transfer agents (GTAs). It describes them as genetic elements derived from ancestral bacteriophages that the host has domesticated [PMID 38511257](https://pubmed.ncbi.nlm.nih.gov/38511257/). Unlike typical bacteriophages, GTAs show no preference for replicating or transferring the genes that encode them. They package chromosomal DNA, and sometimes extrachromosomal DNA, into virus-like capsids and pass it to neighboring cells [PMID 38511257](https://pubmed.ncbi.nlm.nih.gov/38511257/). The review stresses that GTAs resemble defective prophages, so finding new ones is not trivial. Candidate detection relies on genetic similarity to known GTAs. That approach has worked in α-proteobacterial lineages but is harder in more distant bacteria [PMID 38511257](https://pubmed.ncbi.nlm.nih.gov/38511257/). It also asks what the true prevalence of GTAs in prokaryote genomes is, and it presents this as an open question [PMID 38511257](https://pubmed.ncbi.nlm.nih.gov/38511257/). The paper is an abstract-level review. It does not report any annotation-proxy benchmark.

This fits the hub's main caveat. The prophage_ecology report finds prophage annotations in every one of 27,702 species. It says this likely inflates prevalence because the clusters include domesticated remnants and bacterial homologs, and it calls the false positive rate uncharacterized. The review agrees that domesticated, defective-prophage-like elements exist and are hard to tell apart from prophages by similarity alone [PMID 38511257](https://pubmed.ncbi.nlm.nih.gov/38511257/). That makes the hub's concern about remnants plausible. It does not quantify it.

The review also gives one concrete class of remnant that could be present in the near-universal packaging module A. GTAs package DNA into capsids, so a packaging-annotated cluster may come from a domesticated GTA rather than an active prophage [PMID 38511257](https://pubmed.ncbi.nlm.nih.gov/38511257/). This is a hypothesis for module A only. The abstract says nothing about the lysis module D or the other modules. The corpus's own reading of A, D and F as domesticated remnants, which it describes as consistent with Bobay et al. (2014), is not tested by this paper. The review's point that GTA detection depends on similarity to known GTAs also suggests that keyword, Pfam or eggNOG proxies would not separate GTAs from prophages. This extends the hub, which names bacterial integrases, host cell-wall lysins and phage-defense systems as the false-positive sources, by adding GTAs as another candidate source. The review does not test this either.

The corpus's proposals to run geNomad, VIBRANT or PHASTER on representative genomes are not addressed by the candidate paper. The review gives no false-positive rates or tool comparisons. The hub's prevalence figures therefore stay unvalidated against the literature here. They are consistent with the review's cautions but are not confirmed or contradicted by it.

## How annotation-proxy detection was done

The prophage_ecology report used eggNOG functional annotations as proxies for prophage genes, not tools such as geNomad or VIBRANT. [src: prophage_ecology] It queried 93M eggNOG annotations with 112 WHERE clause conditions. This found 4,005,537 prophage-associated gene clusters across 27,702 species. [src: prophage_ecology]

The prophage_amr_comobilization report used keyword/Pfam matching on bakta_annotations. [src: prophage_amr_comobilization] It counted 1,261,929 strict and 3,465,244 broad prophage marker clusters. [src: prophage_amr_comobilization] Its strict markers were terminase, phage structural proteins, and holin/lysin. [src: prophage_amr_comobilization] The report says its full inventory has 83,008 AMR (antimicrobial resistance) gene clusters. [src: prophage_amr_comobilization]

The prophage_ecology report claims the first systematic module-level analysis across >27,000 species and 10 environment categories. [src: prophage_ecology] It says earlier studies examined whole-prophage presence/absence or specific phage types. [src: prophage_ecology]

## Prevalence and what it means

Every one of the 27,702 species carried prophage annotations. [src: prophage_ecology] The report notes this far exceeds the estimate of Touchon et al. (2016) that ~46% of bacterial genomes harbor prophages. [src: prophage_ecology] It attributes the gap likely to its broader definition. It identifies individual prophage-associated gene clusters, including domesticated remnants, not intact prophages. [src: prophage_ecology]

Three modules were near-universal: packaging (A, 100%), lysis (D, 99.9%) and lysogenic regulation (F, 100%). [src: prophage_ecology] The report suggests modules A, D and F likely include many domesticated prophage remnants. These are defective prophages under purifying selection that keep packaging, lysis and regulatory genes. [src: prophage_ecology] It describes this as consistent with Bobay et al. (2014). [src: prophage_ecology]

Only 34.9% of species carry all 7 modules. [src: prophage_ecology]

Per-module gene clusters and share of species:

- A. Packaging: 707,217 clusters, 100.0% of species. [src: prophage_ecology]
- B. Head Morphogenesis: 87,336 clusters, 56.1% of species. [src: prophage_ecology]
- C. Tail: 189,271 clusters, 55.6% of species. [src: prophage_ecology]
- D. Lysis: 724,499 clusters, 99.9% of species. [src: prophage_ecology]
- E. Integration: 773,417 clusters, 99.1% of species. [src: prophage_ecology]
- F. Lysogenic Regulation: 1,682,902 clusters, 100.0% of species. [src: prophage_ecology]
- G. Anti-Defense: 63,508 clusters, 64.3% of species. [src: prophage_ecology]

Conservation is reported separately from the remnant interpretation. Lysis D was 62.6% core and packaging A 57.0% core. Integration E was 59.3% singleton and head B 56.0% singleton. [src: prophage_ecology] Prophage marker clusters in the amr_comobilization inventory were 83.8% accessory and 53.8% singleton. AMR clusters were 69.7% accessory and 36.1% singleton. [src: prophage_amr_comobilization]

## False positives and saturation

The phage_defense_arsenal report says its module classifier over-counts by design. Integrase, holin and endolysin terms also match non-phage genes, such as host integrases and cell-wall lysins. [src: phage_defense_arsenal] The prophage_ecology report likewise names bacterial integrases as homologs that may inflate prevalence. [src: prophage_ecology] The amr_comobilization report adds that phage-defense systems may be false positives and divergent prophages may be missed. [src: prophage_amr_comobilization]

The module count saturates at 7 for 35% of species. The eggNOG-description classifier is deliberately broad, so the count is not a specific prophage count. [src: phage_defense_arsenal] For this reason the arms-race regression uses n_prophage_clusters, an unbounded continuous count, as its primary predictor. n_prophage_modules is a coarse categorical secondary predictor. [src: phage_defense_arsenal]

Validation detected all 7 modules in each of 8 well-characterized prophage-carrying species. [src: prophage_ecology] The module definitions are validated for the core backbone (A, D, F) and less for accessory functions (E, G). [src: prophage_ecology]

## Proposed validation

The prophage_ecology report proposes running geNomad or VIBRANT on representative genomes to estimate false positive and negative rates and calibrate module prevalence. [src: prophage_ecology] The amr_comobilization report proposes applying geNomad or PHASTER to Lakehouse genomes and ingesting a new table. This would replace keyword detection with a validated tool. [src: prophage_amr_comobilization] It also proposes using scaffoldseq contig sequences to compute true genomic distances instead of ordinal gene positions. [src: prophage_amr_comobilization]

## Open Directions

- Run geNomad or VIBRANT on representative genomes and compare calls per module with the annotation proxy. This would close the uncharacterized false positive rate and test whether A, D and F prevalence reflects remnants.
- Ingest geNomad or PHASTER output as a Lakehouse table and recompute the AMR-prophage co-location with base-pair distances.
- Repeat the arms-race regression using only strict markers. This would test whether over-counting by broad terms changes the result.

See also [[concepts/limits-of-keyword-and-marker-based-functional-annotation]] and [[concepts/modular-architecture-and-co-occurrence-of-prophage-genes]].
