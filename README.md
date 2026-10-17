# To-Do List

A simple command-line Python app to add and view tasks. Tasks are saved to a JSON file, so they are still there the next time you run the program.

## Features

- Add a new task (empty tasks are rejected)
- View all saved tasks with their ID numbers
- Tasks persist between runs using `tasks.json`
- Handles a missing or unreadable `tasks.json` without crashing
- Simple menu with input validation for invalid options

## Requirements

- Python 3.6 or newer
- No external libraries (uses the built-in `json` module)

## How to Run

```bash
python todo_list.py
```

On Windows you can also use `py todo_list.py`.

A `tasks.json` file is created automatically in the same folder when you add your first task.

## Example Session

```
1. Add task
2. View tasks
3. Exit
Choose (1/2/3): 1
Write your task: Finish Python project
Task added successfully!

1. Add task
2. View tasks
3. Exit
Choose (1/2/3): 2
1. Finish Python project

1. Add task
2. View tasks
3. Exit
Choose (1/2/3): 3
Goodbye!
```

## How It Works

| Function | Purpose |
|---|---|
| `load_tasks()` | Reads tasks from `tasks.json`; returns an empty list if the file is missing or invalid |
| `save_tasks(tasks)` | Writes the task list to `tasks.json` |
| `add_task(tasks, task)` | Validates the text, creates a new ID, adds the task and saves |
| `view_tasks(tasks)` | Prints all tasks, or a message if there are none |
| `show_menu()` | Prints the menu options |
| `main()` | Runs the menu loop |

### Data Format

Tasks are stored as a list of dictionaries:

```json
[
  { "id": 1, "task": "Finish Python project" },
  { "id": 2, "task": "Push code to GitHub" }
]
```

## Known Limitations

- Tasks cannot be deleted or marked as complete yet
- If `tasks.json` becomes corrupted, it is treated as empty and will be overwritten on the next save

## Possible Improvements

- Delete tasks and mark them as done
- Edit existing tasks
- Support Urdu or emoji text with `encoding="utf-8"`
- Add due dates or priorities

## Author

Zaina
