import string  # import string module
print("Please enter your string: ")  # print
str1=input()   # take input
letters=set(string.ascii_uppercase) # use of function ascii_uppercase
if(set(str1.upper())>=letters):  # checking if all the letters are present
    print("all the letters are present")   # use of print
else:
    print("all the letters are not present") # use of print