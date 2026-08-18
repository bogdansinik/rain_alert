import requests
import os

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("API_KEY")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


LAT = os.environ.get("LAT")
LON = os.environ.get("LON")

print(LAT, LON)
CNT = 4
params = {"lat": LAT, "lon": LON, "appid": API_KEY, "cnt": CNT}
response = requests.get(OMW_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
weather_codes = []
will_rain = False
for hour_data in weather_data["list"]:
    code = int(hour_data["weather"][0]["id"])
    weather_codes.append(code)
    if code < 600:
        will_rain = True


# if will_rain:
if True:
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    parameters = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "It's going to rain today. Remember to bring an umbrella ☔️"
    }

    response = requests.post(url, data=parameters)
    response.raise_for_status()

    print("Notification sent successfully via Telegram!")

