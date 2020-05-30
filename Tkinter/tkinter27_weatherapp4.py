"""
Build a weather app.
This is the built from   tkinter27_weatherapp3.py

This is gathering the same weather data for Denver, but the primary
    changes will be so that the window colors will correspond with the
    air quality. For example; if we have good quality the color are green.
    Bad quality air, the colors will be red...etc
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
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80231&distance=5&API_KEY=E04FECF3-DD5A-44E9-A883-23D5E1E08A6A")
    api = json.loads(api_request.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
    category = api[0]['Category']['Name']
    """
    Note: We are formatting BG colors to match exactly what is on the website guidelines.
    We are on the website and it shows the varying levels, Good, USG, Hazardous,...etc.
    In Firefox, on the website image that shows a color, such as the AQI colors
    If I right click on the image just showing the color "Green"
            --> The you can click on several things like, "Selection Source", or "Inspect Element"
    And you can find the color hex-values and many other things.
    """
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
    root.configure(background=weather_color)
    my_label1 = Label(root, text=city + "\nAir Quality: " + str(quality) + "\n" + category, font=("Helvetica", 40), background=weather_color)
    my_label1.pack()
# --------------------
except Exception as e:
    api = "Error....."
# ----------------------------------------------------

"""
                     Denver-Boulder
                    Air Quality: 42
                        Good
"""
root.mainloop()
