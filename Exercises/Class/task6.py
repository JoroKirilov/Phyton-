# Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals
# in the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists
# (mammals, fishes, birds). The class should also have 2 more methods:
# •	add_animal(species, name) - based on the species, adds the name to the corresponding list
# •	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}
# Total animals: {total_animals}"
# On the first line, you will receive the name of the zoo. On the second line, you will receive number n.
# On the following n lines you will receive animal info in the format: "{species} {name}".
# Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
# On the final line, you will receive a species.
# At the end, print the info for that species and the total count of animals in the zoo.

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def get_number_of_animal(self):
        return len(self.birds) + len(self.fishes) + len(self.mammals)

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        else:
            self.birds.append(name)

    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species == "fish":
            print(f"Fishs in {self.name}: {', '.join(self.fishes)}")
        else:
            print(f"Birds in {self.name}: {', '.join(self.birds)}")


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
n = int(input())
for _ in range(n):
    species1, name1 = input().split()
    zoo.add_animal(species1, name1)

species_search = input()
zoo.get_info(species_search)
print(f"Total animals: {zoo.get_number_of_animal()}")
