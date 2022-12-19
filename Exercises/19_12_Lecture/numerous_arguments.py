def users_list(main_user, *users, main_user_age=None, **user_options):
    print(main_user, main_user_age)
    for user in users:
        print(user, user_options(user))


my_dict = {'a': 1, 'b': 2, 'c': 3}
users_list("Ivan", *["Petar", "Valia", "Kosio"], **"ivan")
