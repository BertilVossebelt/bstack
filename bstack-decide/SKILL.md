---
name: bstack-decide
description: Turns a ticket into decisions the user makes before any code is written. Finds where similar logic already is, lists the open decisions, then stops. Step 3 of the ticket flow. Use after /bstack-orient, or when the user asks for the decisions on a ticket. Run it before /bstack-build, unless the user says to skip it.
---

# /bstack-decide

Make sure the user makes the decisions behind a ticket, not the agent. Do not write code. Do not edit files. When you are done, wait for the user.

Point to evidence: file:line, existing patterns. Do not just state conclusions.

## Investigate (for yourself, not for the output)

- Get the ticket. Follow [TICKET.md](../bstack/TICKET.md).
- Answer from the code what the code can answer.
- If the user gave notes with the ticket, the notes are the design. Do not list alternatives that contradict them. Raise only gaps that the notes leave open, or real conflicts with the code.
- Do not put a case out of scope because of a guess, such as "this rarely happens". Cover the case, or ask the user. If you ask, call it an assumption.
- For each rule in the ticket, find which system it applies to: this API, a client, a front-end, a CLI. Read the lines around it. Only rules for the system you change are requirements.
- Before you report a conflict in the ticket or the user's notes, quote both lines. Read their context. Report it only if it is still a conflict.
- Find where the code already makes similar values or behaviour: pipelines, services, calculators, mappers.
  - Use the existing place, not new logic.
  - Notice if the change copies a rule that already exists in another place.
  - If a place makes values of the same kind, the new value belongs there too. This is true even if the value does not exist there yet.
  - Read each line again before you cite it.
- Find which choices the ticket leaves open. These all count: placement, a new calculation or an existing value, rounding, naming, data shape, anything that is saved.
- Look for performance and security gaps. Answer these questions for yourself each time:
  - What does one request read from the database? For the largest customer or tenant? For all of them together? Can it use an index?
  - Does the change add a query or a call per row? Does it run an expensive query more than once?
  - Who can call this? Can they get data of customers, tenants or users they must not see?
  - Where does user input go? Can it change a query or the output in a way nobody wants?
  - What is the expected use? Get it from the ticket or the /bstack-ticket answers. Expected use is not a limit.
  - What is the possible use? Anyone with access can call it from a script or an AI agent, in a loop or in parallel.
  - What do the expected use and the possible use do to the database and to other users?
- Base the risk level on the possible use. Follow [RISK.md](../bstack/RISK.md).
- Make a real gap a decision. Mark it "(performance)" or "(security)". If there is no real gap, do not add one.
- Check each pick against the purpose of the ask. Drop a pick that blocks what the requester needs the change for.
- If the change can scan a lot of data (no index, a leading `%`, large text columns, work per row):
  - Get the table size from the database metadata on a development or test database. Get the row count and the data size, e.g. with `sp_spaceused` on SQL Server or `pg_total_relation_size` on PostgreSQL. This is fast and does not scan.
  - Before you pick an approach, search the code for a faster query on the same data, such as another query on the same table or column.
  - Never call the risk acceptable without a number. Make it a decision. Say that it is not measured.
  - Offer to time the query on a development or test database. Ask first, because other people may use that database.
  - Never use a production connection.
- Check that your picks agree with each other and with the patterns you found. If an alternative matches a found pattern better, swap them.

## Output

The user must be able to read it in 30 seconds. Write in Simplified Technical English. Read the rules in [STE.md](../bstack/STE.md) before you write. Check your output against them before you send it. Follow this example exactly in shape, length and tone:

```
**Decide:**
1. Date format: ISO date only (alt: date and time). Same as `issuedAfter`.
2. (performance, risk: medium) Index on `PaidAt`: add one (alt: none). Without it, each export reads all invoices.
   An index makes the filter fast. The catch: one migration, and slightly slower invoice saves.
3. (security, risk: high) Company check: limit to the caller's companies (alt: none). Without it, users export other companies' invoices.

**Settled:**
- An empty `paidAfter` is ignored.
- Unpaid invoices never match.
```

### Rules

- A decision is one line: the choice, the pick, the alternative and a few words why. Max 25 words.
- Add one indented line only for a mechanism choice: a library call, a query shape, a data type. Say what it does in practice and what its catch is. Max two sentences.
- Give each performance or security decision a risk level from [RISK.md](../bstack/RISK.md).
- **Decide:**
  - Holds only choices that could reasonably go another way. Obvious choices go in **Settled**.
  - Decisions are optional. **Decide** can be empty.
  - Never add a decision to fill the list.
  - Never add a decision that the ticket, the user's notes or the code already answers.
  - All decisions are for the user. Do not address questions to the ticket's author.
- **Settled:** max 5 points of one short sentence each. Omit the section if it is empty.
- Do not use tables. Do not describe current behaviour beyond what one decision needs. Do not add a closing summary.

End with one line: "Confirm or change these. Next: /bstack-build. Optional first: /bstack-spec (a spec for the team), /bstack-review decide (a fresh check of the decisions)."
