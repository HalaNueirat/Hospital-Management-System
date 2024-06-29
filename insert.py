import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1452001",
    database="hospital"
)

mycursor = mydb.cursor()

sql = """INSERT INTO patient (p_ssn, Fname, Lname, address, Tel_number, Bdate, dep_no, sex, blood_type)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

val = [
    (1, 'lara', 'rashid', 'arraba', 596878, '1994-09-22', 1, 'F', 'O+'),
    (2, 'leen', 'sami', 'ajja', 597111, '1997-12-31', 2, 'F', 'O-'),
    (3, 'nour', 'hamad', 'yabad', 596222, '1995-05-16', 3, 'M', 'A+'),
    (4, 'omar', 'hani', 'yamon', 596888, '1996-12-18', 4, 'M', 'AB')
]

mycursor.executemany(sql, val)
mydb.commit()
sql="insert into doctors (ssn,university,specialization,bord )  values(%s,%s,%s,%s)"
val=[
   (1 , 'aaup' ,'bone', 'arabic'),
   (2 , 'bzu' ,'obstetrice', 'palestinian'),
   (3 , 'aau' ,'general', 'jordanian'),
   (4 , 'nnu' ,'surgery', 'syrian'),
   (5 , 'nnu' ,'nerves', 'palestinian') 
  
    ]
mycursor.executemany(sql,val)
mydb.commit()

sql="insert into medicine  (medicine_id,Name,method_of_use ,price )  values(%s,%s,%s,%s)"
val=[
   (1,'panadol','after_eating',30),
   (2,'novadixon','before_eating',50),
   (3,'trufen','after_eating',40),
   (4,'flu','before_eating',20),
   (5,'Aspirin','after_eating',55)
  
    ]
mycursor.executemany(sql,val)
mydb.commit()

sql = "INSERT INTO bill ( p_ssn, Bill_Date, method_payment, amount) VALUES ( %s, %s, %s, %s)"
val = [
    ( 1, '2020-09-22', 'checks', 1000),
    ( 2, '2021-12-31', 'bank', 2000),
    ( 3, '2021-05-16', 'cash', 500),
    ( 4, '2022-12-18', 'cash', 600)
]
mycursor.executemany(sql, val)
mydb.commit()
sql="insert into departments (dep_no,dep_name,mgr_ssn )  values(%s,%s,%s)"
val=[
    (1, 'bone',1),
    (2 , 'obstetrics',2),
    (3 , 'dialysis',3),
    (4, 'surgery',4),
    (5 , 'nerves',5)
    ]
mycursor.executemany(sql,val)
mydb.commit()
