import requests

api_key = "0178f64ae43499c6bf276800f68aa579"

user_input = input("Enter City: ")
weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
#print(weather_data.status_code) #displays 200 -> request successful
#print(weather_data.json()) #prints all info about HYDERABAD fetched from openweather.api
if weather_data.json()['cod']=='404':
    print("No Such City Found!")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    print(f"The weather in {user_input} is {weather}")
    print(f"The temperature in {user_input} is {temp}°C")