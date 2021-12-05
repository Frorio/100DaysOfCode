height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
your_bmi = int(bmi)
print("Your BMI: " + str(your_bmi))