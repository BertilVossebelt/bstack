---
name: bstack-review
description: Reviews a /bstack-decide or a /bstack-build result before the next step. Checks the work against the ticket, the confirmed decisions and the code, including performance and security. Reports numbered findings in Simplified Technical English. Optional step. Use when the user asks to review the decisions or the build.
---

# /bstack-review

Review the decisions or the build with fresh eyes. Report findings. Do not fix anything. When you are done, wait for the user.

## What to review

- `/bstack-review decide`: the /bstack-decide output in this conversation.
- `/bstack-review build`: the uncommitted changes (`git diff`) from /bstack-build.
- No argument: review the build if there are uncommitted changes. Otherwise, review the decisions.

## How

- Run the review in a fresh subagent with an empty context. Then it does not share the reasoning that made the work.
- Do not use a fork or a helper that sees this conversation.
- If you cannot start such a subagent, say so in one line. Then do the review yourself, with the same limits.
- Give the subagent only:
  - the ticket id;
  - the confirmed decisions;
  - what to review: the /bstack-decide output, or "the uncommitted changes".
- Do not give it your explanations, the /bstack-orient rundown or why choices were made. Let it read the code itself.

Ask it to check:

- **Decisions:** decisions that /bstack-decide missed, picks that conflict with existing patterns or with each other, claims about the code that are wrong.
- **Build:**
  - bugs;
  - behaviour that differs from the confirmed decisions;
  - missing or weak tests;
  - the code style rules from the user's and the project's instructions (such as AGENTS.md or CLAUDE.md), memories, code style docs and the linter and formatter config (such as `.editorconfig`).
- **Approach, for both:** is this the best way to do it in this codebase?
  - Search for an existing service, pipeline, mapper or helper that already makes this value or behaviour. Also search for one that makes values of the same kind.
  - Flag new logic that copies or bypasses it.
  - Flag new logic outside such a place if it belongs in that place. This is true even if the value does not exist there yet.
  - Flag a placement that differs from how similar features are built.
- **Performance, for both:** queries that load or scan too much, work per row that could happen once, missing paging, calls repeated in a loop.
- **Security, for both:** missing permission or ownership checks, user input that gets to a query or the output unchecked, data returned to users who must not see it.

Check each finding in the code. Code comments are hints, not proof. If you cannot check a finding, mark it "(not checked)".

## Output

Write in Simplified Technical English. Read the rules in [STE.md](../bstack/STE.md) before you write. Check your output against them before you send it. Follow this example in shape and length:

```
**Findings:**
1. [line 15] (security, risk: high) — the endpoint does not check the company permission. A user can export invoices of other companies.
2. [line 42] (bug) — `ApplyExportFilters` skips the date check if the value is empty. The filter then returns all invoices.
3. [line 88] (performance, risk: medium) — `WriteCsv` loads all invoices before it writes. Large companies can run out of memory.
4. [line 60] (approach) — the change calculates the VAT in the controller. `InvoiceTotalService` ([link]) calculates the other invoice amounts. Add the VAT there.

**Questions:**
1. Must `paidAfter` also accept a date with a time?
```

- Each finding has:
  - a link, labelled with its line;
  - a type: bug, approach, decision, performance, security, test or style;
  - what is wrong, and the effect.
- Give each performance and security finding a risk level from [RISK.md](../bstack/RISK.md).
- Findings and questions are optional. Never add one to fill the list. If there are none, write "No findings."
- **Questions:** only points the reviewer cannot decide from the ticket or the code. Omit the section if it is empty.
- Order the findings by impact, highest first.

End with one line: "Tell me which findings to fix. After a decide review, next: /bstack-build."
