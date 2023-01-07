class custom_range:
    def __init__(self, start, end):
        self.i = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            current = self.i
            self.i += 1
            return current
        else:
            raise StopIteration()


my_iter = custom_range(1, 10)
print(type(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
print(next(my_iter))
print()
for num in my_iter:
    print(num)