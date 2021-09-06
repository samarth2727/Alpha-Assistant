import pyttsx3   
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
from tkinter import *
import random

engine = pyttsx3.init('sapi5')                 #'sapi5'microsoft speech API
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[0].id)        #set voice from your windows
 
window = Tk()

def speak(audio):                               # speak function
    engine.say(audio)                           # python -m speech_recognition
    engine.runAndWait()

def wishme():                                   #function to wish a person and intoduce itself.
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=12:
        speak("good morning")
    
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    
    else:
        speak('good evening')
    speak("I am Alpha, how may i help you.")

def takecommand():   
    r = sr.Recognizer()                            # takes micrphone inpurt from user and string output;
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


#def sendEmail(to,content)

def play():

    btn1.configure(bg = 'skyblue')
    wishme()
    while True :
        btn1.configure(bg= 'skyblue')
        query = takecommand().lower()

        if 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "wikipedia" in query:
    
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences="2")
            speak("Acording to wikipedia.")
            speak(results)
         
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            speak('Here are your favorites')
            music_dir = 'F:\Samarth projects\python projects\Alpha Assistant\music'  # Enter the Path of Music Library
            songs = os.listdir(music_dir)
            n = random.randint(0,4)
            os.startfile(os.path.join(music_dir, songs[n]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(" the time is %s" %strtime)
               
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'thank you' in query:
            speak('your welcome.')

        elif "why you came to world" in query:
            speak("Thanks to samarth and rahul. further It's a secret")

window.geometry("400x400")
window.minsize(300,200)

window.title("Alpha Assistant")

label1 = Label(text="Alpha Assistant \n your personal assistant",bg="skyblue", padx=400,pady=15, font="bold",borderwidth=5,relief=SUNKEN)
label1.pack()

photo=PhotoImage(file="alpha.png")
pic=Label(image=photo)
pic.pack()

frame=Frame(window ,borderwidth=4,bg="black")
frame.pack(side=BOTTOM, pady=50)


btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.place(x = 50, y = 80)
btn1.config(font=("Courier", 12))
btn1.pack()

window.mainloop()

        

