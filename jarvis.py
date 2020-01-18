import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
import time
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour==12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening")
    speak(" I am Jarvis sir . Please tell me how may i help you")
    
def takeCommand():
    #It takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("can you repeat sir")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('','')
    server.sendmail('',to,content)
    server.close()
if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing task based on query
        
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak(" According to wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open github' in query:
            webbrowser.open("https://github.com/niladribit69")
          
        elif 'play music' in query:
            music_dir=''
            songs=os.listdir(music_dir)
            #print(songs)
            n=len(songs)
            ran=random.randint(-1, n-1)
            os.startfile(os.path.join(music_dir,songs[ran]))
            
        elif 'open gallery' in query:
            gallery_dir=''
            gallery=os.listdir(gallery_dir)
            n=len(gallery)
            ran=random.randint(-1, n-1)
            os.startfile(os.path.join(gallery_dir,gallery[ran]))
            
        elif 'play movie' in query:
            movie_dir=''
            movie=os.listdir(movie_dir)
            n=len(movie)
            speak("playing movie")
            os.startfile(os.path.join(movie_dir,movie[n-1]))
            
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif "what\'s up" in query or "how are you" in query:
            stmsg=['Just doing my thing!','Iam fine!','Nice!']
            speak(random.choice(stmsg))
            
        elif 'message' in query:
            try:
                url = "https://www.fast2sms.com/dev/bulk"
                speak("say message")
                message=takeCommand()
                speak("enter contact")
                number=takeCommand()
                speak("message loaded")
                fin=''
                for i in number:
                    if i.isdigit():
                        fin=fin+i
                payload = 'sender_id=FSTSMS&message='+message+'&language=english&route=p&numbers='+fin
                headers = {
                'authorization': "",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                speak("message sent successfully")
            except Exception as e:
                print(e)
                speak("sorry not able to send")
            
        elif 'email' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                speak("enter roll no")
                roll=takeCommand()
              
                fin=''
                for i in roll:
                    if i.isdigit():
                        fin=fin+i
                
                to=fin+"@kiit.ac.in"
                to=str(to)
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry not able to send")
                
        elif 'copy it' in query:
            try:
                speak("what you want to copy")
                text1=takeCommand()
            
                speak("searching wikipedia...")
                results=wikipedia.summary(text1,sentences=2)
                speak(" According to wikipedia ")
                print(results)
                speak(results)
            
            #with open('file.txt', 'w') as file:
                #file.write(results)
                f = open("", "w", encoding='utf-8')
                f.writelines(results)
                speak("pasted the wikipedia results ")
                f.close()
            except Exception as e:
                print(e)
                speak("sorry not able to find results")
                
        elif 'translate' in query:
            try:
                speak("say what you want to translate")
                text=takeCommand()
                from textblob import TextBlob
                word=TextBlob(text)
                a=word.translate(to='hi')
                mytext=str(a)
                from gtts import gTTS
                language='hi'
                output=gTTS(text=mytext,lang=language,slow=False)
                output.save("output.mp3")
                os.system("start output.mp3")
            except Exception as e:
                print(e)
                speak("unable to understand")
                
        elif 'say about me' in query:
            try:
                f = open("", "r",encoding='utf-8')
                about_me=(f.read())
                speak(about_me)
                f.close()
            except Exception as e:
                print(e)
                speak("Unable")
                
        elif 'who are you' in query:
            try:
                f = open("", "r",encoding='utf-8')
                about_me=(f.read())
                speak(about_me)
                f.close()
            except Exception as e:
                print(e)
                speak("Unable")
                
        elif 'weather' in query:
            try:
                speak("say location sir")
                loc=takeCommand()
                print(loc)
                url=''+loc
                from bs4 import BeautifulSoup
                from urllib.request import urlopen


                page=urlopen(url)
                soup=BeautifulSoup(page,'lxml')
                fetched_text=' '.join(map(lambda p:p.text,  soup.find_all('p')))
                string1=''
                for i in fetched_text:
                    if(i=='C'):
                        break
                    else:
                        string1=string1+i
                from gtts import gTTS
                language='en'
                output=gTTS(text=string1,lang=language,slow=False)
                output.save("output.mp3")
                os.system("start output.mp3") 
            except Exception as e:
                print(e)
                speak("NOT ABLE TO RECOGNIZE")
                
        elif 'direction' in query:
            try:
                speak("say starting location please")
                loc1=takeCommand()
                speak("say destination")
                loc2=takeCommand()
                url2=''
                import webbrowser
                speak("google maps opening")
                webbrowser.open(url2)
            except Exception as e:
                print(e)
                speak("NOT ABLE TO RECOGNIZE")     
        
        elif 'alarm' in query:
            speak("you cant continue untill alarm is off")
            speak("enter hour")
            alarm_HH = takeCommand()
            speak("enter min")
            alarm_MM = takeCommand()

            print("You want to wake up at " + alarm_HH + ":" + alarm_MM)

            while True:
                    now = time.localtime()
                    if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
            
                        music_dir=''
                        songs=os.listdir(music_dir)
            #print(song)
                        n=len(songs)
                        ran=random.randint(-1, n-1)
                        os.startfile(os.path.join(music_dir,songs[ran]))
                        speak("success")
                        break
       
        elif 'quit' in query:
            speak("see  you  soon  sir ")
            music_dir=''
            songs2=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs2[0]))
            sys.exit()
            
        else:
            query=query
            speak('Searching...')
            try:
                results=wikipedia.summary(query,sentences=2)
                speak(" According to wikipedia ")
                print(results)
                speak(results)
            except:
                print("please type sir")
