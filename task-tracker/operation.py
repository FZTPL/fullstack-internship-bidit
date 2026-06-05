import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "w")
        json.dump([], file)
        file.close()

    file = open(FILE_NAME, "r")
    tasks = json.load(file)
    file.close()

    return tasks


def save_tasks(tasks):
    file = open(FILE_NAME, "w")
    json.dump(tasks, file, indent=4)
    file.close()


def add_task(description):
    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo"
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def update_task(task_id, description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            save_tasks(tasks)
            print("Task updated successfully.")
            return

    print("Task not found.")


def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    print("Task not found.")


def mark_in_progress(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            save_tasks(tasks)
            print("Task marked as in progress.")
            return

    print("Task not found.")


def mark_done(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print("Task marked as done.")
            return

    print("Task not found.")


def list_tasks(status=None):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:

        if status is None:
            print(task["id"], "-", task["description"], "-", task["status"])

        elif task["status"] == status:
            print(task["id"], "-", task["description"], "-", task["status"])