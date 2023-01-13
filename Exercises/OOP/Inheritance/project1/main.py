from Inheritance.project1.child import Child
from Inheritance.project1.person import Person

person1 = Person("Peter", 25)
child1 = Child("Peter Junior", 5)

print(person1.name)
print(person1.age)
print(child1.__class__.__bases__[0].__name__)
print(child1.name)
print(child1.__str__())