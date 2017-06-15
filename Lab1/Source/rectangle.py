import math                       # use of math module
print("Enter the value of length:")
length=int(input())               # fetch length using input function
print("Enter the value of breadth:")
breadth=int(input())              # fetch length using input function
perimeter= int(2*(length+breadth))  # mathematical formula for perimeter of the rectangle
print("The perimeter of the rectangle with the given length "+
      str(length) +" and breadth " + str(breadth) +" is "+ str(perimeter))  # print statement for the perimeter