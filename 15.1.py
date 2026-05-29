from tkinter import *
import requests

def get_weather():
    city = cityField.get()

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city, "count": 1}

    geo_result = requests.get(geo_url, params=geo_params)
    geo_data = geo_result.json()

    if not geo_data.get("results"):
        info["text"] = "Город не найден"
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {"latitude": lat, "longitude": lon, "current_weather": "true"}

    weather_result = requests.get(weather_url, params=weather_params)
    weather_data = weather_result.json()

    temp = weather_data["current_weather"]["temperature"]
    info["text"] = f"{city}: {temp}°C"


root = Tk()
root["bg"] = "#fafafa"
root.title("Погодное приложение")
root.geometry("300x250")
root.resizable(width=False, height=False)

frame_top = Frame(root, bg="#ffb700", bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

cityField = Entry(frame_top, bg="white", font=30)
cityField.pack()

btn = Button(frame_top, text="Посмотреть погоду", command=get_weather)
btn.pack()

frame_bottom = Frame(root, bg="#ffb700", bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

info = Label(frame_bottom, text="Погода в городе", bg="#ffb700", font=40)
info.pack()

root.mainloop()