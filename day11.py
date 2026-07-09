
# class Human:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
    
#     @property
#     def getName(self):
#         return self.name
    

#     @getName.setter
#     def setName(self,second):
#         if len(second)>3:
#             self.name=second


# h1=Human("Geeta",56,23000)

# h1.name="%^&*()"
# print(h1.name)

# h1.setName="Abhishek"
# print(h1.getName)


# def greet():
#     print("Happy Birthday Abhi")

# def addTwoNum(num1,num2):
#     print("The sum is:",(num1+num2))

# print("Hello")
# greet()
# print("BBBBBBBBBBBYYYYYYYYYYEEEEEEEEE")

# def decor(func1):
#     print("-----------------")
#     func1(7,4)
#     print("-----------------")

# decor(greet)
# decor(addTwoNum)



# def decorator(func1):
#     def wrapper():
#         print("--------------")
#         func1()
#         print("--------------")
#     return wrapper


# @decorator
# def greet():
#     print("Happy Birthday Abhi")


# @decorator
# def helloFunc():
#     print("Hello abhi")
#     print("Nice to meet you")

# greet()
# helloFunc()

# class Animal:

#     def run(self):
#         print("Animal is running")

#     def walk(self):
#         print("Animal is walking")


# a1=Animal()
# a1.run()
# a1.walk()

# class Cow(Animal):

#     def eatGrass(self):
#         print("Cow is Eating the grass")


# class Bull(Cow):

#     def plough(self):
#         print("Bull is plouging the Field")

# c1=Cow()
# c1.eatGrass()
# c1.run()
# c1.walk()

# c1=Bull()
# c1.eatGrass()
# c1.run()
# c1.walk()
# c1.plough()

# class Cat(Animal):
#     def mew(self):
#         print("Cat iw mewing")

# c2=Cat()
# c2.run()
# c2.mew()

# class Horse(Cow,Cat):
#     def fastRun(self):
#         print("Horse is running")

# h1=Horse()
# h1.walk()
# h1.fastRun()
# h1.mew()

# class Human:

#     def __init__(self,name,age,salary):
#         self.__name=name
#         self._age=age
#         self.salary=salary

# h1=Human("Rohan",34,90000)
# print(h1.__name)
# print(h1.salary)
# print(h1._Human__name)

# def AddtWnum():
#     """Hello add twnum"""
#     pass

# print(AddtWnum.__doc__)