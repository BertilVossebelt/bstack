---
name: bstack-commit
description: Commits the change from /bstack-build in logical commits, gives the push command and offers to write the PR description. Follows the commit, branch and PR rules in the user's instructions and memories. Step 5 of the ticket flow. Use when the user asks to commit, or to commit and push.
---

# /bstack-commit

Commit the change. Never push. When you are done, wait for the user.

## Rules first

Before you do anything else, collect each rule about branches, commits, pushing and PR descriptions. Look in:
- the user's and the project's instructions (such as AGENTS.md or CLAUDE.md), and the files they point to;
- memories (the memory index and the memory files it lists). Read each memory about commits, branches or PRs;
- contribution docs in the project (such as `CONTRIBUTING.md`).

These rules win over the defaults in this skill. If two sources conflict, tell the user. Ask before you pick one.

## Steps

1. Read the notes file. Follow [NOTES.md](../bstack/NOTES.md). Use the ticket id and the **Build** section to write the messages.
2. Run `git status`, `git diff`, `git diff --staged` and `git log --oneline -15`. The log shows the message style and the scopes the repo uses.
3. Do not commit on the default branch (such as `main`). If you are on it, make a branch first. Use the branch names that the rules or the existing branches use. Put the ticket id in the name. If you do not know the ticket id, ask.
4. Put the changes in logical groups. Stage by file, or by hunk if a file holds two changes.
5. If two changes are mixed so that a split needs a code state that never existed, stop. Tell the user and ask first.
6. Commit each group.
7. Do not push. Give the push command (see **Push**).

## Message

If the rules say nothing, use these defaults:
- Conventional commits: `<type>(<scope>): <subject>`.
- Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `build`, `ci`, `chore`, `style`, `revert`.
- Use a scope from `git log` if one fits. Otherwise use a short lowercase name for the part of the code that changed.
- Write the subject in the imperative mood. Start with a lowercase letter. Do not end with a period. Keep it below 72 characters.

## Push

Check `git status -sb` and the upstream (`git rev-parse --abbrev-ref @{u}`). Then give one of these:
- If `git push` works as it is: say the commits are ready to push.
- If the branch has no upstream: `git push -u origin <branch>`.
- If you changed commits that are already pushed: `git push --force-with-lease`.
- If the branch is behind the remote: `git pull --rebase`, then `git push`.

## Output

Write in Simplified Technical English. Follow the rules in [STE.md](../bstack/STE.md).

```
**Committed:**
- <hash> <subject>

**Push:** <the command, or "ready to push">
```

Then add the `Notes:` link line. End with one line: "Do you want me to write the PR description?"

## PR description

Do this only after the user says yes.

- Use the language and the writing voice that the rules name for PR descriptions. If they name none, use the language of the ticket and the rules in [STE.md](../bstack/STE.md).
- Put the draft in one ` ```markdown ` block, so the user can copy the raw text.
- Make the length match the change. A small change gets two or three sentences about the result.
- The text must read cold. Do not echo the discussion. Do not name options that were not picked.
- Write only what is true and what the reader needs.
- Before you send it, check the draft against each rule, one by one. Remove each part that fails.
- Do not post the PR description. The user posts it.
