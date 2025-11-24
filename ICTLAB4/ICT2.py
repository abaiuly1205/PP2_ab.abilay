while True:
    num1 = input("Enter the first number (or 'q' to quit): ")
    if num1.lower() == 'q':
        print("Exiting calculator...")
        break
    num2 = input("Enter the second number (or 'q' to quit): ")
    if num2.lower() == 'q':
        print("Exiting calculator...")
        break
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid number input. Please try again.")
        continue
    operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ")
    if operation.lower() == 'q':
        print("Exiting calculator...")
        break
    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Error: Invalid operation. Please try again.")
