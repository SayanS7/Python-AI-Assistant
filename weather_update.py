from bs4 import BeautifulSoup
import requests
from win32com.client import Dispatch

def weather(search):
    speak = Dispatch("SAPI.Spvoice")
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak.Speak(f"{search} is {temp}")
