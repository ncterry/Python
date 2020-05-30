"""
On a window we can have sliders up/down, and left right on a window.
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("The Title Text")
root.geometry("400x400")

# Create a vertical slider.
# We named it vertical, but did not define it as vertical. Default is vertical.
# Strange aspect, "from_"  needs the underscore. No clue why....
vertical = Scale(root, from_=0, to=200)
vertical.pack()
#
# Move horizonal slider from 0-200 pixels, need to set orient here.
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()
# ---------------------------------------------------------------------------
# Label displays how far horizontal slider moved, if you click the button.
my_label = Label(root, text=horizontal.get()).pack()

def slide():  # Fuction says number of how far you moved the slider 0-200, on label
    my_label = Label(root, text=horizontal.get()).pack()
    #
# Move horizontal slider to position 83
# Click button, the the label will display "83" to show how far you moved.
my_button = Button(root, text="Click Me", command=slide).pack()
# ---------------------------------------------------------------------------
# ==================
root.mainloop()
