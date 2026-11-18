# Student Task Manager

A simple Python console application to add, display, complete and delete tasks.

## Features

- Add tasks (empty titles are rejected)
- Display all tasks with a completion mark
- Mark a task as completed by its ID
- Delete a task by its ID
- Automated tests with GitHub Actions

## Setup

1. Install Python 3.x
2. Clone the repository:

```
git clone https://github.com/urwa190/student-task-manager.git
cd student-task-manager
```

## Usage

```
python task_manager.py
```

Choose an option from the menu: 1 Add, 2 Show, 3 Complete, 4 Delete, 5 Exit.

## Running Tests

```
python -m unittest discover -s tests -v
```

Project status: In Progress