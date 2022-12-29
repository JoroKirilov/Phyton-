def make_seq(num):
    list_seq = [0, 1]
    result = 0
    for _ in range(num - 2):
        result = list_seq[-1] + list_seq[-2]
        list_seq.append(result)
    return list_seq


def locate_num(search_num, fibunachi_seq_number):
    tmp_list = make_seq(fibunachi_seq_number)
    for idx in range(len(tmp_list)):
        if search_num == tmp_list[idx]:
            return idx
    else:
        return print("not in the sequence")


print(locate_num(13 , 10))