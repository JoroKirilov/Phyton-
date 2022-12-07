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


# starting_point = 20
# while starting_point < 30:
#     print("I'm in while loop with break")
#     if starting_point >= 25:
#         print("We hit the break")
#         break;
#     starting_point += 1
# else:
#     print("WHILE LOOP ENDED SUCCESSFULLY")

# while True:
#     # define some retry logic
#     break

# for c in [-4, 0, 3, 19]:
#     print('\ninitial c =', c)
#
#     count = 0
#
#     while 5 > c >= 0:
#         print('c =', c)
#
#         c += 1
#         count += 1
#     else:
#         if c == count == 5:
#             print('normal termination. c=', c)

a = 0

# while a < 10:
#     b = 0
#     while b < 10:
#         c = 0
#         while c < 10:
#             print('{}{}{}'.format(a, b, c))
#             pass
#             c += 1
#         b += 1
#     a += 1
# else:
#     print('normal termination')