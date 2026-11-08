import os


print("Welcome to To-Do application\n")
print("Type your choice number: \n 1. Make a new to-do list.\n 2. See an existing list. \n 3. Delete a list." )

try:
    opt = int(input("Enter your choice: "))
except:
    raise ValueError("Enter a valid number!")

if opt == 2:

    folder = "folder"

    files = os.listdir(folder)

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")

    try:
        n = int(input("Enter the index of the file: "))
    except:
        raise ValueError("Enter a valid number!")
    