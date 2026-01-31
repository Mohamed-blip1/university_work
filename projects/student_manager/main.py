__version__ = "1.0.1"

import os

students = {}

while True:
    
    # Menu
    print("1. Add student")
    print("2. Add grade to student")
    print("3. Display all students")
    print("4. Calculate student average")
    print("5. Save to file")
    print("6. Load from file")
    print("0. Exit")
    choice=int(input(">"))

    match choice:
        case 0:
            break
        case 1:
            name = str(input("Enter student name: "))
            if name not in students:
                students[name]=[]
                print("student successefully added.")
            else:
                print("student already exist!")
        case 2:
            name = str(input("Enter a student name: "))

            grades=students.get(name)
            if grades is not None:
                grade = float(input("Enter grade(0-20): "))
                
                if grade>=0 and grade <=20:
                    grades.append(grade)
                    print("Grade added successefully added.")
                else:
                    print("Invalid grade!")
            else:
                print("Student does not exist!")
        case 3:
            print()
            if students:
                for name, grades in students.items():
                    print(f"{name} -> {grades}")
            else:
                print("There is no student in the list!")
        case 4:
            name = str(input("Enter student name: "))
            
            if name in students:
                if students[name]:
                    average = sum(students[name]) /len(students[name])
                    print(f"Average = {average:.2f}")
                else:
                    print("The student has no grades!")
            else:
                print("Student does not exist!")
        case 5:
            if len(students)>0:
                with open("students_file.txt",'w') as file:
                    for student,grades in students.items():
                        file.write(student+':'+','.join(str(g) for g in grades)+'\n')
                print("Data saved successfully.")
            else:
                print("Nothing to save!")
        case 6:
            if os.path.exists("students_file.txt"):
                with open("students_file.txt",'r') as file:
                    students.clear()
                    for line in file:
                        line = line.strip()
                        if line:
                            name,grades_str=line.split(':')
                            if grades_str:
                                grades = [float(g) for g in grades_str.split(",")]
                            else:
                                grades=[]
                            students[name]=grades
                    if students:
                        print("Data load successfully.")
                    else:
                        print("No data to load!")
            else:
                print("File does not exist!")
        case _:
            print("Invalid choice!")
    print()
