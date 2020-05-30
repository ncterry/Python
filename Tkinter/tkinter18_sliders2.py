"""On a window we can have sliders up/down, and left right on a window."""
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
# Move horizonal slider from 0-200 pixels
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()
# ---------------------------------------------------------------------------
# Label displays how far horizontal slider moved, if you click the button.
my_label = Label(root, text=horizontal.get()).pack()

def slideWindowAdjust():
    # Move horizonal slider to position 134
    # Changes root window label to 134
    # Adjust window size to 134 pix also.
    # Window size gets value we moved the horizonal slider, and keeps vertical at 400
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")
    #
# Move horizontal slider to position 83
# Click button, the the label will display "83" to show how far you moved.
#my_button = Button(root, text="Click Me", command=slide).pack()
my_button2 = Button(root, text="Click Me", command=slideWindowAdjust).pack()
# ---------------------------------------------------------------------------
# ==================
root.mainloop()
