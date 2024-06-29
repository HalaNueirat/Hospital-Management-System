import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1452001",
    database="hospital"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM patient")
result = mycursor.fetchall()
for row in result:
    print(row)

mycursor.execute("SELECT * FROM departments")
result = mycursor.fetchall()
for row in result:
    print(row)

mycursor.execute("SELECT * FROM bill")
result = mycursor.fetchall()
for row in result:
    print(row)

mycursor.execute("SELECT * FROM medicine")
result = mycursor.fetchall()
for row in result:
    print(row)

mycursor.execute("SELECT * FROM doctors")
result = mycursor.fetchall()
for row in result:
    print(row)
