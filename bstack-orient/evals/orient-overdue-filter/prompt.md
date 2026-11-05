---
tags: [bstack]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

/bstack-orient

There is no issue tracker here, so here is the ticket text:

LIB-41 Overdue filter on the loans export
Created by: Sam (front desk lead)

The front desk calls members with overdue books every Monday. Now they export all loans for the branch and filter them in Excel. Please add an overdue filter to GET /branches/{id}/loans/export, so the CSV only has overdue loans.

We agreed: a loan is overdue when its due date is before today and it is not returned.

The code is in app/.

Input files: app/
