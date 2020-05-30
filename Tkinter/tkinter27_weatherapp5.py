"""
Build a weather app.
This is the built from   tkinter27_weatherapp4.py

We took out notes from the last file, such as color notes.
This is a copy of tkinter27_weatherapp4.py, but now instead of hardcoding
    the zipcode for Denver in our API, we are inserting an Entry Box
    into our window, so that we can enter any zipcode and have our program
    go get the area-name, AQI number, and quality name.

Post Program success explanation.
We have a blank root window, with just an Entry box and button.
1) Enter the Zip code that you want info on.
2) Click the button.
                    -->  "90210" + Button
5/29/2020 at 10:51pm - Our root window turns all green with:

        NW Coastal LA
        Air Quality: 20
        Good

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
root.geometry("400x500")

# Create Zipcode lookup FUNCTION
def ziplookup():
    # ----------------------------------------------------
    # try/except in case the return data throws an error.
    # Try to get the information from our url
    # Then try to parse it into a json/python usable format.....or else, error.
    """
    Example of how the data is returned. Narrow that down....

    {"DateObserved":"2020-05-29 ","HourObserved":19,"LocalTimeZone":"MST","ReportingArea":"Denver-Boulder","StateCode":"CO",
    "Latitude":39.768,"Longitude":-104.873,"ParameterName":"O3","AQI":42,"Category":{"Number":1,"Name":"Good"}},
    """
    try:
        # Below is the original URL for Denver. Change that Zipcode to grab from entry box.
        #api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80231&distance=5&API_KEY=E04FECF3-DD5A-44E9-A883-23D5E1E08A6A")
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=E04FECF3-DD5A-44E9-A883-23D5E1E08A6A")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#8f3797"
        elif category == "Hazardous":
            weather_color = "#660000"

        # Text will still be black, but the everything else will be the corresponding color.
        # Potential issue - if label for 2nd searched city is smaller than the first,
        #       There may be label overlap. We have not cleared the prior label yet....
        root.configure(background=weather_color)
        my_label1 = Label(root, text=city + "\nAir Quality: " + str(quality) + "\n" + category, font=("Helvetica", 20), background=weather_color)
        my_label1.grid(row=1, column=0, columnspan=2)
    # --------------------
    except Exception as e:
        api = "Error....."
# -------------End ZipLookup Function-----------------
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# Entry box / button to enter zipcode for the API to search with.
# Sticky to make sure there is not a gap betwee box + button
zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)
#
zip_button = Button(root, text="Lookup Zipcode", command=ziplookup)
zip_button.grid(row=0, column=1)
# ----------------------------------------------------

root.mainloop()
