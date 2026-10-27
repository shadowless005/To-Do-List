# A command-line to-do list. Tasks last for the current session only.

tasks = []


def show_menu():
    # Display the available actions.
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    # Add a task only when its name is not blank.
    name = input("Enter task: ").strip()
    if not name:
        print("Task cannot be empty. Please enter a task name.")
        return
    tasks.append({"task": name, "done": False})
    print(f"Task '{name}' added!")


def view_tasks():
    # Show numbered tasks and their completion status.
    if not tasks:
        print("No tasks yet.")
        return
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "DONE!" if task["done"] else "NOT DONE"
        print(f"{index}. {task['task']} [{status}]")


def mark_task_done():
    # Validate the selection before marking a task complete.
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
    except ValueError:
        print("Please enter a valid whole number.")
    else:
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid task number. That task does not exist.")
    finally:
        # Display a separator after either a valid or invalid selection.
        print("-" * 30)


def delete_task():
    # Delete a task only after validating its number.
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
    except ValueError:
        print("Please enter a valid whole number.")
    else:
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number. That task does not exist.")
    finally:
        print("-" * 30)


def main():
    # Keep showing the menu until the user exits.
    print("Welcome to your To-Do List!")
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
