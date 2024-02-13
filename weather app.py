import requests

apiKeys = "54fa0149f32598b8de4cf172383a469b"

city = input("Please enter the name of a city")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKeys}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    for key in data:
        print(key, ":", data[key])
    temp = (temp - 273.15)*1.8 + 32
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} F')
    print(f'Description: {desc} ')
else:
    print("Sorry there was an error getting the weather data")


