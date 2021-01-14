import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()
def wishme():
   hour=int(datetime.datetime.now().hour)

   if hour>=0 and hour<12:
      speak("Good morning ")

   elif hour>12 and hour<=17:
      speak("Good afternoon ")
   else:
      speak("Good evening ")
   speak("I am Gaurav mishra  sir. pelase tell me how can i help you")


def takecomand():

   r=sr.Recognizer()
   with sr.Microphone() as source:
      print("Linsting......")
      r.energy_threshold = 600 # minimum audio energy to consider for recording
      r.dynamic_energy_threshold = True
      r.dynamic_energy_adjustment_damping = 1
      r.dynamic_energy_ratio = 2
      r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
      r.operation_timeout = None

      audio=r.listen(source)

   try:
      print("Recognization.....")
      query=r.recognize_google(audio, language='en-in')
      print("user said :",query)
   
   except Exception as e:
      print(e)
      print(" please say that again......")
      return "None"
   return query

def emailSend(to,content):
   server=smtplib.SMTP('smpt.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.login('g4gaurav892001@gmail.com', '9955995957 ')
   server.sendmail('g4gaurav892001@gmail.com', to, content)
   server.close()


if __name__ == '__main__':

    wishme()

    while True:
      query=takecomand().lower()
      if 'wikipedia' in query:
         speak("serachingung....")
         query=query.replace("wikipedia", "")
         result=wikipedia.summary(query,sentences=2)
         speak("According to wikipifia....")
         print(result)
         speak(result)
      elif 'open youtube' in query:
         webbrowser.open("https://www.youtube.com/?gl=IN")
         speak("According to you....")
      elif 'open google' in query:

         webbrowser.open("google.com")

      elif 'open stack overflow' in query:

         webbrowser.open("stakoverflow.com")
      elif 'open facebook' in query:

         webbrowser.open("facebook.com")
      elif 'open amazone' in query:

         webbrowser.open("amazone.com")
      elif 'open email' in query:

         webbrowser.open("email.com")

      elif 'play music' in query:

         music_dir="C:\\Users\\acer\\Documents\\movies\\all song"
         song=os.listdir(music_dir)
         os.startfile(os.path.join(music_dir, song[0]))

      elif 'play video' in query:
         vedio_dir="C:\\Users\\acer\\Documents\\movies\\all vidio"
         vedio=os.listdir(vedio_dir)
         os.startfile(os.path.join(vedio_dir, vedio[26]))   


      elif 'open code' in query:
         codepath="C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)
      
      elif 'the time' in query:
         start=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"ok sir i tell you , the time is {start}")
      elif 'email send to gaurav' in query:
         try:
            speak('what should i send ')
            content=takecomand()
            to=""
            emailSend(to, content)
            speak('email has beem sended')

         except Exception as  e:
            print(e)
            speak("sorry sir your email is not sended. please chack it")

            
         
      elif 'thank you' in query:

         speak("welcome sir i am for you . enjoy it")
         break




    
     