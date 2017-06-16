print("Enter the string:")
str1=input()
a=0
b=0
for c in str1:
    if(c.isdigit()):
        a=a+1

    elif(c.isalpha()):
        b=b+1
print("the total number of digits are :", a)
print("the total number of letter are :", b)