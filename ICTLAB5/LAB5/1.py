temp = float(input("температура: "))
t = input("C (цельсий → фаренгейт) или F (фаренгейт → цельсий): ")

if t.upper() == "C":
    print(temp * 9/5 + 32)
elif t.upper() == "F":
    print((temp - 32) * 5/9)
else:
    print("ошибка: выберите C или F")
