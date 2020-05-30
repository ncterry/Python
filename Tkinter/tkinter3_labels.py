
"""
https://www.youtube.com/watch?v=YXPyB4XeYLA
Tkinter Course - Create Graphic User Interfaces in Python Tutorial

Python comes built in with tkinter
Everything is a widget in tkinter

    # python3 tkinter3_labels.py
"""
from tkinter import *
# ---------------------
root = Tk()     # State the root widget. This is tied to everything
# Create Labels
myLabel1 = Label(root, text="Hello World")          # We created labels
myLabel2 = Label(root, text="My name is Nate.")
myLabel3 = Label(root, text="                ")     # empty space columns. Inefficient, but effective.
# ----------------------------
# Place labels
#myLabel1.pack()  # Pack = shoving it in the window anywhere. Cant use pack + grid together
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=5)  # grid = place it somewhere. pack & grid do not work together.
                     # NOTE window will auto indent myLabel2 in col2 if nothing in 2,3,4
                     # There are better ways to space labels etc, but we will show those later.
myLabel3.grid(row=1, column=2)  # myLabel3 is spacing on column, between myLabel1 and myLabel2
# --------------------------------------------------------------------
# We can combine the label creation and placement:
myLabel4 = Label(root, text="combo placement").grid(row=4, column=1)
# --------------
root.mainloop()     # The loop that will keep the window running indefinitely.
                    # we have a small window with a simple label .
