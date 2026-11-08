with open("text.txt", "r") as f:
    a = (f.read())
    print(a)

print("\n\nEnter the option number \n\t1. Enter new tasks. \n\t2. Mark one task as done. \n\t3. Clear all task. \n\t4. Exit.")

try:
    opt = int(input("Enter your option here: "))
except:
    raise ValueError("Enter a valid number!")

if opt == 1:
    try:
        nof = int(input("Enter the number of tasks to be added: "))
    except:
        raise ValueError("Enter a valid number!")
    
    print("Enter your task!")

    for i in range(0, nof):
        task = input("")
        with open("text.txt", "a") as f:
            f.write(f"\n{task}")
    print("Done!")
