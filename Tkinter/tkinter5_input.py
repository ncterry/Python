"""
https://www.youtube.com/watch?v=YXPyB4XeYLA
Tkinter Course - Create Graphic User Interfaces in Python Tutorial

This is for user input, using the base code from tkinter4_buttons.py
"""
# -----------------------------
from tkinter import *
# -----------------------------
root = Tk()
# -----------------------------
# Initializes a simple user input box on the window.
    # Make input box wider, w/yellow back, &black text, &wide border.
userentry = Entry(root, width=50, bg="yellow", fg="black", borderwidth=10)
userentry.pack()
userentry.insert(0, "My Name is:  ")    # Place instructions in input box.
                                            # But it will be included w/input.get()
#userentry.get()   # Capture the input. We will use this in the function
# -----------------------------
# This function = action for when a button is clicked.
def myClick():
    hellovar = "Hello " + userentry.get()  # string + user input
    myLabel2 = Label(root, text=hellovar)  # Simple label on window
    myLabel2.pack()
# -----------------------------
myButton1 = Button(root, text="Enter Your Name. Then Click", command=myClick)
myButton1.pack()
# -----------------------------
root.mainloop()     # The loop that will keep the window running indefinitely.
