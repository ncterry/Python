"""
This is a simple calculator, just basic functions for mathing numbers together.
There is much to add and improve, this is just for a straightforward example
    on how to create a window with buttons, functions, inputs, all tied together.

        # python3 tkinter6_simpleCalculator.py
"""

# -----------------------------
from tkinter import *
# -----------------------------
root = Tk()
root.title("Simple Calculator")
# -----------------------------
# This is for aesthetics. This is to show the full number that you want in the entry box
# If we dont save and recycle numbers, 108 will appear as   110110108 because the box was not cleared.
def button_click(newnumber):        # EX. str(108), save 1, then get 0=(10), then get 8=(108)
    currentNum = userentry.get()    # Save what WAS in there. Ex. currentNum=10
    userentry.delete(0, END)        # Now remove 10 from visual input box.
    userentry.insert(0, str(currentNum + str(newnumber)))
    # str(1) + str(0) = str(10) + str(8) = str(108)
# -----------------------------
def button_clear():
    userentry.delete(0, END)  # Remove text from entry box, when clear button clicked.
# -----------------------------
def button_equal():  # global math var tells equal which action was just pressed + - * /
    second_number = userentry.get()
    userentry.delete(0, second_number)
    if math == "addition":
        userentry.insert(0, f_num + int(second_number))
    if math == "subtraction":
        userentry.insert(0, f_num - int(second_number))
    if math == "multiplication":
        userentry.insert(0, f_num * int(second_number))
    if math == "division":
        userentry.insert(0, f_num / int(second_number))
# -----------------------------
# Currently cant do:    num+num+num+num=   you need num+num= +num= +num=
def button_add():  # Simple Calculator - 1+2=3 +4=7 +3=10 ...need to press num+num= then + again, num, then = again.
    first_number = userentry.get()  # The last number in the entry box.
    global f_num                    # Make global, so we can use in the equal function.
    global math
    math = "addition"               # So that button_equal, knows the + button was pressed.
    f_num = int(first_number)       # Sent in string, make sure convert to int so we can add.
    userentry.delete(0, END)        # Clear first number from entry box after + is pressed
# -----------------------------
def button_subtract():
    first_number = userentry.get()  # The last number in the entry box.
    global f_num                    # Make global, so we can use in the equal function.
    global math
    math = "subtraction"            # So that button_equal, knows the - button was pressed.
    f_num = int(first_number)       # Sent in string, make sure convert to int so we can add.
    userentry.delete(0, END)        # Clear first number from entry box after + is pressed
    # -----------------------------
def button_multiply():
    first_number = userentry.get()  # The last number in the entry box.
    global f_num                    # Make global, so we can use in the equal function.
    global math
    math = "multiplication"         # So that button_equal, knows the * button was pressed.
    f_num = int(first_number)       # Sent in string, make sure convert to int so we can add.
    userentry.delete(0, END)        # Clear first number from entry box after + is pressed
    # -----------------------------
def button_divide():
    first_number = userentry.get()  # The last number in the entry box.
    global f_num                    # Make global, so we can use in the equal function.
    global math
    math = "division"               # So that button_equal, knows the / button was pressed.
    f_num = int(first_number)       # Sent in string, make sure convert to int so we can add.
    userentry.delete(0, END)        # Clear first number from entry box after + is pressed
    # -----------------------------
# Visual entry box. Technically not needed, but lets user see what they are doing.
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
 # Dont need lambda. Not sending a value below, we are committing an action.
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=42, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

#
# Place buttons
# Location is just personal preference.
# columnspan uses is to make sure the space is filled even with 1 button.
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
#
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
# -----------------------------
root.mainloop()     # The loop that will keep the window running indefinitely.
