---
name: bstack-spec
description: Writes a spec of a ticket for the team, from the decisions confirmed in /bstack-decide. Gives copyable Markdown in Simplified Technical English with one concrete example, then offers to add it to the ticket description. Optional step. Use when the user asks for a spec to share.
---

# /bstack-spec

Write the confirmed decisions as a spec that the team can read cold. Do not write code. Do not edit files. Show the spec first. Add it to the ticket only after the user says yes (see **Add to the ticket**). When you are done, wait for the user.

## Investigate (for yourself, not for the output)

- Get the ticket. Follow [TICKET.md](../bstack/TICKET.md).
- Read the notes file and add the user's answers since the last step. Follow [NOTES.md](../bstack/NOTES.md).
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

If you have a tool that can edit the ticket, end with one line: "Add this to the ticket description? Next: /bstack-build. Optional first: /bstack-review decide (a fresh check of the decisions)." Otherwise, end with: "Paste it into the ticket. Next: /bstack-build. Optional first: /bstack-review decide (a fresh check of the decisions)."

If the build is already done (see the **Build** section of the notes file), use this "Next" instead: "Next: /bstack-commit. Optional first: /bstack-review build (a fresh check of the change)."

## Add to the ticket

Do this only after the user says yes.

1. Fetch the ticket description again, right before you edit. Someone may have changed it.
2. Add the spec below the existing description. Put an empty line between them. Never remove, change or reorder existing text.
3. If the description already holds an older spec from this skill, ask the user first. Replace it only if they say so.
4. Use the tracker's own edit tool, such as `save_issue` for Linear. If the tool can append or patch, use that, not a full replace.
5. Fetch the description again. Check that the old text is still there, unchanged, and that the spec is below it. If not, tell the user at once and show the old text.
6. Say in one line that the spec is in the ticket. Give the ticket link.
