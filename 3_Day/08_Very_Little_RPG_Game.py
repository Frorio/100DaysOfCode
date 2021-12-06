print("Welcome to the Treasure island!\n Your mission is to find the treasure!")
print("You are woke up close to a dangeon. You decided to enter it\nInside the dangeon you see two doors. Pink and Red one. Between the doors you see a plate with information.\n Plate: You can shoose only one way or you will die!")


first_choisee = input("Which way you will choose?  Red door or Pink door?  R/P")
if first_choisee == "R":
    print("You passed though the red door and appiared in a soup store. The end!")
elif first_choisee == "P":
    print("You passed though the red door and appiared in equestria. The end!")
else:
    print("You escaped the dangeon. The end!")