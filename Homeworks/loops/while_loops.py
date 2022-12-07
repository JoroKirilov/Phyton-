# while<condition>
#     do something
#     <do something to update condition>
#     break

# counter = 0
# while counter < 5:
#     print(f"Counter value is: {counter}")
#     counter += 1
# else:
#     print("GAME OVER")


# we must be aware when using continue in while loop

# starting_point = 20
# while starting_point < 30:
#     print("I'm in while loop")
#     if starting_point >= 25:
#         continue   # endless loop like this
#     starting_point += 1

# number = 5
# while number <= 5:
#     print(f"{number} ** 2 // 3 % 5 = ", number ** 2 // 3 % 5)
#     number += 1
# else:
#     print("While loop ended successfully")


starting_point = 20
while starting_point < 30:
    print("I'm in while loop with break")
    if starting_point >= 25:
        print("We hit the break")
        break;
    starting_point += 1
else:
    print("WHILE LOOP ENDED SUCCESSFULLY")