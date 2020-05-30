"""
This is creating radio buttons, but is creating them from a tuple loop
    radio buttons with pizza toppings for a pizza store.

    # python3 tkinter12_radiobuttons2.py
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("Create Radio Buttons")
#
def clicked(value):     # When reg-button clicked, places current radiobutton:topping on label.
    pizzaLabel = Label(root, text=value)
    pizzaLabel.pack()
#
# [ ("Text user sees"), ("Value given when button is clicked.") ]
# [ ("Type"),            ("Value") ]
TOPPINGS = [
    ("Pepperoni",   "PepperoniX"),
    ("Cheese",      "CheeseX"),
    ("Mushroom",    "MushroomX"),
    ("Onion",       "OnionX")]
#
# var to assign a value, then send this var to the label.
pizza = StringVar()
pizza.set("Default Cheese")  # Set default topping. Will be the opening window label.
#
# current radiobutton value -set to-> pizza-var,  then click reg-button   -set to->   Label
pizzaLabel = Label(root, text=pizza.get())
pizzaLabel.pack()
#
# type is the topping text displayed next to radio buttons
# topping is the text-value that is assigned when selected.
#       We added an X on those just to show the difference in the window.
# For-loop to create a radio button for each type in the TOPPINGS tuple.
# anchor=W   Set button text to the left of the window.
for type, topping in TOPPINGS:
    Radiobutton(root, text=type, variable=pizza, value=topping).pack(anchor=W)
#
# You select the radio button, and that assigns the value to the variable.
# That value does not get placed on the Window label, until you click the reg-button.
myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
# ==================
root.mainloop()
