l = list(map(int, input().split()))

k = sum(l[1:]) + 1
res = l[0] * k
print(res)