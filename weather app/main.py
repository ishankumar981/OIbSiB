import tkinter as tk
from tkinter import messagebox
import requests

# Your OpenWeatherMap API Key
API_KEY = "7bbc8f6707bc741a00307998089503ef"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)

        # Print response for debugging
        print("Status Code:", response.status_code)
        print("Response:", response.text)

        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            weather = data["weather"][0]["main"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            result.config(
                text=f"City: {city_name}, {country}\n\n"
                     f"Temperature: {temp} °C\n"
                     f"Feels Like: {feels_like} °C\n"
                     f"Weather: {weather}\n"
                     f"Description: {description.title()}\n"
                     f"Humidity: {humidity}%\n"
                     f"Pressure: {pressure} hPa\n"
                     f"Wind Speed: {wind_speed} m/s"
            )

        else:
            message = data.get("message", "Unknown Error")
            result.config(text=f"Error: {message}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", str(e))


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Weather App")
root.geometry("450x420")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Label(
    root,
    text="Enter City Name",
    font=("Arial", 12)
).pack()

city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack(pady=10)

tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
).pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    justify="left"
)
result.pack(pady=20)

root.mainloop()
