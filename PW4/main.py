from domains import student, course, mark
from input import get_int_input, get_string_input
from cursesoutput import initialize_curses, terminate_curses, print_message, get_user_input

class School:
  def __init__(self):
    self.students = []
    self.courses = []

  def input_students(self):
    stdscr = initialize_curses()
    print_message(stdscr, "1: Input student information")
    id = get_int_input(stdscr, "Enter student id: ")
    name = get_string_input(stdscr, "Enter student name: ")
    dob = get_string_input(stdscr, "Enter student date of birth: ")
    self.students.append(student.Student(id, name, dob))
    terminate_curses(stdscr)

  def input_courses(self):
    stdscr = initialize_curses()
    print_message(stdscr, "2: Input course information")
    id = get_int_input(stdscr, "Enter course id: ")
    name = get_string_input(stdscr, "Enter course name: ")
    credit = get_int_input(stdscr, "Enter course credit: ")
    self.courses.append(course.Course(id, name, credit))
    terminate_curses(stdscr)

  # ... other functions using curses_output methods (similar logic)

if __name__ == "__main__":
  school = School()
  while True:
    stdscr = initialize_curses()
    print_message(stdscr, "Select an option:")
    # ... rest of the menu options using curses output functions
    terminate_curses(stdscr)
