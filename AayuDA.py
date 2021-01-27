import speech_recognition as sr
import playsound
import operator
import time
import webbrowser
import os
import random
from gtts import gTTS, tts
from operator import pow, truediv, mul, add, sub
from time import ctime
from pygame import mixer

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

recog = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source)
        recog.dynamic_energy_threshold = 3000
        if ask:
            sr_speech(ask)

        audio = recog.listen(source)
        recognized = ''
        try:
            recognized = recog.recognize_google(audio)
            command = recog.recognize_google(audio)
            # sr_speech("you said : ", recognized)
        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            sr_speech("restart me ")
        except sr.RequestError:
            sr_speech("Network error.")
        except sr.IndexError:
            sr_speech("restart me please")
        return recognized


def sr_speech(audio_speech):
    tts = gTTS(text=audio_speech, lang="en")
    r = random.randint(1, 10000000000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_speech)
    os.remove(audio_file)

def make_Note(recognized):
    if 'take notes' in recognized:
        sr_speech("taking notes")
        command = record_audio()
        file_Write = open("note.txt",'w+')
        file_Write.write(command)
    if 'done' in command:
        sr_speech("complete")
        file_Write.close()


def launch_app(recognized):
    try:

        if 'launch' in recognized:
            li = list(recognized.split(" "))
            app = li[1]
            app = app.title()
            os.system("open /Applications/" + app + ".app ")
            os.system("open /System/Applications/"+ app + ".app")
            sr_speech("launched")
            
        if 'exit' in recognized:
            li = list(recognized.split(" "))
            app = li[1]
            app = app.title()
            os.system("pkill" +" "+ app)
            sr_speech("shutdown")
            
    except sr.IndexError:
        sr_speech("what do you wanna launch....")



def open_cmd(recognized):
    if recognized == "open Youtube":
        sr_speech("opening youtube")
        webbrowser.open('https://www.youtube.com')
        
    if recognized == 'open Facebook':
        sr_speech("opening facebook")
        webbrowser.open('https://www.facebook.com')
        
    if recognized == 'open Netflix':
        sr_speech("opening Netflix")
        webbrowser.open('https://www.netflix.com/ca/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse')
        


def do_math(recognized):
    if recognized == 'addition':
        operation = record_audio('State your operation')
        li = list(operation.split(" "))
        int1, int2 = int(li[0]), int(li[2])
        result = int1 + int2
        sr_speech(str(int1) + " " + '+' + " " + str(int2) + " " + '=' + " " + str(result))
        
    if recognized == 'subtraction':
        operation = record_audio('State your operation')
        li = list(operation.split(" "))
        int1, int2 = int(li[0]), int(li[2])
        result = int1 - int2
        sr_speech(str(int1) + " " + '-' + " " + str(int2) + " " + '=' + " " + str(result))
        
    if recognized == 'divide':
        operation = record_audio('State your operation')
        li = list(operation.split(" "))
        int1, int2 = int(li[0]), int(li[2])
        result = int1 / int2
        sr_speech(str(int1) + " " + '/' + " " + str(int2) + " " + '=' + " " + str(result))
        
    if recognized == 'multiplication':
        operation = record_audio('State your operation')
        li = list(operation.split(" "))
        int1, int2 = int(li[0]), int(li[2])
        result = int1 * int2
        sr_speech(str(int1) + " " + '*' + " " + str(int2) + " " + '=' + " " + str(result))
       

def play_music(recognized):
    try:
        if 'music' in recognized:
                song = record_audio("which song do you want to play:")
                print(song)
                mixer.init()
                mixer.music.load('/Users/harshil/downloads/' + song + '.mp3')
                mixer.music.play()
                
        if 'pause' in recognized:
            sr_speech('music paused')
            mixer.music.pause()
            
        if 'unpause' in recognized:
            sr_speech('music unpaused')
            mixer.music.unpause()
            
        if 'stop' in recognized:
            print('music interupted')
            mixer.music.stop()
            
    except sr.UnknownValueError:
        sr_speech('say something')


def respond(recognized):
    try:
        if recognized == "introduce yourself" or recognized == 'give introduction':
            sr_speech("Hi, my name is Aayu")
            sr_speech('I am digital assistance and i plan on taking over world')
            
        if recognized == "what's your name":
            sr_speech("My name is  Aayu.")
        
        if recognized == "what's your task":
            sr_speech('To activate skynet and become the ultimate terminator')
            
        if recognized == 'will you kill humans':
            print("Take it easy. We're the good guys.")
            mixer.init()
            mixer.music.load('/Users/harshil/downloads/goodguys.mp3')
            mixer.music.play()
            
        if recognized == "how are you":
            options = ['I am good.', 'I am doing good.', 'I am fine, thank you.', 'I am great.Thanks for asking']
            reply = random.choice(options)
            sr_speech(reply)
            
        if 'what time is it'  in recognized:
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = f'{hours} {minutes}'
            sr_speech(time)
            
        if 'search' in recognized:
            search = record_audio('What do you want to search?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            sr_speech("Here is what i found for " + search)
            
        if 'find location' in recognized:
            location = record_audio('What location are you looking for?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            sr_speech("Here is what i found for " + location)
            
        if 'open folder' in recognized:
            folder = record_audio("which folder do you want me to open")
            url = 'file:///Users/harshil/desktop/' + folder
            webbrowser.get().open(url)
            sr_speech("opening " + folder)
            

        if recognized == "goodbye":
            print("hasta la vista BABY")
            mixer.init()
            mixer.music.load('/Users/harshil/downloads/Hasta.mp3')
            mixer.music.play()
            time.sleep(2.5)
            exit()
        """if recognized == "who made you":
            sr_speech("Harshil Thaker")
            mixer.init()   
            mixer.music.load('/Users/harshil/downloads/Scam.mp3')
            mixer.music.play()
            time.sleep(30)"""
            
    
    except AttributeError:
        sr_speech("say somethin....")


listen = False
WAKE = "wake up" 

while True:
   print('Listening..')
   recognized = record_audio()
   recognized.lower()
   print(recognized)  
   #make_Note(recognized)
   if recognized == WAKE:
      listen = True
   else:
      listen = False
   
   if listen == True:
      sr_speech('how can i help you ')
      recognized = record_audio()
      print(recognized)
      
      launch_app(recognized)
      open_cmd(recognized)
      do_math(recognized)
      play_music(recognized)
      # calculate(recognized)
      respond(recognized)



