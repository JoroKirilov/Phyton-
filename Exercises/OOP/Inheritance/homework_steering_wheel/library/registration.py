from Inheritance.homework_steering_wheel.library.library import Library
from Inheritance.homework_steering_wheel.library.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_record:
            library.user_record.append(user)
        else:
            print(f"User with id = {user.user_id} already registered in the library!")

    def remove_user(self, user: User, library: Library):
        if user in library.user_record:
            library.user_record.remove(user)
        else:
            print("We could not find such user to remove!")

    def change_username(self, user_id: int, new_username: str, library: Library ):
        for user in library.user_record:
            if user_id == user.user_id:
                user.username = new_username
                break
        else:
            print(f"There is no user with id = {user_id}")



