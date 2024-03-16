def write_students_to_file(students, filename="students.txt"):
  with open(filename, "w") as file:
    for student in students:
      file.write(f"{student.id},{student.name},{student.dob}\n")
def write_courses_to_file(courses, filename="courses.txt"):
  with open(filename, "w") as file:
    for course in courses:
      file.write(f"{course.id},{course.name},{course.credit}\n")
def write_marks_to_file(marks, filename="marks.txt"):
  if isinstance(marks, dict):
    with open(filename, "w") as file:
      for student_id, student_marks in marks.items():
        for mark in student_marks:
          file.write(f"{student_id},{mark.course.id},{mark.mark}\n")
  else:
    with open(filename, "w") as file:
      for mark in marks:
        file.write(f"{mark.student_id},{mark.course.id},{mark.mark}\n")
import pickle
def compress_data(data, filename="students.dat"):
  with open(filename, "wb") as file:
    pickle.dump(data, file)
def decompress_data(filename="students.dat"):
  with open(filename, "rb") as file:
    return pickle.load(file)
import os
def load_data(filename="students.dat"):
  try:
    with open(filename, "rb") as file:
      return pickle.load(file)
  except FileNotFoundError:
    return None
