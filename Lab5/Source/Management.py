class Person():      # class
    pass

    def __init__(self, name, book): # methods
        self.name = name
        self.book = book

    def perdetails(self):        # method
        print("Customer name: %s" % self.name)
        print("Book name: %s" % self.book)


class Books():     # class
    pass

    def __init__(self):      # methods
        self.totalbooks = 80
        self.oldbooks = 40
        self.newbooks = 40

    def bookdetails(self):
        print("Customer name: %s" % self.totalbooks)
        print("Book name: %s" % self.oldbooks)
        print("Book name: %s" % self.newbooks)


class Student():   # class
    pass

    def __init__(self, name, ssn):   #methods
        self.name = name
        self.ssn = ssn

    def studetails(self):
        print("Student name: %s" % self.name)
        print("SSN : %d" % self.ssn)




class Librarian(Person, Student):   #class
    pass

    def __init__(self, name, salary):   #methods
        self.name = name
        self.salary = salary

    def libdetails(self):
        print("Librarian:", self.name, "  Salary", self.salary)

class Library(Librarian):           # class
    def __init__(self, name, booknum):
        self.name = name
        self.booknum = booknum

    def pr(self):                  # method
        print(self.name)
        super.__init__("tarun","$7000")

# object creations and calling

pers =Person("santo","The Invincible")
pers.perdetails()

stu=Student("Marice",521)
stu.studetails()



obj=Librarian("Mabi", 3000)
obj.libdetails()


ob = Library("Miller", 13000)
print("The name of the library: %s" % ob.name)
print("The total number of books: %d" % ob.booknum)




