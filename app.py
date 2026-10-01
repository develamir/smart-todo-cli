from todo import (
    add_task,
    show_tasks,
    complete_task,
    delete_task,
    search_tasks,
    statistics
)


def menu():
    print("\n========================")
    print("       SMART TODO")
    print("========================")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Statistics")
    print("0. Exit")


while True:
    menu()

    choice = input("\nChoose: ")

    if choice == "1":
        title = input("Task title: ")

        if title:
            add_task(title)
            print("\nTask added successfully!")
        else:
            print("\nTask title cannot be empty.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        task_id = int(input("Task ID: "))
        complete_task(task_id)

    elif choice == "4":
        task_id = int(input("Task ID: "))
        delete_task(task_id)

    elif choice == "5":
        keyword = input("Search: ")
        search_tasks(keyword)

    elif choice == "6":
        statistics()

    elif choice == "0":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")