__version__ = "2.1.0"

import os
from enum import Enum

FILE_NAME="tasks_file.txt"

tasks_dict={}
keys_sorted_by_priority=[]

ALL, COMPLETED, UNCOMPLETED = 0,1,2
SORTED=True
UP_TO_DATE=True
MODIFIED_ITEM=False


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

def refresh_keys(force=False):
    global SORTED, MODIFIED_ITEM, keys_sorted_by_priority
    if MODIFIED_ITEM or force:
        keys_sorted_by_priority=[
            (info["priority"], task_name) for task_name, info in tasks_dict.items()]
        MODIFIED_ITEM=False
        SORTED=False

def sort_keys(force=False):
    global SORTED
    if not SORTED or force:
        keys_sorted_by_priority.sort()
        SORTED=True

def list_tasks(choice) -> bool:
    global ALL, COMPLETED, MODIFIED_ITEM
    refresh_keys()
    sort_keys()
    exist=False
    if choice == ALL:
        for _, task_name in keys_sorted_by_priority:
            info=tasks_dict.get(task_name)
            if info["done"]:
                print(f"{task_name} : Completed.")
            else:
                print(f"{task_name} : Not completed.")
            exist=True
    else:
        choice = (choice == COMPLETED)
        for _, task_name in keys_sorted_by_priority:
            info=tasks_dict.get(task_name)
            if info["done"]==choice:
                print(f"{task_name}")
                exist=True
    return exist

def save_tasks():
    global UP_TO_DATE
    refresh_keys()
    sort_keys()
    with open(FILE_NAME,"w") as file:
        for _, task_name in keys_sorted_by_priority:
            info=tasks_dict.get(task_name)
            file.write(task_name+":"+str(info["done"])+":"+str(info["priority"])+"\n")
        file.write("end\n")
        for  key_priority, key_name in keys_sorted_by_priority:
            file.write(str(key_priority)+":"+key_name+"\n")
    UP_TO_DATE=True
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
                if not UP_TO_DATE:
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
                    priority=int(input("choose task priority (1-3) (1:more important): "))
                    if priority>=1 and priority<=3:
                        tasks_dict[task_name]={"done":False,"priority":priority}
                        keys_sorted_by_priority.append((priority,task_name))
                        MODIFIED_ITEM=True
                        SORTED=False
                        UP_TO_DATE=False
                        print("Task added successfully.")
                    else:
                        print("Invalid choice!")
                else:
                    print("Task name already exist!")
        case Menu.LIST_ALL.value:
            if tasks_dict:
                list_tasks(ALL)
            else:
                print("No taskes yet!")
        case Menu.LIST_COMPLETED.value:
            if tasks_dict:
                print("Completed tasks:")
                exist=list_tasks(COMPLETED)
                if not exist:
                    print("No task has been completed yet!")
            else:
                print("No taskes yet!")
        case Menu.LIST_UNCOMPLETED.value:
            if tasks_dict:
                print("Uncompleted tasks:")
                exist=list_tasks(UNCOMPLETED)
                if not exist:
                    print("All tasks has been completed!")
            else:
                print("No taskes yet!")
        case Menu.SEARCH_BY_KEYWORD.value:
            keyword=input("Enter a keyword: ").strip()
            if not keyword:
                print("Empty keyword is not allowed!")
            else:
                exist=False
                for task_name, info in tasks_dict.items():
                    if keyword.lower() in task_name.lower():
                        exist=True
                        if info["done"]:
                            print(f"{task_name} : Completed.")
                        else:
                            print(f"{task_name} : Not completed.")
                if not exist:
                    print("No such a task!")
        case Menu.MARK.value:
            task_name = str(input("Enter task name: ")).strip()
            if task_name in tasks_dict:
                tasks_dict[task_name]["done"]=True
                MODIFIED_ITEM=True
                UP_TO_DATE=False
                # If later were sorting based on "done" status
                # SORTED=False
                print("Task marked as DONE")
            else:
                print("Task does not exist")
        case Menu.EDITE.value:
            task_name=input("Enter task name: ").strip()
            if not task_name:
                print("Empty task name are not allowed!")
            else:
                if task_name in tasks_dict:
                    task_new_name=input("Enter a new name: ").strip()
                    if not task_new_name:
                        print("Empty task name are not allowed!")
                    else:
                        if task_new_name in tasks_dict:
                            print("Task name already exist.")
                        else:
                            info=tasks_dict.get(task_name)
                            del tasks_dict[task_name]
                            tasks_dict[task_new_name]=info
                            MODIFIED_ITEM=True
                            UP_TO_DATE=False
                            print("Task name has been changed successfully.")
                else:
                    print("Task name does not exist!")
        case Menu.DELETE.value:
            task_name=input("Enter task name: ").strip()
            if not task_name:
                print("Empty task name are not allowed!")
            else:
                if task_name in tasks_dict:
                    delete_choice = 1
                    if not tasks_dict[task_name]["done"]:
                        print("Task still uncompleted!")
                        print("Are you sure you want to delete it?")
                        print("1. Delete")
                        print("2. Cancel")
                        delete_choice = int(input(">"))

                    if delete_choice==1:
                        del tasks_dict[task_name]
                        UP_TO_DATE=False
                        MODIFIED_ITEM=True
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
                    keys_sorted_by_priority.clear()
                    with open(FILE_NAME,"r") as file:
                        for line in file:
                            line = line.strip()
                            if line == "end":
                                break
                            if line:
                                task_name, done_str, priority_str = line.split(":")
                                done= (done_str == "True")
                                priority= int(priority_str)
                                tasks_dict[task_name]={"done":done,"priority":priority}
                        for line in file:
                            line=line.strip()
                            if line:
                                priority_str, task_name=line.split(":")
                                keys_sorted_by_priority.append((int(priority_str),task_name))
                        if tasks_dict:
                            # refresh_keys(True)
                            sort_keys(True)
                            UP_TO_DATE=True
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
