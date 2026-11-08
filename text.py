
# Create the file if it doesn't exist
with open("tasks.txt", "a") as f:
    pass

# Display existing tasks
with open("tasks.txt", "r") as f:
    a = f.read()
    print(a)

print("\n\nEnter the option number:")
print("\t1. Enter new tasks.")
print("\t2. Mark one task as done.")
print("\t3. Clear all tasks.")
print("\t4. Exit.")

try:
    opt = int(input("Enter your option here: "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit


# OPTION 1: ADD NEW TASKS
if opt == 1:
    try:
        nof = int(input("Enter the number of tasks to be added: "))
    except ValueError:
        print("Enter a valid number!")
        raise SystemExit

    if nof <= 0:
        print("Enter a number greater than 0!")

    else:
        print("Enter your tasks!")

        with open("tasks.txt", "a") as f:
            for i in range(nof):
                task = input(f"{i + 1}. ")

                if task.strip():
                    f.write(f"[ ] {task.strip()}\n")

        print("Done!")


# OPTION 2: MARK A TASK AS DONE
elif opt == 2:

    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f if line.strip()]

    if not tasks:
        print("No tasks available!")

    else:
        # Add checkboxes to old tasks if necessary
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
            raise SystemExit

        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number!")

        elif tasks[task_no - 1].startswith("[✓] "):
            print("This task is already completed!")

        else:
            tasks[task_no - 1] = "[✓] " + tasks[task_no - 1][4:]

            with open("tasks.txt", "w") as f:
                f.write("\n".join(tasks) + "\n")

            print("Task marked as done!")


# OPTION 3: CLEAR ALL TASKS
elif opt == 3:

    confirm = input("Are you sure you want to clear all tasks? (y/n): ")

    if confirm.lower() == "y":
        with open("tasks.txt", "w") as f:
            pass

        print("All tasks cleared!")

    else:
        print("Operation cancelled.")


# OPTION 4: EXIT
elif opt == 4:
    print("Exiting application...")

else:
    print("Invalid option!")
