# input the number of students in a class
def get_number_of_students():
    n = int(input("Enter the number of students: "))
    return n

# input the information of a student
def get_student_info():
    id = input("Enter the student ID: ")
    name = input("Enter the student name: ")
    dob = input("Enter the student date of birth (dd/mm/yyyy): ")
    return id, name, dob

# input the number of courses
def get_number_of_courses():
    n = int(input("Enter the number of courses: "))
    return n

# input the information of a course: id, name
def get_course_info():
    id = input("Enter the course ID: ")
    name = input("Enter the course name: ")
    return id, name

# choose a course, input the marks for the students in that course
def get_marks(students, courses):
    course_id = input("Enter the course ID to input marks: ")
    if course_id in courses:
        for student in students:
            mark = float(input(f"Enter the mark for student {student['name']}: "))
            student['marks'][course_id] = mark
    else:
        print("Invalid course ID")

# listing functions

# display the courses
def display_courses(courses):
    print("The courses are:")
    for id, name in courses.items():
        print(f"ID: {id}, Name: {name}")

# display the students
def display_students(students):
    print("The students are:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

# display the marks of the students for a given course
def display_marks(students, courses):
    course_id = input("Enter the course ID to display marks: ")
    if course_id in courses:
        print(f"The marks for course {courses[course_id]} are:")
        for student in students:
            if course_id in student['marks']:
                print(f"{student['name']}: {student['marks'][course_id]}")
            else:
                print(f"{student['name']}: No mark")
    else:
        print("Invalid course ID")

# create empty LISTS for students and courses
students = []
courses = {}

# get the number of students and courses
num_students = get_number_of_students()
num_courses = get_number_of_courses()

# get the information of the students and courses
for i in range(num_students):
    id, name, dob = get_student_info()
    students.append({'id': id, 'name': name, 'dob': dob, 'marks': {}})

for i in range(num_courses):
    id, name = get_course_info()
    courses[id] = name

# get the marks for a course
get_marks(students, courses)

# display the courses and students
display_courses(courses)
display_students(students)

# display the marks for a course
display_marks(students, courses)
