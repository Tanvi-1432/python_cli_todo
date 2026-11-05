import json

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent = 4)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def menu():
    print("**********************\n"
          "* 1. Add a task      *\n"
          "* 2. Display tasks   *\n"
          "* 3. Delete a task   *\n"
          "* 4. Edit a task     *\n"
          "* 5. Complete a task *\n"
          "* 6. Quit            *\n"
          "**********************\n")

def user_choice():
    MAINMENU = {
        "1" : "add a task",
        "2" : "display tasks",
        "3" : "delete a task",
        "4" : "edit a task",
        "5" : "complete a task",
        "6" : "quit",
    }
    while True:
        menu()
        choice = input("Enter your choice(1, 2, 3, 4, 5, 6): ").strip().lower()
        if choice in MAINMENU:
            return MAINMENU[choice]
        else:
            print("Invalid choice. Please try again.")


def get_task(prompt):
    while True:
        task = input(prompt).strip()
        if task:
            return task

        print("Task cannot be empty. Please try again.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for index, task in enumerate(tasks, start = 1):
        print(f"{index}.{'[X]' if task['completed'] else '[ ]'} {task['task']}")

def get_task_index(tasks, prompt):
    while True:
        try:
            display_tasks(tasks)
            task_index = int(input(prompt).strip())
            if 1 <= task_index <= len(tasks):
                index = task_index - 1
                return index
            print("Invalid task. Please try again.")
        except ValueError:
            print("enter a valid task number.")

def exit_program():
    print("Goodbye!")

def main():
    tasks = load_tasks()
    while True:
        choice = user_choice()
        if choice == "add a task":
            task = get_task("Enter your task: ")
            tasks.append({"task": task, "completed": False})
            save_tasks(tasks)
        elif choice == "display tasks":
            if tasks:
                display_tasks(tasks)
            else:
                print("No tasks were found.")
        elif choice == "delete a task":
            if tasks:
                prompt = "Enter the index of the task you would like to delete: "
                index = get_task_index(tasks, prompt)
                deleted_task = tasks.pop(index)
                save_tasks(tasks)
                print(f"you have deleted: {index + 1}.{'[X]' if deleted_task['completed'] else '[ ]'} {deleted_task['task']}")
            else:
                print("There is no task for you to delete.")

        elif choice == "edit a task":
            if tasks:
                prompt = "Enter the index of the task you would like to edit: "
                edit_task_index = get_task_index(tasks, prompt)
                new_task = get_task("Enter your new task: ")
                tasks[edit_task_index]["task"] = new_task
                save_tasks(tasks)
            else:
                print("There is no task for you to edit.")

        elif choice == "complete a task":
            if tasks:
                prompt = "Enter the index of the task you would like to complete: "
                task_completed_index = get_task_index(tasks, prompt)
                if tasks[task_completed_index]["completed"]:
                    print("you have already completed the task.")
                else:
                    tasks[task_completed_index]["completed"] = True
                    save_tasks(tasks)
                    print(f"Completed: {tasks[task_completed_index]['task']}")
            else:
                print("There is no task for you to complete.")


        elif choice == "quit":
            exit_program()
            break

if __name__ == '__main__':
    main()
