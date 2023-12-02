# to-do list application

# create a list to store tasks
tasks = []

# add a task
def add_task(title, description):
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)

# list tasks
def list_tasks():
    for task in tasks:
        print(f"{task['title']}: {task['description']}")

# mark a task as complete
def mark_task_complete(task_id):
    task = tasks[task_id]
    task["completed"] = True

# delete a task
def delete_task(task_id):
    tasks.pop(task_id)

# save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['title']},{task['description']},{task['completed']}\n")

# load tasks from a file
def load_tasks():
    with open("tasks.txt", "r") as f:
        for line in f:
            task = line.split(",")
            tasks.append({"title": task[0], "description": task[1], "completed": task[2]})

# main function
def main():
    # load tasks from file
    load_tasks()

    # display menu
    while True:
        print("To-Do List Application")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Save tasks")
        print("6. Exit")

        # get user input
        choice = input("Enter your choice: ")

        # perform the selected action
        if choice == "1":
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")
            print()
            add_task(title, description)
        elif choice == "2":
            list_tasks()
            print()
        elif choice == "3":
            task_id = int(input("Enter the ID of the task to mark as complete: "))
            print()
            mark_task_complete(task_id)
        elif choice == "4":
            task_id = int(input("Enter the ID of the task to delete: "))
            print()
            delete_task(task_id)
        elif choice == "5":
            save_tasks()
            print()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == "__main__":
    main()