print("Enter the numbers:")
numbers =input()
list1=list(numbers)
print(list1)
list2=list(list1[0])
list2.append(list1[-1])
print(list2)

