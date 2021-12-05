print("Welcome to Frorio's Pizza Deliveries! ")
size = input("What size pizza do you want? S, M, L?  ")
add_pepperoni = input("Do you want pepperoni? Y / N   ")
extra_cheese = input("Do you want extra cheese? Y / N  ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

bill = 0

if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
elif size == "L":
    bill += large_pizza
if add_pepperoni == "Y":
    if size == "S" or "M":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
    print(f"Your pizza: ${bill}")
else:
    print(str(bill))