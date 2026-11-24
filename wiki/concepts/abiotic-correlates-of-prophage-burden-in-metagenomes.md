---
type: "Concept"
description: "Whether taxonomy-inferred prophage burden in environmental metagenomes correlates with abiotic variables such as pH and temperature, and whether this agrees with pangenome-based enrichment; covers inference caveats."
sources: ["summaries/prophage_ecology__REPORT.md"]
---
# Abiotic correlates of prophage burden in metagenomes

Taxonomy-inferred prophage burden in NMDC metagenomes correlates with abiotic variables, most strongly pH and temperature, and this partly agrees with pangenome-based enrichment. [src: prophage_ecology] The evidence is a single report (prophage_ecology). It is correlational and rests on an inference not validated for prophage genes. [src: prophage_ecology] See also [[summaries/prophage_ecology__REPORT]] and [[concepts/environmental-structuring-of-prophage-gene-modules-beyond-host-phylogeny]].

## Literature Context

The two candidate papers do not test the hub's central question. Neither relates taxonomy-inferred prophage burden in metagenomes to pH or temperature, and neither checks the genus-level inference. They give only indirect context on prophage biology in specific environments.

One study of coral mucus reports that rising sea surface temperature promotes the spread of Vibrio species, which cause disease in many marine organisms [PMID 38366190](https://pubmed.ncbi.nlm.nih.gov/38366190/). The authors identified two phage species that infect Vibrio mediterranei by combining cultivation and metagenomic approaches. They also suggest that lytic Vibrio infections could trigger prophage induction, which might spread genetic elements such as virulence factors in the mucus layer [PMID 38366190](https://pubmed.ncbi.nlm.nih.gov/38366190/). This is a suggestion from one host-associated system, not a measured link between temperature and prophage content. It is compatible with the corpus's interpretation that induction triggers could explain environmental correlations. It does not test that interpretation, and it concerns induction by infection rather than by pH or temperature shifts.

A genome report on the Arthrospira/Limnospira strain O9.13F, isolated from an alkaline, winter-freezing Siberian lake, is relevant to the pH discussion only loosely. The authors confirmed the absence of plasmids and functional prophage sequences in that single genome [PMID 34943919](https://pubmed.ncbi.nlm.nih.gov/34943919/). The strain is also haloalkalotolerant, and it grew best at 20 °C, below the 35 °C reported as optimal for other strains of the genus [PMID 34943919](https://pubmed.ncbi.nlm.nih.gov/34943919/). One isolate cannot support or refute a population-level trend. Still, it shows that an organism from an alkaline environment can lack functional prophages. That sits uneasily with any assumption that alkalinity is uniformly associated with higher burden. It is a single-genome observation, so it is a caution and not a contradiction.

The corpus's own findings are not tested by these papers. The report found 57 significant module-abiotic correlations across 6,365 samples, with pH and temperature the strongest predictors. Its pangenome cross-validation was partial, covering modules B, C and G. Its suggestion that alkaline environments may favor lysogeny is untested here, and the candidate papers neither confirm nor refute it. The corpus's claims are therefore novel relative to this evidence. The inference caveats stay open: genus-level conservation of prophage content, and the lack of validation for prophage genes. The coral work supports one of the corpus's proposed follow-ups, which is cross-referencing environment-enriched modules with induction triggers. Direct detection of prophages in assemblies is still needed to ground the inference.

## Correlations with abiotic variables

The inference covered 6,365 samples with 87.2% median matching coverage and found 57 significant module-abiotic correlations (false discovery rate, FDR, < 0.05). [src: prophage_ecology] The report treats its hypothesis H1d as supported, with pH and temperature the strongest predictors. [src: prophage_ecology] Genus-level pangenome-derived burden scores were applied to the samples through two-tier taxonomy mapping (a [[entities/gtdb]] metadata bridge plus taxonomy_dim genus matching). [src: prophage_ecology] Source data are in [[entities/nmdc-integrated-collections]].

Spearman correlations reported:

| Module set | Variable | rho |
|---|---|---|
| Packaging | pH | 0.519 [src: prophage_ecology] |
| All modules | pH | 0.474 [src: prophage_ecology] |
| All modules | temperature | 0.399 [src: prophage_ecology] |
| All modules | depth | 0.361 [src: prophage_ecology] |
| All modules | total nitrogen | 0.333 [src: prophage_ecology] |

The report calls the positive pH correlation notable and suggests alkaline environments may favor lysogeny, consistent with pH-sensitive stress-induced prophage induction. [src: prophage_ecology] This is an interpretation, not a tested mechanism.

## Agreement with pangenome enrichment

Cross-validation shows concordance for modules B, C and G. [src: prophage_ecology] B_head_morphogenesis, C_tail and G_anti_defense were significant in both the bacterial pangenome enrichment and the NMDC correlation analyses. [src: prophage_ecology] Four other modules (A_packaging, D_lysis, E_integration, F_lysogenic_regulation) were NMDC-significant but not pangenome-enriched beyond phylogenetic expectation. The report attributes this to near-universal presence masking environment-specific pangenome variation. [src: prophage_ecology] Concordance is therefore partial, and the explanation for the four modules is the report's own and untested. See also [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions]].

## Inference caveats

The method assumes genus-level conservation of prophage content. That may fail for recently acquired or lost prophages. [src: prophage_ecology] The approach was validated for the polyhydroxybutyrate (PHB) granule ecology project but not independently for prophage genes. [src: prophage_ecology] The correlations are cross-sectional. The report proposes NMDC longitudinal samples, if available, to test within-site change over time and give causal evidence. [src: prophage_ecology] It also proposes cross-referencing environment-enriched modules with induction triggers (SOS response, pH stress, temperature shifts) to explain the pH and temperature correlations mechanistically. [src: prophage_ecology]

## Open Directions

- Validate taxonomy-based burden against prophages detected directly in NMDC metagenome assemblies. This would close the gap that the inference is unvalidated for prophage genes.
- Test sensitivity to genus-level conservation by repeating the analysis at lower taxonomic resolution or excluding genera with variable prophage content.
- Cross-reference environment-enriched modules with induction triggers to explain the pH and temperature correlations.
- Use NMDC longitudinal samples, if available, to test within-site changes in burden over time.
