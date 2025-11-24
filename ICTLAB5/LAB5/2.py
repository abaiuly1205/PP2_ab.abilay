import random

findme = random.randint(1, 100)

while True:
    n = input("введите число или q для выхода: ")
    if n == "q":
        break

    n = int(n)
    if n > findme:
        print("too high!")
    elif n < findme:
        print("too low!")
    else:
        print("You found me:)")
        break
