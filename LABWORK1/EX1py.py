students = []
courses = []

def add_student():

    id = input("Student ID: ")
    name = input("Name: ")
    dob = input(" (dd/mm/yyyy): ")
    students.append({"id": id, "name": name, "dob": dob, "marks": {}})

def add_course():

    id = input("Course ID: ")
    name = input("Name: ")
    courses.append({"id": id, "name": name})

def enter_marks():

    student_id = input("Student ID: ")
    course_id = input("Course ID: ")
    mark = input("Mark: ")

    for student in students:
     if student["id"] == student_id:
            student["marks"][course_id] = mark
            break

def list_students():

    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}, Marks: {student['marks']}")
def list_courses():

    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

while True:
    print("1. Add student")
    print("2. Add course")
    print("3. Enter marks")
    print("4. List students")
    print("5. List courses")
    print("6. Quit")
    choice = input("Pick one: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        add_course()
    elif choice == '3':
        enter_marks()
    elif choice == '4':
        list_students()
    elif choice == '5':
        list_courses()
    elif choice == '6':
        break
    else:
        print("Wrong choice. Pick between 1 and 6.")