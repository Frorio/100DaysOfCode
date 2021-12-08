#  split_inp = "Hello, from, AskPython"
#  op = str_inp.split(",")
#  print(op)

# op = [Hello, from, AskPython]

import random

names_string = input("Give me everybody's names, sperated by a comma: ")
names = names_string.split(", ")


num_items = len(names)
random_choise = random.randint(0, num_items - 1) #You need to -1 because you count from 0
person_who_will_pay = names[random_choise]
print(person_who_will_pay)

# You can use the choice()