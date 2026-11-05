---
name: bstack-orient
description: Explains the code around a ticket before any decision is made. Gives a short rundown in Simplified Technical English with file:line links, so the user can read the code with a map in mind. Step 2 of the ticket flow. Use after /bstack-ticket, before /bstack-decide.
---

# /bstack-orient

Give the user a map of the code that a ticket touches. The user reads the code. The rundown only tells them where to look and what they will find. Do not write code. Do not edit files. When you are done, wait for the user.

## Investigate (for yourself, not for the output)

- Get the ticket. Follow [TICKET.md](../bstack/TICKET.md).
- Read the notes file and add the user's answers since the last step. Follow [NOTES.md](../bstack/NOTES.md).
- Trace the data in the order it moves. Trace only the part of the flow that the change touches:
  - If the ticket changes the flow itself, start where the data enters (a user action, a request, a job, an event). End where it leaves (a response, a stored row, a file, a page).
  - If the ticket only adds to or changes one part of an existing flow, start at the first step the change depends on. End at the last step that sees the new data.
  - If the ticket touches both how data is saved and how it is read, trace both.
- Find what each confusing project-specific name means. Use the code, not guesses.
- Read each line again before you cite it.
- Never say that something is missing because a search did not find it.
- Check each claim about behaviour in the code: what fails, what is ignored, what is returned. Do not use comments as proof. If you cannot check a claim, write "(not checked)" after it.

## Output

The user must be able to read it in 30 seconds. Short beats complete: leave out what the user does not need for this ticket. Follow this example exactly in shape, length and tone. Each `[line N]` and each `(link)` is a clickable `file:///` link with an absolute path.

```
**Trigger:** An accountant downloads the invoice export ([`InvoiceController.Export`](link)).

**Where:** The Path covers how the filters get into the database query. It starts in [`InvoiceExportService.Export`](link), which runs for each export download.

**Terms:**
- export row: one line in the CSV, built from one invoice ([InvoiceExportMapper](link)).

**Path:**
1. [line 40] — [`InvoiceExportService.Export`](link) receives an `InvoiceExportRequest` with the filters from the query string ([definition](link)).
2. [line 77] — `Export` sends the query and the request to [`InvoiceQueryBuilder.ApplyExportFilters`](link).
3. [line 120] — `ApplyExportFilters` adds one `Where` per filter in the request. The new filter goes here.
4. [line 150] — `Export` caps the result at 10,000 invoices. This keeps one export from loading the whole table.

**Related:**
- [line 18] (step 1) — the filter properties on `InvoiceExportRequest`. Add `paidAfter` here.
- [line 131] (step 3) — the `issuedAfter` filter keeps invoices issued after a date. Copy its date check and its empty-value check.

Read the code along the Path, then run /bstack-decide.
```

### Rules

- **Trigger:** one short sentence before **Where**. Say what makes the flow run, as an event the user knows: an order is created, a user saves a page, a job runs at night. Put the code name of the entry point (a route, a job, an event handler) in brackets, if at all. Never give only code names.
- **Where:** max 2 short sentences. Say which part of the flow the Path covers. Then name the code where step 1 starts, and link it to the trigger.
- **Terms:** only names the user cannot follow the Path without. Max 2. One short sentence and one link each. Omit the section if there are none.
- **Path:**
  - Follow the data in the order it moves. Max 5 steps. Fewer is better.
  - Cover only the part of the flow that the change touches (see **Investigate**).
  - Never start at a model or a list of fields.
  - Each step receives what the step before it passed on.
- If the ticket touches both how data is saved and how it is read, split the Path into **Path (save):** and **Path (read):**. Max 4 steps each. The read Path starts where the reader asks for the data, such as a page load or a request.
- A step:
  - Starts with one link. Label the link with its line or range.
  - Then gives one short sentence about one thing. Add a second sentence only for where the change goes or for the why.
  - The range covers only that thing.
- If a step receives or passes data that the ticket uses, say what the data holds. Do not name data that the ticket does not use.
- If a large block of code sits between two steps, give it its own step. Give a general summary and "Not needed for this ticket."
- If the purpose of a step is not obvious, say why it happens. Examples: it removes, resets or copies something. Use the second sentence for the why.
- Say what a step does, not how. Do not quote expressions. Do not mention conversions, null checks or casts.
- Facts outside the flow go in **Related**, or leave them out. Examples: a class that only another feature uses, a rule that already covers the change.
- **Related:**
  - Existing code that the change must follow. Max 3 entries.
  - Say what it is in plain words, then what to copy. Max two short sentences.
  - Give each entry its step number. Order the entries by step number.
  - If the Path is split, write the step as "(save 2)" or "(read 3)". Put the save entries first.
- Put nothing after **Related** except the `Notes:` line and the closing line. No decisions, proposals or warnings. Those belong in /bstack-decide.

Write the **Code** section of the notes file: the Trigger and Where lines and the place where the change goes. Follow [NOTES.md](../bstack/NOTES.md). Then add the `Notes:` link line.

## Simplified Technical English

Write in Simplified Technical English. Read the rules in [STE.md](../bstack/STE.md) before you write. Check your output against them before you send it.

## Before sending

Check each line against the example and the rules. Write a line again if it breaks one. Check these in particular:
- Each label like "pipeline" has its explanation in brackets.
- There is no jargon, such as "entity", "predicate" or "navigation". Use "manually" where it fits, not "itself".
- Each **Related** entry has a step number. The entries follow the Path order.
- Each step with a purpose that is not obvious says why.
- Each method is named with its class the first time, also in **Trigger** and **Where**: `InvoiceService.CreateAsync`, not `CreateAsync`.
- Each class, method or file name is a clickable link to its definition the first time it appears, in every section.
- No step says "the method" or "it" for code that the step does not name.
- Each name the user has not seen yet comes with what it is. Leave out a name the ticket does not need.
- **Trigger** is an event the user knows, not a list of code names.
- **Where** names the code of step 1 and links it to the trigger. Step 1 follows from it.
- The Path covers only the part of the flow that the change touches. No step is about code that does not change and that the change does not depend on.
- Each step takes what the step before it passed on.
