class Employee:
    
    company="Tesla"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def printDetails(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My salary is {self.salary}")

e1=Employee("Abhishek",34,56000)
# e1.printDetails()
print(e1.company)

e2=Employee("Rohan",24,52000)
# e1.printDetails()
e2.company="Toyota"
print(e2.company)

# Employee.company="HP"

e3=Employee("Kashish",14,12000)
print(e3.company)


