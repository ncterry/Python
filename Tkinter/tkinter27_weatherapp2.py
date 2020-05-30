"""
Build a weather app. This is the built from   tkinter27_weatherapp.py
We are just cleaning up our API return to 3 specific items.
"""
# PIL=Pillow. Terminal: pip3 install Pillow
# Needed:   sudo apt-get install python3-pil.imagetk
from tkinter import *
from PIL import Image, ImageTk
import requests     # pip3 install requests
import json
# ----------------------------------------------------
root = Tk()
root.title("Weather App")
root.geometry("400x400")
# ----------------------------------------------------
# try/except in case the return data throws an error.
# Try to get the information from our url
# Then try to parse it into a json/python usable format.....or else, error.
"""
{"DateObserved":"2020-05-29 ","HourObserved":19,"LocalTimeZone":"MST","ReportingArea":"Denver-Boulder","StateCode":"CO",
"Latitude":39.768,"Longitude":-104.873,"ParameterName":"O3","AQI":42,"Category":{"Number":1,"Name":"Good"}},
"""
try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80231&distance=5&API_KEY=E04FECF3-DD5A-44E9-A883-23D5E1E08A6A")
    api = json.loads(api_request.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error....."
# ----------------------------------------------------
my_label1 = Label(root, text=city + " Air Quality: " + str(quality) + "\n" + category)
my_label1.pack()
"""                 Denver-Boulder Air Quality: 42
                                Good
"""
root.mainloop()
