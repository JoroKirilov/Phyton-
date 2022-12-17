def set_entry_checker():
#     # Ask for user's data: First name, age and VIP status.
#     # If user's age is under 18, do not allow user to proceed
#     # If user's age is between 18 - 25, allow them to stay up to 11pm
#     # If group 18_25 has more than 10 users, do not allow user to enter.
#     # If user is aged over 25, welcome them without any additional conditions.
#     # As an output print out the users count from each group, and also print the VIPs
#     # Example input: (Georgi 28, VIP) OR (Alex 25)
#     pass

    group_info = {}
    people_in_group = 0
    vip_in_group = 0
    data = input("Give me first name , age and VIP status\n").split()
    if len(data) > 2:
        vip_in_group += 1
    name = data[0]
    age = int(data[1])
    if age > 25:
        people_in_group += 1

    group_info.setdefault(people_in_group, vip_in_group)
    return group_info



print(set_entry_checker())