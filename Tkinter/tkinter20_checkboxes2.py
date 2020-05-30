"""
Checkboxes, are similar to radio buttons.
Square boxes that basically just relate to 0/1

This is nearly the same as   tkinter19_checkboxes.py
But here it to a string  (on/off) instead of 0/1

"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("tkinter19_checkboxes")
root.geometry("400x400")
#
#var = IntVar()  # var for value of checkbox we want to assign a 0 or 1
var = StringVar()
# Create and place the actual checkbutton, and tie it to the var
c = Checkbutton(root, text="Check this box!", variable=var, onvalue="On", offvalue="Off")
c.deselect()  # IntVar starts auto deslected, but StringVar starts auto selected. (bad)
c.pack()
#
# Function will update the label, when button is clicked
# Label will change to 0 if button is clicked when box is NOT checked.
# Lavel will change to 1 if button is clicked when the box IS checked.
def show():
    my_label = Label(root, text=var.get()).pack()
#
my_label = Label(root, text=var.get()).pack()
my_button = Button(root, text="Show Selection", command=show).pack()
# ==================
root.mainloop()
