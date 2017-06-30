c = 0   # initialization
r = 0     # initialization
print("The size of the board is 3")
n = 3      # size of the board
aList = ['   ', '   ', '   ']
bList = ['   ', '   ', '   ']
cList = ['   ', '   ', '   ']
w = ""


def get():  # define the function
    c = int(input("Enter column:")) # enter the column number
    c = c - 1
    r = int(input("Enter row:"))   # enter the row number
    if (r > 1):
        r = r * 2 - 1
   # print(c)
    #print(r)

    if (r == 1 and aList[c] != '   '):  # if condition
        get()
    if (r == 3 and bList[c] != '   '):  # if condition
        get()
    if (r == 5 and cList[c] != '   '):   # if condition
        get()
    return c, r


def printme():                   # function definition
    for q in range(9):
        c, r = get()

        if (r == 1 and q % 2 == 0):

            aList[c] = " x "
        elif (r == 3 and q % 2 == 0):

            bList[c] = " x "
        elif (r == 5 and q % 2 == 0):

            cList[c] = " x "
        elif (r == 1):
            aList[c] = " o "
        elif (r == 3):
            bList[c] = " o "
        elif (r == 5):
            cList[c] = " o "
        print(aList)               # to see where the x or o goes
        print(bList)
        print(cList)
        for i in range(7):

            hor = ""
            if (i % 2 == 0 or i == 6):
                for k in range(3):
                    hor = hor + " ---"

            elif (1):
                for j in range(n + 1):
                    if (j < 3 and i == 1):
                        hor = hor + "|" + aList[j]
                    if (j < 3 and i == 3):
                        hor = hor + "|" + bList[j]
                    if (j < 3 and i == 5):
                        hor = hor + "|" + cList[j]
                    elif (j == 3):
                        hor = hor + "|"


            print(hor)


for q in range(9):         # for q in cells ranging from 0 to 8.
    printme()

