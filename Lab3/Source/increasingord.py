# definition of function called second
def Second(elem):
    return elem[1]
# given list of tuples
tup1=(7,5)
tup2=(3,1)
tup3=(2,3)
# create a new list
k=[]
#append the tuples to list
k.append(tup1)
k.append(tup2)
k.append(tup3)
print("The list of tuples is"+ str(k))
#sort the list using the function Second with key
k.sort(key=Second)
# print the sorted list
print( "The sorted list  is " + str(k))


