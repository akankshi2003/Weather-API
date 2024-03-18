import requests
import pyttsx3

api_key = 'd31778f93f0ecac6e1e137b6d2135942'

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

engine = pyttsx3.init()
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp_fahrenheit = round(weather_data.json()['main']['temp'])
    temp_celecius = round((temp_fahrenheit - 32) * 5 / 9, 2)
    wind = weather_data.json()['wind']['speed']
    
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp_celecius}ºC")
    print(f"The wind speed in {user_input} is: {wind} meter/second")
    
    engine.say(f"The weather in {user_input} is: {weather}")
    engine.say(f"The temperature in {user_input} is: {temp_celecius} degrees celcius")
    engine.say(f"The wind speed in {user_input} is: {wind} meter per second")
    engine.runAndWait()