weight = int(input("weight: "))
height = int(input("height: "))
BMI = weight / height ** 2
print("BMI:", BMI)
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 24.9:
    print("Normal weight")
elif 25 <= BMI < 29.9:
    print("Overweight")
else:
    print("Obesity")