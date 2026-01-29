import os

tasks={}

while True:
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Save")
    print("5. Load")
    print("0. Exit")
    choice = int(input(">"))

    match choice:
        case 0:
            break
        case 1:
            name = str(input("Enter task name: "))
            if name not in tasks:
                tasks[name]=False
                print("Task added successfully.")
            else:
                print("Task name already exist!")
        case 2:
            if tasks:
                for task_name, done in tasks.items():
                    if done:
                        print(f"{task_name} : Completed.")
                    else:
                        print(f"{task_name} : Not completed.")
            else:
                print("No taskes yet!")
        case 3:
            task_name = str(input("Enter task name: "))
            
            if task_name in tasks:
                if tasks[task_name]:
                    print("Task already Done!")
                else:
                    tasks[task_name]=True
                    print("Task marked as DONE.")
            else:
                print("Task does not exist!")
        case 4:
            if tasks:
                with open("tasks_file.txt","w") as file:
                    for task_name, status in tasks.items():
                        if status:
                            file.write(task_name+":"+"Completed"+"\n")
                        else:
                            file.write(task_name+":"+"Not completed"+"\n")
                print("Data Saved successfully.")
            else:
                print("Nothing to save!")
        case 5:
            if os.path.exists("tasks_file.txt"):
                load_choice=1
                if tasks:
                    print("you have some unsaved tasks!")
                    print("Are you sure you want to load.")
                    print("1. Load")
                    print("2. Cancel")
                    load_choice=int(input(">"))

                match load_choice:
                    case 1:
                        tasks.clear()
                        with open("tasks_file.txt","r") as file:
                            for line in file:
                                line = line.strip()
                                task_name, status_str = line.split(":")
                                #if status_str.lower()=="completed":
                                #    status=True
                                #else:
                                #    status=False
                                status=(status_str.lower()=="completed")
                                tasks[task_name]=status
                            print("Data loaded successfully.")
                    case _:
                        print("Load operation canceled!")
            else:
                print("No saved file found!")
        case _:
            print("Invalid choice!")
    print()

