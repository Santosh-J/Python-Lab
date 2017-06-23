print("Enter the size of the board:")
n=int(input())
for i in range(n):
    hor=""
    ver=""
    for j in range(n):
        hor = hor + " ---"
    print (hor)
    for k in range(n+1):
        ver= ver+ "|   "
    print(ver)
hor=""
for j in range(n):
    hor = hor + " ---"
print (hor)

