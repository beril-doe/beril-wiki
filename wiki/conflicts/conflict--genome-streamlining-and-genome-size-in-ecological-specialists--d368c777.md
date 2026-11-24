<!-- tension-hash: d368c777697e9d69 -->
# Genome Size in Ecological Specialists: Larger Within a Phylum, Smaller Across Genera, and an Unresolved Metal-Gene Signal

Two reports disagree about how genome size relates to ecological specialization, and a second question follows about whether the metal-gene signal is special. Deep-clay Bacillota_B genomes are larger than soil relatives [src: bacillota_b_subsurface_accessory], while across genera specialists have smaller genomes and denser conserved gene sets [src: comprehensive_metal_ecology]. Separately, a coreness-matched permutation test places the overall metal-gene effect (β, a regression coefficient) within the null (emp_p = 0.298, the empirical permutation p-value) [src: comprehensive_metal_ecology], yet the report reads a 30–60% gap from housekeeping genes as a genuine content signal [src: comprehensive_metal_ecology]. The answer decides whether streamlining (genome compaction) can serve as a general explanation for specialists. It also decides whether metal-gene density is evidence of selection. See [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]].

## Evidence Sides

**Side A: specialists have larger genomes (within a phylum)**
- Deep-clay Bacillota_B genomes are larger than soil relatives. [src: bacillota_b_subsurface_accessory]
- This is a within-phylum comparison, so its scope differs from the genus-level analysis. Neither report resolves the difference.

**Side B: specialists have smaller genomes (across genera)**
- Across genera, specialists have smaller genomes and denser conserved gene sets. [src: comprehensive_metal_ecology]
- This is a genus-level niche-breadth analysis (niche breadth is how many environments a taxon occupies). [src: comprehensive_metal_ecology]

**Metal-gene signal: null versus content reading**
- The coreness-matched permutation finds the overall β within the null (emp_p = 0.298). Coreness means how conserved a gene is across genomes. [src: comprehensive_metal_ecology]
- The report reads the 30–60% gap from housekeeping as a genuine content signal. [src: comprehensive_metal_ecology]
- The report says the two address different questions. [src: comprehensive_metal_ecology]

## Possible Reconciliations

- **Hypothesis: scale dependence.** Genome size may track specialization differently within one phylum than across many genera, so both results can hold. This is untested.
- **Hypothesis: different questions.** The permutation null tests overall magnitude, while the 30–60% gap concerns content relative to housekeeping genes. Both readings may be compatible, but the report only asserts this. [src: comprehensive_metal_ecology]
- **Hypothesis: lineage-specific exceptions.** Deep-clay Bacillota_B may be an exception to the cross-genus pattern rather than a contradiction of it. This is untested.

## Resolving Work

- Repeat the genome-size versus niche-breadth regression within other single phyla, using the genus-level method, to ask whether the sign flips at phylum scale.
- Rerun the Bacillota_B comparison with a larger anchor group and a phylogenetically controlled model (for example PGLS, phylogenetic generalized least squares), to ask whether the larger-genome result survives.
- Place Bacillota_B genera in the cross-genus niche-breadth dataset, to ask whether they are outliers from the smaller-genome trend.
- Compare metal-gene β against many coreness-matched null sets, stratified by functional category, to ask whether any category departs from the null even though the overall β does not.
- Test the 30–60% gap from housekeeping genes against a genome-size-matched null, to ask whether it exceeds what compaction alone produces.
