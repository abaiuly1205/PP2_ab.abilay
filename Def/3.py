import math
a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4*a*c

root = lambda sign:(-b + sign * math.sqrt(d))/(2*a)

if d >= 0:
    x1 = root(1)
    x2 = root(-1)
    print(x1)
    print(x2)
else:
    print("The quadratic equation has no roots.")