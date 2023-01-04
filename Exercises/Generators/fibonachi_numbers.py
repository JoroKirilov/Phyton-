def fibonaci_numbers(num):
    result = [0, 1]
    for i in range(3, num):
        result.append(result[-2] + result[-1])
    return result


print(fibonaci_numbers(10))


def generate_fibonacci(num):
    yield 0
    yield 1
    num1 = 0
    num2 = 1
    result = 0
    for i in range(2, num):
        yield result + num1
        result = num1 + num2
        num1 = num2
        num2 = num1 + num2


def generator(n):
     a, b = 0, 1
     for i in range(n + 1):         # fibonacci with generator
         yield a
         a, b = b, a + b


for i in generator(10):
    print(i, end="  ")


def my_fibunacci(limit):
    fibunachi_seq = [0,1]

    for x in range(limit):
        fibunachi_seq.append( fibunachi_seq[-1] + fibunachi_seq[-2])
        yield fibunachi_seq[-1] + fibunachi_seq[-2]
        if fibunachi_seq[-1] + fibunachi_seq[-2] >= limit:
            break


print(list(my_fibunacci(20)))