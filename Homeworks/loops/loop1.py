# football_teams = ["Barcelona", "Real Madrid", "Chelsea", "Arsenal"]
#
# for teams in football_teams:
#     print(f"{teams}")


# students_data = [
#     ("Pesho", 32, ["Python", "Web", "Caching"]),
#     ("Georgi", 33, ["Python", "Web", "Caching"]),
#     ("Ivan", 35, ["Python", "Web", "Caching"]),
#     ("Dinko", 31, ["Html", "CSS", "Caching"]),
# ]

# for name, age, courses in students_data:
#     print(name)
#     for course in courses:
#         print(f"{course}, ", end="")
#     print()

# dict_comprehentions = {x: str(x) for x in range(5) if x % 3 != 0}
# for x in dict_comprehentions:
#     print(x)
#
# for key in dict_comprehentions.keys():
#     print(key)

# for value in dict_comprehentions.values():
#     print(value)

# for key, value in dict_comprehentions.items():
#     print(key, value)


# age = {1, 1, 2, 32, 43, 54, 24}
#
# print()
# for age in age:
#     print(age)


#for loop with normal ending

# for blue in (1, 2, 3, 4, 5, 6, 7):
#     print(blue % 2)

# else:
#     print("The for loop was a success!")


# for char in "CodeT AcademyBG":
#     pass
#     if char == 'B':
#         break
#     elif char == 'T':
#         continue
#     print(char, ord(char))
# else:
#     print("GAME OVER")

# names = ['John', 'Bill', "Ivan"]
#
# ages = [32, 42, 35, 36]
#
# weights = [98, 78, 87]
#
# heights = [[5, 8], [4, 1], [6, 1]]
#
# for name, age, weight, height in zip(names, ages, weights, heights):
#     feet, inches = height
#
#     print(f"{name}: age = {age} years: weigh = {weight}, height = {height}")


a = [0, 1, -2, 3, -4, -5, -6, -7, 8, -9, 10, 11, -12]
for number in a.copy():
    if number < 0:
        a.remove(number)
    print(a)



