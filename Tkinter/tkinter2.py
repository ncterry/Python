
"""
https://www.youtube.com/watch?v=YXPyB4XeYLA
Tkinter Course - Create Graphic User Interfaces in Python Tutorial

Python comes built in with tkinter
Everything is a widget in tkinter

"""


from tkinter import *

root = Tk()     # The root widget. Tied to everything
myLabel = Label(root, text="Hello World")   # We created it, now place in a window.
myLabel.pack()      # Packing is shoving in the window, wherever space is available.
root.mainloop()     # The loop that will keep the window running indefinitely.
                    # From here, we have a small window with a simple label in the top left corner of the screen.
