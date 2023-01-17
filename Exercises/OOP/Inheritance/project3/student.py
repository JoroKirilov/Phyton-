from person import Person


class Student(Person):
    def __init__(self, semester, faculty_number, *args, **kwargs):
        super().__init__(*args)
        self.semester = semester
        self.faculty_number = faculty_number
        self.scholarship = kwargs.pop("scholarship", 0)

    def study(self, discipline):
        print(f"{self.name} is studying {discipline}")


student = Student(8, 9988855, "Pesho", 32, "Male", 185, scholarship=1000)
student.study("Math")
print(student.semester, student.faculty_number, student.scholarship)