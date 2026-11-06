---
type: "Finding"
description: "Clade size does not predict essentiality rate (rho=-0.13, p=0.36), and essentiality penetrance shows only a weak positive correlation with core fraction (rho=0.123, p=1.6e-17)."
finding_id: "essential_genome--876909a2"
result: "null result"
source: "essential_genome"
quantities: [{"value": "rho=-0.13, p=0.36", "what": "correlation of clade size with essentiality rate", "unit": "", "denominator": "", "scope": ""}, {"value": "rho=0.123, p=1.6e-17", "what": "correlation of essentiality penetrance with core fraction", "unit": "", "denominator": "", "scope": "97.1% core for >80% penetrance vs 92.8% for <20%"}]
caveat: "The 48 Fitness Browser organisms are biased toward culturable Proteobacteria, with uncultured lineages, Actinobacteria and Firmicutes underrepresented."
first_added: "2026-10-27"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# Clade size does not predict essentiality rate; core link weak

Clade size does not predict essentiality rate (rho=-0.13, p=0.36), and essentiality penetrance shows only a weak positive correlation with core fraction (rho=0.123, p=1.6e-17). [src: essential_genome]

## Key figures

- **rho=-0.13, p=0.36**: correlation of clade size with essentiality rate [src: essential_genome]
- **rho=0.123, p=1.6e-17**: correlation of essentiality penetrance with core fraction (scope 97.1% core for >80% penetrance vs 92.8% for <20%) [src: essential_genome]

## Evidence

> Weak positive correlation between essentiality penetrance and core fraction (rho=0.123, p=1.6e-17): families essential in more organisms tend to be slightly more core (97.1% for >80% penetrance vs 92.8% for <20%). Clade size does NOT predict essentiality rate (rho=-0.13, p=0.36). [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

The 48 Fitness Browser organisms are biased toward culturable Proteobacteria, with uncultured lineages, Actinobacteria and Firmicutes underrepresented. [src: essential_genome]

> - **48 organisms is taxonomically limited**: The Fitness Browser organisms are biased toward culturable Proteobacteria. Essentiality patterns in uncultured lineages, Actinobacteria, or Firmicutes are underrepresented. [src: essential_genome]

## Other caveats in this report

- Of the hypothetical essential genes, 3,912 have orthologs and are predictable by this method, while 4,385 are orphan genes that the method cannot predict. [src: essential_genome]
- The report distinguishes its experimentally defined essential set from computationally conserved gene sets by requiring lethal transposon disruption across the tested organisms. [src: essential_genome]
- The report proposes paralogs, alternative pathways, and accessory-genome compensation as explanations for variable essentiality; its broad-spectrum antibiotic-target inference is an interpretation rather than a tested drug-efficacy result. [src: essential_genome]
- Recently acquired genes, rapid evolution, and lineage-specific innovation are proposed—not established—explanations for orphan essentials; the report compares them with 149 of 473 genes (31%) of unknown function in a minimal Mycoplasma genome. [src: essential_genome]
- Essential-gene calls are an upper bound because lack of insertions can reflect small size, AT-rich sequence, or scaffold-edge effects rather than lethality. [src: essential_genome]
