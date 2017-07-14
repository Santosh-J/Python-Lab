

class Employee():
    emp=0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.emp)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Ebki", 1000)
emp2 =  Employee("maggi",1200)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()

class Manager (Employee):
    pass

m1 = Manager("Ebki", 1000)
m2 = Manager("maggi",1200)
m1.displayEmployee()
m2.displayEmployee()