import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
   
    speak("I am jadu Sir how may help you")       

def takecommand():
   

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('buntyrajputsingh11@gmail.com', 'bunty@123')
    server.sendmail('swapneshaero@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takecommand().lower()

        
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
    

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.bing.com/search?q={cm}")

        elif "open youtube" in query:
            speak("sir,what should i search on youtube")
            x = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            
        elif "open my team" in query:
            webbrowser.open("http://ieeerait.in/")
            
      
        elif "play music" in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "play video" in query:
            speak("ok i am playing videos")
            video_dir = 'D:\\video'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0])) 

        elif "play song on cloud" in query:
            speak("tell me the song name!")
            p = takecommand()
            webbrowser.open(f"https://soundcloud.com/search?q={p}")

    
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "open pdf" in query:
            codePath = "C:\\Users\\SWAPNESH\\AppData\\Local\\SumatraPDF\\SumatraPDF.exe"
            os.startfile(codePath)
            
        elif "open command prompt" in query:
            os.system("start cmd")


        elif "your name" in query:
            speak("Thanks for Asking my name, my self jadu")

      
            
            
        elif "send mail" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "swapneshaero@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        
       












