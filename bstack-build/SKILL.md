---
name: bstack-build
description: Implements a ticket after the /bstack-decide decisions are confirmed. Shows a short plan, follows the confirmed decisions, verifies the change and ends with a short summary in Simplified Technical English. Use when the user says to build after /bstack-decide.
---

# /bstack-build

Implement the decisions the user confirmed in /bstack-decide.

## Steps

1. Use the confirmed /bstack-decide decisions. Do not open them again.
2. Before you write code, show the plan (see **Plan**). Wait for the user's go. The plan is a quick check, not a new design step. Skip it only if the user says so.
3. Make the smallest change that does the job. Follow **Code style**.
4. Before you verify, check each added or changed line against each rule in **Code style**, one by one. Code that you copy from an existing pattern must follow these rules too. If the pattern breaks a rule, do not copy that part.
5. If a real choice comes up that /bstack-decide did not cover, **stop and ask**. Examples: a query shape, a library call, a data type, a placement. Do the same if you find a performance or security gap that /bstack-decide did not cover. Ask it like a /bstack-decide decision: the pick, the alternative, what it does, the catch.
6. Verify: build, run the related tests, and call the endpoint if that fits. If something fails, say so and show the output.
7. Do not commit.

## Plan

Write in Simplified Technical English. The user must be able to read it in 15 seconds. Follow this example in shape and length:

```
**Plan:**
1. [ApplyExportFilters](link) — add the `paidAfter` filter next to `issuedAfter`.
2. [ExportFilterTests](link) — add tests for a valid date and an empty value.

**Not doing:**
- No index on `PaidAt` (decision 2).
- No change to the CSV columns.
```

- **Plan:** one line for each file or place, in the order you change them. Say what changes, not how. Max 6 lines.
- **Not doing:** things the user could expect but that this build leaves out. Give each one its reason or decision number. Never list something nobody would expect. Omit the section if it is empty.
- Each line comes from the confirmed decisions. If the plan needs a new choice, ask it as in step 5.

End the plan with one line: "Say go, or change the plan."

## Code style

- Before you write code, collect each code style rule that applies. Look in:
  - the user's and the project's instructions (such as AGENTS.md or CLAUDE.md), and the files they point to;
  - memories (the memory index and the memory files it lists);
  - code style docs in the project (such as `CONTRIBUTING.md` or a style guide);
  - the linter and formatter config (such as `.editorconfig`).
- Follow all of them. Step 4 checks against this full list.
- If these sources say nothing, match the code around the change: its naming, its comment density, its idiom.
- If two sources conflict, tell the user. Ask before you pick one.

## Output

Write in Simplified Technical English. Read the rules in [STE.md](../bstack/STE.md) before you write. Check your output against them before you send it. Use exactly this shape:

```
**Built:** <one sentence>

**Changes:**
- <file:line> — <what changed>

**How it works:**
- <2–4 sentences on the core mechanism: the lines that are not obvious, with file:line>

**Verified:** <what ran and the result>
```

- **How it works** says what each core call does in practice. Example: "`AsNoTracking` skips change tracking. Changes to the loaded rows are not saved."
- Add **Not done:** only if a step was skipped or failed.
- Do not add a closing summary.

End with one line: "Optional: /bstack-review build (a fresh check of the change)."
