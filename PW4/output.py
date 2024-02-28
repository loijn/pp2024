def list_courses(school):
    print("4: Display courses")
    if school.courses:
        for course in school.courses:
            print(f"Course id: {course.id}, Course name: {course.name}")
    else:
        print("No courses in database.")

def list_students(school):
    print("5: Display students")
    if school.students:
        for student in school.students:
            print(f"Student id: {student.id}, Student name: {student.name}, Date of birth: {student.dob}")
            for mark in school.marks:
                if mark.student.id == student.id:
                    print(f"Grade in course {mark.course.name}: {mark.mark}")
    else:
        print("No students in database.")
