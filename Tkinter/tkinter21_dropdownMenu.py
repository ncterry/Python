"""
Create drop down menus
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

# Dropdown box is same as an Option Menus
clicked = StringVar()   # We can define as an IntVar also
clicked.set("Mon")      # Dropdown will have all 7 days, but we default with Mon
drop = OptionMenu(root, clicked, "Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
drop.pack()

# Button calls function, to change the label to the current dropdown selection.
myButton = Button(root, text="Show Selection", command=showSelection).pack()

# ==================
root.mainloop()
