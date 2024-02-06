def long(list):
    max = list[0]
    for x in list:
        if len(x) > len(max):
            max = x
        else:
            continue
    return max
list = input().split()
print(long(list))