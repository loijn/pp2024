from Student import Student
from Course import Course
from Mark import Mark
def get_user_input(message):
  user_input = input(message)
  return user_input
def get_student_info():
  student_id = int(get_user_input("Enter student ID: "))
  student_name = get_user_input("Enter student name: ")
  student_dob = get_user_input("Enter student date of birth (YYYY-MM-DD): ")
  return Student(student_id, student_name, student_dob)
def get_course_info():
  course_id = int(get_user_input("Enter course ID: "))
  course_name = get_user_input("Enter course name: ")
  course_credit = float(get_user_input("Enter course credit: "))
  return Course(course_id, course_name, course_credit)
def get_mark_info(courses):
  student_marks = {}
  for course in courses:
    mark = float(get_user_input(f"Enter mark for {course.name} ({course.id}): "))
    student_marks[course.id] = mark
  return student_marks


def main():
  # Load data from compressed file (if applicable)
  data = load_data()
  if data:
    students = data["students"]
    courses = data["courses"]
    marks = data["marks"]
  else:
    students = []
    courses = []
    marks = {}  # Or a list of Mark objects (decide based on your approach)

  # Program logic for user interaction (menus, functionalities)
  while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Add Marks")
    print("4. View Students")
    print("5. View Courses")
    print("6. View Marks")
    print("7. Exit")

    choice = get_user_input("Enter your choice: ")

    if choice == '1':
      student = get_student_info()
      students.append(student)
      print("Student added successfully!")
    elif choice == '2':
      course = get_course_info()
      courses.append(course)
      print("Course added successfully!")
    elif choice == '3':
      if not students or not courses:
        print("Please add students and courses before adding marks.")
      else:
        student_id = int(get_user_input("Enter student ID for adding marks: "))
        student_found = False
        for student in students:
          if student.id == student_id:
            student_found = True
            student_marks = get_mark_info(courses)
            marks[student_id] = student_marks
            print("Marks added successfully!")
            break
        if not student_found:
          print("Student with ID", student_id, "not found.")
    elif choice == '4':
      if not students:
        print("No students added yet.")
      else:
        print("\nStudents:")
        for student in students:
          print(f"ID: {student.id}, Name: {student.name}")
    elif choice == '5':
      if not courses:
        print("No courses added yet.")
      else:
        print("\nCourses:")
        for course in courses:
          print(f"ID: {course.id}, Name: {course.name}, Credit: {course.credit}")
    elif choice == '6':
      if not marks:
        print("No marks added yet.")
      else:
        print("\nMarks:")
        for student_id, student_marks in marks.items():
          print(f"Student ID: {student_id}")
          for course_id, mark in student_marks.items():
            for course in courses:
              if course.id == course_id:
                print(f"  - {course.name}: {mark}")
