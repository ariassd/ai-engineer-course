import os
import json

# File to store tasks
FILE_NAME = "tasks.db"


# Get all tasks previously saved into the database file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                (
                    task_id,
                    title,
                    status,
                ) = line.strip().split("|")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks


# Save tasks in database file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id}|{task['title']}|{task['status']}\n")


# Export all tasks in CSV format
def export_tasks_csv(tasks):
    file_name = input("Write the destination file name: ")
    file_name += ".csv"
    with open(file_name, "w") as file:
        file.write(f"task_id,title,status\n")
        for task_id, task in tasks.items():
            file.write(f"{task_id},{task['title']},{task['status']}\n")

        print(f"files was fully exported into {file_name}")


# Export all tasks in JSON format
def export_tasks_json(tasks):
    file_name = input("Write the destination file name: ")
    file_name += ".json"
    with open(file_name, "w") as file:
        export_format = [
            {"task_id": task_id, "title": task["title"], "status": task["status"]}
            for task_id, task in tasks.items()
        ]
        file.write(json.dumps(list(export_format), indent=2))
        print(f"files was fully exported into {file_name}")


# Create new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added")


# View the list of tasks created
def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")


# Mark a task complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' is compete")
    else:
        print("Task ID not found")


# Delete task
def delete_task(tasks):
    task_id = int(input("Enter task ID to mark deleted: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' was deleted")
    else:
        print("Task ID not found")


def clear_console():
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")


# Entry point of the system
def main():
    tasks = load_tasks()

    # Map with actions available for the system
    options = {
        "Exit": lambda tasks: (save_tasks(tasks), print("Goodbye"), exit()),
        "Add task": add_task,
        "View tasks": view_tasks,
        "Mark task complete": mark_task_complete,
        "Delete task": delete_task,
        "Export JSON": export_tasks_json,
        "Export CSV": export_tasks_csv,
    }

    # Get the menu in String format to show it to the operator
    menu = "\n".join([f"{i}. {list(options.keys())[i]}" for i in range(len(options))])

    while True:

        print("Tasks manager menu")
        print(menu)
        print("")
        choice = input("Enter your choice: ")

        # Check if operator's choice is valid
        if not choice.isdigit() or len(list(options.keys())) <= int(choice):
            print("Sorry the option you choose is not valid, please try again")
            continue
        selection = list(options.keys())[int(choice)]
        action = options.get(selection)

        print("")
        print(f"==== {selection.upper()} ======")
        action(tasks)

        print("\n=========================")
        input("Pres enter to continue")
        print("")
        clear_console()


if __name__ == "__main__":
    main()
