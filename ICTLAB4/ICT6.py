a = []
sumodd = 0
sumeven = 0
for i in range(1, 101):
    a.append(i)
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        sumeven = sumeven + a[i]
    elif a[i] % 2 == 1:
        sumodd = sumodd + a[i]
print(sumeven)
print(sumodd)