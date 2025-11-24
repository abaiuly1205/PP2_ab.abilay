a = int(input("enter a number: "))
if a > 0:
    print("positive")
else:
    print("non-positive")
b = 1

for i in range(1, 11):
    c = i * a
    print(b, "*", a, "=", c)
    b += 1