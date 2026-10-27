---
type: "Finding"
description: "Bakta-validated lanmodulin occurred in 62 genomes from 10 species, all 62/62 within Beijerinckiaceae, Acetobacteraceae, or Hyphomicrobiaceae, with a one-sided test against the 80% threshold giving p = 9.8 \u00d7 10\u207b\u2077."
finding_id: "lanthanide_methylotrophy_atlas--d54adcf1"
result: "observation"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "62", "what": "genomes with bakta-validated lanmodulin", "unit": "genomes", "denominator": "", "scope": "10 species"}, {"value": "62 / 62 = 100 %", "what": "lanmodulin genomes in the three pre-specified methylotroph families", "unit": "%", "denominator": "62 lanmodulin genomes", "scope": ""}, {"value": "9.8 \u00d7 10\u207b\u2077", "what": "one-sided binomial p against the 80 % threshold", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 505 eggNOG lanM preferred-name calls were judged false positives concentrated in gut Bacillota, so the report uses bakta product exclusively for lanmodulin detection."
first_added: "2026-10-27"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# Bakta-validated lanmodulin is confined to alpha-Proteobacterial methylotroph families

Bakta-validated lanmodulin occurred in 62 genomes from 10 species, all 62/62 within Beijerinckiaceae, Acetobacteraceae, or Hyphomicrobiaceae, with a one-sided test against the 80% threshold giving p = 9.8 × 10⁻⁷. [src: lanthanide_methylotrophy_atlas]

## Key figures

- **62 genomes**: genomes with bakta-validated lanmodulin (scope 10 species) [src: lanthanide_methylotrophy_atlas]
- **62 / 62 = 100 %**: lanmodulin genomes in the three pre-specified methylotroph families (denominator 62 lanmodulin genomes) [src: lanthanide_methylotrophy_atlas]
- **9.8 × 10⁻⁷**: one-sided binomial p against the 80 % threshold [src: lanthanide_methylotrophy_atlas]

## Evidence

> Bakta-validated `product = 'Lanmodulin'` is detected in **62 genomes** (10 species). Every one of them — **62 / 62 = 100 %** — falls within Beijerinckiaceae, Acetobacteraceae, or Hyphomicrobiaceae, the three α-Proteobacterial methylotroph families pre-specified in H3. One-sided binomial test against the 80 % threshold: **p = 9.8 × 10⁻⁷** — **H3a strongly supported.** [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

The 505 eggNOG lanM preferred-name calls were judged false positives concentrated in gut Bacillota, so the report uses bakta product exclusively for lanmodulin detection. [src: lanthanide_methylotrophy_atlas]

> The 505 eggNOG `Preferred_name='lanM'` "false positives" are concentrated in unrelated gut Bacillota — *Streptococcus pneumoniae* (10), *Blautia_A wexlerae* (9), *Enterococcus faecalis* (8), *Ruminococcus_B gnavus* (8), *Streptococcus pyogenes* (7), and similar — none of them lanthanide users. Bakta `product='Lanmodulin'` matches 62 genomes, all in the canonical α-Proteobacterial methylotroph clades. **For BERDL pangenome lanmodulin work, use bakta product exclusively.** [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- The initial per-phylum binomial framework did not formally control phylogenetic non-independence; the report describes three subsequent validation strategies. [src: lanthanide_methylotrophy_atlas]
- Environmental associations used per-class Fisher exact tests for any xoxF against a generic-environmental reference, with Benjamini–Hochberg correction. [src: lanthanide_methylotrophy_atlas]
- The REE-impacted class had only 37 genomes; its 10.81% xoxF rate and odds ratio 3.51 were descriptive, with adjusted p value 0.082. [src: lanthanide_methylotrophy_atlas]
- The report grades H2 as partially supported: soil/sediment and marine enrichment and host-associated depletion passed its correction, while the n=37 REE-impacted elevation did not pass the false-discovery-rate threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- Of 2,185 genomes with no eggNOG pqq, 1,288 (59%) had at least one bakta PQQ product. The other 897 (24% of all xoxF carriers) lacked evidence in both sources; assembly incompleteness, pseudogenization, and community-acquired PQQ remain unresolved without sequence-level inspection. [src: lanthanide_methylotrophy_atlas]
