import pyttsx3 
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os 
import pyautogui
import psutil
# pip install pyautogui(library using to take screenshot in system)
# pip install psutil

engine = pyttsx3.init()
engine.say("hello")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak("Welcome to Manyara")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    
    
    
    def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome to my system")
    speak("the current time is")
    time()
    speak("the current date is ")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and < 12:
        speak("Good moring sir!")
    elif hour >=12 and < 18:
        speak("Good Afternoon sir")
    elif hour >18 and hour < 24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")
    speak("Molshay at your service. Please tell me how can I help you? ")

wishme() (#you can remove this function and it will work)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizning....")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)
    
    
    except Exception as e:
        print(e)
        speak("Say that again Please...")
        
        return "None"
        
    return query
    
def sendEmail (to,content):
    server = smtplib.SMTP('smtp .gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail account',password here)
    server.sendmail('eamil account' to, content)
    server.close()
    
takeCommand()

def screenshot():
    img = pyautogui.screenshot()
    img.save()
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)
    battery = psutil.sensors_battery()
    speak('Batter is at')
    speak(battery.percent)



if _name_ == "_main_":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences =2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak('what should i say?')
                content = takeCommand()
                to = 'another account gmail'
                # sendEmail(to,content)
                speak(content)
                speak ('Email has been sent! ')
            except Exception as e:
                print(e)
                speak('uable to send the Email')
                
        elif 'search in chrome' in query:
            speak('what should I search ?')
            chromepath = 'copy your path of chrome exa(C:/Program File (x86)/Google....%s')
            search = takeCommand().lower()
            wb.get (chromepath).open_new_tab(search + '.com')
            
        elif 'logout' in query:
            os.system('shutdown -l')
        
        elif 'shutdown' in query:
            os.system('shutdown /s/t 1')
        
        elif 'logout' in query:
            os.system('shutdown /r /t 1')
            
        elif 'play songs' in query:
            songs_dir = "enter directory of your song file example D:\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif 'remember that' in query:
            speak('What should i remember?')
            data = takeCommand()
            speak('you said me to remember that' + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        # create the file in order for AI save
        
        elif 'do you know anything' in query:
            remember = open ('data.txt', 'r')
            speak('you said to me to remember tha' + remember.read())
            
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
            
        elif 'offline' in query:
            quit()
            
 

