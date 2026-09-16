<!-- tension-hash: bc62c0e9aeb9992e -->
# Marker Definition Versus Ecological Finding: Four Disagreements Over What a Functional Marker Licenses

This page records four related but distinct disagreements surfaced under the `## Tensions` heading of [[concepts/functional-marker-validation]]. Each turns on the same underlying question — how much ecological interpretation a gene-based marker can carry — but each fails in a different way: a marker substitution that reverses a cohort narrative, two projects naming the same retained signal differently, a multivariate effect size whose denominator is disputed, and a reannotation that improves descriptions without establishing function. They matter because in every case the *statistics* are not in dispute; what is in dispute is what the measured quantity is a measurement *of*. Resolving them by averaging numbers or by preferring the newer report would destroy exactly the information that makes them useful. All four are covered below; none are deferred.

## Evidence Sides

### 1. Iron reduction: shallow enrichment versus no cohort difference

**Side A — the original shallow-enrichment narrative.** The original analysis supported a shallow-enrichment narrative for iron reduction. [src: bacillota_b_subsurface_accessory] Its iron-reduction markers were the KEGG Orthology identifiers K07811, K17324, and K17323 — KEGG Orthology (KO) being a controlled vocabulary of gene-function groups. [src: bacillota_b_subsurface_accessory]

**Side B — the corrected detector finds nothing.** The corrected detector found no significant deep-versus-shallow, deep-versus-baseline, or shallow-versus-baseline difference. [src: bacillota_b_subsurface_accessory] The disagreement is attributable to marker definition rather than to silently reconciling numerical results: K07811, K17324, and K17323 were replaced by PFAM and motif-based signals — PFAM is a protein-family domain database — and the resulting cohort counts and tests changed. [src: bacillota_b_subsurface_accessory]

**Side B′ — the correction's own stated limit.** The correction is considered robust for the multi-heme cytochrome signal but remains a Phase 1 correction that does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained. [src: bacillota_b_subsurface_accessory] This is a partial dissent from Side B rather than a return to Side A: it concedes the reversal of the iron-reduction result while leaving the downstream ecological comparison unadjudicated.

### 2. "Sulfite reduction" versus dissimilatory "sulfate reduction"

**Side A — sulfite reduction.** The existing source describes the retained signal as "sulfite reduction." [src: bacillota_b_subsurface_accessory]

**Side B — dissimilatory sulfate reduction.** The new clay report describes it as dissimilatory "sulfate reduction." [src: clay_confined_subsurface]

**What is not in dispute.** Both report 5/9 positives and the same null scale, but the terminology is not identical. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] Because sulfate reduction and sulfite reduction are different steps of the same dissimilatory pathway, the shared count cannot by itself establish that the two labels denote the same marker set; this requires verification against the underlying marker definitions and source tables rather than silently treating the labels as interchangeable. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface]

### 3. Conditional db-RDA variance versus total environmental effect

**Side A — the conditional result.** Conditioning on batch and project effects produced R² = 0.799 and p = 0.005 with 999 permutations in a db-RDA — distance-based redundancy analysis, an ordination method that regresses a community dissimilarity matrix on explanatory variables. [src: soil_metal_functional_genomics]

**Side B — the unconditional effect is unknown.** The unconditional R² for metals alone was not reported and may be substantially lower. [src: soil_metal_functional_genomics] This does not contradict the conditional result; it **refines** what that result can support, because the reported value describes residual variance after project accession was removed rather than necessarily total community COG variance — COG being the Clusters of Orthologous Groups functional classification. [src: soil_metal_functional_genomics]

**A second, related dispute inside the same project.** The 2,355 discoveries among 3,915 implied tests represent a 60% discovery rate, but co-contamination may make tests non-independent and the true FDR may be higher than reported — FDR is the false discovery rate, the expected fraction of significant calls that are false positives. [src: soil_metal_functional_genomics]

### 4. Annotation coverage versus functional certainty

**Side A — annotation has largely closed the gap.** 33,105 of 39,532 pangenome-linked dark genes received non-hypothetical Bakta descriptions — "dark genes" being genes without established function, and Bakta being a genome annotation tool. [src: functional_dark_matter]

**Side B — descriptions are not markers.** The report still treats pathway, domain, module, and environmental links as hypotheses requiring validation. [src: functional_dark_matter] This **refines** rather than overturns the principle of [[concepts/functional-marker-validation]]: broader annotation improves candidate identification, but a database product description is not equivalent to a biologically specific ecological marker. [src: functional_dark_matter]

## Possible Reconciliations

These are hypotheses, not established findings.

**Disagreement 1.** The most parsimonious hypothesis is that the two sides measure different molecular quantities and are both internally valid: the original cohort pattern may be a real distributional difference in the genes K07811, K17324, and K17323 actually represent, while the corrected result is a real null for PFAM- and motif-defined multi-heme cytochrome content. [src: bacillota_b_subsurface_accessory] Under this hypothesis nothing was miscomputed and only the *label* on the original axis was wrong, which would explain why the correction is described as robust for the multi-heme cytochrome signal yet leaves the Bagnoud porewater comparison undetermined. [src: bacillota_b_subsurface_accessory] A weaker alternative hypothesis is a power difference: replacing one marker family with another changed the cohort counts, and a null after replacement need not be evidence of equality. [src: bacillota_b_subsurface_accessory]

**Disagreement 2.** The hypothesis that makes both labels correct is a definitional one: the two reports may be naming different members of one marker panel — an upstream sulfate-activating step and a downstream sulfite-reducing step — which would produce identical genome-level positivity because the same 5/9 genomes carry both. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] A competing hypothesis is that one report inherited the other's counts while re-describing them; the shared 5/9 and shared null scale are equally consistent with genuine agreement and with propagation. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] Only the marker definitions and source tables distinguish these.

**Disagreement 3.** Both statements can hold if R² = 0.799 is read strictly as a share of *residual* variance after project accession was removed, not as total community COG variance. [src: soil_metal_functional_genomics] The hypothesis is then that metals explain a large fraction of a small remainder — the number is not wrong, only over-read. For the discovery-rate half, the hypothesis is that co-contamination induces correlation among metals such that 2,355 of 3,915 tests are not 3,915 independent opportunities, inflating apparent discovery without any single test being miscalculated. [src: soil_metal_functional_genomics]

**Disagreement 4.** Both sides are compatible if annotation coverage and functional specificity are treated as separate axes: 33,105 of 39,532 genes can gain non-hypothetical descriptions while the pathway, domain, module, and environmental links built on them remain hypotheses. [src: functional_dark_matter] The hypothesis here is that the 83.7%-scale improvement is a gain in *candidate prioritization* and not in *validated function*, so no reconciliation beyond keeping the two axes distinct is required. [src: functional_dark_matter]

## Resolving Work

**Disagreement 1 — iron reduction.**
- Re-run the cohort comparison with the original KOs and the corrected PFAM/motif detector side by side on the identical genome set, reporting both cohort count tables, to establish whether the reversal is a change of measurand or a change of power. [src: bacillota_b_subsurface_accessory]
- Complete the Phase 1 correction into a full re-adjudication of the clay-project comparison with the Bagnoud porewater pattern, stating explicitly which part of that comparison survives on the corrected iron-reduction side. [src: bacillota_b_subsurface_accessory]
- Assay iron reduction physiologically in a subset of deep and shallow isolates, so that a marker-based null can be checked against phenotype rather than against another marker set. [src: bacillota_b_subsurface_accessory]
- Report the detection rates of K07811, K17324, and K17323 as the transporter and reductase functions they actually encode, to determine whether the original cohort pattern is a real but differently-named signal. [src: bacillota_b_subsurface_accessory]

**Disagreement 2 — sulfite versus sulfate.**
- Diff the two projects' marker definition tables gene-by-gene and publish the intersection, resolving whether "sulfite reduction" and dissimilatory "sulfate reduction" name the same panel. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface]
- Verify that the 5/9 positives are the same nine genomes and the same five positives in both reports, rather than equal counts over different cohorts. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface]
- Recompute the null under each definition separately and confirm that "the same null scale" reflects an identical null model rather than two similar ones. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface]
- Fix one canonical term for the retained signal across both projects and propagate it, so the shared count stops appearing under two names.

**Disagreement 3 — db-RDA scope and discovery rate.**
- Report the unconditional db-RDA R² for metals alone on the same data, alongside the conditional R² = 0.799 with p = 0.005 and 999 permutations, so readers can see both quantities. [src: soil_metal_functional_genomics]
- Run a variance-partitioning decomposition separating metal-only, project-only, and shared components, which directly answers what fraction of total community COG variance metals explain. [src: soil_metal_functional_genomics]
- Re-estimate FDR over the 3,915 implied tests under a dependence-tolerant procedure, or by permutation preserving the metal correlation structure, to test whether the 60% discovery rate survives non-independence from co-contamination. [src: soil_metal_functional_genomics]
- Quantify the inter-metal correlation matrix and report how many of the 2,355 discoveries are unique to a single metal after conditioning on its co-contaminants. [src: soil_metal_functional_genomics]

**Disagreement 4 — annotation versus function.**
- Sample the 33,105 genes with non-hypothetical Bakta descriptions and score what fraction of descriptions are biologically specific enough to serve as ecological markers, versus generic family or domain labels. [src: functional_dark_matter]
- For a prioritized subset, test the pathway, domain, module, and environmental links experimentally, converting a stated hypothesis class into a measured validation rate. [src: functional_dark_matter]
- Compare the 33,105 annotated against the remaining genes of the 39,532 pangenome-linked dark set for systematic differences, to check whether annotation coverage is biased toward genes that were already interpretable. [src: functional_dark_matter]
