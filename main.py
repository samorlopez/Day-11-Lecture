from person import Person
from student import Student
from teacher import Teacher
from course import Course

if __name__ == '__main__':
    student2 = Student("Lei Ann")
    student1 = Student("Sam")
    teacher1 = Teacher("Prof")
    print(student2.name)
    print(student1.name)
    print(teacher1.name)
    hcde_class = Course("HCDE 310", teacher1)
    print(hcde_class.teacher.name)
    print(teacher1.courses_taught)
    hcde_class.enroll_student(student1)
    hcde_class.enroll_student(student2)
    for student in hcde_class.students:
        print(student.name)
    print(student1.courses_enrolled)