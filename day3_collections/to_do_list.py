tasks = []

while True:
    print("\n----- To-Do List -----")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    answer = input("Choose an option: ")

    if answer == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")

    elif answer == "2":
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")

    elif answer == "3":
        if not tasks:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif answer == "4":
        print("Goodbye!")
        break

    else:
        print("Incorrect input.")
