from tkinter import *
import requests

def get_city_info():
    city = cityField.get()

    url = "https://countriesnow.space/api/v0.1/countries/population/cities"

    try:
        result = requests.get(url)
        data = result.json()
    except:
        info["text"] = "Ошибка подключения"
        return

    if not data.get("data"):
        info["text"] = "Данные не найдены"
        return

    city_info = None
    for item in data["data"]:
        if item.get("city", "").lower() == city.lower():
            city_info = item
            break

    if city_info:
        city_name = city_info.get("city", "Неизвестно")
        country = city_info.get("country", "Неизвестно")

        population_data = city_info.get("populationCounts", [])
        if population_data:
            population = population_data[0].get("value", "Нет данных")
        else:
            population = "Нет данных"

        info["text"] = f"Факты о городе {city_name}:\n\n1. Страна: {country}\n2. Население: {population} чел."
    else:
        info["text"] = f"Город '{city}' не найден"


root = Tk()
root["bg"] = "#fafafa"
root.title("Факты о городе")
root.geometry("400x350")
root.resizable(width=False, height=False)

frame_top = Frame(root, bg="#ffb700", bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

cityField = Entry(frame_top, bg="white", font=30)
cityField.pack()

btn = Button(frame_top, text="Узнать факты", command=get_city_info)
btn.pack()

frame_bottom = Frame(root, bg="#ffb700", bd=5)
frame_bottom.place(relx=0.15, rely=0.45, relwidth=0.7, relheight=0.45)

info = Label(frame_bottom, text="Введите город", bg="#ffb700", font=20, justify=LEFT)
info.pack()

root.mainloop()