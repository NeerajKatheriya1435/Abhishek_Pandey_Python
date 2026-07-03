

# def addTwoNum(num1,num2):
#     print(num1+num2)

# addTwoNum(4,7)

# def greet():
#     a=8
#     b=7
#     avg=(a+b)/2
#     # print("Good morning")
#     return avg

# print(greet())

# def addTwNum(*num):
#     # print(num)
#     sum=0
#     for i in num:
#         sum+=i
#     # # print(num1+num2)
#     # print("helo")
#     print(sum)


# addTwNum(4,5)
# addTwNum(4)
# addTwNum(,4)

# addTwNum(4,5,6,4,3)
# addTwNum(4,5,6,4,3,4,3,2)

# def greet(**kwags):
#     print(kwags)

# greet(name="Rohan",age=56)

# l1=[3,4,5,7,4,5,4,3,8]

# l1[3]=89
# print(l1[3])
# print(l1[2])

# print(l1[2:6])
# print(l1[2:])
# print(l1[:])
# print(l1[::2])

# l1=[i for i in range(50) if i>45]
# print(l1)

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]

# namesWith_O = [item for item in names if len(item)>5]
# print(namesWith_O)
# Example 1:

# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# colors.reverse()
# print(colors)

# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)
# colors.insert(2,"Rohan")
# colors.append("Rohan")
# colors.pop()
# colors.remove("green")
# del colors
# print(colors)
# l1=[4,5,6]
# l2=[2,7,3]

# l1.extend(l2)
# print(l1+l2)

# t1=(23,5,2022,5,5)

# t1[3]=89
# l1=list(t1)
# l1.insert(2,78)
# t1=tuple(l1)

# print(t1.count(5))
# print(t1.index(2022))

name="Neeraj"
age=67

# str1="Hello my name is {1} and age is {0}"
# print(str1.format(name,age))
# print(str1.format(age,name))
# print(str1.format(age,name))

# madam
# print(f"My name is {name} and age is {age}")



# l1=[4,6,23,4,7]

# max=l1[0]

# for i in l1:
#     if(i>max):
#         max=i

# print(max)

# l1=[14,7,9,3,2]

# length=len(l1)

# for i in range(length-1):
#     for j in range(0,(length-i-1)):
#         if(l1[j]>l1[j+1]):

#             temp=l1[j]
#             l1[j]=l1[j+1]
#             l1[j+1]=temp
# print(l1)
# a=8

l1=[4,5,7,3,8]

largest=l1[0]
# second=l1[0]

# for i in l1:
#     if i>largest:
#         second=largest
#         largest=i
#         # print(second)
#         # print(largest)

#     elif(i<largest and i>second):
#         second=i

# print(largest)
# print(second)

def checkPrime(num):
    for i in range(2,num):
        if(num%i==0):
            return True

numnew=56

# if(checkPrime(numnew)):
#     print("Not Prime")
# else:
#     print("Prime")

# for i in range(1,100):
#     if(checkPrime(i)):
#         pass
#     else:
#         print(i)

# def fact(num):
#     fact1=1
#     for i in range(1,num+1):
#         fact1=fact1*i
#     return fact1
    
# print(fact(5))