from person import Person

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year

if __name__ == '__main__':
    student1 = Student('John', 18, 'Freshman')
    person1 = Person('Joe', '19')
