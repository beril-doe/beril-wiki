---
type: "Research direction"
description: "Within E. coli carriers, is Crohn's disease association concentrated in strains carrying iron-siderophore or genotoxin clusters, and do those strains show the adherent-invasive phenotype that the marker genes only suggest?"
hypothesis: "Among carriers, CD association tracks strain content (pks, Yersiniabactin, Enterobactin) more than E. coli abundance. Marker-positive isolates are enriched for adherent-invasive behaviour in cell assays, and marker-negative isolates are not."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Carriage counts and cluster enrichments exist, but strain-resolved marker calls need new read-level work and phenotype assays need new measurements."
collections: ["kbase-ke-pangenome"]
findings: ["ibd_phage_targeting--446eca8c", "ibd_phage_targeting--6d9fa20c"]
conflicts: []
papers: ["35359974", "28130329", "41606218"]
builds_on: ["findings/ibd_phage_targeting--446eca8c", "findings/ibd_phage_targeting--6d9fa20c"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Is the Crohn's E. coli signal carried by siderophore- and genotoxin-bearing strains?

Within E. coli carriers, is Crohn's disease association concentrated in strains carrying iron-siderophore or genotoxin clusters, and do those strains show the adherent-invasive phenotype that the marker genes only suggest?

## Hypothesis

Among carriers, CD association tracks strain content (pks, Yersiniabactin, Enterobactin) more than E. coli abundance. Marker-positive isolates are enriched for adherent-invasive behaviour in cell assays, and marker-negative isolates are not.

## Why it matters

E. coli was detected in only 8 of 23 UC Davis CD patients (35%), so species-level depletion may be unwarranted. Strain-level targeting would change which patients get an E. coli phage cocktail.

## How to test it

Step 1, lakehouse: in the HMP2 cohort, which has CD and non-IBD subjects, call marker genes in E. coli reads and test CD association separately in carriers with and without markers, using E. coli genome gene content to check marker co-occurrence. Step 2, experiment: for UC Davis isolates (all CD, so used for phenotype and carriage exemplars only, not a CD-versus-control contrast), run adhesion/invasion assays alongside marker typing. Tier-A cluster enrichment (iron_siderophore OR 44.4, FDR 6.5e-56; genotoxin_microcin OR 234.0, FDR 3.3e-35) only motivates the hypothesis. The comparator was the full 10,060-cluster catalog, so the 44× iron OR is partly inflated by background rarity (51 / 9,774 = 0.5 %) and is not a precise effect size.

## What would support or refute it

Support: CD association is present in marker-positive carriers and absent in marker-negative ones, and marker status predicts the invasive phenotype. Refutation: both strata are equally CD-associated, or markers do not predict the phenotype. Marker-negative null results cannot show that non-AIEC strains lack association, since marker status is only a proxy for AIEC. The small 23-patient cohort supplies exemplars, not robust validation.

## Data

Approach: analysis then experiment. Readiness: needs compute. Carriage counts and cluster enrichments exist, but strain-resolved marker calls need new read-level work and phenotype assays need new measurements.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/ibd_phage_targeting--446eca8c|Tier-A core gene clusters are enriched for iron-siderophore and genotoxin themes]] (Insufficient literature evidence)
- Finding: [[findings/ibd_phage_targeting--6d9fa20c|E. coli is rarer in this Crohn's cohort than AIEC literature implies]] (Extends retrieved work)

## Closest published work

- [PMID 35359974](https://pubmed.ncbi.nlm.nih.gov/35359974/) Prevalence, Abundance, and Virulence of Adherent-Invasive Escherichia coli in Ulcerative Colitis, Colorectal Cancer, and Coeliac Disease.
- [PMID 28130329](https://pubmed.ncbi.nlm.nih.gov/28130329/) Bacteriophages Targeting Adherent Invasive Escherichia coli Strains as a Promising New Treatment for Crohn's Disease.
- [PMID 41606218](https://pubmed.ncbi.nlm.nih.gov/41606218/) From niche to niche: investigating microbial communities and their specialised metabolite gene clusters in human microbiomes.

PMID 35359974 reports AIEC prevalence by disease group and PMID 28130329 proposes AIEC-targeting phages; neither tests marker-stratified CD association within carriers in a metagenome cohort.
