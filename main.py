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
import psutil
import pyautogui

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
            print("user : ' ", Query, " ' ")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query

def Speak(audio):
    engine = pyttsx3.init('sapi5')
    engine.getProperty('voices')
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def cur_time():
    t = dt.datetime.now().strftime('%I:%M %p')
    Speak("The time is " + t)

def date():
    year = int(dt.datetime.now().year)
    month = int(dt.datetime.now().month)
    date = int(dt.datetime.now().day)
    Speak("Today's date is ")
    Speak(date)
    Speak(month)
    Speak(year)

def cpu():
    usage = str(psutil.cpu_percent())
    Speak("CPU is at "+ usage)

    battery = psutil.sensors_battery()
    Speak("Battery is at"+ str(battery.percent)+ "%")
    
def wishme():
    Speak("Welcome back sir!")
    cur_time()
    hour = dt.datetime.now().hour
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

def TaskExecution():
    wishme()

    while True:
        command = take_commands()

        # Basic Tasks
        if "introduce yourself" in command:
            introduction()

        elif "date" in command:
             date()
        
        elif "time" in command:
            cur_time()
        
        # Opening Tasks
        elif "open" in command:
            open_app = command.replace('open ', '')

            if open_app == "Word":
                Speak("Opening Microsoft Word")
                os.system("start winword")
                time.sleep(5)
            
            elif open_app == "PowerPoint":
                Speak("Opening Microsoft Powerpoint")
                os.system("start powerpnt")
                time.sleep(5)
            
            elif open_app == "Excel":
                Speak("Opening Microsoft Excel")
                os.system("start excel")
                time.sleep(5)

            elif open_app == "Notepad":
                Speak("Opening Notepad")
                os.system("start notepad")
                time.sleep(5)

            elif open_app == "Facebook":
                Speak("sir, please enter the user name manually")
                name = input("Enter username here : ")
                webbrowser.open(f"www.facebook.com/{name}")
                Speak(f"sir here is the profile of the user {name}")
                time.sleep(5)

            elif open_app == "Instagram":
                Speak("sir, please enter the user name manually")
                name = input("Enter username here : ")
                webbrowser.open(f"www.instagram.com/{name}")
                Speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
            
            elif open_app == "Twitter":
                Speak("Opening Twitter")
                webbrowser.open("www.twitter.com/")
                time.sleep(5)
            
            elif open_app == "GitHub":
                Speak("sir, please enter the user name manually")
                name = input("Enter username here : ")
                webbrowser.open(f"https://github.com/{name}")
                Speak(f"sir here is the profile of the user {name}")
                time.sleep(5)

        # Advance Features
        elif "tell me a joke" in command:
            Speak(pyjokes.get_joke())

        elif "search Google for" in command:
            go_search = command.replace('search Google for', '')
            Speak('searching ' + go_search)
            pywhatkit.search(go_search)
            time.sleep(5)

        elif "search Youtube for" in command:
            yt_search = command.replace('search Youtube for', '')
            Speak('playing ' + yt_search)
            pywhatkit.playonyt(yt_search)
            time.sleep(5)

        elif "search Wikipedia for" in command:
            wiki_search = command.replace('search Wikipedia for', '')
            info = wikipedia.summary(wiki_search, 2)
            Speak("According to Wikipedia")
            print(info)
            Speak(info)
            time.sleep(5)

        elif "what's in the news" in command:
            News()
        
        elif "what's the weather in" in command:
            city_name = command.replace("what's the weather in ", '')
            weather(city_name)

        elif "show me the CPU and battery percentage" in command:
            cpu()

        elif "remember that" in command:
            data = command.replace("remember that", '')
            remember = open("To-Dolist.txt","w")
            remember.write(data)
            Speak("Certainly Sir! The reminder has been added to your to-do list..")
            remember.close()

        elif "check my to do list" in command:
            filesize = os.path.getsize("To-Dolist.txt")
            if filesize==0:
                Speak("Sir!, there are no reminders")
            else:
                remember = open("To-Dolist.txt","r")
                Speak("Checking To-Do list...")
                Speak(remember.readlines())

        elif "switch the window" in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "take screenshot" in command or "take a screenshot" in command:
            Speak("sir, please tell me the name for this screenshot file")
            name = command().lower()
            Speak("please hold the screen for few seconds, i am taking the screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            Speak("I am done sir, the screenshot is saved in our main folder")

        elif "goodbye" in command:
            Speak("Thank you...have a nice day sir!")
            break

        else:
            Speak(command)
            Speak("Pardon me, please repeat that again sir!")


# END OF FUNCTIONS

if __name__ == '__main__':

    TaskExecution()