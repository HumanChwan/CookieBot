def check_log(a, b):
    cnt_dig = cnt_plc = 0
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                cnt_dig += 1
                if i == j:
                    cnt_plc += 1
    return [cnt_dig, cnt_plc]


def repeat_found(input_string):
    bool_digit = [False] * 10
    for i in input_string:
        if bool_digit[int(i)]:
            return True
        else:
            bool_digit[int(i)] = True
    return False
