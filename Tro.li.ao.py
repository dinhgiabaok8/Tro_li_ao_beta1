import pyaudio
import speech_recognition as sr
import pyttsx3
import dialogflow
from datetime import date
from datetime import datetime
from googlesearch import search
from gtts import gTTS
import os
robotear=sr.Recognizer()
robotmouth = pyttsx3.init()
robotbrain=""
#Chon ngon ngu:
#Ngon_ngu = input('Please chosse: \n1.Eng \n2.Vi \n  ')
Ngon_ngu='1'
if Ngon_ngu == '1':
	while True:
		#Xu li mang nghe
		robotear.energy_threshold=4000

		with sr.Microphone() as source:
		   audio=robotear.record(source, duration=3)
		try:
		   you = robotear.recognize_google(audio)
		except:
		   you=" "

		print("You:"+you)
		#Xu li AI
		if you == " ":
		        robotbrain="Sorry,I can't hear you,try again"
		elif "hello" in you:
		        robotbrain="Hi Bao"
		elif "my name" in you:
		        robotbrain="Your's name is Bao"
		elif "today" in you:
		         today = date.today()
		         robotbrain = today.strftime("%B %d, %Y")
		elif "time" in you:
		         now = datetime.now()
		         robotbrain = now.strftime("%H hour %M minutes %S seconds")
		elif "hi" in you:
			robotbrain="Whatzzup bro"
		elif "bye" in you:
			robotbrain="Bye Bao"
			print(robotbrain)
			robotmouth.say(robotbrain)
			robotmouth.runAndWait()
			print(robotbrain)
			break
			# how are you / okay/ok /who are you/funny story/sad story/
		elif "how are you" in you:
			robotbrain="I'm fine, Thanks"
		elif "okay" in you:
			robotbrain="Okay"
		elif "ok" in you:
			robotbrain="Okay"
		elif "who are you" in you:
			robotbrain="I'm an assistant-who can healp you solve problem"
		elif "funny story" in you:
		    robotbrain="Thinking no one could hear me as I loaded a UPS tractor trailer, I began to whistle. I was really getting into it when a coworker in the next trailer poked his head in. “You know, I always used to wish I could whistle,” he said. “Now I just wish you could.” —Megs Brunne"	
		elif "sad story" in you:
			robotbrain="I became an EMT to save people’s lives.Twenty minutes of CPR on my dad proved that was a lie."
		elif "story" in you:
			robotbrain="One of my wife’s third graders was wearing a Fitbit watch, which prompted my wife to ask, “Are you tracking your steps?” “No,” said the little girl. “I wear this for Mommy so she can show Daddy when he gets home.” —James Avery"
		elif "your name" in you:
			robotbrain="My name is Tele"
		elif "old are you" in you:
		    robotbrain="I don't remember, but I was born in 24,July 2020"
		else:
		    robotbrain=" "

		print('Tele:'+robotbrain)
		#Xu li mang noi
		robotmouth.say(robotbrain)
		robotmouth.runAndWait()
elif Ngon_ngu == '2':
	while True:
			#Xu li mang nghe
			robotear.energy_threshold=4000

			with sr.Microphone() as source:
			   audio=robotear.record(source, duration=3)
			try:
			   you = robotear.recognize_google(audio, language='vi-VN')
			except:
			   you=" "

			print("You:"+you)
			#Xu li AI
			if you == " ":
			        robotbrain="Tôi không nghe thấy gì, hãy thử lại"
			elif "hello" in you:
			        robotbrain="Hi Bao"
			elif "my name" in you:
			        robotbrain="Your's name is Bao"
			elif "today" in you:
			         today = date.today()
			         robotbrain = today.strftime("%B %d, %Y")
			elif "time" in you:
			         now = datetime.now()
			         robotbrain = now.strftime("%H hour %M minutes %S seconds")
			elif "hi" in you:
				robotbrain="Whatzzup bro"
			elif "bye" in you:
				robotbrain="Bye Bao"
				print(robotbrain)
				robotmouth.say(robotbrain)
				robotmouth.runAndWait()
				print(robotbrain)
				break
				# how are you / okay/ok /who are you/funny story/sad story/
			elif "how are you" in you:
				robotbrain="I'm fine, Thanks"
			elif "okay" in you:
				robotbrain="Okay"
			elif "ok" in you:
				robotbrain="Okay"
			elif "who are you" in you:
				robotbrain="I'm an assistant-who can healp you solve problem"
			elif "funny story" in you:
			    robotbrain="Thinking no one could hear me as I loaded a UPS tractor trailer, I began to whistle. I was really getting into it when a coworker in the next trailer poked his head in. “You know, I always used to wish I could whistle,” he said. “Now I just wish you could.” —Megs Brunne"	
			elif "sad story" in you:
				robotbrain="I became an EMT to save people’s lives.Twenty minutes of CPR on my dad proved that was a lie."
			elif "story" in you:
				robotbrain="One of my wife’s third graders was wearing a Fitbit watch, which prompted my wife to ask, “Are you tracking your steps?” “No,” said the little girl. “I wear this for Mommy so she can show Daddy when he gets home.” —James Avery"
			elif "your name" in you:
				robotbrain="My name is Tele"
			elif "old are you" in you:
			    robotbrain="I don't remember, but I was born in 24,July 2020"
			else:
			    robotbrain=" "

			print('Tele:'+robotbrain)
			#Xu li mang noi
			robotmouth.say(robotbrain)
			robotmouth.runAndWait()

else:
	print("Please try again.")
