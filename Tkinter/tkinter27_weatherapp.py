"""
Build a weather app.
Some basic data, and url on:    "tkinter27_gathereddata.txt"

Using python and API to connect and scrape info on local zipcode
    Working with:   www.airnow.gov
            Tab:    "Maps & Data": "Developers/API"
            Click the "Login Page" link.
            Either login, or "Request an AirNow API Account"
            Nathan Terry, tracksta6, ncharlesterry, @2L Airnow
    Now Login:
        Tab:    "Web Services"
        Link:   "Current Observations By Reporting Area": "By Zip code":
            There is a documentation link that shows what type of data we get.
            2nd Line:   "Query Tool"    --> Use this
                Selections/Inputs:
                    1a) Zipcode:    80231
                    1b) Distance:   5 miles
                    1c) Format:     application/json

                    2) Click "Build" and you will get a "Generated URL"
                    http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80231&distance=5&API_KEY=E04FECF3-DD5A-44E9-A883-23D5E1E08A6A

            Note - you would need an API key for this, but as you can see in the URL, since we were
                logged in to airnow.gov when we generated this URL, the API-Key is included.


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
try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80231&distance=5&API_KEY=E04FECF3-DD5A-44E9-A883-23D5E1E08A6A")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error....."
# ----------------------------------------------------
my_label1 = Label(root, text=api)
my_label1.pack()  # Base format will be text much wider than our window. FYI
"""
API's will return data in different ways, dictionaries, lists, etc.
We need to know what we are getting, so we can format our window.
We notice a list, with 3 inner dictionaries...

Example Output:
[{"DateObserved":"2020-05-29 ","HourObserved":19,"LocalTimeZone":"MST","ReportingArea":"Denver-Boulder","StateCode":"CO",
"Latitude":39.768,"Longitude":-104.873,"ParameterName":"O3","AQI":42,"Category":{"Number":1,"Name":"Good"}},
{"DateObserved":"2020-05-29 ","HourObserved":19,"LocalTimeZone":"MST","ReportingArea":"Denver-Boulder","StateCode":"CO",
"Latitude":39.768,"Longitude":-104.873,"ParameterName":"PM2.5","AQI":30,"Category":{"Number":1,"Name":"Good"}},
{"DateObserved":"2020-05-29 ","HourObserved":19,"LocalTimeZone":"MST","ReportingArea":"Denver-Boulder","StateCode":"CO",
"Latitude":39.768,"Longitude":-104.873,"ParameterName":"PM10","AQI":49,"Category":{"Number":1,"Name":"Good"}}]

So we know there are 3 dictionary objects, in the list, so [0, 1, 2]
Use another label, but just grab the first dictionary

{"DateObserved":"2020-05-29 ","HourObserved":19,"LocalTimeZone":"MST","ReportingArea":"Denver-Boulder","StateCode":"CO",
"Latitude":39.768,"Longitude":-104.873,"ParameterName":"O3","AQI":49,"Category":{"Number":1,"Name":"Good"}}
"""
# It is Still wider than our root window, but we cut it down to just the first object.
my_label2 = Label(root, text=api[0])
my_label2.pack()
"""
Above, you can see that the first dictionary that we grabbed, api[0], actually has
    sub-dictionaries also. So we can further isolate subs.
Below we will just grab the area name, and the Air Quality Index number.
"""
# Still wider than our root window, but we cut it down to just the first object.
my_label3 = Label(root, text=api[0]["ReportingArea"] + " AQI:" + str(api[0]["AQI"]))
my_label3.pack()
""" Now our third label now just shows:     'Denver-Boulder AQI:42'
        We can isolate and expand as much as we want.
There is even a sub-sub-dictionary at the end for the quality, name.

........","AQI":42,"Category":{"Number":1,"Name":"Good"}},"
Let's get that....
"""
my_label4 = Label(root, text=api[0]["Category"]["Name"]) # "Good"
my_label4.pack()


# ==================
root.mainloop()
