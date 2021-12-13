#### First way to do it #####

#   Data massive form 1 to 100
#   nums = list(range(1, 101))
#   res = 0

#    for num in nums:
#        if num % 2 == 0:
#            res += num
#    print(res)

#### Second way to do it ####

res = 0

# Range starting form 2 to 100 (2, 4, 6, 8, 10... 100)
for num in range(2, 101, 2):
    res+=num
print(res)