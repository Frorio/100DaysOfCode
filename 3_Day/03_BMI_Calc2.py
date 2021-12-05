height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2
print(f"Your BMI: {bmi}")

if bmi < 18.5:
    print("You have underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You have overweight")
elif bmi < 35:
    print("You have obese")
else:
    print("Bruh... Your so fatty")