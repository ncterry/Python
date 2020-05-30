"""
Create drop down menus
This is the same as tkinter21_dropdownMenu.py

But we are accounting for if we have a HUGE list to put in the menu.
The first file we just added in the days manually, but here
    we tie the drop down menu options to a pre-defined list.
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("Drop Down Menus")
root.geometry("400x400")

# Function changed label to which option was selected, after button is clicked.
def showSelection():
    mylabel = Label(root, text=clicked.get()).pack()
#
# List to hold the menu options. Still 7 days, but good if you have a huge list.
menuoptions = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Dropdown box is same as an Option Menus
clicked = StringVar()   # We can define as an IntVar also
clicked.set(menuoptions[0]) # Dropdown will have all 7 days, set default to first in list.
# Make sure to add the  *  to indicate ALL of the list.
drop = OptionMenu(root, clicked, *menuoptions)
drop.pack()

# Button calls function, to change the label to the current dropdown selection.
myButton = Button(root, text="Show Selection", command=showSelection).pack()

# ==================
root.mainloop()
