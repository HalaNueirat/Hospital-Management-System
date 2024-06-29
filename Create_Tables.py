import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1452001",
    database="hospital"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE if not exists patient (
  p_ssn INT PRIMARY KEY,
  Fname VARCHAR(20),
  Lname VARCHAR(20),
  address VARCHAR(20),
  Tel_number INT(7),
  Bdate DATE,
  dep_no INT NOT NULL,
  sex CHAR(1),
  blood_type VARCHAR(2)
)
""")

mycursor.execute("""
CREATE TABLE if not exists Bill (
    Bill_Id INT auto_increment PRIMARY KEY,
    p_ssn INT(6) NOT NULL,
    Bill_Date DATE,
    Method_payment VARCHAR(15),
    amount INT(6)
)
""")

mycursor.execute("""
CREATE TABLE if not exists Doctors (
    ssn INT PRIMARY KEY,
    university VARCHAR(20),
    specialization VARCHAR(20),
    Bord VARCHAR(20)
)
""")

mycursor.execute("""
CREATE TABLE if not exists Medicine (
    medicine_id INT PRIMARY KEY,
    Name VARCHAR(20),
    method_of_use VARCHAR(20),
    price INT
)
""")

mycursor.execute("""
CREATE TABLE if not exists Departments (
    dep_no INT PRIMARY KEY,
    dep_name VARCHAR(20),
    mgr_ssn INT NOT NULL
)
""")
