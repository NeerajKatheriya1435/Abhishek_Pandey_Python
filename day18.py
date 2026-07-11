class Employee:
    
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        # print("Hello Good morning")
    
    # def greet(self):
    #     print("Good morning123")

    
# class Programmer(Employee):

    # def __init__(self, name, age, salary,language):
    #     super().__init__(name, age, salary)
    #     self.language=language
    #     # print("After Employee")

    # def canProgram(self):
    #     print("Program can program")
    #     super().greet()

# e1=Employee("John",45,89000)

# p1=Programmer("Sangeeta",34,34000,"Python")
# p1.canProgram()

# class Employee:
    
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def __str__(self):
#         return f"My name is: {self.name} and age is: {self.age}"
    
#     def __len__(self):
#         return len(self.name)

# e1=Employee("Niketan",78,36000)

# print(dir(e1))
# print(e1)
# print(len(e1))
# print(e1.__str__())

# class Point:
#     def __init__(self,xpoint,ypoint):
#         self.xpoint=xpoint
#         self.ypoint=ypoint

#     def __add__(self, rohan):
#         self.xpoint=self.xpoint+rohan.xpoint
#         self.ypoint=self.ypoint+rohan.ypoint
#         return Point(self.xpoint,self.ypoint)

#     def __str__(self):
#         return f"({self.xpoint},{self.ypoint})"

# p1=Point(5,7)
# print(p1)

# p2=Point(7,8)
# print(p2)

# p3=p1+p2
# print(p3)