import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as wb
import os
import sys
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine. getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Hello sir, i am your voice assistant, how can i help you")
print("A moment of silence, please...")

def take_command():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold=10000
            print('Speak Now ....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
            talk("Oops! Didn't catch that ")
    except:
        pass
    return command

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yaswanth.bellala278@gmail.com', 'Yaswanth@2782001')
    server.sendmail('yaswanth.bellala278@gmail.com', to, content)
    server.close()
 
def run_alexa():
    command = take_command()
    print(command)
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'open windows' in command:
            talk('opening windows')
            os.system('explorer C:\\{}'.format(command.replace('open', '')))

    elif 'open outlook' in command:
            talk('opening outlook')
            url = 'outlook.office365.com/mail/inbox'
            wb.open("outlook.com")

    elif 'open facebook' in command:
            talk('opening'+ command)
            url = 'https://www.facebook.com/'
            wb.open("facebook.com")
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
    
    elif 'what is the' and 'who is the 'in command:
        person = command.replace('what is the ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'dinner' in command:
        talk('sorry, I have a headache')
        print('sorry, I have a headache')
    
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        print('I am in a relationship with wifi')
    
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    
    elif 'topic' in command:
        url = 'https://en.wikipedia.org/wiki/'
        with sr.Microphone() as source:
            listener.energy_threshold=10000
            print('search your query')
            voice = listener.listen(source)
            try:
                get = listener.recognize_google(voice)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:
                print("Oops!")
            except sr.RequestError as e:
                print('failed'.format(e))

    elif 'send message' in command:
            send = command.replace('send ', '')
            talk('sending message')
            rem = "Many more happy returns of the day! Hacker"
            pywhatkit.sendwhatmsg_to_group("+91 8639230698", rem, 14, 38)
            
    
    elif 'video' in command:
        url = 'https://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            listener.energy_threshold=10000
            print('search your video')
            voice = listener.listen(source)
            try:
                get = listener.recognize_google(voice)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:
                print("Oops!")
            except sr.RequestError as e:
                print('failed'.format(e))

    elif 'open youtube' in command:
            wb.open("youtube.com")

    elif 'open google' in command:
            wb.open("google.com")

    elif 'open gmr' in command:
            wb.open("gmrit.org") 

    elif 'open files' in command:
            filePath = "D:\\"
            os.startfile(filePath)

    elif 'send email' in command:
            try:
                talk("What should I say?")
                content = take_command()
                to = "yaswanth.bellala278@gmail.com"    
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry my friend. I am not able to send this email")

    elif 'stop' in command:
        talk("Bye sir")
        sys.exit()

    else:
        talk('I could not hear you properly Say that again please...')

while True:
    run_alexa()