from domains.mark import Mark

class Student:
  def __init__(self, id, name, dob):
    self.id = id
    self.name = name
    self.dob = dob
    self.marks = []

  def add_mark(self, course, mark):
    self.marks.append(Mark(course, mark))
