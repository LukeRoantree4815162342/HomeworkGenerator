## Preferred Workflow:

---

### First of all, Thanks! :)

---

> work to address only one issue at a time.
(If it happens to fix multiple unintentionally that's fine)

> pull the latest version of master

> make your feature/bugfix/whateer the issue is

> pull from master again when done, address any conflicts locally

> *without having committed any changes yet* switch to a new branch with 'git checkout -b 'Issue(<Issue number>)'

> add and commit your changes, then push to create a new remote branch with your changes; git add <files> ; git commit -m '<message>' ; git push --set-upstream origin 'Issue(<Issue Number>)'

> on github, open a pull request for your branch - don't merge it yourself.

---

## When to vary from this workflow:

> if the issue is large, and/or time consuming, it is fine to make the new local & remote branches earlier, and commit/push as you go, but mention this when you open a pull request

> small changes to documentation files (spelling fixes, dependency updating, thanking contributors, etc.) can be committed straight to master. If in doubt, open an issue for it and follow the general workflow
