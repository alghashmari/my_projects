import requests
from datetime import datetime
MY_LAT = 21.406455
MY_LAG = 39.263143

parameters = {
    "lat": MY_LAT,
    "lng": MY_LAG,
    "formatted": 0,  # Use ISO 8601 format for time
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Extracting and cleaning the time portion
sunrise_time = sunrise.split("T")[1].split(":")
sunset_time = sunset.split("T")[1].split(":")

time_now = datetime.now()

print(f"Sunrise time is: {':'.join(sunrise_time[:2])}")
print(f"Sunset time is: {':'.join(sunset_time[:2])}")
print(time_now)
