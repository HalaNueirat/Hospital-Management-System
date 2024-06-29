import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window2=Tk()
#create title for window
window2.title("Patient")

 # Set a default background color
window2.configure(background="#000000")  
#Set the image path & Load the image
background_image = ImageTk.PhotoImage(Image.open("C:/Users/zaytona/Downloads/hospital.jpg"))
# Create a Label widget to display the background image
background_label = Label(window2, image=background_image)
background_label.place(relwidth=1, relheight=1)
def add_patient():
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1452001",
        database="hospital"
    )

    # Create a cursor
    mycursor = mydb.cursor()

    # Get the values from the input fields
    ssn = int(ssn_entry.get())
    fname = fname_entry.get()
    lname = lname_entry.get()
    address = address_entry.get()
    tel_number = int(tel_entry.get())
    bdate = bdate_entry.get()
    dep_no = int(dep_entry.get())
    sex = sex_entry.get()
    blood_type = blood_entry.get()

    # SQL query to insert the patient into the database
    sql = """INSERT INTO patient (p_ssn, Fname, Lname, address, Tel_number, Bdate, dep_no, sex, blood_type) 
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    val = (ssn, fname, lname, address, tel_number, bdate, dep_no, sex, blood_type)

    try:
        # Execute the query
        mycursor.execute(sql, val)

        # Commit the changes
        mydb.commit()
        
        # Display a success message
        print("Patient added successfully!")
    except:
        # Display an error message
        print("Error")


#search for a patient       
def search_patient():
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1452001",
        database="hospital"
    )

    # Create a cursor
    mycursor = mydb.cursor()

    # Get the value from the search field
    ssn = int(search_entry.get())

    # SQL query to search for a patient by SSN
    sql = "SELECT * FROM patient WHERE p_ssn = %s"
    val = (ssn,)

    try:
        # Execute the query with the SSN parameter
        mycursor.execute(sql, (ssn,))

        # Fetch the row
        row = mycursor.fetchone()

        if row:
            ssn = row[0]
            first_name = row[1]
            last_name = row[2]
            address = row[3]
            tel_number = row[4]
            birth_date = row[5]
            department_no = row[6]
            sex = row[7]
            blood_type = row[8]

            # Update the text widget with the retrieved values
            result_text.delete("1.0", "end")
            result_text.insert("1.0", "SSN: " + str(ssn) + "\n")
            result_text.insert("end", "First Name: " + first_name + "\n")
            result_text.insert("end", "Last Name: " + last_name + "\n")
            result_text.insert("end", "Address: " + address + "\n")
            result_text.insert("end", "Tel Number: " + str(tel_number) + "\n")
            result_text.insert("end", "Birth Date: " + str(birth_date) + "\n")
            result_text.insert("end", "Department No.: " + str(department_no) + "\n")
            result_text.insert("end", "Sex: " + sex + "\n")
            result_text.insert("end", "Blood Type: " + blood_type)
        else:
            # Update the text widget with the "Patient not found" message
            result_text.delete("1.0", "end")
            result_text.insert("1.0", "Patient not found")

    except Exception as e:
        print("Error:", e)

    # Close the cursor and the database connection
    mycursor.close()
    mydb.close()
def delete_patient():
    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1452001",
            database="hospital"
        )

        # Create a cursor
        mycursor = mydb.cursor()

        # Get the value from the entry field
        ssn = int(delete_entry.get())

        # SQL query to delete a patient by SSN
        sql = "DELETE FROM patient WHERE p_ssn = %s"
        val = (ssn,)

        # Execute the query with the SSN parameter
        mycursor.execute(sql, val)

        # Commit the changes
        mydb.commit()

        # Display a success message
        print(f"Patient with SSN {ssn} deleted successfully!")

    except Exception as e:
        # Display an error message
        print(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

def update_manager():
    # Get the department name and new manager SSN from the entry widgets
    dep_name = dep_name_entry.get()
    new_mgr_ssn = new_mgr_ssn_entry.get()

    try:
        # Connect to the database
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1452001",
        database="hospital"
        )
        # Create a cursor
        mycursor = mydb.cursor()
        # Update the manager SSN in the Departments table based on the department name
        update_query = """
        UPDATE departments
        SET mgr_ssn =%s
        WHERE dep_name =%s
        """

        mycursor.execute(update_query,(new_mgr_ssn,dep_name))

        # Commit the changes
        mydb.commit()

        messagebox.showinfo("Success", "Manager information updated successfully.")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def calculate_total_bill():
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1452001",
        database="hospital"
    )

    # Create a cursor
    mycursor = mydb.cursor()
      # Get the value from the search field
    ssn = int(p_ssn_entry.get())
    Medicine_name = str(name_entry.get())
    sql = "SELECT medicine_id FROM medicine WHERE name = %s "
    mycursor.execute(sql, (Medicine_name,))
    row = mycursor.fetchone()

    if row:
        medicine_id = row[0]
    else:
        print("Medicine not found")
        return
    
    # Retrieve the price of the medicine using the medicine ID
    sql = "SELECT price FROM medicine WHERE medicine_id = %s"
    mycursor.execute(sql, (medicine_id,))
    row = mycursor.fetchone()

    if row:
        medicine_price = row[0]
    else:
        print("Medicine price not found")
        return
    
    # Calculate the total bill
    total_bill = medicine_price*int(amount_entry.get())
    
    # Insert the bill information into the database
    insert_sql = "INSERT INTO bill ( p_ssn, Bill_Date, method_payment, amount) VALUES ( %s, CURDATE(), %s, %s)"
  
    method_payment = "Cash"  # Example value, you can modify it based on your requirements
    values = ( ssn, method_payment, total_bill)
    mycursor.execute(insert_sql, values)
    mydb.commit()
    
    # Print the total bill amount
        # Print the total bill amount
    total_bill = str(total_bill)  # Convert the total bill to a string
    total_bill_label.config(text="Total Bill Amount: " + total_bill)
    print("Total Bill Amount:", total_bill)
    
    # Close the cursor and the database connection
    mycursor.close()
    mydb.close()    

# Create input fields and labels for each patient attribute
ssn_label = Label(window2, text="SSN:")
ssn_label.grid(row=0, column=0)
ssn_entry = Entry(window2, background="lightblue")
ssn_entry.grid(row=0, column=1)

fname_label = Label(window2, text="First Name:")
fname_label.grid(row=1, column=0)
fname_entry = Entry(window2, background="lightblue")
fname_entry.grid(row=1, column=1)

lname_label = Label(window2, text="Last Name:")
lname_label.grid(row=2, column=0)
lname_entry = Entry(window2, background="lightblue")
lname_entry.grid(row=2, column=1)

address_label = Label(window2, text="Address:")
address_label.grid(row=3, column=0)
address_entry = Entry(window2, background="lightblue")
address_entry.grid(row=3, column=1)

tel_label = Label(window2, text="Tel Number:")
tel_label.grid(row=4, column=0)
tel_entry = Entry(window2, background="lightblue")
tel_entry.grid(row=4, column=1)

bdate_label = Label(window2, text="Birth Date:")
bdate_label.grid(row=5, column=0)
bdate_entry = Entry(window2, background="lightblue")
bdate_entry.grid(row=5, column=1)

dep_label = Label(window2, text="Department No:")
dep_label.grid(row=6, column=0)
dep_entry = Entry(window2, background="lightblue")
dep_entry.grid(row=6, column=1)

sex_label = Label(window2, text="Sex:")
sex_label.grid(row=7, column=0)
sex_entry = Entry(window2, background="lightblue")
sex_entry.grid(row=7, column=1)

blood_label = Label(window2, text="Blood Type:")
blood_label.grid(row=8, column=0)
blood_entry = Entry(window2, background="lightblue")
blood_entry.grid(row=8, column=1)
# Create a button to add the patient
add_button = Button(window2, text="Add Patient", command=add_patient, background="lightblue")
add_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Create widgets for searching a patient
search_label = Label(window2, text="Search by SSN:")
search_label.grid(row=10, column=2, padx=10, pady=15)
search_entry = Entry(window2, background="lightblue")
search_entry.grid(row=10, column=3, padx=10, pady=15)

search_button = Button(window2, text="Search", command=search_patient, background="lightblue")
search_button.grid(row=10, column=4, columnspan=2, padx=10, pady=10)

# Create a text widget to display the search result
result_text = Text(window2, height=10, width=30)
result_text.grid(row=11, column=2, columnspan=2, padx=10, pady=10)

# Create widgets for deleting a patient
delete_label = Label(window2, text="Delete by SSN:")
delete_label.grid(row=0, column=7, padx=10, pady=15)
delete_entry = Entry(window2, background="lightblue")
delete_entry.grid(row=0, column=9, padx=10, pady=15)

delete_button = Button(window2, text="Delete Patient", command=delete_patient, background="lightblue")
delete_button.grid(row=1, column=8, columnspan=2, padx=10, pady=10)

# Create widgets for updating department manager
dep_name_label = Label(window2, text="Department Name:")
dep_name_label.grid(row=3, column=7, columnspan=2, padx=10, pady=10)
dep_name_entry = Entry(window2, background="lightblue")
dep_name_entry.grid(row=3, column=9, columnspan=2, padx=10, pady=10)

new_mgr_ssn_label = Label(window2, text="New Manager SSN:")
new_mgr_ssn_label.grid(row=4, column=7, columnspan=2, padx=10, pady=10)
new_mgr_ssn_entry = Entry(window2, background="lightblue")
new_mgr_ssn_entry.grid(row=4, column=9, columnspan=2, padx=10, pady=10)

update_button = Button(window2, text="Update Manager", command=update_manager, background="lightblue")
update_button.grid(row=5, column=8, columnspan=2, padx=10, pady=10)

# Create widgets for calculating total bill
p_ssn_label = Label(window2, text="Patient SSN:")
p_ssn_label.grid(row=7, column=7, columnspan=2, padx=10, pady=10)
p_ssn_entry = Entry(window2, background="lightblue")
p_ssn_entry.grid(row=7, column=9, columnspan=2, padx=10, pady=10)

name_label = Label(window2, text="Medicine Name:")
name_label.grid(row=8, column=7, columnspan=2, padx=10, pady=10)
name_entry = Entry(window2, background="lightblue")
name_entry.grid(row=8, column=9, columnspan=2, padx=10, pady=10)

amount_label = Label(window2, text="Amount:")
amount_label.grid(row=9, column=7, columnspan=2, padx=10, pady=10)
amount_entry = Entry(window2, background="lightblue")
amount_entry.grid(row=9, column=9, columnspan=2, padx=10, pady=10)

# Create a button to calculate the total bill
bill_button = Button(window2, text="Calculate Total Bill", command=calculate_total_bill, background="lightblue")
bill_button.grid(row=10, column=9, columnspan=2, padx=10, pady=10)

# Create a text widget to display the total bill result
total_bill_label = Label(window2, text="Total Bill Amount:")
total_bill_label.grid(row=11, column=9, columnspan=2,padx=10, pady=10)


# Run the Tkinter event loop
# Start the Tkinter event loop
window2.mainloop()
