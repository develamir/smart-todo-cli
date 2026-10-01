import json

FILE_NAME = "data.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(title):
    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)


def show_tasks():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo tasks found.")
        return

    print("\n========== TASKS ==========")

    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f'{task["id"]}. [{status}] {task["title"]}')


def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("\nTask completed!")
            return

    print("\nTask not found.")


def delete_task(task_id):
    tasks = load_tasks()

    new_tasks = []

    for task in tasks:
        if task["id"] != task_id:
            new_tasks.append(task)

    if len(new_tasks) == len(tasks):
        print("\nTask not found.")
        return

    save_tasks(new_tasks)
    print("\nTask deleted!")


def search_tasks(keyword):
    tasks = load_tasks()

    results = []

    for task in tasks:
        if keyword.lower() in task["title"].lower():
            results.append(task)

    if len(results) == 0:
        print("\nNo matching tasks found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for task in results:
        status = "✓" if task["completed"] else " "
        print(f'{task["id"]}. [{status}] {task["title"]}')


def statistics():
    tasks = load_tasks()

    total = len(tasks)
    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    remaining = total - completed

    print("\n========== STATISTICS ==========")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Remaining: {remaining}")