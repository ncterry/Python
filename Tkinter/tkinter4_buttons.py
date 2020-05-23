"""
https://www.youtube.com/watch?v=YXPyB4XeYLA
Tkinter Course - Create Graphic User Interfaces in Python Tutorial

This is for buttons. Full explanations for labels, and grid spacing is on tkinter3_labels.
"""
from tkinter import *
# -----------------------------
root = Tk()     # State the root widget. This is tied to everything
# -----------------------------
# This function = action for when a button is clicked.
def myClick():
    myLabel2 = Label(root, text="Look I clicked on the button.")  # Simple label on window
    #myLabel2.grid(row=4, column=3)
    myLabel2.pack()
    # If you click the button several times, with grid, since the message is
    #       in the same place, then nothing changes. If you use pack() then
    #       the same message will repeat, and another gets copied on the window.
# -----------------------------
    # Create button
    # Button text does not appear when run on Macbook, just an OS issue???.
    # Button text DOES appear when running from Linux
#myButton1 = Button(root, text="Click Me", state=DISABLED)  # ---DISABLED -> ignore/blank-out button.
#myButton1 = Button(root, text="Click Me")                  # ---Basic button
#myButton1 = Button(root, text="Click Me", fg="red", bg="blue", padx=50, pady=20) # ---Adjust size, color
#myButton1 = Button(root, text="Click Me", command=myClick, bg="blue") # ---Add command-funtion + background color.
myButton1 = Button(root, text="Click Me", command=myClick) # ---Just command. function should not have () following.
# -----------------------------
# Place the button
#myButton.pack()  # We have label already using pack. Cant use grid + pack
myButton1.pack()
# -----------------------------
root.mainloop()     # The loop that will keep the window running indefinitely.
