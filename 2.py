# 2. Student Grades Manager
# ● Use: Dictionary (student: grades list), functions (add grades, calculate average), loops
# ○ Add student grades
# ○ Calculate average grade per student
# ○ Show all students with averages

students = {}


def add_grades(name, n):
    grades = []
    for i in range(n):
        grade = float(input(f"Enter Grade {i+1}: "))
        grades.append(grade)

    if name in students:
        students[name].extend(grades)
    else:
        students[name] = grades


def calculate_average(name):
    if name in students:
        average = sum(students[name]) / len(students[name])
        print(f"Average: {average:.2f}")
    else:
        print("Not found")


def show_all_students():
    if not students:
        print("No students found.")
    else:
        print("\n---- All Students ----")
        for name, grades in students.items():
            avg = sum(grades) / len(grades)
            print(f"{name}: {avg:.2f}")


while True:
    print("\n1.Add grades")
    print("2. calculate Average")
    print("3. Show all students with averages")

    print("4. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            name_of_student = input("Enter student name: ")
            student_grades = int(input("Enter number of grades: "))
            add_grades(name_of_student, student_grades)

        case "2":
            name_of_student = input("Enter student name to calculate average: ")
            calculate_average(name_of_student)

        case "3":
            show_all_students()

        case "4":
            print("Exiting...")
            break
        case _:
            print("Invalid choice, try again.")
