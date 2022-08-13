"""Authomatically creates a file in the directory called addressess"""

from logging import root
from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("400x400")

# Creating a database or connect to one

conet = sqlite3.connect("address_book.db")
# creating a cursor
cus = conet.cursor()

# Creating Table(Columns and rows)
cus.execute(
    """CREATE TABLE
    addresses(
        first_name text,
        last_name text,
        address text,
        country text,
        city text,
        state text,
        zipcode integer
    )
    """
)

# commit any changes to database
conet.commit()
# Close database
conet.close()


root.mainloop()