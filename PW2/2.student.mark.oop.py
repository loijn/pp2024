#classes
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark
class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
#input
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
        self.courses.append(Course(id, name))
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
                        self.marks.append(Mark(student, course, mark))
                        break
            else:
                print("Student not found.")
        else:
            print("Course not found.")
    def list_courses(self):
#show
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
                for mark in self.marks:
                    if mark.student.id == student.id:
                        print(f"Grade in course {mark.course.name}: {mark.mark}")
        else:
            print("No students in database.")
# Main
if __name__ == "__main__":
    school = School()
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
            break
        else:
            print("Invalid option. Please select a number between 1 and 6.")
