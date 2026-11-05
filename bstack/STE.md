# Simplified Technical English for bstack output

## Rules

- One idea per sentence. Do not join two ideas with "and", "but", ", which", ", so" or a semicolon. Write two sentences.
- Max 20 words per sentence.
- Use the active voice: "The job deletes old rows", not "Old rows are deleted".
- Put a condition first. Start it with "If": "If the value is empty, the filter skips it."
- Write in one language. Use English, unless the skill or the user names another language. Do not mix in words from another language. This includes team jargon.
- Use the code's names for things. Always use the same name. Do not use synonyms.
- Name a method with its class the first time: `InvoiceService.CreateAsync`, not `CreateAsync`. A method name alone often does not say what it acts on.
- Make each class, method or file name a clickable `file:///` link to its definition the first time it appears.
- Use plain, common words with one meaning: "paginates", not "pages".
- Do not use jargon like "predicate", "navigation", "materialize" or "entity". If you must use a term, explain it in a few words.
- Give a label like "pipeline" a few-word explanation in brackets: "the import pipeline (reads the CSV, validates rows, saves them)".
- Do not write "handles" or "processes" alone. Say what the code does and what it returns.
- Do not use filler or hedging words like "probably" or "basically". Mark an unchecked claim with "(not checked)".
- Use lists, not paragraphs.

## Examples

- Bad: "The export skips empty rows, which makes the file smaller."
  Good: "The export skips empty rows. This makes the file smaller."
- Bad: "Rows that are older than a year are removed by the job, and the rest are kept."
  Good: "The job removes rows older than a year. It keeps the other rows."

## Before sending

Check each sentence of your output:
1. Does it hold two ideas? Split it.
2. Is it longer than 20 words? Shorten it or split it.
3. Is it passive? Make it active.
4. Does it use jargon, a vague label or a word from another language? Replace it.
