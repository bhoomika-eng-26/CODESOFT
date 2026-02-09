tasks = []

def menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added 👍")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                removed_task = tasks.pop(num - 1)
                print(f"Deleted task: {removed_task}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using the To-Do List 😊")
        break

    else:
        print("Please enter a valid option.")
