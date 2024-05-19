import speech_recognition as sr
import pyttsx3
import requests
import datetime
import wikipedia

def SpeakText():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User:", query)

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query
 

def assistant_speaks(output):
    print(f"APK: {output}")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(output)
    engine.runAndWait()

def answer(q):
    try:
        response = requests.get(f"https://api.popcat.xyz/chatbot?msg={q}&owner=Ankit&botname=APK").json().get('response')
        return response
    except requests.exceptions.RequestException as e:
        print("Error fetching data from API:", e)
        return "Sorry, I couldn't fetch a response at the moment."
    except ValueError as e:
        print("Error decoding JSON response from API:", e)
        return "Sorry, I couldn't decode the response from the API."

assistant_speaks("Hello, I am APK. How can I help you today?")


if __name__ == '__main__':

    while True:

        query = SpeakText().lower()

        if 'wikipedia' in query:
            try:
                assistant_speaks('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                assistant_speaks("According to Wikipedia")
                print(results)
                assistant_speaks(results)

            except wikipedia.exceptions.DisambiguationError as e:
                assistant_speaks("Several pages matched your query. Here are some options:")
                options = e.options
                for i, option in enumerate(options, start=1):
                    print(f"{i}. {option}")
                assistant_speaks("Please choose a specific option.")
    
                choice = int(SpeakText().lower()) - 1
                if choice >= 0 and choice < len(options):
                    query = options[choice]
                    results = wikipedia.summary(query, sentences=3)
                    assistant_speaks(results)
                else:
                    assistant_speaks("Invalid choice. Please try again.")

            except wikipedia.exceptions.PageError as e:
                assistant_speaks("Sorry, I couldn't find any results for your query.")

            
        elif 'the time' in query:
            print("User:", query)
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            assistant_speaks(f"Sir, the time is {strTime}")

        else:
            assistant_speaks(answer(query))
