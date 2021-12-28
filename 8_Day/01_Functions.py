#Simple function

def greet():
    print("1")
    print("2")
    print("3")
greet() #1 2 3

#Function that allows for input 

def greet_with_name(name):#   <-------x
    print(f"Hello {name}")#           |
    print(f"How do you do {name}?")#  | Angela
#                                     |
greet_with_name("Angela")   #---------x

Something = 123
#   |        |
#   ↓        ↓
#Parameter  Argument