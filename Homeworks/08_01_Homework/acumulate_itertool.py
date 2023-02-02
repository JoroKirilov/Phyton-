import itertools

def list_iter(num):
    tmp_list = []
    for i in range(num):
        tmp_list.append(i)
    return tmp_list

result = list(itertools.accumulate(list_iter(10)))
print(result)
print("That is it")