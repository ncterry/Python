"""
Work with databases
The Is a simple example on how to create a simple database and add a table to it.
This table that we are adding does nothing other than place the structure of a table.
There will be  no data in it until next tkinter24_databases2.py

Be careful running this program, if you add the same table to a database, there
    could be conflict or overwriting.

>>> python3 tkinter23_databases.py
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
# Use sqlite3 database that comes with python. Not the most advanced but easy
import sqlite3
#
root = Tk()
root.title("Databases")
root.geometry("400x400")
#
# Create database or connect to connect to one
# Creates a new db in stated directory.
connectionVar = sqlite3.connect('/root/Desktop/address_book.db')
cursorVar = connectionVar.cursor()  # Create cursor. Cursor takes command from here to db
#
cursorVar.execute("""CREATE TABLE addresses (
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer )""") # Create table in th db
#
connectionVar.commit()  # Commit changes
connectionVar.close ()  # Close connection

# ==================
root.mainloop()
