# Ticket notes

Each ticket has one notes file. It keeps what the earlier steps found and what the user decided. Then a later step, or a new session, does not lose the plot.

## Where

- Path: `~/.bstack/<repo>/<ticket-id>.md`. `<repo>` is the folder name of the git repo. `<ticket-id>` comes from [TICKET.md](TICKET.md). If there is no ticket id, use the branch name.
- Never put the file in the repo.
- Make the folder if it does not exist.

## Read

- At the start of each skill, read the file if it exists.
- Add what the user answered or confirmed since the last skill. Do this before you do anything else.
- Trust the file over your memory of the conversation. If they disagree, ask the user.

## Write

- Each skill writes only its own section. Replace the section if it already exists.
- Write in Simplified Technical English. Use lists. Keep each section short: the file is a memory aid, not a report.
- Use `file:///` links with absolute paths for code.
- Write only what the user said, confirmed or can see in your output. Mark a pick the user did not confirm yet as "(not confirmed)".

## Shape

```
# <ticket-id>: <ticket title>

## Ticket
- Ask: <what goes in and what comes out>
- Answers: <the user's answers to the unclear points>

## Code
- Trigger: <what makes the flow run>
- Where: <which part the change touches>
- <link> — <place where the change goes>

## Decisions
1. <decision>: <pick> (not confirmed | confirmed)
- Settled: <point>

## Build
- [ ] <plan line>
- [x] <plan line that is done>
- Not doing: <point>
- Verified: <what ran and the result>

## Review
1. <finding> — <fix | no fix | open>
```

Leave out a section that has no content yet.

## Link

End each skill's output with one line before the closing line: `Notes: [<ticket-id>.md](file:///<absolute path>)`.
