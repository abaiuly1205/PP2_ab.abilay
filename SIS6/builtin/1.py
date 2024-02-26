def f(list):
    res = 1
    for i in range(len(list)):
        res *= list[i]
    return res

l = list(map(int, input().split()))
result = f(l)
print(result)