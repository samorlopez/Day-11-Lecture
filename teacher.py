from person import Person


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses_taught = []
