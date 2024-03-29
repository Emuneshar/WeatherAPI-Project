import requests

apiKeys = "54fa0149f32598b8de4cf172383a469b"

city = input("Please enter the name of a city: \n")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKeys}'

def convertToF(kelvin):
    return round((kelvin-273.15)*1.8 +32)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    for key in data:
        print(key, ":", data[key])
    temp = convertToF(temp)
    desc = data['weather'][0]['description']
    feelsLike = data['main']['feels_like']

    # This is how we get the high temp for the day
    highTemp = data['main']['temp_max']
    highTemp = convertToF(highTemp)

    # homework is to get, convert and print out the low temp for the day

    feelsLike = convertToF(feelsLike)
    print(f'Temperature: {temp} F')
    print(f'Description: {desc} ')
    print(f'Feels like : {feelsLike}F')
    print(f'High temp for today: {highTemp}F')
else:
    print("Sorry there was an error getting the weather data")


