tasks = []

while True:
    print("\ntask manager")
    print("1. add task")
    print("2. view tasks")
    print("3. remove task")
    print("q. quit")

    choice = input("\nchoose an action: ")

    if choice == "1":
        task = input("enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if tasks:
            print("\nyour tasks:")
            for i, t in enumerate(tasks, 1):
                print(i, '.', t)
        else:
            print("no tasks yet!")

    elif choice == "3":
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(i, '.', t)
            num = int(input("enter task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("task removed")
            else:
                print("invalid number")
        else:
            print("no tasks to remove")

    elif choice == "q":
        print("goodbye")
        break

    else:
        print("invalid choice")
