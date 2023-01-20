# Table (seats, material, color) Make a Table class, representing a physical table.
# It is up to you to choose attributes. The table should allow People to sit on free chairs,
# where free chairs must be no more than Table's places.
# We should be able to allow People to sit on a free chair and
# to leave a chair. We should be able to tell what is the free capacity of the Table.

class Table:
    def __init__(self, material: str, color: str):
        self.material = material
        self.color = color
        self.capacity = 4
        self.free_seats = self.capacity

    def get_free_seat(self):
        return self.free_seats

    def sit_on_table(self):
        if self.get_free_seat():
            self.free_seats -= 1
            return "Someone is sitting on the table"
        return "No free chairs"

    def get_up_of_table(self):
        if self.free_seats < self.capacity:
            self.free_seats += 1
            return "Someone is getting up from the table"
        return "Nobody on the table"

table1 = Table("WOOD", "BLACK")
print(table1.free_seats)
print(table1.sit_on_table())
print(table1.sit_on_table())
print(table1.get_up_of_table())