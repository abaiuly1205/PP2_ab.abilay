temp = float(input("Temerature: "))
t = input("C (C → F) or F (F → C): ")

if t.upper() == "C":
    print(temp * 9/5 + 32)
elif t.upper() == "F":
    print((temp - 32) * 5/9)
else:
    print("Error: choose C or F")