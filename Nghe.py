import pyaudio
import speech_recognition as sr

robotear=sr.Recognizer()
robotear.energy_threshold=4000

with sr.Microphone() as source:
   audio=robotear.listen(source)

try:
   print("You:" + robotear.recognize_google(audio))
except:
   print("Sorry, I can't hear you,try again")