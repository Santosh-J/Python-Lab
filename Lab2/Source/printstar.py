import string  # import string module
print("Enter your name:")  # print statement
str1=input()               # take the input
ch=str1[0]                 # fetch the first letter of the input
print(ch)                 # print that letter
if (ch=='s' or ch=='S'):             # use of if statement
    for row in range(7):              # code only for the letter s
        for col in range(5):
            if (row == 0 or row == 6 or row == 3 or (col == 0 and (row > 0 and row < 4)) or (col == 4 and (row > 3 and row < 7))):
                print("*", end="")
            else:
                print(end=" ")
        print()
else:
    print("Please enter your input starting with S ")