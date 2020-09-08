from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wish():
	tim=int(datetime.datetime.now().hour)
	if tim >=0 and tim<12:
		speak("Good Morning sir!")
	elif tim >=12 and tim < 18:
		speak("Good Afternoon sir!")
	else:
		speak("Good Evening sir!")

	speak("I am friday , please tell how may i help you")


def takecommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold=1
		audio=r.listen(source)

	try:
		print("Recognizing...")
		query=r.recognize_google(audio,language='en-in')
		print(f"You Said : {query}\n")

	except Exception as e:
		print("Could not recognize , Please say that again")
		return "None"
	return query			

def closee():
	exit()

def main():
	wish()
	try:
		while True:
			query=takecommand().lower()

			if 'wikipedia' in query:
				speak("Searching wikipedia...")
				query=query.replace("wikipedia","")
				results=wikipedia.summary(query,sentences=2)
				speak("Accoring to wikipedia..")
				print(results)
				speak(results)
			
			elif 'open youtube' in query:
				webbrowser.open("youtube.com")

			elif 'open gmail' in query:
				webbrowser.open("gmail.com")	

			elif 'open linkedin' in query:
				webbrowser.open("linkedin.com")	

			elif 'google' in query:
				webbrowser.open("google.com")

			elif 'quora' in query:
				webbrowser.open("quora.com")

			elif 'github' in query:
				webbrowser.open("github.com")

			elif 'stackoverflow' in query:
				webbrowser.open("stackoverflow.com")

			elif 'the time' in query:
				strTime=datetime.datetime.now().strftime("%H:%M:%S")
				speak(f"sir, the time is {strTime}")			

			elif 'open sublime' in query:
				spath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
				os.startfile(spath)

			elif 'open dev' in query:
				dpath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"	
				os.startfile(dpath)

			elif 'quit' in query:
				exit()
		
	except Exception as e:
		speak("Please try again sir.")

root=Tk()

root.title("F.R.I.D.A.Y")
root.geometry("400x240")
root.minsize(400,240)
root.maxsize(400,240)
root.configure(background="light grey")

Label(root,text="Welcome to Virtual Assistant",font="comicsansms 20 bold",bg="light blue").pack(pady=10)
Button(root,text="Start",command=main,font="comicsansms 15 bold",pady=5).pack(pady=10)
Button(root,text="End",command=closee,font="comicsansms 15 bold",pady=5).pack(pady=10)

root.mainloop()