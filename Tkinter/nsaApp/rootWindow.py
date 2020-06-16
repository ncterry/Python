"""
This is the root window for the NSA based App.
This application has many python actions such as:
    pingsweep
    portscan
    arpspoof    etc...

We will have a dropdown menu on the root page.
    ex. Choose portscan
        This opens another window.
        Enter an IPv4 + Click button.
        It will run a portscan and print to label.
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("NSA Application")
root.geometry("500x800")
# --------------------------------------------------
# Root Window Title
mainlabel = Label(root, text="NSA Tools", font=("Helvetica", 20))
mainlabel.grid(row=0, column=1, pady=(20, 20))
bottomlabel = Label(root, text="")  # Just hold the name of the menu selection
bottomlabel.grid(row=4, column=1)
returnlabel = Label(root, text="")  # Hold the content returned by called program
returnlabel.grid(row=5, column=1)
# --------------------------------------------------

# Function changes bottomlabel to show option selected, after button is clicked.
# Then,   Dropdown Menu labels == same name as the file.
# If that name is called we know which function to call.
def showSelection():
    bottomlabel.configure(text=clicked.get())
    if clicked.get() == "Ping":
        from Ping import ping  # Import file + function we need to call
        ping()  # Then call it. 
    else:
        return


# --------------------------------------------------
# List to hold the menu options.
# Menu option needs to == target file name + .py
# User selects option, then system just can copy name, and run ....py-file
menuoptions = ["Ping",
"Pingsweep",
"Portscan",
"...",
"...",
"...",
"..."]
# -----------------------------------------------------
# Dropdown box is same as an Option Menus
menulabel = Label(root, text="Drop Menu", font=("Helvetica", 16))
menulabel.grid(row=1, column=0)
clicked = StringVar()       # We can define as an IntVar also if we need
clicked.set(menuoptions[0]) # Dropdown will have all menu options, set default to first in list.
# Drop down menu tab
# Make sure to add the  *  to indicate ALL of the list.
drop = OptionMenu(root, clicked, *menuoptions)
drop.grid(row=1, column=1, padx=20, pady=(20,20), ipadx=100)
# -------------------------------------------------------------------------------
# Button calls function, to change the label to the current dropdown selection.
myButton = Button(root, text="Show Selection", command=showSelection, background="orange")
myButton.grid(row=2, column=1)
# ==================
# ==================
root.mainloop()
# ==================
# ==================
