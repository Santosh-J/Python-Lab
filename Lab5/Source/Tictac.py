import sys  # import sys for exit

class Tictactoe:           # class name

    def __init__(self):
        self.t = 0
        self.c = 0  # initialization
        self.r = 0  # initialization
        self.q = 0

    print("The size of the board is 3")
    n = 3  # size of the board
    aList = ['   ', '   ', '   ']
    bList = ['   ', '   ', '   ']
    cList = ['   ', '   ', '   ']
    w = ""




    def get(self):  # function definition

        print("  ")
        print("enter your choice")
        print("  ")
        c = int(input("Enter column:"))  # enter the column number
        c = c - 1
        r = int(input("Enter row:"))  # enter the row number
        if (r > 1):
            r = r * 2 - 1

        if (r == 1 and self.aList[c] != '   '):  # if condition
            print("Please re-enter")
            self.get()
            return
        if (r == 3 and self.bList[c] != '   '):  # if condition
            print("Please re-enter")
            self.get()
            return
        if (r == 5 and self.cList[c] != '   '):  # if condition
            print("Please re-enter")
            self.get()
            return
        if (r > 5 or c >= 3):
            print("Please re-enter")
            self.get()
            return

        print(c)
        print(r)
        self.q = self.q + 1;
        t = self.q
        #print("thus %d" % t)
        self.draw(c, r, t)

    def draw(self, c, r, q):
        if (r == 1 and q % 2 == 0 and self.aList[c] == "   "):

            self.aList[c] = " x "
        elif (r == 3 and q % 2 == 0 and self.bList[c] == "   "):

            self.bList[c] = " x "
        elif (r == 5 and q % 2 == 0 and self.cList[c] == "   "):

            self.cList[c] = " x "
        elif (r == 1 and q % 2 != 0 and self.aList[c] == "   "):

            self.aList[c] = " o "
        elif (r == 3 and q % 2 != 0 and self.bList[c] == "   "):

            self.bList[c] = " o "
        elif (r == 5 and q % 2 != 0 and self.cList[c] == "   "):

            self.cList[c] = " o "

        print(self.aList)  # to see where the x or o goes
        print(self.bList)
        print(self.cList)

        for i in range(7):

            hor = ""
            if (i % 2 == 0):
                for k in range(3):
                    hor = hor + " ---"

            elif (i % 2 != 0):
                for j in range(self.n + 1):
                    if (j < 3 and i == 1):
                        hor = hor + "|" + self.aList[j]
                    if (j < 3 and i == 3):
                        hor = hor + "|" + self.bList[j]
                    if (j < 3 and i == 5):
                        hor = hor + "|" + self.cList[j]
                    elif (j == 3):
                        hor = hor + "|"
            if (i < 7):
                print(hor)
        print("")
        for i in range(3):
            j = 0
            if (self.aList[i] == self.bList[i] == self.cList[i] and self.aList[i] == self.bList[i] == self.cList[
                i] != "   "):
                print("winner is player %s" % self.aList[i])
                sys.exit()
            if (i == 0):
                if (self.aList[j] == self.aList[j + 1] == self.aList[j + 2] and self.aList[j] == self.aList[j + 1] ==
                    self.aList[j + 2] != "   "):
                    print("winner is player %s" % self.aList[j])
                    sys.exit()
            if (i == 1):
                if (self.bList[j] == self.bList[j + 1] == self.bList[j + 2] and self.aList[j] == self.aList[j + 1] ==
                    self.aList[j + 2] != "   "):
                    print("winner is player %s" % self.aList[j])
                    sys.exit()
            if (i == 2):
                if (self.aList[j] == self.aList[j + 1] == self.aList[j + 2] and self.aList[j] == self.aList[j + 1] ==
                    self.aList[j + 2] != "   "):
                    print("winner is player %s" % self.aList[j])
                    sys.exit()
            if (self.aList[j] == self.bList[j + 1] == self.cList[j + 2] and self.aList[j] == self.bList[j + 1] ==
                self.cList[j + 2] != "   "):
                print("winner is player %s" % self.aList[j])
                sys.exit()
            if (self.cList[j] == self.bList[j + 1] == self.aList[j + 2] and self.cList[j] == self.bList[j + 1] ==
                self.aList[j + 2] != "   "):
                print("winner is player %s" % self.cList[j])
                sys.exit()

    def star(self):
        for q in range(9):
            self.get()


ob = Tictactoe()
ob.star()