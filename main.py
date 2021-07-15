import speech_recognition as sr
import pyttsx3
import datetime as dt
import os
import time
import webbrowser
import pywhatkit
import pyjokes
import wikipedia


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognization")
            Query = r.recognize_google(audio, language='en-in')
            print("the query is printed=' ", Query, " ' ")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def Speak(audio):
    engine = pyttsx3.init()
    engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    # print("THESE ARE THE  APPLICATIONS YOU MAY OPEN.......")
    Speak("Hello Sir....how may I help you?")

    while True:
        print("Actions Performed----> Commands")
        print("\nFOR EXIT----> Exit\n"
              "Time--------> What is the time right now?\n"
              "Jokes--------> tell me a joke\n"
              "Google Search--------> Search {topic}\n"
              "Wikipedia--------> Who is {topic}\n"
              "Youtube--------> play {title}\n"
              "Facebook--------> open Facebook\n"
              "Instagram--------> open Instagram\n"
              "Twitter--------> open Twitter\n"
              "Amazon--------> open Amazon\n"
              "Flipkart--------> open Flipkart\n"
              "MS-WORD--------> open Word\n"
              "MS-POWERPOINT--------> open PowerPoint\n"
              "MS-EXCEL--------> open Excel\n"
              "GOOGLE CHROME --------> open Chrome\n"
              "NOTEPAD--------> open Notepad")

        time.sleep(7)
        command = take_commands()

        if "what is the time right now" in command:
            t = dt.datetime.now().strftime('%I:%M %p')
            print("\n{0}".format(t))
            Speak("Current time is " + t)

        elif "tell me a joke" in command:
            Speak(pyjokes.get_joke())

        elif "search" in command:
            go_search = command.replace('search', '')
            Speak('searching ' + go_search)
            pywhatkit.search(go_search)
            break

        elif "play" in command:
             song = command.replace('play', '')
             Speak('playing ' + song)
             pywhatkit.playonyt(song)
             break

        elif "who is" in command:
            wiki_search = command.replace('who is', '')
            info = wikipedia.summary(wiki_search, 2)
            print(info)
            Speak(info)
            break

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

        elif "open Amazon" in command:
            Speak("Opening Amazon")
            webbrowser.open("www.amazon.in")

        elif "open Flipkart" in command:
            Speak("Opening Flipkart")
            webbrowser.open("www.flipkart.com")

        elif "exit" in command:
            Speak("exiting...")
            Speak("Thank you...have a nice day...sir")
            break

        else:
            Speak(command)
            print("Input is not Valid,Please Try Again")
            Speak("Input is not Valid.....please try again")
