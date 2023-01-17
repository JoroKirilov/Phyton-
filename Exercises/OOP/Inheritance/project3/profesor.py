from student import Student


class Profesor(Student):
    Title = "Profesor"

    def __init__(self, faculty: str, years_of_exp: int, semester, faculty_number, *args, **kwargs):
        super().__init__(semester, faculty_number, *args, **kwargs)
        self.faculty = faculty
        self.years_of_exp = years_of_exp
        self.discipline = []

    def add_discipline(self, disc):
        self.discipline.append(disc)


profesor1 = Profesor(("Math", 20, 8, 23345654, ))
profesor1.add_discipline("Algebra")
profesor1.add_discipline("Geometry")
