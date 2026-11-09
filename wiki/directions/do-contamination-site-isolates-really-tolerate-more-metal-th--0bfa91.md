---
type: "Research direction"
description: "Heavy-metal-site isolates, and to a lesser degree waste and industrial isolates, scored higher on predicted metal tolerance, even within the dominant phylum. Do closely related strains from contaminated and clean sources differ in measured tolerance, and does tolerance grade with contamination type?"
hypothesis: "Within the same genus, isolates from heavy-metal sites tolerate higher metal concentrations than isolates from environmental baselines, with waste and industrial isolates in between, and genome-based scores predict this order."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The existing evidence is genome-based scores, and the available metal utilization tests were too few to check the prediction."
collections: ["kbase-ke-pangenome"]
findings: ["bacdive_metal_validation--09db2bda", "bacdive_metal_validation--1ac30de6", "bacdive_metal_validation--60f073d0", "bacdive_metal_validation--2a7f4c05"]
conflicts: []
papers: ["41601069", "33540257", "27371958"]
builds_on: ["findings/bacdive_metal_validation--09db2bda", "findings/bacdive_metal_validation--1ac30de6", "findings/bacdive_metal_validation--60f073d0", "findings/bacdive_metal_validation--2a7f4c05"]
projects: ["bacdive_metal_validation"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do contamination-site isolates really tolerate more metal than relatives from clean environments?

Heavy-metal-site isolates, and to a lesser degree waste and industrial isolates, scored higher on predicted metal tolerance, even within the dominant phylum. Do closely related strains from contaminated and clean sources differ in measured tolerance, and does tolerance grade with contamination type?

## Hypothesis

Within the same genus, isolates from heavy-metal sites tolerate higher metal concentrations than isolates from environmental baselines, with waste and industrial isolates in between, and genome-based scores predict this order.

## Why it matters

The grading across contamination types hangs on a very small heavy-metal group and a surprising lack of link with metal-utilization tests. Direct measurement would show whether genome scores reflect selection by contamination or lineage composition.

## How to test it

Pick Pseudomonadota genera with isolates from heavy-metal sites, waste or sludge, industrial sites and environmental baselines. Obtain strains from culture collections and measure the lowest inhibitory concentration for copper, zinc, cadmium and nickel. Compare across source classes within genus and against each strain's score from the Pangenome Collection metal-gene counts.

## What would support or refute it

Support: measured tolerance rises from baseline to heavy-metal-site isolates within genera and follows the genome score. Refute: tolerance is similar across sources within a genus, which would make the earlier signal a lineage effect.

## Data

Approach: experiment. Readiness: needs new measurements. The existing evidence is genome-based scores, and the available metal utilization tests were too few to check the prediction.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/bacdive_metal_validation--09db2bda|Heavy-metal contamination isolates score higher on predicted metal tolerance than baseline]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_metal_validation--1ac30de6|Contamination signal persists within the dominant phylum Pseudomonadota]] (Extends retrieved work)
- Finding: [[findings/bacdive_metal_validation--60f073d0|Metal-tolerance score effect appears to grade with contamination category]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_metal_validation--2a7f4c05|Metal utilization tests show no significant link to predicted score]] (Insufficient literature evidence)

## Closest published work

- [PMID 41601069](https://pubmed.ncbi.nlm.nih.gov/41601069/) Co-selection for heavy metal and multidrug resistance: Cadmium primes bacterial antibiotic resistance by enhancing intrinsic oxidative stress tolerance.
- [PMID 33540257](https://pubmed.ncbi.nlm.nih.gov/33540257/) Heavy metal pollution promotes antibiotic resistance potential in the aquatic environment.
- [PMID 27371958](https://pubmed.ncbi.nlm.nih.gov/27371958/) Antibiotic and metal resistance in a ST395 Pseudomonas aeruginosa environmental isolate: A genomics approach.

PMIDs 41601069 and 33540257 link contamination to resistance at community level, and PMID 27371958 describes one environmental isolate. None compares measured tolerance of related isolates from different source classes.
