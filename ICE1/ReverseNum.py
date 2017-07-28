num=int(input("enter the num:"))
reverseNumber = ""
while( num!=0):
    remainder=num%10

    num=num//10

    reverse=0
    reverse = (reverse *10)+remainder
    reverseNumber = reverseNumber+str(reverse)

print(reverseNumber)

