def addTasks():

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