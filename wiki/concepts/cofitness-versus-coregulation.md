---
type: "Concept"
description: "Cofitness reveals shared fitness responses but does not prove direct co-regulation."
sources: ["summaries/amr_cofitness_networks__REPORT.md"]
---
# Cofitness Networks Do Not Establish Direct Co-regulation

Cofitness measures similarity in genes’ fitness profiles across experimental conditions, whereas direct co-regulation would require evidence that the genes are controlled by shared regulatory machinery; therefore, a cofitness edge is evidence of a shared phenotypic response, not proof of transcriptional control. [src: amr_cofitness_networks]

The [[summaries/amr_cofitness_networks__REPORT]] provides a pan-bacterial test of this distinction using Fitness Browser matrices, independent component analysis (ICA) fitness modules, antimicrobial-resistance (AMR) catalogs, and functional annotations. [src: amr_cofitness_networks] The analysis found extensive AMR support networks and functional enrichment, but it explicitly leaves direct co-regulation versus shared dispensability unresolved. [src: amr_cofitness_networks]

## What the networks show

Among 801 AMR genes with fitness data, 769 (96%) had at least one extra-operon cofitness partner at |r| > 0.3. [src: amr_cofitness_networks] The dataset contained 180,370 total cofitness partners, of which 179,375 were extra-operon, with only 0.6% excluded as near-operon pairs. [src: amr_cofitness_networks] Mean support-network sizes were 233 genes at |r| > 0.3, 110 at |r| > 0.4, and 71 at |r| > 0.5. [src: amr_cofitness_networks]

These associations are compatible with shared regulation, but they are also compatible with genes responding similarly to environmental conditions without being directly co-regulated. [src: amr_cofitness_networks] In particular, genes can share condition-responsive fitness patterns because both are dispensable in one condition and more important in another, even when no common transcription factor or signaling pathway directly controls them. [src: amr_cofitness_networks]

The ICA result provides a related but distinct form of evidence: AMR-containing modules had a median of 46 genes versus 27 genes in non-AMR modules, with Mann–Whitney U-test p = 1.7×10⁻⁸. [src: amr_cofitness_networks] This supports structured, condition-dependent organization of fitness phenotypes, but module membership alone does not identify the molecular regulatory mechanism producing that organization. [src: amr_cofitness_networks]

## Why enrichment is not proof of co-regulation

Using [[entities/interproscan]] Gene Ontology annotations, the analysis found enrichment for flagellum-dependent cell motility in 5 organisms with mean odds ratio (OR) 4.7, flagellum assembly in 5 organisms with mean OR 5.3, bacterial-type flagellum in 4 organisms with mean OR 4.9, flagellum-dependent swarming in 4 organisms with mean OR 5.0, histidine biosynthesis in 3 organisms with mean OR 5.3, and tryptophan biosynthesis in 3 organisms with mean OR 5.3. [src: amr_cofitness_networks] These enrichments could indicate shared regulatory or signaling architecture, but they could also reflect categories that are jointly unnecessary under the laboratory conditions used to measure fitness. [src: amr_cofitness_networks]

Fitness Browser experiments generally use shaken liquid culture, where flagella and chemotaxis may be unnecessary, and often use rich or defined media with amino acid supplements, where biosynthesis may be redundant. [src: amr_cofitness_networks] AMR genes are likewise expected to be dispensable when antibiotics are absent. [src: amr_cofitness_networks] The resulting shared dispensability can generate correlated condition-dependent fitness profiles without establishing direct co-regulation. [src: amr_cofitness_networks]

Evidence favoring the shared-dispensability interpretation includes enrichment for categories expected to be dispensable in shaken-flask culture and the absence of energy-metabolism enrichment in 0/25 organisms in a permutation test with fold 0.91. [src: amr_cofitness_networks] That permutation matched conservation class but not mean fitness level, so it does not fully distinguish shared dispensability from shared regulation. [src: amr_cofitness_networks]

The annotation contrast reinforces that detectability of enrichment depends on representation quality rather than establishing mechanism. [src: amr_cofitness_networks] The old SEED/KEGG analysis found 0/280 significant enrichment tests at FDR (false discovery rate) < 0.05, whereas [[entities/interproscan]] Gene Ontology analysis found 35/3,193 significant tests. [src: amr_cofitness_networks] InterProScan provided 68% gene coverage, reported as 3.6× better than the old SEED annotations. [src: amr_cofitness_networks]

## Organism-specific structure is not the same as shared regulation

Support-network organization was more organism-specific than mechanism-specific: the mean Jaccard similarity of Gene Ontology terms was 0.375 for cross-mechanism comparisons within the same organism and 0.207 for within-mechanism comparisons across organisms, with Mann–Whitney U-test p = 4.3×10⁻¹³. [src: amr_cofitness_networks] This supports the interpretation that each organism’s regulatory, metabolic, and signaling architecture shapes its AMR support networks more strongly than resistance-mechanism class. [src: amr_cofitness_networks]

However, organism-specific network structure does not by itself prove direct co-regulation. [src: amr_cofitness_networks] Organism-specific media responses, metabolic dependencies, conditionally dispensable functions, and regulatory architecture could all contribute to the observed pattern. [src: amr_cofitness_networks] Thus, the result strengthens the claim that cofitness is biologically structured, while leaving the causal source of that structure open. [src: amr_cofitness_networks]

The conserved core across mechanisms included transmembrane transport in 87–100% of organisms, signal transduction in 87–100%, transcription regulation in 96–100%, and phosphorelay signaling in 91–100%. [src: amr_cofitness_networks] Flagellar motility occurred in 53–61% of organisms and amino acid biosynthesis in 30–73%. [src: amr_cofitness_networks] These recurring categories are consistent with common regulatory or physiological responses, but their recurrence is not sufficient to demonstrate that the AMR genes and support genes share direct regulatory control. [src: amr_cofitness_networks]

The annotation comparison strengthened the organism-specificity result without resolving the co-regulation question: within-mechanism Jaccard similarity increased from 0.069 with old KEGG annotations to 0.207 with InterProScan Gene Ontology, while cross-mechanism similarity increased from 0.249 to 0.375. [src: amr_cofitness_networks] The cross-mechanism-versus-within-mechanism comparison had p = 1.0 with old KEGG annotations and p = 4.3×10⁻¹³ with InterProScan Gene Ontology. [src: amr_cofitness_networks]

## Analytical limits on causal interpretation

The reported Pearson correlation removes each gene’s mean fitness before correlating fitness profiles, so uniformly slightly positive fitness values alone would produce zero correlation. [src: amr_cofitness_networks] Nevertheless, genes with similar condition-dependent changes in dispensability can still have high cofitness without direct co-regulation. [src: amr_cofitness_networks]

Missing fitness values were treated as zero in z-score space through `np.nan_to_num`, which approximates but does not equal pairwise-complete Pearson correlation. [src: amr_cofitness_networks] The report considers the dense Fitness Browser matrices unlikely to substantially alter the conclusions, but this preprocessing remains a limitation when interpreting individual edges as biological relationships. [src: amr_cofitness_networks]

The null relationship between support-network size and AMR fitness cost also does not establish independence between cofitness and regulation. [src: amr_cofitness_networks] Network size was not correlated with AMR gene fitness cost, with Spearman rho = −0.006, p = 0.87, and N = 769. [src: amr_cofitness_networks] Within mechanisms, correlations were rho = −0.049 for efflux, rho = +0.038 for enzymatic resistance, and rho = −0.031 for metal resistance, with all p > 0.4. [src: amr_cofitness_networks] The report also states that the uniform resistance cost was +0.086 and was not explained by co-regulatory-neighborhood size. [src: amr_cofitness_networks]

This null result may reflect insufficient variance in fitness cost across genes, so it should not be treated as evidence that network connectivity has no regulatory or physiological relevance. [src: amr_cofitness_networks]

## Relation to condition-specific fitness

This concept refines [[concepts/condition-specific-fitness]]: cofitness networks may capture condition-specific shared dispensability rather than direct co-regulation. [src: amr_cofitness_networks] It also complements [[concepts/cofitness-network-architecture]], where the size and organization of networks can be described without assigning a regulatory mechanism to every edge. [src: amr_cofitness_networks] Interpretation should remain connected to [[concepts/gene-essentiality]], because essentiality and dispensability are measured in particular genetic and environmental contexts rather than as universal properties of genes. [src: amr_cofitness_networks]

## Open Directions

- Recompute AMR cofitness against random non-AMR genes matched to the same mean-fitness distribution, including the −0.05 to +0.05 range proposed in the report, and test whether flagellar and amino-acid-biosynthesis enrichment persists after mean-fitness matching. [src: amr_cofitness_networks]
- Partition fitness matrices into antibiotic-exposure and standard-growth conditions, then test whether support-network edges and functional enrichment are condition-specific or persist across both regimes. [src: amr_cofitness_networks]
- Compare direct regulatory evidence, such as shared transcription-factor targets or condition-specific expression responses, with cofitness edges to ask what fraction of high-|r| associations have independent support for co-regulation. [src: amr_cofitness_networks]
- Recalculate networks at |r| > 0.4 and |r| > 0.5, using coordinate-based operon exclusion rather than matrix row position, and test whether the organism-specificity and enrichment results remain stable. [src: amr_cofitness_networks]
- Measure mean fitness for flagellar knockouts and other conditionally dispensable gene classes under the same experimental conditions, then test whether their fitness profiles explain the AMR-neighborhood enrichment without invoking direct co-regulation. [src: amr_cofitness_networks]
