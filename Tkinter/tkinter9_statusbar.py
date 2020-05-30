"""
Same as tkinter8_imageviewer.py
    But we have added a status bar and formatted it.
    Everything added has #NEW#  to the right

This is to open a window and then view a collection of images
# Folder with Images:   /root/Desktop/tkinter8/

    # python3 tkinter9_statusbar.py
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
# -------------------------------------------------------
def forward(image_number):
    # global vars that can transfer between forward/back functions
    global my_label
    global button_forward
    global button_back
    #
    my_label.grid_forget()  # window forgets previous photo
    my_label = Label(image=image_list[image_number]) # change to next photo in list
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))    # next photo
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))      # prev photo
    # Forward button should be disabled if we reach the last photo in the list.
    if image_number == 2:  # Disable button on last index of photo-list.
        button_forward = Button(root, text=">>", state=DISABLED) # reach last photo, can only use button_back
    # Buttons and label are always in the same place.
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)
    #NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
    # Update the status label after forward button pressed
    # + 1  so we compensate for which photo, vs position in list. 2nd photo is in list position 1
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #NEW#
    status.grid(row=2, column=0, columnspan=3, sticky=W+E) #NEW# sticky=W+# -> stretch across full window
    #NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
# -------------------------------------------------------
def back(image_number):
    global my_label
    global button_forward
    global button_back
    #
    my_label.grid_forget()  # window ignores placement on grid. forget last photo
    my_label = Label(image=image_list[image_number]) # change to next photo in list
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))    # next photo
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))      # prev photo
    # Back button should be disabled if we reach the first photo in the list.
    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED) # reach last photo, can only use button_back
    # Buttons and label are always in the same place.
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)
    #NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
    # Update the status label after back button pressed
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #NEW#
    status.grid(row=2, column=0, columnspan=3, sticky=W+E) #NEW# sticky=W+# -> stretch across full window
    #NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
# -------------------------------------------------------
root = Tk()                             # initialize root window
root.title("Build an Image Viewer")     # put a title at top or root window.
#root.geometry("500x500")
# -------------------------------------------------------
# State our 3 images.
my_img1 = ImageTk.PhotoImage(Image.open("/root/Desktop/tkinterimages/image1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("/root/Desktop/tkinterimages/image2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("/root/Desktop/tkinterimages/image2b.jpg"))
# Set images into a list
image_list = [my_img1, my_img2, my_img3]        # list of photos
#
#NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
#   [                     Image 1 0f 3]     bd=border,  Sunk into window, text on right side (E)
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #NEW#
#NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
#
# Place first image on window for when the program starts.
my_label = Label(image=image_list[0])           # First photo in list that pops up on window.
my_label.grid(row=0, column=0, columnspan=3)    # Have 3 buttons, so image spans all 3 columns
# -------------------------------------------------------
# First buttons created and placed on open of window.
button_back = Button(root, text="<<", state=DISABLED) # initial button, start on first photo, cant go back.
button_exit = Button(root, text="Exit Program", command=root.quit) # exit program
#       Window starts on image-0, this first button moves to image-1, then image is adjusted via functions.
button_forward = Button(root, text=">>", command=lambda: forward(1))
# -------------------------------------------------------
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10) #NEW - added pady=10 for spaceing between status
#NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
status.grid(row=2, column=0, columnspan=3, sticky=W+E) #NEW# sticky=W+# -> stretch across full window
#NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW##NEW#
# ================
root.mainloop()
