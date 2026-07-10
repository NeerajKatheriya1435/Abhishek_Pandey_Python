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
    
    @classmethod
    def fromData(cls,str1):
        name,age,salary=str1.split("-")
        return cls(name,int(age),int(salary))


    # @classmethod
    # def meth1(cls,second):
    #     cls.company=second
    

# e1=Employee("Rohan",67,45000)
# print(e1.company)

# # Employee.meth1("HP")

# e2=Employee("Kashish",37,45000)
# print(e2.company)

# e3=Employee("Kashish",37,45000)
# print(e3.company)

# e4=Employee("Kashish",37,45000)
# print(e4.company)
# str1="Rohan-80-45000"
# e1=Employee(str1)

# e1=Employee.fromData(str1)
# e1.printDetails()

# e2=Employee("Kashish",56,45000)
# e2.printDetails()

# e3=Employee.fromData("Karan-26-43000")
# e3.printDetails()

# e1=Employee("Kashish",56,45000)
# print(dir(e1))
# print(e1.__dict__)
# str1="Hello"
# help(str1.upper)

# str1="Hello"
# help(str1.isalnum)