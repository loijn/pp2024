import math
import numpy as np
import curses

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
    self.stdscr = None  # Initialize for curses window
    self.students = []
    self.courses = []

  def initialize_curses(self):
    self.stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    self.stdscr.keypad(True)

  def terminate_curses(self):
    curses.nocbreak()
    curses.echo()
    curses.endwin()

  def display_message(self, message, y=1, x=1):
    self.stdscr.addstr(y, x, message)
    self.stdscr.refresh()

  def get_user_input(self, message, y=1, x=1):
    self.display_message(message, y, x)
    self.stdscr.move(y, x + len(message))
    curses.echo()
    user_input = self.stdscr.getstr()
    curses.noecho()
    return user_input

  def input_students(self):
    self.display_message("1: Input student information", 1, 1)
    while True:
      student_id = self.get_user_input("Enter student id: ", 2, 1)
      if not student_id.isdigit():
        self.display_message("Invalid ID. Please enter a number.", 4, 1)
        continue
      student_name = self.get_user_input("Enter student name: ", 5, 1)
      student_dob = self.get_user_input("Enter student date of birth: ", 6, 1)
      self.students.append(Student(int(student_id), student_name, student_dob))
      self.display_message("Student added successfully!", 8, 1)
      choice = self.get_user_input("Add another student? (y/n): ", 9, 1)
      if choice.lower() != 'y':
        break

  # Similar functions for input_courses and input_marks with curses interaction

  def list_courses(self):
    self.display_message("4: Display courses", 1, 1)
    if self.courses:
      for course in self.courses:
        self.display_message(f"Course id: {course.id}, Course name: {course.name}", 2, 1)
    else:
      self.display_message("No courses in database.", 3, 1)
    self.stdscr.getch()  # Wait for user input to continue

  # Similar functionalities for list_students, calculate_gpa, and sort_by_gpa with curses interaction

# Main function
if __name__ == "__main__":
  school = School()
  school.initialize_curses()

  while True:
    school.display_message("Select an option:", 1, 1)
    school.display_message("1. Input student information", 2, 1)
    school.display_message("2. Input course information", 3, 1)
    school.display_message("3. Input grades for a course", 4, 1)
    school.display_message("4. Display courses", 5, 1)
    school.display_message("5. Display students", 6, 1)
    school.display_message("6. Calculate GPA for a student", 7, 1)
    school.display_message("7. Sort students by GPA", 8, 1)
    school.display_message("8. Exit", 9, 1)
    option = school.get_user_input("Your option: ", 10, 1)

    # Handle menu options
