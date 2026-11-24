---
name: wiki-shared
description: Write a plain statement about two to four linked results from different microbial-biology research projects.
---

# Describe shared results

## Tools

- `submit_record(record)` submits one JSON object for the group. Fix any
  objections and submit again. You have three attempts.
- `claims(ids, quotes=true)` and `read_source(source, start, end)` let you
  read claims or report passages again.
- `finish(note)` ends the session.

## Input

`RESULTS` holds two to four findings from different projects that a reviewer
linked, with the project name and each finding's title, claim, evidence quote
and quantities.
`RELATION` says how the findings relate, and `LINKS` gives the labels of the
links between them.

## The record

Submit `{"title": "...", "sentence": "...", "question": "...", "lanes": {"<result id>": "..."}, "how": "..."}`.

- `title` uses 3 to 12 words to name what the projects found.
- `sentence` uses one or two sentences and 3 to 45 words to say what the projects found and why it is interesting.
- `question` uses 3 to 14 words to state the question the projects asked and ends with `?`.
- `lanes` gives 2 to 8 words for each result id naming what that project compared or measured.
- `how` uses at most two sentences and 3 to 50 words to describe how the results relate, following `RELATION`.

## Rules

- Write in plain biological words for a microbiologist who does not read statistics.
- When results report identical figures or one project uses another's data, say they share an analysis or data in both `sentence` and `how`.
- When results reach different conclusions, such as different directions or a pattern that only one finds, say what differs in `title` and `sentence`. Never present them as one result.
- Claim only what the results tested. A comparison of how common genes are does not show what niche they serve.
- Never say or imply the projects confirm, corroborate, validate, reproduce, replicate or agree with each other, or that they are independent.
- Leave out caveats, limitations and “however” clauses, and avoid “novel”, “first” and “breakthrough”.
- Use no statistics. Use only figures the results state. Make no claim about people.
