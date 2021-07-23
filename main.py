import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
#import wikipedia
#import pyjokes

listener = sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

intro = 'hi i am jeanie'
intro1 = 'how may i help you'
talk(intro)
talk(intro1)

def take_command():
    try:
        with sr.Recognizer(device_index=1) as source:
            print("listening...")
            voice = listener.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if "jeanie" in command():
                print(command)
                talk(command)
    except:
        pass
    return take_command

take_command()

def run_jeanie():
    command = take_command()
    if 'play' in command():
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command():
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    """elif 'who is' in command():
      person = command.replace('who is', '')
      info = wikipedia.summary(person, 2)
      print(info)
      talk(info)
    elif 'joke' in command():
      talk(pyjokes.get_joke())"""
    else:
        talk('i did not understand the command')

while True:
    run_jeanie()
