
# a=7
# def addNum():
#     # a=8
#     print(a)

# addNum()
# print(a)

# file1=open("data.txt","r")
# print(file1.read())
# file1.close()

# ptr1=open("kashish.txt","w")
# ptr1=open("kashish.txt","a")
# ptr1.write("Akshay is good boy and \nhow are you")
# ptr1.write("Suman is good girl")
# ptr1.write("Rohan is good boy")
# ptr1.write("Naya Content bhi add ho jaye")

# file1=open("data.txt","rb")
# print(file1.read())
# file1.close()

# file1=open("data.txt","r")
# print(file1.readline())
# print(file1.readline())
# file1.close()

# while True:
#     temp=file1.readline()
#     if not temp:
#         break
#     print(temp)

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()

# file1=open("data.txt","r")
# print(file1.readline()) 
# file1.seek(0)

# print(file1.readline())
# print(file1.tell())
# file1.close()

# with open("data1.txt","w") as f:
#     f.write("Hello Abhishek")
#     f.truncate(5)

# l1=[3,4,5,6,7]

# def graceFunc(num):
#     return num+5

# graceFunc=lambda a:a+5
# graceFunc=lambda a:a*a

# print(graceFunc(8))

# from functools import reduce
# l1=[3,4,5,6,7]

# lsit1=list(map(lambda a:a+5,l1))
# print(lsit1)

# lsit1=list(filter(lambda a:a>5,l1))
# print(lsit1)

# lsit1=reduce(lambda a,b:a+b,l1)
# print(lsit1)

# a=5
# b=5

# print(a is b)
# print(a == b)

# c=[1,4,5]
# d=[1,4,5]

# print(c is d)
# print(c == d)


