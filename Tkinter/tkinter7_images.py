"""

    # python3 tkinter7_images.py
"""
from tkinter import *
# Pillow to use other image files like JPG etc.....
from PIL import Image   # PIL=Pillow. Terminal: pip3 install Pillow
from PIL import ImageTk # Needed:   sudo apt-get install python3-pil.imagetk
#
root = Tk()
root.title("Learn to insert images in tkinter.")
#root.iconbitmap('c:/root/Desktop/tkinter7_imagesicon.ico')  # icon not working.
#
# 3 step process. This packs an image on the full window
my_img = ImageTk.PhotoImage(Image.open("/root/Desktop/tkinter7_imagesicon.png"))
my_label = Label(image=my_img)  # We opened the file, now place as a label.
my_label.pack() # pack the image-label into the Window.



# Simple button to quit/close the window.
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


# =====================
root.mainloop()
