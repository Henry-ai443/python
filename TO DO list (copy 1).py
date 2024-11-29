tasks = []

while True:
    print("\nMENU")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input ("Enter the task: ")
        tasks.append(task)
    elif choice == "2":
        if not tasks:
            print("No tasks to remove!")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}.{task}")
            task_num = int(input("Enter the task number to remove: "))
            if 1<= task_num < len(tasks):
                tasks.pop(task_num - 1)
            else:
                print("Invalid task number!")
    elif choice == "3":
        if not tasks:
            print("No tasks in the list!")
        else:
            print("Tasks:")
            for task in tasks:
                print(f"-{task}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input try again!")