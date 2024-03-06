import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import requests
import time

r = sr.Recognizer() 

def SpeakText():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")

def play_audio(file):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)
    sound.stop() 
    os.remove(file)   

def assistant_speaks(output):
    print("APK:", output)
    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = "audio.mp3"  
    toSpeak.save(file)
    play_audio(file)

def answer(q):
    url = f"https://api.popcat.xyz/chatbot?msg={q}&owner=apk000&botname=APK"
    try:
        response = requests.get(url)
        data = response.json()
        ans = data.get('response')
        return ans
    except requests.exceptions.RequestException as e:
        print("Error fetching data from API:", e)
        return "Sorry, I couldn't fetch a response at the moment."
    except ValueError as e:
        print("Error decoding JSON response from API:", e)
        return "Sorry, I couldn't decode the response from the API."

assistant_speaks("Hello, I am APK. How can I help you today?")
while True:
    time.sleep(3)
    data = SpeakText()
    print("User:", data)
    assistant_speaks(answer(data))