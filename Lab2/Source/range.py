import math    # import the math module
print("The numbers which are divisible by 5 and 7 between 1500 and 2700 :") # print statement
for i in range(1500,2700):  # use of range function
    if (i%5==0 and i%7==0):   # condition
        print(i) # print the number.
    else:
        print("Condition not met ")
