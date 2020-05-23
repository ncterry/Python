"""
This is a simple calculator, just to add numbers together
"""

# -----------------------------
from tkinter import *
# -----------------------------
root = Tk()
root.title("Simple Calculator")
# -----------------------------
def button_click(newnumber):        # EX. str(108), get 1, get 0=(1+0), get 8=(10+8)
    currentNum = userentry.get()    # Save what WAS in there. Ex. currentNum=10
    userentry.delete(0, END)        # Now remove 10 from visual input box.
    userentry.insert(0, str(currentNum + str(newnumber))) # Combine str(10) + str(8) = str(108)
# -----------------------------
userentry = Entry(root, width=35, borderwidth=5)
userentry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# -----------------------------
# Create buttons
# Normal button->"button_click"---"Lambda: button_click()""->lets us pass in a param
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_click())
button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: button_click())
button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_click())

#
# Place buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
#
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
#
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
#
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)  # Button fits 2 columns
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)  # Button fits 2 columns
# -----------------------------
# -----------------------------
root.mainloop()     # The loop that will keep the window running indefinitely.
