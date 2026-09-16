<!-- tension-hash: 8853ea91529080d0 -->
# Annotation nulls across precomputed substrates: absence signal or method-dependent gap?

Several projects in the corpus report missing gene or domain calls. Whether a marker appears absent changes with the annotation substrate and the marker set used. On a precomputed Pfam (protein-family domain database) substrate, null rates differ between audits. One Pfam family was confirmed silently absent in one lineage. Two annotation pipelines also disagree on whether a cofactor pathway is present. [src: gene_function_ecological_agora, bacillota_b_subsurface_accessory, lanthanide_methylotrophy_atlas] This matters because downstream claims of gene loss or pathway absence rest on these nulls. Yet the projects describe the disagreements as method-level, and none of them establishes biological absence. [src: gene_function_ecological_agora, bacillota_b_subsurface_accessory, lanthanide_methylotrophy_atlas] The broader framing is in [[concepts/homology-search-negative-evidence]].

## Evidence Sides

**Side 1 — Pfam null rates vary with marker set and substrate**
On the same precomputed Pfam substrate, one audit reported 12/22 marker Pfams missing. Another reported 7 of 33 markers with zero clusters. By contrast, `interproscan_domains` (domain calls from InterProScan, a tool that scans proteins against multiple domain databases) had 1 zero-coverage marker. [src: gene_function_ecological_agora] The null rate is therefore a property of the substrate and the marker selection, not a stable count of absent functions. [src: gene_function_ecological_agora]

**Side 2 — A specific Pfam is silently absent in Bacillota_B**
PF14537 was confirmed silently absent in Bacillota_B. [src: bacillota_b_subsurface_accessory] The project does not establish this as a biological absence. [src: gene_function_ecological_agora, bacillota_b_subsurface_accessory, lanthanide_methylotrophy_atlas]

**Side 3 — eggNOG and bakta disagree on PQQ biosynthesis**
The lanthanide atlas compares two pipelines on PQQ (pyrroloquinoline quinone, a cofactor) biosynthesis. eggNOG assigns orthologous-group functional annotations, and bakta is a genome annotation pipeline. The two disagree on whether PQQ biosynthesis is present. [src: lanthanide_methylotrophy_atlas] The same report says bakta over-calls pqqA-E. It also gives two unreconciled denominators, 2,320 versus 2,185, for genomes carrying xoxF (a lanthanide-dependent methanol dehydrogenase gene) but lacking eggNOG pqq. [src: lanthanide_methylotrophy_atlas] One pipeline therefore reports absence where the other reports presence, and the over-calling caveat stops either from being taken as ground truth. [src: lanthanide_methylotrophy_atlas]

## Possible Reconciliations

- *Hypothesis:* the gap between Pfam audits comes from differences in marker-set composition, not substrate behavior.
- *Hypothesis:* the precomputed Pfam substrate has coverage gaps that `interproscan_domains` does not share, which would explain both the marker-level nulls and the PF14537 silent absence.
- *Hypothesis:* the eggNOG–bakta PQQ disagreement mixes eggNOG under-calls with bakta over-calls. Neither pipeline alone would then give a reliable absence call.
- *Hypothesis:* the two xoxF denominators come from different pipeline stages or filters, not from an error in either count.

## Resolving Work

- Rerun the 22-marker and 33-marker sets against both the precomputed Pfam substrate and `interproscan_domains` on one shared genome set. Question: how much of the null-rate difference comes from the substrate rather than the marker selection?
- Run a sensitive profile-HMM (hidden Markov model) search for PF14537 directly on Bacillota_B proteomes and nucleotide assemblies. Question: is the silent absence a substrate gap or a true lack of the domain?
- Benchmark eggNOG and bakta pqqA-E calls against curated genomes with known PQQ status. Question: what are each pipeline's false-positive and false-negative rates?
- Trace the provenance of the 2,320 and 2,185 xoxF genome sets through the lanthanide atlas notebooks. Question: which filter separates them, and which denominator should downstream rates use?
