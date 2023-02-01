from ZOO.animals import Animal
from ZOO.workers import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animal = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return "Not enough money"
        if self.__animal_capacity is len(self.animal):
            return "Not free cage for this animal"
        self.__budget -= price
        self.animal.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) is self.__workers_capacity:
            return "No need of workers"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} is a new employee"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name is worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no worker with this name"

    def pay_workers(self):
        month_expenses = 0
        for workers in self.workers:
            month_expenses += workers.salary
        if month_expenses > self.__budget:
            return "Not enough money for salaries"
        self.__budget -= month_expenses
        return "Every worker get his salary"






