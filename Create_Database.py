import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1452001")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists hospital")
