tasks = []


def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    """Add a task without allowing an empty name."""
    name = input("Enter task: ").strip()

    if not name:
        print("Task name cannot be empty.")
        return

    tasks.append({"task": name, "done": False})
    print(f"Task '{name}' added!")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("Tasks:")
    for index, t in enumerate(tasks, start=1):
        status = "DONE!" if t["done"] else "NOT DONE"
        print(f"{index}. {t['task']} [{status}]")


def mark_task_done():
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """Validate the task number before removing a task."""
    view_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if not 0 <= index < len(tasks):
            raise IndexError

    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("That task does not exist.")
    else:
        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task['task']}")
    finally:
        print("Returning to the main menu.")


print("Welcome to your To-Do List Application!")

# Keep showing the menu until the user chooses to exit.
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

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
