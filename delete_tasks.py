def deleteTasks():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ")
    
    if confirm.lower() == "y":
        with open("tasks.txt", "w") as f:
            pass

        print("All tasks cleared!")
    
    else:
        print("Operation cancelled.")