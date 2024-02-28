# main.py

from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from domains.school import School
import input
import output

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
            input.input_students(school)
        elif option == '2':
            input.input_courses(school)
        elif option == '3':
            input.input_marks(school)
        elif option == '4':
            output.list_courses(school)
        elif option == '5':
            output.list_students(school)
        elif option == '6':
            break
        else:
            print("Invalid option. Please select a number between 1 and 6.")
