from mark_tasks import markTasks
from add_tasks import addTasks
from delete_tasks import deleteTasks


with open("tasks.txt", "a") as f:
    pass

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
    addTasks()

# OPTION 2: MARK A TASK AS DONE
elif opt == 2:
    markTasks()

# OPTION 3: CLEAR ALL TASKS
elif opt == 3:
    deleteTasks()

# OPTION 4: EXIT
elif opt == 4:
    print("Exiting application...")

else:
    print("Invalid option!")