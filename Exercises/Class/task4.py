class People:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.party_people = []


party_1 = Party()
while True:
    name_of_guests = input()
    if name_of_guests == "End":
        break
    party_1.party_people.append(name_of_guests)
print("Going: ", end='')
print(*party_1.party_people, sep=", ")
print(f"Total: {len(party_1.party_people)}")

"Going: {people}"
"Total: {total_people_going}"
