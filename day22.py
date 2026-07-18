# # age=-459876

# # if (age<0 or age>120):
# #     raise ValueError("Age is not Possible")

# # if(age>18):
# #     print("You can drive the car")
# # else:
# #     print("You can not drive the car")

# a=7
# b=5

# # if

# # try:
# #     print("The division is:",(a/b))
# #     inp1=int(input("Enter the num1: "))

# # except ValueError as e:
# #     print("Please Input correct Integer",e)

# # except ZeroDivisionError as e:
# #     print("Can not divide by zero by Abhishek",e)

# # finally:
# #     print("This will run definetily")

# # else:
# #     print("With Succesful try syntax")

# # print("Important line")

# import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(
#         host="localhost",          # Change to your database server host
#         user="root",      # Your MySQL username (e.g., 'root')
#         password="password",  # Your MySQL password
#         database="tilak"   # The target database name
#     )

#     cursor = connection.cursor()

#     insertData="""
#     # insert into students(stdid,name,age) values
#     # (%s,%s,%s)
#     # """

#     # apnadata=(105,"Sajid",67)

#     # cursor.execute(insertData,apnadata)

#     # connection.commit()

#     # print(f"{cursor.rowcount} is affected")

#     # print(cursor.execute("select * from tilak"))

#     query = "SELECT * FROM students"
#     cursor.execute(query)

#     # 4. Fetch all rows from the executed query
#     rows = cursor.fetchall()

#     # 5. Loop through and display the data
#     print(f"\nTotal rows retrieved: {cursor.rowcount}\n")
#     for row in rows:
#         print(row)


# except Error as e:
#     print(f"Error while connecting to MySQL: {e}")
#     print(f"Inserted Record ID: {cursor.lastrowid}")

# finally:
#     # 7. Always close the cursor and connection cleanup
#     if 'connection' in locals() and connection.is_connected():
#         # cursor.close()
#         connection.close()
#         print("MySQL connection closed.")

