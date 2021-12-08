row1 = ["o", "o", "o"]
row2 = ["o", "o", "o"]
row3 = ["o", "o", "o"]

map = [row1, row2, row3]


print(f"{row1}\n{row2}\n{row3}")
position = input("Where you want to put the treasure?  ")

horizontal = int(position[0]) #2
vertical = int(position[1]) #3

selected_row = map[vertical - 1][horizontal - 1] = "x"


print(f"{row1}\n{row2}\n{row3}")

#        1    2    3
#    1 ["o", "o", "o"]
#    2 ["o", "o", "o"]
#    3 ["o", "o", "o"]

#           23
#     ["o", "o", "o"]
#     ["o", "o", "o"]
#     ["o", "x", "o"]