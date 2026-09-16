<!-- tension-hash: 95ccf0a395bea2a0 -->
# Does `is_core` Mean ≥95% Prevalence or Majority Presence?

The corpus does not describe the pangenome "core" gene flag consistently. The pangenome tables and the antimicrobial-resistance fitness-cost analysis describe core as a ≥95% prevalence threshold [src: pitfalls; amr_fitness_cost], while the structural-annotation analysis describes `is_core` as presence in the majority of genomes within each species clade [src: alphafold_msa_annotation]. The evidence does not show whether these are two different thresholds or two descriptions of one flag. This matters because statements about gene conservation (whether a gene belongs to the core shared by nearly all genomes of a species or to the variable accessory set) are only comparable across projects if they use the same boundary. That boundary already sits at the centre of [[concepts/pangenome-core-boundary-and-clade-size-bias]].

## Evidence Sides

**Side A: core means ≥95% prevalence**
The pangenome tables and the antimicrobial-resistance (AMR) fitness-cost analysis both use a ≥95% prevalence threshold for core genes. [src: pitfalls; amr_fitness_cost] Under this reading, a gene cluster is core only if it is present in at least that share of a species' genomes.

**Side B: core means majority presence**
The structural-annotation analysis describes `is_core` as presence in the majority of genomes within each species clade. [src: alphafold_msa_annotation] Read literally, this is a looser criterion than Side A's threshold.

**Unresolved status**
The evidence does not resolve whether this reflects a different threshold or a loose description of the same flag. Conservation statements from these projects should therefore not be pooled without checking the definition. [src: alphafold_msa_annotation; pitfalls]

## Possible Reconciliations

- **Hypothesis 1 (loose wording):** The structural-annotation project may have read the same `is_core` column as the other projects and paraphrased it imprecisely as "majority". If so, its results share Side A's boundary and the disagreement is only one of description.
- **Hypothesis 2 (different operational definition):** That project may have derived or recomputed a core label with a majority cutoff instead of using the stored flag. If so, its core set could differ from one defined by Side A's threshold, and its core-versus-accessory contrasts would not be directly comparable to those using that threshold.
- **Hypothesis 3 (mixed usage):** Some steps may have used the stored flag and others a majority-based summary. If so, each result would need to be checked separately to establish which definition it rests on.

## Resolving Work

- **Data:** the structural-annotation project's notebooks and queries. **Method:** trace whether core labels come directly from the stored `is_core` column or are recomputed from genome counts. **Question:** which definition do its core-versus-accessory results actually use?
- **Data:** the pangenome `gene_cluster` table. **Method:** for each species, compute observed prevalence of clusters flagged `is_core` and compare it with the ≥95% threshold and with a majority cutoff. **Question:** does the stored flag behave as Side A states?
- **Data:** the structural-annotation project's core-versus-accessory comparisons. **Method:** rerun them under both a ≥95% and a majority definition. **Question:** do its conclusions change with the definition, so that pooling with Side A projects is unsafe?
- **Data:** species clades with few genomes in the pangenome tables. **Method:** tabulate how many clusters change classification between the two definitions as clade size varies. **Question:** is any definitional mismatch amplified where clade-size bias is already a concern?
