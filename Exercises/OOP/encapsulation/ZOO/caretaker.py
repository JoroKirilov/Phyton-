from ZOO.workers import Worker


class CareTaker(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)