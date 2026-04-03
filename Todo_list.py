import json

try:
    with open("tasks.txt", "r") as f:
        tasks = json.load(f)
except:
    tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks")
        else:
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Deleted")
        else:
            print("Invalid number")

    elif choice == "4":
        with open("tasks.txt", "w") as f:
            json.dump(tasks, f)
        print("Saved & Exiting")
        break