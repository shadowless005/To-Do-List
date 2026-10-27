# Python To-Do List Application

This Python project is a functional command-line to-do list application. Users can add, view, mark as done, and delete tasks, then exit the application.

## How to Run

1. Install Python 3 if it is not already installed.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open a terminal in the folder containing `to-do.py` and run:

```bash
python3 to-do.py
```

No additional packages are required.

## How to Use

When the application starts, a welcome message and a numbered menu appear. Enter an option from 1 through 5:

- **Option 1 — Add Task:** Add a new task to the list. Empty or whitespace-only task names are rejected.
- **Option 2 — View Tasks:** Display the current tasks with their numbers and either `DONE!` or `NOT DONE`. If the list is empty, the application displays `No tasks yet.`
- **Option 3 — Mark Task as Done:** Enter the number of the task to mark it as complete. Select option 2 afterward to see its updated status.
- **Option 4 — Delete Task:** Enter the number of the task to remove it from the list. A confirmation message shows which task was deleted.
- **Option 5 — Exit:** Close the application with the message `Goodbye!`.

The menu repeats after each action until you select option 5.

## Input Validation and Error Handling

- Invalid menu choices display a message asking for a number between 1 and 5.
- Blank task names are not added to the list.
- Selecting view, mark as done, or delete when the list is empty displays `No tasks yet.`
- Entering text or a decimal instead of a task number displays `Please enter a valid whole number.`
- Selecting a task number that does not exist displays `Invalid task number. That task does not exist.`
- The mark-as-done and delete functions use `try`, `except`, `else`, and `finally`. The `finally` block prints a separator after each task-number attempt, whether the input is valid or invalid.

## Task Storage and Code Organization

Tasks are stored in a Python list. Each task is a dictionary containing its name and completion status.

The code is organized into functions for displaying the menu, adding tasks, viewing tasks, marking tasks as done, deleting tasks, and running the main application loop.

Tasks are stored in memory for the current session only. Exiting the application clears the list; tasks are not saved to a file or database.

## Testing

The application was checked with:

- Adding, viewing, completing, and deleting a task
- Viewing, completing, or deleting tasks when the list is empty
- Empty and whitespace-only task names
- Invalid main-menu choices
- Text, decimal, zero, negative, and out-of-range task selections
- Exiting the application

## Author

Matthew Shin
