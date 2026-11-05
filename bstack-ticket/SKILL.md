---
name: bstack-ticket
description: Explains what a ticket asks before any code is read. Gives a short rundown in Simplified Technical English of who wants what and why, with one concrete example. Step 1 of the ticket flow. Use at the start of a ticket, before /bstack-orient.
---

# /bstack-ticket

Help the user understand the ask. Read the ticket, not the code. Do not write code. Do not edit files. When you are done, wait for the user.

## Investigate (for yourself, not for the output)

- Get the ticket. Follow [TICKET.md](../bstack/TICKET.md).
- Read the notes file and add the user's answers since the last step. Follow [NOTES.md](../bstack/NOTES.md).
- Find who created the ticket. If the user created it, do not explain their own intent back to them. Keep **Who and why** to one line.
- For each rule in the ticket, find which system it applies to: this API, a client, a front-end, a CLI. Read the lines around it. A rule for another system is not part of the ask. It is not a gap.
- Find gaps the same way each time. Go through each point. Note what the ticket does not answer:
  - Input: which values are allowed? What happens with an empty or invalid value?
  - Result: what exactly is in it? What is not?
  - Edge cases: no results, many results, existing data that does not fit.
  - Scope: what is part of this ticket? What belongs to another ticket?
  - Users: who uses it? Does that change who may see or do it?
  - Use: does a person, a script or an AI agent use it? How often? Are there many calls at the same time?
- Keep only the gaps that change what gets built. Drop a gap that the ticket, its comments or linked tickets answer.
- Look up only what the ticket needs explained: a linked ticket, a parent ticket, a term. Do not trace code. /bstack-orient does that.

## Output

The user must be able to read it in 30 seconds. Follow this example exactly in shape, length and tone.

````
**Who and why:** The accountants ask this. They now export all invoices and delete old rows by hand.

**What they want:** GET /invoices/export gets a `paidAfter` filter. The export then holds only invoices paid after that date.

**Example:**
```
GET /invoices/export
    ?paidAfter=2026-10-01
    &companyId=<company-id>
```
Returns a CSV with only invoices paid in October or later.

**Terms:**
- paid date: the date the payment provider confirmed the payment, not the invoice date.

**Unclear:**
1. Does `paidAfter` include the given day itself?
2. What happens to invoices that are not paid yet?
````

### Rules

- **What they want:** what goes in and what comes out. Max two sentences. No implementation.
- **Example:**
  - Give one concrete request or action and its result.
  - Use the ticket's own values if it has them.
  - Put a request in a code block, with one query parameter per line. Put the result in a sentence below it.
  - Include only the parameters that matter for the ask.
- **Terms:**
  - Only business or domain terms from the ticket that the user may not know. Max 3.
  - No code names. Those belong in /bstack-orient.
  - One short sentence each. Omit the section if there are none.
- **Unclear:**
  - Only real gaps about the result the requester wants. A gap must change what gets built.
  - Do not ask what the ticket, its comments or linked tickets already answer.
  - Questions are optional. Max 3. Fewer or none is fine.
  - Never add a question to fill the list. Never ask a question you can answer yourself.
  - Ask plain questions to the user. Do not address them to the author. The user answers them or forwards them.
  - No questions about how it gets built (matching rules, escaping, performance). Those belong in /bstack-decide.
  - Number the questions. Omit the section if there are none.
- Put nothing after **Unclear** except the `Notes:` line and the closing line.

## Simplified Technical English

Write in Simplified Technical English. Read the rules in [STE.md](../bstack/STE.md) before you write. Check your output against them before you send it. If you must use a term, put it in **Terms**.

## Before sending

Check that no **Unclear** question is about how it gets built. Remove such a question. /bstack-decide covers it.

Write the **Ticket** section of the notes file. Put the unclear points under Answers as open questions. Follow [NOTES.md](../bstack/NOTES.md). Then add the `Notes:` link line.

End with one line: "Answer what is unclear, then run /bstack-orient." If nothing is unclear, end with "Run /bstack-orient."
