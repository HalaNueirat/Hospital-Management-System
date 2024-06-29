import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1452001",
    database="hospital"
)

mycursor = mydb.cursor()
mycursor.execute("drop table patient")
mydb.commit()
mycursor.execute("drop table doctors")
mydb.commit()
mycursor.execute("drop table bill")
mydb.commit()
mycursor.execute("drop table departments")
mydb.commit()
mycursor.execute("drop table medicine")
mydb.commit()
