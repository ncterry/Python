# Current Py file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Security+_StudyApp.py
# =================
# Current txt file Directory address
# /Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/SecurityPlus_StudyFile.txt
# =================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# Imports Imports Imports Imports Imports Imports
# Program made with python 3.5.2
#       Pycharm Community Edition
# Runs with idle:
#       Run Module

from tkinter import *
# ==================================================
import tkinter as tk
from tkinter import ttk
# Using PIL for the pop up window on the StudyPage
from PIL import Image, ImageTk
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
XL_FONT  = ("Verdana", 30)  # Base font that we want to use and will call
LARGE_FONT = ("Verdana", 18)  # Base font that we want to use and will call
NORM_FONT = ("Verdana", 12)  # Base font that we want to use and will call
SMALL_FONT = ("Verdana", 10)  # Base font that we want to use and will call

# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# To get the popup window:
#       Run program: StartPage:  TradingPage:   Agree:  File:  Save Settings

def text_popupmsg(msg):
    # Create popup window, and set it's geometry
    '''
    Not used at the moment.
    '''
    popup = tk.Tk()
    popup.geometry("600x700")

    # Set the popup window title
    popup.wm_title("Title on top of File: Save Settings: popup")
    # Set a label in the popup window
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)



    image2 = Image.open("/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Party.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    label2 = Label(image=photo2)
    label2.image2 = photo2
    label2.pack()



    # Set a button in the popup window with a command to destroy popup window
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()
# ==================================================

# ==================================================
# ==================================================
# START PRIMARY TK CLASS      PRIMARY TK CLASS        PRIMARY TK CLASS
# ==================================================
class SecurityPlus(tk.Tk):
    '''
    Note: This is our primary page container format/configuration page for all pages.
        Set geometry, title, image(not working though)

        We have a menu that is not being used at the momemnt.

        We have a popup message coming from the menu selection, just for show at the moment.


     __init__ implies that this will be run automatically if the class is called.
         other def methods will not run automatically.
            args = arguments = open ended, you can pass whatever you want through
            kwargs = key-word arguments, basically dictionaries.
     '''
    def __init__(self, *args, **kwargs):
        # Now initialize tkinter also.
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self, "NCT's Security+ Study App")
        tk.Tk.geometry(self, "1000x1000")
        # Can't get the icon to show, now just a png icon
        # Resized to 12/16 pixels
        tk.Tk.iconbitmap(self, "icon.png")

        # =================
        container = ttk.Frame(self)
        # Making a quick window, use pack, for more detailed, use grid
        # side= What side do you want this on.
        # fill= Fill the entire space
        # expand= If there is any more white space in the window. Use it.
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Menubar block created in file 9
        # Create an overall menubar, and assign to this tkinter
        menuBar1 = tk.Menu(container)
        # Adding a tearoff divider into the menu that drops down
        fileMenu1 = tk.Menu(menuBar1, tearoff=0)
        # Now actually place a literal piece on the menubar
        menuBar1.add_cascade(label="File", menu=fileMenu1)
        # Create a subpiece under the File Tab
        # Currently Save Settings pulls up a popup
        # PopUp relies on method above, but doesn't do anything at the moment
        fileMenu1.add_command(label="Save Settings",
                              command=lambda: text_popupmsg("Msg sent from class SecurityPlus"))
        # Create a separator under the File Tab
        fileMenu1.add_separator()
        # ==================================================

        tk.Tk.config(self, menu=menuBar1)
        # ----------------------------------------------------
        # ==================================================
        # Specify a dictionary here
        self.frames = {}
        # We will have numerous windows, and either click/button will bring another.
        # One application with numerous windows.
        # ==================================================
        # ==================================================
        # ==================================================
        # ===================FOR PAGE LOOP===============================
        # For loop that ranges in our page limits
        # Make sure to add any new page to our tuple for loop
        for F in (StartPage,
                  ConfirmAddPage):
            # Use F so that we can progress through our pages.
            frame = F(container, self)
            self.frames[F] = frame
            # grid is more specific compared to pack.
            # sticky is using North/South/East/West -->
            #    will stretch to the size of the window.
            #       if you just use ew then it will stretch all to the sides.
            frame.grid(row=0, column=0, sticky="nsew")
        # ==================================================
        # ==================================================
        self.show_frame(StartPage)
    # ==================================================
    # ==================================================
    # Set function to show a frame for a specific page.
    def show_frame(self, controller1):
        # self.frames is looking at the frame dictionary that we created above.
        #       Controller is which frame we want to access
        frame = self.frames[controller1]
        # Then we will run a library function on the frame.
        frame.tkraise()
# ==================================================
# END PRIMARY TK CLASS      PRIMARY TK CLASS        PRIMARY TK CLASS
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# ==================================================
# ==================================================
class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=XL_FONT)
        label.pack(padx=10, pady=10)


        image1 = Image.open("/Users/Tracksta6/Dropbox/Computer Science/tkinter/Py3_SecurityPlus_StudyApp/Party.jpg")
        photo1 = ImageTk.PhotoImage(image1)
        label1 = Label(image=photo1)
        label1.image1 = photo1
        label1.pack()


        # ttk will give us a good looking button
        startPage_CloseButton = ttk.Button(self, text="Close Program",
                                           command=quit, width=15)
        startPage_CloseButton.pack(pady=(0,10))
# ==================================================
# ==================================================
# ==================================================
# ==================================================
class ConfirmAddPage(ttk.Frame):
    # Simple confirmation page
    # Lets user agree that they will be changing the file
    # If user agrees, it will take them to the change page

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="The Study File", font=XL_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        askButton = ttk.Label(self, text="""Do you want to add information to your txt file?
        \nChange at your own risk.""", font=NORM_FONT)
        askButton.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        returHomeButtonf = ttk.Button(self, text="Return to Home Page",
                             command=lambda: controller.show_frame(StartPage))
        returHomeButtonf.pack()

        # ----------------------------
        # This will auto-take you back to the start of the program
        addToStudyFilePage_disagreeButton = ttk.Button(self, text="DisAgree",
                                                command=lambda: controller.show_frame(StartPage))
        addToStudyFilePage_disagreeButton.pack()
        # ----------------------------
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================
#   MAIN    MAIN    MAIN    MAIN    MAIN    MAIN
# ==================================================
app = SecurityPlus()

app.mainloop()
# ==================================================
#   MAIN    MAIN    MAIN    MAIN    MAIN    MAIN
# ==================================================

