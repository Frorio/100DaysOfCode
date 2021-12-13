#       Your program should print each number from 1 to 100 in turn

#       When the number is divisible by 3, then instead of printing the number it should print "Fizz"

#       Whet the number is divisible by 5, then instead of printing the number it should print "Buzz"

#       And if the number is divisible by both 3 and 5 e. g. 15 then
#       instead of the number it should print "FizzBuzz"

nums = list(range(1, 101))
for num in nums:
    if num % 3 == 0 and num % 5 == 0: print("Fizz Buzz") #Divisible by 3 and 5
    elif num % 5 == 0: print("Buzz") #Divisible by 5
    elif num % 3 == 0: print("Fizz") #Divisible by 3
    else: print(num) #not fizz or buzz num
    