---
tags: [bstack]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

/bstack-decide

There is no issue tracker here, so here is the ticket text:

LIB-63 Late fee in the loans export
Created by: Noor (finance)

Finance wants a late_fee column in GET /branches/{id}/loans/export, so they can check what members owe.

My notes: show the fee in euros with 2 decimals.

The code is in app/.

Input files: app/
