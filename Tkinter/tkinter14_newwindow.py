"""
The entry text for a window.

>>> python3 tkinter14_newwindow.py
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("The Main Window")
#
# Create new window, remember to declaure that name in your statements. (root vs secondwindow )
secondwindow = Toplevel()   # Create 2nd window as a Toplevel(), NOT another Tk() like root window.
secondwindow.title("The Second Window")
toplabel = Label(secondwindow, text="2nd window label").pack()
myimg = ImageTk.PhotoImage(Image.open("/root/Desktop/tkinterimages/image2.jpg"))
myimglable = Label(secondwindow, image=myimg).pack()


# ==================
root.mainloop()
