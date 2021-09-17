from LIVE_News import News
from weather_update import weather
import speech_recognition as sr
import pyttsx3
from tkinter import *
import datetime as dt
import os
import time
import webbrowser
import pywhatkit
import pyjokes
import wikipedia
import psutil
import pyautogui

root = Tk()
root.geometry('700x700+400+85')
root.title("ECHO : AI Voice Assistant")

global var
global var2

var = StringVar()
var2 = StringVar()

# IMPORTANT FUNCTIONS
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        root.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            var.set("Recognizing...")
            root.update()
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
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

    Speak("I am Echo...how may I help you sir!?")

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
            
            elif open_app == "Excel":
                Speak("Opening Microsoft Excel")
                os.system("start excel")
                time.sleep(5)

            elif open_app == "Notepad":
                Speak("Opening Notepad")
                os.system("start notepad")
                time.sleep(5)

            # linkdin

            elif open_app == "leetcode":
                Speak("Opening leetcode")
                webbrowser.open("https://leetcode.com")
                time.sleep(5)
            
            elif open_app == "GitHub":
                Speak("Opening GitHub")
                webbrowser.open("https://github.com")
                time.sleep(5)

            elif open_app == "Facebook":
                Speak("Opening Facebook")
                webbrowser.open("www.facebook.com")
                time.sleep(5)

            elif open_app == "Instagram":
                Speak("Opening Instagram")
                webbrowser.open("www.instagram.com")
                time.sleep(5)

            elif open_app == "Twitter":
                Speak("Opening Twitter")
                webbrowser.open("www.twitter.com/")
                time.sleep(5)

        # Advance Features
        elif "tell me a joke" in command:
            Speak(pyjokes.get_joke())

        elif "search Google for " in command:
            go_search = command.replace('search Google for ', '')
            Speak('searching ' + go_search)
            pywhatkit.search(go_search)
            time.sleep(5)

        elif "search YouTube for " in command:
            yt_search = command.replace("search Youtube for ", "")
            Speak('playing ')
            pywhatkit.playonyt(yt_search)
            time.sleep(5)

        elif "who is " in command:
            wiki_search = command.replace("who is ", "")
            info = wikipedia.summary(wiki_search, sentences=2)
            Speak("According to Wikipedia")
            print(info)
            root.update()
            Speak(info)
            time.sleep(5)

        elif "live news" in command:
            root.update()
            News()
        
        elif "weather in" in command:
            city_name = command.replace("weather in ", '')
            weather(city_name)

        elif "CPU and battery percentage" in command:
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

        elif "switch window" in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "goodbye" in command:
            Speak("Thank you...have a nice day sir!")
            break

        else:
            Speak("Pardon me, please repeat that again sir!")



def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)
# END OF FUNCTIONS

# GUI 
label2 = Label(root, textvariable = var2, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var2.set('User Said:')
label2.pack()

label1 = Label(root, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='img/Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]

label = Label(root, width = 500, height = 500)
label.pack()
root.after(0, update, 0)

btn = Button(text = 'Run Assistant',width = 20, command = TaskExecution, bg = '#5C85FB')
btn.config(font=("Courier", 16))
btn.pack()

btn1 = Button(text = 'Exit Window',width = 20,command = root.destroy, bg = '#5C85FB')
btn1.config(font=("Courier", 16))
btn1.pack()

root.mainloop()