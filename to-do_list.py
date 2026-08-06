def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as f:
            print(f.read())
    except:
        print("No tasks found")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        task = input("Enter task: ")
        add_task(task)

    elif ch == 2:
        view_tasks()

    else:
        break
