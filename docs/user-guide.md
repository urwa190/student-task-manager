# User Guide

## Start the app

```
python task_manager.py
```

## Menu options

| Option | What it does |
|---|---|
| 1 | Add a task. Enter a title; empty titles are rejected. |
| 2 | Show all tasks. `[ ]` means pending, `[x]` means completed. |
| 3 | Complete a task. Enter its ID number. |
| 4 | Delete a task. Enter its ID number. |
| 5 | Exit the program. |

## Example session

```
Choose: 1
Title: Finish DevOps lab
Choose: 2
[ ] 1. Finish DevOps lab
Choose: 3
Task ID: 1
Task completed.
Choose: 2
[x] 1. Finish DevOps lab
```

## Common errors

- `Error: Task title cannot be empty.` : type at least one character.
- `Task not found.` : check the ID with option 2.
- `Error: invalid literal...` : the ID must be a number.