# 1. Write a decorator that would be used on a function that return a number. If today is wednesday,
# friday, or sunday, the function should return the number decreased byt 1.5.
import functools

days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}


def decreased_number(number_of_days, days_dict=None):
    if days_dict is None:
        days_dict = days_of_week

    def decorator(func_ref):
        def wrapper(num):
            result = func_ref(num)
            bonus_price = result - 1.5
            days_decreased = ["Wednesday", "Friday", "Sunday"]
            if days_dict[number_of_days] in days_decreased:
                return f"Beer bonus price on {days_dict[number_of_days]} - only {bonus_price}"
            else:
                return f"Regularly beer price - {result}"

        return wrapper

    return decorator


beer_price = 11


@decreased_number(7)       # DAYS WHEN YOUR ARE GOOD TO BUY MORE BEER ( 2 , 5 , 7 )
def set_price(price):
    return price


print(set_price(beer_price))
