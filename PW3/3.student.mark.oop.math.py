import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = []
class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
class Mark:
    def __init__(self, course, mark):
        self.course = course
        self.mark = mark
class School:
    def __init__(self):
        self.students = []
        self.courses = []
    def input_students(self):
        print("1: Input student information")
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        self.students.append(Student(id, name, dob))
    def input_courses(self):
        print("2: Input course information")
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        self.courses.append(Course(id, name, credit))
    def input_marks(self):
        print("3: Input grades")
        course_id = input("Enter course id: ")
        course = next((course for course in self.courses if course.id == course_id), None)
        if course:
            print(f"Course name: {course.name}")
            student_id = input("Select student by id: ")
            student = next((student for student in self.students if student.id == student_id), None)
            if student:
                while True:
                    mark = float(input("Enter grade out of 20: "))
                    if mark < 0 or mark > 20:
                        print("Invalid grade. Grade should be between 0 and 20.")
                    else:
                        student.marks.append(Mark(course, math.floor(mark)))
                        break
            else:
                print("Student not found.")
        else:
            print("Course not found.")
    def list_courses(self):
        print("4: Display courses")
        if self.courses:
            for course in self.courses:
                print(f"Course id: {course.id}, Course name: {course.name}")
        else:
            print("No courses in database.")
    def list_students(self):
        print("5: Display students")
        if self.students:
            for student in self.students:
                print(f"Student id: {student.id}, Student name: {student.name}, Date of birth: {student.dob}")
                for mark in student.marks:
                    print(f"Grade in course {mark.course.name}: {mark.mark}")
        else:
            print("No students in database.")
    def calculate_gpa(self, student):
        if not student.marks:
            return None
        total_mark = np.sum([mark.mark * mark.course.credit for mark in student.marks])
        total_credit = np.sum([mark.course.credit for mark in student.marks])
        return total_mark / total_credit
    def sort_by_gpa(self):
        self.students.sort(key=self.calculate_gpa, reverse=True)
# Main func
if __name__ == "__main__":
    school = School()
    while True:
        print("Select an option:")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input grades for a course")
        print("4. Display courses")
        print("5. Display students")
        print("6. Calculate GPA for a student")
        print("7. Sort students by GPA")
        print("8. Exit")
        option = input("Your option: ")
        if option == '1':
            school.input_students()
        elif option == '2':
            school.input_courses()
        elif option == '3':
            school.input_marks()
        elif option == '4':
            school.list_courses()
        elif option == '5':
            school.list_students()
        elif option == '6':
            student_id = input("Enter student id: ")
            student = next((student for student in school.students if student.id == student_id), None)
            if student:
                gpa = school.calculate_gpa(student)
                if gpa is not None:
                    print(f"GPA for student {student.name}: {gpa}")
                else:
                    print("No grades available for this student.")
            else:
                print("Student not found.")
        elif option == '7':
            school.sort_by_gpa()
            print("Students sorted by GPA.")
        elif option == '8':
            break
        else:
            print("Invalid option. Please select a number between 1 and 8.")
