---
type: "Finding"
description: "Of the 9 species with sufficient plant-host annotation for a subclade \u00d7 host test (\u22655 host-annotated genomes, \u22652 hosts, \u22652 subclades), 2 pass both within-species and across-species Bonferroni: Xanthomonas campestris segregates to Brassica hosts (46/47 genomes in subclade 2) and Xanthomonas vasicola to Zea mays (47/52 in subclade 0)."
finding_id: "plant_microbiome_ecotypes--64143b61"
result: "observation"
source: "plant_microbiome_ecotypes"
quantities: [{"value": "46/47", "what": "X. campestris genomes in subclade 2 that are on Brassica", "unit": "genomes", "denominator": "47 genomes in subclade 2", "scope": "X. campestris"}, {"value": "47/52", "what": "X. vasicola genomes in subclade 0 that are on Zea mays", "unit": "genomes", "denominator": "52 genomes in subclade 0", "scope": "X. vasicola"}, {"value": "2", "what": "species passing both within-species and across-species Bonferroni", "unit": "species", "denominator": "9 species with sufficient host annotation", "scope": ""}]
caveat: "Only 18 (28%) of 65 plant-associated species with \u226520 genomes have any phylogenetic-tree distance data, so the other 47, including several major plant-associated taxa, are absent from this test."
first_added: "2026-10-27"
source_hash: "ab4bafa20bb607a1edf87a293d67885cd96017817bfabdbff2c19bac9dc95272"
---
# Two Xanthomonas species segregate by plant host across subclades

Of the 9 species with sufficient plant-host annotation for a subclade × host test (≥5 host-annotated genomes, ≥2 hosts, ≥2 subclades), 2 pass both within-species and across-species Bonferroni: Xanthomonas campestris segregates to Brassica hosts (46/47 genomes in subclade 2) and Xanthomonas vasicola to Zea mays (47/52 in subclade 0). [src: plant_microbiome_ecotypes]

## Key figures

- **46/47 genomes**: X. campestris genomes in subclade 2 that are on Brassica (denominator 47 genomes in subclade 2; scope X. campestris) [src: plant_microbiome_ecotypes]
- **47/52 genomes**: X. vasicola genomes in subclade 0 that are on Zea mays (denominator 52 genomes in subclade 0; scope X. vasicola) [src: plant_microbiome_ecotypes]
- **2 species**: species passing both within-species and across-species Bonferroni (denominator 9 species with sufficient host annotation) [src: plant_microbiome_ecotypes]

## Evidence

> **Canonical Phase 2b finding (H6, layered on the same scan)**: of the 9 species with sufficient plant-host annotation for a subclade × host test (≥5 host-annotated genomes, ≥2 hosts, ≥2 subclades), **2 species pass both within-species and across-species Bonferroni**: *Xanthomonas campestris* segregates to Brassica hosts (46/47 genomes in subclade 2 are on Brassica, p = 2.7×10⁻¹² raw, 3.3×10⁻¹¹ after within-species pair-search Bonferroni) and *Xanthomonas vasicola* segregates to *Zea mays* (47/52 in subclade 0, p = 1.4×10⁻¹¹ / 1.7×10⁻¹⁰). [src: plant_microbiome_ecotypes]

From the report [[summaries/plant_microbiome_ecotypes__REPORT]].

## Caveat

Only 18 (28%) of 65 plant-associated species with ≥20 genomes have any phylogenetic-tree distance data, so the other 47, including several major plant-associated taxa, are absent from this test. [src: plant_microbiome_ecotypes]

> of 65 plant-associated species with ≥20 genomes, only **18 (28%) have any phylogenetic-tree distance data** in `kbase_ke_pangenome.phylogenetic_tree_distance_pairs` — the other 47 (including major plant-associated taxa *Bradyrhizobium japonicum*, *B. diazoefficiens*, *Mesorhizobium ciceri*, *Sinorhizobium medicae*, *Burkholderia glumae*, *Methylobacterium extorquens*, *Streptomyces scabiei*, *Xylella taiwanensis*, *Clavibacter michiganensis*) are absent from the tree, a database-coverage limitation now documented in `docs/pitfalls.md`. [src: plant_microbiome_ecotypes]

## Other caveats in this report

- The original compartment PERMANOVA R² = 0.527 was largely a taxonomic-sampling artifact: excluding three dominant species reduced it to 0.072, although the reported per-marker enrichments persisted. The stated compartment counts do not sum to 1,136 and should not be silently reconciled. [src: plant_microbiome_ecotypes]
- The proposed purifying-selection explanation is an interpretation of mixed proxy evidence, not a direct demonstration of selection. [src: plant_microbiome_ecotypes]
- Co-occurring plant-associated genera show a small redundancy signal. The earlier extreme Cohen’s d = −7.54 largely resulted from using the SD of permutation means instead of the raw pair-level SD; corrected analyses yield about −0.4. [src: plant_microbiome_ecotypes]
- The reduction in COG3569 odds ratio from 8.92 to 6.01 indicates partial phylogenetic confounding. [src: plant_microbiome_ecotypes]
- NB02 classified 15,474/25,660 species (60.3%) as dual-nature by binary marker presence; NB07's weighted composite scheme classified 25.2% as dual-nature. The passage establishes different classification definitions but does not give an NB07 denominator. [src: plant_microbiome_ecotypes]
