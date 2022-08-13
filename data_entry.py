"""Authomatically creates a file in the directory called addressess"""
# From DataBase file

from logging import root
from tkinter import *
import sqlite3
from turtle import st

root = Tk()
root.title("Database")
root.geometry("365x450")

# Creating Table(Columns and rows)
"""Already created in Database file"""

# Creating the submit function

def submit():
    # To submit to the database itself we create a cursor in the function
    
    # Creating a database or connect to one
    conet = sqlite3.connect("address_book.db")
    # creating a cursor
    cus = conet.cursor()

    # Insert into table
    cus.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:country,:city,:state,:zipcode)",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'country': country.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
    }
    
    )

    # clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    country.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

    # commit any changes to database
    conet.commit()
    # Close database in the functiong after changes
    conet.close()

# Creating the query function(show) to display data

def show():

    # To show the database itself we create a cursor in the function
    
    # Creating a database or connect to one
    conet = sqlite3.connect("address_book.db")
    # creating a cursor
    cus = conet.cursor()
    
    # Querying to database
    cus.execute("SELECT *,oid FROM addresses") # oid is the primary  key id
    records = cus.fetchall()
    # prints in terminal[a list]
    print(records)
    # loop through records
    print_records = ''
    for record in records:
        print_records += str(record[0])+" "+str(record[1])+"\t"+str(record[7])+ "\n" 
    # show records in root window 
    show_label = Label(root,text = print_records)
    show_label.grid(row=12,column=0,columnspan=2)

    # commit any changes to database
    conet.commit()
    # Close database in the functiong after changes
    conet.close()

# Creating function to delete a record

def delete_box():

    # To delete data from the database itself we create a cursor in the function
    
    # Creating a database or connect to one
    conet = sqlite3.connect("address_book.db")
    # creating a cursor
    cus = conet.cursor()

    # Delete a record
    cus.execute("DELETE from addresses WHERE oid=" + id.get())
    id.delete(0,END)

    # commit any changes to database
    conet.commit()
    # Close database in the functiong after changes
    conet.close()

# Creating the edit function

def edit_box():

    # Create another windows 
    global edit
    edit = Tk()
    edit.title("Edit A Record")
    edit.geometry("300x270")
        
    # Creating a database or connect to one
    conet = sqlite3.connect("address_book.db")
    # creating a cursor
    cus = conet.cursor()
    
    # Getting id to edit
    record_id = id.get()
    # Querying to database
    cus.execute("SELECT * FROM addresses WHERE oid=" + record_id) # oid is the primary  key id
    records = cus.fetchall()
    # create Global variables for the textbox names
    global f_nameedit
    global l_nameedit
    global addressedit
    global countryedit
    global cityedit
    global stateedit
    global zipcodeedit
    # Creating text boxes
    f_nameedit = Entry(edit,width=30)
    f_nameedit.grid(row=0,column=1,padx=20,pady=(10,0)) # top,buttom

    l_nameedit = Entry(edit,width=30)
    l_nameedit.grid(row=1,column=1)

    addressedit = Entry(edit,width=30)
    addressedit.grid(row=2,column=1)

    countryedit = Entry(edit,width=30)
    countryedit.grid(row=3,column=1)

    cityedit = Entry(edit,width=30)
    cityedit.grid(row=4,column=1)

    stateedit = Entry(edit,width=30)
    stateedit.grid(row=5,column=1)

    zipcodeedit = Entry(edit,width=30)
    zipcodeedit.grid(row=6,column=1) 

    # creating the text box label
    f_name_label = Label(edit , text= "First Name :")
    f_name_label.grid(row=0,column=0)

    l_name_label = Label(edit , text= "Last Name :")
    l_name_label.grid(row=1,column=0)

    address_label = Label(edit , text= "Address :")
    address_label.grid(row=2,column=0)

    country_label = Label(edit , text= "Country :")
    country_label.grid(row=3,column=0)

    city_label = Label(edit , text= "City :")
    city_label.grid(row=4,column=0)

    state_label = Label(edit , text= "State :")
    state_label.grid(row=5,column=0)

    zipcode_label = Label(edit , text= "Zipcode :")
    zipcode_label.grid(row=6,column=0)

    # Loop through records which is a list
    for record in records:
        f_nameedit.insert(0,record[0])
        l_nameedit.insert(0,record[1])
        addressedit.insert(0,record[2])
        countryedit.insert(0,record[3])
        cityedit.insert(0,record[4])
        stateedit.insert(0,record[5])
        zipcodeedit.insert(0,record[6])

    save_but = Button(edit,text = "Save The ID Records",command=save_box)
    save_but.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=38)
    
    edit.mainloop()

def save_box():
    
    # To delete data from the database itself we create a cursor in the function
    
    # Creating a database or connect to one
    conet = sqlite3.connect("address_book.db")
    # creating a cursor
    cus = conet.cursor()
    record_id = id.get()
    # Updating a record
    cus.execute("""UPDATE addresses SET 
    first_name = :f_name,
    last_name = :l_name,
    address = :address,
    country = :country,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
    WHERE oid = :oid""",
    {
        'f_name': f_nameedit.get(),
        'l_name': l_nameedit.get(),
        'address': addressedit.get(),
        'country': countryedit.get(),
        'city': cityedit.get(),
        'state': stateedit.get(),
        'zipcode': zipcodeedit.get(),
        'oid': record_id 
    }
    )

    # commit any changes to database
    conet.commit()
    # Close database in the functiong after changes
    conet.close()

    edit.destroy()

#Adding to the table

# Creating text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0)) # top,buttom

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)

address = Entry(root,width=30)
address.grid(row=2,column=1)

country = Entry(root,width=30)
country.grid(row=3,column=1)

city = Entry(root,width=30)
city.grid(row=4,column=1)

state = Entry(root,width=30)
state.grid(row=5,column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=6,column=1)

# Create a delete text box
id = Entry(root,width=30,bg='brown',fg='white')
id.grid(row=9,column=1)

# creating the text box label
f_name_label = Label(root , text= "First Name :")
f_name_label.grid(row=0,column=0)

l_name_label = Label(root , text= "Last Name :")
l_name_label.grid(row=1,column=0)

address_label = Label(root , text= "Address :")
address_label.grid(row=2,column=0)

country_label = Label(root , text= "Country :")
country_label.grid(row=3,column=0)

city_label = Label(root , text= "City :")
city_label.grid(row=4,column=0)

state_label = Label(root , text= "State :")
state_label.grid(row=5,column=0)

zipcode_label = Label(root , text= "Zipcode :")
zipcode_label.grid(row=6,column=0)

# Creating a delete label
id_label = Label(root,text = "Select ID",pady=5)
id_label.grid(row=9,column=0)

# Creating the submit button
sub_but = Button(root,text = "Add Records To Database",command=submit)
sub_but.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

# Creating a query button to show our record
q_but = Button(root,text = "Show Records",command=show)
q_but.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=50)

# Creating a delete button
q_but = Button(root,text = "Delete The ID Records",command=delete_box)
q_but.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=30)

# Creating an Update or Edit button
up_but = Button(root,text = "Edit The ID Records",command=edit_box)
up_but.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=38)

root.mainloop()