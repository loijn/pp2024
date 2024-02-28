# input.py

from PW4.domains.course import Course
from PW4.domains.mark import Mark
from PW4.domains.student import Student
from PW4.domains.school import School

def input_students(school):
    print("1: Input student information")
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    school.students.append(Student(id, name, dob))

def input_courses(school):
    print("2: Input course information")
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    school.courses.append(Course(id, name))

def input_marks(school):
    print("3: Input grades")
    course_id = input("Enter course id: ")
    course = next((course for course in school.courses if course.id == course_id), None)
    if course:
        print(f"Course name: {course.name}")
        student_id = input("Select student by id: ")
        student = next((student for student in school.students if student.id == student_id), None)
        if student:
            while True:
                mark = float(input("Enter grade out of 20: "))
                if mark < 0 or mark > 20:
                    print("Invalid grade. Grade should be between 0 and 20.")
                else:
                    school.marks.append(Mark(student, course, mark))
                    break
        else:
            print("Student not found.")
    else:
        print("Course not found.")
