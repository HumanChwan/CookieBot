def Checklog(a, b):
    cnt_dig = cnt_plc = 0
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                cnt_dig += 1
                if i == j:
                    cnt_plc += 1
    return [cnt_dig, cnt_plc]

def RepeatFound(InputStr):
    boolDig = [False] * 10
    for i in InputStr:
        if boolDig[int(i)-int('0')]:
            return True
        else:
            boolDig[int(i)-int('0')] = True
    return False