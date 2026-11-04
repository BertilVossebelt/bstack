---
name: bstack-orient
description: Explains the code around a ticket before any decision is made. Gives a short rundown in Simplified Technical English with file:line links, so the user can read the code with a map in mind. Step 2 of the ticket flow. Use after /bstack-ticket, before /bstack-decide.
---

# /bstack-orient

Give the user a map of the code that a ticket touches. The user reads the code. The rundown only tells them where to look and what they will find. Do not write code. Do not edit files. When you are done, wait for the user.

## Investigate (for yourself, not for the output)

- Get the ticket. Follow [TICKET.md](../bstack/TICKET.md).
- Trace the data in the order it moves:
  - Start where it enters: a user action, a request, a job, an event.
  - End where it leaves: a response, a stored row, a file, a page.
  - If the ticket touches both how data is saved and how it is read, trace both.
- Find what each confusing project-specific name means. Use the code, not guesses.
- Read each line again before you cite it.
- Never say that something is missing because a search did not find it.
- Check each claim about behaviour in the code: what fails, what is ignored, what is returned. Do not use comments as proof. If you cannot check a claim, write "(not checked)" after it.

## Output

The user must be able to read it in one minute. Follow this example exactly in shape, length and tone. Each `[line N]` is a clickable `file:///` link.

```
**Terms:**
- export row: one line in the CSV, built from one invoice ([InvoiceExportMapper](link)).

**Path:**
1. [line 40] — `Export` receives an `InvoiceExportRequest`. It holds the filters from the query string ([definition](link)).
2. [lines 42–75] — permission checks and logging. Not needed for this ticket.
3. [line 77] — `Export` sends the query and the request to `ApplyExportFilters`.
4. [line 120] — `ApplyExportFilters` adds one `Where` per filter in the request. The new filter goes here.
5. [line 150] — `Export` caps the result at 10,000 invoices. This keeps one export from loading the whole table.
6. [line 160] — `Export` gives the query to `WriteCsv` (turns each invoice into a row and streams the file).

**Related:**
- [line 131] (step 4) — the `issuedAfter` filter keeps invoices issued after a date. Copy its date check and its empty-value check.
- [line 18] (step 1) — the filter properties on `InvoiceExportRequest`. Add `paidAfter` here.

Read the code along the Path, then run /bstack-decide.
```

### Rules

- **Terms:** only names the user needs to read the Path. One short sentence and one link each. Omit the section if there are none.
- **Path:**
  - Follow the data in the order it moves. Max 7 steps.
  - Start where the data enters. End where it leaves.
  - Never start at a model, a helper or a list of fields.
  - Each step receives what the step before it passed on.
- If the ticket touches both how data is saved and how it is read, split the Path into **Path (save):** and **Path (read):**. Max 6 steps each. The read Path starts where the reader asks for the data, such as a page load or a request.
- A step:
  - Starts with one link. Label the link with its line or range.
  - Then gives max two short sentences about one thing.
  - The range covers only that thing.
- If a step receives or passes data that the ticket uses, say what the data holds.
- If a large block of code sits between two steps, give it its own step. Give a general summary and "Not needed for this ticket."
- If the purpose of a step is not obvious, say why it happens. Examples: it removes, resets or copies something. Use one of the two sentences for the why.
- Say what a step does, not how. Do not quote expressions. Do not mention conversions, null checks or casts.
- Facts outside the flow go in **Related**, or leave them out. Examples: a class that only another feature uses, a rule that already covers the change.
- **Related:**
  - Existing code that the change must follow. Max 4 entries.
  - Say what it is in plain words. Then say what to copy. Max two sentences.
  - Give each entry its step number. Order the entries by step number.
  - If the Path is split, write the step as "(save 2)" or "(read 3)". Put the save entries first.
- Put nothing after **Related** except the closing line. No decisions, proposals or warnings. Those belong in /bstack-decide.

## Simplified Technical English

Write in Simplified Technical English. Read the rules in [STE.md](../bstack/STE.md) before you write. Check your output against them before you send it.

## Before sending

Check each line against the example and the rules. Write a line again if it breaks one. Check these in particular:
- Each label like "pipeline" has its explanation in brackets.
- There is no jargon, such as "entity", "predicate" or "navigation". Use "manually" where it fits, not "itself".
- Each **Related** entry has a step number. The entries follow the Path order.
- Each step with a purpose that is not obvious says why.
- Each name the user has not seen yet comes with what it is.
- Step 1 is where the data enters. Each next step takes what the step before it passed on.
