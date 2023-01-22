import itertools

# counter = itertools.count(start=5, step=5)

# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400]
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

mode = itertools.cycle(["ON", "OFF"])
print(next(mode))
print(next(mode))
print(next(mode))
