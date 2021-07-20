from re import search
from LIVE_News import News
from weather_update import weather
import speech_recognition as sr
import pyttsx3
import datetime as dt
import os
import time
import webbrowser
import pywhatkit
import pyjokes
import wikipedia

# IMPORTANT FUNCTIONS
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
        try:
            print("Recognization")
            Query = r.recognize_google(audio, language='en-in')
            if 'Jarvis' in Query:
                Query = Query.replace('Jarvis','')
            print("the query is printed=' ", Query, " ' ")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def Speak(audio):
    engine = pyttsx3.init()
    engine.getProperty('voices')
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def cur_time():
    t = dt.datetime.now().strftime('%I:%M %p')
    Speak("its " + t)

def date():
    year = int(dt.datetime.now().year)
    month = int(dt.datetime.now().month)
    date = int(dt.datetime.now().day)
    Speak("Today's date is ")
    Speak(date)
    Speak(month)
    Speak(year)
    
def wishme():
    Speak("Welcome back sir!")
    hour = dt.datetime.now().hour
    cur_time()

    if hour >= 6 and hour < 12:
        Speak("Good Morning...")
    
    elif hour >= 12 and hour < 17:
        Speak("Good Afternoon...")
    
    elif hour >=17 and hour <= 24:
        Speak("Good Evening...")
    
    else:
        Speak("Good Night...")
    
    Speak("I am Jarvis...how may I help you sir!?")

def introduction():
    desc_file = open("description.txt",'r')
    for desc in desc_file.readlines():
        Speak(desc)

# END OF FUNCTIONS

if __name__ == '__main__':
    
    wishme()

    while True:
        print("Actions Performed----> Commands")
        print("\nFOR EXIT----> Exit\n"
        "Introduction-----> Introduce yourself\n"
        "Current Date-----> what's today's date\n"
        "Jokes--------> tell me a joke\n"
        "Google Search-----> Search Google for {topic}\n"
        "Wikipedia---------> Search Wikipedia for {topic}\n"
        "Live News From BBC------> what's in the news\n"
        "Temperaure of any city---->what's the temperature in{city}\n"
        "Youtube--------> play {title}\n"
        "Facebook--------> open Facebook\n"
        "Instagram--------> open Instagram\n"
        "Twitter--------> open Twitter\n"
        "GitHub---------> open GitHub"
        "MS-WORD--------> open Word\n"
        "MS-POWERPOINT--------> open PowerPoint\n"
        "MS-EXCEL--------> open Excel\n"
        "GOOGLE CHROME------> open Chrome\n"
        "NOTEPAD--------> open Notepad")

        time.sleep(5)
        command = take_commands()

        if "introduce yourself" in command:
            introduction()

        elif "what's today's date" in command:
             date()

        elif "tell me a joke" in command:
            Speak(pyjokes.get_joke())

        elif "search Google for" in command:
            go_search = command.replace('search Google for', '')
            Speak('searching ' + go_search)
            pywhatkit.search(go_search)
            break

        elif "play" in command:
            song = command.replace('play', '')
            Speak('playing ' + song)
            pywhatkit.playonyt(song)
            break

        elif "search Wikipedia for" in command:
            wiki_search = command.replace('search Wikipedia for', '')
            info = wikipedia.summary(wiki_search, 2)
            print(info)
            Speak(info)
            break

        elif "what's in the news" in command:
            News()
        
        elif "what's the temperature in" in command:
            search = command.replace("what's the ", '')
            weather(search)

        elif "open Word" in command:
            Speak("Opening Microsoft Word")
            os.system("start winword")

        elif "open PowerPoint" in command:
            Speak("Opening Microsoft Powerpoint")
            os.system("start powerpnt")

        elif "open Excel" in command:
            Speak("Opening Microsoft Excel")
            os.system("start excel")

        elif "open Chrome" in command:
            Speak("Opening Google Chrome")
            os.system("start chrome")

        elif "open Notepad" in command:
            Speak("Opening Notepad")
            os.system("start notepad")

        elif "open Facebook" in command:
            Speak("Opening Facebook")
            webbrowser.open("www.facebook.com")

        elif "open Instagram" in command:
            Speak("Opening Instagram")
            webbrowser.open("www.instagram.com")

        elif "open Twitter" in command:
            Speak("Opening Twitter")
            webbrowser.open("www.twitter.com/home")

        elif "open GitHub" in command:
            Speak("Opening GitHub")
            webbrowser.open("https://github.com/SayanS7")

        elif "exit" in command:
            Speak("exiting...")
            Speak("Thank you...have a nice day sir!")
            break

        else:
            Speak(command)
            print("Input is not Valid,Please Try Again")
            Speak("Can you please repeat Sir!")
