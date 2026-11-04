# bstack

_Do you understand the code you just shipped?_

bstack is a set of agent skills for working on a ticket. It takes you through the
ticket in small steps, so you understand the ask and the code, and make the decisions
yourself.

An AI agent writes code faster than you can read it. In a codebase you did not write,
that leaves you approving changes you do not understand, and tracing the code by hand
takes longer than the ticket. bstack does the tracing and hands you a map with links
to the lines that matter. The choices stay with you.

Built for working in an existing codebase with few docs and many hands in it.

## Install

Clone the repo, then run the installer from inside it.

**Windows**

```
install.cmd
```

**macOS and Linux**

```bash
./install.sh
```

The installer links each skill folder into `~/.claude/skills`, so an edit in the repo
applies at once. For another agent, pass the folder where it reads skills, such as
`./install.sh ~/.other-agent/skills`.

The skills read tickets with the issue tracker tools your agent has, such as a Linear,
Jira or GitHub MCP server. Without one, they ask you to paste the ticket.

## Usage

Run it from inside the repo the ticket is about. In an agent without slash commands,
ask for the skill by name, such as "run bstack-orient".

```
/bstack                       the loop and the optional steps
/bstack <ticket or task>      the right step for where you are

/bstack-ticket <ticket>       step 1
/bstack-orient                step 2
/bstack-decide                step 3
/bstack-build                 step 4

/bstack-spec                  optional, after decide
/bstack-review decide|build   optional, after decide or build
```

With no ticket id, the skills take it from the branch name. Each skill ends by naming
the next step and the optional ones that fit.

## The loop

Every ticket goes through four steps. After each one, the agent stops and you do your
part before the next one starts.

```
ticket ──▶ orient ──▶ decide ──▶ build
                        │          │
                   spec, review   review
```

| Step        | The agent gives you                                                           | Then you                          |
|-------------|-------------------------------------------------------------------------------|-----------------------------------|
| 1. `ticket` | who asks and why, one concrete example, and what the ticket leaves unclear    | answer what is unclear            |
| 2. `orient` | the data's path through the code, from where it enters to where it leaves     | read the code along that path     |
| 3. `decide` | the open choices, each with a pick, an alternative and what it costs          | confirm or change each choice     |
| 4. `build`  | a short plan to check, then the change and what was verified                  | say go, then read the change      |

Each step reads only what the one before it settled. So `orient` maps the code
for the ask you understood, `decide` asks only what the code does not answer, and
`build` writes only what you confirmed.

Two optional steps fit in where you need them:

- **`spec`**, after `decide`: the decisions as a spec your team can read, ready to paste
  into the ticket.
- **`review`**, after `decide` or `build`: a fresh check by a subagent that did not see
  the reasoning behind the work.

Questions and decisions are never padded. A step with nothing open says so, and you
move on.

## Example

A ticket asks for a `paidAfter` filter on an invoice export. `/bstack-orient` gives:

```
Path:
1. line 40 — Export receives an InvoiceExportRequest. It holds the filters from
   the query string.
2. lines 42–75 — permission checks and logging. Not needed for this ticket.
3. line 77 — Export sends the query and the request to ApplyExportFilters.
4. line 120 — ApplyExportFilters adds one Where per filter in the request.
   The new filter goes here.
5. line 150 — Export caps the result at 10,000 invoices. This keeps one export
   from loading the whole table.
6. line 160 — Export gives the query to WriteCsv (turns each invoice into a row
   and streams the file).

Related:
- line 131 (step 4) — the issuedAfter filter keeps invoices issued after a date.
  Copy its date check and its empty-value check.
```

Then `/bstack-decide` gives:

```
Decide:
1. Date format: ISO date only (alt: date and time). Same as issuedAfter.
2. (performance, risk: medium) Index on PaidAt: add one (alt: none). Without it,
   each export reads all invoices.
   An index makes the filter fast. The catch: one migration, and slightly slower
   invoice saves.
3. (security, risk: high) Company check: limit to the caller's companies
   (alt: none). Without it, users export other companies' invoices.

Settled:
- An empty paidAfter is ignored.
- Unpaid invoices never match.
```

Each `line N` is a link that opens the file at that line.

## Plain English

All output follows Simplified Technical English (ASD-STE100): one idea per sentence,
at most 20 words, active voice, and the code's own names. The rules are in
[bstack/STE.md](bstack/STE.md).

Claims about behaviour are checked in the code, not in comments. What could not be
checked is marked `(not checked)`.

## Performance and security

`decide` and `review` look for gaps every time, and report them only when there is one.
Each gets a risk level:

|          |                                                                         |
|----------|-------------------------------------------------------------------------|
| `low`    | light slowdowns or small issues, only in rare situations                |
| `medium` | slowdowns or errors that other users notice, in realistic situations    |
| `high`   | an outage, data loss or a data leak is possible                         |

The level is based on what anyone with access could do, from a script or an AI agent
in a loop, not on how the ticket expects it to be used. The levels are in
[bstack/RISK.md](bstack/RISK.md).

## Adapting it

The skills are plain Markdown. Edit a `SKILL.md` in this repo and the next run uses it.

Code style and the spec's language come from your own agent instructions (`AGENTS.md`,
`CLAUDE.md`), not from the skills.

## Uninstall

Delete the `bstack*` links in the skills folder you installed into.

## Licence

MIT, copyright Bertil Vossebelt. See [LICENSE](LICENSE).
