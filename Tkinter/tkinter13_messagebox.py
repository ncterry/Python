"""
This shows how to pop a message box, and then what to do based on the Buttons
    that pop up with certain popup boxes. There are 6 primary types of pop up boxes.
    We have all 6 below, but only 1 (askyesno) is active. 

# python3 tkinter13_messagebox.py
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
#
root = Tk()
root.title("The Title Text")
#
# Several types of popup boxes:
#   showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popupfunc():

    # response = messagebox.showinfo("This is my showinfo Popup!", "Hello World")
    # response = messagebox.showwarning("This is my showwarning Popup!", "Hello World")
    # response = messagebox.showerror("This is my showerror Popup!", "Hello World")
    # response = messagebox.askquestion("This is my askquestion Popup!", "Hello World")
    # response = messagebox.askokcancel("This is my askokcancel Popup!", "Hello World")
    #
    # Different popup box buttons return different things, but usually just a 1 or 0
    response = messagebox.askyesno("This is my askyesno Popup!", "Hello World")
    Label(root, text=response).pack()    # print numerical value to window, yes returns 1,   no returns 0
    if response == 1:
        Label(root, text="You clicked Yes").pack()
    elif response == 0:
        Label(root, text="You clicked No").pack()

# Message box is just a simple pop up box with yes/no etc.
Button(root, text="Click Me", command=popupfunc, padx=100, pady=100).pack()

# ==================
root.mainloop()
