import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"  # replace with your API key
CITY = input("Enter City Name : ")
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    # print(data)
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Weather in {CITY}: {weather}, {temperature}°C")
else:
    print("Failed to get data:", response.status_code)
