__version__ = "2.0.1"

import os
from enum import Enum

FILE_NAME="tasks_file.txt"

tasks_dict={}

up_to_date=True


class Menu(Enum):
        EXIT=0
        ADD=1
        LIST_ALL=2
        LIST_COMPLETED=3
        LIST_UNCOMPLETED=4
        SEARCH_BY_KEYWORD=5
        MARK=6
        EDITE=7
        DELETE=8
        SAVE=9
        LOAD=10

def list_tasks(choice) -> bool:
    exist=False
    for task_name, status in tasks_dict.items():
        if status==choice:
            print(f"{task_name}")
            exist=True
    return exist

def save_tasks():
    with open(FILE_NAME,"w") as file:
        for task_name, status in tasks_dict.items():
            if status:
                file.write(task_name+":"+"True"+"\n")
            else:
                file.write(task_name+":"+"False"+"\n")
    global up_to_date
    up_to_date=True
    print("Data Saved successfully.")

while True:
    print("1 . Add task")
    print("2 . List all tasks")
    print("3 . List completed tasks")
    print("4 . List uncompleted tasks")
    print("5 . Search task by keyword")
    print("6 . Mark task as done")
    print("7 . Edite task name")
    print("8 . Delete task")
    print("9 . Save")
    print("10. Load")
    print("0 . Exit")              
    choice = int(input(">"))     

    
    match choice:
        case Menu.EXIT.value:
                if not up_to_date:
                    print(up_to_date)
                    exit_choice=3
                    print("What should happen to your unsaved changes")
                    print("1. Save")
                    print("2. Discard")
                    print("3. Cancel")
                    exit_choice=int(input(">"))
                    if exit_choice==1:
                        save_tasks()
                        break
                    elif exit_choice==2:
                        break
                    else:
                        print("Exiting cancelled ")
                else:
                    break
        case Menu.ADD.value:
            task_name = str(input("Enter task name: ")).strip()
            if not task_name:
                print("Empty task name are not allowed!")
            else:
                if task_name not in tasks_dict:
                    tasks_dict[task_name]=False
                    up_to_date=False
                    print("Task added successfully.")
                else:
                    print("Task name already exist!")
        case Menu.LIST_ALL.value:
            if tasks_dict:
                for task_name, done in tasks_dict.items():
                    if done:
                        print(f"{task_name} : Completed.")
                    else:
                        print(f"{task_name} : Not completed.")
            else:
                print("No taskes yet!")
        case Menu.LIST_COMPLETED.value:
            if tasks_dict:
                exist=list_tasks(True)
                if not exist:
                    print("No task has been completed yet!")
            else:
                print("No taskes yet!")
        case Menu.LIST_UNCOMPLETED.value:
            if tasks_dict:
                exist=list_tasks(False)
                if not exist:
                    print("All tasks has been completed!")
            else:
                print("No taskes yet!")
        case Menu.SEARCH_BY_KEYWORD.value:
            keyword=input("Enter a keyword: ").strip()
            exist=False
            for task_name, status in tasks_dict.items():
                if keyword.lower() in task_name.lower():
                    exist=True
                    if status:
                        print(f"{task_name} : Completed.")
                    else:
                        print(f"{task_name} : Not completed.")
            if not exist:
                print("No such a task!")
        case Menu.MARK.value:
            task_name = str(input("Enter task name: "))
            if task_name in tasks_dict:
                tasks_dict[task_name]=True
                up_to_date=False
                print("Task marked as DONE")
            else:
                print("Task does not exist")
        case Menu.EDITE.value:
            task_name=input("Enter task name: ")
            if task_name in tasks_dict:
                task_new_name=input("Enter a new name: ").strip()
                if not task_new_name:
                    print("Empty task name are not allowed!")
                else:    
                    if task_new_name in tasks_dict:
                        print("Task name already exist.")
                    else:    
                        status=tasks_dict[task_name]
                        del tasks_dict[task_name]
                        tasks_dict[task_new_name]=status
                        up_to_date=False
                        print("Task name has been changed successfully.")
            else:
                print("Task name does not exist!")

        case Menu.DELETE.value:
            task_name=input("Enter task name: ")
            if task_name in tasks_dict:
                delete_choice = 1
                if not tasks_dict[task_name]:
                    print("Task still uncompleted!")
                    print("Are you sure you want to delete it?")
                    print("1. Delete")
                    print("2. Cancel")
                    delete_choice = int(input(">"))

                if delete_choice==1:
                    del tasks_dict[task_name]
                    up_to_date=False
                    print("Task deleted successfully.")
                else:
                    print("Delete operation canceled.")
            else:
                print("Task does not exist!")
        case Menu.SAVE.value:
            if tasks_dict:
               save_tasks()
            else:
                print("Nothing to save!")
        case Menu.LOAD.value:
            if os.path.exists("tasks_file.txt"):
                load_choice=1
                if tasks_dict:
                    print("you have some unsaved tasks!")
                    print("Are you sure you want to load.")
                    print("1. Load")
                    print("2. Cancel")
                    load_choice=int(input(">"))

                if load_choice == 1:
                    tasks_dict.clear()
                    with open(FILE_NAME,"r") as file:
                        for line in file:
                            line = line.strip()
                            if line:
                                task_name, status_str = line.split(":")
                                status= (status_str == "True")
                                tasks_dict[task_name]=status
                        if tasks_dict:
                            up_to_date=True
                            print("Data loaded successfully.")
                        else:
                            print("No data to load!")
                else:
                    print("Load operation canceled!")
            else:
                print("No saved file found!")
        case _:
            print("Invalid choice!")
    print()
