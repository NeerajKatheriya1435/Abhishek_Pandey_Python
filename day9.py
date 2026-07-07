
class Human:
    # name="Rohan"
    # age=56
    # salary=45000

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        # print("hello constructor")
    
    def details(self):
        print(f"My name is {self.name}")
        print(f"My name is {self.age}")
        print(f"My name is {self.salary}")
    
        

h1=Human("Rohan",78,45000)
h1.details()
# Human.details(h1)
# print(h1.name)
# print(h1.age)
# print(h1.salary)

h2=Human("Durga",18,49000)
h2.details()
# print(h2.name)
# print(h2.age)
# print(h2.salary)