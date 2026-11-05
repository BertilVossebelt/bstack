---
name: bstack
description: The bstack front door for work on a ticket. Run /bstack alone to list the ticket skills. Run it with a ticket or a task to go to the right step.
---

# /bstack

The front door for bstack. Read what the user wants. Pick one skill. Run it. Stop.

## The flow

| Step | Skill | What it does |
|---|---|---|
| 1 | `/bstack-ticket` | Explains what the ticket asks: who, why, one example, what is unclear. Reads only the ticket. |
| 2 | `/bstack-orient` | Maps the code that the ticket touches, with links. |
| 3 | `/bstack-decide` | Lists the decisions before any code is written. |
| optional | `/bstack-spec` | Writes the confirmed decisions as a spec for the team. |
| 4 | `/bstack-build` | Shows a short plan. Then builds the confirmed decisions and explains the result. |
| optional | `/bstack-review` | Reviews the decisions (after step 3) or the build (after step 4). Includes performance and security. |
| 5 | `/bstack-commit` | Commits the change, gives the push command and offers a PR description. |

## Steps

1. If the user typed `/bstack` alone, show the table above. Then ask what they want to do. Do not route.
2. If the user gave only a ticket id or a ticket URL, start at `/bstack-ticket`.
3. Otherwise, find where the user is in the flow. Use the conversation and the notes file ([NOTES.md](NOTES.md)), if it exists:
   - A ticket that is already explained goes to `/bstack-orient`.
   - Code that is already mapped goes to `/bstack-decide`.
   - A request for a spec to share goes to `/bstack-spec`.
   - Confirmed decisions go to `/bstack-build`.
   - A request to review or check the work goes to `/bstack-review`.
   - A request to commit goes to `/bstack-commit`.
4. Say in one sentence which skill you picked. Run it. Do not run the next one.

## Do not

- Run more than one skill.
- Ask more than one question before you route.
- Explain, plan or write code in this skill.

## Simplified Technical English

Write the routing sentence and each question in Simplified Technical English. Follow the rules in [STE.md](STE.md).
