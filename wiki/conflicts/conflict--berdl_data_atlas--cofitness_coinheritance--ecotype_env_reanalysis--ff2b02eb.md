<!-- tension-hash: 459994d3d70b48a3 -->
# Broad Cross-Collection Bridges vs. Evidentially Validated Use

[[concepts/cross-tenant-data-bridging]] records a conflict between the apparent breadth of cross-tenant integration and the evidence that those connections represent shared authority, biological direction, or realized use. This matters because a technically valid schema join can be mistaken for a validated biological relationship, while sparse documentation can be mistaken for evidence that a bridge is unused.

## Evidence Sides

### **Schema-level connectivity can be broad but weakly evidenced**

The atlas contains 536 schema-level bridges, yet the original audit recorded five high-leverage bridges with zero realized use. UC1 was subsequently sample-executed, while UC2–UC5 remained untested. [src: berdl_data_atlas] The realized-use count is a lower bound because README mining may miss plans and notebooks. [src: berdl_data_atlas] Therefore, “zero documented use” and “zero use” are not equivalent claims. The NMDC audit likewise found that 20 entries resolve to 7 resources, including `kbase.nmdc_neon` as a NEON namesake collision, contradicting the assumption that a catalog prefix, tenant, or name proves common authority. [src: nmdc_context_audit]

### **Some bridges are actionable, but biological interpretation remains uncertain**

The 19-metabolite Fitness Browser bridge is directly actionable, but missing consumption actions mean production cannot be treated as utilization. Meanwhile, 107 formula-only ModelSEED matches expand to 900 candidate molecules. [src: webofmicrobes_explorer] Tryptophan increased in WoM and had 231 significant Fitness Browser genes and a complete GapMind pathway, yet 0/50 *P. fluorescens* strains used it as carbon. [src: fw300_metabolic_consistency] Binary growth was predictable for tryptophan (AUC 0.933), phenylalanine (0.932), and valine (0.927), while continuous phenotypes had negative R². [src: genotype_to_phenotype_enigma]

### **Cross-dataset associations can be real without establishing mechanism**

The prophage study found concordant module-level pangenome and NMDC associations, but annotations came from eggNOG rather than geNomad or VIBRANT; the false-positive rate is uncharacterized. [src: prophage_ecology] Its environmental effect exceeded family-level phylogeny in the reported PERMANOVA, while genome size was dominant (rho=0.717), only 28% of genomes had embeddings, and genus-level NMDC inference assumed conserved prophage content. [src: prophage_ecology] Human-associated environments enriched tail (log2(OR)=2.21), head morphogenesis (1.98), and anti-defense (1.70), but these findings do not demonstrate coevolution. [src: prophage_ecology]

## Possible Reconciliations

- **Hypothesis — documentation scope:** The five bridges may have more realized use than README mining records, so low documented use may reflect incomplete discovery rather than nonuse.
- **Hypothesis — semantic scope:** A schema-level join may correctly link records while leaving chemical identity, biological direction, or utilization unresolved.
- **Hypothesis — authority scope:** Multiple names may resolve to the same resource without implying common governance or provenance.
- **Hypothesis — mechanism scope:** Concordant associations may reflect shared ecology, genome size, annotation artifacts, or domesticated remnants rather than causal interaction.

## Resolving Work

- Execute UC2–UC5 and audit plans, notebooks, and workflows to distinguish genuinely unused bridges from undocumented use.
- Resolve every joined identifier to resource-level provenance and authority, testing whether names, prefixes, and tenants encode actual governance.
- Validate the 107 formula-only matches with structure-level chemical evidence and consumption-action data, asking which 900 candidate molecules are biologically actionable.
- Reannotate prophages with geNomad, VIBRANT, and eggNOG, estimate false-positive rates, and retest environmental associations while controlling for genome size.
- Test predicted metabolite use experimentally across the relevant strains, separating production, uptake, and growth.
