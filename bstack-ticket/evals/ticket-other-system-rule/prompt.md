---
tags: [bstack]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

/bstack-ticket

There is no issue tracker here, so here is the ticket text. I wrote it myself:

LIB-52 Returned-after filter
Created by: me

Add a returnedAfter filter to GET /branches/{id}/loans/export. Dates are YYYY-MM-DD, like lentAfter.

CLI note: the library-cli `export` command must show a spinner while it waits for the CSV.
