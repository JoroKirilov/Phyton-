# The Trainer class should receive a name (string). The Trainer should also have an attribute pokemons
# (list, empty by default). The Trainer has three methods:
# -	add_pokemon(pokemon: Pokemon)
# o	Add the pokemon to the collection and return "Caught {pokemon_name} with health {pokemon_health}".
# Note: use the pokemon's details method.
# o	If the pokemon is already in the collection, it should return "This pokemon is already caught"
# o	Hint: to import the Pokemon class you should add "from project.pokemon import Pokemon"
from pokemon import *


# -	release_pokemon(pokemon_name: String)
# o	Check if you have a pokemon with that name and remove it from the collection. It should return "You have released {pokemon_name}"
# o	If there is no pokemon with that name in the collection, return "Pokemon is not caught"
# -	trainer_data()
# o	The method returns the information about the trainer and his pokemon collection in this format:
# "Pokemon Trainer {trainer_name}
#  Pokemon count {the amount of pokemon caught}
#  - {pokemon_details}
#  ...
#  - {pokemon_details}"

class Trainer():
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return pokemon.pokemon_details()

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for el in self.pokemons:
            result += str(el)
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
