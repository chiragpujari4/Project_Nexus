import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
from time import sleep
import os
import cmd
import cv2
import wikipedia
import pywhatkit
import webbrowser
import pyautogui
import json
import requests

engine=pyttsx3.init('sapi5') #Initiating python engine.
voices=engine.getProperty('voices') #Getting voices from the engine.
engine.setProperty('voices',voices[0].id) #setting a particular voice for the model.

def speak(audio): #Function to speak.
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand(): #Function to take commands from the user.
    r=sr.Recognizer() #Speech Recognition module's recognizer.
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=4 # To pause it for listening.
        audio=r.listen(source,phrase_time_limit=5) #To listen the command.

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using Google's speech recognition model.
        print(f"user said: {query}") #To print what user said.
        speak(query)

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# Additional Functionalities -

def wish(): #Wish function
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning")
    elif(hour>12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Nexus, What can I help you with")


if __name__=="__main__":
    #speak("this is nexus")
    #takecommand()
    wish()
    if 1:
        query=takecommand().lower() #Taking input from the user.
        # Tasks -
        
        if "open notepad" in query: #Open notepad.
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd")            
            
        #Online Tasks -
        
        if "google" in query:
            import wikipedia as googleScrap            
            speak("This is what I found on google")

            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,1)
                speak(result)

            except:
                speak("No speakable output available")
                
        if "youtube" in query:
            speak("This is what I found for your search!") 
            web  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done, Sir")


        if "wikipedia" in query:
            speak("Searching from wikipedia....")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia..")
            print(results)
            speak(results)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
            
        elif "open" in query:
            dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
    
            speak("Launching, sir")
            if ".com" in query or ".co.in" in query or ".org" in query:
                webbrowser.open(f"https://www.{query}")
            else:
                keys = list(dictapp.keys())
                for app in keys:
                    if app in query:
                        os.system(f"start {dictapp[app]}")

        elif "close" in query:
            dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
            
            
            speak("Closing,sir")
            if "one tab" in query or "1 tab" in query:
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")
            elif "2 tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")
            elif "3 tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")
        
            elif "4 tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")
            elif "5 tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("All tabs closed")

            else:
                keys = list(dictapp.keys())
                for app in keys:
                    if app in query:
                         os.system(f"taskkill /f /im {dictapp[app]}.exe")
                         
            

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jarvis","")
            speak("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())
            
            
        elif "news" in query:
            api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=eb2e71808169420a943698aeca17ed45",
                "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=eb2e71808169420a943698aeca17ed45",
                "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=eb2e71808169420a943698aeca17ed45",
                "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=eb2e71808169420a943698aeca17ed45",
                "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=eb2e71808169420a943698aeca17ed45",
                "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=eb2e71808169420a943698aeca17ed45"
            }

            content = None
            url = None
            speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
            field = input("Type field news that you want: ")
            for key ,value in api_dict.items():
                if key.lower() in field.lower():
                    url = value
                    print(url)
                    print("url was found")
                    break
                else:
                    url = True
            if url is True:
                print("url not found")

            news = requests.get(url).text
            news = json.loads(news)
            speak("Here is the first news.")

            arts = news["articles"]
            for articles in arts :
                article = articles["title"]
                print(article)
                speak(article)
                news_url = articles["url"]
                print(f"for more info visit: {news_url}")

                a = input("[press 1 to cont] and [press 2 to stop]")
                if str(a) == "1":
                    pass
                elif str(a) == "2":
                    break
        
            speak("thats all")


        
        