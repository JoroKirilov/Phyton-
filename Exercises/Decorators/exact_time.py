import time


def exec_time(func):
    def wrapper(*args):
        # start watch
        start = time.time()
        func(*args)
        end = time.time()
        # end watch
        return end - start
        # return seconds
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))