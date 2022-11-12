import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener=sr.Recognizer()
engine =pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold= 1000
            print('listening...')
            voices=listener.listen(source)
            command=listener.recognize_google(voices)
            command=command.lower()
            if 'Bat' in command:
                command = command.replace('bat','')
                print(command)
    except:
        pass
    return command

def run_bat():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is'+time)
    elif 'who is' or 'what is' in command:
        page = command.replace('who is' or 'what is','')
        info=wikipedia.summary(page,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_bat()