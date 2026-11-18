# Lab Report - Student Task Manager

**Name:** Urwa Kamal
**Course:** DevOps for Cloud Computing (CSC418)
**Repository:** https://github.com/urwa190/student-task-manager
**Release:** https://github.com/urwa190/student-task-manager/releases/tag/v1.0.0

---

## 1. Difference between Git and GitHub; purpose of add, commit and push

Git is a version control tool that I install and run on my own computer. It keeps a complete history of my project, so I can see what changed, when it changed, and go back to an older version if something breaks. It works even without an internet connection.

GitHub is an online website that stores Git repositories in the cloud. It is built on top of Git and adds features for working with others, such as Issues, Pull Requests, Actions and Releases. In short, Git is the tool and GitHub is the place where the work is shared.

- **git add** moves my changes to the staging area. This lets me choose exactly which changes will go into the next commit instead of saving everything at once.
- **git commit** saves the staged changes as a snapshot in my local history, together with a message that explains what I changed.
- **git push** uploads my local commits to the repository on GitHub, so the work is backed up online and visible to others.

## 2. Why branches and Pull Requests are used; what causes merge conflicts

A branch is a separate line of development. I created `feature/add-task`, `feature/complete-task` and `feature/delete-task`, and built each feature on its own branch. This means unfinished or broken code never touches `main`, which always stays in a working state. Branches also let several people work at the same time, and if an idea does not work out, the branch can simply be deleted.

A Pull Request (PR) is a request to merge a branch into `main`. Instead of merging directly, the changes are shown on GitHub so they can be reviewed file by file, commented on, and checked by automated tests. Only after the review is the PR merged. In this lab I opened a PR for each feature branch, linked it to an Issue, added a review comment and then merged it.

A merge conflict happens when two branches change the same lines of the same file in different ways, and Git cannot decide which version to keep. In my lab, I added "Project status: Planning" to `README.md` on `main`. I then created two branches from that commit. One changed the line to "In Progress" and the other changed it to "Completed". The first branch merged without a problem, but when I merged the second one, Git stopped and showed a conflict, because both branches had edited the same line. I opened the file, looked at the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), deleted the markers, kept one final status line, and committed the merge to finish it.

## 3. Difference between fetch and pull, and between merge and rebase

`git fetch` downloads the latest commits from GitHub but does not change my working files or my current branch. It lets me look at what others have done before I decide to combine it with my work. `git pull` does a fetch and then immediately merges the new commits into my current branch, so my files are updated right away. So `pull` is basically `fetch` plus `merge`.

Merge and rebase both combine changes from one branch into another, but they do it differently. Merge joins the two branches with a new merge commit and keeps the full history exactly as it happened, including the branches. Rebase takes my commits and replays them on top of the latest commit of the other branch, which gives a clean, straight history without a merge commit. The downside is that rebase rewrites commit history, so it should not be used on branches that other people are already using. In this lab I used merge.

## 4. How GitHub Issues and Actions help a development team

GitHub Issues keep the team's tasks, bugs and feature ideas in one place. Each Issue has a description and a label, such as `enhancement` or `documentation`, so everyone can see what needs to be done and what type of work it is. A Pull Request can be linked to an Issue with `Closes #number`, and the Issue is closed automatically when the PR is merged, so progress is tracked without extra effort.

GitHub Actions runs automated workflows on GitHub's servers. In this project, my workflow runs the unit tests every time code is pushed to `main` or a Pull Request is opened against `main`. If a test fails, the run shows a red cross, so the problem is found before the code is merged. If everything passes, it shows a green tick. This saves the team from running tests by hand and helps keep `main` stable.

## 5. One difficulty I faced and how I solved it

When I ran the app for the first time and chose the "Complete" option, it crashed with `AttributeError: 'TaskManager' object has no attribute 'complete_task'`. At first I did not understand why, because I had pasted the method into the file. After checking the code, I found that `complete_task` and `delete_task` were indented 8 spaces instead of 4, so Python treated them as functions inside `get_tasks` instead of methods of the `TaskManager` class. I fixed the indentation so that all methods start at the same level inside the class, ran the app again to confirm that completing a task worked, and committed the fix.

I also made a mistake while preparing the merge conflict. I created the "Completed" branch before committing the "Planning" line on `main`, so the first merge failed because the other branch did not exist. I deleted that branch, redid the steps in the correct order, and the conflict then appeared as expected. This taught me that the order of commits and branches matters a lot in Git.

---

Screenshots of the key steps are in the `word document`.