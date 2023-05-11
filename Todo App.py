def show_menu():
    print("Todo List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks found.")
    else:
        print("Todo List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def mark_task_complete(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return

    task_index = get_valid_task_index(todo_list)
    if task_index is None:
        return

    task = todo_list[task_index]
    print(f"Marking task '{task}' as complete...")
    todo_list.pop(task_index)
    print("Task marked as complete!")

def delete_task(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return

    task_index = get_valid_task_index(todo_list)
    if task_index is None:
        return

    task = todo_list[task_index]
    print(f"Deleting task '{task}'...")
    todo_list.pop(task_index)
    print("Task deleted!")

def get_valid_task_index(todo_list):
    task_index = input("Enter the task number: ")
    try:
        task_index = int(task_index)
        if task_index < 1 or task_index > len(todo_list):
            print("Invalid task number.")
            return None
        return task_index - 1
    except ValueError:
        print("Invalid task number. Please enter a valid integer.")
        return None

def save_tasks_to_file(todo_list):
    filename = input("Enter the filename to save tasks: ")
    try:
        with open(filename, "w") as file:
            for task in todo_list:
                file.write(task + "\n")
        print("Tasks saved to file successfully!")
    except IOError:
        print("Error occurred while saving tasks to file.")

def load_tasks_from_file(todo_list):
    filename = input("Enter the filename to load tasks from: ")
    try:
        with open(filename, "r") as file:
            tasks = file.read().splitlines()
            todo_list.clear()
            todo_list.extend(tasks)
        print("Tasks loaded from file successfully!")
    except IOError:
        print("Error occurred while loading tasks from file.")

def todo_list_app():
    todo_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_task_complete(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            save_tasks_to_file(todo_list)
        elif choice == "6":
            load_tasks_from_file(todo_list)
        elif choice == "7":
            print("Exiting the todo list...")
            break
        else:
            print("Invalid choice. Please try again.")

todo_list_app()
