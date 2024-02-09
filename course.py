class Course:
    def __init__(self, name, teacher):
        self.teacher = teacher
        self.name = name
        self.students = []
        teacher.courses_taught.append(self.name)

    def enroll_student(self, student):
        self.students.append(student)
        student.courses_enrolled.append(self.name)
