"""
Using python to analyze data with matplotlib
Charts

>>> python3 thkinter28_matplotlib.py

"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np  # pip3 install numpy
import matplotlib.pyplot as plt  # pip3 install matplotlib

#
root = Tk()
root.title("Matplotlib Charts")
root.geometry("400x400")
#
def graph():
    # We can import data from csv or excel, but we are just creating it here.
    #       (avg house price,   standard deviation,   #of plot points)
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)  #histogram of house prices, seperated into 50 bins
    plt.show()
# ----------------------------
mybutton = Button(root,text="Show Graph", command=graph)
mybutton.pack()

# ==================
root.mainloop()
