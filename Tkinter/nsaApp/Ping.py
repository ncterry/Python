# --------------------------------------------------
# Function Call:        try1.ping("8.8.8.8")
#
import platform     # For getting the operating system name
import subprocess   # For executing a shell command.
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
#
"""
Returns True (1) if host (str) responds to a ping request.
The Host may not respond to a ping (ICMP) request even if host name is valid.
"""
def runping():
    host = entrybox.get()
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Building the command.
    # >>> ping -c 1 google.com
    command = ['ping', param, '1', host]
    #return subprocess.call(command) == 0
    if subprocess.call(command) == 0:
        returnlabel.configure(text=f'True: Ping on {host} Successful.')
    else:
        returnlabel.configure(text=f'False: Ping on {host} UnSuccessful.')


def ping():  # host = ip
    # Create new window, remember to declaure that name in your statements. (root vs secondwindow )
    pingwindow = Toplevel()   # Create 2nd window as a Toplevel(), NOT another Tk() like root window.
    pingwindow.title("The Ping Window")  # Top window title
    toplabel = Label(pingwindow, text="Ping a Host")  # Simple label for window.
    toplabel.grid(row=0, column=1)
    #
    global entrybox  # global entrybox so runping() can get() from it.
    entrybox = Entry(pingwindow, width=50, bg="yellow", fg="black", borderwidth=10)
    entrybox.grid(row=2, column=1)
    #
    entryBoxlabel = Label(pingwindow, text="Enter Target IPv4", padx=20)
    entryBoxlabel.grid(row=2, column=0)
    #
    entryBoxbutton = Button(pingwindow, text="Run Ping", command=runping)
    entryBoxbutton.grid(row=3, column=1)
    # Global label to hold results of runping function()
    global returnlabel
    returnlabel = Label(pingwindow, text="")
    returnlabel.grid(row=4, column=1)

# ---------------------------------------------------------------------------
# -----Simple Example--------------------------------------------------------
#print(ping("8.8.8.8"))
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
