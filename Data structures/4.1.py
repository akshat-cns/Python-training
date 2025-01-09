def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f" {task['title']} - {'Completed' if task['completed'] else 'Pending'}")


def add_task(tasks):
    title = input("\nEnter the task title: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added!")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_num = int(input("\nEnter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        new_title = input("Enter the new title: ")
        if new_title:
            tasks[task_num]["title"] = new_title
        status = input("Mark as completed? (yes/no): ").strip().lower()
        if status == "yes":
            tasks[task_num]["completed"] = True
        elif status == "no":
            tasks[task_num]["completed"] = False
        print("Task updated!")
    else:
        print("Invalid task number!")



def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task['title']}' removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    tasks = []
    while True:
        print(''' \nTo-Do List Manager:
    1. View tasks
    2. Add a task
    3. Update a task
    4. Remove a task
    5. Exit ''')
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            remove_task(tasks)
        elif choice == 5:
            print("Exit!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()