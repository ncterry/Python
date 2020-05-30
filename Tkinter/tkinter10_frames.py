"""
Simple adjustment to just place a frame (square black line) around the window.

    # python3 tkinter_10_frames.py
"""
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
root = Tk()
root.title("Work with frames on window")
#
# Create a frame in the window with padding from the window edge
# The frame will not show up until you have something else in the window.
# The vast majority of tkinter cant tolerate pack + grid
#       but a frame can pack, and other stuff (buttons here can combine with grid.)
# You don't need text in a frame
frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)
# Place this button in the window, so the frame has something to go around.
b = Button(frame, text="Don't Click Here.")
b2 = Button(frame, text="....Or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

# =====================
root.mainloop()
