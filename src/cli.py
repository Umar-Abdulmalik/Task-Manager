from src.manager import TaskManager

MENU = """
Task Manager
------------
1. Add a task
2. List tasks
3. Complete a task
4. Delete a task
5. Search tasks
6. Quit
"""


def format_task(task):
    mark = "x" if task.done else " "
    return f"[{mark}] {task.id}. {task.title}"


def ask_id(prompt):
    value = input(prompt).strip()
    if not value.isdigit():
        raise ValueError("Please enter a number.")
    return int(value)


def show(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(format_task(task))


def run(manager=None):
    manager = manager or TaskManager()
    while True:
        print(MENU)
        choice = input("Choose 1-6: ").strip()
        try:
            if choice == "1":
                task = manager.add(input("Task title: "))
                print(f"Added: {format_task(task)}")
            elif choice == "2":
                show(manager.list_tasks())
            elif choice == "3":
                task = manager.complete(ask_id("Task ID to complete: "))
                print(f"Completed: {format_task(task)}")
            elif choice == "4":
                manager.delete(ask_id("Task ID to delete: "))
                print("Deleted.")
            elif choice == "5":
                show(manager.search(input("Search for: ")))
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 6.")
        except ValueError as error:
            print(f"Error: {error}")