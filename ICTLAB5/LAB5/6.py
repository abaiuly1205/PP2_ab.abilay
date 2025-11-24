while True:
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Exit")

    c = input("Выбор: ")

    if c == "4":
        break

    a = float(input("Первое число: "))
    b = float(input("Второе число: "))

    if c == "1":
        print(a + b)
    elif c == "2":
        print(a - b)
    elif c == "3":
        print(a * b)
    else:
        print("Неверный выбор")