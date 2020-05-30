"""
use the file dialog box to open files.
We have a root window with just a button.
We click on the button and it opens a 2nd window to select targeted files.
We select a file in that 2nd window. Click Open
That returns the address of the file (image here)
The address is opened as a photo, and set as an image label on the root window.

We also have a label in the root window of that image address as well.
>>> python3 tkinter16_file.py
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog  # New
#
root = Tk()
root.title("The Title Text")
#

#
# We can do any files, but we are just working with images here.
# Image folder:   /root/Desktop/tkinterimages/
#       1) Set directory with files in it.
#       2) Set new window Title
#       3) State which types of files we are looking for, and will appear in the window.
#           --> anthing with .jpg,
#           --> anything with .png,
#           --> and just any single file type.
def openfile():
    global my_image
    root.filename =  filedialog.askopenfilename(initialdir="/root/Desktop/tkinterimages/",
                                                title="Select A File",
                                                filetypes=(("png files", "*.png"),
                                                            ("jpg files", "*.jpg"),
                                                            ("All files", "*.*")))
    my_label = Label(root, text=root.filename).pack()           # Grab address of file we select in second window. Set address as label.
    my_image = ImageTk.PhotoImage(Image.open(root.filename))    # Open address of image as an Image, not a label.
    my_image_label = Label(image=my_image).pack()               # Pack opened image on root window.
#
# Button on root window to find and open a file.
my_button = Button(root, text="Open File", command=openfile, padx=20, pady=30).pack()
# ==================
root.mainloop()
