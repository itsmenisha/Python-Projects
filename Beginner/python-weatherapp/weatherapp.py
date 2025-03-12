from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Get API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")


# Create root window
root = Tk()
root.title("Weather App: Just Trust Howl")
root.geometry("900x500+200+100")
root.resizable(False, False)


def getWeather():
    la.destroy()
    la1.destroy()  # This deletes the label from the window
    la2.destroy()  # This deletes the label from the window

    global path
    city = text.get()

    geolocator = Nominatim(user_agent="Agent location")
    location = geolocator.geocode(city)

    if location is None:
        raise ValueError("City not found.")

    # Get timezone using latitude and longitude
    tf = TimezoneFinder()
    time_zone = tf.timezone_at(lng=location.longitude, lat=location.latitude)

    if time_zone is None:
        raise ValueError("Timezone could not be determined.")

    # Get current time in the specified timezone
    home = pytz.timezone(time_zone)
    date_today = datetime.now(home)
    current_time = date_today.strftime("%I:%M %p")

    clock.place(x=40, y=140)
    time_name.place(x=40, y=110)

    clock.config(text=current_time)  # Updating the clock label
    time_name.config(text="Current Weather")

    api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={API_KEY}"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    # Change background image

    if temp <= 0:  # Freezing temperatures
        path12 = path5

    elif 1 <= temp <= 10:  # Cold weather
        path12 = path4

    elif 11 <= temp <= 20:  # Cool weather
        path12 = path3

    elif 21 <= temp <= 30:  # Warm weather
        path12 = path7

    elif 31 <= temp <= 40:  # Hot weather
        path12 = path2

    else:  # Extremely hot weather
        path12 = path6

    bg_image = Image.open(path12)
    bg_resized = bg_image.resize((900, 500))  # Resize to match window size
    bg_photo = ImageTk.PhotoImage(bg_resized)
    bg_label.config(image=bg_photo)
    bg_label.image = bg_photo

    t.place(x=585, y=125)
    t.config(text=(temp, "°"))

    e.place(x=585, y=240)
    e.config(text=(condition, "|", "YOU", "ARE", temp, "°", "HOT"), bg="black")

    a.config(text=(wind))
    b.config(text=(humidity))
    c.config(text=(description))
    d.config(text=(pressure))


# Load and resize the background image
path1 = "a1.png"
path2 = "b2.png"
path3 = "c3.png"
path4 = "d4.png"
path5 = "e5.png"
path6 = "f6.png"
path7 = "g7.png"

path12 = path1
path = 1


def resource_path(relative_path):
    import sys
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller extracts files here
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


bg_image = Image.open(resource_path(path12))

bg_resized = bg_image.resize((900, 500))  # Resize to match window size
bg_photo = ImageTk.PhotoImage(bg_resized)

bg_label = Label(root, image=bg_photo)  # Fix here with 'Label'
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep a reference to prevent garbage collection
bg_label.image = bg_photo

# Search bar
text = Entry(root, justify="center", width=18, font=(
    "Albertus", 17), border=0, fg="white", bg="black")
text.place(x=55, y=45)
text.focus()

image = Image.open("searchicon.png")
image_resized = image.resize((50, 50))  # Resize the image
# Convert to PhotoImage for tkinter
Search_icon = ImageTk.PhotoImage(image_resized)
my_image = Button(image=Search_icon, borderwidth=0, cursor="hand2",
                  bg="#9c9a9d", border=0, command=getWeather)  # Fix here with 'Button'
my_image.place(x=310, y=40)

# Time display
time_name = Label(root, font=("Albertus", 14), border=0, bg="#fafafa")
time_name.place(x=0, y=110)

clock = Label(root, font=("Albertus", 14), border=0, bg="#fafafa")
clock.place(x=0, y=140)

la = Label(root, text="Weather App", font=(
    "Albertus", 14), border=0, fg="black", bg="#fafafa")
la.place(x=60, y=180)
la1 = Label(root, text="Inspired By", font=(
    "Albertus", 14), border=0, fg="black", bg="#fafafa")
la1.place(x=140, y=230)
la2 = Label(root, text="Howl's moving castle‍💕💗", font=(
    "Albertus", 14), border=0, fg="black", bg="#fafafa")
la2.place(x=190, y=280)

# Weather Report Labels
label1 = Label(root, text="WIND", font=("Albertus", 14),
               border=0, fg="white", bg="#9c9a9d")
label1.place(x=120, y=380)

label2 = Label(root, text="HUMIDITY", font=("Albertus", 14),
               border=0, fg="white", bg="#9c9a9d")
label2.place(x=250, y=380)

label3 = Label(root, text="DESCRIPTION", font=(
    "Albertus", 14), border=0, fg="white", bg="#9c9a9d")
label3.place(x=460, y=380)

label4 = Label(root, text="PRESSURE", font=("Albertus", 14),
               border=0, fg="white", bg="#9c9a9d")
label4.place(x=700, y=380)

# Placeholder labels for values
t = Label(root, text="", font=("Albertus", 60),
          border=0, fg="#961a04", bg="#e8e8e8")
t.place(x=582, y=125)
e = Label(root, text="", font=("Albertus", 15),
          border=0, fg="white", bg="#e8e8e8")
e.place(x=582, y=240)

a = Label(root, text="💜🧡🖤", font=("Albertus", 14),
          border=0, fg="white", bg="#9c9a9d")
a.place(x=120, y=410)

b = Label(root, text="💚🤎💛", font=("Albertus", 14),
          border=0, fg="white", bg="#9c9a9d")
b.place(x=250, y=410)

c = Label(root, text="💜🧡🖤", font=("Albertus", 14),
          border=0, fg="white", bg="#9c9a9d")
c.place(x=460, y=410)

d = Label(root, text="💚🤎💛", font=("Albertus", 14),
          border=0, fg="white", bg="#9c9a9d")
d.place(x=700, y=410)

root.mainloop()
