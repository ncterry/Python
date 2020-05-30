"""
Work with databases
This is the same as   tkinter24_databases2
but we added a way to delete an entry here.

Delete entry box accepts OID numbers
OID is the primary key for this DB, the second entry in the DB will have OID = 2
Input       2        in delete_box, then press delete_button
This calls the delete function, which grabs the input in the delete_box
    and then runs an SQL command to delete the 2 entry in the DB 

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
root.geometry("600x600")
#
# Creates a new db, or connects to existing in stated directory.
connectionVar = sqlite3.connect('/root/Desktop/address_book.db')
cursorVar = connectionVar.cursor()  # Create cursor. Cursor takes command from here to db
# ----------------------------------------------------------------------------
# We added this table in tkinter23. Don't do it again. Now we add data to it.
# cursorVar.execute("""CREATE TABLE addresses (
#                 first_name text,
#                 last_name text,
#                 address text,
#                 city text,
#                 state text,
#                 zipcode integer )""") # Create table in th db
# ----------------------------------------------------------------------------
# Create function to delete a record
def delete():
    # Creates a new db, or connects to existing in stated directory.
    # Need this connection/cursor in every function
    connectionVar = sqlite3.connect('/root/Desktop/address_book.db')
    cursorVar = connectionVar.cursor()  # Create cursor. Cursor takes command from here to db

    # execute an SQL command
    # We have the command and then concatenate the value we get from delete box.
    # Delete the second entry into the database
    #          EX. DELETE from addresses WHERE oid= 2
    cursorVar.execute("DELETE from addresses WHERE oid=" + delete_box.get())

    connectionVar.commit()  # Commit changes
    connectionVar.close ()  # Close connection
# -------------------------End DELETE function.---------------------------------------------------

# Create submit function for submit Button
def submit():
    # Creates a new db, or connects to existing in stated directory.
    # Need this connection/cursor in every function
    connectionVar = sqlite3.connect('/root/Desktop/address_book.db')
    cursorVar = connectionVar.cursor()  # Create cursor. Cursor takes command from here to db
    # Grab entry boxes, and Insert into TABLE
    cursorVar.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
                        {
                            'f_name': f_name.get(),
                            'l_name': l_name.get(),
                            'address': address.get(),
                            'city': city.get(),
                            'state': state.get(),
                            'zipcode': zipcode.get()
                        })  # python dictionary --> key:value --> (value.get() from input box)
                        #
    connectionVar.commit()  # Commit changes
    connectionVar.close ()  # Close connection
    #
    f_name.delete(0, END) # Clear text boxes after submission
    l_name.delete(0, END) # Clear text boxes after submission
    address.delete(0, END) # Clear text boxes after submission
    city.delete(0, END) # Clear text boxes after submission
    state.delete(0, END) # Clear text boxes after submission
    zipcode.delete(0, END) # Clear text boxes after submission
# ----------END SUBMIT FUNCTION--------------------------------------------------------------
#
# Create query function. This currently prints first + last names from db
def query():
    # Creates a new db, or connects to existing in stated directory.
    # Need this connection/cursor in every function
    connectionVar = sqlite3.connect('/root/Desktop/address_book.db')
    cursorVar = connectionVar.cursor()  # Create cursor. Cursor takes command from here to db
    # Query the DB
    # Select ALL, from any DB entry that has an Original ID (primary key)
    # sqlite3 default creates an OID whether you state it or not. It's always there
    cursorVar.execute("SELECT *, oid FROM addresses")
    records = cursorVar.fetchall()      #.fetchone(),   .fetchmany(7)
    print(records)                      # just prints record list to terminal
    # Example print:
    # [('Nate', 'Terry', '412 W 10 St', 'Loveland', 'CO', 80537, 1),
    # ('Zach', 'Carey', '6220 Sterne Pkwy', 'Littleton', 'CO', 80231, 2)]

    # -------------
    # Add star line just for aesthetics when label gets printed on window.
    print_records = '**************\n'   # var to hold return results from for-loop below
    # ******************* Query Example 1 ***********************************
    # for record in records[0]:   # This look only looks at the first full record.
    #     print_records += str(record) + "\n"
    """         [Show Records]
                     Nate
                    Terry
                 412 W 10th st
                   Loveland
                      CO
                     80537
                       1
    """
    # ******************** Query Example 2 ********************************
    for record in records:   # Go through list, print every    f_name + l_name + OID
        print_records += str(record[0]) + " " + str(record[1]) +  " " + str(record[6]) + "\n"
    """                     Nate Terry
                            Zach Carey
    """
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)  # row=12 so that records printed below the delete button.
    # Now if you click the button "Show Records" it will place a label on root window
    # ----------------------------------------
    connectionVar.commit()  # Commit changes
    connectionVar.close ()  # Close connection
# -----------END QUERY FUNCTION-----------------------------------------------------------
#
# Create permanent text entry boxes on root window
f_name = Entry(root, width=30)          # Create box ------------------------
f_name.grid(row=0, column=1, padx=20, pady=(10,0))   # Position
l_name = Entry(root, width=30)          # --------------------------
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)         # --------------------------
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)            # --------------------------
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)           # --------------------------
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)         # --------------------------
zipcode.grid(row=5, column=1, padx=20)
#
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)
# -------------------------------------
# Create permanent text box labels on root window
f_name_label = Label(root, text="First Name")   # Create label
f_name_label.grid(row=0, column=0, pady=(10,0))              # Position label
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
#
delete_box_label = Label(root, text="Delete OID Number:")
delete_box_label.grid(row=9, column=0, padx=(10,0))
# -------------------------------------
# Create Submit Button
submit_buttton = Button(root, text="Add Record to Database", command=submit)
submit_buttton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=112) # ipadx = size of button
# -------------------------------------
# Create db query button.
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
# -------------------------------------
# Create a delete button
delete_button = Button(root, text="Delete OID Entry", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
# -------------------------------------
connectionVar.commit()  # Commit changes
connectionVar.close ()  # Close connection
# ==================
root.mainloop()
