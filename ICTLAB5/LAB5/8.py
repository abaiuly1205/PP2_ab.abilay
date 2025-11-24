tasks = []

while True:
    print("\nTask Manager")
    print("1. Add")
    print("2. View")
    print("3. Remove")
    print("q. Quit")

    choice = input("\nChoose an action: ")

    if choice == "1":
        task = input("enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if tasks:
            print("\nTasks:")
            for i, t in enumerate(tasks, 1):
                print(i, '.', t)
        else:
            print("There is no tasks yet!")

    elif choice == "3":
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(i, '.', t)
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("The task was successfully removed.")
            else:
                print("Invalid number, try again")
        else:
            print("There is no tasks to remove.")

    elif choice == "q":
        print("Bye!")
        break

    else:
        print("Invalid choice")