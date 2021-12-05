print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
   
    if age < 12:
        print("You have to pay $5")
        bill = 5
    
    elif age < 18:
        print("you have to pay $7")
        bill = 7
    
    else:
        print("You have to pay $12")
        bill = 12
    
    want_photo = input("Do you want a photo taken? Y or N")
    if want_photo == "Y" or "y":
        print(f"You have to pay: ${bill + 3}")

else:
    print("You can't ride the")

# if height == 120: #you can't use just "="
#     print("You can ride the rollercoaster!")
# else:
#     print("You can't ride the")