---
name: bstack-spec
description: Writes a spec of a ticket for the team, from the decisions confirmed in /bstack-decide. Gives copyable Markdown in Simplified Technical English with one concrete example, ready to paste into the issue tracker. Optional step. Use when the user asks for a spec to share.
---

# /bstack-spec

Write the confirmed decisions as a spec that the team can read cold. Do not write code. Do not edit files. Never post the spec. The user posts it. When you are done, wait for the user.

## Investigate (for yourself, not for the output)

- Get the ticket. Follow [TICKET.md](../bstack/TICKET.md).
- Use the decisions the user confirmed in /bstack-decide and later in the conversation. Do not open them again. Do not add decisions of your own.
- If the spec needs a point that is not decided, ask before you write.
- Take example values from real data or the ticket. Do not guess them. If you use a placeholder, tell the user outside the spec.

## Output

Put the whole spec in one ` ````markdown ` block (four backticks). Then the user can copy it with nested code blocks intact. Outside the block, add max one line.

Shape:
- `## Spec`, then a short opening: what changes, in a few sentences or a short list.
- One concrete example: a request, a JSON shape or an action, in a code block. Use the real names and values.
- One `###` section for each part that a reader needs. Examples: the admin screens, existing data, the release order. Leave out a part with nothing to say.
- `### Out of scope` (in the spec's language) if the conversation put things out of scope. Omit it otherwise.

### Rules

- Language:
  - Use the language that the user's instructions (such as AGENTS.md or CLAUDE.md) name for team documents.
  - If they name none, use the language of the ticket.
  - Apply the rules in [STE.md](../bstack/STE.md) to that language: one idea per sentence, max 20 words, active voice, common words, the code's names and no synonyms.
- If the user's instructions describe a writing voice, STE wins where they conflict. The other voice rules still apply.
- Use lists, not paragraphs.
- The spec must read cold:
  - No sentences that echo the discussion.
  - No options that were not picked.
  - No "X, not Y" contrasts.
- State the result and the mechanism. Leave out file names, line numbers, class names and implementation steps. Keep a name only if the team needs it to talk about the change, such as a field, a slot or a job.
- Match the length to the change. A small change gets only the opening and the example.
- Mention a colleague with `@name` only where the spec asks them to do something.

## Before sending

Check each sentence against the STE rules. Check that the spec reads cold for someone who missed the discussion.

End with one line: "Paste it into the ticket. Next: /bstack-build. Optional first: /bstack-review decide (a fresh check of the decisions)."
