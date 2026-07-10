class Car:
    
    def __init__(self,name,petrol,speed):
        self.name=name
        self.petrol=petrol
        self.speed=speed
    
    def carDetails(self):
        print(f"Car name is {self.name}")
        print(f"Car petrol limit is {self.petrol}")
        print(f"Car spped is {self.speed}")

    @staticmethod
    def addTwoNum(num1,num2):
        print(f"The sum is: {num1+num2}")


c1=Car("RangeRover",25,300)
# print(c1.name)
c1.carDetails()

c2=Car("Toyota",20,250)
# print(c2.name)
c2.carDetails()

Car.addTwoNum(4,8)


