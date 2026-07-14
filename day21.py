
import time

# print(time.time())

# start=time.time()

# for i in range(35000):
#     print(i)

# end=time.time()

# print(end-start)

# print(time.localtime())

# local=time.localtime()
# parser=time.strftime("%Y/%m/%d %H:%M:%S", local)
# print("The time is:",parser)

# print(time.ctime())

# print("helllo i am hacker...............")
# time.sleep(3)
# print("Your system has hack")

import requests

# response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.text)

# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# import requests
# response =requests.get("https://jsonplaceholder.typicode.com/users")
# print(response.status_code)
# print(response.json())

# payload = {'username': 'neeraj', 'password': '1234'}
# response = requests.post('https://httpbin.org/post', data=payload)
# print(response.status_code)
# print(response.json()) # Converts JSON response to Python dict

# params = {'q': 'canada best image'}
# response = requests.get('https://www.google.com/search',params=params)
# print(response.url)

# import argparse

# myParser=argparse.ArgumentParser(description="my description")

# myParser.add_argument("num1",type=float,help="First Num")
# myParser.add_argument("num2",type=float,help="Second Num")
# myParser.add_argument("--operation","-o",choices=["add","sub"])

# obj=myParser.parse_args()

# if obj.operation=="add":
#     print(obj.num1+obj.num2)
# else:
#     print(obj.num1-obj.num2)

# li1=[i for i in range(3400000000)]
# print(li1[0])

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1
# num1=count_up_to(45)
# print(next(num1))
# print(next(num1))

# # print("heelo")
# # print(next(num1))

# for i in range(5):
#     print(next(num1))