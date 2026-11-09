# Task Manager

A command-line task manager written in Python. Add, list, complete, delete and
search tasks. Tasks are saved to a JSON file, so they are still there the next
time you run the program.

## Features

- Add, list, complete and delete tasks
- Search tasks by keyword (not case sensitive)
- Tasks saved automatically to `tasks.json`
- Input checks and friendly error messages
- Unit tests with pytest

## Requirements

Python 3.9 or newer.

## Getting started

```
git clone https://github.com/Umar Abdulmalik/task-manager.git
cd task-manager
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Running the tests

```
python -m pytest -v
```

## Project structure

```
task-manager/
├── main.py              # starts the app
├── src/
│   ├── task.py          # Task model and validation
│   ├── manager.py       # add, complete, delete, search, save and load
│   └── cli.py           # menu and user input
├── tests/               # pytest tests
└── requirements.txt
```

## What I learned

- Structuring a Python project into separate modules
- Using dataclasses, JSON storage and error handling
- Writing unit tests with pytest
- Using Git and GitHub with clear commits

## Ideas for the future

- Due dates and priorities
- Editing an existing task
- A Django web version

## Author

Umar Abdulmalik · [GitHub](https://github.com/Umar Abdulmalik)