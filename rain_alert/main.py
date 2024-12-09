import requests


api_key = "9ff84a11959083085a0324392c20f2fe"
lat = "21.485811"
lon = "39.192505"

weather_request = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}")
weather_data = weather_request.json()
print(weather_data.keys())

forecast = weather_data["list"][0]
date_time = forecast["dt_txt"]
tem = forecast["main"]["temp"]
humidity = forecast["main"]["humidity"]
sea_level = forecast["main"].get("sea_level")

print(f"Date: {date_time}\n Temperature: {tem}\n Humidity: {humidity}\n Sea level: {sea_level}")