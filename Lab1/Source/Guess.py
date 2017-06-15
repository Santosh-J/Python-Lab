import random                 # use of random module
print("Hello! welcome to the Guess Game!")   # intro line using print
print("A random number is generated by the PC and you need to guess it in one chance.")
num=random.randint(1,10)          # Creation of random number from 1 to 10
print("Random number is generated from 1 to 10. Now try to guess it.")
print("Enter your number:")
num1=int(input())                 # fetching the input from user
if(num1==num):                    # if user's input is equal to the number generated
    print("Perfect! You have guessed it correct " + "The number is " + str(num))
elif(num1<num):                   # use of elif statement
    print("The number you guessed is lower than required."+ "The number generated is "+ str(num))
else:
    print("The number is greater than required."+ "The number generated is "+ str(num))
print("Thank You for playing!" + "Better luck next time!")