"""
The entry text for a window.
This pops up a main window with a button.
Click the button, and it creates a new window with an image label.

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
def openNewWindow():

    # Need to make myimg global so the button can use it also.
    global myimg
    # Create new window, remember to declaure that name in your statements. (root vs secondwindow )
    secondwindow = Toplevel()   # Create 2nd window as a Toplevel(), NOT another Tk() like root window.
    secondwindow.title("The Second Window")
    toplabel = Label(secondwindow, text="2nd window label").pack()
    myimg = ImageTk.PhotoImage(Image.open("/root/Desktop/tkinterimages/image2.jpg"))
    myimglable = Label(secondwindow, image=myimg).pack()
    # Add button to the second window to close this window.
    closewindow = Button(secondwindow, text="Close Window", command=secondwindow.destroy).pack()

# Button starts on root window.
# Click button to open up the secondwindow with the image.
newwindowButton = Button(root, text="Open Second Window", command=openNewWindow, padx=50, pady=20).pack()


# ==================
root.mainloop()
