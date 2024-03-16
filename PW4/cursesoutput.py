import curses

def initialize_curses():
  stdscr = curses.initscr()
  curses.cbreak()
  curses.noecho()
  stdscr.keypad(True)
  stdscr.idcok(False)
  stdscr.idlok(False)  
  return stdscr

def terminate_curses(stdscr):
  curses.nocbreak()
  curses.echo()
  curses.endwin()

def print_courses(stdscr, courses):
  if not courses:
    stdscr.addstr(1, 1, "No courses in database.")
    return
  y, x = 1, 1
  stdscr.erase()  # Clear the screen before displaying courses
  for course in courses:
    stdscr.addstr(y, x, f"Course id: {course.id}, Course name: {course.name}")
    y += 1
  stdscr.refresh()  # Refresh the screen after updates

def print_students(stdscr, students):
  if not students:
    stdscr.addstr(1, 1, "No students in database.")
    return
  y, x = 1, 1
  stdscr.erase()  # Clear the screen before displaying students
  for student in students:
    stdscr.addstr(y, x, f"Student id: {student.id}, Student name: {student.name}, Date of birth: {student.dob}")
    y += 1
    for mark in student.mark:
      stdscr.addstr(y, x, f"Grade in course {mark.course.name}: {mark.mark}")
      y += 1
  stdscr.refresh()  # Refresh the screen after updates

def print_message(stdscr, message, y=1, x=1):
  stdscr.addstr(y, x, message)

def get_user_input(stdscr, message, y=1, x=1):
  stdscr.addstr(y, x, message)
  stdscr.move(y, x + len(message))  # Move cursor to the end of the message
  curses.echo()
  user_input = stdscr.getstr()
  curses.noecho()
  return user_input
