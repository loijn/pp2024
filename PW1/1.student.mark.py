students = []
courses = []
marks = {}

# student in4
def input_students():
    print("1: Input student information")
    id = input("Enter student id: ")
    name = input("Enter name: ")
    dob = input("date of birth: ")
    students.append((id, name, dob))
# course in4
def input_courses():
    print("2: Input course information")
    id = input("Enter course id: ")
    name = input("course name: ")
    courses.append((id, name))
# marks
def input_marks():
    print("3: Input grades")
    course_id = input("Enter course id: ")
    course_name = next((name for id, name in courses if id == course_id), None)
    if course_name:
        print(f"Course name: {course_name}")
        student_id = input("Select student by id: ")
        while True:
            mark = float(input("Enter grade out of 20: "))
# grade and corse check
            if mark < 0 or mark > 20:
                print("grade entering failed. Grade should be between 0 and 20.")
            else:
                marks[(student_id, course_id)] = mark
                break
    else:
        print("Course not found.")

# display courses
def list_courses():
    print("4: Display courses")
    if courses:
        for id, name in courses:
            print(f"Course id: {id}, Course name: {name}")
    else:
        print("No courses in database.")
# display students
def list_students():
    print("5: Display students")
    if students:
        for id, name, dob in students:
            print(f"Student id: {id}, Student name: {name}, Date of birth: {dob}")
            for course_id, course_name in courses:
                print(f"Grade in course {course_name}: {marks.get((id, course_id), 'N/A')}")
    else:
        print("No students in database.")

# Main func
if __name__ == "__main__":
 while True:
    print("Select an option:")
    print("1. Input student information")
    print("2. Input course information")
    print("3. Input grades for a course")
    print("4. Display courses")
    print("5. Display students")
    print("6. Exit")
    option = input("Your option: ")
    if option == '1':
        input_students()
    elif option == '2':
            input_courses()
    elif option == '3':
            input_marks()
    elif option == '4':
            list_courses()
    elif option == '5':
            list_students()
    elif option == '6':
        break
    else:
        print("Please select a number between 1 and 6.")
