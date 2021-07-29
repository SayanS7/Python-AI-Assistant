import requests
from win32com.client import Dispatch

def weather(city_name):
    api_key="8ef61edcf1c576d65d836254e11ea420"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    speak = Dispatch("SAPI.Spvoice")
    x=response.json()
    
    if x["cod"]!="404":
        y=x["main"]
        
        current_temperature_K = y["temp"]
        current_temperature_C = current_temperature_K - 273.15
        current_temperature = round(current_temperature_C, 2)
        
        current_humidiy = y["humidity"]
        
        z = x["weather"]
        
        weather_description = z[0]["description"]
        
        print(" Temperature : " + str(current_temperature) + 
            "\n humidity : " + str(current_humidiy) +"%"+
            "\n description : " + str(weather_description))

        speak.Speak(" Temperature is " + str(current_temperature) +
           "\n humidity is " + str(current_humidiy) +"%"+
           "\n description  " + str(weather_description))
        
        
    
    else:
        speak.Speak("City Not Found")