# class Employee:
    
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
    
#     def greet(self):
#         print("Good Morning")


# class Programmer(Employee):

#     def __init__(self, name, age, salary,language):
#         super().__init__(name, age, salary)
#         self.language=language
    
#     def canProgram(self):
#         print("Programmer can run the program in",self.language)
#         super().greet()

# e1=Employee("Abhishek",67,45000)

# p1=Programmer("Tilak",45,23000,"Python")
# p1.canProgram()


# class Employee:
    
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
    
#     def greet(self):
#         print("Good Morning")


# e1=Employee("Rohan",78,34000)

# class Programmer(Employee):

#     def __init__(self, name, age, salary,language):
#         super().__init__(name, age, salary)
#         self.language=language
    
#     def canProgram(self):
#         print("Programmer can run the program in",self.language)
#         super().greet()

# print(dir(e1))
# print(e1.__dict__)
# print(e1.__init_subclass__())

# p1=Programmer("Tilak",45,23000,"Python")
# p1.canProgram()
# print(p1.__init_subclass__())


# class Employee:
    
    # def __init__(self,name,age,salary):
    #     self.name=name
    #     self.age=age
    #     self.salary=salary

    # def __str__(self):
    #     return f"My name is: {self.name} and age is: {self.age}"
    
    # def greet(self):
    #     print("Good Morning")

    # def __len__(self):
    #     return len(self.name)
    
    # def __repr__(self):
    #     return f"My name is = {self.name} and age= {self.age}"

        

# e1=Employee("Rohan",78,34000)

# print(e1)
# print(f"Total Character in my name is: {len(e1)}")

# e2=Employee("Kashish",34,38000)
# print(e2)
# print(f"Total Character in my name is: {len(e2)}")

# print(repr(e1))


# class Points:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __str__(self):
#         return f"({self.x},{self.y})"
    
#     def __add__(self, other):
#         self.x=self.x+other.x
#         self.y=self.y+other.y
#         return Points(self.x,self.y)

# p1=Points(5,8)
# p2=Points(7,2)

# print(p1)
# print(p2)


print(p1)
print(p2)
p3=p1+p2
print(p3)

