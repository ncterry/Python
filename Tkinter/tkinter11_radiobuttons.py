"""
Radio buttons can be used as a standard button would, but can also act as
    as selection. You can select a radio button next to the number 2. The window
    may not do anything yet, but the program will save 2 for a next action. However,
    that selection may also act as a regular button and commit an action also.
    Simply depends on your code. The next tutorial:
            tkinter12_radiobuttons2.py   shows the simple selection aspect
    for radio buttions while this one changes the label also.
    
    # python3 tkinter_radiobuttons.py
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("Create Radio Buttons")
#
def clicked(value):     # When radio buttons clicked, places lambda value on label.
    myrLabel = Label(root, text=value)
    myrLabel.pack()
#
# Tkinter var for the radio Buttons
# r stays an int variable, but the r-value can change depending on the button.
r = IntVar()
#r.get()            # get the r value when the radio button is clicked
#r.set("111")       # set the value of r regardless of if button is clicked.
#s = StringVar()    # string variable

# Click on these, the r-value will be 1 or 2, send to function, to place value as label.
Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 3", variable=s, value="six").pack()
#
myrLabel = Label(root, text=r.get())   # Get the value from r-var and set as label value.
myrLabel.pack()
#
myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()
# ==================
root.mainloop()
