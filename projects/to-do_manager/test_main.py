import main
import os

# Test sort_keys() and refresh_keys()--------------------------

def test_sort_keys():

    main.keys_sorted_by_priority.clear()

    main.keys_sorted_by_priority.append((3,"priority 3"))
    main.keys_sorted_by_priority.append((1,"priority 1"))
    main.keys_sorted_by_priority.append((2,"priority 2"))

    main.SORTED=False

    main.sort_keys()

    assert main.SORTED
    assert main.keys_sorted_by_priority == [(1,"priority 1"),(2,"priority 2"),(3,"priority 3")]

    print("test_sorted_keys passe!")

def test_forced_sort_keys():

    main.keys_sorted_by_priority.clear()

    main.keys_sorted_by_priority.append((3,"priority 3"))
    main.keys_sorted_by_priority.append((1,"priority 1"))
    main.keys_sorted_by_priority.append((2,"priority 2"))

    main.SORTED=True

    main.sort_keys(True)

    assert main.SORTED
    assert main.keys_sorted_by_priority == [(1,"priority 1"),(2,"priority 2"),(3,"priority 3")]

    print("test_forced_sorted_keys passe!")

test_sort_keys()
test_forced_sort_keys()
print("done testing sort_keys()")
print()

def test_refresh_keys():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()

    main.tasks_dict["item3"]={"done":False,"priority":3}
    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.tasks_dict["item2"]={"done":True,"priority":2}

    main.SORTED = True
    main.MODIFIED_ITEM = True

    main.refresh_keys()

    assert not main.MODIFIED_ITEM
    assert not main.SORTED
    assert main.keys_sorted_by_priority == [(3,"item3"), (1,"item1"),(2,"item2")]

    print("test_refresh_keys passe!")

def test_forced_refresh_keys():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()

    main.tasks_dict["item3"]={"done":False,"priority":3}
    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.tasks_dict["item2"]={"done":True,"priority":2}

    main.SORTED = True
    main.MODIFIED_ITEM = False

    main.refresh_keys(True)

    assert not main.MODIFIED_ITEM
    assert not main.SORTED
    assert main.keys_sorted_by_priority == [(3,"item3"), (1,"item1"),(2,"item2")]

    print("test_forced_refresh_keys passe!")

test_refresh_keys()
test_forced_refresh_keys()
print("done testing refresh_keys()")
print()

# Test add_task()--------------------------

def test_add_task():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()

    main.MODIFIED_ITEM = False
    main.UP_TO_DATE = True
    main.SORTED = True

    success = main.add_task("math",2)

    assert success
    assert "math" in main.tasks_dict
    assert main.tasks_dict["math"]["done"] == False
    assert main.tasks_dict["math"]["priority"] == 2
    assert main.keys_sorted_by_priority == [(2,"math")]

    assert main.MODIFIED_ITEM == True
    assert main.UP_TO_DATE == False
    assert main.SORTED == False

    print("test_add_task passed!")

def test_add_duplicate_task():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()

    main.tasks_dict["python"]={ "done" : False, "priority" : 1 }
    main.keys_sorted_by_priority.append((1,"python"))

    main.MODIFIED_ITEM = False
    main.UP_TO_DATE = True
    main.SORTED = True

    success = main.add_task("python",1)

    assert not success
    assert len(main.tasks_dict) == 1
    assert len(main.keys_sorted_by_priority) == 1

    assert main.MODIFIED_ITEM == False
    assert main.UP_TO_DATE == True
    assert main.SORTED == True

    print("test_add_duplicate_task passsed!")

test_add_task()
test_add_duplicate_task()
print("done testing add_task()")
print()

# Test get_tasks() and get_tasks_by_keyword() --------------------------

def test_get_tasks_all():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()
    
    main.tasks_dict["item3"]={"done":False,"priority":3}
    main.keys_sorted_by_priority.append((3,"item3"))
    
    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.keys_sorted_by_priority.append((1,"item1"))
    
    main.tasks_dict["item2"]={"done":True,"priority":2}
    main.keys_sorted_by_priority.append((2,"item2"))

    main.MODIFIED_ITEM = True
    main.SORTED = False

    getted_tasks = main.get_tasks(main.ALL)

    assert getted_tasks == [
        ("item1", {"done":False,"priority":1}),
        ("item2", {"done":True,"priority":2}),
        ("item3", {"done":False,"priority":3})
        ]

    print("test_get_tasks_all passed!")

def test_get_tasks_completed():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()
    
    main.tasks_dict["item3"]={"done":True,"priority":3}
    main.keys_sorted_by_priority.append((3,"item3"))
    
    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.keys_sorted_by_priority.append((1,"item1"))
    
    main.tasks_dict["item2"]={"done":True,"priority":2}
    main.keys_sorted_by_priority.append((2,"item2"))

    main.MODIFIED_ITEM = True
    main.SORTED = False

    getted_tasks = main.get_tasks(main.COMPLETED)

    assert getted_tasks == [
        ("item2", {"done":True,"priority":2}),
        ("item3", {"done":True,"priority":3})
        ]
    
    print("test_get_tasks_completed passed!")
    

def test_get_tasks_uncompleted():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()
    
    main.tasks_dict["item3"]={"done":False,"priority":3}
    main.keys_sorted_by_priority.append((3,"item3"))
    
    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.keys_sorted_by_priority.append((1,"item1"))
    
    main.tasks_dict["item2"]={"done":True,"priority":2}
    main.keys_sorted_by_priority.append((2,"item2"))

    main.MODIFIED_ITEM = True
    main.SORTED = False

    getted_tasks = main.get_tasks(main.UNCOMPLETED)

    assert getted_tasks == [
        ("item1", {"done":False,"priority":1}),
        ("item3", {"done":False,"priority":3})
        ]

    print("test_get_tasks_uncompleted passed!")

test_get_tasks_all()
test_get_tasks_completed()
test_get_tasks_uncompleted()
print("done testing get_tasks()")
print()

# Test get_tasks_by_keyword()--------------------------

def test_get_tasks_by_keyword():
        
    main.tasks_dict.clear()
    
    main.tasks_dict["item3"]={"done":False,"priority":3}
    main.tasks_dict["some3"]={"done":False,"priority":3}
    
    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.tasks_dict["some1"]={"done":False,"priority":1}

    main.tasks_dict["item2"]={"done":True,"priority":2}
    main.tasks_dict["some2"]={"done":True,"priority":2}

    main.keys_sorted_by_priority.append((3,"item3"))
    main.keys_sorted_by_priority.append((3,"some3"))

    main.keys_sorted_by_priority.append((2,"item2"))
    main.keys_sorted_by_priority.append((2,"some2"))
    
    main.keys_sorted_by_priority.append((1,"item1"))
    main.keys_sorted_by_priority.append((1,"some1"))

    main.SORTED = False
    main.MODIFIED_ITEM = True

    getted_tasks = main.get_tasks_by_keyword("me")

    assert getted_tasks == [
        ("some1", {"done":False,"priority":1}),
        ("some2", {"done":True,"priority":2}),
        ("some3", {"done":False,"priority":3})
    ]

    print("test_get_tasks_by_keyword passed!")

test_get_tasks_by_keyword()
print("done testing get_tasks_by_keyword()")
print()

# Test edit_task_status()--------------------------

def test_edit_task_status():

    main.tasks_dict.clear()

    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.tasks_dict["item2"]={"done":True,"priority":2}
    
    main.UP_TO_DATE = True
    main.MODIFIED_ITEM = False

    # Task does not exist case
    case1 = main.edit_task_status("some",True)
    
    assert not case1
    assert main.tasks_dict.get("some") == None

    assert main.UP_TO_DATE == True
    assert main.MODIFIED_ITEM == False
    
    case2 = main.edit_task_status("item1",True)
    case3 = main.edit_task_status("item2",False)
    
    assert case2
    assert case3
    assert main.tasks_dict["item1"] == {"done":True,"priority":1}
    assert main.tasks_dict["item2"] == {"done":False,"priority":2}
    
    assert main.UP_TO_DATE == False
    assert main.MODIFIED_ITEM == True

    print("test_edit_task_status passed!")

test_edit_task_status()
print("done testing edit_task_status()")
print()

# Test edit_task_name()--------------------------

def test_edit_task_name():

    main.tasks_dict.clear()
    main.keys_sorted_by_priority.clear()

    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.tasks_dict["item2"]={"done":True,"priority":2}
    main.tasks_dict["item3"]={"done":False,"priority":3}

    old_tasks = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}

    main.MODIFIED_ITEM=False
    main.UP_TO_DATE=True
    main.SORTED=True

    # Not existing task case
    case1 = main.edit_task_name("","some")
    
    tasks_case1 = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}

    assert tasks_case1 == old_tasks
    assert not case1
    assert main.MODIFIED_ITEM == False
    assert main.UP_TO_DATE == True
    assert main.SORTED == True
    
    # Taking name case
    case2 = main.edit_task_name("item1","item2")
    
    tasks_case2 = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}

    assert tasks_case2 == old_tasks
    assert not case2
    assert main.MODIFIED_ITEM == False
    assert main.UP_TO_DATE == True
    assert main.SORTED == True

    # Success case
    case3 = main.edit_task_name("item1","some1")
    case3 = main.edit_task_name("item2","some2")
    case3 = main.edit_task_name("item3","some3")
    
    tasks_case3 = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}

    expected = {('some1', False, 1), ('some2', True, 2), ('some3', False, 3)}
    
    assert tasks_case3 == expected
    assert case3

    assert main.MODIFIED_ITEM == True
    assert main.UP_TO_DATE == False
    assert main.SORTED == False

    print("test_edit_task_name passed!")

test_edit_task_name()
print("done testing edit_task_name()")
print()

# Test delete_task()--------------------------

def test_delete_task():

    main.tasks_dict.clear()

    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.tasks_dict["item2"]={"done":True,"priority":2}
    main.tasks_dict["item3"]={"done":False,"priority":3}

    old_tasks = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}

    main.MODIFIED_ITEM = False
    main.UP_TO_DATE = True
    main.SORTED = True

    # Task does not exist case
    case1 = main.delete_task("some")

    tasks_case1 = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}
    
    assert not case1
    assert old_tasks == tasks_case1

    assert main.MODIFIED_ITEM == False
    assert main.UP_TO_DATE == True
    assert main.SORTED == True

    # Task does not exist case
    case2 = main.delete_task("item2")

    tasks_case2 = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}
    expected = {('item1', False, 1), ('item3', False, 3)}    

    assert case2
    assert tasks_case2 == expected

    assert main.MODIFIED_ITEM == True
    assert main.UP_TO_DATE == False
    assert main.SORTED == False

    print("test_delete_task passed!")

test_delete_task()
print("done testing delete_task()")
print()

# Test save_tasks() & load_tasks()--------------------------

FILENAME = "test_main_file.txt"

def test_save_tasks_and_load_tasks ():

    if os.path.exists(FILENAME):
        os.remove(FILENAME)
   
    main.tasks_dict.clear()
    main.FILE_NAME=FILENAME

    main.tasks_dict["item1"]={"done":False,"priority":1}
    main.tasks_dict["item2"]={"done":True,"priority":2}
    main.tasks_dict["item3"]={"done":False,"priority":3}

    main.UP_TO_DATE = False

    main.save_tasks()
    assert main.UP_TO_DATE == True

    # File not found case
    main.tasks_dict.clear()
    main.UP_TO_DATE = False
    main.FILE_NAME = "some.txt"

    case1 = main.load_tasks()

    tasks = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}

    assert main.UP_TO_DATE == False
    assert not case1
    assert not tasks
    
    # Success load case
    main.tasks_dict.clear()
    main.UP_TO_DATE = False
    main.FILE_NAME=FILENAME

    case2 = main.load_tasks()

    tasks = {(task_name,info["done"],info["priority"]) for task_name, info in main.tasks_dict.items()}
    expected = {('item1', False, 1),('item2', True, 2), ('item3', False, 3)}

    assert main.UP_TO_DATE == True
    assert case2
    assert tasks == expected
    
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

    print("test_save_tasks_and_load_tasks passed!")

test_save_tasks_and_load_tasks()
print("done testing save_tasks() and load_tasks()")
print()
