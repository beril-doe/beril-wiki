---
type: "Concept"
description: "Combining annotation pipelines expands functional coverage and exposes residual uncertainty."
sources: ["summaries/discoveries.md"]
---
# Complementary Annotation Pipelines Rescue Functional Inference

Functional annotation is best treated as an evidence-integration problem rather than a single-tool decision. The [[summaries/discoveries]] synthesis shows that Bakta and eggNOG recover different parts of gene-function space, so their union can rescue assignments missed by either pipeline alone. [src: discoveries]

## Complementary coverage

Across 132.5M gene clusters, eggNOG provided higher COG coverage (51% versus 8.2% for Bakta), KEGG coverage (38.5% versus 17.3%), and Pfam coverage (63% versus 7.7%). [src: discoveries] Bakta provided higher GO coverage (15% versus 7.4%), product-description coverage (71.2% versus 70.4%), and unique UniRef50 links covering 79.2%. [src: discoveries]

These results **support** a complementary-pipeline model: eggNOG contributes broad orthology, pathway, and domain mappings, while Bakta contributes product descriptions, GO assignments, and distinct UniRef50 connectivity. [src: discoveries] The comparison does not establish that either pipeline is universally more accurate, because the reported metrics measure coverage of annotation categories rather than independent functional correctness. [src: discoveries]

## Union rescues missed clusters

Combining Bakta and eggNOG increased coverage for any functional annotation to 77.3%. [src: discoveries] Bakta rescued 11.2M gene clusters among the 39.2M clusters missed by eggNOG. [src: discoveries] This **supports** using a union or evidence-triangulation workflow when the objective is to minimize unannotated sequence space, while retaining the provenance of which pipeline supplied each assignment. [src: discoveries]

The result connects directly to [[concepts/evidence-triangulation-for-functional-annotation]] and [[concepts/composite-functional-annotation]]: an annotation supported by multiple independent evidence types should be distinguished from an assignment supplied by only one pipeline. [src: discoveries] It also refines [[concepts/functional-dark-matter]], because apparent darkness can reflect pipeline-specific blind spots rather than complete absence of functional evidence. [src: discoveries]

## Provenance and database coverage remain limiting factors

Only 33.3% of Bakta's 17.6M distinct UniRef50 identifiers existed in the BERDL UniProt identifier table. [src: discoveries] This **weakens** any interpretation that a Bakta UniRef50 link automatically provides locally recoverable downstream functional detail, because identifier presence in the annotation output did not guarantee representation in the queried BERDL table. [src: discoveries]

The findings therefore **support** provenance-aware joins between annotation outputs and reference databases, with explicit reporting of missing identifiers and source-specific coverage. [src: discoveries] This requirement is related to [[concepts/schema-to-value-space-join-validation]] and [[concepts/provenance-aware-resource-discovery]], which address whether an annotation can be connected to usable reference data rather than merely recorded as a label. [src: discoveries]

## Implications for functional inference

A practical composite workflow should preserve Bakta and eggNOG assignments separately, merge them only after identifier and evidence-type validation, and mark whether a function is pipeline-specific or independently supported. [src: discoveries] The workflow should also distinguish descriptive product labels, orthology assignments, domain evidence, pathway mappings, GO terms, and UniRef50 links instead of treating them as interchangeable evidence. [src: discoveries]

This approach **refines** [[concepts/environmental-resistome]] because resistance conclusions can change when one annotation namespace detects relevant functions and another does not. [src: discoveries] It also **supports** [[concepts/structural-annotation-gap]]: recovering a label through a complementary pipeline is useful, but it does not by itself demonstrate that the underlying gene model, family assignment, or biological interpretation is correct. [src: discoveries]

## Open Directions

- Join the 17.6M Bakta UniRef50 identifiers against a refreshed BERDL UniProt identifier table, and quantify how much downstream functional evidence becomes recoverable after the missing identifier coverage is addressed. [src: discoveries]
- Build a gold-standard subset with experimentally characterized proteins, then compare Bakta-only, eggNOG-only, and union annotations by precision and recall rather than coverage alone. [src: discoveries]
- Stratify the 11.2M Bakta-rescued clusters by COG, KEGG, Pfam, GO, product-description, and UniRef50 evidence to determine which annotation classes contribute most to functional recovery. [src: discoveries]
- Test whether pipeline-specific annotations alter downstream resistome, pangenome, or dark-gene conclusions by rerunning the same analyses with Bakta-only, eggNOG-only, and provenance-filtered union annotations. [src: discoveries]
