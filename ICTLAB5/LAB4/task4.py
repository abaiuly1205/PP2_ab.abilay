list = []

for i in range(1, 51):
    list.append(i)
    
print("Numbers from 1 to 50:")
for number in list:
    print(number)

for number in list:
    if number % 3 == 0 and number % 5 == 0:
        print(number , "is divisible by both 3 and 5")