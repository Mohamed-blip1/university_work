__version__ = "2.2.0"

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
        EXIT="0"
        ADD="1"
        LIST_ALL="2"
        LIST_COMPLETED="3"
        LIST_UNCOMPLETED="4"
        SEARCH_BY_KEYWORD="5"
        MARK="6"
        EDITE="7"
        DELETE="8"
        SAVE="9"
        LOAD="10"
        MENU="m"

def refresh_keys(force : bool =False):
    global SORTED, MODIFIED_ITEM, keys_sorted_by_priority

    if MODIFIED_ITEM or force:
        keys_sorted_by_priority.clear()
        keys_sorted_by_priority.extend(
            (info["priority"], task_name) for task_name, info in tasks_dict.items())
    
        MODIFIED_ITEM=False
        SORTED=False

def sort_keys(force: bool =False):
    global SORTED
    if not SORTED or force:
        keys_sorted_by_priority.sort()
        SORTED=True

def get_tasks(choice) -> list:
    """Choices are : ALL, COMPLETED, UNCOMPLETED"""

    refresh_keys()
    sort_keys()

    if choice == ALL:
        return [(task_name, tasks_dict[task_name]) for _, task_name in keys_sorted_by_priority]
    else:
        status = (choice == COMPLETED)
        return [(task_name, tasks_dict[task_name]) for _, task_name in keys_sorted_by_priority
                                                    if  tasks_dict[task_name]["done"]==status]

def get_tasks_by_keyword(keyword: str):
    
    refresh_keys()
    sort_keys()

    return [(task_name, tasks_dict[task_name]) for _, task_name in keys_sorted_by_priority
                                                if keyword.lower() in task_name.lower()]

def add_task(task_name: str, priority: int) -> bool:
    global MODIFIED_ITEM, UP_TO_DATE, SORTED

    if task_name in tasks_dict:
        return False

    tasks_dict[task_name]={"done":False,"priority":priority}
    keys_sorted_by_priority.append((priority,task_name))

    MODIFIED_ITEM=True
    UP_TO_DATE=False
    SORTED=False

    return True

def edit_task_status(task_name: str, new_status: bool) -> bool:
    global MODIFIED_ITEM, UP_TO_DATE

    if task_name not in tasks_dict:
        return False

    tasks_dict[task_name]["done"] = new_status

    # If later were sorting based on "done" status
    # SORTED=False

    MODIFIED_ITEM=True
    UP_TO_DATE=False

    return True

def edit_task_name(old_name: str, new_name: str) -> bool:
    """
    Renames a task. Returns True if successful, False otherwise
    """
    global MODIFIED_ITEM, UP_TO_DATE, SORTED
    
    if old_name not in tasks_dict or new_name in tasks_dict:
        return False
    
    tasks_dict[new_name] = tasks_dict.pop(old_name)
    
    MODIFIED_ITEM=True
    UP_TO_DATE=False
    SORTED=False

    return True

def delete_task(task_name: str) -> bool:
    global UP_TO_DATE, MODIFIED_ITEM, SORTED

    if tasks_dict.pop(task_name,None) is not None:
        UP_TO_DATE=False
        MODIFIED_ITEM=True
        SORTED=False
        return True

    return False

def save_tasks() -> bool:
    global UP_TO_DATE

    refresh_keys()
    sort_keys()

    with open(FILE_NAME,"w") as file:
        for task_name, info in get_tasks(ALL):
            file.write(task_name+":"+str(info["done"])+":"+str(info["priority"])+"\n")

    UP_TO_DATE=True

    return True

def load_tasks() -> bool:
    global UP_TO_DATE

    if not os.path.exists(FILE_NAME):
        return False
    
    tasks_dict.clear()
    with open(FILE_NAME,"r") as file:
        for line in file:
            line = line.strip()
            if line:
                task_name, done_str, priority_str = line.split(":")
                done= (done_str == "True")
                priority= int(priority_str)
                tasks_dict[task_name]={"done":done,"priority":priority}

    refresh_keys(force=True)
    sort_keys(force=True)
    
    UP_TO_DATE=True

    return True    

def menu():
    print("[1] . Add task")
    print("[2] . List all tasks")
    print("[3] . List completed tasks")
    print("[4] . List uncompleted tasks")
    print("[5] . Search task by keyword")
    print("[6] . Mark task as done")
    print("[7] . Edite task name")
    print("[8] . Delete task")
    print("[9] . Save")
    print("[10]. Load")
    print("[0] . Exit")

menu()
while True:
    print()
    print("[m] Menu")
    choice = input(">")
    
    match choice:
        case Menu.MENU.value:
            menu()
        case Menu.EXIT.value:
                if not UP_TO_DATE:
                    exit_choice="3"
                    print("Warning: Unsaved changes!")
                    print("1. Save")
                    print("2. Discard")
                    print("3. Cancel")
                    exit_choice = input(">")
                    if exit_choice == "1":
                        save_tasks()
                        break
                    elif exit_choice == "2":
                        break
                    else:
                        print("✗ Failed to Exit.")
                else:
                    break

        case Menu.ADD.value:
            task_name = input("Enter task name: ").strip()
            if not task_name:
                print("Empty task name not allowed!")
                continue
            
            priority = input("choose task priority (1-3): ")
            if not ("1" <= priority <= "3"):
                print("Invalid priority!")
                continue

            priority = int(priority)
            if add_task(task_name, priority):
                print("Task added successfully.")
            else:
                print("Task already exist!")

        case Menu.LIST_ALL.value:
            if tasks_dict:
                print(f"\n--- ({len(tasks_dict)}) Task ---")
                
                for task_name, info in get_tasks(ALL):
                    status = "✓ Completed" if info["done"] else "✗ Pending"
                    print(f"[{status}] {task_name}")
            else:
                print("No taskes yet!")

        case Menu.LIST_COMPLETED.value:
            if tasks_dict:
                tasks = get_tasks(COMPLETED)

                if not tasks:
                    print("No task has been completed yet!")
                    continue

                print(f"--- ✓ Completed tasks ({len(tasks)}) ---")
                for task_name, _ in tasks:
                    print(task_name)

            else:
                print("No taskes yet!")

        case Menu.LIST_UNCOMPLETED.value:
            if tasks_dict:
                tasks = get_tasks(UNCOMPLETED)

                if not tasks:
                    print("All tasks has been completed!")
                    continue

                print(f"--- ✗ Pending tasks ({len(tasks)}) ---")
                for task_name, _ in tasks:
                    print(task_name)

            else:
                print("No taskes yet!")

        case Menu.SEARCH_BY_KEYWORD.value:
            keyword=input("Enter a keyword: ").strip()

            if not keyword:
                print("Error: Empty keyword is not allowed!")
                continue

            tasks = get_tasks_by_keyword(keyword)

            if not tasks:
                print(f"No tasks found matching: '{keyword}'")

            print(f"\n--- Search Results ({len(tasks)}) ---")
            for task_name, info in tasks:
                status = "✓ Completed" if info["done"] else "✗ Pending"
                print(f"[{status}] {task_name}")

        case Menu.MARK.value:
            task_name = str(input("Enter task name: ")).strip()

            if edit_task_status(task_name, True):
                print("Task marked as ✓ DONE")
            else:
                print("Task does not exist")

        case Menu.EDITE.value:
            old_name=input("Enter task name: ").strip()
            new_name=input("Enter a new name: ").strip()

            if not old_name or not new_name:
                print("Error: Task names cannot be empty!")
                continue

            if edit_task_name(old_name, new_name):
               print(f"Success: '{old_name}' renamed to '{new_name}'.")
            else:
                print("Error: Could not rename. Either the task doesn't exist or the name is taken.")

        case Menu.DELETE.value:
            task_name=input("Enter task name: ").strip()

            task_data = tasks_dict.get(task_name)
            if not task_data:
                print("Error: Task does not exist!")
                continue

            should_delete = True
            if not task_data["done"]:
                print(f"Warning: Task '{task_name}' is still [✗ Pending]!")
                choice = input("Are you sure you want to delete? (1: Yes, 2: No): ")
                if choice != "1":
                    should_delete = False

            if should_delete:
                if delete_task(task_name):
                    print("Task deleted successfully.")
                else:
                    print("Error: Task could not be deleted.")
            else:
                print("Delete operation canceled.")

        case Menu.SAVE.value:
                
                if not tasks_dict:
                    confirm = input(f"Tasks list empty. Save anyway to clear file? (y/n): ").lower()
                    if confirm != 'y':
                        print("✗ Failed to save data.")
                        continue
                
                if save_tasks():
                    print("✓ Data synchronized to disk.")
                else:
                    print("✗ Failed to save data.")

        case Menu.LOAD.value:

            if tasks_dict:
                print("Warning: unsaved data detected!")
                confirm = input("Are you sure you want to load? (y/n): ")
                if confirm != "y":
                    print("✗ Failed to load data.")
                    continue

            if load_tasks():
                print("✓ Data loaded successfully.")
            else:
                print("✗ Failed to load data.")
                print(f"Error: '{FILE_NAME}' file does not exist.")

        case _:
            print("Error: Invalid choice!")

print()
