import json

FILENAME = "tasks.json"


def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
 

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, task):
    task = task.strip()
    if task == "":
        return False

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1

    tasks.append({"id": new_id, "task": task})
    save_tasks(tasks)
    return True


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for t in tasks:
            print(f"{t['id']}. {t['task']}")


def show_menu():
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")


def main():
    my_tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose (1/2/3): ")

        if choice == "1":
            task = input("Write your task: ")
            if add_task(my_tasks, task):
                print("Task added successfully!")
            else:
                print("Task cannot be empty!")

        elif choice == "2":
            view_tasks(my_tasks)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
