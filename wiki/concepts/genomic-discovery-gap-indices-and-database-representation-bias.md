---
type: "Concept"
description: "Covers how to quantify which biomes and environments are under-represented in public genome databases using indices such as GDI, including the index's construction caveats and sampling-bias checks; stops at specific biome ranking."
sources: ["summaries/soil_frontier_genomics__REPORT.md"]
---
# Genomic discovery gap indices and database representation bias

The Genomic Discovery Index (GDI) is one way to quantify which environments are under-represented in public genome databases. The evidence here comes from a single report, [[summaries/soil_frontier_genomics__REPORT]], on soil biomes. That report defines GDI as OTU (operational taxonomic unit) richness divided by (mean genome completeness + 1), computed at 1° spatial bins. [src: soil_frontier_genomics] The report itself calls the index novel, with no published precedent, and lists several construction and sampling-bias caveats. [src: soil_frontier_genomics]

## Literature Context

The single candidate paper does not address genomic discovery gap indices directly. It is relevant to one assumption underneath them. Any index built from environmental sequencing, including the Genomic Discovery Index (GDI) in [[summaries/soil_frontier_genomics__REPORT]], assumes that the sequenced DNA represents the community in the sample. That assumption deserves scrutiny.

[PMID 21183646](https://pubmed.ncbi.nlm.nih.gov/21183646/) is an abstract-only report on soil metagenome access. It notes that soil microbial communities contain the highest level of prokaryotic diversity of any environment. It also states that extraction methods do not provide a uniform and unbiased subsample of metagenomic DNA, so accurate species distributions cannot be determined. According to the authors, any such bias propagates errors into estimates of overall microbial diversity and may exclude some microbial classes from study. They fractionated metagenomic DNA by vertical soil sampling, density gradients (cell separation), cell lysis stringency and DNA fragment size. Each fraction had a unique genetic diversity, with different predominant and rare species, judged by ribosomal intergenic spacer analysis (RISA) fingerprinting and phylochips. Combining fractions gave access to a more genetically diverse proportion of the metagenome, a gain of more than 80% over the best single extraction method. The authors stress that extracted DNA pools differ from the currently inaccessible complete soil metagenome. This is a methods study of soil DNA recovery. It says nothing about public genome databases or spatial bins.

The corpus's caveats sit consistently with this paper. The report concedes that GDI may be dominated by its OTU richness term and that its pH pattern may reflect sampling effort. The extraction-bias finding adds a third possible source of distortion that the report does not list: richness and completeness estimates depend on how DNA was recovered. Uneven recovery could distort both terms of the index. This extends the report's list of checks, but only as a hypothesis. The paper does not show that extraction bias affects GDI, and the abstract gives no data on the soils behind the report's 1° bins.

The literature here neither supports nor contradicts the report's central claims. These include the +0.8 pH unit gap, the near-tie between Forest GDI (902.36) and Cropland GDI (890.82), and the novelty of the index. The report's call for rarefaction and bootstrap confidence intervals remains untested against this evidence. Its self-described novelty, with no published precedent, is not contradicted by the candidate paper. Testing GDI's robustness to extraction method would be a sensible further open direction.

## How the index is built

GDI = OTU Richness / (Mean Genome Completeness + 1), computed at 1° spatial bins. [src: soil_frontier_genomics] The report states that the index is novel and has no published precedent. [src: soil_frontier_genomics] The report labels forest and cropland soils, which have the highest GDI values, as genomic-frontier biomes. [src: soil_frontier_genomics]

## Construction caveats

- The formula gives a GDI of 902 even with zero genomes (completeness = 0, denominator = 1). [src: soil_frontier_genomics]
- GDI conflates two dimensions, sampling gap and OTU richness. The report says it could be dominated by the richness term alone. [src: soil_frontier_genomics]
- The report proposes that reporting richness and completeness separately, as a 2D scatter, would be more interpretable than a scalar index. [src: soil_frontier_genomics]

## Sampling-bias checks

The report found that frontier areas (GDI > 1000) have mean pH = 6.74, against mean pH = 5.94 in mapped areas. This is a +0.8 pH unit gap, which the report reads as systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics]

The report limits this reading with a reverse-causality caveat. Alkaline soils may have fewer database genomes simply because fewer samples from those pH ranges were ever sequenced. That would be a sampling-effort bias, not a sign that alkaline microbes are harder to assemble or less studied. [src: soil_frontier_genomics]

The report proposes controlling for the number of 16S samples in each pH bin before computing GDI. This would separate true assembly or annotation gaps from sampling gaps. [src: soil_frontier_genomics]

Ranking differences also need uncertainty. Forest GDI (902.36) and Cropland GDI (890.82) differ by 1.3%. Without bootstrap CIs (confidence intervals), the report considers them not meaningfully distinguishable. [src: soil_frontier_genomics] It recommends describing the two as jointly the highest-GDI biomes, not as a ranked ordering. [src: soil_frontier_genomics]

## Pending checks

The report lists these analyses as not yet done:
- Rarefaction-corrected GDI, using uniform 16S sequencing depth before richness calculation. [src: soil_frontier_genomics]
- Bootstrap 95% CIs on biome-level GDI rankings, which require a raw-data rerun. [src: soil_frontier_genomics]
- Control of the pH discovery bias for the number of 16S samples per pH bin. [src: soil_frontier_genomics]
- Forest versus Cropland GDI reported with uncertainty before any ranked ordering is claimed. [src: soil_frontier_genomics]

## Open Directions

- Rerun GDI from raw data with rarefied 16S depth and bootstrap CIs. This would show whether the biome differences exceed the noise in the index.
- Plot richness against completeness per 1° bin as a 2D scatter. This would show whether the richness term alone drives the high-GDI bins.
- Stratify by the number of 16S samples per pH bin before computing GDI. This would test whether the alkaline gap reflects sampling effort or real assembly gaps.
- Test the index on a case with zero genomes to define its floor behaviour. This addresses the formula's value of 902 at zero completeness.
