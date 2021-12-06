print("Sup, mate. Welcome to the Love Calculator!")
name1 = input("What is yr name, pal?\n Name: ")
name2 = input("What is their name?\n Name: ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
love_e = lower_case_string.count("e")

first_name_count = int(t + r + u + e)
second_name_count = int(l + o + v + love_e)

love = str(first_name_count) + str(second_name_count)

if int(love) < 25:
    print(f"Your love: {love}%   :c")
elif int(love) < 50:
    print(f"Your love: {love}%   :/")
elif int(love) < 75:
    print(f"Your love: {love}%   :)")
else:
    print(f"Your love: {love}%   :O")