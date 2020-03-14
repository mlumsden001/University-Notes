class Employee:

    def __init__(self, name , age , employeeID):
        self.employeeID = employeeID
        self.name = name
        self.age = age

    def getName(self):
        return "Name: " + self.name

    def getAge(self):
        return "Age:", self.age

    def getEmployeeID(self):
        return "Employeed ID:", self.employeeID

    def toString(self):
        return "[",  self.name, ",", self.age, ",", self.employeeID, "]"

def readPeople(people):
    for p in people:
        print(p.toString())


def addPeople(people, p):
    people.append(p)


people = []

tom = Employee("Tom", 40, 234563)
matt = Employee("Matt", 35, 244545)
addPeople(people, tom)
print(tom.getName())
print(tom.getAge())
print(tom.getEmployeeID())
