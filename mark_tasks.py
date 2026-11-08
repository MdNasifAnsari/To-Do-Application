def markTasks():

    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f if line.strip()]

    if not tasks:
        print("No tasks available!")
        return

    # Add checkboxes to tasks if necessary
    for i in range(len(tasks)):
        if not tasks[i].startswith(("[ ] ", "[✓] ")):
            tasks[i] = "[ ] " + tasks[i]

    print("\nYour Tasks:")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    try:
        task_no = int(input("\nEnter the task number to mark as done: "))
    except ValueError:
        print("Enter a valid number!")
        return

    if task_no < 1 or task_no > len(tasks):
        print("Invalid task number!")

    elif tasks[task_no - 1].startswith("[✓] "):
        print("This task is already completed!")

    else:
        tasks[task_no - 1] = "[✓] " + tasks[task_no - 1][4:]

        with open("tasks.txt", "w") as f:
            f.write("\n".join(tasks) + "\n")

        print("Task marked as done!")