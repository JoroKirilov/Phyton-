class Party:
    def __init__(self):
        self.people = []
        self.drinks = []

    def drinking_list(self, drink):
        self.drinks.append(drink)

    def invite(self, guest):
        self.people.append(guest)

    def name_of_attendees(self):
        return ', '.join([people.name for people in self.people])

    def number_of_guest(self):
        return len(self.people)


class Person:
    def __init__(self, names, drinking, meat):
        self.name = names
        self.favorite_drinking = drinking
        self.favorite_meat = meat


party = Party()
guest1 = Person("Georgi", "Beer", "BBQ")
guest2 = Person("Ivan", "Vodka", "Spagetti")
guest3 = Person("Rumi", "Juice", "Pizza")
guest4 = Person("Angel", "Beer", None)
guests = [guest1, guest2, guest3, guest4]
for element in guests:
    party.invite(element)
    party.drinking_list(element.favorite_drinking)

print(party.name_of_attendees())
print(party.drinks)

