---
type: "Dataset"
description: "PubMed article records held as kescience_pubmed."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md"]
aliases: ["kescience_pubmed"]
---
# PubMed

PubMed here means the PubMed article records held in the KBase Data Lakehouse as the database kescience_pubmed. The inventory lists 39,994,988 PubMed article records. [src: berdl_data_atlas]

## Key facts

- The inventory lists 39,994,988 PubMed article records in the [[entities/kbase-data-lakehouse|KBase Data Lakehouse]]. [src: berdl_data_atlas]
- The table pubmed_article_wide in kescience_pubmed supplies the 40M PubMed records. [src: berdl_data_atlas]
- The platform summary also gives 40M PubMed records, alongside reference layers that are all queryable from one Spark cluster. [src: berdl_data_atlas]

## Use

For literature questions, the report recommends kescience_paperblast together with kescience_pubmed, joined via pmid / doi. [src: berdl_data_atlas] The cross-project digest describes kescience_pubmed as supporting literature text mining and as a sibling of kescience_paperblast (see [[entities/paperblast]]). [src: discoveries]

## Related pages

See [[summaries/berdl_data_atlas__REPORT]], [[summaries/discoveries]] and [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]] for the platform context.
