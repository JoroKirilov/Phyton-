happiness_index = [int(el) for el in input().split()]
factor = int(input())
real_happiness = [happy * factor for happy in happiness_index]
people = len(happiness_index)
average_happiness = sum(real_happiness) // people
happy_employers = [employers for employers in real_happiness if employers > average_happiness]
if len(happy_employers) >= (people // 2):
    print(f"Score: {len(happy_employers)}/{people}. Employees are happy!")
else:
    print(f"Score: {len(happy_employers)}/{people}. Employees are not happy!")
