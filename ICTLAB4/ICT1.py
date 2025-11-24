x = float(input("Enter x: "))
y = float(input("Enter y: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    print("Result:", x + y)
elif op == '-':
    print("Result:", x - y)
elif op == '*':
    print("Result:", x * y)
elif op == '/':
    if y == 0:
        print("Error")
    else:
        print("Result:", x / y)
else:
    print("Invalid operation!")