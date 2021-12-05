#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places

from typing import final


bill = float(input("Enter your bill: "))
tip = bill * float(input("Enter tip you want to pay in %: "))

final_bill = bill + tip / 100
final_bill = round(final_bill, 2)
print(f"Your bill with tip will be: {final_bill}$")

splited_bill = final_bill / int(input("How many people will pay?: "))
splited_bill = round(splited_bill, 2)
print(f"Each of you will pay: {splited_bill}")